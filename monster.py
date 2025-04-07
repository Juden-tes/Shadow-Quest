class Monster:
    def __init__(self, name, health, attack, defense, is_night=False, element="none"):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.is_night = is_night
        self.element = element
        # Store base attributes to avoid cumulative multipliers.
        self.base_health = health
        self.base_attack = attack
        self.base_defense = defense
        if is_night:
            self.scale_stats_for_night()  # If you have additional logic here

    def take_damage(self, amount):
        damage = max(amount - self.defense, 0)
        self.health -= damage
        print(f"{self.name} takes {damage} damage. Health: {self.health}")

    def attack_player(self, player):
        print(f"{self.name} attacks {player.name}!")
        player.take_damage(self.attack)