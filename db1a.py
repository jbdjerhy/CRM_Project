import csv
from datetime import datetime
from pythonProject.Instructions.Flask_Import import app, db, Lead, Agent

csv_file_path = 'cleaned_leads.csv'
csv_agent_path = 'Agents.csv'


def import_csv_to_db(file_path, model_class, column_mapping):
    with app.app_context():
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)

            # Prepare a list to hold the lead objects for batch insert
            objects_to_add = []

            for row in reader:
                # Debugging statements
                print("Row data:", row)

                # Map CSV columns to model fields:
                data = {key: row.get(value, '').strip() for key, value in column_mapping.items()}

                # Convert date_created to date object
                if 'date_created' in data:
                    try:
                        date_created = datetime.strptime(data['date_created'], '%Y-%m-%d').date()
                    except ValueError:
                        date_created = None

                # Convert worked to boolean
                if 'worked' in data:
                    data['worked'].lower() in ['true', '1', 'yes']

                obj = model_class(**data)
                objects_to_add.append(obj)

                # Commit in batches of 1000 to optimize performance
                if len(object_to_add) >= 1000:
                    try:
                        db.session.bulk_save_objects(objects_to_add)
                        db.session.commit()
                        object_to_add = []  # Reset the list after committing
                    except Exception as e:
                        print(f"Error during batch commit: {e}")
                        db.session.rollback()

            # Commit any remaining leads not yet committed
            if object_to_add:
                try:
                    db.session.bulk_save_objects(object_to_add)
                    db.session.commit()
                except Exception as e:
                    print(f"Error during final batch commit: {e}")
                    db.session.rollback()


if __name__ == "__main__":
    # Import leads
    import_csv_to_db(csv_file_path, Lead, {
        'first_name': 'First Name',
        'last_name': 'Last Name',
        'state': 'State',
        'city': 'City',
        'zip_code': 'ZIP',
        'date_created': 'Date Created',
        'worked': 'Worked'
    })

    # Import agents
    import_csv_to_db(csv_agent_path, Agent, {
        'agent_id': 'Agent ID',
        'first_name': 'First Name',
        'last_name': 'Last Name',
        'location': 'Agent Location',
        'score': 'Agent Score'
    })
