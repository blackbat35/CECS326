import random


def kth_least_element(arr, a):

    pivot = arr[0]

    left = [x for x in arr if x < pivot]
    right = [x for x in arr if x > pivot]

    num_left = len(left)
    num_right = len(arr) - len(right)

    if a < num_left:
        return kth_least_element(left, a)
    elif a >= num_right:
        return kth_least_element(right, a - num_right)
    else:
        return pivot


diff = []
diff1 = []

n = int(input("Enter an integer n: "))
arr = random.sample(range(-100, 100), n)
print(arr)

k = int(input("Enter an integer k: "))
while k <= 0 or k >= n:
    k = int(input("Enter an integer k: "))

m = len(arr)//2
median = kth_least_element(arr, m)
print("median:", median)

a = len(arr)
for i in range(0, a):
    value = abs(arr[i] - median)
    value1 = arr[i] - median
    diff.append(value)
    diff1.append(value1)
print(diff)
print(diff1)

if k < n - 1:
    kth_biggest_element = kth_least_element(diff, k+1)
    for i in range(0, a):
        if diff[i] < kth_biggest_element and diff[i] != 0:
            diff2 = diff1[i] + median
            print(diff2)
else:
    arr.remove(median)
    print(arr)

arr.sort()
print(arr)
