from typing import List, Optional
from .location import Location
from .map import IndoorMap
from ..utils.graph import Graph

class PathFinder:
    def __init__(self, indoor_map: IndoorMap):
        self.map = indoor_map
        self.graph = self._build_graph()
        
    def _build_graph(self) -> Graph[Location]:
        graph = Graph[Location]()
        
        # Add all locations as vertices first
        for location in self.map.points_of_interest.values():
            graph.add_vertex(location)
            
        # Add all paths
        for start, end in self.map.walkable_paths:
            # Create new Location objects with same coordinates
            start_loc = Location(start.x, start.y, start.floor)
            end_loc = Location(end.x, end.y, end.floor)
            
            # Add vertices if they don't exist
            graph.add_vertex(start_loc)
            graph.add_vertex(end_loc)
            
            # Add the edge
            graph.add_edge(start_loc, end_loc)
            
        return graph
        
    def find_path(self, start: Location, end: Location) -> Optional[List[Location]]:
        """
        Find a path between start and end locations using BFS
        Returns None if no path is found
        """
        if start.floor != end.floor:
            return None
            
        # Create new Location objects with same coordinates
        start_loc = Location(start.x, start.y, start.floor)
        end_loc = Location(end.x, end.y, end.floor)
        
        visited = set()
        queue = [[start_loc]]
        
        while queue:
            path = queue.pop(0)
            node = path[-1]
            
            if node == end_loc:
                return path
                
            if node not in visited:
                visited.add(node)
                for neighbor in self.graph.edges.get(node, []):
                    if neighbor not in visited:
                        new_path = list(path)
                        new_path.append(neighbor)
                        queue.append(new_path)
        
        return None