#Practice Drills and Exercises for Phase 0 Foundation
#This file contains various drills and exercises to reinforce the concepts learned in Phase 0 Foundation.

#DRILL 01: DATA NAVIGATION
#Objective: Nested Indexing
#Constraint: Onle line of code only. No intermediate variables.

training_logs = [
    {
        "epoch": 1, 
        "errors": ["timeout", "overflow"]
    },
    {
        "epoch": 2, 
        "errors": ["underflow", "gradient_explode"]
    }
]

#Task:Exact syntax to extract "gradient_explode" from training_logs
print(training_logs[1]["errors"][1])  #Expected Output: gradient_explode

# #Drill 02: Function Scaffolding
# #Objective: Scope & Return Logic
# #Constraint: Watch indentation carefully.

# prompt_database = []
# #Your code here:
# def clean_and_store(raw_prompt):
#     cleaned_prompt = raw_prompt.strip().lower()
#     prompt_database.append(cleaned_prompt)
#     return cleaned_prompt  #Mistake: returning cleaned_prompt instead of integer length of list

#Drill 02 (Attempt 2): Function Scaffolding
#Objective: Scope & Return Logic
prompt_database = []
#Your code here:
def clean_and_store(raw_prompt):
    cleaned_prompt = raw_prompt.strip().lower()
    prompt_database.append(cleaned_prompt)
    return len(prompt_database)  #Corrected: returning integer length of list

#Drill 03: Loop Gauntlet
#Objective: While Loops & Break.
#Constraint: Handle capitlization inputs robustly.

while True:
    user_input = input("Enter command (type 'quit' to exit): ").strip().lower()
    if user_input == "sk-secret123":
        print("Access Granted.")
        break
    else:
        print("Access Denied")

#Drill 04: Synthesis Challenge
#Objective: Combine Loops, Functions, and Return Values.
#Prerequesite: Assume clean_and_store and prompt_database = []
#Pass items into clean_and_store and collect lengths into current_size

# incoming_stream = ["  DATA_01 ", "DATA_02", "  meta_prompt ", "context_window", "stop_token"]

# current_size = []
# for raw_prompt in incoming_stream:
#     size = clean_and_store(raw_prompt)
#     current_size.append(size)
#     if size == 3:
#         print("Batch Full.")
#         break

#Drill 05: The Token Counter
#Objective: Frequency Analysis (Dictionary Logic)
#Constraint: Count the list of raw tokens manually (without counter or get())

token_stream = ["user", "system", "user", "user", "system"]
token_counts = {}

for token in token_stream:
    if token in token_counts:
        token_counts[token] += 1
    else:
        token_counts[token] = 1
