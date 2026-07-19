import csv
import os
from datetime import date
Expenses=[]
if os.path.exists("expenses.csv"):
    with open("expenses.csv", "r", newline="") as file:
        reader = csv.DictReader(file)

        for expense in reader:
            expense["amount"] = float(expense["amount"])
            Expenses.append(expense)
while True:
 print("----EXPENSE TRACKER----")
 print("1.Add Expenses")
 print("2.View Expenses")
 print("3.View Total")
 print("4.Delete Expense")
 print("5.Exit")

 choice = input("Enter your choice:")

 if choice =="1":
      print("Add Expense Selected")
      while True:
        try:
          amount = float(input("Enter expense amount: ₹"))

          if amount <= 0:
                print("Amount must be greater than 0.")
          else:
                break

        except ValueError:
          print("Please enter a valid number.")
      
      description =input("add description:")
      category =input("Enter category:")
      expense_date=date.today()
                      
      expense={
        "amount":amount,"description":description,"category":category,"date":str(expense_date)
     }
      Expenses.append(expense)
      with open("expenses.csv", "a", newline="") as file:
        writer = csv.DictWriter(
         file,
          fieldnames=["amount", "description", "category", "date"]
        )
        if os.path.getsize("expenses.csv") == 0:
            writer.writeheader()

        writer.writerow(expense)
      print("Expense added succesfully!!")
     
 elif choice =="2":
     print("----------------------")
     print("View Expense Selected") 
     if len(Expenses)==0:
          print("No expenses Recorded.")
     else:
          for index, expense in enumerate(Expenses, start=1):
            print(index, ".", expense["description"])
            print("Amount:", expense["amount"])
            print("Description:",expense["description"])
            print("Category:", expense["category"])
            print("Date:",expense["date"])
 elif choice =="3":
      print("----------------------")    
      print("View Total Selected")
      total=0
      for expense in Expenses:
        total=total+expense["amount"]
      print("Total Expenses:",total)
 elif choice == "4":
    if len(Expenses) == 0:
        print("No expenses to delete.")

    else:
        for index, expense in enumerate(Expenses, start=1):
            print(index, ".", expense["description"])

        delete_choice = int(input("Enter the expense number to delete: "))

        if 1 <= delete_choice <= len(Expenses):
            deleted_expense = Expenses.pop(delete_choice - 1)
            with open("expenses.csv", "w", newline="") as file:
             writer = csv.DictWriter(
             file,
             fieldnames=[
                "amount",
                "description",
                "category",
                "date"
            ]
           )

             writer.writeheader()
             writer.writerows(Expenses)
            print(
                "Deleted:",
                deleted_expense["description"]
            )

        else:
             print("Invalid expense number.")     
 elif choice=="5":
      print("GOODBYE!!")
      break
 else:
      print("invalid choice")     