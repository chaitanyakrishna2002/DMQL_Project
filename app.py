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

# Function to display summary of the data
def display_data_summary(data):
    st.subheader("Data Summary")
    data_summary = get_data_summary(data)
    for name, summary in data_summary.items():
        st.write(f"**{name}**: {summary}")

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
