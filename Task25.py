# Напишите функцию которая находит самое длинное слово в строке.

def myfunc():
    text = input("Enter a sentence: ").split(" ")
    count = 0
    for i in text:
        if len(i) > count:
            count = len(i)
            word = i
    print("The longest word is: ", word)
myfunc()
