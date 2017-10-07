from __future__ import print_function
from eventregistry import * 
from goose_scraper_news import get_article_data_goose
from article import Article
from sumy_summarizer import kl_sum_of_articles
import base64, requests

def get_current_topics():
	er = EventRegistry(apiKey="APIKEY")

	# q = GetTrendingConcepts(source = "news", count = 10,
	#     returnInfo = ReturnInfo(
	# conceptInfo = ConceptInfoFlags(trendingHistory = True)))

	# ret = er.execQuery(q)
	# print(er.format(ret))

	q = GetTrendingConceptGroups(source = "news")
	# get top trends for individual concept groups - people, locations and organizations
	q.getConceptTypeGroups()
	ret = er.execQuery(q)

	res = er.format(ret)

	all_articles = []

	for i in range(2):
		topic_label = ret["org"]["trendingConcepts"][i]["label"]["eng"]
		q = QueryArticles(keywords = topic_label)
		res = er.execQuery(q)

		topic = {}
		topic["label"] = topic_label
		topic["articles"] = []
		articles = res["articles"]
		count = articles["count"]

		article_texts = []
		for i in range(count):
			a = articles["results"][i]
			if a["isDuplicate"] == True: 
				continue
			else: 
				article_obj = Article()
				article_obj["title"] = a["title"]
				print(a["title"])
				article_obj["date"] = a["date"]
				article_obj["source_title"] = a["source"]["title"]
				source_url = a["url"]
				article_obj["source_url"] = source_url

				d = get_article_data_goose(source_url)
				article_obj["full_text"] = d["full_text"]
				article_texts.append(d["full_text"])

				article_obj["short_description"] = d["short_desc"]
				if "image_url" in d:
					article_obj["image_url"] = d["image_url"]
				article_obj["tags"] = d["tags"]
				article_obj["videos"] = d["videos"]
				article_obj["reference_urls"] = d["references"]

				# print(article_obj)
				topic["articles"].append(article_obj)
		summary = kl_sum_of_articles(article_texts)
		topic["kl_summary"] = summary
		all_articles.append(topic)
		# send to Nick's server that will interface with the app
		res = requests.post('https://calhacks4-182212.appspot.com/articles', json=topic)
		print 'response from server:', res.text
		dictFromServer = res.json()

	print(all_articles)
	return all_articles

if __name__ == "__main__":
	print(get_current_topics())


