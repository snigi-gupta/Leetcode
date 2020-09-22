import heapq
import collections
class Connections:
    def __init__(self, first, second, cost):
        self.firstTown = first
        self.secondTown = second
        self.cost = cost
    def __repr__(self):
        return self.firstTown + " " + self.secondTown + " " + self.cost

class Solution:
    def minimumCost(self, N, connections):
        weight = 0
        # allCities = set([i for i in range(1, N + 1)])
        uniqueTowns = {}
        count = 0
        for city in connections:
            if city.firstTown not in uniqueTowns:
                uniqueTowns[city.firstTown] = 0
                count += 1
            if city.secondTown not in uniqueTowns:
                uniqueTowns[city.secondTown] =0
                count += 1
        heap = []
        graph = collections.defaultdict(list)
        for x in connections:
            graph[x.firstTown].append((x.secondTown, x.cost, x))
            graph[x.secondTown].append((x.firstTown, x.cost, x))
        for v, d, obj in graph[connections[0].firstTown]:  # start from any random start node
            heapq.heappush(heap, (d, connections[0].firstTown, v, obj))
        res = []
        while heap:
            w, u, v, obj = heapq.heappop(heap)
            if v not in uniqueTowns:
                continue
            # weight += w
            res.append(obj)
            if u in uniqueTowns:
                del uniqueTowns[u]
            if v in uniqueTowns:
                del uniqueTowns[v]
            for n, d, obj1 in graph[v]:
                heapq.heappush(heap, (d, v, n, obj1))
        if uniqueTowns:
            return []

        # return res
        for c in res:
            print(c.firstTown, c.secondTown, c.cost)

if __name__ == "__main__":
    num = 5 #edges
    connections = []
    conn = Connections("Town A", "Town B", 1)
    connections.append(conn)
    conn = Connections("Town B", "Town C", 4)
    connections.append(conn)
    conn = Connections("Town B", "Town D", 6)
    connections.append(conn)
    conn = Connections("Town D", "Town E", 5)
    connections.append(conn)
    conn = Connections("Town C", "Town E", 1)
    connections.append(conn)

    sol = Solution()
    sol.minimumCost(num, connections)


