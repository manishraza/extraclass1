hours_worked = float(input("enter the hours"))
hours_rate = float(input("enter the rate"))
if hours_worked <= 40:
    gross_pay = hours_worked * hours_rate
else:
    regular_pay = 40 * hours_rate
    overtime_pay = (hours_worked - 40) * 1.5 * hours_rate
    gross_pay = regular_pay + overtime_pay
print(gross_pay)