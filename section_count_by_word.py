import xml.etree.ElementTree as ET
import os
from collections import Counter
import matplotlib.pyplot as plt


def get_sections(filename):
	tree = ET.parse(filename)
	root = tree.getroot()
	sections = {}
	# year = filename[15:19]

	# section = ""
	# nyt_dict = {}
	# all_words = Counter()
	total_uses = 0

	for doc in root:
		for article in doc:
			contains_virus = False
			cur_sec = ""
			for section in article.iter("section"):
				cur_sec = section.text
			for content in article.iter("content"):
				words = content.text
				try:
					sec_list = cur_sec.split("; ")
					sec = "Technology"	# use these two lines if using only technology sections
					if sec in sec_list:
						word_list = words.split(" ")
						for i in range(len(word_list)):
							test1 = word_list[i].lower()
							if test1.startswith("virus"):
								# if i + 1 < len(word_list):
								# 	test2 = word_list[i+1].lower()
								# 	if test2.startswith("virus"):
								total_uses += 1
				except AttributeError:
					break

	return total_uses


def plot_by_section(year_dict):
	# also include "Technology" and "Science" sections
	# sections = ["Technology"]
	# for tup in most_common:
	# 	sections.append(tup[0])

	# legend_words = []
	# for section in sections:
	# 	years = []
	# 	counts = []
	# 	for key, values in sorted(year_dict.items()):
	# 		years.append(key)
	# 		print(key, values[section])
	# 		counts.append(values[section])
	# 	plt.plot(years, counts)
	# 	legend_words.append(section)

	years = []
	counts = []
	for key, val in sorted(year_dict.items()):
		years.append(key)
		counts.append(val)
	plt.plot(years, counts)

	# plt.legend(legend_words, loc='upper left')
	# plt.xticks(range(1997, 2017))
	plt.show()


def all_xmls(directory):
	# directory = os.fsencode(directory_in_str)
	year_dict = {}
	count = 0
	for file in os.listdir(directory):
		count += 1
		if count % 10 == 0: print(count)
		filename = os.fsdecode(file)
		if filename.endswith(".xml"): 
			file = os.path.join(directory, filename)
			total_uses = get_sections(file)
			# print(total_uses)
			year = filename[:4]
			if year in year_dict:
				year_dict[year] += total_uses
			else:
				year_dict[year] = total_uses
	plot_by_section(year_dict)



all_xmls("xml_files/")
