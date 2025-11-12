# A passage cleaner that replaces specified text in a given passage.

print("Welcome to the Passage Cleaner!")

text_1 = input("What do you want to replace?")
text_2 = input(f"What do you want to replace {text_1} with?")

passage = input("Enter your passage: ")

passage = passage.replace(text_1, text_2)

print(f"Cleaned passage: {passage}")
