# Given an array A[] and a number x, check for pair in A[] with sum as x

# Solution 1 - Complexity - O(n2)
def get_pair_count_1(arr, sum):
    count = 0
    size = len(arr)
    for i in range(size):
        for j in range(i+1, size):
            if arr[i] + arr[j] == sum:
                count += 1
    return count

# Solution 2 - Complexity - O(n)
def get_pair_count_2(arr, sum):
    count = 0
    temp_arr = [0] * 1000
    size = len(arr)

    for i in range(size):
        temp_arr[arr[i]] = arr[i]

    size = len(temp_arr)
    for i in range(size):
        val = sum - temp_arr[i]
        if temp_arr[val] !=0:
            count += 1
    return count/2
if __name__ == '__main__':
    a = [1,5,7,-1]
    print get_pair_count_1(a, 6)
    print get_pair_count_2(a, 6)