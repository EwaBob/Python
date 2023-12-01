# ligatury włączone ustawienia -> editor -> font -> enable ligatures -> czcionka |JetBrains Mono

#towrzę funkcje o nazwie Get Input, ktora przyjmuje typ slowa
def get_input(word_type: str):
    user_input: str = input(f"Enter a {word_type}:")
    return user_input

noun1 = get_input("noun")
adjective1 = get_input("adjective")
verb1 = get_input("verb")
noun2 = get_input("noun")
verb2 = get_input("verb")

story = f"""
Once upon a time, there was a {noun1} who loved to {verb1} all day.
One day, "{noun2} walked into the room and caught the {noun1} in the act. 

{noun2}: "What are you doing?"
{noun1}: :I am just {verb1}ing, what's the big deal?
{noun2}: "Well, it is not every day that you see a {noun1} {verb1}ing in the middle og the day."
{noun1}: " I guess you are right. Maybe I should take a break."
{noun2}: "That is probably a good idea. Why do not we go {verb2} instead?"
{noun2}: "Sure, that's sounds like fun!"
 
 And so {noun2} and the {noun1} wnt off to {verb2} and had a great time. 
 The end
"""

print(story)

