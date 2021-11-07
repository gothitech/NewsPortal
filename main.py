# Python3 program for the
# above approach
import re


# Function to remove the HTML tags
# from the given tags
def RemoveHTMLTags(strr):
    # Print string after removing tags
    print(re.compile(r'<[^>]+>').sub('', strr))

strr = "<div><b>Geeks for Geeks</b></div>"

#
# # Driver code
# if __name__ == '__main__':
#     # Given String
#     strr = "<div><b>Geeks for Geeks</b></div>"
#
#     # Function call to print the HTML
#     # string after removing tags
#     RemoveHTMLTags(strr);
#
# # This code is contributed by vikas_g