# Cartoon Talks Chatbot
## Overview
The Cartoon Talks Chatbot is a simple chatbot application built with Python's tkinter library. It provides users with a graphical user interface (GUI) to interact with a chatbot that can answer questions about popular cartoon and anime characters.

## Features
1) Provides predefined responses to queries about popular cartoon and anime characters.

2) Supports basic conversational commands like greetings and exits.

3) Displays user messages and bot responses in a user-friendly GUI.

## How to Run:

1. Prerequisites: Ensure you have Python 3 and the tkinter library installed. You can install tkinter using pip install tkinter.

2. Save the Code: Save the Python code (provided below) as a file named cartoon_chatbot_gui.py.

3. Run the Script: Open a terminal or command prompt, navigate to the directory where you saved the file, and execute the following command:
    bash
   cartoon_chatbot.py

## Installation
Clone or download the repository containing the chatbot script.

Ensure Python is installed and properly set up on your system.

## Usage
1) Open the terminal or your Python IDE.

2) Run the Python script:
    
    python <script_name>.py
    
    Replace <script_name> with the name of the Python file (e.g., cartoon_chatbot.py).

3) A GUI window will appear titled Cartoon Talks Chatbot.

4) Interact with the chatbot by typing your message into the input field and clicking the "Send" button.

## Supported Commands

*Character Information*

Who is Doraemon?

Response: "Doraemon is a Japanese Anime."

Who is Shizuka?

Response: "Shizuka is a character in an Anime named Doraemon. She is the best friend of Nobita."

Who is Nobita?

Response: "Nobita is a character in the Anime Doraemon, known for his lazy and clumsy nature."

Who is Mickey Mouse?

Response: "Mickey Mouse is a cartoon character created by Walt Disney."

Who is Donald Duck?

Response: "Donald Duck is a cartoon character famous for his short temper and distinctive voice."

## Basic Commands

Who are you?

Response: "I'm chatbot."

Hello, Hi, Hii, Hmm

Response: "Hello! How can I assist you with cartoon characters today?"

Exit Commands: "Quit", "Exit", "Goodbye", "Bye"

Response: "Goodbye! Have a great day!"


## Fallback Message

For unrecognized inputs, the chatbot will respond: "I am not sure about that. Can you ask something else?"

## Code Explanation
### Main Components
#### 1. *CartoonChatbot Class*

    Contains the chatbot's logic.

    Defines rules for responses and handles user input.

 
        

#### 2. *CartoonChatbotGUI Class*

    Manages the graphical interface using tkinter.
    
    Handles user input and displays bot responses in the GUI.
    
    
## Key Functions
### 1. get_response(user_input)

    def get_response(self, user_input):
        
        user_input = user_input.lower()

### 2. send_message()

    user_input = self.user_input_field.get() 

    self.user_input_field.delete(0, END) 

## Screenshots
![image alt](https://github.com/deepu6441/rulebase_chatbot/blob/44926dc16351ae18e4726ee118768dad722a0f67/Screenshot%202025-01-17%20141435.png) 

## Customization
Add more cartoon characters and responses by extending the self.rules dictionary in the CartoonChatbot class.

Modify the GUI layout by changing the tkinter components in the CartoonChatbotGUI class.

## Future Enhancements
1) Add natural language processing (NLP) for more dynamic responses.
2) Include images or multimedia for character information.
3) Implement a history feature to store past conversations.
