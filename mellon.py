import random, re, sys

rnd = random.SystemRandom()
words_file = open("words.txt")
word_count = int(sys.argv[1]) if len(sys.argv) >= 2 else 10
syllable_count = int(sys.argv[2]) if len(sys.argv) >= 3 else 2

# Get all words in teh file
words = [word.rstrip() for word in words_file.readlines()]

# Remove words with non-word characters
words = [word for word in words if len(re.findall("[^a-z]", word)) == 0]

# Remove all words with more than X syllables
words = [
    word
    for word in words
    if len(re.findall("[^aeiouy]*[aeiouy]+[^aeiouy]*", word)) <= syllable_count
]

# Pick X words at random
words = [rnd.choice(words).rstrip() for i in range(word_count)]

print(words)
words_file.close()
