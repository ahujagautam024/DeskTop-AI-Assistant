
#import Speech Recognition module
import speech_recognition as speech
#import the os module
import os
import datetime

# import openai module
import openai

#from config file just to import the api key for accessing open AI API
from config import api_key

import random

#function OpenAIAssistant for chatbot this will chat and response to your queries.
def openAIAssistant(prompt):
    openai.api_key = api_key

    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {
        "role": "user",
        "content": prompt
        }
    ],
    temperature=1,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )

    print(response["choices"][0]["message"]["content"])
    Speak(response["choices"][0]["message"]["content"])
    

def AI(prompt):
    openai.api_key = api_key

    text = f"Open AI Response for prompt: {prompt} \n *************************************\n\n"

    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {
        "role": "user",
        "content": prompt
        }
    ],
    temperature=1,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )

    text += response["choices"][0]["message"]["content"]

    print(response["choices"][0]["message"]["content"])

    #

    with open(f"OpenAI/prompt - {random.randint(0,1224)}", "w") as f:
        f.write(text)


# function to speak with the text generated from open AI
def Speak(text):
    os.system(f"say {text}")



#function to take user's input through mic using speech recognition module
def takeMicInput():
    r = speech.Recognizer()
    with speech.Microphone() as source:
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language="en-in")
            print(f'User said: {query}')
            return query
        except Exception as e:
            return "Some Error Occured. Sorry, I was not able to get you, can you repeat"
        


#Main function driver code
if __name__ == '__main__':
    Speak("Hello I am an A.I Assistant")
    
    while True:
        print("Listening")
        text_said = takeMicInput()
        #Speak(text_said)
        sites = [["youtube", "https://www.youtube.com"],["wikipedia", "https://www.wikipedia.com"], ["google", "https://www.google.com"]]
        
        if "stop".lower() in text_said.lower():
            break

        '''
        for site in sites:
            if f"Open {site[0]}".lower() in text_said.lower():
                Speak(f"Opening {site[0]}") 
                webbrowser.open(site[1])
        '''


        if "the time" in text_said.lower():
            strfTime = datetime.datetime.now().strftime("%H:%M:%S")
            Speak(f'The time is {strfTime}')

        elif "open facetime".lower() in text_said.lower():
            os.system(f"open /System/Applications/FaceTime.app")

        elif "Using Open".lower() in text_said.lower():
            AI(prompt = text_said)

        else:
            openAIAssistant(prompt=text_said)


        

                