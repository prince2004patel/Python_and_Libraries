### LEVEL 2

## 1. Create a variable message with the value. Print the variable.

# message = "Hello, World!"
# print(message)

## 2. Ask the user to enter their name and print the number of characters using len().

# name = input("Enter your name: ")
# print("The number of characters in your name is:", len(name))

## 3. Given: text = "Data Science" Print: First character Last character Fifth character

# text = "Data Science"
# print("First character:", text[0])
# print("Last character:", text[-1])
# print("Fifth character:", text[4])

## 4. Using: text = "MachineLearning" Print: "Machine" "Learning" Every second character

# text = "MachineLearning"
# print("First part:", text[:7])
# print("Second part:", text[7:])
# print("Every second character:", text[::2])

## 5. Ask the user to enter a sentence and print: All uppercase All lowercase Title case

# sentence = input("Enter a sentence: ")
# print("Uppercase:", sentence.upper())
# print("Lowercase:", sentence.lower())
# print("Title case:", sentence.title())

## 6. Given text and Remove leading and trailing spaces and print the cleaned string.

# text ="    Python is fun    "
# cleaned_text = text.strip()
# print("Cleaned string:", cleaned_text)

## 7. Give sentence and Replace "Java" with "Python".

# sentence = "I love Java programming."
# updated_sentence = sentence.replace("Java", "Python")
# print("Updated sentence:", updated_sentence)

## 8. Ask the user to enter a sentence and count how many times the letter 'a' appears.

# sentence = input("Enter a sentence: ")
# count_a = sentence.count('a')
# print("The letter 'a' appears", count_a, "times in the sentence.")

## 9. Given a filename from the user, check whether: It starts with "data" It ends with ".csv"

# filename = input("Enter a filename: ")

# starts_with_data = filename.startswith("data")
# ends_with_csv = filename.endswith(".csv")

# print("Starts with 'data':", starts_with_data)
# print("Ends with '.csv':", ends_with_csv)

## 10. Ask the user to enter a word and print the word in reverse order.

word = input("Enter a word: ")
reversed_word = word[::-1]
print("Reversed word:", reversed_word)
