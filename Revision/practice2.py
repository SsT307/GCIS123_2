'''
Write a recursie Python function nmed is_plaindrome that checks whether a give string is a palindrome. 
A plaindrome is a word, phrase, or sequence that reads the same backward as forward (ignoring case and spaces).
'''
'''\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ PRACTICE FIBINOCCI SEQUENCE \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\'''

def is_palindrome(phrase):
    phrase = phrase.lower()
    if len(phrase)>1:
        if phrase[0] == phrase[-1]:
            is_palindrome(phrase[1:-1])
        else: return False
    return True
        
print(is_palindrome('anAnanana'))