from weighted_graph import WGraph
def main():
    wg = WGraph(5)
    wg.add_edge(0,1,1)
    wg.add_edge(1,2,2)
    wg.add_edge(2,3,3)
    wg.add_edge(3,4,4)
    wg.print_edges()
    print(wg.dijkstra(0,4))

if __name__ == "__main__":
    main()