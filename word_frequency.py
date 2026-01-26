# def Word_frequency_Counter():
#     collection = {}
#     text = input("Enter your Text: ")
#     text = text.replace(".","")
#     text = text.replace("!","")
#     text = text.replace(",","")
#     items = text.split()  # string text is converted into list items
#     for words in items:
#         clean_word = words.lower()
#         collection[clean_word] = collection.get(clean_word, 0) + 1
#     print(collection)
# Word_frequency_Counter()


#method two
# using python libraray collection i will count the word frequency
from collections import Counter

def Word_frequency_Counter():
    text = input("Enter your Text: ")
    text = text.replace(".","")
    text = text.replace("!","")
    text = text.replace(",","")
    items = text.split()  # string text is converted into list items
    for words in items:
        clean_word = words.lower()
    collection = Counter(clean_word)
    print(collection)
Word_frequency_Counter()
