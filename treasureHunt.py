import queue
def minDistance(numrows,numcols,lot):
    dirsteps = [[1,0],[-1,0],[0,1],[0,-1]]
    return calcMindistance(0,0,lot,0,dirsteps)

def calcMindistance(row,col,lot,cursteps,dirsteps):
    if len(lot) == 0 or lot[row][col] == 1:
        return -1
    if lot[row][col] == 9:
        return cursteps
    q = queue.Queue()
    q.put([0,0])
    lot[0][0] = 1
    while not q.empty():
        for i in range(q.qsize()):
            pos = q.get()
            for c in dirsteps:
                x = pos[0] + c[0]
                y = pos[1] + c[1]
                if x < 0 or x > len(lot)-1 or y < 0 or y > len(lot[0])-1 or lot[x][y] == 1:
                    continue
                if lot[x][y] == 9:
                    return cursteps + 1
                q.put([x,y])
                lot[x][y] = 1

        cursteps = cursteps + 1


def main():
    # 0 is flat,1 is dangerous and 9 is the treasure
    island = [[0, 0, 0, 0],
              [1, 0, 1, 0],
              [0, 0, 0, 0],
              [9, 1, 0, 0]]
    steps  =minDistance(4,4,island)
    print(steps)

if __name__ == '__main__':
    main()

#this follows BFS and counts the levels that it visits until it gets the destination
# 0,0 ---> 0
# 0,1 --->1
# 1,1 and 0,2 --->2
# 2,1 and 0,3 ----> 3
# 2,0 2,2 and 1,3 ---> 4
# 3,0 ----> 5