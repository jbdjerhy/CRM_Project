from datetime import date
from Flask_Import import Lead


def classify(self, date_created, worked):
    age = date.today() - date_created
    if age < 1:
        status = "fresh"
    elif age in range(1, 4) and worked == "no":
        status = "urgent"
    elif age > 3 and worked == "no":
        status = "stale"
    return status


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
