class Location:
    def __init__(self, x: float, y: float, floor: int = 0):
        self.x = x
        self.y = y
        self.floor = floor
        
    def distance_to(self, other: 'Location') -> float:
        """Calculate Euclidean distance to another location on the same floor"""
        if self.floor != other.floor:
            raise ValueError("Cannot calculate distance between different floors")
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5
    
    def __eq__(self, other: object) -> bool:
        """Override equality comparison"""
        if not isinstance(other, Location):
            return False
        return (self.x == other.x and 
                self.y == other.y and 
                self.floor == other.floor)
    
    def __hash__(self) -> int:
        """Make Location hashable for use as dictionary key"""
        return hash((self.x, self.y, self.floor))
    
    def __str__(self):
        return f"Location(x={self.x}, y={self.y}, floor={self.floor})"