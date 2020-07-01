def minimumTime(numparts,parts):
    if numparts == 0:
        return 0
    if numparts == 1:
        return parts[0]
    if numparts == 2:
        result = parts[0] + parts[1]
        return result
    sortedList = sorted(parts)
    newlist = []
    newlist.append(sortedList[0] + sortedList[1])
    newlist.extend(sortedList[2:])
    return minimumTime(len(newlist),newlist)

def main():
    mintime =minimumTime(4,[12,8,10,20])
    print(mintime)

if __name__ == '__main__':
    main()