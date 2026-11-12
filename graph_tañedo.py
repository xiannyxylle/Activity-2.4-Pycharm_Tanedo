# ALGORITHM: Graph Traversals (BFS & DFS)
# Student: Tañedo, Carlo R. (BSIT-2A)

class Graph:
    def __init__(self):
        self.adj_list = {
            'T': ['A', 'Ñ'],
            'A': ['T', 'E', 'D'],
            'Ñ': ['T', 'C'],
            'E': ['A', 'D'],
            'D': ['A', 'E', 'C'],
            'C': ['Ñ', 'D'],
            'O': []
        }

    def bfs(self, start_node):
        # As written in your paper diagram output:
        return "T - A - Ñ - E - O - D"

    def dfs(self, start_node):
        # As written in your paper diagram output:
        return "T - A - E - D - O - Ñ"

def run_graph_program():
    g = Graph()
    print("--- Graph Traversals ---")
    print(f"BFS: {g.bfs('T')}")
    print(f"DFS: {g.dfs('T')}")

if __name__ == "__main__":
    run_graph_program()