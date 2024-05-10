expenses={}
def expense(category,amount,details):
    if category in expenses:
        expenses[category].append((amount,details))
    else:
        expenses[category]=[(amount,details)]
    print("Expense is included successfully......")
def outline_expenses():
    total_expenses = 0
    for category,items in expenses.items():
        print("Category:",category)
        category_total=0
        for item in items:
            category_total += item[0]
            print("Amount:",item[0],"Details:",item[1],"Category:",category_total)
        total_expenses += category_total
        print("*********************")
    print("Total expenses is:",total_expenses)            
def main():
    while True:
        print("----------------------")
        print("Expense Tracker")
        print("1.Expense")
        print("2.Outline of expenses")
        print("3.Exit")
        choice=input("Enter your choice(1/2/3):")
        if choice == "1":
            category=input("Enter the category of expense:")
            amount=float(input("Enter the cost of expense:"))
            details=input("Enter the details of expense:")
            expense(category,amount,details)
        elif choice == "2":
            outline_expenses()
        elif choice == "3":
            break
        else:
            print("invalid input......")
main()