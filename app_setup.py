from app_setup import app, db
from flask import render_template
import csv
from datetime import datetime


# Define the Lead model
class Lead(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    state = db.Column(db.String(50), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    zip_code = db.Column(db.String(20), nullable=False)
    date_created = db.Column(db.Date, nullable=False)
    worked = db.Column(db.Boolean, nullable=False)


# Define the Agent model
class Agent(db.Model):
    agent_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    location = db.Column(db.String(50), nullable=False)
    score = db.Column(db.Float)


csv_file_path_leads = 'cleaned_leads.csv'
csv_file_path_agents = 'Agents.csv'


def import_csv_to_db(file_path, model_class, column_mapping):
    with app.app_context():
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            objects_to_add = []
            for row in reader:
                data = {key: row.get(value, '').strip() for key, value in column_mapping.items()}
                if 'date_created' in data:
                    try:
                        data['date_created'] = datetime.strptime(data['date_created'], '%Y-%m-%d').date()
                    except ValueError:
                        data['date_created'] = None
                if 'worked' in data:
                    data['worked'] = data['worked'].lower() in ['true', '1', 'yes']
                obj = model_class(**data)
                objects_to_add.append(obj)
                if len(objects_to_add) >= 1000:
                    try:
                        db.session.bulk_save_objects(objects_to_add)
                        db.session.commit()
                        objects_to_add = []
                    except Exception as e:
                        print(f"Error during batch commit: {e}")
                        db.session.rollback()
            if objects_to_add:
                try:
                    db.session.bulk_save_objects(objects_to_add)
                    db.session.commit()
                except Exception as e:
                    print(f"Error during final batch commit: {e}")
                    db.session.rollback()


@app.route('/leads')
def show_leads():
    leads = Lead.query.all()
    return render_template('leads.html', leads=leads)


@app.route('/agents')
def show_agents():
    agents = Agent.query.all()
    return render_template('agents.html', agents=agents)


if __name__ == "__main__":
    from assignments import assign_leads_to_agents, verify_lead_assignments, verify_leads_per_agent

    import_csv_to_db(csv_file_path_leads, Lead, {
        'first_name': 'First Name',
        'last_name': 'Last Name',
        'state': 'State',
        'city': 'City',
        'zip_code': 'ZIP',
        'date_created': 'Date Created',
        'worked': 'Worked'
    })
    import_csv_to_db(csv_file_path_agents, Agent, {
        'agent_id': 'Agent ID',
        'first_name': 'First Name',
        'last_name': 'Last Name',
        'location': 'Agent Location',
        'score': 'Agent Score'
    })
    assign_leads_to_agents()
    verify_lead_assignments()
    verify_leads_per_agent()
    app.run(debug=True)
