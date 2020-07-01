def reverse_list(num_list,start,end):
    while(start < end):
        temp = num_list[start]
        num_list[start] = num_list[end]
        num_list[end] = temp
        start = start + 1
        end = end - 1
    return num_list

def reverse_words(word_list):
    reversed_list = reverse_list(word_list,0,len(word_list) - 1)
    print(reversed_list)
    start = 0
    for i in range(len(reversed_list) + 1):
        if i == len(reversed_list) or reversed_list[i] == ' ':
            end = i - 1
            reverse_list(reversed_list,start, end)
            start = i + 1
    return reversed_list


if __name__ == '__main__':
    word_list = ['C','A','K','E',' ','P','O','U','N','D',' ','S','T','E','A','L']
    #print(word_list)
    #result = reverse_words(word_list)
    #print(''.join(result))
    result = reverse_words(word_list)
    print(''.join(result))
