# HW3.4 PyParagraph

import os
import re

# Make sure the current working directory is same as .py file location
path = os.path.abspath(os.path.dirname(__file__))

# Set path for files
pypara = os.path.join(path, "PyParagraph.txt")

with open(pypara, "r") as txtfile:
    txtreader = txtfile.readlines()

#Determine the number of words in the paragraph    
    for word in txtreader:
        words = word.split(" ")

#Determine the average letters per word
    total_letters = 0
    for n in words:
        letters = n.split()
        total_letters = int(total_letters + len(n))

#Determine the number of sentences
    for line in txtreader:
        sentences = line.split(".")

print("\nText Analysis")
print("--------------------------------")
print("Word count: " + str(len(words)))
print("Sentence count: " + str(int(len(sentences) - 1)))
print("Average letters per word: " + str(round(total_letters / int(len(words)), 1)))
print("Average words in sentence: " + str(round(int(len(words)) / int(len(sentences) - 1), 1)))

# Export output to a .txt file
filename_path = os.path.join(path, "PyParagraph_Output.txt")
with open(filename_path, "w") as output:
    output.write("\nText Analysis")
    output.write("\n--------------------------------")
    output.write("\nWord count: " + str(len(words)))
    output.write("\nSentence count: " + str(int(len(sentences) - 1)))
    output.write("\nAverage letters per word: " + str(round(total_letters / int(len(words)), 1)))
    output.write("\nAverage words in sentence: " + str(round(int(len(words)) / int(len(sentences) - 1), 1)))
