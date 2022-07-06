""" Problem
Write a function called is_palindrome that takes a string as a parameter. The function will return True if the string is a palindrome (is the same forward and backward). The function will return False if the string is not a palindrome.
Expected Output
If the function call is is_palindrome("level"), the the function would return True
If the function call is is_palindrome("house"), the the function would return False
Important
Do not use a helper function for this problem. Though this is good situation in which to use one, the auto-grader only works if all of the coding is done inside the is_palindrome function. """

def is_palindrome(pali):
    if pali == pali[::-1]:
        return True
    else:
        return False
