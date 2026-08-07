# --- Mad Libs Game: The Haunted Kitchen Chaos ---
print("Welcome to the New Python Mad Libs Game!")
print("Please enter the requested types of words to create a wild cooking story.\n")

# Gather the new inputs
noun1 = input("Enter a room or cooking appliance (Noun, e.g., kitchen, microwave): ")
adjective1 = input("Enter a strange texture or smell (Adjective, e.g., slimy, neon-green): ")
noun2 = input("Enter a type of food or ingredient (Noun, e.g., spaghetti, broccoli): ")
adjective2 = input("Enter a funny physical reaction (Adjective, e.g., terrified, dizzy): ")
verb = input("Enter a messy action word (Verb ending without 'ing', e.g., chop, juggle): ")
time = input("Enter a precise cooking time frame (e.g., 3 hours past midnight): ")


print(f"Today I went to the {noun1}.")
print(f"There I saw a {adjective1} {noun2}.")
print(f"I was so {adjective2} looking at that {noun2}, I couldn't stop {verb}ing.")
print(f"By then it was already {time} and I had to go back home.")