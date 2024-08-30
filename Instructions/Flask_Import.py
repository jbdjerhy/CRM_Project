import csv
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# Set up the database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///leads.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database

db = SQLAlchemy(app)


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


# Route to display lead information
@app.route('/leads')
def display_leads():
    # Query all leads from the database
    leads = Lead.query.all()
    return render_template('leads.html', leads=leads)


# Route to display lead information
@app.route('/agents')
def display_leads():
    # Query all leads from the database
    agents = Agent.query.all()
    return render_template('agents.html', agents=agents)


if __name__ == '__main__':
    app.run(debug=True)
