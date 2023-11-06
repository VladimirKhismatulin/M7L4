import speech_recognition as speech_recog
import time
import random
score = 0
tries = 0
levels = {"e": ["dairy", "mouse", "computer"],
          "m": ["programming", "algorithm", "developer"],
          "h": ["neural network", "machine learning", "artificial intelligence"]}
def play_game(level):
    global tries
    global score
    print("Please say...")
    time.sleep(2)
    c = random.choice(level)
    print(c)
    mic = speech_recog.Microphone()
    recog = speech_recog.Recognizer()
    for i in range(2):
        right = False
        tries += 1
        with mic as audio_file:
            recog.adjust_for_ambient_noise(audio_file)
            audio = recog.listen(audio_file)
            try:
                b = recog.recognize_google(audio, language="en-EN")
                if b.lower() == c:
                    print("Correct!")
                    score += 1
                    right = True
                else:
                    print(f"You said {b}. That's wrong answer.")
            except:
                print("Time's out.")
        if right == False and i == 0:
            print("Lets try again.")
            time.sleep(2)
            print(f"Say {c}.")
        else:
            break
    print(f"Your tries: {tries}, your score: {score}.")
while True:
    try:
        put = input("e (easy), m (medium), h (hard) or s (stop)? ")
        if put != "s":
            a = levels[put]
            play_game(a)
        else:
            break
    except:
        print("You wrote something wrong. Please try again.")
        