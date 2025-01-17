from tkinter import *

class CartoonChatbot:
    def __init__(self):
        # Define rules as key-value pairs (case-insensitive matching)
        self.rules = {
            "who is doraemon": "Doraemon is a Japanese Anime.",
            "who is shizuka": "Shizuka is a character in an Anime named Doraemon. She is the best friend of Nobita.",
            "who is nobita": "Nobita is a character in the Anime Doraemon, known for his lazy and clumsy nature.",
            "who is mickey mouse": "Mickey Mouse is a cartoon character created by Walt Disney.",
            "who is donald duck": "Donald Duck is a cartoon character famous for his short temper and distinctive voice.",
            "who are you": "I'm chatbot."
        }

        self.exit_commands = ["quit", "exit", "goodbye", "bye"]
        self.start_commands = ["hii", "hello", "hmm"]

    def get_response(self, user_input):
        # Convert input to lowercase for case-insensitive matching
        user_input = user_input.lower()

        # Check for exit commands
        if user_input in self.exit_commands:
            return "Goodbye! Have a great day!"

        # Check for start commands
        if user_input in self.start_commands:
            return "Hello! How can I assist you with cartoon characters today?"

        # Return a predefined response or a default message
        return self.rules.get(user_input, "I am not sure about that. Can you ask something else?")

class CartoonChatbotGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Cartoon Talks Chatbot")

        self.chatbot = CartoonChatbot()

        # Create GUI elements
        self.user_input_label = Label(root, text="You:")
        self.user_input_label.pack()
        self.user_input_field = Entry(root, width=50)
        self.user_input_field.pack()
        self.send_button = Button(root, text="Send", command=self.send_message)
        self.send_button.pack()

        self.bot_response_label = Label(root, text="Bot:")
        self.bot_response_label.pack()
        self.bot_response_text = Text(root, height=10, width=50, state=DISABLED)
        self.bot_response_text.pack()

    def send_message(self):
        user_input = self.user_input_field.get()
        self.user_input_field.delete(0, END) 

        response = self.chatbot.get_response(user_input)

        # Enable the Text widget to allow writing
        self.bot_response_text.config(state=NORMAL)
        self.bot_response_text.insert(END, response + "\n")
        self.bot_response_text.config(state=DISABLED)

if __name__ == "__main__":
    root = Tk()
    gui = CartoonChatbotGUI(root)
    root.mainloop()