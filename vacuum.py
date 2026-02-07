class RationalVacuumAgent:
    def __init__(self):
        # Environment configuration from Figure 1
        # 4x4 grid with specific dirt locations marked
        self.locations = [
            ['A', 'B', 'C', 'D'],
            ['E', 'F', 'G', 'H'],
            ['I', 'J', 'K', 'L'],
            ['M', 'N', 'O', 'P']
        ]
        
        # Dirt configuration from the problem statement
        # Dirty locations: B, C, E, G, H, I, K, M, O, P
        self.dirt_status = {
            'A': False, 'B': True,  'C': True,  'D': False,
            'E': True,  'F': False, 'G': True,  'H': True,
            'I': True,  'J': False, 'K': True,  'L': False,
            'M': True,  'N': False, 'O': True,  'P': True
        }
        
        # Map location to coordinates for movement
        self.location_coords = {}
        for row in range(4):
            for col in range(4):
                loc = self.locations[row][col]
                self.location_coords[loc] = (row, col)
        
        # Agent state initialization
        self.current_loc = 'A'  # Starting position
        self.energy = 100
        self.bag_load = 0
        self.bag_capacity = 10
        self.total_dirty = sum(1 for status in self.dirt_status.values() if status)
        self.cleaned = 0
        self.visited = {'A'}  # Track visited locations
        self.action_count = 0
        self.goal_achieved = False
        
        # Statistics
        self.moves_made = 0
        self.sucks_made = 0
        self.empty_actions = 0
    
    # Main decision function based on Figure 2 logic
    def decide_action(self):
        # Check goal condition first
        if self.is_goal_achieved():
            return "GOAL_ACHIEVED"
        
        # Check energy
        if self.energy <= 0:
            return "OUT_OF_ENERGY"
        
        # Check if bag needs emptying
        if self.bag_load >= self.bag_capacity:
            if self.current_loc == 'A':
                return "EMPTY_BAG"
            else:
                return self.get_path_home()
        
        # Check current location status
        current_dirty = self.dirt_status[self.current_loc]
        
        # Decision logic based on Figure 2 percept-action pairs
        if current_dirty:
            return "SUCK"
        else:
            # Need to move to next dirty location
            next_target = self.find_next_dirty_location()
            if next_target:
                return self.get_movement_direction(next_target)
            else:
                # All dirt cleaned, return home
                return self.get_path_home()
    
    # Find the next dirty location to clean
    def find_next_dirty_location(self):
        dirty_locs = [loc for loc, dirty in self.dirt_status.items() if dirty]
        
        if not dirty_locs:
            return None  # No more dirt
        
        # Find the closest dirty location using Manhattan distance
        current_row, current_col = self.location_coords[self.current_loc]
        closest_loc = None
        min_distance = float('inf')
        
        for loc in dirty_locs:
            row, col = self.location_coords[loc]
            distance = abs(row - current_row) + abs(col - current_col)
            if distance < min_distance:
                min_distance = distance
                closest_loc = loc
        
        return closest_loc
    
    # Determine movement direction to reach target
    def get_movement_direction(self, target):
        if self.current_loc == target:
            return "SUCK"  # Shouldn't happen, but safety check
        
        curr_row, curr_col = self.location_coords[self.current_loc]
        target_row, target_col = self.location_coords[target]
        
        # Determine optimal direction (prioritize horizontal then vertical)
        if curr_col < target_col:
            return "MOVE_EAST"
        elif curr_col > target_col:
            return "MOVE_WEST"
        elif curr_row < target_row:
            return "MOVE_SOUTH"
        else:
            return "MOVE_NORTH"
    
    # Get path back to home (location A)
    def get_path_home(self):
        if self.current_loc == 'A':
            if self.bag_load >= self.bag_capacity:
                return "EMPTY_BAG"
            else:
                return "WAIT"  # Already home with non-full bag
        
        # Calculate direction to home
        return self.get_movement_direction('A')
    
    # Execute the chosen action
    def execute_action(self, action):
        if self.energy <= 0:
            return False
        
        # Deduct energy for any action
        self.energy -= 1
        self.action_count += 1
        
        if action == "SUCK":
            if self.dirt_status[self.current_loc]:
                self.dirt_status[self.current_loc] = False
                self.bag_load += 1
                self.cleaned += 1
                self.sucks_made += 1
                print(f"  Cleaned {self.current_loc}, Bag: {self.bag_load}/{self.bag_capacity}")
        
        elif action == "EMPTY_BAG":
            if self.current_loc == 'A':
                self.bag_load = 0
                self.empty_actions += 1
                print(f"  Emptied bag at home")
        
        elif action.startswith("MOVE_"):
            direction = action.split("_")[1]
            self.move_agent(direction)
            self.moves_made += 1
        
        elif action == "GOAL_ACHIEVED":
            self.goal_achieved = True
            return False
        
        return True
    
    # Move agent in specified direction
    def move_agent(self, direction):
        curr_row, curr_col = self.location_coords[self.current_loc]
        
        if direction == "NORTH" and curr_row > 0:
            self.current_loc = self.locations[curr_row-1][curr_col]
        elif direction == "SOUTH" and curr_row < 3:
            self.current_loc = self.locations[curr_row+1][curr_col]
        elif direction == "EAST" and curr_col < 3:
            self.current_loc = self.locations[curr_row][curr_col+1]
        elif direction == "WEST" and curr_col > 0:
            self.current_loc = self.locations[curr_row][curr_col-1]
        
        self.visited.add(self.current_loc)
    
    # Check if goal is achieved
    def is_goal_achieved(self):
        # All conditions from problem:
        # 1. All locations clean
        # 2. Agent at home (A)
        # 3. Bag empty (implied by problem statement)
        
        all_clean = not any(self.dirt_status.values())
        at_home = (self.current_loc == 'A')
        
        return all_clean and at_home and self.bag_load == 0
    
    # Visualize current state
    def display_state(self):
        print("\n" + "="*50)
        print(f"Step {self.action_count}: Agent at {self.current_loc}")
        print(f"Energy: {self.energy}, Bag: {self.bag_load}/{self.bag_capacity}")
        print(f"Cleaned: {self.cleaned}/{self.total_dirty} dirty locations")
        
        # Display grid
        print("\nCurrent Grid Status:")
        for row in range(4):
            row_display = []
            for col in range(4):
                loc = self.locations[row][col]
                status = "D" if self.dirt_status[loc] else "C"
                agent = "*" if loc == self.current_loc else " "
                row_display.append(f"{loc}{status}{agent}")
            print(" ".join(row_display))
        print("="*50)
    
    # Main execution loop
    def run(self):
        print("="*60)
        print("RATIONAL VACUUM AGENT SIMULATION")
        print("="*60)
        print("Starting at location A with 100 energy")
        print(f"Total dirty locations: {self.total_dirty}")
        print("Dirty locations: B, C, E, G, H, I, K, M, O, P")
        print("="*60)
        
        self.display_state()
        
        while self.energy > 0 and not self.goal_achieved:
            # Get decision
            action = self.decide_action()
            
            if action in ["GOAL_ACHIEVED", "OUT_OF_ENERGY"]:
                print(f"\nTerminating: {action}")
                break
            
            print(f"\nAction: {action}")
            
            # Execute action
            if not self.execute_action(action):
                break
            
            # Display new state
            self.display_state()
        
        # Final report
        self.generate_report()
    
    # Generate final performance report
    def generate_report(self):
        print("\n" + "="*60)
        print("FINAL PERFORMANCE REPORT")
        print("="*60)
        print(f"Goal Achieved: {'YES' if self.goal_achieved else 'NO'}")
        print(f"Energy Remaining: {self.energy}/100")
        print(f"Total Actions: {self.action_count}")
        print(f"  Moves: {self.moves_made}")
        print(f"  Clean Actions: {self.sucks_made}")
        print(f"  Empty Actions: {self.empty_actions}")
        print(f"Locations Cleaned: {self.cleaned}/{self.total_dirty}")
        print(f"Bag Emptied: {self.empty_actions} time(s)")
        print(f"Visited Locations: {len(self.visited)}/16")
        
        # Calculate efficiency
        if self.goal_achieved:
            efficiency = (self.total_dirty * 10) - self.action_count
            print(f"\nPerformance Score: {efficiency} "
                  f"(Clean: +{self.total_dirty*10}, Actions: -{self.action_count})")
        
        print("="*60)

# Simulation runner
def simulate_agent():
    agent = RationalVacuumAgent()
    agent.run()

if __name__ == "__main__":
    simulate_agent()