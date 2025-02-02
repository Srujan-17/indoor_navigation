import json
from typing import Dict
from .location import Location
from .map import IndoorMap

class FloorPlanLoader:
    def __init__(self):
        self.indoor_map = IndoorMap()

    def load_from_json(self, file_path: str) -> IndoorMap:
        """Load floor plan from a JSON file"""
        with open(file_path, 'r') as f:
            data = json.load(f)
            
        # Store the raw data for reference
        self.indoor_map.floor_plan_data = data
            
        # Load points of interest
        for poi in data.get('points_of_interest', []):
            location = Location(
                x=poi['x'],
                y=poi['y'],
                floor=data.get('floor', 0)
            )
            self.indoor_map.add_point_of_interest(poi['name'], location)
            
        # Load walkable paths
        for path in data.get('walkable_paths', []):
            start = Location(
                x=path['start']['x'],
                y=path['start']['y'],
                floor=data.get('floor', 0)
            )
            end = Location(
                x=path['end']['x'],
                y=path['end']['y'],
                floor=data.get('floor', 0)
            )
            self.indoor_map.add_path(start, end)
            
        return self.indoor_map