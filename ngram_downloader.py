import google_ngram_downloader
 
word = "virus"
count = 0
try_ = 0
fname, url, records = next(google_ngram_downloader.readline_google_store(ngram_len=1, indices=word))

# print(google_ngram_downloader.count_coccurrence(records, word))

try:
	record = next(records)
 
	while record.ngram.lower() != word:
		if try_ % 10000 == 0: print(try_)
		record = next(records)
		try_ += 1
 
	while record.ngram.lower() == word:
		count = count + record.match_count
		record = next(records)
		
except StopIteration:
	pass

print(count)