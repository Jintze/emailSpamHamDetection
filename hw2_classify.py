from hw2_prob import *
import os
import math

def evaluateEmail():
    path = "Data/test/test_Lemmatized"
    files= os.listdir(path)
    # probability_spam_words = {}
    # totalWordsNumSpam = 0
    n = 0
    hamEmail = []
    spamEmail = []
    probability_ham_words = {}
    probability_spam_words = {}
    for file in files:
        probOfHam = 0
        probOfSpam = 0
        fileContent = open(path+"/"+file, "r")
        words = fileContent.read()
        splitWords = words.replace('\n',' ').split(" ")

        for line in open("probability_spam_words.txt"): 
            splitLine = line.split(" ")
            splitLine[1] = splitLine[1][:-1]
            num = float(splitLine[1])
            # print(splitLine)
            # print(type(num))
            probability_spam_words[splitLine[0]] = num

        for x in splitWords:
            # print(probability_spam_words[x])
            if x in probability_spam_words:
                value = probability_spam_words[x]
                probOfSpam += math.log(value)
        
        for line in open("probability_ham_words.txt"): 
            splitLine = line.split(" ")
            splitLine[1] = splitLine[1][:-1]
            num = float(splitLine[1])
            # print(splitLine)
            # print(type(num))
            probability_ham_words[splitLine[0]] = num

        for x in splitWords:
            # print(probability_spam_words[x])
            if x in probability_ham_words:
                value = probability_ham_words[x]
                probOfHam += math.log(value)
        
        if probOfHam + math.log(220/259) > probOfSpam + math.log(39/259):
        # if probOfHam > probOfSpam:
            print(file + ' is Ham')
        else:
            print(file + ' is Spam')
            
    

    #     for x in range(len(splitWords)):
    #         wordToWrite = splitWords.pop(0)
    #         if wordToWrite in probability_spam_words:
    #             probability_spam_words[wordToWrite] += 1
    #         else:
    #             probability_spam_words[wordToWrite] = 1
                
    # for x,y in probability_spam_words.items():
    #     totalWordsNumSpam = totalWordsNumSpam + y
    # print(totalWordsNumSpam)
    # for x in probability_spam_words:
    #     if probability_spam_words[x] == 0:
    #         probability_spam_words[x] += 1
    #     probability_spam_words[x] = math.log((probability_spam_words[x])/totalWordsNumSpam)
    # for x,y in probability_spam_words.items():
    #     file = open("probability_spam_words.txt", "a")
    #     file.writelines(str(x) + ' ')
    #     file.writelines(str(y) + '\n')            

def main():
    evaluateEmail()

if __name__ == "__main__":
    main()