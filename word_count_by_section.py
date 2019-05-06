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
	# total_articles = 0

	for doc in root:
		for article in doc:
			contains_virus = False
			cur_sec = ""
			for section in article.iter("section"):
				cur_sec = section.text
			for content in article.iter("content"):
				words = content.text
				try:
					word_list = words.split(" ")
					for i in range(len(word_list)):
						if word_list[i].startswith("virus"):
							contains_virus = True
							break
				except AttributeError:
					break
			if contains_virus:
				try:
					sec_list = cur_sec.split("; ")
					for sec in sec_list:
						if sec in sections:
							sections[sec] += 1
						else:
							sections[sec] = 1
				except AttributeError:
					break

	return Counter(sections)


def plot_by_section(year_dict, most_common):
	# also include "Technology" and "Science" sections
	sections = ["Technology", "Science"]
	for tup in most_common:
		sections.append(tup[0])

	legend_words = []
	for section in sections:
		years = []
		counts = []
		for key, values in sorted(year_dict.items()):
			years.append(key)
			print(key, values[section])
			counts.append(values[section])
		plt.plot(years, counts)
		legend_words.append(section)

	plt.legend(legend_words, loc='upper left')
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
			tot_sections = get_sections(file)
			# print(tot_sections)
			year = filename[:4]
			if year in year_dict:
				year_dict[year] += tot_sections
			else:
				year_dict[year] = tot_sections
	# print(year_dict)
	all_years = Counter()
	for key, values in sorted(year_dict.items()):
		all_years += values
	# print(all_years)
	most_common = all_years.most_common(3)
	plot_by_section(year_dict, most_common)



all_xmls("xml_files/")
