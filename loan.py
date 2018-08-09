import sys
import os
import math
#calculating monthly payments for a loan


def monthly_payment(interest_rate):
    '''
    calculates the monthly payment for the loan. the user firsts enters the loan amount, the interest rate
    and the time it takes to pay it back. we're using the formula L=[i(1+i)n]/[1+i](n-1) where L is the monthly payment
    i=interest rate and n=time in months
    '''

    print ('Hello there!')
    print('')
    print('Please enter the loan amount')
    loan_amount = float(input(''))
    print('')
    print('Please enter the duration of the loan in years')
    time = int(input(''))
    print('')

    time=float(time)
    rate = interest_rate/100
    number_of_months = time*12
    payment = (loan_amount*(rate*(1+rate)*number_of_months))/((1+interest_rate)*(number_of_months-1))
    print("you will pay ksh{0:.2f} every month for the next {1:.0f} months!!".format(payment, number_of_months))


monthly_payment(5)
