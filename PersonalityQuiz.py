pinkiepie_points = 0
rarity_points = 0
twilightsparkle_points = 0
fluttershy_points = 0
applejack_points = 0
rainbowdash_points = 0

answer1 = input("Do you prefer 1)Pink, 2)White, 3)Purple, 4)Yellow, 5)Orange, or 6)Blue? Please respond with a number: ")
if answer1 == "1":
    pinkiepie_points += 1
elif answer1 == "2":
    rarity_points += 1
elif answer1 == "3":
    twilightsparkle_points += 1
elif answer1 == "4":
    fluttershy_points += 1
elif answer1 == "5":
    applejack_points += 1
elif answer1 == "6":
    rainbowdash_points += 1

input()
answer2 = input("Do you have 1)Curly Hair, 2)Wavy Hair, 3)Straight Hair, or 4)Protective Hairstyle?: ")
if answer2 == (1):
    pinkiepie_points += 1
elif answer2 == (2):
    rarity_points += 1
    fluttershy_points += 1
elif answer2 == (3):
    twilightsparkle_points += 1
    rainbowdash_points += 1
if answer2 == (4) or answer2 == (3):
    applejack_points += 1
input()
answer3 = input("Would you rather have 1)Magic powers, the ability to 2)Fly or 3)Be the Best at a skill of your choice?: ")
if answer3 == (1):
    rarity_points += 1
elif answer3 == (2):
    fluttershy_points or rainbowdash_points += 1
elif answer3 == (3):
    pinkiepie_points += 1
    applejack_points += 1
if answer3 == (1) or answer3 == (2):
    twilightsparkle_points += 1
input()
answer4 = input("Would you rather spend your free time 1)Partying, 2)Sewing, 3)Studying, 4)Reading Alone, 5)Garden, or 6)Sports?: ")
if answer4 == "1":
    pinkiepie_points += 1
elif answer4 == "2":
    rarity_points += 1
elif answer4 == "3":
    twilightsparkle_points += 1
elif answer4 == "4":
    fluttershy_points += 1
elif answer4 == "5":
    applejack_points += 1
elif answer4 == "6":
    rainbowdash_points += 1
input()
answer5 = input("Which is your flaw? 1)Over Energetic, 2)Perfectionist, 3)Self Isolation, 4)Social Anxiety, 5)Overprotectiveness, or 6)Too Competitive: ")
if answer5 == "1":
    pinkiepie_points += 1
elif answer5 == "2":
    rarity_points += 1
elif answer5 == "3":
    twilightsparkle_points += 1
elif answer5 == "4":
    fluttershy_points += 1
elif answer5 == "5":
    applejack_points += 1
elif answer5 == "6":
    rainbowdash_points += 1
input()
if pinkiepie_points > rarity_points and pinkiepie_points > twilightsparkle_points and pinkiepie_points > fluttershy_points and pinkiepie_points > applejack_points and pinkiepie_points > rainbowdash_points:
    print("You are Pinkiepie! She is high-energy, unpredictable Earth pony who works at the bakery and acts as the town's party planner. She is the comic relief who breaks the fourth wall to bring joy and laughter to others.")
elif rarity_points > pinkiepie_points and rarity_points > twilightsparkle_points and rarity_points > fluttershy_points and rarity_points > applejack_points and rarity_points > rainbowdash_points:
    print("You got Rarity! She is a sophisticated unicorn fashion designer and businesswoman who values beauty and high fashion. She can be melodramatic but has a deeply generous heart and constantly helps others see their inner beauty.")
elif twilightsparkle_points > pinkiepie_points and twilightsparkle_points > rarity_points and twilightsparkle_points > fluttershy_points and twilightsparkle_points > applejack_points and twilightsparkle_points > rainbowdash_points:
    print("You got Twilight Sparkle! She is the leader of the group, she is an intelligent, studious, and organized unicorn (later alicorn) who thrives on knowledge and planning. She often acts as the voice of reason but can be prone to perfectionism and anxiety.")
elif fluttershy_points > pinkiepie_points and fluttershy_points > rarity_points and fluttershy_points > twilightsparkle_points and fluttershy_points > applejack_points and fluttershy_points > rainbowdash_points:
    print("You got Fluttershy! She is a shy and gentle pegasus who loves caring for animals, often preferring their company over others. Despite her timid nature, she has a quiet strength and will become assertive to protect her friends or creatures. ")
elif applejack_points > pinkiepie_points and applejack_points > rarity_points and applejack_points > twilightsparkle_points and applejack_points > fluttershy_points and applejack_points > rainbowdash_points:
    print("You got Applejack! She is a reliable, strong, and hardworking Earth pony who runs the family apple orchard. She is down-to-earth, direct, and sometimes stubborn, often acting as the group's muscle and dependable center. ")
elif rainbowdash_points > pinkiepie_points and rainbowdash_points > rarity_points and rainbowdash_points > twilightsparkle_points and rainbowdash_points > fluttershy_points and rainbowdash_points > applejack_points:
    print("You got Rainbowdash! She is a confident and bold pegasus who manages the weather in Ponyville and dreams of flying with the Wonderbolts. She is fiercely loyal and action-oriented, though she can be arrogant and competitive.")
else:
    print("You got a tie!")