#Xerini Technical Interview Code
#Written in python 3.7.4
#Open file and store in list format
listedWords = []
txtfile = open("english.txt",'r')
for line in txtfile:
    listedWords.append(line)
txtfile.close()

'''Quick Note:
    When using .append, the length of each word from the txt file is increased by 1. This is because
    there is a new line ('\n') char added in the list before the comma so later on when comparing the length
    of the passed string and the known strings, I will reduce the value of the length of the known 
    strings by 1.
'''
#Create functions:

#one fucntion to split the total list into only those of the same length as the passed word
def splitListByLength(length):
    reducedList = []
    for word in listedWords:
        if len(word) - 1 == length:
            reducedList.append(word)
    return reducedList



def checkAnagram(string):
    if type(string) != str:
        return ("Invalid variable type passed, Please only pass in Strings")
    valid_chars = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    listOfAnagrams = []
    lenString = len(string)
    #Use the split list function to get the words of same length
    reducedList = splitListByLength(lenString)
    #Now we reduce the passed string into seperate characters
    stringAsChars = list(string.lower())
    #check for invalid chars
    for ch  in stringAsChars:
        if ch not in valid_chars:
            return "Invalid character passed within String"
    for word in reducedList:
        #the last char is removed from word as it is '\n'
        wordAsChars = list(word.lower())[:-1]
        #set as true until proven otherwise
        anagram = True
        #checks each character in the passed string against the characters of the known words
        for char in stringAsChars:
            if char in wordAsChars:
                #remove the character if its triggered so that 2 of a letter in the passed string dont trigger on the same character
                wordAsChars.remove(char)
            else:
                #if one char doeesnt match then its not an anagram
                anagram = False
        
        if anagram:
            listOfAnagrams.append(word.lower()[:-1])
        
    return listOfAnagrams
    

def test_valid():
    assert checkAnagram("rabbit") == ['rabbit']
    assert checkAnagram("fried") == ['fired', 'fried']
    assert checkAnagram("juice") == ['juice']
    
    
def test_erroneous():
    assert checkAnagram(123) == "Invalid variable type passed, Please only pass in Strings"
    assert checkAnagram(True) == "Invalid variable type passed, Please only pass in Strings"
    assert checkAnagram(()) == "Invalid variable type passed, Please only pass in Strings"
    assert checkAnagram("ab$%") == "Invalid character passed within String"
    assert checkAnagram("£abe£") == "Invalid character passed within String"
    assert checkAnagram("&*():@{}") == "Invalid character passed within String"
    
    
def test_boundary():
    assert checkAnagram("") == []
    assert checkAnagram("a") == ['a']
    #Longer than any other word
    assert checkAnagram("googleplex") == []

    
