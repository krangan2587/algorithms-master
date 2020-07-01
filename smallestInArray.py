# O(n) solution for smallest number in array
def getSmallest(arr1):
    small = arr1[0]
    for i in arr1[1:]:
        if small < i:
            continue
        else:
            small = i
    return small
# O(n) solution for biggest number in array

def getLargest(arr1):
    big = arr1[0]
    for i in arr1[1:]:
        if big > i:
            continue
        else:
            big = i
    return big

if __name__ == '__main__':
    arr1 = [20,17,56,9,4,5]
    print(getSmallest(arr1))
    print(getLargest(arr1))
