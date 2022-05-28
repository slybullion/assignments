# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here
    word=input("enter a word: ")
    anagram=input("enter the second word:")
    if (sorted(word)==sorted(anagram)):
        print(word, " and ", anagram, "are anagrams")
    else:
        print (word," and ",anagram,"are not anagrams")

        
find_anagram(" word"," anagram")
