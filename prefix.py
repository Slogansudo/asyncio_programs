from collections import Counter


def prefix(data):
    words_x = Counter()
    for word in data:
        words = set(word)
        words_x.update(words)
    result = words_x.most_common(1)
    return result


data = ['apple', 'banana', 'kivi', 'orange', 'apple']
word = prefix(data)
natija = word[0][0]
print("Natija: ", natija)
