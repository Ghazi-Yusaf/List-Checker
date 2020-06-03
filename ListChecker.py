from prettytable import PrettyTable
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

# Open file and add each line to list
with open("Lists/UserList.txt", "r") as file:
    userList = [line.strip() for line in file]

# Find user input
userInput = input("\nEnter the list of ingredients, each seperated by commas, to compare to user list and find matches:\n\n")

# Split user input (comma seperated) into list
productList = userInput.split(",")

# Tables for pretty output
matches = PrettyTable(["Ingredient"])
closeMatches = PrettyTable(["Product Ingredient", "User Ingredient", "Similarity Ratio (0-100)"])
closeMatches.reversesort = True

# Loop through input list
for item in productList:
    # Loop through user list
    for itemCheck in userList:
        # Check for direct matches to ingredients
        if fuzz.WRatio(item, itemCheck) == 100:
            matches.add_row([itemCheck])
            break
        # Check for similar matches to ingredients
        if fuzz.WRatio(item, itemCheck) >= 90:
            closeMatches.add_row([item, itemCheck, fuzz.WRatio(item, itemCheck)])
            break

# Sort similar matches by most similar to least similar
closeMatches.sortby = "Similarity Ratio (0-100)"

# Print tables
print("\nDirect matches:")
print(matches)
print("\nSimilar matches (Similarity ratio over 90), use your own discretion:")
print(closeMatches)
print()