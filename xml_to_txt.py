import xml.etree.ElementTree as ET
import os


def build_txt(filename):
	tree = ET.parse(filename)
	root = tree.getroot()
	# year = filename[15:19]

	# section = ""
	# nyt_dict = {}
	# all_words = Counter()
	# total_articles = 0

	for doc in root:
		for article in doc:
			contains_virus = False
			date = 0
			title = ""
			sec = ""
			words = ""
			for p_date in article.iter("pub_date"):
				date = p_date.text
			for h_line in article.iter("headline"):
				head = h_line.text
				for word in str(head):
					title += word
				# title += h_line.text
			for cur_sec in article.iter("section"):
				section = cur_sec.text
				for word in str(section):
					sec += word
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
				real_title = title.copy()
				for char in [";", "*", ":", "?", "<", ">", "|", "/", "\\", '"', " "]: # replaces disallowed folder characters with underscores
					title = title.replace(char, "_")
				if len(title) < 1:
					title = "unknown_title__"
				loc = "virus_text_files/" + title[:15] + ".txt"
				with open(loc, "w") as f:
					f.write(real_title + "\n")
					f.write(date + "\n")
					f.write(sec + "\n")
					f.write(words)

def all_xmls(directory):
	# directory = os.fsencode(directory_in_str)
	count = 0
	for file in os.listdir(directory):
		count += 1
		if count % 10 == 0: print(count)
		filename = os.fsdecode(file)
		if filename.endswith(".xml"): 
			file = os.path.join(directory, filename)
			build_txt(file)

all_xmls("xml_files/")
