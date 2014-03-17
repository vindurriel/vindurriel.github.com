#encoding=utf-8
from collections import defaultdict
import re
MAX_SUMMARY_SIZE = 300
SUMMARY_RATIO= 0.2
stop_words= set(u"where the of is and to in that we for an are by be as on with can if from which you it this then at have all not one has or that".split())
def tokenize(text):
	'''Very simple white space tokenizer, in real life we'll be much more
	fancy.
	'''
	import jieba
	return jieba.cut(text)
def split_to_sentences(text):
	'''Very simple spliting to sentences by [.!?] and paragraphs.
	In real life we'll be much more fancy.
	'''
	import nltk.data
	tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
	text ="\n\n".join(tokenizer.tokenize(text))
	import re
	sentences=[]
	start = 0
	for match in re.finditer(u'(\s*[。？！]\s*)|(\n{2,})', text):
		sentences.append(text[start:match.end()].strip())
		start = match.end()
	sentences=filter(bool,sentences)
	sentences=filter(lambda x:len(x)>2,sentences)
	return sentences
def token_frequency(text):
	'''Return frequency (count) for each token in the text'''
	frequencies = defaultdict(int)
	for token in tokenize(text):
		frequencies[token] += 1
	return frequencies
def sentence_score(sentence, frequencies):
	return sum((frequencies[token] for token in tokenize(sentence) if token not in stop_words))/len(sentence)
def create_summary(sentences,frequencies):
	summary = []
	import math
	len_sentence=int(math.ceil(len(sentences)*SUMMARY_RATIO))
	len_sentence=max(len_sentence,1)
	len_sentence=min(len_sentence,10)
	index=[]
	for i in range(len(sentences)):
		index.append((i,sentence_score(sentences[i],frequencies)))
	index.sort(key=lambda s:s[1],reverse=1)
	index=index[:len_sentence]
	index.sort(key=lambda s:s[0])
	for i in index:
		summary.append(sentences[i[0]])
	return '\n'.join(summary)
def summarize(text):
	frequencies = token_frequency(text)
	sentences = split_to_sentences(text)
	
	summary = create_summary(sentences,frequencies)
	return summary


if __name__ == '__main__':
	import os
	dirname=r'E:\workspace\vindurriel.github.com\_posts'
	fnames=os.listdir(dirname)
	for fname in fnames:
		if not fname.endswith(".md"):continue
		fname=os.path.join(dirname,fname)
		print fname
		orgtext=None
		with open(fname,'r') as f:
			orgtext=f.read().decode('utf-8')
		if u"---\n\n"  in orgtext:
			text=orgtext.split(u"---\n\n")[1]
		summary=summarize(text)
		import cgi
		summary=cgi.escape(summary,quote=True).replace(u"\n",u"<br/>")
		import re
		regex=re.compile("description:\s*\"(.*?)\"")
		orgtext=regex.sub(u"description: \"{}\"".format(summary),orgtext)
		with open(fname,'w') as f:
			f.write(orgtext.encode('utf-8'))