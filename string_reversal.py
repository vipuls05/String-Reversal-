user_input = input('Input a string: ')

def reverse(string):
    if isinstance(string, str) and string.strip():  # Ensure entered string isn't empty
        # Split the sentence into words then reverse each word and join them with spaces
        reversed_sentence = ' '.join(word[::-1] for word in string.split())
        print(reversed_sentence.lower())
    else:
        print("Please enter a valid non-empty string.")

reverse(user_input)


