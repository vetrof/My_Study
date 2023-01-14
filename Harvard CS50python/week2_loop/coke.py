
# Suppose that a machine sells bottles of Coca-Cola (Coke)
# for 50 cents and only accepts coins in these denominations:
# 25 cents, 10 cents, and 5 cents.

# create start variable
cost = 50
usr_coin = 0

# create infinite loop while cost > 0
while cost > 0:

    # display how need user insert cents
    cost = cost - usr_coin
    print('Amount Due: ', cost)

    # user insert coin
    insert = int(input('Insert Coin: '))

    # match user input to 25, 10, 5 coin

    match insert:
        case 25 | 10 | 5:
            cost -= insert


# calc change if user insert to math coin
change = cost * (-1)
print('Change Owen:', change)

