def calculate_islands(dimensions, matrix):
    M, N = dimensions
    is_visited = [[False] * N for _ in range(M)]
    islands_count = 0
    
    for i in range(M):
        for j in range(N):
            if matrix[i][j]==1 and not is_visited[i][j]:
                stack = [(i, j)]
                while stack:
                    row, col = stack.pop()
                    if 0 <= row < M and 0 <= col < N and matrix[row][col]==1 and not is_visited[row][col]:
                        is_visited[row][col] = True
                        stack.append((row+1, col))
                        stack.append((row-1, col))
                        stack.append((row, col+1))
                        stack.append((row, col-1))
                islands_count += 1
                
    return islands_count

test_cases = [
    ([3, 3], [
        [0, 1, 0],
        [0, 0, 0],
        [0, 1, 1]
    ]),
    ([3, 4], [
        [0, 0, 0, 1],
        [0, 0, 1, 0],
        [0, 1, 0, 0]
    ]),
    ([3, 4], [
        [0, 0, 0, 1],
        [0, 0, 1, 1],
        [0, 1, 0, 1]
    ]),
]

for dimensions, matrix in test_cases:
    print(calculate_islands(dimensions, matrix))
