'''
Return the "centered" average of an array of ints,
which we'll say is the mean average of the values,
except ignoring the largest and smallest values in
the array. If there are multiple copies of the
smallest value, ignore just one copy, and likewise
for the largest value. Use int division to produce
the final average. You may assume that the array is
length 3 or more.
'''

def centeredAvg(nums):
    n = [int(i) for i in nums.split()]
    n.sort()
    n.pop()
    n.pop(0)
    sum = 0
    for i in range(len(n)):
        sum += n[i]
    return sum/len(n)

if __name__ == '__main__':
    print(centeredAvg(input("Enter nums separated by space: ")))