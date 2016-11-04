# Using text2 from the nltk book corpa, create your own version of the
# MadLib program.  

# Requirements:
# 1) Only use the first 150 tokens
# 2) Pick 5 parts of speech to prompt for, including nouns
# 3) Replace nouns 15% of the time, everything else 10%

# Deliverables:
# 1) Print the orginal text (150 tokens)
# 1) Print the new text
import nltk
import random
from nltk.book import text2

print("START*******\n\n")
text2 = text2[0:151]
string = ""
for token in text2:
	string += ' ' + token
print('Original Text\n--------------')
print(string)
tokens = nltk.word_tokenize(string)
tagged_tokens = nltk.pos_tag(tokens)
tagmap = {"NN":"a noun","NNS":"a plural noun","VBD":"a past-tense verb","JJ":"an adjective", "IN":"a preposition"}
substitution_probabilities = {"NN":.15,"NNS":.1,"VBD":.1,"JJ":.1,"IN":.1}

changed_text = []
final_text = ""
for (word, tag) in tagged_tokens:
	if tag not in substitution_probabilities or random.random() > substitution_probabilities[tag]:
		changed_text.append(word)
	else:
		new_word = input("Please enter %s:\n" % (tagmap[tag]))
		changed_text.append(new_word)
for token in changed_text:
	final_text += ' ' + token
print('\nChanged Text\n---------------')
print(final_text)

print("END*******")
