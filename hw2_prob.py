# I start this assignment today, so there are not so many codes yet.
# Most of the things I did during the lab are to figure out the 
# requirements of it and kinda have a plan of how will I make it.
import os
import math

def readFileHam():
    path = "Data/train/train_Lemmatized"
    files= os.listdir(path)
    probability_ham_words = {}
    totalWordsNumHam = 0
    for file in files:
        if file != '.DS_Store':
            if file[0] != 's':
                fileContent = open(path+"/"+file, "r")
                words = fileContent.read()
                splitWords = words.replace('\n',' ').split(" ")

                file = open("probability_ham_words.txt", "a")
                for x in range(len(splitWords)):
                    wordToWrite = splitWords.pop(0)
                    if wordToWrite in probability_ham_words:
                        probability_ham_words[wordToWrite] += 1
                    else:
                        probability_ham_words[wordToWrite] = 1
                
    for x,y in probability_ham_words.items():
        totalWordsNumHam = totalWordsNumHam + y
    print(totalWordsNumHam)
    for x in probability_ham_words:
        if probability_ham_words[x] == 0:
            probability_ham_words[x] += 1
        # probability_ham_words[x] = math.log((probability_ham_words[x])/totalWordsNumHam)
        probability_ham_words[x] = probability_ham_words[x]/totalWordsNumHam
    for x,y in probability_ham_words.items():
        file = open("probability_ham_words.txt", "a")
        file.writelines(str(x) + ' ')
        file.writelines(str(y) + '\n')      


def readFileSpam():
    path = "Data/train/train_Lemmatized"
    files= os.listdir(path)
    probability_spam_words = {}
    totalWordsNumSpam = 0
    for file in files:
        if file != '.DS_Store':
            if file[0] == 's':
                fileContent = open(path+"/"+file, "r")
                words = fileContent.read()
                splitWords = words.replace('\n',' ').split(" ")

                file = open("probability_spam_words.txt", "a")
                for x in range(len(splitWords)):
                    wordToWrite = splitWords.pop(0)
                    if wordToWrite in probability_spam_words:
                        probability_spam_words[wordToWrite] += 1
                    else:
                        probability_spam_words[wordToWrite] = 1
                
    for x,y in probability_spam_words.items():
        totalWordsNumSpam = totalWordsNumSpam + y
    print(totalWordsNumSpam)
    for x in probability_spam_words:
        if probability_spam_words[x] == 0:
            probability_spam_words[x] += 1
        # probability_spam_words[x] = math.log((probability_spam_words[x])/totalWordsNumSpam)
        probability_spam_words[x] = probability_spam_words[x]/totalWordsNumSpam
    for x,y in probability_spam_words.items():
        file = open("probability_spam_words.txt", "a")
        file.writelines(str(x) + ' ')
        file.writelines(str(y) + '\n')              

def main():
    readFileHam()
    readFileSpam()

if __name__ == "__main__":
    main()