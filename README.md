# Personal Finance Dashboard

## Overview

The Personal Finance Dashboard is a Streamlit application designed to help you manage and track your personal finances. This tool provides a comprehensive view of your income, expenses, and savings, with features to analyze trends, track investments, and receive financial recommendations.

## Features

- **Monthly Income and Expense Tracking**: Record your monthly income and various types of expenses such as groceries, utilities, rent, entertainment, and others.
- **Trend Analysis**: Visualize income, expenses, and savings trends over multiple months to understand your financial behavior.
- **Savings Tracker**: Track your savings for each month and view total savings to date.
- **Investment Tracking**: Add and monitor investments with expected returns.
- **Advanced Recommendations**: Get personalized financial advice based on your spending patterns.
- **Budget Planning**: Set and track your monthly budget to stay within your financial goals.

## Getting Started

### Prerequisites

- Python 3.7 or higher
- Streamlit
- Pandas
- Matplotlib
- Seaborn
- Python-dotenv

### Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/chitrank123/personal-finance-dashboard.git
   cd personal-finance-dashboard

2. **Create and Activate Virtual Environment**
    python -m venv financeenv
    source financeenv/bin/activate  # On Windows use `financeenv\Scripts\activate`

3. **Install Dependencies**
    pip install -r requirements.txt

4. **Set Up Environment Variables**
    VALID_LICENSE_KEYS=["yourkey1", "yourkey2"]

5. **Run The Application**
    streamlit run app.py

### Usage

- **License Key**: Enter a valid license key to access the dashboard features.
- **Select Month**: Use the sidebar to select the month you want to view or add new data.
- **Add Monthly Data**: Input your income and expenses for the selected month and submit.
- **View Trends and Recommendations**: Analyze your financial trends and get recommendations based on your spending.

### License

This project is licensed under the MIT License - see the LICENSE file for details.

### Contributing

**Contributions are welcome! Please follow these steps to contribute:**

1. Fork the repository.
2. Create a new branch (git checkout -b feature-branch).
3. Commit your changes (git commit -am 'Add new feature').
4. Push to the branch (git push origin feature-branch).
5. Create a new Pull Request.

### Contact

For any questions or feedback, please reach out to Chitranktak.

### Acknowledgements

- Thanks to the Streamlit team for creating this fantastic framework.
- Special thanks to the Pandas and Matplotlib communities for their valuable libraries.