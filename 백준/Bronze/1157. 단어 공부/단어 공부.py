word            = list(input())
word_frequency  = {}

for _alphabet in word:
    _alphabet = _alphabet.upper()
    if _alphabet in word_frequency:
        word_frequency[_alphabet] += 1
    else:
        word_frequency[_alphabet]  = 1

max_frequency = max(word_frequency.values())
if len([k for k, v in word_frequency.items() if v == max_frequency]) > 1:
    print("?")
else:
    result = [i for i in word_frequency if word_frequency[i] == max_frequency]
    print(result[0])