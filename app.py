import streamlit as st
import pandas as pd
import os

# Function to fetch data from CSV files
def fetch_data(csv_files):
    data = {}
    for file in csv_files:
        data[os.path.basename(file)] = pd.read_csv(file)
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

# Function to display appointment status
def display_appointment_status(appointment_id, csv_file):
    appointment = search_appointment_by_id(appointment_id, csv_file)
    if appointment is not None:
        st.write("Appointment Status:")
        st.write(appointment)
    else:
        st.error("Appointment not found.")

# Function to display summary of the data
def display_data_summary(data):
    st.subheader("Data Summary")
    data_summary = get_data_summary(data)
    for name, summary in data_summary.items():
        st.write(f"**{name}**: {summary}")

# Set background color
set_background("black")  # Set background color to black

# Streamlit app
st.title('Quarry Crafters')

# Display Quarry Crafters content
st.write("Welcome to Quarry Crafters! This is the Quarry Crafters page content.")

# Display summary of the data
display_data_summary(data)

# Sidebar navigation
selected_page = st.sidebar.selectbox("Select Page", ["Quarry Crafters"] + list(data.keys()))

# Conditionally display dashboard data
if selected_page != "Quarry Crafters":
    st.title(selected_page)
    st.write(data[selected_page])
