class DayNightMode:
    def __init__(self):
        self.current_time = "day"  # Default

    def set_time(self, choice):
        """Set time based on player choice"""
        if choice.lower() in ["day", "night"]:
            self.current_time = choice.lower()
            print(f"It is now {self.current_time}.")
        else:
            print("Invalid choice! Please enter 'day' or 'night'.")

    # returns the XP multiplier for the current slot
    def xp_bonus(self):
        return 1.5 if self.current_time == "night" else 1.0

    # flip the time of day in one call
    def toggle(self):
            self.current_time = "night" if self.current_time == "day" else "day"
            print(f"\n🌗  It is now {self.current_time.upper()}.")

    # how many things the player may do in the current time‑slot
    def actions_allowed(self):
        return 3 if self.current_time == "day" else 4

    def apply_day_night_effects(self, player, monster):
        """Applies effects based on the time of day."""
        if self.current_time == "night":
            monster.attack *= 1.2  # Monster + 20% 
            monster.defense *= 1.2
            monster.health *= 1.2
            player.attack *= 0.9  # Player - 10% 
            player.defense *= 0.9
            player.health *= 0.9
        else:  # Day
            monster.attack *= 0.8  # Monster - 20% 
            monster.defense *= 0.8
            monster.health *= 0.8
            player.attack *= 1.1  # Player + 10% 
            player.defense *= 1.1
            player.health *= 1.1

    def is_shop_open(self):
        """Checks if the shop is open."""
        return self.current_time == "day"