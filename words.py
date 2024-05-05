#Take input in the form string
sentence=input("Enter a sentence or paragraph:\n")
#splitting the input string
words=sentence.split()
def count_words(sentence):
    if not sentence:
        return 0
    #counting no.of words in the string
count=len(words)    
print("Number of words in given sentence or paragraph is:",count)