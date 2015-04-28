#get title from content input
def concept_title(concept):
	start_number = concept.find('Concept_Title:')
	end_number = concept.find('Concept_Description:')
	title = concept[start_number+14:end_number]
	return title

#get description from content input
def concept_description(concept):
	start_number = concept.find('Concept_Description:')
	description = concept[start_number+21:]
	return description

#get title and description by concept number
def get_concept_by_number(text, concept_number):
    n = concept_number
    concept_count = 0
    while concept_count < n:
        start_location = text.find('Concept_Title:')
        end_location = text.find('Concept_Title:',start_location+1)
        if end_location == -1:
            current_text = text[start_location:]
            break
        current_text = text[start_location:end_location]
        text = text[end_location:]
        concept_count = concept_count + 1
    return current_text

def generate_html_format(title, description):
	htme1 = ''''
	<div class="concept">
	    <h3>''' + title + '</h3>'
	html2 = '<div class="des_concept">' + description
	html3 = '</div></div>'
	full_html = html1 + html2 + html3
	return full_html


concept_input = '''
Concept_Title:Computer
Concept_Description:
Most machines (like a toaster) are designed to do a few things.
Unless you physically alter these machines, they will only be able to do those things.
Computers are different.
A computer can be programmed to do anything we want, as long as we can write a program that specifies a specific sequence of instructions.
Concept_Title:Program
Concept_Description:
A program is a precise sequence of steps that a computer can follow to do something useful. Web browsers, games, mobile apps, and simple print statements are all examples of computer programs.
Concept_Title:Programming Languages
Concept_Description:
A programming language is what programmers use to tell a computer what to do. Python is one example of a programming language.
Concept_Title:Interpreter
Concept_Description:
An interpreter is a computer program that directly executes, i.e. performs, instructions written in a programming or scripting language, without previously compiling them into a machine language program.'''


print concept_title(get_concept_by_number(concept_input, 3))
print concept_description(get_concept_by_number(concept_input, 3))

