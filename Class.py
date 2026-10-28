# import pyttsx3
# engine = pyttsx3.init()
# engine.say("hay i am good")
# engine.runAndWait()


import os
dirPath = "/"
all_path = os.listdir(dirPath)
print("path: ", all_path)

for i in all_path:
    print(i)