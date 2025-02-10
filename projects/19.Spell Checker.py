from textblob import TextBlob
w = input("Enter the words: ")
words = w.split(',')

words = [word.strip() for word in words]

corrected_words = []

for word in words:
    corrected_words.append(TextBlob(word).correct())

print('Original words:', words)
print('Corrected words:', [str(word) for word in corrected_words])
