# def total(galleons, sickles, knuts):
#     return (galleons * 17 + sickles) * 29 + knuts
#
# coins = [100, 50, 25]
#
# print(*coins)
#
# print(total(*coins), "Knuts")




def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts

coins = {"galleons": 100, "sickles": 50, "knuts": 25}

print(coins)

print(total(**coins), "Knuts")

