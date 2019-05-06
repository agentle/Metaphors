
# from lxml import etree
import xml.etree.ElementTree as ET
from collections import Counter
import matplotlib.pyplot as plt
import os
import string
import re
import copy

stopwords = ['--','', 'a','able','about','across','after','all','almost','also','am','among','an','and','any','are','as','at','be','because','been','but','by','can','cannot','could','dear','did','do','does','either','else','ever','every','for','from','get','got','had','has','have','he','her','hers','him','his','how','however','i','if','in','into','is','it','its','just','least','let','like','likely','may','me','might','most','must','my','neither','no','nor','not','of','off','often','on','only','or','other','our','own','rather','said','said.','say','says','she','should','since','so','some','than','that','the','their','them','then','there','these','they','this','tis','to','too','twas','us','wants','was','we','were','what','when','where','which','while','who','whom','why','will','with','would','yet','you',"you'",'your']


# print(root.tag, root.attrib)

# for doc in root:
# 	# print(doc.tag, doc.attrib)
# 	# for article in doc:
# 	# 	print(article.tag, article.attrib)
# 	# for item in doc[0]:
# 		# print(item.tag, item.attrib)
# 	for section in doc:
# 		# print(section)
# 		for word in section:
# 			# print(word.tag, word.attrib)
# 			for content in word:
# 				print(content)
			# for 
		# print(word)
		# for word in item[3]:
		# 	print(word)

##### USE TEXTBLOB Ngrams!!! ######


def get_trigrams(filename):
	tree = ET.parse(filename)
	root = tree.getroot()
	year = filename[15:19]

	section = ""
	nyt_dict = {}
	all_words = Counter()
	total_articles = 0

	for doc in root:
		for article in doc:
			word_used = False
			for section in article.iter("section"):
				cur_sec = section.text
			for content in article.iter("content"):
				# print(text.items())
				# for word in content.text:
				# 	print(word)
				# print(content.tag)
				words = content.text
				try:
					word_list = words.split(" ")
					for i in range(len(word_list)):
						if word_list[i].startswith("virus"):
							sec_list = cur_sec.split("; ")

							# for sec in sec_list:	# use this if using all sections

							sec = "Technology"	# use these two lines if using only technology sections
							if sec in sec_list:



								if not word_used:
									total_articles += 1
									word_used = True

								# print(sec_list)
								if sec not in nyt_dict:
									nyt_dict[sec] = []
								if ((i - 2 >= 0) and (i + 2 < len(word_list))):
									trigrams = [word_list[i-2], word_list[i-1], word_list[i+1], word_list[i+2]]
									nyt_dict[sec].append(trigrams)
									# if year == "2016":
									# 	print(total_articles)
									# 	print(trigrams)

									tri_dict = {}
									for tri in trigrams:
										tri = re.match("(\w+)", tri).group(1)
										tri = tri.lower()
										if tri not in stopwords:
											if tri not in tri_dict:
												tri_dict[tri] = 1
											else:
												tri_dict[tri] += 1
									all_words.update(tri_dict)
									# print(tri_dict)
							# print(word_list[i-2], word_list[i-1], word_list[i])
							# print(word_list[i-1], word_list[i], word_list[i+1])
							# print(word_list[i], word_list[i+1], word_list[i+2])
				except AttributeError:
					break

	return nyt_dict, all_words, total_articles







def all_uses_of_word(directory):
	# directory = os.fsencode(directory_in_str)

	yearly_dict = {}

	count = 0

	for file in os.listdir(directory):
		count += 1
		if count % 10 == 0: print(count)
		# print(count)
		filename = os.fsdecode(file)
		if filename.endswith(".xml"): 
			file = os.path.join(directory, filename)
			# continue
			# print(filename)
			year = filename[:4]
			# print(year)
			nyt_dict, all_words, total_uses = get_trigrams(file)
			if year not in yearly_dict:
				yearly_dict[year] = total_uses
			else:
				yearly_dict[year] += total_uses
		else:
			continue
	return yearly_dict

