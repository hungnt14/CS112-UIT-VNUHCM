n = int(input())
cost = [list(map(int, input().split())) for _ in range(n)]
visitedCity = [0 for _ in range(n)]

def GoGoGooooooooooooooooo(currentCity, totalVisitedCity):
    if (totalVisitedCity == n):
        return cost[currentCity][0]
    
    minCost = 99999999999999
    for i in range(n):
        if (not visitedCity[i] and cost[currentCity][i] < minCost):
            visitedCity[i] = True
            minCost = min(minCost, GoGoGooooooooooooooooo(i, totalVisitedCity + 1) + cost[currentCity][i])
            visitedCity[i] = False
    return minCost

visitedCity[0] = 1
print(GoGoGooooooooooooooooo(0, 1))