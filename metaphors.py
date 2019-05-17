import re

def get_n_longest_values_g(dictionary, n):
    longest_entries = sorted(
        dictionary.items(), key=lambda t: len(t[1]), reverse=True)[:n]
    return [(key, len(value)) for key, value in longest_entries]

smallest = 2000
freq_dict = {}

stopwords = ['a','able','about','across','after','all','almost','also','am','among','an','and','any','are','as','at','be','because','been','but','by','can','cannot','could','dear','did','do','does','either','else','ever','every','for','from','get','got','had','has','have','he','her','hers','him','his','how','however','i','if','in','into','is','it','its','just','least','let','like','likely','may','me','might','most','must','my','neither','no','nor','not','of','off','often','on','only','or','other','our','own','rather','said','say','says','she','should','since','so','some','than','that','the','their','them','then','there','these','they','this','tis','to','too','twas','us','wants','was','we','were','what','when','where','which','while','who','whom','why','will','with','would','yet','you','your']

with open("googlebooks-eng-all-2gram-20120701-vi", "r") as f:
	array = []
	for line in f:
		# if line.startswith("virus_NOUN") or line.startswith("Virus_NOUN") or line.startswith("virus_ADJ") or line.startswith("Virus_ADJ"):
		if line.startswith("virus") or line.startswith("Virus"):
			match = re.match("(\S+)\s(\S+)\\s(\d+)\s(\d+)\s(\d+)", line)

			main_word = match.group(1)
			second_word = match.group(2)
			# third_word = match.group(3) # use this only if tri-gram, increment next 3
			year = match.group(3)
			frequency = match.group(4)
			num_texts = match.group(5)

			if year not in freq_dict: # adds year to dictionary
				freq_dict[year] = {}

			# removes punctuation
			if not second_word.startswith("_") and not second_word.startswith(",") and not second_word.startswith(".") and not second_word.startswith("(") and not second_word.startswith(";") and not second_word.startswith("?") and not second_word.startswith("&") and not second_word.startswith("^"):
				
				remove_underscore = re.match("([A-Za-z]+)_(\S+)", second_word)	
				if remove_underscore:	# this removes the _ after a word
					second_word = remove_underscore.group(1)

				if second_word.lower() not in stopwords:
					if second_word not in freq_dict[year]:
						freq_dict[year][second_word] = frequency
					else:
						freq_dict[year][second_word] += frequency

		# counter += 1
		# if counter < 10:
		# 	print(line)

		# else:
		# 	break
# print(smallest)
# print(freq_dict)
for date_key in sorted(freq_dict.keys()):
	print(date_key, get_n_longest_values_g(freq_dict[date_key], 10))
	print()
	print()
	# for word_key in freq_dict[date_key].keys():
	# 	print(date_key, word_key)#, get_n_longest_values_g(freq_dict[date_key][word_key], 2))
	# 	print()
	# 	print()
