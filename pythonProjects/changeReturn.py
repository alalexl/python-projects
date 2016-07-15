from math import *
def calculate(cost, money):
    if money < cost:
        return("Not enough money")
    else:
        change = money - cost
        temp = change
        q = floor(temp / .25)
        temp -= q * .25
        d = floor(temp / .1)
        temp -= d * .1
        n = floor(temp / .05)
        temp -= n * .05
        #return("Change is $" + change + ". Q: " + q + " D: " + d + " N: " + n + " P: " + p)
        return("Change is ${0}. Q: {1} D: {2} N: {3} P: {4}".format(change,q,d,n,temp))

def main():
    cost = float(input("Item cost? "))
    money = float(input("Amount of money given? "))
    print(calculate(cost, money))

if __name__ == '__main__':
    main()

#floating numbers are dumb