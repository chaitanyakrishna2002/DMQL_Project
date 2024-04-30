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

# Function to get summary statistics of the data
def get_data_summary(data):
    summary = {}
    for name, df in data.items():
        summary[name] = {
            'Number of Rows': df.shape[0],
            'Number of Columns': df.shape[1],
            'Column Names': df.columns.tolist()
        }
    return summary

# Function to display summary of the data
def display_data_summary(data):
    st.subheader("Data Summary")
    data_summary = get_data_summary(data)
    for name, summary in data_summary.items():
        st.write(f"**{name}**: {summary}")

# Function to save new appointment to CSV file
def save_appointment(appointment_data, csv_file):
    df = pd.read_csv(csv_file)
    df = df.append(appointment_data, ignore_index=True)
    df.to_csv(csv_file, index=False)

# Function to display appointment status
def display_appointment_status(appointment_id, csv_file):
    df = pd.read_csv(csv_file)
    appointment = df[df['Appointment ID'] == appointment_id]
    if not appointment.empty:
        st.write("Appointment Status:")
        st.write(appointment)
    else:
        st.error("Appointment not found.")

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
st.title('Quarry Crafters')

# Sidebar navigation
selected_page = st.sidebar.selectbox("Select Page", ["Quarry Crafters", "Schedule Appointment"] + list(data.keys()))

# Conditionally display dashboard data
if selected_page == "Quarry Crafters":
    display_data_summary(data)
elif selected_page == "Schedule Appointment":
    schedule_appointment(data, csv_files[8])  # Index 8 corresponds to 'service_appointments.csv'
else:
    st.title(selected_page)
    st.write(data[selected_page])
