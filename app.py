import streamlit as st
import pandas as pd
import os
import random

# Function to fetch data from CSV files
def fetch_data(csv_files):
    data = {}
    for file in csv_files:
        if os.path.exists(file):  # Check if file exists
            data[os.path.basename(file).replace('.csv', '')] = pd.read_csv(file)
        else:
            st.error(f"File not found: {file}")
    return data

# Function to get summary statistics of the data
def get_data_summary(data):
    summary = {}
    for name, df in data.items():
        summary[name] = df.columns.tolist()
    return summary

# Function to display summary of the data
def display_data_summary(data):
    st.subheader("Data Summary")
    data_summary = get_data_summary(data)
    for name, columns in data_summary.items():
        st.write(f"**{name} Columns**: {columns}")

# Set background color and text color
def set_background(color):
    if color:
        st.markdown(f"""<style>
                        .reportview-container {{
                            background-color: {color};
                            color: white;
                        }}
                        </style>""", unsafe_allow_html=True)

# Function to generate a random 4-digit appointment ID
def generate_appointment_id():
    return random.randint(1000, 9999)

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

# Sidebar navigation
selected_page = st.sidebar.selectbox("Select Page", ["Home", "Schedule Appointment"] + list(data.keys()))

# Display summary on the home page
if selected_page == "Home":
    st.subheader("Home Page")
    st.write("Welcome to Query Crafters! This is the Home Page content.")
    display_data_summary(data)
elif selected_page == "Schedule Appointment":
    st.subheader("Schedule Appointment")
    customer_name = st.text_input("Customer Name")
    address = st.text_area("Address")
    required_service = st.text_input("Required Service")
    
    if st.button("Submit"):
        # Generate a 4-digit appointment ID
        appointment_id = generate_appointment_id()
        st.success(f"Appointment scheduled successfully! Appointment ID: {appointment_id:04}")
else:
    st.title(selected_page)
    st.write(data[selected_page])
