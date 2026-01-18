# #Practice Drills and Exercises for Phase 0 Foundation
#This file contains various drills and exercises to reinforce the concepts learned in Phase 0 Foundation.

# #DRILL 01: DATA NAVIGATION
# #Objective: Nested Indexing
# #Constraint: Onle line of code only. No intermediate variables.

# training_logs = [
#     {
#         "epoch": 1, 
#         "errors": ["timeout", "overflow"]
#     },
#     {
#         "epoch": 2, 
#         "errors": ["underflow", "gradient_explode"]
#     }
# ]

# #Task:Exact syntax to extract "gradient_explode" from training_logs
# print(training_logs[1]["errors"][1])  #Expected Output: gradient_explode

# #Drill 02: Function Scaffolding
# #Objective: Scope & Return Logic
# #Constraint: Watch indentation carefully.

# prompt_database = []
# #Your code here:
# def clean_and_store(raw_prompt):
#     cleaned_prompt = raw_prompt.strip().lower()
#     prompt_database.append(cleaned_prompt)
#     return cleaned_prompt  #Mistake: returning cleaned_prompt instead of integer length of list

# #Drill 02 (Attempt 2): Function Scaffolding
# #Objective: Scope & Return Logic
# prompt_database = []
# #Your code here:
# def clean_and_store(raw_prompt):
#     cleaned_prompt = raw_prompt.strip().lower()
#     prompt_database.append(cleaned_prompt)
#     return len(prompt_database)  #Corrected: returning integer length of list

# #Drill 03: Loop Gauntlet
# #Objective: While Loops & Break.
# #Constraint: Handle capitlization inputs robustly.

# while True:
#     user_input = input("Enter command (type 'quit' to exit): ").strip().lower()
#     if user_input == "sk-secret123":
#         print("Access Granted.")
#         break
#     else:
#         print("Access Denied")

# #Drill 04: Synthesis Challenge
# #Objective: Combine Loops, Functions, and Return Values.
# #Prerequesite: Assume clean_and_store and prompt_database = []
# #Pass items into clean_and_store and collect lengths into current_size

# incoming_stream = ["  DATA_01 ", "DATA_02", "  meta_prompt ", "context_window", "stop_token"]

# current_size = []
# for raw_prompt in incoming_stream:
#     size = clean_and_store(raw_prompt)
#     current_size.append(size)
#     if size == 3:
#         print("Batch Full.")
#         break

# #Drill 05: The Token Counter
# #Objective: Frequency Analysis (Dictionary Logic)
# #Constraint: Count the list of raw tokens manually (without counter or get())

# token_stream = ["user", "system", "user", "user", "system"]
# token_counts = {}

# for token in token_stream:
#     if token in token_counts:
#         token_counts[token] += 1
#     else:
#         token_counts[token] = 1

# #Drill 06: Spec Adherence
# #Objective: Follow Specifications Precisely of Return vs Print
# #Constraint: Write a function called calculate_loss that takes a number error_val.
# def calculate_loss(error_val):
#     loss = error_val ** 2
#     return loss 

# #Task A (Fixing Drill 02): Write a while loop that counts from 1 to 5.

# #Inside the loop, print the current number.

# #Outside the loop (after it finishes), print "Done".

# #Constraint: Do NOT use break. Use indentation.
# number = 0
# while number <= 5:
#     print(number)
#     number += 1
# print("Done")


# #Set 2: Extra Practice Drills for Phase 0 Foundation
# #Drill 01: Navigating Nested Structures and updating data
# #Task: Update list of stop words with string "SYSTEM"

# model_config = {
#     "name": "GPT-4-Turbo",
#     "params": {
#         "temperature": 0.7,
#         "stop_words": ["<end>", "USER:"]
#     }
# }
# model_config["params"]["stop_words"].append("SYSTEM")

# #Drill 02: Iteration and Conditional Logic
# #Task: Loop through list of raw scores and append High Confidence list with scores above 0.8 else do nothing.

# raw_scores = [0.95, 0.4, 0.88, 0.12, 0.99]
# high_confidence = []
# for score in raw_scores:
#     if score > 0.8:
#         high_confidence.append(score)
#     else:
#         pass

# #Drill 03: Function Definition and Return Values
# #Task: Write a funcion called calculate_accuracy that takes two parameters: correct_predictions and total_predictions. The function should return the accuracy as a float.

# def calculate_accuracy(correct_predictions, total_predictions):
#     accuracy = correct_predictions / total_predictions
#     return accuracy

# #Drill 04: While Loop with User Input
# #Task: Write a while loop that keeps running until "generated_seeds" length reaches 3. Inside loop, generated a random seed (integer between 1 and 100) and append to list.

# import random
# generated_seeds = []
# while len(generated_seeds) < 3:
#     seed = random.randint(1, 100)
#     generated_seeds.append(seed)

# #Drill 05: Filter Function
# #Task: Create a clean batch list that filters from raw data with intergers over 0 only.

# input_list = [10, -5, 0, 23, -1, 7, -3]
# def filter_clean_data(input_list):
#     clean_batch = []
#     for item in input_list:
#         if item > 0:
#             clean_batch.append(item)
#     return clean_batch

# #Drill 06: Final Exam - Manual Mode 
# #Task: Calculate API Bill 

# model_costs = {"gpt-4": 0.03, "gpt-3.5": 0.002}
# usage_logs = [
#     {"model": "gpt-4", "tokens": 100},
#     {"model": "gpt-3.5", "tokens": 1000},
#     {"model": "llama-2", "tokens": 500} # TRAP: Not in cost dict
# ]

# def calculate_bills(usage_logs, model_costs):
#     total_bill= 0
#     for log in usage_logs:
#         model = log["model"]
#         tokens = log["tokens"]
#         if model in model_costs:
#             cost = model_costs[model]
#             total_bill += tokens * cost
#         else:
#             pass
#     return total_bill
# total_bill = calculate_bills(usage_logs, model_costs)