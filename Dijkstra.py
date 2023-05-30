

import heapq

class Edge:
    def __init__(self, weight, start_vertex, target_vertex):
        self.weight = weight
        self.start_vertex = start_vertex
        self.target_vertex = target_vertex

class Node:
    def __init__(self, name):
        self.name = name
        self.visited = False
        self.predecessor = None
        self.neighbors = []
        self.min_distance = float("inf")
    
    def __lt__(self, other_node):
        return self.min_distance < other_node.min_distance
    
    def add_edge(self, point, weight, destination_vertex, destination):
        
        edge = Edge(weight, self, destination_vertex)
        self.neighbors.append(edge)
        print(f"{point} --> {destination} : {weight} KM")

class Dijkstra:
    def __init__(self):
        self.heap = []
    
    def calculate(self, start_vertex, start_point ):
        start_vertex.min_distance = 0
        heapq.heappush(self.heap, start_vertex)
        print(f"Point medan perang di {start_point}")
        
        while self.heap:
            actual_vertex = heapq.heappop(self.heap)
            if actual_vertex.visited:
                continue
            for edge in actual_vertex.neighbors:
                start = edge.start_vertex
                target = edge.target_vertex
                new_distance = start.min_distance + edge.weight
                if new_distance < target.min_distance:
                    target.min_distance = new_distance
                    target.predecessor = start
                    heapq.heappush(self.heap, target)
            actual_vertex.visited = True
    
    def get_shortest_path(self, vertex, start_point):
       
        print(f"Markas di titik {start_point}")
        print(f"Jalur terpendek yang ditempuh sejauh {vertex.min_distance} KM")
        actual_vertex = vertex
        print(f"Jalur yang harus ditempuh pasukan yaitu : ")
        while actual_vertex is not None:
            print(f"{actual_vertex.name}", end=" ")
            actual_vertex = actual_vertex.predecessor
        






