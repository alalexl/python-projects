#return true if string contains xyz that doesnt have . in front

def checkPeriod(str):
    n = str.find('xyz')
    if n == 0:
        return True
    elif str[n-1] != '.':
        return True
    else:
        return False


if __name__ == '__main__':
    print(checkPeriod(input("Enter a string: ")))