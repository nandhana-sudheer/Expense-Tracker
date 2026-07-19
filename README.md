# Expense Tracker

A beginner-friendly expense tracking application built with Python.

This project includes two versions:

* A command-line version
* A Streamlit web application

## Features

* Add expenses
* Store amount, description, category, and date
* View all expenses
* Calculate total expenses
* Delete expenses
* Validate user input
* Save expenses to a CSV file
* Load saved expenses when the program starts
* Use a web interface with Streamlit

## Project Versions

### Command-Line Version

The original version runs in the terminal.

Run it with:

```bash
python main.py
```

### Streamlit Web Version

The Streamlit version provides a web-based interface.

Run it with:

```bash
streamlit run app.py
```

## Technologies Used

* Python
* CSV
* Streamlit
* Git
* GitHub

## Project Structure

```text
expense-tracker/
│
├── main.py          # Command-line version
├── app.py           # Streamlit web version
├── .gitignore       # Files ignored by Git
└── README.md        # Project documentation
```

## How to Run the Project

### 1. Clone the repository

```bash
git clone YOUR_REPOSITORY_URL
```

### 2. Open the project folder

```bash
cd expense-tracker
```

### 3. Install Streamlit

```bash
pip install streamlit
```

### 4. Run the command-line version

```bash
python main.py
```

### 5. Run the Streamlit version

```bash
streamlit run app.py
```

## Data Storage

Expenses are stored in a CSV file.

Each expense contains:

* Amount
* Description
* Category
* Date

The `expenses.csv` file is ignored by Git so personal expense data is not uploaded to GitHub.

## What I Learned

Through this project, I practiced:

* Python variables and data types
* Lists and dictionaries
* Loops and conditional statements
* Error handling with `try` and `except`
* Reading and writing CSV files
* File handling with `with open()`
* Working with dates
* Using Python modules
* Building a web application with Streamlit
* Using Git and GitHub



## Author

Created as a Python learning project.
