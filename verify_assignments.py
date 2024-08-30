from app_setup import app
from assignments import verify_lead_assignments, verify_leads_per_agent

if __name__ == "__main__":
    with app.app_context():
        verify_lead_assignments()
        verify_leads_per_agent()
