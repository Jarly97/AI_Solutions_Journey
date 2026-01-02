# # Context: RPG Character Sheet
# # Curly Brackets {} denote a dictionary

# player_stats = {
#     "name": "Zed",
#     "level": 1,
#     "hp": 100,
#     "is_alive": True
# }

# #Accessing data by "Key" (Label)
# print(player_stats["name"])
# print(player_stats["hp"] - 15)
# #Modifying data by "Key" (Label)
# player_stats["level"] = 2 
# player_stats["mana"] = 200  #Adding new key-value pair

# BATCH PROCESSING EXERCISE
# Context: Filtering a Chat Log
# This is how we process conversation history for APIs. 

# chat_log = [
#     {"role": "system", "content": "You are a helpful assistant."},
#     {"role": "user", "content": "Hello!"},
#     {"role": "ai", "content": "Hi there! how can I help?"},
#     {"role": "user", "content": "Explain Python loops."}
# ]

# print("---Human Messages---")

# #The Loop
# for message in chat_log:
#     #Logic: Check if 'role' is 'user'
#     if message["role"] == "user":
#         print(message["content"])

# # Exercise: Print all AI messages
# for message in chat_log:
#     #Logic: Check if 'role' is 'ai'
#     if message["role"] == "ai":
#         print(message["content"])

# #Exercise: Context Window- Memory Management
# #Context: Creating a memory manager for chat history 

# conversation_history = []

# for message in conversation_history:
#     print("Ask me Anything!")
#     while True:
#         if message["role"] == "user":
#             user = input("You: ")
#             conversation_history.append({"role": "user", "content": user})
#             if user == "exit":
#                 break
# print (conversation_history)

# # #Correction of the above exercise
# # Exercise: Context Window- Memory Management
# # Context: Creating a memory manager for chat history
# conversation_history = [] #start with an empty "memory"

# print("Ask me Anything! Type 'exit' to quit.")
# while True:
#     #Wait for user input
#     user_input = input("You: ")
#     #Check for exit condition
#     if user_input.lower() == "exit":
#         break
#     #Add user message to conversation history (Create a dictionary for the message)
#     conversation_history.append({"role": "user", "content": user_input})
#     #Final output of conversation history
# print ("---Final Chat History---")
# print (conversation_history)

# #Exercise: Wrapping  memory manager in a function
# # Context: Function to manage chat history 

# def start_chat_bot():
#     print ("Ask me Anything! Type 'exit' to quit.")
#     conversation_history = [] #start with an empty "memory"
#     while True:
#         #Wait for user input
#         user_input = input("You: ")
#         #Check for exit condition
#         if user_input.lower() == "exit":
#             break
#         #Add user message to conversation history (Create a dictionary for the message)
#         conversation_history.append({"role": "user", "content": user_input})
#     return conversation_history
#     #Final output of conversation history
# chat_history = start_chat_bot()
# print ("---Final Chat History---")
# print(chat_history)

# #Exercise: Adding a System role/Persona to the chat bot
# # Context: Function Arguments to manage chat history with system persona
# def start_chat_bot(system_prompt="You are a helpful assistant."):
#     print(system_prompt)
#     print ("Ask me Anything! Type 'exit' to quit.")
#     conversation_history = [
#         {"role": "system", "content": system_prompt}
#     ] # added system prompt to "memory" as function argument
#     while True:
#         #Wait for user input
#         user_input = input("You: ")
#         #Check for exit condition
#         if user_input.lower() == "exit":
#             break
#         #Add user message to conversation history (Create a dictionary for the message)
#         conversation_history.append({"role": "user", "content": user_input})
#     return conversation_history
#     #Final output of conversation history
# chat_history = start_chat_bot(system_prompt="You are a helpful assistant.")
# print ("---Final Chat History---")
# print(chat_history)