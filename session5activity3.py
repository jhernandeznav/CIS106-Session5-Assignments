# program for wage done
name = input('Enter your last name: ')
hours_worked = float(input('Enter the amount hours work per week: '))
rate = float(input('Enter the rate per hour:$ '))
print('Last name:', name)
print('Hours worked:', hours_worked)
print('Hourly rate:$', rate)


def calculate_pay():
    pay = hours_worked * rate
    return pay


def calculate_overtime_pay():
    overtime_pay = (int(hours_worked - 40) * (float(rate) * 1.50) + 40 * float(rate))
    return overtime_pay


def display_pay(pay):
    print('Gross pay $', pay)


def display_overtime(overtime_pay):
    print('Gross pay $', overtime_pay)


def main():
    if float(hours_worked) <= 40:
        pay = calculate_pay()
        display_pay(pay)
    else:
        overtime_pay = calculate_overtime_pay()
        display_overtime(overtime_pay)


main()
# display regular hours, regular pay, overtime hours and overtime pay
