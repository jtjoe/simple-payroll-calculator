
# Simple Payroll Calculator

menu = "\nPress 's' to start calculating employee payroll or 'q' to exit"
print("Welcome to Simple Payroll Calculator!" + menu)
choice = input('\nPlease enter your choice: ').lower()

def calculate(name, hours, rate):
    ot, otp = 0.0, 0.0
    if hours <= 0 or rate <= 0:
        return "Invalid Hours Worked or Hourly Rate, please try again"
    if hours - 40 > 0:
        print("overtime calculation here")
        ot = hours - 40
        otp = ot * (rate * 1.5)
    print("calculating the rest here")
    gross = otp + (hours - ot) * rate
    fed = gross * 0.1
    state = gross * 0.03
    fica = gross * 0.07
    net = gross - (fed + state + fica)
    return f"Name: {name}, Hours: {hours}, Rate: {rate}\nGross Pay: {gross}, OT Pay: {otp}, Fed Tax:{fed}, State Tax: {state}, FICA: {fica}, Net Pay: {net}"

while choice != 'q':
    if choice not in ['s','q']:
        choice = input('\nUnknown input, please try again:\n' + menu).lower()
    if choice == 'q':
        print("\nExiting Payroll Calculator")
        break
    else:
        name = input('Please enter Employee Name:')

        try:
            hours = float(input('Please enter Hours Worked:'))
        except ValueError as e:
            print(f"Error '{e}' occurred")
            hours = float(input('\nInvalid input, please enter Hours Worked again:'))
        try:
            rate = float(input('Please enter Hourly Rate:'))
        except ValueError as e:
            print(f"Error '{e}' occurred")
            rate = input('\nInvalid input, please enter Hourly Rate again:')

        print(calculate(name, float(hours), float(rate)))
    choice = input('\nPlease enter your choice: ').lower()
print("\nExiting Payroll Calculator")
