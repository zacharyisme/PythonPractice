#String test
# s = 'audacity'
# print 'U'+s[2:]

#Write python code that prints out the number of hours in 7 weeks.
# weeks=7
# d_week=7
# h_day=24
# hours_in_7weeks=weeks*d_week*h_day
# print hours_in_7weeks

#combind two strings to one string.
# s='udacity'
# t='bodacious'
# new_s = s[0]
# new_t = t[2:]
# new_string = new_s + new_t
# print new_string

#find second string position of a string, if no second string, print -1.
# text = 'all zip files are zipped'
# first_sting_posotion = text.find('zip')
# second_string_position = text.find('zip',first_sting_posotion+1)
# print second_string_position

#Define procedure, square, that takes one number as its input, and reurn the square of that number.
# def square(n):
# 	answer = n*n
# 	return answer
# print square(5)

#abba procedure
# def abbaize(a, b):
# 	return a+(b*2)+a

# print abbaize('a','b')
# print abbaize('dog','cat')

# def generate_html(c_title,c_des):
#     concept_class_start = '<div class="concept">'
#     concept_description_class_start = '<div clsss="des_concept">'
#     class_end = '</div>'
#     indent_space = ' '*4
#     print concept_class_start
#     print indent_space+c_title
#     print class_end
#     print concept_description_class_start
#     print indent_space+c_des
#     print class_end

# concept = 'This concept is generated automatically'
# description = 'This is a page generated through program by using python language.'
# generate_html(concept, description) #if function can print out, i don't need to use "print" to call function to provent show "none" in the end.

# #Define a procedure, bigger, that takes in
# #two numbers as inputs, and returns the
# #greater of the two inputs.
# def bigger (a, b):
# 	if a > b:
# 		return a
# 	return b
# print 'Bigger Number is '+ str(bigger(9, 5))


# def is_friend(name):
# 	first_character=name[0]
# 	if first_character == 'D':
# 		return 'True'
# 	if first_character == 'N':
# 		return 'True'
# 	else:
# 		return 'False'
# print is_friend('Ned')

##Print out the biggest number.
# def biggest (a, b, c):
# 	if a < b:
# 		if b < c:
# 			return c
# 		return b
# 	else:
# 		if a < c:
# 			return c
# 		return a
# print biggest(8,11,10)

##Defind print numbers
# def print_num(n):
# 	i = 0
# 	while i != n:
# 		i = i+1
# 		print i
# print_num(0)

##Days in Month (List practice)
days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]
def how_many_days(month):
	days = days_in_month[month-1]
	return days
print how_many_days(2)