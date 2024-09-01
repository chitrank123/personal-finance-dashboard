import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Fetch and process license keys from environment variables
license_keys_str = os.getenv("VALID_LICENSE_KEYS")
VALID_LICENSE_KEYS = [key.strip() for key in license_keys_str.split(',')] if license_keys_str else []
print("valid liscence keys",VALID_LICENSE_KEYS)
# License key input
license_key = st.text_input("Enter your license key")
print("license_key",license_key)
if license_key in VALID_LICENSE_KEYS:
    st.success("License key validated!")
    
    # Load the data
    @st.cache_data
    def load_data():
        data = pd.read_csv("data/transactions.csv")
        data['Month'] = pd.to_datetime(data['Month'], format='%Y-%m').dt.to_period('M')
        return data

    data = load_data()

    # Sidebar for Month Selection
    st.sidebar.header("Select Month")
    selected_month = st.sidebar.selectbox("Month", options=data['Month'].unique())

    # Filter data by the selected month
    filtered_data = data[data['Month'] == selected_month]

    # Main Dashboard
    st.title("Monthly Personal Finance Dashboard")
    st.write(f"Overview for {selected_month}")

    # Summary Statistics
    st.header("Summary")
    total_income = filtered_data['Income'].sum()
    total_expenses = filtered_data.iloc[:, 2:].sum(axis=1).sum()  # Summing all expense columns
    net_balance = total_income - total_expenses

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Income", f"₹{total_income:,.2f}")
    col2.metric("Total Expenses", f"₹{total_expenses:,.2f}")
    col3.metric("Net Balance", f"₹{net_balance:,.2f}")

    # Expense Breakdown
    st.header("Expense Breakdown")
    expense_breakdown = filtered_data.iloc[:, 2:].sum(axis=0)

    fig, ax = plt.subplots()
    ax.pie(expense_breakdown, labels=expense_breakdown.index, autopct='%1.1f%%')
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    st.pyplot(fig)

    # Add New Month Data
    st.header("Add Monthly Data")
    with st.form("monthly_data_form"):
        # Date input using default format (YYYY-MM-DD)
        month = st.date_input("Month", value=datetime.today())

        # Convert the selected date to 'YYYY-MM' format
        month_str = month.strftime('%Y-%m')
        
        income = st.number_input("Income (₹)", min_value=0.01, step=0.01)
        groceries = st.number_input("Groceries (₹)", min_value=0.00, step=0.01)
        utilities = st.number_input("Utilities (₹)", min_value=0.00, step=0.01)
        rent = st.number_input("Rent (₹)", min_value=0.00, step=0.01)
        entertainment = st.number_input("Entertainment (₹)", min_value=0.00, step=0.01)
        others = st.number_input("Others (₹)", min_value=0.00, step=0.01)
        
        submit = st.form_submit_button("Add Monthly Data")
        
        if submit:
            new_month_data = pd.DataFrame({
                "Month": [month_str],  # Use the formatted month string
                "Income": [income],
                "Groceries": [groceries],
                "Utilities": [utilities],
                "Rent": [rent],
                "Entertainment": [entertainment],
                "Others": [others]
            })
            
            new_month_data.to_csv("data/transactions.csv", mode='a', header=False, index=False)
            st.success("Monthly data added successfully!")

    # Trend Analysis
    st.header("Trend Analysis")
    income_trend = data.groupby('Month')['Income'].sum()
    expenses_trend = data.iloc[:, 2:].groupby(data['Month']).sum().sum(axis=1)
    savings_trend = income_trend - expenses_trend

    fig, ax = plt.subplots()
    ax.plot(income_trend.index.astype(str), income_trend, label='Income', marker='o')
    ax.plot(expenses_trend.index.astype(str), expenses_trend, label='Expenses', marker='o')
    ax.plot(savings_trend.index.astype(str), savings_trend, label='Savings', marker='o')
    ax.set_xlabel('Month')
    ax.set_ylabel('Amount (₹)')
    ax.set_title('Income, Expenses, and Savings Trend')
    ax.legend()
    st.pyplot(fig)

    # Savings Tracker
    st.header("Savings Tracker")
    st.write(f"Savings for {selected_month}: ₹{net_balance:,.2f}")
    st.write(f"Total Savings so far: ₹{savings_trend.sum():,.2f}")

    # Investment Tracking
    st.header("Investment Tracking")
    with st.form("investment_form"):
        investment_name = st.text_input("Investment Name")
        investment_amount = st.number_input("Investment Amount (₹)", min_value=0.01, step=0.01)
        investment_return = st.number_input("Expected Return (%)", min_value=0.0, step=0.1)
        
        submit_investment = st.form_submit_button("Add Investment")
        
        if submit_investment:
            st.write(f"Added Investment: {investment_name}, Amount: ₹{investment_amount:,.2f}, Expected Return: {investment_return}%")

    # Advanced Recommendations
    st.header("Advanced Recommendations")
    if net_balance < 0:
        st.warning(f"Your expenses exceed your income for {selected_month}. Consider reducing unnecessary expenses.")
    else:
        st.success(f"You're saving ₹{net_balance:,.2f} this month. Consider investing your savings to grow your wealth.")

    # Budget Planning
    st.header("Budget Planning")
    budget = st.number_input("Set Monthly Budget (₹)", min_value=0.01, step=0.01)
    remaining_budget = budget - total_expenses

    st.write(f"Remaining Budget for {selected_month}: ₹{remaining_budget:,.2f}")

    # Recommendations Based on Spending Patterns
    if remaining_budget < 0:
        st.warning("You've exceeded your budget for the month!")
    else:
        st.success("You're within your budget. Great job!")
else:
    st.error("Invalid license key. Please enter a valid key to access the features.")
    st.stop()  # Stop further execution if the key is invalid
