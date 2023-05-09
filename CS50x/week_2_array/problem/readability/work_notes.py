
letters = 214
words = 56
sentiens = 4

# letters_mid =  (letters / words) * 100
# sentiens_mid = (sentiens / words) * 100

letters_mid =  382.14
sentiens_mid = 7.14

index_koulmann = 0.0588 * letters_mid - 0.296 * sentiens_mid - 15.8

print("sentiens_mid", sentiens_mid)
print("letters_mid", letters_mid)
print("index_koulmann", index_koulmann, round(index_koulmann))

