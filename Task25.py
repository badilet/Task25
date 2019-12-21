# Напишите функцию которая находит самое длинное слово в строке.
# sentence = input("Enter a sentence:")
# def longest_word():
# print(len(sentence.split()))
def find_longest_word(word_list):
    longest_word = ''
    for word in word_list:
        if len(word) > len(longest_word):
            longest_word = word
            print(longest_word)

find_longest_word()
