# DeskTop-AI-Assistant
This is a small project contributing to using openai api with python as smart Desktop talking assistant.


# Steps to complete the project:
  1. Choosing the code editor: In my case it is Visual Studio Code.
  2. Installing python and required packages (Speech Recognition, OpenAI, portaudio using brew(on mac), pyaudio.
  3. Starting to code main.py
  4. defining functions for the specific purposes.
  5. Testing the code continously.
  6. wrapping up.


# Files in the project:
  1. main.py (Consists of the executable process code that our project aims).
  2. config.py (for API_KEY to use openAI API's).


# Functions in main.py
  1. Speak(text) : This function takes text as input and speaks the text in audio format as output.
  2. takeMicInput(): This function uses speech recognition to take users input using the microphone and convert that to string text that returns users prompt.
  3. AI(prompt): This function takes user's prompt as input and calls the open AI api with the prompt and stores the prompt along with answers in the folder OpenAI/randomInteger.
  4. OpenAIAssistant(prompt): This function takes user's prompt as input and calls the open AI api with the prompt, passes the response from the API to the Speak function which then AI assistant speaks.
  5. main(): executable driver code.
