name = input("Enter your name: ")
mood = input("How are you feeling today? happy/sad/sleepy/depressed: ")
energy = int(input("Enter your energy level from 1 to 10: "))

if energy < 3:
    print("You seem to be low on energy today. You might want to take it easy and rest.")

if energy >= 6:
    print("Your energy is not too low. You can still do some activities today.")
else:
    print("You might want to take it easy and rest.")

if mood == "sad":
    advice = "Talk to someone you trust or do something that makes you feel better."
elif mood == "sleepy":
    advice = "Get some rest or take a short nap."
elif mood == "depressed":
    advice = "Reach out to a friend or family member for support."
elif mood == "happy":
    advice = "That's great! Keep doing what makes you happy and spread positivity."
else:
    advice = "Whatever your mood is, just remember to take care of yourself."

import datetime
today = datetime.datetime.now()

print("\n--------------------------------")
print("DAILY MOOD ADVISOR REPORT")
print("----------------------------------")
print("Name:", name)
print("Mood:", mood)
print("Energy Level:", energy)
print("Date and Time:", today)
print("Advice:", advice)
print("================================")