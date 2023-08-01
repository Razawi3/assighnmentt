def is_vowel(character):
    vowels = ["a", "A", "e", "E", "i", "I", "O", "o", "U", "u"]
    if character in vowels:
        return True
    else:
        return False
print(is_vowel("a"))
print(is_vowel("t"))
