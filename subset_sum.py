#This function is an recursive approach for the subset problem.There is another top down /recursive way to do this which will be presented
#in an upcoming module

def issubset_sum(arr , sum):
    rem_sum = sum
    if rem_sum == 0:
        return True
    for index,ele in enumerate(arr):
        if ele <= rem_sum:
            rem_sum = rem_sum - ele
            if index == len(arr) - 1 and rem_sum !=0:
                return False
            r_status = issubset_sum(arr[index+1:],rem_sum)
            if r_status is True:
                break
            else:
                rem_sum = rem_sum + ele
        else:
            r_status = False

    return r_status

if __name__ == '__main__':
    arr = [3,34,4,12,5,2]
    sum = 33
    status = issubset_sum(arr,sum)
    print(status)