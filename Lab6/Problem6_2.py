import numpy as np
import random


def quick_sort(arr, ascending=True):
    if len(arr) <= 1:
        return arr
    less, equal, greater = [], [], []
    pivot = arr[0]

    for x in range(0, len(arr)):
        equal = [x for x in arr if x == pivot]
        less = [x for x in arr if x < pivot]
        greater = [x for x in arr if x > pivot]
    greater = quick_sort(greater, ascending=ascending)
    less = quick_sort(less, ascending=ascending)

    if ascending:
        final = less + equal + greater
    else:
        final = greater + equal + less
    return final


def init(arr):
    #global MPSSL, MPSSR
    n = len(arr)
    n_left = n//2
    #print(n_left)
    S_left = []
    S_right = []
    for i in range(0, n_left):
        S_left.append(arr[i])
    for i in range(n_left, n):
        S_right.append(arr[i])
    print(S_left)
    print(S_right)
    S_left_sum = np.cumsum(S_left)
    S_right_sum = np.cumsum(S_right)
    print(S_left_sum)
    print(S_right_sum)
    S_left_sum_sort = quick_sort(S_left_sum, ascending=True)
    S_right_sum_sort = quick_sort(S_right_sum, ascending=False)
    print(S_left_sum_sort)
    print(S_right_sum_sort)
    m = len(S_left_sum_sort)
    n = len(S_right_sum_sort)
    i = 0
    j = 0
    S_min = 99999
    S_min_n = []
    #print(S_left_sum_sort[m-1])
    #print(S_right_sum_sort[n-1])

    while True:
        if (i == m) or (j == n):
            break

        S = S_left_sum_sort[i] + S_right_sum_sort[j]

        if S <= 0:
            i += 1

        elif (S < S_min) and (S > 0):
            S_min = S
            S_min_n.append(S_min)
            j += 1

        elif S > S_min:
            S_min_n.append(S)
            j += 1
        """
        if i > m - 1:
            return i == m - 1
        elif j > n - 1:
            return j == n - 1
        """
    print(S_min_n)
    S_min1 = min(x for x in S_min_n if x > 0)

    return S_min1

#testarr = [-34,49, -58, 76, 29, -71, -54, 63]
#testarr = [2, -3, 1, 4, -6, 10, -12, 5.2, 3.6, -8]
#testarr = [-7, 13, -4, 16, 4];
#n = len(testarr)
#L = testarr[0: 2]
#R = testarr[2: 5]
#print(L)
#print(R)
n = int(input("Enter an integer n: "))
arr = random.sample(range(-20, 20), n)
print(arr)
print(init(arr))





