from src.core.floor_plan_loader import FloorPlanLoader
from src.core.pathfinding import PathFinder

def print_available_locations(indoor_map):
    """Print all available locations with their room codes"""
    print("\nAvailable Locations:")
    print("-" * 50)
    print(f"{'Room Code':<10} {'Location':<30} {'Type':<15}")
    print("-" * 50)
    
    for poi in indoor_map.floor_plan_data["points_of_interest"]:
        if "room_code" in poi:
            print(f"{poi['room_code']:<10} {poi['name']:<30} {poi['type']:<15}")
    print("-" * 50)

def find_path_with_direction(pathfinder, indoor_map, start_point, end_point):
    """Find and display path between two points"""
    print(f"\nFinding path from {start_point} to {end_point}...")
    
    start_location = indoor_map.points_of_interest[start_point]
    end_location = indoor_map.points_of_interest[end_point]
    
    path = pathfinder.find_path(start_location, end_location)
    
    if path:
        print(f"\nPath found ({len(path)} steps):")
        for i, location in enumerate(path):
            next_poi = next((poi["name"] for poi in indoor_map.floor_plan_data["points_of_interest"] 
                           if poi["x"] == location.x and poi["y"] == location.y), None)
            if next_poi:
                print(f"Step {i+1}: {next_poi}")
            else:
                print(f"Step {i+1}: Continue along corridor")
    else:
        print("\nNo path found")

def test_washroom_paths(pathfinder, indoor_map):
    """Test direct paths to washrooms"""
    print("\nTesting direct paths to washrooms:")
    
    scenarios = [
        ("Main Entrance", "Male Washroom"),
        ("Main Entrance", "Female Washroom"),
        ("Male Washroom", "Main Entrance"),
        ("Female Washroom", "Main Entrance")
    ]
    
    for start_point, end_point in scenarios:
        find_path_with_direction(pathfinder, indoor_map, start_point, end_point)

def main():
    # Load floor plan
    loader = FloorPlanLoader()
    indoor_map = loader.load_from_json('data/floor_plans/main_building_ground.json')
    
    # Initialize pathfinder
    pathfinder = PathFinder(indoor_map)
    
    # Print available locations
    print_available_locations(indoor_map)
    
    while True:
        print("\nNavigation Options:")
        print("1. Find path between two locations")
        print("2. Test washroom direct paths")
        print("3. Exit")
        
        choice = input("\nEnter your choice (1-3): ")
        
        if choice == "1":
            print("\nAvailable locations:")
            locations = list(indoor_map.points_of_interest.keys())
            for i, loc in enumerate(locations):
                print(f"{i+1}. {loc}")
            
            try:
                start_idx = int(input("\nEnter start location number: ")) - 1
                end_idx = int(input("Enter destination number: ")) - 1
                
                if 0 <= start_idx < len(locations) and 0 <= end_idx < len(locations):
                    find_path_with_direction(pathfinder, indoor_map, 
                                          locations[start_idx], 
                                          locations[end_idx])
                else:
                    print("Invalid location numbers!")
            except ValueError:
                print("Please enter valid numbers!")
                
        elif choice == "2":
            test_washroom_paths(pathfinder, indoor_map)
            
        elif choice == "3":
            print("\nThank you for using the navigation system!")
            break
            
        else:
            print("\nInvalid choice! Please try again.")

if __name__ == "__main__":
    main()