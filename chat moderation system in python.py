
forbidden_words = ["bad", "ugly", "stupid", "idiot", "hate","nerd","kill","fuck"]

chat_history = []

def censor_message(message):
    words = message.split()
    censored = []
    for word in words:
        if word.lower() in forbidden_words:
            censored.append("*" * len(word))  
        else:
            censored.append(word)
    return " ".join(censored)

print("Chat Moderation System")
print("Type 'exit' to stop chatting.\n")

while True:
    msg = input("Enter message: ")
    if msg.lower() == "exit":
        print("exitted chat")
        break
    moderated = censor_message(msg)
    chat_history.append(moderated)

    print("\n--- Chat History ---")
    for line in chat_history:
        print(line)
    print("--------------------\n")