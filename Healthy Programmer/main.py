# Healthy Programmer

# 9am - 5pm
# Water - water.pm3 (3.5 litres) - Drank - log after every 26 min 200ml
# Eyes - eyes.mp3 - every 30 in - EyDone - log
# Physical Activity - physical.mp3 every - 45 min - ExDone - log

# Rules
# Pygame module to play audio


import time
from pygame import mixer


mixer.init()

initialMins = int(time.time())

class Activities:
    def __init__(self, music, statement, log ):
        self.music = music
        self.statement = statement
        self.log = log

    def activity(self):
        # Playing music
        mixer.music.load(self.music)
        mixer.music.set_volume(1.0)
        mixer.music.play(-1)

        # Taking input from user
        now = time.strftime("%I:%M:%S %p", time.localtime())
        userInput = input(f"[ {now} ]: {self.statement}")

        # Stopping music after getting input
        if userInput:
            mixer.music.stop()

        # Writing data to log file
        now = time.asctime(time.localtime(time.time()))
        with open("UserRecord.txt", "a") as f:
            f.write(f"\n[ {now} ]: {self.log}")


drink = Activities("water.mp3", "Enter 'Drank' after drinking 1 glass or 200ml of water:", "Drank Water")
eyes = Activities("eyes.mp3", "Enter 'EyDone' after looking at an object 20m away from you for at least one loop of music: ", "Relaxation of Eyes Done")
physical = Activities("physical.mp3", "Enter 'ExDone' After doing some Physical Exercises: ", "Physical Exercise Done")


waterCount = eyeCount = physicalCount = 1

while True:
    presentMins = int(time.time())
    mins = (presentMins - initialMins) / 60
    waterTime = mins == 26*waterCount
    eyesTime = mins == 30*eyeCount
    physicalTime = mins == 45*physicalCount

    if waterTime and eyesTime and physicalTime:
        drink.activity()
        eyes.activity()
        physical.activity()
        waterCount += 1
        eyeCount += 1
        physicalCount += 1

    elif waterTime and eyesTime:
        drink.activity()
        eyes.activity()
        waterCount += 1
        eyeCount += 1

    elif waterTime and physicalTime:
        drink.activity()
        physical.activity()
        waterCount += 1
        physicalCount += 1

    elif eyesTime and physicalTime:
        eyes.activity()
        physical.activity()
        eyeCount += 1
        physicalCount += 1

    elif waterTime:
        drink.activity()
        waterCount += 1

    elif eyesTime:
        eyes.activity()
        eyeCount += 1

    elif physicalTime:
        physical.activity()
        physicalCount += 1

