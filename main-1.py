from employee import Employee

def add_employee(employees):
    emp_id = input("Enter Employee ID: ")
    name = input("Enter Employee Name: ")
    position = input("Enter Position: ")
    basic_salary = float(input("Enter Basic Salary: "))
    hours_worked = float(input("Enter Hours Worked: "))
    hourly_rate = float(input("Enter Hourly Rate: "))
    
    employee = Employee(emp_id, name, position, basic_salary, hours_worked, hourly_rate)
    employees[emp_id] = employee

def view_employee(employees):
    emp_id = input("Enter Employee ID to View: ")
    employee = employees.get(emp_id)
    if employee:
        employee.display_details()
    else:
        print("Employee not found.")

def update_employee(employees):
    emp_id = input("Enter Employee ID to Update: ")
    employee = employees.get(emp_id)
    if employee:
        print("Enter new details (leave blank to keep current value):")
        name = input(f"Name ({employee.name}): ") or employee.name
        position = input(f"Position ({employee.position}): ") or employee.position
        basic_salary = input(f"Basic Salary ({employee.basic_salary}): ") or employee.basic_salary
        hours_worked = input(f"Hours Worked ({employee.hours_worked}): ") or employee.hours_worked
        hourly_rate = input(f"Hourly Rate ({employee.hourly_rate}): ") or employee.hourly_rate

        employee.update_details(name=name, position=position, basic_salary=float(basic_salary), 
                                hours_worked=float(hours_worked), hourly_rate=float(hourly_rate))
        print("Employee details updated.")
    else:
        print("Employee not found.")

def delete_employee(employees):
    emp_id = input("Enter Employee ID to Delete: ")
    if emp_id in employees:
        del employees[emp_id]
        print("Employee deleted.")
    else:
        print("Employee not found.")

def generate_report(employees):
    total_salary = 0
    for emp in employees.values():
        total_salary += emp.calculate_salary()

    print("Payroll Report")
    print(f"Total Employees: {len(employees)}")
    print(f"Total Salary Paid: {total_salary}")
    print(f"Average Salary: {total_salary / len(employees) if employees else 0}")

def main():
    employees = {}

    while True:
        print("\n--- Employee Payroll System ---")
        print("1. Add Employee")
        print("2. View Employee")
        print("3. Update Employee")
        print("4. Delete Employee")
        print("5. Generate Report")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_employee(employees)
        elif choice == '2':
            view_employee(employees)
        elif choice == '3':
            update_employee(employees)
        elif choice == '4':
            delete_employee(employees)
        elif choice == '5':
            generate_report(employees)
        elif choice == '6':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
