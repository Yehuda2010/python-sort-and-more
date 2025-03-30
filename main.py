from graph import Graph

def main():
    g = Graph(13)
    g.add_edge(0,1)
    g.add_edge(0,2)
    g.add_edge(1,3)
    g.add_edge(1,4)
    g.add_edge(2,5)
    g.add_edge(2,6)
    g.add_edge(3,7)
    g.add_edge(3,8)
    g.add_edge(4,9)
    g.add_edge(4,10)
    g.add_edge(5,11)
    g.add_edge(5,12)
    g.print_edges()
    print()
    g.dfs(0)
    print()
    g.bfs(0)

if __name__ == "__main__":
    main()