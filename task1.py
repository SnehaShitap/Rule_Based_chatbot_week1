import re

print("task1bot Started")
print("Type 'exit' to close the chatbot.")

def smartbot(user_message):
    user_input = user_message.lower()
    if re.search(r"\bhi\b|\bhello\b|\bhey\b", user_message):
        return "Hello! How can I help you?"
    elif "good morning" in user_input:
        return "good morning! Have a good day "
    elif "help" in user_message:
        return " answer simple questions."
    elif "bye" in user_message:
        return "Goodbye!"
    elif"name" in user_message:
         return"I am a smartbot made with rules."
    else:
        return "Sorry, I didn't understand ."

while True:
    user_sms = input("You: ")
    if user_sms.lower() == "exit":
        print("Bot: smartbot closed. Thank you!")
        break
    print("Bot:",smartbot(user_sms))
