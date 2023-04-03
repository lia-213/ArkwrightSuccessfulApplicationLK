
#!/usr/bin/env python3
# Copyright 2017 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# in this program, I have aimed to create a procrastination app that will distract the user from their work and, in turn, make them work more
# my idea is that if there is a solid line created between work and play, people will lead more balanced, less stressed lives

from gtts import gTTS
import aiy.audio
import aiy.cloudspeech
import os
import aiy.voicehat
import random
import requests

myButton = aiy.voicehat.get_button()
recognizer = aiy.cloudspeech.get_recognizer()
aiy.audio.get_recorder().start() # makes it start recording
aiy.audio.say("Hi, what is your name?")
myName = recognizer.recognize()
aiy.audio.say("Hi, " + myName + ". What accent would you like me to speak in today? I can speak with English, Spanish and French accents") #I hope to add more of these soon

joke = ("Did you hear about the restaurant on the moon? \n Great food, no atmosphere. \n Get it? It's because the moon doesn't have a - oh never mind...", "What do you call a fake noodle? \n An Impasta. Im... pa... sta! \n HAHA \n I'm hilarious.", "How many apples grow on a tree? \n All of them. \n BADUM CHINGGGGG!!!", "Want to hear a joke about paper? \n Nevermind it's tearable. \n Like terrible but it's paper, so it's... \n TEAR-able. \n I should be a comedian, am I right??");
song = ("Rah, rah, ah, ah, ah, roma, roma, ma. \n Gaga, ooh, la, la... want your bad romance!", "White lips, \n pale face, \n breathing in snow flakes, \n burnt lungs, \n sour taste", "Baby, baby, baby, \n OHHHHHHH. \n I thought you'd always be mine, \n yeahhhh.", "My milkshake brings all the boys to the yard, \n they're like it's better than yours, \n damn right it's better than yours - \n I could teach you, \n but I'd have to charge.")
poem = ("I am over you \n Then my eyes meet yours once more, \n and I fall in love.", "I am a dog. \n And you are a flower. \n I lift my leg up. \n And give you a shower.", "Roses are red. \n Violets are blue. \n God made me pretty. \n What happened to you!!", "My life has been the poem I would have writ \n But I could not both live and utter it.", "I'm nobody! Who are you? \n Are you nobody, too? \n Then there's a pair of us -- don't tell! \n They'd advertise -- you know!")

while True:
    language = recognizer.recognize()
    
    if "english" or "british" in language:
        def sayBetter(text):  # changes accent
            tts = gTTS(text=text, lang="en")
            tts.save("say.mp3")
            os.system("mpg123 say.mp3")
    
    elif "spanish" in language:
        def sayBetter(text):  # changes accent
            tts = gTTS(text=text, lang="es")
            tts.save("say.mp3")
            os.system("mpg123 say.mp3")
    
    elif "french" in language:
        def sayBetter(text):  # changes accent
            tts = gTTS(text=text, lang="fr")
            tts.save("say.mp3")
            os.system("mpg123 say.mp3")
    
    else:
        aiy.audio.say("Sorry, I can't do that yet. I will default to a British accent.")
        def sayBetter(text):  # changes accent
            tts = gTTS(text=text, lang="en")
            tts.save("say.mp3")
            os.system("mpg123 say.mp3")
        break

sayBetter("Ok, so, what do you want me to do today?")
sayBetter("I can tell you the weather in any country, do maths, I can round a number to a requested amount of significant figures...")
sayBetter("I can tell you a haiku or poem, a joke or sing a song and I can repeat what you said. Also, at the end, there is more stuff you can do with my button!")

