import streamlit as st
import pandas as pd
import os
from datetime import datetime

# Function to fetch data from CSV files
def fetch_data(csv_files):
    data = {}
    for file in csv_files:
        if os.path.exists(file):  # Check if file exists
            data[os.path.basename(file)] = pd.read_csv(file)
        else:
            st.error(f"File not found: {file}")
    return data

# Function to display summary of the data
def display_data_summary(data):
    st.subheader("Data Summary")
    for name, df in data.items():
        display_name = name.replace(".csv", "").replace("_", " ").title()
        st.write(f"**{display_name}**: {df.columns.tolist()}")

# Function to save new appointment to CSV file
def save_appointment(appointment_data, csv_file):
    df = pd.read_csv(csv_file)
    df = df.append(appointment_data, ignore_index=True)
    df.to_csv(csv_file, index=False)

# Function to display page for scheduling appointments
def schedule_appointment(data, csv_file):
    st.title("Schedule Appointment")
    st.write("Please fill in the details to schedule a new appointment.")
    appointment_id = st.text_input("Appointment ID")
    customer_id = st.text_input("Customer ID")
    date = st.date_input("Date", min_value=datetime.now())
    time = st.time_input("Time")
    service_type = st.selectbox("Service Type", ["Repair", "Maintenance", "Consultation"])
    appointment_data = {'Appointment ID': appointment_id, 'Customer ID': customer_id, 'Date': date, 'Time': time, 'Service Type': service_type}
    if st.button("Schedule Appointment"):
        save_appointment(appointment_data, csv_file)
        st.success("Appointment scheduled successfully!")

# Function to search for specific records
def search_records(data, search_query):
    search_results = {}
    for name, df in data.items():
        search_results[name] = df[df.apply(lambda row: any(search_query.lower() in str(val).lower() for val in row), axis=1)]
    return search_results

# Function to filter data based on criteria
def filter_data(data, filter_criteria):
    filtered_results = {}
    for name, df in data.items():
        filtered_results[name] = df.query(filter_criteria)
    return filtered_results

# Function to perform analytics on the data
def perform_analytics(data):
    st.title("Analytics")
    st.write("Performing analytics on the data...")
    # Add your analytics code here

# Function to add new records
def add_record(data, csv_file):
    st.title("Add New Record")
    st.write("Please fill in the details for the new record:")
    new_record_data = {}
    for col in data.columns:
        new_record_data[col] = st.text_input(col)
    if st.button("Add Record"):
        df = pd.read_csv(csv_file)
        df = df.append(new_record_data, ignore_index=True)
        df.to_csv(csv_file, index=False)
        st.success("Record added successfully!")

# Function to modify existing records
def modify_record(data, csv_file):
    st.title("Modify Record")
    st.write("Please select the record to modify:")
    selected_record_index = st.selectbox("Select Record", data.index)
    modified_record_data = {}
    for col in data.columns:
        modified_record_data[col] = st.text_input(col, value=data.loc[selected_record_index, col])
    if st.button("Modify Record"):
        df = pd.read_csv(csv_file)
        df.loc[selected_record_index] = modified_record_data
        df.to_csv(csv_file, index=False)
        st.success("Record modified successfully!")

# Function to delete records
def delete_record(data, csv_file):
    st.title("Delete Record")
    st.write("Please select the record to delete:")
    selected_record_index = st.selectbox("Select Record", data.index)
    if st.button("Delete Record"):
        df = pd.read_csv(csv_file)
        df.drop(selected_record_index, inplace=True)
        df.to_csv(csv_file, index=False)
        st.success("Record deleted successfully!")

# Set background color and text color
def set_background(color):
    if color:
        st.markdown(f"""<style>
                        .reportview-container {{
                            background-color: {color};
                            color: white;
                        }}
                        </style>""", unsafe_allow_html=True)

# List of paths to your CSV files
csv_files = [
    r'Customers.csv',
    r'Parts.csv',
    r'Sales.csv',
    r'Salespersons.csv',
    r'car_models.csv',
    r'customer_feedback.csv',
    r'design_improvements.csv',
    r'inventory.csv',
    r'service_appointments.csv',
    r'service_technicians.csv'
]

# Fetch data from CSV files
data = fetch_data(csv_files)

# Set background color
set_background("black")  # Set background color to black

# Streamlit app
st.title('Query Crafters')

# Welcome message
st.write("Welcome to Query Crafters! This is the home page.")

# Display summary of the data
display_data_summary(data)

# Sidebar navigation
selected_page = st.sidebar.selectbox("Select Page", ["Home", "Schedule Appointment", "Search Records", "Filter Data", "Analytics", "Add New Record", "Modify Record", "Delete Record"])

# Conditionally display dashboard data
if selected_page == "Schedule Appointment":
    schedule_appointment(data, csv_files[8])  # Index 8 corresponds to 'service_appointments.csv'
elif selected_page == "Search Records":
    search_query = st.sidebar.text_input("Enter Search Query")
    if search_query:
        search_results = search_records(data, search_query)
        st.write(search_results)
    else:
        st.info("Please enter a search query.")
elif selected_page == "Filter Data":
    filter_criteria = st.sidebar.text_input("Enter Filter Criteria")
    if filter_criteria:
        filtered_results = filter_data(data, filter_criteria)
        st.write(filtered_results)
    else:
        st.info("Please enter filter criteria.")
elif selected_page == "Analytics":
    perform_analytics(data)
elif selected_page == "Add New Record":
    add_record(data, csv_files[0])  # Index 0 corresponds to 'Customers.csv'
elif selected_page == "Modify Record":
    modify_record(data, csv_files[0])  # Index 0 corresponds to 'Customers.csv'
elif selected_page == "Delete Record":
    delete_record(data, csv_files[0])  # Index 0 corresponds to 'Customers.csv'
