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
selected_page = st.sidebar.selectbox("Select Page", ["Home"] + [name.replace(".csv", "").title() for name in data.keys()])

# Conditionally display dashboard data
if selected_page == "Home":
    pass  # Home page content already displayed
else:
    st.title(selected_page)
    search_query = st.sidebar.text_input("Search")
    if search_query:
        st.write(data[selected_page.lower().replace(" ", "_") + ".csv"].query(f"{search_query} in {data[selected_page.lower().replace(" ", "_") + '.csv'].columns.tolist()}"))
    else:
        st.write(data[selected_page.lower().replace(" ", "_") + ".csv"])