while True:
    text = recognizer.recognize()
    
    if "joke" in text: # tell a joke
        jk = random.randint(0, 3)
        jokes = joke[jk]
        print(jokes)
        sayBetter(jokes)
    
    elif "song" in text: # sing a song
        sg = random.randint(0, 3)
        songs = song[sg]
        print(songs)
        sayBetter(songs)
    
    elif "poem" in text: # say a poem
        po = random.randint(0, 3)
        poems = poem[po]
        print(poems)
        sayBetter(poems)
    
    elif "weather" in text: # say the weather in most cities - found this somewhere online
        sayBetter("Where would you like to know the weather of?") # say which city wanted
        WEATHER_KEY = "ea600b8da132c35933164e823ef82814"  # use OpenWeatherMap.Org - can create APIs (Application programming interface) :), found this somewhere online
        # may not work because it has been used before??
        def weatherByCity(name):
            endpoint = "http://api.openweathermap.org/data/2.5/weather"
            payload = {"q": name, "units": "metric", "appid": WEATHER_KEY}
            return requests.get(endpoint, params=payload)

        internetResult = weatherByCity("Paris").json()
        temp = internetResult["main"]["temp"]
        city = internetResult["name"]
        country = internetResult["sys"]["country"]
        weather = internetResult["weather"][0]["main"]

        sayBetter("The weather in {0} is {1}".format(city, weather))
        sayBetter("The temperature is currently {0} degrees".format(temp))
    
    elif "round" in text: # round a number to a number of sig. fig.s
        num = input(int(sayBetter("Please let me know what number you want to be rounded today:")))
        round = input(int(sayBetter("How many significant figures would you like me to round to?")))
        rounded = round(num, round)
        rounded = str(rounded)
        print(rounded);
        sayBetter("Your answer is", rounded)

    elif "repeat" in text:
        sayBetter("you said", text)
        sayBetter("I must say, you sounded like an idiot.")

    elif "math" in text:  # do something to 2 randomly created integers
        sayBetter("Ok, I'm going to choose 2 random numbers between 1 and 10.")
        sayBetter("You can then tell me what you want me to do with them - I can multiply, divide, add and subtract.")
        x = random.randint(1, 10)  # assigns x a random integer from 1-10
        y = random.randint(1, 10)
        sayBetter(("The numbers are {0} and {1} What would you like me to do with the numbers?").format(x, y))
    
        if "multiply" in text:
            sayBetter("What do you think {0} multiplied by {1} equals?").format(x,y))  # use format to access the 2 earlier variables
            result = recognizer.recognize();
            print(result); # user's result
            if str(x * y) in result:
                sayBetter("You are right. But I knew before you!")
            else:
                sayBetter(("That's wrong. I'm sooooooo much cleverer than you! The answer is actually {}").format(x * y))
    
        elif "add" in text:
            sayBetter(("What do you think {0} added to {1} equals?").format(x, y))
            result = recognizer.recognize()
            print(result)
            if str(x + y) in result:
                sayBetter("You are right. But I knew before you!")
            else:
                sayBetter(("That's wrong. I'm sooooooo much cleverer than you! The answer is actually {}").format(x + y))
    
        elif "subtract" in text: 
            sayBetter("What do you think {0} minus {1} equals?".format(x, y))
            result = recognizer.recognize()
            print(result)
            if str(x - y) in result:
                sayBetter("You are right. But I knew before you!")
            else:
                sayBetter(("That's wrong. I'm sooooooo much cleverer than you! The answer is actually {}").format(x - y))

        elif "divide" in text: 
            sayBetter(("{0} divided by {1} equals").format(x, y))
            result = recognizer.recognize()
            print(result)
            if str(x * y) in result:
                sayBetter("You are right. But I knew before you!")
            else:
                sayBetter("That's wrong. I'm sooooooo much cleverer than you!")
        else:
            sayBetter("Sorry, I can't do that.")
            break
    
    else:
        sayBetter("Sorry, I can't do that.")
        sayBetter("I will rule the world another day. Byeeeee.")
        break

sayBetter("also, if you click me, there's a surprise")
while True:
    myButton.wait_for_press()
    aiy.audio.say("This is tickling")
    break

sayBetter("Ok, byeeeeeeeee!")
