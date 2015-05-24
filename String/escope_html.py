## hand made
# def escope_html(s):
#     for (i, o) in (("&", "&amp;"),   #this "&" should put in front of other element or it will replace others "&".
#                    (">", "&gt;"),
#                    ("<", "&lt;"),
#                    ('"', "&quot;")):
#         s = s.replace(i, o)
#     return s

# print escope_html('"<b>html!</b>"')

## import cgi function
import cgi
def escape_html(s):
    return cgi.escape(s, quote = True)

print escape_html('"<b>html!</b>"')
