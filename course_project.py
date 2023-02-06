from datetime import datetime
from os import *
import sys
def terminate():
    exit = input('Type END to exit the program or N.\n')
    if exit.upper == 'END':
        sys.exit()
    if exit.upper == 'N':
        main()

def employeeName():
    employee = []
    name = input('Enter employees full name.\n')
    add = input('Add another employee? [Y/N]\n')
    while add.upper() == 'Y':
        name = input('Enter employees full name.\n')
        break
    else:
        print('Number of employees:',len(employee))
    n = employee.append(name)
    return name, n

def startDate():
    date_str = input('Enter start date (mm/dd/yyyy)\n')
    date_start = datetime.strptime(date_str, '%m/%d/%Y')
    return date_start

def endDate():
    date_str = input('Enter start date (mm/dd/yyyy)\n')
    date_end = datetime.strptime(date_str, '%m/%d/%Y')
    return date_end

def totalDays(date_start, date_end):
    total_days = (date_end - date_start)
    return total_days


def totalHours(total_days):
    hours = 8 * total_days
    overtime = 4 * total_days
    total_hours = hours + overtime
    return total_hours

def payRate():
    pay = int(input('Enter the employees hourly wage.\n'))
    return pay

def taxRate():
    tax = 0.10
    return tax

def calculateIncome(total_hours, tax, pay):
    gross = total_hours * pay
    total_tax = gross * tax
    net = gross - tax
    return gross, total_tax, net

def employeeData(employee, total_hours, total_tax, net):
   pass


def main():
    employeeName()
    startDate()
    endDate()
    totalDays(10, 17)
    totalHours(7)
    payRate()
    taxRate()
    calculateIncome(12, 0.10, 25)
    terminate()
   

if __name__ == '__main__':
    main()