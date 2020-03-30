# from hw2_prob import *
import os
import math

def evaluateEmail():
    path = "Data/test/test_Lemmatized"
    files = os.listdir(path)
    # probability_spam_words = {}
    # totalWordsNumSpam = 0
    n = 1
    num = 0.0
    hamEmail = []
    spamEmail = []
    probability_ham_words = {}
    probability_spam_words = {}
    
    for file in files:
        currentWordsDict = {}
        probOfHam = 0
        probOfSpam = 0
        fileContent = open(path+"/"+file, "r")
        words = fileContent.read()
        splitWords = words.replace('\n',' ').split(" ")
        for x in range(len(splitWords)):
            wordToCalculate = splitWords.pop(0)
            if wordToCalculate in currentWordsDict:
                currentWordsDict[wordToCalculate] += 1
            else:
                currentWordsDict[wordToCalculate] = 1

        for line in open("probability_spam_words.txt"): 
            splitLine = line.split(" ")
            splitLine[1] = splitLine[1][:-1]
            num = float(splitLine[1])

            probability_spam_words[splitLine[0]] = num

        fileOutput = open("Output" + str(n) + ".txt", "a")
        fileOutput.writelines("P(Spam, " + words + ')\n')

        for x,y in currentWordsDict.items():
            if x in probability_spam_words:
                value = y * probability_spam_words[x]
                probOfSpam += math.log2(value)
                # probOfSpam += value
                fileOutput.writelines("P('" + x + "'|Spam) = " + str(value) + "\n")
        fileOutput.writelines("log2 P(Spam, " + words + ") = " + str(probOfSpam) + "\n\n")

        for line in open("probability_ham_words.txt"): 
            splitLine = line.split(" ")
            splitLine[1] = splitLine[1][:-1]
            num = float(splitLine[1])

            probability_ham_words[splitLine[0]] = num
        
        
        fileOutput.writelines("P(Ham, " + words + ')\n')

        for x,y in currentWordsDict.items():
            # print(probability_spam_words[x])
            if x in probability_ham_words:
                value = y * probability_ham_words[x]
                probOfHam += math.log2(value)
                # probOfHam += value
                fileOutput.writelines("P('" + x + "'|Hpam) = " + str(value) + "\n")
        fileOutput.writelines("log2 P(Ham, " + words + ") = " + str(probOfHam) + "\n\n")
        
        if probOfHam + math.log2(220/259) > probOfSpam + math.log2(39/259):
        # if probOfHam + 220/259 > probOfSpam + 39/259:
        # if probOfHam > probOfSpam:
            print(file + ' is Ham')
            fileOutput.writelines("Conclusion: This message is classified as Ham.\n")
        else:
            print(file + ' is Spam')
            fileOutput.writelines("Conclusion: This message is classified as Spam.\n")
        n += 1


def main():
    evaluateEmail()

if __name__ == "__main__":
    main()