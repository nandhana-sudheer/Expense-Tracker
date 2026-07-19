import streamlit as st
import csv
import os
from datetime import date


st.title("Expense Tracker")

st.header("Add an Expense")


amount = st.number_input(
    "Enter expense amount",
    min_value=0.0
)


description = st.text_input(
    "Enter expense description"
)


category = st.text_input(
    "Enter expense category"
)


if st.button("Add Expense"):

    if amount <= 0:
        st.error("Amount must be greater than 0.")

    elif description == "":
        st.error("Please enter a description.")

    elif category == "":
        st.error("Please enter a category.")

    else:

        expense = {
            "amount": amount,
            "description": description,
            "category": category,
            "date": str(date.today())
        }


        file_exists = os.path.exists("expenses.csv")


        with open("expenses.csv", "a", newline="") as file:

            writer = csv.DictWriter(
                file,
                fieldnames=[
                    "amount",
                    "description",
                    "category",
                    "date"
                ]
            )


            if not file_exists or os.path.getsize("expenses.csv") == 0:
                writer.writeheader()


            writer.writerow(expense)


        st.success("Expense added successfully!")
st.header("All Expenses")

if os.path.exists("expenses.csv"):

    with open("expenses.csv", "r", newline="") as file:

        reader = csv.DictReader(file)

        expenses = list(reader)


    if len(expenses) == 0:

        st.info("No expenses recorded yet.")

    else:

        st.dataframe(expenses)
        total = 0

        for expense in expenses:
          total = total + float(expense["amount"])

        st.subheader("Total Expenses")

        st.write(f"₹{total:.2f}")

else:

    st.info("No expenses recorded yet.")    