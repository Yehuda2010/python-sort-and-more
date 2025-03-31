from collections import defaultdict

class Graph:
    def __init__(self, n):
        self.n = n
        self.edges = defaultdict(list)

    def add_edge(self, u, v):
        if (0 <= u and u <= self.n-1) and (0 <= v and v <= self.n-1):
            if u not in self.edges[v]:
                self.edges[v].append(u)
            if v not in self.edges[u]:
                self.edges[u].append(v)
        else:
            print("numbers are not in range...")
    
    def print_edges(self):
        for k, v in self.edges.items():
            print(k, ":", v)
    
    def dfs(self, v, checked=[]):
        if 0 <= v and v <= self.n - 1:
            checked.append(v)
            print(v)
            for w in self.edges[v]:
                if w not in checked:
                    self.dfs(w, checked)
    
    def bfs(self, v):
        if 0 <= v and v <= self.n - 1:
            checked = []
            queue = [v]
            while queue:
                cur = queue.pop(0)
                if cur not in checked:
                    print(cur)
                    checked.append(cur)
                    for w in self.edges[cur]:
                        queue.append(w)
    
    def distance(self, u, v):
        if (0 <= u and u <= self.n - 1) and (0 <= v and v <= self.n - 1):
            dist = 0
            checked = []
            queue = [(u, dist)]
            while queue:
                cur, dist = queue.pop(0)
                if cur not in checked:
                    if cur == v:
                        return dist
                    checked.append(cur)
                    for w in self.edges[cur]:
                        queue.append((w, dist + 1))
            return float('inf')

    def distance2(self, u, v, checked=[], dist=0):
        if (0 <= u and u <= self.n - 1) and (0 <= v and v <= self.n - 1):
            if u == v:
                return dist
            checked.append(u)
            for w in self.edges[u]:
                if w not in checked:
                    result = self.distance2(w, v, checked, dist + 1)
                    if result is not None:
                        return result