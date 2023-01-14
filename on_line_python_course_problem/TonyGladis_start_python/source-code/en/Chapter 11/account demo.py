# This program creates an instance of the SavingsAccount
# class and an instance of the CD account.

import accounts

def main():
    # Get the account number, interest rate,
    # and account balance for a savings account.
    print('Enter the following data for a savings account.')
    acct_num = input('Account number: ')
    int_rate = float(input('Interest rate: '))
    balance = float(input('Balance: '))

    # Create a SavingsAccount object.
    savings = accounts.SavingsAccount(acct_num, int_rate,
                                      balance)

    # Get the account number, interest rate,
    # account balance, and maturity date for a CD.
    print('Enter the following data for a CD.')
    acct_num = input('Account number: ')
    int_rate = float(input('Interest rate: '))
    balance = float(input('Balance: '))
    maturity = input('Maturity date: ')

    # Create a CD object.
    cd = accounts.CD(acct_num, int_rate, balance, maturity)

    # Display the data entered.
    print('Here is the data you entered:')
    print()
    print('Savings Account')
    print('---------------')
    print(f'Account number: {savings.get_account_num()}')
    print(f'Interest rate: {savings.get_interest_rate()}')
    print(f'Balance: ${savings.get_balance():,.2f}')
    print()
    print('CD')
    print('---------------')
    print(f'Account number: {cd.get_account_num()}')
    print(f'Interest rate: {cd.get_interest_rate()}')
    print(f'Balance: ${cd.get_balance():,.2f}')
    print(f'Maturity date: {cd.get_maturity_date()}')

# Call the main function.
if __name__ == '__main__':
      main()