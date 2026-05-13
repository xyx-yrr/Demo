graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

n = 4
visited = [False] * n

city = 0
visited[city] = True

cost = 0
path = [city]

for i in range(n - 1):

    min_cost = 999
    next_city = -1

    for j in range(n):

        if not visited[j] and graph[city][j] < min_cost:
            min_cost = graph[city][j]
            next_city = j

    visited[next_city] = True
    path.append(next_city)

    cost += min_cost
    city = next_city

cost += graph[city][0]
path.append(0)

print("Path:", path)
print("Cost:", cost)