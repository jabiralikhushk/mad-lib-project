# Mad Libs Game in Python

# Step 1: Story Template with placeholders
story = """
Once upon a time in a land far away, there was a [adjective] dragon named [name].
This dragon loved to [verb] all day long, especially when it was [adjective] outside.
One day, the dragon met a [noun] who was very [adjective]. They became fast friends and decided to [verb] together.
"""

# Step 2: Ask the user for their input to fill in the placeholders
adjective1 = input("Enter an adjective: ")
name = input("Enter a name: ")
verb1 = input("Enter a verb: ")
adjective2 = input("Enter another adjective: ")
noun = input("Enter a noun: ")
adjective3 = input("Enter one more adjective: ")
verb2 = input("Enter another verb: ")

# Step 3: Replace the placeholders with the user's input
final_story = story.replace("[adjective]", adjective1, 1) \
                   .replace("[name]", name, 1) \
                   .replace("[verb]", verb1, 1) \
                   .replace("[adjective]", adjective2, 1) \
                   .replace("[noun]", noun, 1) \
                   .replace("[adjective]", adjective3, 1) \
                   .replace("[verb]", verb2, 1)

# Step 4: Display the final story
print("\nHere's your Mad Libs story:\n")
print(final_story)
