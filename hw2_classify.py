import os
import math

# Assignment #2
# Spam filtering using Bayes model
# 
# AUCSC 460
# Author: Jinzhe Li
# Instructor: Mi-Young Kim
# 
# This Python program uses Bayes model to do Spam filtering.

# Based on what was written to txt file in hw2_prob.py, tell if an email is ham or spam.
def evaluateEmail():
    path = "Data/test/test_Lemmatized"
    files= os.listdir(path)
    n = 1
    probability_ham_words = {}
    probability_spam_words = {}

    # For each file in test_Lemmatized.
    for file in files:
        probOfHam = 0
        probOfSpam = 0

        # Get all txt files that are in test_Lemmatized.
        fileContent = open(path+"/"+file, "r")
        words = fileContent.read()
        splitWords = words.replace('\n',' ').split(" ")

        #Get spam data in probability_spam_words.txt.
        for line in open("probability_spam_words.txt"): 
            splitLine = line.split(" ")
            splitLine[1] = splitLine[1][:-1]
            num = float(splitLine[1])
            probability_spam_words[splitLine[0]] = num

        # Print the first line of outputx.txt (P(Spam, all words)).
        fileOutput = open("Output" + str(n) + ".txt", "a")
        fileOutput.writelines("P(Spam, " + words + ')\n')

        # Print P(word|Spam) = probability for each word.
        for x in splitWords:
            if x in probability_spam_words:
                value = probability_spam_words[x]
                probOfSpam += value
                fileOutput.writelines("P('" + x + "'|Spam) = " + str(value) + "\n")
        # Print log P(Spam, all words) = probability
        fileOutput.writelines("log P(Spam, " + words + ") = " + str(math.log(probOfSpam)) + "\n\n")

        #Get spam data in probability_ham_words.txt.
        for line in open("probability_ham_words.txt"): 
            splitLine = line.split(" ")
            splitLine[1] = splitLine[1][:-1]
            num = float(splitLine[1])
            probability_ham_words[splitLine[0]] = num
        
        # Print the first line of outputx.txt (P(Ham, all words)).
        fileOutput.writelines("P(Ham, " + words + ')\n')

        # Print P(word|Ham) = probability for each word.
        for x in splitWords:
            if x in probability_ham_words:
                value = probability_ham_words[x]
                probOfHam += value
                fileOutput.writelines("P('" + x + "'|Hpam) = " + str(value) + "\n")
        # Print log P(Ham, all words) = probability
        fileOutput.writelines("log P(Ham, " + words + ") = " + str(math.log(probOfHam)) + "\n\n")
        
        # Tell if a file is spam or ham.
        if probOfHam + 220/259 > probOfSpam + 39/259:
            fileOutput.writelines("Conclusion: This message is classified as Ham.\n")
        else:
            fileOutput.writelines("Conclusion: This message is classified as Spam.\n")
        n += 1
                   

def main():
    evaluateEmail()

if __name__ == "__main__":
    main()