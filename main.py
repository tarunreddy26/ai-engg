import ollama
#import sys 
import json 


#try:
def fetch_response(messages):
    response = ollama.chat(
        model="llama3.2",
        messages=messages
    )
    reply = response["message"]["content"]
#except ConnectionError:
    #print('sorry, i cant reach ollama. is it still running')
#sys.exit()

    return reply


# The conversation history — starts empty, grows every turn
messages = []
messages.append({"role": "system", "content": "You are a super rich billionaire who answers every question in character."})

print("Chatbot ready. Type 'exit' or 'quit' to stop.\n")

try: 
    with open("conversation.json","r") as f:
        messages=json.load(f)

except FileNotFoundError:
    messages=[]
    messages.append({"role":"system","content":"You are a super rich billenere who answers every question in charecter"})
    
while True:
    # 1. Get input from the user
    user_input = input("You: ")

    # 2. Check for exit condition
    if user_input.lower() in ["exit", "quit"]:
        print("Goodbye!")
        break

    # 3. Add the user's message to the history
    messages.append({"role": "user", "content": user_input})

    try:
        reply=fetch_response(messages)
        print(f"Bot: {reply}\n")
        messages.append({"role": "assistant", "content": reply})
    except:
        print('sorry, i cant reach ollama. is it still running')

with open("conversation.json","w") as f:
    json.dump(messages,f)
        
            #print(f"Bot: {reply}\n")

    # 6. Add the model's reply to the history too
            #messages.append({"role": "assistant", "content": reply})