#project: Trigger chatbot
#Author: Eddie Kairu
#Description: A very simple interactive chatbot that responds to:
#user input using conditional statements. 
#Demonstrates first unerstanding of while loops, string methods, conditionals (if/elif/else), and user input

#set the chatbot's name
bot_name = "Trigger"

#greet the user
print(f"hello, I'm {bot_name}. How can I help you?")

#start an infinite conversation loop
while True:
 #Take user input, remove extra spaces, and make it lowercase for cinsistency
 user_input = input("You: ").strip().lower()

 #respond to greetings
 if user_input in ["hi", "hello"]:
    print(f"{bot_name}: Hello, what's up!")

 #respond when user asks for the bot's name
 elif "what is your name" in user_input:
    print(f"{bot_name}: {bot_name}, my name is {bot_name}!")

 #exit the chat if the user says goodbye
 elif user_input in ["goodbye", "bye"]:
   print(f"{bot_name}: Goodbye! See you later!")
   break
 
  #default response for unrecognized input
 else:
  print(f"{bot_name}: I don't understand yet, I'm still learning!")
#end of program