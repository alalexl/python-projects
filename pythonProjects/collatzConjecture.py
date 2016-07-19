
def collatz(num):
    if num < 2:
        return "Number is less than or equal to one. "
    else:
        steps = 0
        while num != 1:
            if num % 2 == 0:
                num /= 2
                steps += 1
            else:
                num *= 3
                num += 1
                steps += 1
        return "It took {} step(s).".format(steps)
    
if __name__ == '__main__':
    print(collatz(int(input("Enter a number greater than one: "))))