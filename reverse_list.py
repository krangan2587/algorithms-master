def reverse_list(num_list):
    start = 0
    end = len(num_list) - 1
    while(start < end):
        temp = num_list[start]
        num_list[start] = num_list[end]
        num_list[end] = temp
        start = start + 1
        end = end - 1
    return num_list

if __name__ == '__main__':
    num_list = [45,10,5,34,23,8]
    list_str = ['K','A','S','T','U','R','I']
    print(reverse_list(num_list))
    print(reverse_list(list_str))