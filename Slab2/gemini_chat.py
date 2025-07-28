import google.generativeai as genai

genai.configure(api_key="YOUR_GEMINI_API_KEY")  # Replace with your actual API key

chat = genai.ChatModel().start_chat(history=[])

while True:
    msg = input("You: ")
    if msg.lower() == "exit":
        break
    response = chat.send_message(msg)
    print("Gemini:", response.text)
