import streamlit as st
import pandas as pd
from datetime import datetime

# Function to fetch data from CSV files
def fetch_data(csv_files):
    data = {}
    for file in csv_files:
        if st.sidebar.checkbox(f"Load {file}", True):  # Checkbox to optionally load data
            if st.sidebar.button(f"Refresh {file}"):  # Button to refresh data
                data[os.path.basename(file)] = pd.read_csv(file)
        else:
            data.pop(os.path.basename(file), None)  # Remove data if checkbox is unchecked
    return data

# Function to search for records
def search_records(data):
    st.sidebar.subheader("Search")
    search_term = st.sidebar.text_input("Enter search term:")
    search_results = {}
    for name, df in data.items():
        search_results[name] = df[df.apply(lambda row: row.astype(str).str.contains(search_term, case=False).any(), axis=1)]
    return search_results

# Function to filter records
def filter_records(data):
    st.sidebar.subheader("Filter")
    filtered_data = {}
    for name, df in data.items():
        # Example: filter sales by date range
        if name.lower() == "sales.csv":
            st.sidebar.write("Filter sales by date range:")
            start_date = st.sidebar.date_input("Start Date", min_value=datetime.now())
            end_date = st.sidebar.date_input("End Date", min_value=start_date)
            filtered_data[name] = df[(df['Date'] >= start_date) & (df['Date'] <= end_date)]
        # Add more filters as needed
    return filtered_data

# Function to perform analytics
def perform_analytics(data):
    st.sidebar.subheader("Analytics")
    # Example: generate sales report
    if "Sales.csv" in data:
        st.sidebar.write("Generate Sales Report:")
        sales_data = data["Sales.csv"]
        sales_report = sales_data.groupby("Product").sum()["Revenue"]
        st.sidebar.write(sales_report)

# Function to add new records
def add_record(data):
    st.sidebar.subheader("Add New Record")
    # Example: add new customer
    if "Customers.csv" in data:
        st.sidebar.write("Add New Customer:")
        new_customer_name = st.sidebar.text_input("Customer Name")
        # Add more fields as needed
        if st.sidebar.button("Add Customer"):
            new_customer = {"Name": new_customer_name}  # Construct new customer data
            data["Customers.csv"] = data["Customers.csv"].append(new_customer, ignore_index=True)
            st.sidebar.success("New customer added successfully!")

# Function to modify existing records
def modify_record(data):
    st.sidebar.subheader("Modify Record")
    # Example: modify customer details
    if "Customers.csv" in data:
        st.sidebar.write("Modify Customer Details:")
        customer_name = st.sidebar.text_input("Enter Customer Name to Modify")
        # Add more fields as needed
        modified_customer_name = st.sidebar.text_input("Modified Customer Name")
        if st.sidebar.button("Modify Customer"):
            data["Customers.csv"].loc[data["Customers.csv"]["Name"] == customer_name, "Name"] = modified_customer_name
            st.sidebar.success("Customer details modified successfully!")

# Function to delete records
def delete_record(data):
    st.sidebar.subheader("Delete Record")
    # Example: delete customer
    if "Customers.csv" in data:
        st.sidebar.write("Delete Customer:")
        customer_name = st.sidebar.text_input("Enter Customer Name to Delete")
        if st.sidebar.button("Delete Customer"):
            data["Customers.csv"] = data["Customers.csv"].loc[data["Customers.csv"]["Name"] != customer_name]
            st.sidebar.success("Customer deleted successfully!")

# Set up Streamlit app
st.title("Query Crafters")
st.sidebar.title("Options")

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

# Sidebar operations
if data:
    search_results = search_records(data)
    filtered_data = filter_records(data)
    perform_analytics(data)
    add_record(data)
    modify_record(data)
    delete_record(data)

# Display search results
if search_results:
    st.subheader("Search Results")
    for name, df in search_results.items():
        st.write(f"**{name}**: {len(df)} records found")
        st.write(df)

# Display filtered data
if filtered_data:
    st.subheader("Filtered Data")
    for name, df in filtered_data.items():
        st.write(f"**{name}**: {len(df)} records")

# Display data
if data:
    st.subheader("Data")
    for name, df in data.items():
        st.write(f"**{name}**: {len(df)} records")
        st.write(df)
