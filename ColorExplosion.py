def solution(bubbles):
    eligible = set()
    for i in range(len(bubbles)):
        for j in range(len(bubbles[0])):
            pending_eligible = set()
            x = bubbles[i][j]
            count = 0
            pending_eligible.add((i, j))
            for a, b in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                if 0 <= i+a < len(bubbles) and 0 <= j+b < len(bubbles[0]) and bubbles[i+a][j+b] == x:
                    count += 1
                    pending_eligible.add((i+a, j+b))

            if count >= 2:
                eligible.update(pending_eligible)

    for i, j in eligible:
        bubbles[i][j] = 0

    for i in range(len(bubbles)-1, -1, -1):
        for j in range(len(bubbles[0])-1, -1, -1):
            z = i
            while z < len(bubbles)-1 and bubbles[z+1][j] == 0:
                temp = bubbles[z][j]
                bubbles[z][j] = 0
                bubbles[z+1][j] = temp
                z += 1
    return bubbles


bubbles = [[2, 3, 0, 0, 0],
           [3, 3, 3, 0, 0],
           [2, 3, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [2, 3, 0, 0, 0]]
resssss = [[0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [2, 0, 0, 0, 0],
           [2, 0, 0, 0, 0],
           [2, 3, 0, 0, 0]]
print(solution(bubbles))
