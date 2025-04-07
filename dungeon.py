import random
from monster import Monster

class Dungeon:
    def __init__(self, name, base_monsters):
        self.name = name
        self.base_monsters = base_monsters  # Template monsters
        self.level = 1

    def spawn_monsters(self, day_night):
        scaled = []
        for m in self.base_monsters:
            mult = 1 + 0.25 * (self.level - 1)
            hp  = int(m.health * mult)
            atk = int(m.attack * mult)
            dfs = int(m.defense * mult)
            # Assume base monsters may have an element attribute; if not, default to "none".
            mob = Monster(m.name, hp, atk, dfs, element=getattr(m, "element", "none"))
            if day_night.current_time == "night":
                day_night.apply_day_night_effects(player=None, monster=mob)
            scaled.append(mob)
        return scaled

    def handle_encounter(self, player, monster):
        while monster.health > 0 and player.health > 0:
            print(f"\nYou face {monster.name} (HP: {monster.health}).")
            print("Encounter Options:")
            print("  A) Basic Attack")
            print("  U) Use Ability")
            print("  I) Check Inventory")
            print("  F) Flee")
            action = input("Choose an option ➜ ").strip().lower()
            if action == "i":
                # Show inventory without costing an action.
                if player.inventory:
                    print("Your Inventory:", ", ".join(player.inventory))
                else:
                    print("Your inventory is empty.")
                continue
            elif action == "f":
                if random.random() < 0.5:
                    print("You successfully fled from the encounter!")
                    return "fled"
                else:
                    print("Flee attempt failed! You must fight!")
            elif action == "u":
                # Use an ability – if canceled, repeat the loop.
                if player.use_ability(monster):
                    # After ability use, check if monster is defeated.
                    if monster.health <= 0:
                        print(f"{monster.name} is defeated!")
                        return "defeated"
                else:
                    continue  # Ability canceled; show options again.
            else:  # Default: Basic Attack
                print(f"{player.name} attacks {monster.name} with a basic strike!")
                player.attack_monster(monster)
            if monster.health <= 0:
                print(f"{monster.name} is defeated!")
                return "defeated"
            # Monster counterattacks.
            monster.attack_player(player)
            if player.health <= 0:
                print(f"{player.name} has been defeated!")
                return "defeated"
        return "defeated"

    def enter(self, player, fight_sys, day_night):
        print(f"\n🗡️  You descend into **{self.name}** (Dungeon Level {self.level})")
        monsters = self.spawn_monsters(day_night)
        for mob in monsters:
            outcome = self.handle_encounter(player, mob)
            if outcome == "fled":
                print("You escaped this encounter. Moving on...")
                continue  # No reward if you flee.
            if player.health <= 0:
                return  # End dungeon if player dies.
            player.enemies_defeated += 1
        print("🏆  Floor cleared! The dungeon grows more dangerous...")
        self.level += 1