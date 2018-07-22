#####################################################################
# Braden Harrelson
# Password Project
# CMPS 4663 Cyber Security
# Dr Halverson
# This program is designed to reduce our 20 dictionary file to not 
# have words smaller than 5 letters.
#####################################################################

#open the input and output files
inf = open("Dictionary20K.txt", "r")
outf = open("NewDict.txt", "w")
#loop through the words
for word in inf:
    #strip the hidden characters such as newlines
    word = word.strip()
    #if the length is 5 or more, write it to the new file
    if len(word) >= 5:
        outf.write(word + "\n")
#close the files
inf.close()
outf.close()