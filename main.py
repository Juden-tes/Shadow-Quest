import os, random
from player import Player
from monster import Monster
from fight_system import FightSystem
from shop import Shop
from dungeon import Dungeon
from day_night_mode import DayNightMode
from quest_system import Quest, QuestSystem

# ---------------------------------------------------------------------------
#        WORLD OBJECTS
# ---------------------------------------------------------------------------
# Monsters Creation
fight_sys = FightSystem()
shop = Shop()
day_night = DayNightMode()
base_mobs = [Monster("Goblin", 50, 8, 3)]
dungeon = Dungeon("Dark Dungeon", base_mobs)

qs = QuestSystem([
    Quest("Defeat 5 enemies",   reward_coins=50,  reward_xp=20, required_kills=5),
    Quest("Defeat 15 enemies",  reward_coins=150, reward_xp=60, required_kills=15),
])

# ---------------------------------------------------------------------------
#       HELPER
# ---------------------------------------------------------------------------
# System definitions
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_quests():
    print("\n📜  **Quests**")
    for q in qs:
        status = "✓" if q.completed else "…"
        print(f" {status}  {q.description}  (reward {q.reward_coins}c)")


# ---------------------------------------------------------------------------
#           MAIN GAME
# ---------------------------------------------------------------------------
print("     Welcome to....")
print("""
   ▄████████    ▄█    █▄       ▄████████ ████████▄   ▄██████▄   ▄█     █▄ 
  ███    ███   ███    ███     ███    ███ ███   ▀███ ███    ███ ███     ███
  ███    █▀    ███    ███     ███    ███ ███    ███ ███    ███ ███     ███
  ███         ▄███▄▄▄▄███▄▄   ███    ███ ███    ███ ███    ███ ███     ███
▀███████████ ▀▀███▀▀▀▀███▀  ▀███████████ ███    ███ ███    ███ ███     ███
         ███   ███    ███     ███    ███ ███    ███ ███    ███ ███     ███
   ▄█    ███   ███    ███     ███    ███ ███   ▄███ ███    ███ ███ ▄█▄ ███
 ▄████████▀    ███    █▀      ███    █▀  ████████▀   ▀██████▀   ▀███▀███▀ 
                                                                          
████████▄   ███    █▄     ▄████████    ▄████████     ███                  
███    ███  ███    ███   ███    ███   ███    ███ ▀█████████▄              
███    ███  ███    ███   ███    █▀    ███    █▀     ▀███▀▀██              
███    ███  ███    ███  ▄███▄▄▄       ███            ███   ▀              
███    ███  ███    ███ ▀▀███▀▀▀     ▀███████████     ███                  
███    ███  ███    ███   ███    █▄           ███     ███                  
███  ▀ ███  ███    ███   ███    ███    ▄█    ███     ███                  
 ▀██████▀▄█ ████████▀    ██████████  ▄████████▀     ▄████▀                """)


while True:
    start_game = input("\nDo you want to continue? y = yes || x = exit: ").lower()

    if start_game == 'y':
        break
    elif start_game == 'x':
        print("Farewell, brave soul.")
        exit()
    else:
        print("Invalid input. Please type 'y' to start or 'x' to exit.")
   
clear()

# Creation of player
while True:
    player = Player(input("What is your name? "))
    if input(f"Is your name {player.name}? (y/n): ").lower() == "y":
        print("Great! Your journey begins now...")
        break
    else:
        print("Let's try again!")
    
if input("Press any key to continue or \"x\" to exit").lower() == "x":
    exit()

print('''
Shadow Quests consist about killing enemies in the dungeon, leveling up, getting items and getting stornger and killing more neemies
      ''')

clear()
print('''
                   _     _    _     _
                  [_]___[_]__[_]___[_]
                  [__#__][__I_]__I__#]
                  [_I_#_I__#[__]__#__]
                     [_]_#_]__I_#_]
                     [I_|/ _W_ \|#]
                     [#_||{(")}||_]
                     [_I||{/~\}||_]
                     [__]|/\_/\||#]
                     [_I__I#___]__]
                     [__I_#_I___#_]
                     [#__I____]__I]
      .-.            [__I_#__I__[_]
    __|=|__          [_#_[__#_]__#]
   (_/`-`\_)         [__#_I__[#_I_]
   //\___/\\\\         [_I__]__#_I__]
   <>/   \<>         [#__I__#_]__I]
    \|_._|/          [_I#__I___I_#]    .:.
     <_I_>           [#__I__]_#___]   -=o=-
      |||            [_I__I#__]___]    ':'
jgs  /_|_\         \\\\[__]#___][__#]//, \|/
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
'''
)
start_slot = ""
while start_slot not in ("day", "night"):
    start_slot = input("Begin at (day/night)? ➜ ").lower()

day_night.set_time(start_slot)

day_count = 1

while player.health > 0:
    clear()
    print(f"===================  DAY {day_count}  ({day_night.current_time.upper()})  ===================")

    if input("Would you like to check your stats? (y/n) ➜ ").strip().lower() == "y":
        player.display_stats()

    actions_left = day_night.actions_allowed()

    # ------------------------------------------------ main turn ------------------------------------------------
    while actions_left > 0 and player.health > 0:
        print(f"\n{actions_left} action(s) remaining")
        print("A) Enter Dungeon")
        if day_night.is_shop_open():
            print("B) Visit Shop")
        print("C) Check Quests")
        print("I) Check Inventory / Equip armour")
        print("E) End the Day early")

        choice = input("Choose an option ➜ ").strip().lower()
        if choice == "a":
            cost = dungeon.level
            if actions_left < cost:
                print(f"Not enough actions to enter the dungeon (requires {cost}).")
            else:
                dungeon.enter(player, fight_sys, day_night)
                actions_left -= cost
        elif choice == "b" and day_night.is_shop_open():
            shop.display_items()
            item = input("What do you want to buy? (blank = cancel) ➜ ").title()
            if item:
                shop.buy(player, item)
                actions_left -= 1
        elif choice == "c":
            show_quests()
            actions_left -= 1
        elif choice =="i":
            print("Inventory:", ", ".join(player.inventory) if player.inventory else "Empty")
            if input("Do you want to equip an armour item? (y/n) ➜ ").strip().lower() == "y":
                player.equip_armour()
        elif choice == "e":
            break
        else:
            print("Invalid option!")

        # After every combat, check quest completion
        for q in qs.quests:
            q.check_completion(player)

        if player.health <= 0:
            break

    # ------------------------------------------------ day ends ------------------------------------------------
    if player.health <= 0: break
    print("\n💤  You take a short rest and regain 10 HP.")
    player.health = min(player.health + 10, 100 + 20 * (player.level - 1))

    day_night.toggle()          # flip day/night

    day_count += 0.5
    

print("\n=== GAME OVER ===")