# Lead Classification System

## Project Overview

**Title:** Lead Classification System

**Description:** The Lead Classification System is designed to manage and classify leads based on their creation date and work status. This system involves cleaning and importing lead data from CSV files into a database, classifying the leads based on specific criteria, and managing lead assignments to agents.

## Objectives

1. **Data Cleaning and Import**: 
   - Clean lead and agent data by handling missing values.
   - Import cleaned data into a database.

2. **Lead Classification**:
   - Classify leads into categories such as "fresh," "urgent," or "stale" based on their age and work status.
   - Provide functionality to look up leads by name and return their classification status.

3. **Lead Assignment**:
   - Assign leads to agents ensuring an even distribution.
   - Verify that all leads have been assigned and report on the number of leads per agent.

## Tools and Technologies

- **Programming Languages**: Python
- **Libraries and Frameworks**:
  - `pandas`: Data manipulation and cleaning.
  - `sqlalchemy`: Database ORM.
  - `Flask`: Web framework for application context.
  - `pyarrow`: Handling data types in `pandas`.
- **Database**: SQLite (with the option to adapt to other databases such as PostgreSQL or MySQL).

## Project Structure

1. **Data Cleaning and Import**:
   - **`cleaning_csv.py`**: Handles data cleaning and CSV import into the database.
   - **`app_setup.py`**: Sets up Flask and SQLAlchemy, initializes the database, and imports models and functions.
   - **`Flask_App.py`**: Defines the database models and routes, imports CSV data, and runs the application.

2. **Lead Classification**:
   - **`classify_lead.py`**: Defines functions to classify leads and look up leads by name.

3. **Lead Assignment and Verification**:
   - **`assignments.py`**: Handles assigning leads to agents, verifies lead assignments, and reports the number of leads per agent.
   - **`verify_assignments.py`**: Script for verifying lead assignments and the distribution of leads among agents.

## Detailed Implementation

### 1. Data Cleaning and Import

**File:** `cleaning_csv.py`

**Functionality:**
- **Read CSV File**: Load data from CSV files for leads and agents.
- **Clean Data**: Handle missing values and ensure data integrity.
- **Import Data**: Insert data into the database in batches to optimize performance.

### 2. Lead Classification

**File:** `classify_lead.py`

**Functionality:**
- **Classify Leads**: Classify leads based on age (e.g., fresh, urgent, stale) and work status.
- **Lookup Functionality**: Provide the ability to look up leads by name and return their classification status.

### 3. Lead Assignment and Verification

**File:** `assignments.py`

**Functionality:**
- **Assign Leads to Agents**: Randomly assign leads to agents, ensuring that each agent receives a fair distribution of leads.
- **Verify Lead Assignments**: Check if all leads have been assigned and report any unassigned leads.
- **Verify Leads Per Agent**: Report the number of leads assigned to each agent.

**File:** `verify_assignments.py`

**Functionality:**
- **Verify Lead Assignments**: Use this script to run verification checks to ensure that the assignment logic is functioning correctly.

## Errors and Workarounds

### 1. Circular Import Errors

**Issue**:
Circular import errors due to dependencies between modules.

**Solution**:
- Reorganized imports to avoid circular dependencies by importing functions and models within specific contexts.

### 2. SQLAlchemy Column Definition Errors

**Issue**:
Incorrect column definitions in SQLAlchemy.

**Solution**:
- Corrected the column definition syntax and ensured proper usage of `db.Column` with appropriate parameters.

### 3. Assignment Logic Issues

**Issue**:
Errors in lead assignment or handling logic.

**Solution**:
- Added validation checks for the number of leads and agents.
- Implemented random sampling and shuffling for fair distribution.

## Lessons Learned

- **Flask and SQLAlchemy**: Gained experience in setting up and configuring a Flask application with SQLAlchemy for ORM.
- **CSV Handling**: Improved skills in importing and cleaning data from CSV files.
- **Managing Circular Imports**: Learned to handle circular imports by restructuring code.
- **Error Handling**: Developed better error handling and debugging techniques.
- **Batch Processing**: Implemented efficient batch processing for large datasets.

## Conclusion

This project highlights proficiency in developing a CRM system with Flask and SQLAlchemy, including data management, classification, and assignment. The documentation reflects practical problem-solving skills and effective use of Python programming techniques.
