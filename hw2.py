# I start this assignment today, so there are not so many codes yet.
# Most of the things I did during the lab are to figure out the 
# requirements of it and kinda have a plan of how will I make it.

def readFile():
    file = open("3-1msg1.txt", "r")
    words = file.read()
    splitWords = words.split(" ")
    print(splitWords)
    file = open("probability_ham_words.txt", "a")
    for x in range(len(splitWords)):
        wordToWrite = splitWords.pop(0)
        file.writelines(wordToWrite + "\n")
def main():
    readFile()

if __name__ == "__main__":
    main()