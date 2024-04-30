import streamlit as st
import pandas as pd
import os

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

# Function to save new appointment to CSV file
def save_appointment(appointment_data, csv_file):
    df = pd.read_csv(csv_file)
    df = df.append(appointment_data, ignore_index=True)
    df.to_csv(csv_file, index=False)

# Function to count appointments for a specific date
def count_appointments_for_date(date, csv_file):
    df = pd.read_csv(csv_file)
    return df[df['Date'] == date.strftime('%Y-%m-%d')].shape[0]

# Function to search for appointment status by ID
def search_appointment_by_id(appointment_id, csv_file):
    df = pd.read_csv(csv_file)
    appointment = df[df['Appointment ID'] == appointment_id]
    return appointment if not appointment.empty else None

# Function to display appointment status
def display_appointment_status(appointment_id, csv_file):
    appointment = search_appointment_by_id(appointment_id, csv_file)
    if appointment is not None:
        st.write("Appointment Status:")
        st.write(appointment)
    else:
        st.error("Appointment not found.")

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
    r'Ccustomer_feedback.csv',
    r'design_improvements.csv',
    r'inventory.csv',
    r'service_appointments.csv',
    r'service_technicians.csv'
]

# Fetch data from CSV files
data = fetch_data(csv_files)

# Function to display summary of the data
def display_data_summary(data):
    st.subheader("Data Summary")
    data_summary = get_data_summary(data)
    for name, summary in data_summary.items():
        st.write(f"**{name}**: {summary}")

# Function to schedule a new appointment
def schedule_appointment():
    st.subheader("Schedule New Appointment")
    appointment_data = {}
    appointment_data['Date'] = st.date_input("Select Date")
    appointment_data['Time'] = st.time_input("Select Time")
    appointment_data['Customer ID'] = st.text_input("Customer ID")
    appointment_data['Service Type'] = st.selectbox("Service Type", ['Repair', 'Maintenance', 'Other'])
    appointment_data['Appointment ID'] = st.text_input("Appointment ID")
    
    if st.button("Schedule Appointment"):
        save_appointment(appointment_data, csv_files[8])
        st.success("Appointment scheduled successfully!")

# Function to check appointment status
def check_appointment_status():
    st.subheader("Check Appointment Status")
    appointment_id = st.text_input("Enter Appointment ID")
    
    if st.button("Check Status"):
        display_appointment_status(appointment_id, csv_files[8])

# Set background color
set_background("black")  # Set background color to black

# Streamlit app
st.title('Quarry Crafters')

# Display Quarry Crafters content
st.write("Welcome to Quarry Crafters! This is the Quarry Crafters page content.")

# Display summary of the data
display_data_summary(data)

# Sidebar navigation
selected_page = st.sidebar.selectbox("Select Page", ["Quarry Crafters", "Schedule Appointment", "Check Appointment Status"])

# Conditionally display dashboard data
if selected_page == "Schedule Appointment":
    schedule_appointment()
elif selected_page == "Check Appointment Status":
    check_appointment_status()
else:
    st.title(selected_page)
    st.write(data[selected_page])
