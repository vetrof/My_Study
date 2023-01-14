# This program tests the CellPhone class.

import cellphone

def main():
    # Get the phone data.
    man = input('Enter the manufacturer: ')
    mod = input('Enter the model number: ')
    retail = float(input('Enter the retail price: '))

    # Create an instance of the CellPhone class.
    phone = cellphone.CellPhone(man, mod, retail)

    # Display the data that was entered.
    print('Here is the data that you entered:')
    print(f'Manufacturer: {phone.get_manufact()}')
    print(f'Model Number: {phone.get_model()}')
    print(f'Retail Price: ${phone.get_retail_price():,.2f}')

# Call the main function.
if __name__ == '__main__':
      main()