'''Write a Python function that checks whether a word or phrase is palindrome or not. 
Note: A palindrome is word, phrase, or sequence that reads the same backward as forward, e.g., madam'''

word = input()

def isPalindrome(word):
    if word == word[::-1]:
        print(True)
    else:
        print(False)

isPalindrome(word)