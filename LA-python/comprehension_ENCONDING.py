import string
from random import shuffle

text = "Hi, I'm the decoded message"
letters = list(string.ascii_letters)
#print letters
encoded_letters = letters[:]
shuffle(encoded_letters)
#print encoded_letters

encoding_key = dict(zip(letters,encoded_letters))
decoding_key = dict(zip(encoding_key.values(),encoding_key.keys()))

encoded_text = ''.join([ encoding_key.get(w,w) for w in text])
decoded_text = ''.join([ decoding_key.get(w,w) for w in encoded_text])

print "Encoded text"
print encoded_text
print "Decoded text"
print decoded_text