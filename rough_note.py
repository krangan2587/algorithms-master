def func2(M):
    from collections import deque
    q = deque()
    q.append((0, 0))
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    steps = 0
    visited = set()
    visited.add((0, 0))
    while q:
        for i in range(len(q)):
            node = q.popleft()
            x, y = node[0], node[1]

            if M[x][y] == 'X':
                return steps

            for dir in dirs:  # inseatd of looping over d[node]
                newX, newY = x + dir[0], y + dir[1]
                # check bounds:
                if newX >= 0 and newX <= len(M) - 1 and newY >= 0 and newY <= len(M[0]) - 1:
                    # check cell:
                    if M[newX][newY] != 'D':
                        # check if visited:
                        if (newX, newY) not in visited:
                            q.append((newX, newY))
                            visited.add((newX, newY))
        steps += 1
    return steps


M = [['O', 'O', 'O', 'O'], ['D', 'O', 'D', 'O'], ['O', 'O', 'O', 'O'], ['X', 'D', 'D', 'O']]
print('>> Using dirs and BFS <<')
print(func2(M))