# tips calc

def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):

    # replace in string '$' on ''
    d = d.replace('$', '')

    return float(d)


def percent_to_float(p):

    # replace '%' on '' and float number
    p = float(p.replace('%', ''))
    return p / 100


main()
