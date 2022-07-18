import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)  # Returns a Match object if there is a match anywhere in the string
if x:
  print("YES! We have a match!")
else:
  print("No match")

# The search() function searches the string for a match, and returns a Match object if there is a match.
# If there is more than one match, only the first occurrence of the match will be returned:
d = "The rain in Spain"
rain = re.search(r"\s", d)
print("The first white-space character is located in position:", rain.start()) 




# The findall() function returns a list containing all matches.
# FIND-ALL
a = re.findall("[a-z]", txt) # #Find all lower case characters alphabetically between "a" and "z":
print(a)


dollar = "That will be 59 dollars"
b = re.findall("\d", dollar) #Find all digit characters:
print(b)



text = "The rain in Spain falls mainly in the plain!"
c = re.findall("falls|stays", text) # Check if the string contains either "falls" or "stays":
print(c)
if c:
  print("Yes, there is at least one match!")
else:
  print("No match")



# The split() Function
# The split() function returns a list where the string has been split at each match:
#Split the string at every white-space character:
space = "The rain in Spain"
v = re.split(r"\s", space)
w = re.split(r"\s", space, 1) # Split the string only at the first occurrence: # You can control the number of occurrences by specifying the maxsplit parameter:
print(v)
print(w)



# The sub() Function
# The sub() function replaces the matches with the text of your choice:
# Replace every white-space character with the number 9:
replace = "The rain in Spain"
o = re.sub(r"\s", "9", replace) # \s is whitespace count, so it got replaced with 9.
p = re.sub("rain", "sun", replace) # here rain got replaced with sun
print(o)
print(p)

# You can control the number of replacements by specifying the count parameter:
az = "The tropical of Amazon"
i = re.sub(r"\s", "|", az, 2) # 2 whitespace got replaced by "|". 
print(i)


# Match Object
# A Match Object is an object containing information about the search and the result.
# Note: If there is no match, the value None will be returned, instead of the Match Object.
s = "The sound in Silence"
z = re.search("un", s)
print(z) #this will print an object

# The Match object has properties and methods used to retrieve information about the search, and the result:
# .span() returns a tuple containing the start-, and end positions of the match.
# The regular expression looks for any words that starts with an upper case "S":
earth = "Nature is Natural"
n = re.search(r"\bN\w+", earth) # Why does it always ends with extra index? (QUESTION) 
print(n.span()) #Search for an upper case "S" character in the beginning of a word, and print its position:


# .string returns the string passed into the function
# Print the string passed into the function:
beauty = "Beauty with Brains"
h = re.search(r"\bB\w", beauty) # #The string property returns the search string:
print(h.string)


# .group() returns the part of the string where there was a match
gru = "Aero group was not reported still on Ground"
g = re.search(r"\br\w+", gru) #Search for an upper case "r" character in the beginning of a word, and print the word.
print(g.group()) # returns (reported)





example = 'an example word:cat!!'
match = re.search(r'word:\w\w\w', example)
# If-statement after search() tests if it succeeded
if match:
  print('found', match.group()) ## 'found word:cat'
else:
  print('did not find')


# BASIC EXAMPLES
# Search for pattern 'iii' in string 'piiig'.
# All of the pattern must match, but it may appear anywhere.
# On success, match.group() is matched text.
match1 = re.search(r'iii', 'piiig') # found, match.group() == "iii"
match2 = re.search(r'igs', 'piiig') # not found, match == None
# . = any char but \n
match3 = re.search(r'..g', 'piiig') # found, match.group() == "iig"
# \d = digit char, \w = word char
match4 = re.search(r'\d\d\d', 'p123g') # found, match.group() == "123"
match5 = re.search(r'\w\w\w\w', '@@abcd!!') # found, match.group() == "abc"
print(match1, "Match1") 
print(match2, "Match2")
print(match3, "Match3")
print(match4, "Match4")
print(match5, "Match5")


# REPETITION EXAMPLES
# i+ = one or more i's, as many as possible.
match6 = re.search(r'pi+', 'piiig') # found, match.group() == "piii"
print(match6, "Match6")

# Finds the first/leftmost solution, and within it drives the +
# as far as possible (aka 'leftmost and largest').
# In this example, note that it does not get to the second set of i's.
match7 = re.search(r'i+', 'piigiiii') # found, match.group() == "ii"
print(match7, "Match7")

# \s* = zero or more whitespace chars
# Here look for 3 digits, possibly separated by whitespace.
match8 = re.search(r'\d\s*\d\s*\d', 'xx1 2   3xx') # found, match.group() == "1 2   3"
match9 = re.search(r'\d\s*\d\s*\d', 'xx12  3xx') # found, match.group() == "12  3"
match10 = re.search(r'\d\s*\d\s*\d', 'xx123xx') # found, match.group() == "123"
print(match8, "Match8")
print(match9, "Match9")
print(match10, "Match10")

# ^ = matches the start of string, so this fails:
match11 = re.search(r'^b\w+', 'foobar') # not found, match == None
# but without the ^ it succeeds:
match12 = re.search(r'b\w+', 'foobar') # found, match.group() == "bar"
print(match11, "Match11")
print(match12, "Match12")


# EMAIL EXAMPLES
email = 'purple alice-b@google.com monkey dishwasher'
match = re.search(r'\w+@\w+', email)
if match:
    print(match.group())  # 'b@google'


# SQUARE BRACKETS EXAMPLES
alice = 'purple alice-b@google.com monkey dishwasher'
match = re.search(r'[\w.-]+@[\w.-]+', alice)
if match:
    print(match.group())  ## 'alice-b@google.com'


# GROUP EXTRACTIONS
extract = 'purple alice-b@google.com monkey dishwasher'
match = re.search(r'([\w.-]+)@([\w.-]+)', extract)
if match:
    print(match.group())   # 'alice-b@google.com' (the whole match)
    print(match.group(1))  # 'alice-b' (the username, group 1)
    print(match.group(2))  # 'google.com' (the host, group 2)



##### FINDALL ###########
## Suppose we have a text with many email addresses
monkey = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher'
## Here re.findall() returns a list of all the found email strings
emails = re.findall(r'[\w\.-]+@[\w\.-]+', monkey) ## ['alice@google.com', 'bob@abc.com']
for email in emails:
    print(email) # do something with each found email string


# # FINDALL WITH FILES
# # Open file
# f = open('rahul_code.py', 'r') # This is a example
# # Feed the file text into findall(); it returns a list of all the found strings
# strings = re.findall(r'some pattern', f.read())

# FINDALL AND GROUPS
blue = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher'
tuples = re.findall(r'([\w\.-]+)@([\w\.-]+)', blue)
print(tuples)  ## [('alice', 'google.com'), ('bob', 'abc.com')]
for tuple in tuples:
    print(tuple[0])  ## username
    print(tuple[1])  ## host
