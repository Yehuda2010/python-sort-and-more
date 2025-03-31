from collections import defaultdict
import heapq

class WGraph:
    def __init__(self, n):
        self.n = n
        self.edges = defaultdict(list)

    def add_edge(self, u, v, weight=1):
        if (0 <= u and u <= self.n-1) and (0 <= v and v <= self.n-1):
            if u not in self.edges[v]:
                self.edges[v].append((u, weight))
            if v not in self.edges[u]:
                self.edges[u].append((v, weight))
        else:
            print("numbers are not in range...")
    
    def print_edges(self):
        for k, v in self.edges.items():
            print(k, ":", v)
    
    def dijkstra(self, start, target):
        priority_queue = [(0, start)]
        distances = {i : float('inf') for i in range(self.n)}
        distances[start] = 0
        while priority_queue:
            cur_distance, cur_node = heapq.heappop(priority_queue)
            if cur_node == target:
                return distance
            for neighbor, weight in self.edges[cur_node]:
                distance = cur_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))
        return None
    
