# Name: Brady Dodd
# Prog Purpose: Generate payroll info
#       Category codes and hourly pay rates:
#       C   Cashier: $16.50
#       S   Stocker: $15.75
#       J   Janitor: $15.75
#       M   Maintenance: $19.50
#       Deduction Rates:
#       Federal income tax rate: 0.12
#       State income tax rate: 0.03
#       Social Security tax rate: 0.062
#       Medicare tax rate: 0.0145

import datetime

#define deduction
DEDUCTION_RATES = (0.12, 0.03, 0.062, 0.0145)

#define pay
PAY_RATES = (16.50, 15.75, 15.75, 19.50)

#define general variables
hours_worked = 0
job_category = 0
pay_rate = 0
gross_pay = 0
federal_deduct = 0
state_deduct = 0
social_security_deduct = 0
medicare_deduct = 0
total_deduct = 0
net_pay = 0

#define program functions
def main():
    another_employee = True
    while another_employee:
        get_user_data()
        perform_calculations()
        display_results()
        yesno = input("\nWould you like to calculate payroll data for another employee? (Y/N): ")
        if yesno.upper() != "Y":
            another_employee = False
            print("\nGet back to work!")

#category code and number of hours
def get_user_data():
    global job_category, hours_worked
    job_category = input("Job category code (C,S,J,M): ")
    
    # cant calculate overtime
    try:
        hours_worked = int(input("Number of hours worked: "))
        if hours_worked > 40:
            raise ValueError("Number of hours worked cannot be above 40.")
    except ValueError as err:
        print(f"\nInvalid input for number of hours worked: {err}")
        hours_worked = 0


#calculating gross, deductions, net
def perform_calculations():
    global pay_rate, gross_pay, federal_deduct, state_deduct, total_deduct, social_security_deduct, medicare_deduct, net_pay

#assign rate
    if job_category.upper() == "C":
        pay_rate = PAY_RATES[0]
    elif job_category.upper() == "S":
        pay_rate = PAY_RATES[1]
    elif job_category.upper() == "J":
        pay_rate = PAY_RATES[2]
    elif job_category.upper() == "M":
        pay_rate = PAY_RATES[3]
    else:
        pay_rate = 0
        print("\nInvalid code entered.")

#gross 
    gross_pay = hours_worked * pay_rate
    
#deductions
    federal_deduct = gross_pay * DEDUCTION_RATES[0]
    state_deduct = gross_pay * DEDUCTION_RATES[1]
    social_security_deduct = gross_pay * DEDUCTION_RATES[2]
    medicare_deduct = gross_pay * DEDUCTION_RATES[3]
    
#net deductions
    total_deduct = federal_deduct+state_deduct+social_security_deduct+medicare_deduct

#net pay
    net_pay = gross_pay - total_deduct

def display_results():
    print('\n******************************')
    print('     Fresh Foods     ')
    print('   Weekly Paycheck   ')
    print('--------------------------------')
    print('Hours Worked        : ' + format(hours_worked,'10.2f'))
    print('Payrate             $ ' + format(pay_rate,'10.2f'))
    print('Gross Pay           $ ' + format(gross_pay,'10.2f'))
    print('Federal income tax  $ ' + format(federal_deduct, '10.2f'))
    print('State income tax    $ ' + format(state_deduct,'10.2f'))
    print('Social security tax $ ' + format(social_security_deduct, '10.2f'))
    print('Medicare tax        $ ' + format(medicare_deduct, '10.2f'))
    print('Total deductions    $ ' + format(total_deduct, '10.2f'))
    print('Net pay             $ ' + format(net_pay,'10.2f'))
    print('--------------------------------')
    print('   ' + str(datetime.datetime.now()))
    print('\n********************************')

main()
