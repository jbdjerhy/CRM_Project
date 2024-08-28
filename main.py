import datetime
import string
import os
import sys
from datetime import date, timedelta


# Sure! Here is a breakdown of each step into intermediate steps:

# ### Step 1: Define the Requirements
# 1. Determine the attributes for the Lead class: `name`, `state`, `city`, `zip_code`, `date_created`.

# print(date.today())
class Lead:
    def __init__(self, first_name, last_name, state, city, zip, date_created, worked):
        self.first_name = first_name
        self.last_name = last_name
        self.state = state
        self.city = city
        self.zip = zip
        self.date_created = date_created
        self.worked = worked

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.state}, {self.city}, {self.zip}, {self.date_created}, {self.worked}"

    # 2. Identify methods for the Lead class: initialization, string representation, filtering, and follow-up classification.
    def classify(self, date_created, worked):
        age = date.today() - date_created
        if age < 1:
            status = "fresh"
        elif age in range(1, 4) and worked == "no":
            status = "urgent"
        elif age > 3 and worked == "no":
            status = "stale"
        return status


# Initialize dictionary to store leads
leads_dict = {}

# 3. Plan the format for storing leads in the text file.
with open("source_main.txt", 'r+') as source:
    dump = source.read()
    dump_split = dump.split('___')
    raw_leads = [i for i in dump_split if i != ""]
# print(raw_leads[-1])
# print(len(raw_leads))
for lead in raw_leads:
    data = [y for y in lead.splitlines() if y != '' and y != '\n']
    lead_name = data[0]
    first_name = (data[1].split(": "))[1]
    last_name = (data[2].split(": "))[1]
    state = (data[3].split(": "))[1]
    city = (data[4].split(": "))[1]
    zip = (data[5].split(": "))[1]
    date_created = (data[6].split(": "))[1]
    worked = (data[7].split(": "))[1]
    # Create Lead object
    lead_obj = Lead(first_name, last_name, state, city, zip, date_created, worked)

    # Add Lead object to dictionary
    leads_dict[f"{first_name} {last_name}"] = lead_obj


# Function to filter leads by search criteria
def filter_leads(search_criteria, value):
    results = []
    for key, lead in leads_dict.items():
        if getattr(lead, search_criteria) == value:
            results.append(lead)
    return results


# Example usage
search_criteria = input("Search by (e.g., state, city, zip): ")
value = input(f"Enter the {search_criteria} value: ")
filtered_leads = filter_leads(search_criteria, value)

for lead in filtered_leads:
    print(lead)

# #print(len(lines))
# item_list = [i for i in lines if i != '\n']
# #print(item_list)
# #print(len(item_list))
# source.close()

# source = open("source_main.txt", "r+")
# text = ""
# for item in item_list:
#      text += str(item)
#      leads = text.split("___")
# for lead in leads:
#     split = lead.split('\n')
#     print(split)
# # for lead in leads:
# #     data = lead.split("\n")
# #     print(data[0])


# 4. Define criteria for follow-up levels based on lead age.

# ### Step 2: Plan the Program Structure
# 1. **Lead Class**:
#    - Define attributes for the Lead class.
#    - Define methods: `__init__`, `__str__`, and others needed for functionality.

# 2. **File Handling**:
#    - Determine the format for writing leads to the file.
#    - Plan how to read leads from the file.
#    - Ensure proper handling of file operations (open, read, write, close).

# 3. **Filtering Functionality**:
#    - Plan functions to filter leads by name.
#    - Plan functions to filter leads by location (state, city, zip).
#    - Plan functions to filter leads by date created.

# 4. **Follow-Up Classification**:
#    - Define age ranges for each follow-up level (e.g., new, urgent, stale).
#    - Plan a function to calculate the age of a lead.
#    - Plan a function to classify leads based on their age.

# ### Step 3: Implement the Program
# 1. **Create the Lead Class**:
#    - Define the `__init__` method to initialize lead attributes.
#    - Define the `__str__` method for string representation of a lead.
#    - Define additional methods for filtering and follow-up classification.

# 2. **File Handling**:
#    - Write a function to save a lead to the text file.
#    - Write a function to read leads from the text file.
#    - Ensure proper handling of file I/O operations.

# 3. **Filtering Functionality**:
#    - Write functions to filter leads by name.
#    - Write functions to filter leads by state, city, and zip code.
#    - Write functions to filter leads by date created.

# 4. **Follow-Up Classification**:
#    - Write a function to calculate the age of a lead in days.
#    - Write a function to classify leads based on their age into follow-up levels (e.g., new, urgent, stale).

# ### Step 4: Testing and Validation
# 1. **Test Lead Class**:
#    - Create test instances of the Lead class.
#    - Verify the initialization and string representation methods.

# 2. **Test File Handling**:
#    - Test saving leads to the text file.
#    - Test reading leads from the text file.
#    - Validate correct data storage and retrieval.

# 3. **Test Filtering Functionality**:
#    - Test filtering leads by name.
#    - Test filtering leads by state, city, and zip code.
#    - Test filtering leads by date created.
#    - Validate correct filtering results.

# 4. **Test Follow-Up Classification**:
#    - Test the age calculation function.
#    - Test the classification function for follow-up levels.
#    - Validate correct classification of leads.

# ### Step 5: Deployment and Maintenance
# 1. **Deployment**:
#    - Ensure the program runs smoothly in the target environment.
#    - Provide user documentation for using the program.

# 2. **Maintenance**:
#    - Plan for regular updates and bug fixes.
#    - Ensure the program remains functional with future enhancements or changes.
