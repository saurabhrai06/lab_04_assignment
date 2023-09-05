class EmployeeTable:
    def __init__(self):
        self.data = [
            {"Employee ID": "161E90", "Name": "Raman", "Age": 41, "Salary (PM)": 56000},
            {"Employee ID": "161F91", "Name": "Himadri", "Age": 38, "Salary (PM)": 67500},
            {"Employee ID": "161F99", "Name": "Jaya", "Age": 51, "Salary (PM)": 82100},
            {"Employee ID": "171E20", "Name": "Tejas", "Age": 30, "Salary (PM)": 55000},
            {"Employee ID": "171G30", "Name": "Ajay", "Age": 45, "Salary (PM)": 44000},
        ]
# data

    def search_by_age(self, age):
        result = [employee for employee in self.data if employee["Age"] == age]
        return result

    def search_by_name(self, name):
        result = [employee for employee in self.data if employee["Name"].lower() == name.lower()]
        return result

    def search_by_salary(self, comparison, salary):
        if comparison == ">":
            result = [employee for employee in self.data if employee["Salary (PM)"] > salary]
        elif comparison == "<":
            result = [employee for employee in self.data if employee["Salary (PM)"] < salary]
        elif comparison == ">=":
            result = [employee for employee in self.data if employee["Salary (PM)"] >= salary]
        elif comparison == "<=":
            result = [employee for employee in self.data if employee["Salary (PM)"] <= salary]
        else:
            result = []
        return result

    def display_results(self, results):
        if not results:
            print("No matching records found.")
        else:
            for employee in results:
                print(employee)

if __name__ == "__main__":
    employee_table = EmployeeTable()

    while True:
        print("\nSearch Options:")
        print("1. Search by Age")
        print("2. Search by Name")
        print("3. Search by Salary")
        print("4. Quit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            age = int(input("Enter the age to search: "))
            results = employee_table.search_by_age(age)
            employee_table.display_results(results)
        elif choice == "2":
            name = input("Enter the name to search: ")
            results = employee_table.search_by_name(name)
            employee_table.display_results(results)
        elif choice == "3":
            comparison = input("Enter the salary comparison (>, <, <=, >=): ")
            salary = int(input("Enter the salary amount: "))
            results = employee_table.search_by_salary(comparison, salary)
            employee_table.display_results(results)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please choose a valid option (1/2/3/4).")


