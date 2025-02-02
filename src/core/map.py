from typing import Dict, List
from .location import Location

class IndoorMap:
    def __init__(self):
        self.points_of_interest: Dict[str, Location] = {}
        self.walkable_paths: List[tuple[Location, Location]] = []
        self.floor_plan_data: Dict = {}  # Add this line
        
    def add_point_of_interest(self, name: str, location: Location):
        """Add a named point of interest to the map"""
        self.points_of_interest[name] = location
        
    def add_path(self, start: Location, end: Location):
        """Add a walkable path between two locations"""
        self.walkable_paths.append((start, end))