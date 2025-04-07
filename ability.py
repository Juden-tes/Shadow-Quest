class Ability:
    def __init__(self, name, element, mana_cost, base_bonus):
        self.name = name
        self.element = element
        self.mana_cost = mana_cost
        self.base_bonus = base_bonus

    def use(self, player, enemy):
        if player.mana < self.mana_cost:
            print(f"Not enough mana to use {self.name}!")
            return 0
        player.mana -= self.mana_cost
        # Base damage is player's attack plus the bonus from the ability.
        damage = player.attack + self.base_bonus

        # Elemental effectiveness: if the ability’s element is strong against the enemy’s,
        # boost damage by 50%.
        # (Define your own matchup here.)
        effective_against = {
            "fire": "dirt",
            "water": "fire",
            "dirt": "air",
            "air": "water"
        }
        enemy_element = getattr(enemy, "element", "none")
        if self.element in effective_against and enemy_element == effective_against[self.element]:
            print(f"{self.name} is super effective against {enemy.name}!")
            damage = int(damage * 1.5)
        return damage
