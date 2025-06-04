import Queue
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []
        for i in range(vertices):
            self.graph.append([])
        

    def add_edge(self, frm, to, bidirectional=True):
        self.graph[frm].append(to)
        if bidirectional == True:
            self.graph[to].append(frm)
    
    def print_graph(self):
        for i in range(self.V):
            print(f"{i} -> ", end="")
            for j in self.graph[i]:
                print(f"{j} ", end="")
            print()

    def neighbors(self, vertex):
        return self.graph[vertex]
    
    def bfs(self, source):
        queue = Queue.Queue()
        flag = [0] * self.V

        queue.enqueue(source)
        flag[source] = 1

        while not queue.isEmpty():
            current_node = queue.dequeue()

            print(current_node, end=" ")

            neighbors_of_current_node = self.neighbors(current_node)
            for neighbor in neighbors_of_current_node:
                if flag[neighbor] == 0:
                    queue.enqueue(neighbor)
                    flag[neighbor] = 1

        
graph = Graph(6)
graph.add_edge(0, 2, bidirectional=False)
graph.add_edge(0, 1, bidirectional=False)
graph.add_edge(1, 2, bidirectional=False)
graph.add_edge(1, 3, bidirectional=False)
graph.add_edge(2, 3, bidirectional=False)
graph.add_edge(3, 4, bidirectional=False)
graph.add_edge(5, 3, bidirectional=False)
graph.add_edge(5, 4, bidirectional=False)

graph.bfs(0)