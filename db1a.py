import csv
from datetime import datetime
from Flask_Import import app, db, Lead

csv_file_path = 'cleaned_leads.csv'
csv_agent_path = ''

def import_csv_to_db(file_path):
    with app.app_context():
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)

            # Prepare a list to hold the lead objects for batch insert
            leads_to_add = []

            for row in reader:
                # Debugging statements
                print("Row data:", row)

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

                # Print debug info
                print(f"Parsed Lead: {first_name}, {last_name}, {state}, {city}, {zip_code}, {date_created}, {worked}")

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

                # Add the lead to the list
                leads_to_add.append(lead)

                # Commit in batches of 1000 to optimize performance
                if len(leads_to_add) >= 1000:
                    try:
                        db.session.bulk_save_objects(leads_to_add)
                        db.session.commit()
                        leads_to_add = []  # Reset the list after committing
                    except Exception as e:
                        print(f"Error during batch commit: {e}")
                        db.session.rollback()

            # Commit any remaining leads not yet committed
            if leads_to_add:
                try:
                    db.session.bulk_save_objects(leads_to_add)
                    db.session.commit()
                except Exception as e:
                    print(f"Error during final batch commit: {e}")
                    db.session.rollback()


if __name__ == "__main__":
    import_csv_to_db(csv_file_path)
