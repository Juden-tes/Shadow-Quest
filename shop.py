class Shop:
    def __init__(self):
        self.items = {
            "Shotgun": 60,
            "Akm": 40,
            "Scar-L": 23,
            "Sniper": 90,
            "Med Kit": 23,
            "Energy Drink": 5,
            "Pain Killer": 5,
            "Time Amulet": 50,
            "Leather Armour": 30,
            "Chainmail Armour": 60
        }

    def display_items(self):
        print("Welcome to the shop! Items for sale:")
        for item, price in self.items.items():
            print(f" - {item}: {price} coins")

    def buy(self, player, item_name):
        if item_name not in self.items:
            print("Error: Item unavailable.")
            return
        cost = self.items[item_name]
        if player.coins < cost:
            print("You don't have enough coins!")
            return
        player.coins -= cost
        player.inventory.append(item_name)
        print(f"You purchased {item_name}.")