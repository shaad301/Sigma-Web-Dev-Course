# import google.generativeai as genai

# API_KEY = "AIzaSyA9oeksNw9k6yyGldZdwfeVHaLy-i_25Lk" 
# genai.configure(api_key=API_KEY)

# model = genai.GenerativeModel("gemini-pro")
# chat = model.start_chat()

# print("Chat with Gemini! Type 'exit' to quit.")
# while True:
#     user_input = input("You: ")
#     if user_input.lower() == 'exit':
#         break
#     response = chat.send_message(user_input)
#     print("Gemini:", response.text)


import google.generativeai as genai

genai.configure(api_key="AIzaSyA9oeksNw9k6yyGldZdwfeVHaLy-i_25Lk")

model = genai.GenerativeModel("models/gemini-1.5-pro")

chat = model.start_chat()

print("Chat with Gemini! Type 'exit' to quit.")

while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("Goodbye!")
        break

    response = chat.send_message(user_input)
    print("Gemini:", response.text)


