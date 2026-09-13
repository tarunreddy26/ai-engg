import ollama

# The conversation history — starts empty, grows every turn
messages = []
messages.append({"role": "system", "content": "You are a super rich billenere who answers every question in charecter"})

print("Chatbot ready. Type 'exit' or 'quit' to stop.\n")

while True:
    # 1. Get input from the user
    user_input = input("You: ")

    # 2. Check for exit condition
    if user_input.lower() in ["exit", "quit"]:
        print("Goodbye!")
        break

    # 3. Add the user's message to the history
    messages.append({"role": "user", "content": user_input})

    # 4. Send the WHOLE history so far to the model
    response = ollama.chat(
        model="llama3.2",
        messages=messages
    )

    # 5. Pull out just the reply text
    reply = response["message"]["content"]
    print(f"Bot: {reply}\n")

    # 6. Add the model's reply to the history too
    messages.append({"role": "assistant", "content": reply})