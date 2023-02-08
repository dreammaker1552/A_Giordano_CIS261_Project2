# Initialize variables to keep track of totals
total_employees = 0
total_hours = 0
total_gross_pay = 0
total_income_tax = 0
total_net_pay = 0

# Continuously prompt for employee information until "End" is entered
while True:
    # Prompt for employee information
    name = input("Enter employee name (Enter 'End' to stop): ")
    if name == "End":
        break
    hours_worked = float(input("Enter hours worked: "))
    hourly_rate = float(input("Enter hourly rate: "))
    tax_rate = float(input("Enter income tax rate (in %): "))

    # Calculate gross pay, income taxes, and net pay
    gross_pay = hours_worked * hourly_rate
    income_tax = gross_pay * (tax_rate / 100)
    net_pay = gross_pay - income_tax

    # Display employee information
    print("Employee Name:", name)
    print("Hours Worked:", hours_worked)
    print("Hourly Rate: $", hourly_rate)
    print("Gross Pay: $", gross_pay)
    print("Income Tax Rate:", tax_rate, "%")
    print("Income Taxes: $", income_tax)
    print("Net Pay: $", net_pay)
    print("")

    # Add to totals
    total_employees += 1
    total_hours += hours_worked
    total_gross_pay += gross_pay
    total_income_tax += income_tax
    total_net_pay += net_pay

# Display payroll summary
print("Payroll Summary")
print("From Date: [Insert From Date]")
print("To Date: [Insert To Date]")
print("Total Number of Employees:", total_employees)
print("Total Hours Worked:", total_hours)
print("Total Gross Pay: $", total_gross_pay)
print("Total Income Taxes: $", total_income_tax)
print("Total Net Pay: $", total_net_pay)

