"""check whether if string is palindrome"""


def is_string_palindrome(text: str) -> bool:
    """check whether string is palindrome
    text (str): input text
    bool: True check input text is palindrome otherwise False
    """
    text = text.lower().replace(" ","")
    left = 0
    right = len(text) - 1
    while left < right:
        if text[left] != text[right]:
            return False
        left += 1
        right -= 1
    return True


if __name__ == "__main__":
    input_text = input("Enter a text: ")
    if is_string_palindrome(input_text):
        print("{} is a palindrome".format(input_text))
    else:
        print("{} is not a palindrome".format(input_text))
