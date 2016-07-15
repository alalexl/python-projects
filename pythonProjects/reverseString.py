def reverseString(str):
    for i in reversed(range(len(str))):
        print(str[i], end="")
    print()

def oneLine(str):
    s = str[::-1]
    print(s)

if __name__ == '__main__':
    #reverseString(input("Enter a string: "))
    oneLine(input("Enter a string: "))