from ability import Ability

class Player:
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.exp = 0
        self.health = 100
        self.attack = 10
        self.defense = 5
        self.armour = 5
        self.coins = 0
        self.mana = 50
        self.abilities = [
            Ability("Sword Attack", element="physical", mana_cost=0, base_bonus=0),
            Ability("Fire Attack", element="fire", mana_cost=10, base_bonus=5)
        ]
        self.equipped_armour = 0
        self.inventory = []
        self.enemies_defeated = 0

    def attack_monster(self, monster):
        print(f"{self.name} attacks {monster.name} with a basic strike!")
        monster.take_damage(self.attack)

    def take_damage(self, amount):
        mitigation = self.defense + self.armour + self.equipped_armour
        damage = max(amount - mitigation, 0)
        self.health -= damage
        print(f"{self.name} takes {damage} damage. Health: {self.health}")

    def level_up(self):
        self.level += 1
        self.attack += 2
        self.defense += 1
        self.health += 20
        self.mana += 10
        print(f"{self.name} leveled up! Now at level {self.level}")

        if self.level == 2:
            # Unlock Water Attack
            self.abilities.append(Ability("Water Attack", element="water", mana_cost=12, base_bonus=5))
            print(f"{self.name} unlocked a new ability: Water Attack!")
        elif self.level == 3:
            # Unlock Dirt Attack
            self.abilities.append(Ability("Dirt Attack", element="dirt", mana_cost=14, base_bonus=7))
            print(f"{self.name} unlocked a new ability: Dirt Attack!")
        elif self.level == 4:
            # Unlock Air Attack
            self.abilities.append(Ability("Air Attack", element="air", mana_cost=16, base_bonus=9))
            print(f"{self.name} unlocked a new ability: Air Attack!")
    
    def equip_armour(self):
        # List armour items in inventory
        armour_items = {
            "Leather Armour": 5,
            "Chainmail Armour": 10
        }
        available = [item for item in self.inventory if item in armour_items]
        if not available:
            print("You have no armour items in your inventory to equip.")
            return
        print("Armour available to equip:")
        for idx, item in enumerate(available, 1):
            print(f"  {idx}) {item} (+{armour_items[item]} armour)")
        choice = input("Choose an armour to equip (or press Enter to cancel): ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(available):
            chosen = available[int(choice)-1]
            self.equipped_armour = armour_items[chosen]
            print(f"You equipped {chosen}. Armour bonus is now +{self.equipped_armour}.")
        else:
            print("No armour equipped.")

    def learn_skill(self, skill):
        if skill not in self.skills:
            self.skills.append(skill)
            print(f"{self.name} learned a new skill: {skill}")

    def use_item(self, item):
        if item == "Time Amulet":
            #DAYNIGHT MODE
            self.inventory.remove(item)
            print("The Time Amulet shatters – reality shifts around you!")
        elif item == "Med Kit":
            self.health = min(self.health + 30, 100 + 20 * (self.level - 1))
            self.inventory.remove(item)
            print(f"{self.name} heals for 30 HP.")
        else:
            print("Nothing happens…")

    def use_ability(self, enemy):
        # List abilities and let the player choose one.
        print("\nChoose an ability:")
        for idx, ab in enumerate(self.abilities, 1):
            mana_text = f" (Mana cost: {ab.mana_cost})" if ab.mana_cost > 0 else ""
            print(f"  {idx}) {ab.name}{mana_text}")
        choice = input("Select ability number (or press Enter to cancel): ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(self.abilities):
            ability = self.abilities[int(choice) - 1]
            damage = ability.use(self, enemy)
            if damage > 0:
                print(f"{self.name} uses {ability.name} on {enemy.name} for {damage} damage!")
                enemy.take_damage(damage)
            return True  # Ability was attempted.
        else:
            print("Ability use canceled.")
            return False

    def add_coins(self, amount):
        self.coins += amount
        print(f"{self.name} earned {amount} coins. Total: {self.coins}")

    def display_stats(self):
        print("\n📊  Your Stats:")
        print(f"  Name: {self.name}")
        print(f"  Level: {self.level}")
        print(f"  Health: {self.health}")
        print(f"  Attack: {self.attack}")
        print(f"  Defense: {self.defense}")
        print(f"  Base Armour: {self.armour}")
        print(f"  Equipped Armour Bonus: {self.equipped_armour}")
        print(f"  Mana: {self.mana}")
        print(f"  EXP: {self.exp}")
        print(f"  Coins: {self.coins}")
        print(f"  Enemies Defeated: {self.enemies_defeated}")
        print("  Abilities: " + ", ".join(a.name for a in self.abilities))
        print("  Inventory: " + (", ".join(self.inventory) if self.inventory else "Empty"))
