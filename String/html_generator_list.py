def generate_concept_HTML(concept_title, concept_description):
    html_text_1 = '''
<div class="concept">
    <h3>
        ''' + concept_title
    html_text_2 = '''
    </h3>
    <div class="des_concept">
        ''' + concept_description
    html_text_3 = '''
    </div>
</div>'''

def make_HTML(concept):
	concept_title = concept[0]
	concept_description = concept[1]
	return generate_concept_HTML(concept_title, concept_description)

my_list = [ ['Python', 'Python is a Programming Language'],
                             ['For Loop', 'For Loops allow you to iterate over lists'],
                             ['Lists', 'Lists are sequences of data'] ]

def make_HTML_from_concepts(concepts_list):
	html = []
	for i in concepts_list:
		concept_html = make_HTML(i)
		html = html + concept_html
	return html

print make_HTML_from_concepts(my_list)
