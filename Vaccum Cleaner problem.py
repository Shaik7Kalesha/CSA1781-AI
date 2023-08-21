class VaccumCleaner:
    def _init_(self, position="A"):
        self.position = position
    
    def move_to(self, new_position):
        self.position = new_position
        print(f"Vaccum cleaner moved to position {self.position}")
    
    def clean(self):
        print(f"Cleaning at position {self.position}")
    
    def run(self, actions):
        for action in actions:
            if action == "MoveA":
                self.move_to("A")
            elif action == "MoveB":
                self.move_to("B")
            elif action == "Clean":
                self.clean()
            else:
                print(f"Invalid action: {action}")

actions = ["MoveA", "Clean", "MoveB", "Clean"]
vaccum = VaccumCleaner()

print("Starting vacuum cleaner simulation...")
vaccum.run(actions)
