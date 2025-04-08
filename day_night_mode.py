class DayNightMode:
    def __init__(self):
        self.current_time = "day"  # Default value

    def set_time(self, choice):
        """Set the time of day based on the player's choice."""
        
        if choice.lower() in ["day", "night"]:
            self.current_time = choice.lower()
            print(f"It is now {self.current_time}.")
        else:
            print("Invalid choice! Please enter 'day' or 'night'.")
            
    def xp_bonus(self):
        return 1.5 if self.current_time == "night" else 1.0

    def toggle(self):
        self.current_time = "night" if self.current_time == "day" else "day"
        print(f"\n🌗  It is now {self.current_time.upper()}.")

    def actions_allowed(self):
        return 3 if self.current_time == "day" else 4

    def apply_day_night_effects(self, player, monster):
        """
        Applies the day/night effects using the base attributes to avoid cumulative modifications.
        If 'player' is None, only the monster's attributes are adjusted.
        """
        if self.current_time == "night":
            # Monster: +20% effect
            monster.health = int(monster.base_health * 1.2)
            monster.attack = int(monster.base_attack * 1.2)
            monster.defense = int(monster.base_defense * 1.2)
            # Player: -10% effect
            if player:
                player.attack = int(player.base_attack * 0.9)
                player.defense = int(player.base_defense * 0.9)
        else:  # Daytime
            # Monster: -20% effect
            monster.health = int(monster.base_health * 0.8)
            monster.attack = int(monster.base_attack * 0.8)
            monster.defense = int(monster.base_defense * 0.8)
            # Player: +10% effect
            if player:
                player.attack = int(player.base_attack * 1.1)
                player.defense = int(player.base_defense * 1.1)
                

    def is_shop_open(self):
        """Checks if the shop is open (only open during daytime)."""
        return self.current_time == "day"