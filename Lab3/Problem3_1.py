import random


def kth_least_element(arr, a):
    pivot = arr[0]

    left = [x for x in arr if x < pivot]
    right = [x for x in arr if x > pivot]

    num_left = len(left)
    num_right = len(arr) - len(right)

    if a < num_left:
        print("left: ", left)
        return kth_least_element(left, a)
    elif a >= num_right:
        print("right: ", right)
        return kth_least_element(right, a - num_right)
    else:
        return pivot


#n = int(input("Enter an integer n: "))
#arr = random.sample(range(-100, 100), n)
arr =[10, 11, 12, 13, 14, 15, 16, 17, 18]
n = len(arr)
k = int(input("Enter an integer k: "))
while k <= 0 or k >= n:
    k = int(input("Enter an integer k: "))
print(arr)
print(kth_least_element(arr, k-1))
#arr.sort()
#print(arr)
