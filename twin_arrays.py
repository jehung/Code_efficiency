## You are given two arrays A and B each containing  integers. You need to choose exactly one number from A and B exactly 
## number from B such that the index of the two chosen numbers is not same and the sum of the 2 chosen values is minimum.

## Your objective is to find and print this minimum value.

#input Format

## The first line contains an integer  denoting the size of two arrays. 
##Each of the next two lines contains  space separated integers denoting array  and  respectively.

## Constraints: 2 <= n <= 10^5, 1 <= array elements <= 10^5

## Output Format: Print the minimum sum which can be obtained under the conditions mentioned in the problem statement.

## Observation: Note that instead of iteraitng through the full length of both arrays which takes O(n^2),
## we can sort the two arrays first. Then we simply take the first element of the two array if they don't happen to 
## have the same index. 

#!/bin/python3

import sys

def twinArrays(ar1, ar2):
    sorted_ar1 = sorted(ar1)
    sorted_ar2 = sorted(ar2)
    if ar1.index(sorted_ar1[0]) != ar2.index(sorted_ar2[0]):
        return sorted_ar1[0] + sorted_ar2[0]
    else:
        return min(sorted_ar1[0]+sorted_ar2[1], sorted_ar1[1]+sorted_ar2[0])
    

'''
def twinArrays(ar1, ar2):
    global_min = float('inf')

    for i in range(len(ar1)):
        for j in range(len(ar2)):
            if j != i:
                if ar1[i] + ar2[j] < global_min:
                    global_min = ar1[i] + ar2[j]
            else:
                pass
    return global_min
'''
n = int(input().strip())
ar1 = list(map(int, input().strip().split(' ')))
ar2 = list(map(int, input().strip().split(' ')))
result = twinArrays(ar1, ar2)
print(result)
