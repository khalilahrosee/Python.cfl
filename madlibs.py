print("=====Welcome to Madlibs!=====")



fighter = input("Choose your fighter: Wizard, Warrior, or Archer?")
if fighter == "Archer":
    print("You chose Archer and have 200 energy!")
elif fighter == "Warrior":
    print("You chose Warrior and have 150 energy!")
elif fighter == "Wizard":
    print("You chose Wizard and have 250 energy!")
Enemy = input("Choose your enemy: Goblin, Troll, or Dragon?")
if Enemy == "Goblin":
    print("You chose Goblin as your enemy!it has 100 energy!")
elif Enemy == "Troll":
    print("You chose Troll as your enemy! it has 150 energy!")
elif Enemy == "Dragon":
    print("You chose Dragon as your enemy! it has 300 energy!")
Ability = input("Choose your ability: Fireball, Lightning, or Ice Shard?")
if Ability == "Fireball":
    print("You chose Fireball as your ability! it gives 50 energy!")
elif Ability == "Lightning":
    print("You chose Lightning as your ability! it gives 75 energy!")
elif Ability == "Ice Shard":
    print("You chose Ice Shard as your ability! it gives 100 energy!")
heads_or_tails = input("heads or tails?:")
if heads_or_tails == "heads":
    print("You chose heads, you attack first!; you attacked your enemy and they lost 50 energy! If your enemy is a goblin, they have 50 energy left, If your enemy is a troll, they have 100 energy left, If your enemy is a dragon, they have 250 energy left!")
if heads_or_tails == "tails":
    print("You chose tails, your enemy attacks first!; your enemy attacked you and you lost 50 energy!")
total_energy = input("How much energy do you have left?: This determines if you win or lose the battle!")
if total_energy == 50 and Enemy == "Goblin":
    print("You win the battle! You defeated the goblin!")
elif total_energy == 100 and Enemy == "Troll":
    print("You win the battle! You defeated the troll!")    
elif Enemy == "Dragon" and total_energy >250:
    print("You win the battle! You defeated the dragon!")
elif Enemy == "Goblin" and total_energy <50:
    print("You lose the battle! The goblin defeated you!")
elif Enemy == "Troll" and total_energy <100:
    print("You lose the battle! The troll defeated you!")
elif Enemy == "Dragon" and total_energy <250:
    print("You lose the battle! The dragon defeated you!")

    

result = input("Did you win or lose?")
if result == "win":
    print("Hurrah! You have won the battle and saved the kingdom! You are a hero!")
elif result == "lose":
    print("Oh no! You have lost the battle and the kingdom is in ruins! You are a failure!")







