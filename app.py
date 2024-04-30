import streamlit as st
import pandas as pd
import os
import matplotlib.pyplot as plt

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

# Function to display summary of Customers data in diagrammatic form
def display_customers_summary(data):
    st.subheader("Customers Summary")
    customers_df = data.get("Customers.csv")
    if customers_df is not None:
        # Plotting a bar chart for the number of customers by country
        customers_by_country = customers_df['Country'].value_counts()
        plt.figure(figsize=(10, 6))
        customers_by_country.plot(kind='bar')
        plt.xlabel('Country')
        plt.ylabel('Number of Customers')
        plt.title('Number of Customers by Country')
        st.pyplot()
    else:
        st.warning("Customers data not found.")

# Function to display summary of Parts data in diagrammatic form
def display_parts_summary(data):
    st.subheader("Parts Summary")
    parts_df = data.get("Parts.csv")
    if parts_df is not None:
        # Plotting a pie chart for the distribution of parts by category
        parts_by_category = parts_df['Category'].value_counts()
        plt.figure(figsize=(8, 8))
        parts_by_category.plot(kind='pie', autopct='%1.1f%%', startangle=90)
        plt.title('Distribution of Parts by Category')
        plt.axis('equal')
        st.pyplot()
    else:
        st.warning("Parts data not found.")

# Function to display summary of Sales data in diagrammatic form
def display_sales_summary(data):
    st.subheader("Sales Summary")
    sales_df = data.get("Sales.csv")
    if sales_df is not None:
        # Plotting a line chart for sales over time
        sales_df['Date'] = pd.to_datetime(sales_df['Date'])
        sales_by_date = sales_df.groupby(sales_df['Date'].dt.to_period('M')).size()
        plt.figure(figsize=(10, 6))
        sales_by_date.plot(kind='line', marker='o')
        plt.xlabel('Month')
        plt.ylabel('Number of Sales')
        plt.title('Sales Over Time')
        st.pyplot()
    else:
        st.warning("Sales data not found.")

# Function to display summary of Inventory data in diagrammatic form
def display_inventory_summary(data):
    st.subheader("Inventory Summary")
    inventory_df = data.get("inventory.csv")
    if inventory_df is not None:
        # Plotting a bar chart for inventory by product
        inventory_by_product = inventory_df.groupby('Product')['Quantity'].sum()
        plt.figure(figsize=(10, 6))
        inventory_by_product.plot(kind='bar')
        plt.xlabel('Product')
        plt.ylabel('Inventory Quantity')
        plt.title('Inventory by Product')
        st.pyplot()
    else:
        st.warning("Inventory data not found.")

# Function to display summary of Salespersons data in diagrammatic form
def display_salespersons_summary(data):
    st.subheader("Salespersons Summary")
    salespersons_df = data.get("Salespersons.csv")
    if salespersons_df is not None:
        # Plotting a bar chart for salespersons by region
        salespersons_by_region = salespersons_df['Region'].value_counts()
        plt.figure(figsize=(10, 6))
        salespersons_by_region.plot(kind='bar')
        plt.xlabel('Region')
        plt.ylabel('Number of Salespersons')
        plt.title('Salespersons by Region')
        st.pyplot()
    else:
        st.warning("Salespersons data not found.")

# Function to display summary of Car Models data in diagrammatic form
def display_car_models_summary(data):
    st.subheader("Car Models Summary")
    car_models_df = data.get("car_models.csv")
    if car_models_df is not None:
        # Plotting a pie chart for the distribution of car models by manufacturer
        car_models_by_manufacturer = car_models_df['Manufacturer'].value_counts()
        plt.figure(figsize=(8, 8))
        car_models_by_manufacturer.plot(kind='pie', autopct='%1.1f%%', startangle=90)
        plt.title('Distribution of Car Models by Manufacturer')
        plt.axis('equal')
        st.pyplot()
    else:
        st.warning("Car Models data not found.")

# Function to display summary of Customer Feedback data in diagrammatic form
def display_customer_feedback_summary(data):
    st.subheader("Customer Feedback Summary")
    customer_feedback_df = data.get("customer_feedback.csv")
    if customer_feedback_df is not None:
        # Plotting a pie chart for the distribution of feedback types
        feedback_types = customer_feedback_df['Feedback Type'].value_counts()
        plt.figure(figsize=(8, 8))
        feedback_types.plot(kind='pie', autopct='%1.1f%%', startangle=90)
        plt.title('Distribution of Feedback Types')
        plt.axis('equal')
        st.pyplot()
    else:
        st.warning("Customer Feedback data not found.")

# Function to display summary of Design Improvements data in diagrammatic form
def display_design_improvements_summary(data):
    st.subheader("Design Improvements Summary")
    design_improvements_df = data.get("design_improvements.csv")
    if design_improvements_df is not None:
        # Plotting a bar chart for the number of design improvements by category
        improvements_by_category = design_improvements_df['Category'].value_counts()
        plt.figure(figsize=(10, 6))
        improvements_by_category.plot(kind='bar')
        plt.xlabel('Category')
        plt.ylabel('Number of Improvements')
        plt.title('Design Improvements by Category')
        st.pyplot()
    else:
        st.warning("Design Improvements data not found.")

# Function to display summary of Service Appointments data in diagrammatic form
def display_service_appointments_summary(data):
    st.subheader("Service Appointments Summary")
    service_appointments_df = data.get("service_appointments.csv")
    if service_appointments_df is not None:
        # Plotting a bar chart for the number of appointments by service type
        appointments_by_service_type = service_appointments_df['Service Type'].value_counts()
        plt.figure(figsize=(10, 6))
        appointments_by_service_type.plot(kind='bar')
        plt.xlabel('Service Type')
        plt.ylabel('Number of Appointments')
        plt.title('Service Appointments by Service Type')
        st.pyplot()
    else:
        st.warning("Service Appointments data not found.")

# Function to display summary of Service Technicians data in diagrammatic form
def display_service_technicians_summary(data):
    st.subheader("Service Technicians Summary")
    service_technicians_df = data.get("service_technicians.csv")
    if service_technicians_df is not None:
        # Plotting a pie chart for the distribution of technicians by specialization
        technicians_by_specialization = service_technicians_df['Specialization'].value_counts()
        plt.figure(figsize=(8, 8))
        technicians_by_specialization.plot(kind='pie', autopct='%1.1f%%', startangle=90)
        plt.title('Distribution of Service Technicians by Specialization')
        plt.axis('equal')
        st.pyplot()
    else:
        st.warning("Service Technicians data not found.")

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

# Sidebar navigation
selected_page = st.sidebar.selectbox("Select Page", ["Quarry Crafters"] + list(data.keys()))

# Conditionally display dashboard data
if selected_page == "Quarry Crafters":
    display_data_summary(data)
elif selected_page == "Customers.csv":
    display_customers_summary(data)
elif selected_page == "Parts.csv":
    display_parts_summary(data)
elif selected_page == "Sales.csv":
    display_sales_summary(data)
elif selected_page == "Inventory.csv":
    display_inventory_summary(data)
elif selected_page == "Salespersons.csv":
    display_salespersons_summary(data)
elif selected_page == "car_models.csv":
    display_car_models_summary(data)
elif selected_page == "customer_feedback.csv":
    display_customer_feedback_summary(data)
elif selected_page == "design_improvements.csv":
    display_design_improvements_summary(data)
elif selected_page == "service_appointments.csv":
    display_service_appointments_summary(data)
elif selected_page == "service_technicians.csv":
    display_service_technicians_summary(data)
else:
    st.title(selected_page)
    st.write(data[selected_page])
