import urllib

def read_text():
    #quotes = open('C:\Users\Zachary\Documents\GitHub\PythonPractice\string\movie_quotes.txt')
    quotes = open(r'C:\Users\Zachary\Documents\GitHub\PythonPractice\addvideotopage\movie_quotes.txt') 
    #add 'r' in front of path to indicate the raw string type of path. It prevent IOError when run the code.
    contents_of_file = quotes.read()
    #print (contents_of_file)
    quotes.close()
    check_profanity(contents_of_file)

def check_profanity(text_to_check):
    #"urllib" module help to get information from the internet
    #"urllib.urlopen" function, it takes a link to a website.
    connection = urllib.urlopen(" http://www.wdyl.com/profanity?q=" + text_to_check)
    output = connection.read()
    print (output)
    connection.close()

read_text()