import random

def dungeon_escape():
    input("Press Enter to start the game...")  # User must press Enter to begin

    print("\n🏰 Welcome to the Dungeon Escape Game! 🏹")
    print("You must survive 5 rooms and escape alive!\n")

    health = 100
    inventory = []
    rooms = ["Dark Hallway", "Treasure Room", "Monster Den", "Trap Room"]

    for i in range(5):  # Player must survive 5 rooms
        room = random.choice(rooms)
        print(f"\n🚪 You entered the {room}.")

        if room == "Dark Hallway":
            print("It's dark and scary... but nothing happens.")

        elif room == "Treasure Room":
            item = random.choice(["Magic Potion", "Sword", "Gold"])
            print(f"💎 You found a {item}!")
            inventory.append(item)

        elif room == "Monster Den":
            print("🐲 A wild monster appears!")
            action = input("Do you want to (F)ight or (R)un? ").strip().lower()
            
            if action == "f":
                if "Sword" in inventory:
                    print("⚔️ You fight with your sword and defeat the monster!")
                else:
                    print("You have no weapon! The monster attacks you.")
                    health -= 30
            elif action == "r":
                print("🏃 You escaped, but lost some health!")
                health -= 10
            else:
                print("Invalid choice! The monster attacks you.")
                health -= 30

        elif room == "Trap Room":
            print("⚠️ You stepped on a trap! You lost 20 health.")
            health -= 20

        print(f"❤️ Health: {health}")

        if health <= 0:
            print("\n💀 You died in the dungeon. Game Over!")
            return

        # Allow player to use potion
        if "Magic Potion" in inventory:
            use_potion = input("Do you want to use a Magic Potion? (Y/N) ").strip().lower()
            if use_potion == "y":
                print("🧪 You used a Magic Potion and restored 30 health!")
                health += 30
                inventory.remove("Magic Potion")

    print("\n🎉 Congratulations! You escaped the dungeon alive! 🎉")
    print(f"🏆 Final Inventory: {inventory}")

# Start the game
dungeon_escape()
