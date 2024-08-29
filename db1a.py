import csv
from Flask_Import import app, db, Lead
from datetime import datetime

csv_file_path = 'leads_data.csv'


def import_csv_to_db(file_path):
    with app.app_context():
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                # Debugging statements
                print("Row data:", row)
                print("Type of 'First Name':", type(row['First Name']))

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

                db.session.add(lead)
                db.session.commit()


import_csv_to_db('leads_data.csv')
