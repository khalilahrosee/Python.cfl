import random
import time


class Player:
    def __init__(self, name, country, role, specialty):
        self.name = name
        self.country = country
        self.role = role
        self.specialty = specialty
        self.health = 100
        self.morale = 80
        self.ammo = 10
        self.xp = 0
        self.rank = "Private"
        self.inventory = ["knife", "field map"]
        self.medals = 0

    def show_profile(self):
        print("\n=== SOLDIER PROFILE ===")
        print(f"Name: {self.name}")
        print(f"Country: {self.country}")
        print(f"Branch: {self.role}")
        print(f"Specialty: {self.specialty}")
        print(f"Rank: {self.rank}")
        print(f"Health: {self.health}")
        print(f"Morale: {self.morale}")
        print(f"Ammo: {self.ammo}")
        print(f"XP: {self.xp}")
        print(f"Medals: {self.medals}")
        print(f"Inventory: {', '.join(self.inventory)}")

    def add_item(self, item):
        if item not in self.inventory:
            self.inventory.append(item)

    def apply_damage(self, amount):
        self.health = max(0, self.health - amount)
        self.morale = max(0, self.morale - max(2, amount // 6))

    def gain_xp(self, amount):
        self.xp += amount
        print(f"\n+{amount} XP earned!")
        if self.xp >= 40:
            self.rank = "Corporal"
        if self.xp >= 90:
            self.rank = "Sergeant"
        if self.xp >= 160:
            self.rank = "Captain"
        if self.xp >= 260:
            self.rank = "Major"
        if self.xp >= 400:
            self.rank = "Colonel"

    def heal(self):
        if "medkit" in self.inventory:
            self.health = min(100, self.health + 30)
            print("You used a medkit and recovered health.")
        else:
            print("You have no medkit.")


def intro():
    print("=" * 70)
    print("ADVANCED WWII CAMPAIGN SIMULATOR")
    print("Build your legend across the bloodiest theaters of the war.")
    print("=" * 70)


def create_player():
    print("\nCreate your soldier:\n")
    name = input("Enter your name: ").strip()
    while not name:
        name = input("Your name cannot be empty. Enter your name: ").strip()

    print("\nChoose your country:")
    print("1. United States")
    print("2. United Kingdom")
    print("3. Germany")
    print("4. Soviet Union")
    print("5. France")
    print("6. Japan")
    country_choice = input("Pick a number: ").strip()

    countries = {
        "1": "United States",
        "2": "United Kingdom",
        "3": "Germany",
        "4": "Soviet Union",
        "5": "France",
        "6": "Japan",
    }
    country = countries.get(country_choice, "United States")

    print("\nChoose your branch:")
    print("1. Marine")
    print("2. Army")
    print("3. Other")
    branch_choice = input("Pick a number: ").strip()

    if branch_choice == "1":
        role = "Marine"
        specialty = "Amphibious Assault"
        health_bonus = 6
    elif branch_choice == "2":
        role = "Army"
        specialty = "Infantry Commander"
        health_bonus = 2
    else:
        role = "Other"
        specialty = input("Enter your specialty (Pilot, Engineer, Spy, etc.): ").strip() or "Special Operative"
        health_bonus = 4

    player = Player(name, country, role, specialty)
    player.health += health_bonus
    player.morale += 6
    if role == "Marine":
        player.add_item("flare")
        player.add_item("smoke bomb")
    elif role == "Army":
        player.add_item("grenade")
        player.add_item("field radio")
    else:
        player.add_item("radio")
        player.add_item("satchel charge")
    return player


def mission_intro(player, mission_name, setting, enemy_name):
    print(f"\n=== {mission_name} ===")
    print(f"Location: {setting}")
    print(f"Commander: {player.name}, your unit has been assigned to {mission_name}.")
    print(f"Enemy contact: {enemy_name}")
    print("The battle is fierce, and every decision may change the war.")


def battle(player, mission_name, enemy_name, enemy_health, terrain):
    print(f"\nEnemy spotted: {enemy_name}")
    print(f"Terrain: {terrain}")
    print("You must fight with discipline and grit.")

    turn = 0
    while player.health > 0 and enemy_health > 0 and turn < 8:
        turn += 1
        print(f"\nTurn {turn} - Choose an action:")
        print("1. Fire your weapon")
        print("2. Throw grenade")
        print("3. Use medkit")
        print("4. Call artillery support")
        print("5. Retreat and regroup")
        choice = input("Action: ").strip()

        if choice == "1":
            if player.ammo <= 0:
                print("You are out of ammo!")
            else:
                player.ammo -= 1
                damage = random.randint(18, 32)
                enemy_health -= damage
                print(f"You hit the enemy for {damage} damage.")
                if enemy_health <= 0:
                    break
                counter = random.randint(8, 22)
                player.apply_damage(counter)
                print(f"The enemy fired back for {counter} damage.")

        elif choice == "2":
            if "grenade" in player.inventory or "satchel charge" in player.inventory:
                if "grenade" in player.inventory:
                    player.inventory.remove("grenade")
                else:
                    player.inventory.remove("satchel charge")
                damage = random.randint(28, 45)
                enemy_health -= damage
                print(f"The explosive blast dealt {damage} damage.")
                if enemy_health <= 0:
                    break
                counter = random.randint(10, 18)
                player.apply_damage(counter)
                print(f"You took {counter} damage from the blast.")
            else:
                print("You do not have an explosive device.")

        elif choice == "3":
            player.heal()

        elif choice == "4":
            if "radio" in player.inventory or "field radio" in player.inventory:
                damage = random.randint(24, 36)
                enemy_health -= damage
                print(f"Artillery support struck the enemy for {damage} damage.")
                player.morale += 8
                if enemy_health <= 0:
                    break
                player.apply_damage(random.randint(5, 12))
                print("The enemy returned fire during the barrage.")
            else:
                print("You have no radio for artillery support.")

        elif choice == "5":
            print("You pull back behind cover and survive the engagement.")
            player.apply_damage(12)
            player.morale -= 5
            break

        else:
            print("Invalid choice. Stay alert.")

        if random.random() < 0.25:
            print("A shell burst near you. The impact rattles your nerves.")
            player.apply_damage(6)

        if player.health <= 0:
            print("You were wounded and collapsed on the battlefield.")
            return False

    if enemy_health <= 0:
        print(f"\nMission success! {mission_name} was secured.")
        player.gain_xp(30)
        player.morale = min(100, player.morale + 10)
        player.medals += 1
        if random.random() < 0.5:
            player.add_item("medkit")
            print("A medic supplied you with a medkit.")
        return True

    print("The enemy broke your assault and forced a retreat.")
    return False


def recovery_phase(player):
    print("\nYou take a moment to regroup, rest, and prepare for the next objective.")
    print("1. Rest and recover")
    print("2. Push forward with your squad")
    print("3. Scout the area for supplies")
    choice = input("Choose your recovery action: ").strip()

    if choice == "1":
        player.health = min(100, player.health + 12)
        player.morale = min(100, player.morale + 8)
        print("Your unit recovers strength and confidence.")
    elif choice == "2":
        player.morale += 5
        player.ammo = min(20, player.ammo + 3)
        print("Your squad advances with renewed determination.")
    elif choice == "3":
        if random.random() < 0.7:
            player.add_item("medkit")
            print("You found a medkit hidden near the wreckage.")
        else:
            print("The area is empty and the search yields nothing.")
    else:
        print("You hesitate too long and lose momentum.")
        player.morale -= 3


def main():
    intro()
    player = create_player()
    player.show_profile()

    time.sleep(1)
    print("\nThe war is already raging. Your orders are being issued.")
    time.sleep(1)

    missions = [
        ("Operation Torch Landing", "North Africa", "Axis machine-gun nest", 90, "The beach is burning under heavy fire."),
        ("The Hedgerow Breakthrough", "Normandy", "Panzer reconnaissance squad", 95, "The fields are muddy and full of traps."),
        ("The Siege of Stalingrad", "Urban ruins", "Sniper cell", 100, "Every building is a fortress."),
        ("The Ardennes Counterattack", "Frozen forest", "Tank crew", 105, "The snow is deep and visibility is poor."),
        ("Kursk Offensive", "Open steppe", "Anti-tank team", 110, "The ground is broken by shells."),
        ("The Battle of the Bulge", "Snow-covered roads", "Assault platoon", 115, "The cold bites through your uniform."),
        ("The Crossing of the Rhine", "Riverbank", "Defensive artillery", 120, "The water is freezing and the banks are mined."),
        ("Operation Market Garden", "Dutch countryside", "Paratrooper ambush", 125, "The roads are clogged with wreckage."),
        ("Berlin Street Fighting", "Ruins of Berlin", "Urban defender", 130, "Buildings crack with every explosion."),
        ("The Fall of the Reich", "Capital streets", "Elite guard", 135, "Victory is close, but the enemy is desperate."),
        ("The Liberation of Paris", "City streets", "Garrison squad", 140, "The city is tense and full of hidden danger."),
        ("The Final Push", "War-torn Europe", "Last defense line", 145, "The end of the war is near, but so is disaster."),
    ]

    for mission_name, setting, enemy_name, enemy_health, flavor in missions:
        print(f"\n{flavor}")
        mission_intro(player, mission_name, setting, enemy_name)
        success = battle(player, mission_name, enemy_name, enemy_health, setting)
        if not success:
            break
        recovery_phase(player)
        player.gain_xp(15)
        print("Your squad advances deeper into the battlefield.")
        time.sleep(1)

    if player.health > 0 and player.xp >= 180:
        print("\n=== VICTORY ===")
        print(f"{player.name} survived the campaign and rose to {player.rank}.")
        print(f"You earned {player.medals} medals and carried your country through the fire.")
        print("The war was brutal, but your courage changed the course of history.")
    else:
        print("\n=== DEFEAT ===")
        print(f"{player.name} fell in battle before the campaign was over.")
        print("The front was unforgiving, but your story will be remembered.")


if __name__ == "__main__":
    main()
