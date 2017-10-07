# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals

from sumy.parsers.html import HtmlParser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
# from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.summarizers.kl import KLSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words


LANGUAGE = "english"
SENTENCES_COUNT = 5

def kl_sum_of_articles(articles):
	f = open("article_text.txt","w")
	for article_text in articles:
		article_text = article_text.encode('ascii', 'ignore')
		f.write(article_text)
	f.close()
	parser = PlaintextParser.from_file("article_text.txt", Tokenizer(LANGUAGE))
	stemmer = Stemmer(LANGUAGE)

	summarizer = Summarizer(stemmer)
	summarizer.stop_words = get_stop_words(LANGUAGE)

	print("Summary: ---")
	summary = ""
	for sentence in summarizer(parser.document, SENTENCES_COUNT):
		print(sentence)
		summary += str(sentence)
	return summary
	print("------------")

if __name__ == "__main__":
	url = "http://www.newsweek.com/las-vegas-fox-news-nra-679317"
	parser = HtmlParser.from_url(url, Tokenizer(LANGUAGE))
	# or for plain text files
	# parser = PlaintextParser.from_file("document.txt", Tokenizer(LANGUAGE))
	stemmer = Stemmer(LANGUAGE)

	summarizer = Summarizer(stemmer)
	summarizer.stop_words = get_stop_words(LANGUAGE)

	for sentence in summarizer(parser.document, SENTENCES_COUNT):
		print(sentence)
