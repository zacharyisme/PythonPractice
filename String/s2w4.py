# Now you'll write the get_concept_by_number function.
# It will take 2 inputs. The first will be text (like 
# in the EXAMPLE_TEXT) shown below. The second will be
# a number. If that number is 1, the function should 
# return the FIRST concept. If it's 2, the second... 
# This is a HARD problem. Give it a shot, but don't worry
# if you don't get it. You'll see the solution next.

EXAMPLE_TEXT = """TITLE: Why Computers are Stupid
DESCRIPTION: The phrase "computers are stupid" refers 
to how they interpret instructions literally. This 
means that small typos can cause big problems.
TITLE: Python
DESCRIPTION: Python is a "programming language." It 
provides programmers a way to write instructions for a 
computer to execute in a way that the computer can understand.
TITLE: While Loops
DESCRIPTION: A while loop repeatedly executes the body of
the loop until the "test condition" is no longer true."""

def get_concept_by_number(text, concept_number):
    n = concept_number
    concept_count = 0
    while concept_count < n:
        start_location = text.find('TITLE:')
        end_location = text.find('TITLE:',start_location+1)
        if end_location == -1:
            current_text = text[start_location:]
            break
        current_text = text[start_location:end_location]
        text = text[end_location:]
        concept_count = concept_count + 1
    return current_text

# you'll know you've solved the problem when the code below
# prints:
'''
   TITLE: Python
   DESCRIPTION: Python is a "programming language." It 
   provides programmers a way to write instructions for a 
   computer to execute in a way that the computer can understand.
'''
print get_concept_by_number(EXAMPLE_TEXT, 2)
