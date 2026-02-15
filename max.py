def count_vowels_and_consonants(string):
    vowels = "aeiouAEIOU"
    num_vowels = 0
    num_consonants = 0
    
    for char in string:
        if char.isalpha():  # Check if the character is a letter
            if char in vowels:
                num_vowels += 1
            else:
                num_consonants += 1
    
    return num_vowels, num_consonants

# Input from the user
input_string = input("Enter a string: ")

# Count vowels and consonants
vowels, consonants = count_vowels_and_consonants(input_string)

# Display the results
print(f"Total number of vowels: {vowels}")
print(f"Total number of consonants: {consonants}")