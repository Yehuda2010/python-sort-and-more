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
        print(self.edges)