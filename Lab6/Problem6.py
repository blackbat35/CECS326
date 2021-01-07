import numpy as np
import random


def quick_sort(arr):
    n = len(arr)
    if n > 1:
        pivot = arr[0]
        less = [x for x in arr if x < pivot]
        greater = [x for x in arr if x > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)
    else:
        return arr


def init(arr, n):
    n_left = n//2
    #print(n_left)
    S_left = []
    S_right = []
    for i in range(n_left - 1, -1, -1):
        S_left.append(arr[i])
    for i in range(n_left, n):
        S_right.append(arr[i])
    #print(S_left)
    #print(S_right)
    S_left_sum = np.cumsum(S_left)
    S_right_sum = np.cumsum(S_right)
    #print(S_left_sum)
    #print(S_right_sum)
    S_left_sum_sort = quick_sort(S_left_sum)
    S_right_sum_sort = quick_sort(S_right_sum)
    print(S_left_sum_sort)
    print(S_right_sum_sort)
    m = len(S_left_sum_sort)
    n = len(S_right_sum_sort)
    i = 0
    #j = 0
    S_min = 99999
    while True:
        S = S_left_sum_sort[i] + S_right_sum_sort[n - 1]
        #print(S)
        if S <= 0:
            i += 1
            #print("i", i)
        else:
            n -= 1
            if (S < S_min) and (S > 0):
                S_min = S

        #else:
         #   j += 1
        """
        if i > m - 1:
            return 0
        elif n < 0:
            return n - 1
        """
        if (i == m - 1) or (n == 0):
            if (S > 0):
                S_min = S
            break

    return S_min


#arr = [-34,49, -58, 76, 29, -71, -54, 63]
#arr = [2, -3, 1, 4, -6, 10, -12, 5.2, 3.6, -8]
#n = len(arr)
n = int(input("Enter an integer n: "))
arr = random.sample(range(-20, 20), n)
print(arr)
print(init(arr, n))




