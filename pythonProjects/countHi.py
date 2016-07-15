def count(str):
    cnt = 0
    for i in range(len(str)-1):
        s = str.lower()
        if s[i] == 'h' and s[i+1] == 'i':
            cnt += 1
    return cnt

if __name__ == '__main__':
    print(count(input("Enter a string: ")))