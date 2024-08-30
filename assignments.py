from app_setup import db
from Flask_App import Lead, Agent
import random


def assign_leads_to_agents():
    with db.session.no_autoflush:
        all_leads = Lead.query.all()
        all_agents = Agent.query.all()

        if len(all_leads) < 50:
            print("Not enough leads available.")
            return

        if len(all_agents) < 10:
            print("Not enough agents available.")
            return

        selected_leads = random.sample(all_leads, 50)
        random.shuffle(all_agents)

        for i, lead in enumerate(selected_leads):
            agent = all_agents[i % len(all_agents)]
            lead.agent_id = agent.agent_id

        try:
            db.session.commit()
            print("Leads successfully assigned to agents.")
        except Exception as e:
            db.session.rollback()
            print(f"Error during assignment: {e}")


def verify_lead_assignments():
    with db.session.no_autoflush:
        leads = Lead.query.all()
        unassigned_leads = [lead for lead in leads if not lead.agent_id]

        if unassigned_leads:
            print(f"Unassigned Leads: {len(unassigned_leads)}")
            for lead in unassigned_leads:
                print(f"Lead ID: {lead.id} - No Agent Assigned")
        else:
            print("All leads are assigned to an agent.")


def verify_leads_per_agent():
    with db.session.no_autoflush:
        agents = Agent.query.all()
        lead_counts = {agent.agent_id: 0 for agent in agents}

        leads = Lead.query.all()
        for lead in leads:
            if lead.agent_id in lead_counts:
                lead_counts[lead.agent_id] += 1

        for agent in agents:
            print(f"Agent ID: {agent.agent_id}, Leads Assigned: {lead_counts[agent.agent_id]}")