def get_info():
	nyt_dict, all_words, total_uses = get_trigrams("1997_5.xml")

	print()
	for key in sorted(nyt_dict.keys()):
		print(key, len(nyt_dict[key]))
	# print(all_words)
	# count = Counter(all_words)

	print("Total uses:", total_uses)

	print()
	print(count.most_common(10))
	print()


def plot_line(py_dict):
	x = []
	y = []
	for key, val in sorted(py_dict.items()):
		x.append(key)
		y.append(val)
	# print(x, y)
	plt.plot(x, y)

	plt.xlabel('Year')
	plt.ylabel('Number of Uses')
	plt.title("Uses of 'Virus' over Time")
	plt.grid(True)
	plt.show()


# main function to generate graph
def plot_by_year():
	yearly_dict = all_uses_of_word("xml_files/")
	plot_line(yearly_dict)

# plot_by_year()








def all_trigrams_in_section(directory):
	# directory = os.fsencode(directory_in_str)

	yearly_dict = {}

	count = 0

	for file in os.listdir(directory):
		count += 1
		if count % 10 == 0: print(count)
		filename = os.fsdecode(file)
		if filename.endswith(".xml"): 
			file = os.path.join(directory, filename)
			# continue
			# print(filename)
			year = filename[:4]
			# print(year)
			nyt_dict, all_words, total_uses = get_trigrams(file)
			# print(year, total_uses)
			if year not in yearly_dict:
				yearly_dict[year] = all_words
			else:
				yearly_dict[year].update(all_words)
		else:
			continue
	return yearly_dict

def plot_top_words_per_year(word_freq):
	all_words = {}
	legend_words = []
	
	for key, values in sorted(word_freq.items()):
		print(key, values.most_common(5))
		for tup in values.most_common(5):
			word = tup[0]
			amount = tup[1]
			if word not in all_words:
				year_dict = {}
				for year in range(1997, 2017):
					year_dict[str(year)] = 0
				all_words[word] = year_dict

			all_words[word][key] += amount
	print(all_words)

	for word, values in all_words.items():
		legend_words.append(word)
		years = []
		counts = []
		for year, count in sorted(values.items()):
			years.append(year)
			counts.append(count)
		plt.plot(years, counts)

	plt.legend(legend_words, loc='upper left')
	plt.show()

	print("plot section")

def plot_top_words_overall(word_freq):
	all_words = Counter()
	legend_words = []
	print(word_freq)
	
	for key, values in sorted(word_freq.items()):
		all_words += values

	for tup in all_words.most_common(10):
		years = []
		counts = []
		word = tup[0]
		legend_words.append(word)

		for year in range(1997, 2017):
			years.append(year)
			counts.append(word_freq[str(year)][word])
		plt.plot(years, counts)

	plt.legend(legend_words, loc='upper left')
	plt.xticks(range(1997, 2017))
	plt.show()

	print("plot section")


	# for word, values in all_words.items():
	# 	legend_words.append(word)
	# 	years = []
	# 	counts = []
	# 	for year, count in sorted(values.items()):
	# 		years.append(year)
	# 		counts.append(count)
	# 	plt.plot(years, counts)

	# plt.legend(legend_words, loc='upper left')
	# plt.show()

	# print("plot section")


	# for word, values in all_words.items():
	# 	legend_words.append(word)
	# 	years = []
	# 	counts = []
	# 	for year, count in sorted(values.items()):
	# 		years.append(year)
	# 		counts.append(count)
	# 	plt.plot(years, counts)

	# plt.legend(legend_words, loc='upper left')
	# plt.show()

	# print("plot section")


# main function to plot trigram words by section
def plot_by_section():
	yearly_dict = all_trigrams_in_section("xml_files/")
	# plot_top_words_per_year(yearly_dict)
	plot_top_words_overall(yearly_dict)


plot_by_section()




