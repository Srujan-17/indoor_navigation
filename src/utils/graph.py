from typing import Dict, List, TypeVar, Generic

T = TypeVar('T')

class Graph(Generic[T]):
    def __init__(self):
        self.edges: Dict[T, List[T]] = {}
        
    def add_vertex(self, vertex: T):
        if vertex not in self.edges:
            self.edges[vertex] = []
            
    def add_edge(self, v1: T, v2: T):
        self.add_vertex(v1)
        self.add_vertex(v2)
        self.edges[v1].append(v2)
        self.edges[v2].append(v1)  # Undirected graph