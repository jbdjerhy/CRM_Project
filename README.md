# Lead Classification System

## Project Overview

**Title:** Lead Classification System

**Description:** The Lead Classification System is designed to classify leads based on their creation date and work status. This system involves cleaning and importing lead data from a CSV file into a database and classifying the leads based on specific criteria.

## Objectives

1. **Data Cleaning and Import**: 
   - Clean lead data by handling missing values.
   - Import cleaned data into a database.
   
2. **Lead Classification**:
   - Classify leads into categories such as "fresh," "urgent," or "stale" based on their age and work status.
   - Provide functionality to look up leads by name and return their classification status.

## Tools and Technologies

- **Programming Languages**: Python
- **Libraries and Frameworks**:
  - `pandas`: Data manipulation and cleaning.
  - `sqlalchemy`: Database ORM.
  - `Flask`: Web framework for application context.
  - `pyarrow`: Handling data types in `pandas`.
- **Database**: SQLite (as an example; can be adapted for other databases such as PostgreSQL or MySQL).

## Project Structure

1. **Data Cleaning and Import Script**:
   - `cleaning_csv.py`: Handles data cleaning and CSV import into the database.

2. **Lead Classification Script**:
   - `classify_lead.py`: Defines functions to classify leads and lookup by name.

## Detailed Implementation

### 1. Data Cleaning and Import

**File:** `cleaning_csv.py`

**Functionality:**

- **Read CSV File**: Load data from a CSV file.
- **Clean Data**: Handle missing values and ensure data integrity.
- **Import Data**: Insert data into the database in batches for efficiency.

**Code:**
```python
import csv
from datetime import datetime
from Flask_Import import app, db, Lead

csv_file_path = 'cleaned_leads.csv'

def import_csv_to_db(file_path):
    with app.app_context():
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            leads_to_add = []
            
            for row in reader:
                # Data parsing
                first_name = row['First Name'].strip() if row['First Name'] else None
                last_name = row['Last Name'].strip() if row['Last Name'] else None
                state = row['State'].strip() if row['State'] else None
                city = row['City'].strip() if row['City'] else None
                zip_code = row['ZIP'].strip() if row['ZIP'] else None
                date_created_str = row['Date Created'].strip()
                worked_str = row['Worked'].strip().lower()

                # Convert date_created to date object
                try:
                    date_created = datetime.strptime(date_created_str, '%Y-%m-%d').date()
                except ValueError:
                    date_created = None

                # Convert worked to boolean
                worked = worked_str in ['true', '1', 'yes']

                # Create a new Lead object
                lead = Lead(
                    first_name=first_name,
                    last_name=last_name,
                    state=state,
                    city=city,
                    zip_code=zip_code,
                    date_created=date_created,
                    worked=worked
                )

                leads_to_add.append(lead)

                # Commit in batches of 1000
                if len(leads_to_add) >= 1000:
                    try:
                        db.session.bulk_save_objects(leads_to_add)
                        db.session.commit()
                        leads_to_add = []
                    except Exception as e:
                        print(f"Error during batch commit: {e}")
                        db.session.rollback()
        
            if leads_to_add:
                try:
                    db.session.bulk_save_objects(leads_to_add)
                    db.session.commit()
                except Exception as e:
                    print(f"Error during final batch commit: {e}")
                    db.session.rollback()

if __name__ == "__main__":
    import_csv_to_db(csv_file_path)
