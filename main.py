from graph import Graph

def main():
    g = Graph(5)
    g.add_edge(0,1)
    g.add_edge(1,2)
    g.add_edge(2,3)
    g.add_edge(3,4)
    g.add_edge(4,0)
    g.print_edges()
    g.dfs(0)

if __name__ == "__main__":
    main()