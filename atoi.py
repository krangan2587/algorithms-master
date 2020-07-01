def atoi(string):
    num = 0
    sign = 1
    x = 0
    if(string[0] == '-'):
        sign = -1
        x = 1
    for i in range(x,len(string)):
        num = num * 10 + (ord(string[i]) - ord("0"))
    return sign * num

print(atoi("345"))