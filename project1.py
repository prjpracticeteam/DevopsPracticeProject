def div4(number):
    if len(number) != 1:
        onesdigit = int(number[-1])
        tensdigit = int(number[-2])

        if tensdigit in [2, 4, 6, 8] and onesdigit in [0, 4, 8]:
            return True
        elif tensdigit in [1, 3, 5, 7, 9] and onesdigit in [2, 6]:
            return True
        else:
            return False
    elif int(number) in [0, 4, 8]:
        return True


if __name__ == "__main__":
    number = input("Enter a number")
    div4(number)
    print(f"{number} is {'' if div4(number) else 'not'} divisble by 4")

