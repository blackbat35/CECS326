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


n = int(input("Enter an integer n: "))
arr = random.sample(range(-100, 100), n)
k = int(input("Enter an integer k: "))
while k <= 0 or k >= n:
    k = int(input("Enter an integer k: "))
print(arr)
m = len(arr) - k
a = len(arr)
b = kth_least_element(arr, m)
print(b)
for i in range(0, a):
    if arr[i] > b:
        print(arr[i])
arr.sort()
print(arr)
