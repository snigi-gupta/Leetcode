# import heapq
import collections
class Connections:
    def __init__(self, first, second, cost):
        self.firstTown = first
        self.secondTown = second
        self.cost = cost
    def __repr__(self):
        return self.firstTown + " " + self.secondTown + " " + self.cost


class Heap:
    def __init__(self):
        self.minHeap = ['heap']

    def insert(self,edge):
        # edge = (weight, destination)
        self.minHeap.append(edge)
        child = len(self.minHeap) - 1
        parent = child // 2
        while(parent >= 1):
            if(self.minHeap[child][0] < self.minHeap[parent][0]):
                self.minHeap[child],self.minHeap[parent] = self.minHeap[parent],self.minHeap[child]
                child = parent
                parent = parent // 2
            else:
                break
    def getMin(self):
        self.minHeap[-1],self.minHeap[1] = self.minHeap[1],self.minHeap[-1]
        min = self.minHeap.pop()
        parent = 1
        l_child = parent * 2
        r_child = parent * 2 + 1
        while(l_child < len(self.minHeap)):
            if(r_child > len(self.minHeap) - 1):
                child_index = l_child
            elif(self.minHeap[l_child][0] < self.minHeap[r_child][0]):
                child_index = l_child
            else:
                child_index = r_child
            if(self.minHeap[parent][0] <= self.minHeap[child_index][0]):
                break
            self.minHeap[parent],self.minHeap[child_index] = self.minHeap[child_index],self.minHeap[parent]
            parent = child_index
            l_child = parent * 2
            r_child = parent * 2 + 1

        return min

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
        # heap = []
        hp = Heap()
        # import pdb; pdb.set_trace();
        # print(hp.minHeap)
        graph = collections.defaultdict(list)
        for x in connections:
            graph[x.firstTown].append((x.secondTown, x.cost, x))
            graph[x.secondTown].append((x.firstTown, x.cost, x))
        for v, d, obj in graph[connections[0].firstTown]:  # start from any random start node
            hp.insert((d, connections[0].firstTown, v, obj))
        res = []
        while len(hp.minHeap) > 1:
            w, u, v, obj = hp.getMin()
            if v not in uniqueTowns:
                continue
            # weight += w
            res.append(obj)
            if u in uniqueTowns:
                del uniqueTowns[u]
            if v in uniqueTowns:
                del uniqueTowns[v]
            for n, d, obj1 in graph[v]:
                hp.insert((d, v, n, obj1))
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
    conn = Connections("Town B", "Town D", 5)
    connections.append(conn)
    conn = Connections("Town D", "Town E", 5)
    connections.append(conn)
    # conn = Connections("Town C", "Town E", 1)
    # connections.append(conn)

    sol = Solution()
    sol.minimumCost(num, connections)


