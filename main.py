from graph import Graph

def main():
    g = Graph(10)
    g.add_edge(1,2)
    g.add_edge(2,3)
    g.add_edge(3,4)
    g.add_edge(3,4)
    g.add_edge(-1,2)
    g.print_edges()
if __name__ == "__main__":
    main()