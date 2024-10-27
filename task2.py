from collections import deque

def is_palindrome(text):
    text = ''.join(filter(str.isalnum, text.lower().replace(" ", "")))
    deque_text = deque(text)
    
    while len(deque_text) > 1:
        if deque_text.popleft() != deque_text.pop():
            return False
            
    return True

# Перевірка 
print(is_palindrome("Racecar")) # True
print(is_palindrome("Madam, I'm Adam")) # True
print(is_palindrome("A Toyota's a Toyota")) # True
print(is_palindrome("Hello world")) # False