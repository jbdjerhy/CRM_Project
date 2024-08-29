from datetime import date
from Flask_Import import Lead

from datetime import datetime, date
from Flask_Import import app, db, Lead


def classify(date_created, worked):
    # Calculate the age of the lead
    age = (date.today() - date_created).days // 365  # Age in years

    # Determine the status based on the age and worked status
    if age < 1:
        status = "fresh"
    elif 1 <= age < 4 and not worked:
        status = "urgent"
    elif age >= 3 and not worked:
        status = "stale"
    else:
        status = "unknown"  # Fallback status
    return status


def get_lead_status(first_name, last_name):
    with app.app_context():
        # Query the database for the lead with the given names
        lead = Lead.query.filter_by(first_name=first_name, last_name=last_name).first()

        if lead:
            # If lead exists, classify based on date_created and worked
            date_created = lead.date_created
            worked = lead.worked
            status = classify(date_created, worked)
            return status
        else:
            return "Lead not found"


if __name__ == "__main__":
    # Example usage
    first_name = 'Megan'
    last_name = 'Chang'
    status = get_lead_status(first_name, last_name)
    print(f"Lead Status: {status}")


# def leads_from_txt(txt_name):
#     # 3. Plan the format for storing leads in the text file.
#     with open(txt_name, 'r+') as source:
#         dump = source.read()
#         dump_split = dump.split('___')
#         raw_leads = [i for i in dump_split if i != ""]
#     # print(raw_leads[-1])
#     # print(len(raw_leads))
#     for lead in raw_leads:
#         data = [y for y in lead.splitlines() if y != '' and y != '\n']
#         lead_name = data[0]
#         first_name = (data[1].split(": "))[1]
#         last_name = (data[2].split(": "))[1]
#         state = (data[3].split(": "))[1]
#         city = (data[4].split(": "))[1]
#         ZIP = (data[5].split(": "))[1]
#         date_created = (data[6].split(": "))[1]
#         worked = (data[7].split(": "))[1]
#         # Create Lead object
#         lead_obj = Lead(first_name, last_name, state, city, zip, date_created, worked)

    # Create Lead object


# Function to filter leads by search criteria
def filter_leads(search_criteria, value, leads_dict=None):
    results = []
    for key, lead in leads_dict.items():
        if getattr(lead, search_criteria) == value:
            results.append(lead)
    return results
