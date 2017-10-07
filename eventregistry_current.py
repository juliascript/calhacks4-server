from __future__ import print_function
from eventregistry import * 
from goose_scraper_news import get_article_data_goose
from article import Article
import base64

def get_current_topics():
	er = EventRegistry(apiKey="<APIKEY>")

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

	first_topic = ret["org"]["trendingConcepts"][0]["label"]["eng"]

	q = QueryArticles(keywords = first_topic)
	res = er.execQuery(q)

	results = []
	articles = res["articles"]
	count = articles["count"]
	for i in range(count):
		a = articles["results"][i]
		if a["isDuplicate"] == True: 
			continue
		else: 
			article_obj = Article()
			article_obj["title"] = a["title"]
			article_obj["date"] = a["date"]
			article_obj["source"] = a["source"]["title"]
			source_url = a["url"]
			article_obj["source_url"] = source_url

			d = get_article_data_goose(source_url)
			article_obj["full_text"] = d["full_text"]
			article_obj["desc_text"] = d["short_desc"]
			if "image_url" in d:
				article_obj["image_url"] = d["image_url"]
			article_obj["tags"] = d["tags"]
			article_obj["videos"] = d["videos"]
			article_obj["refs"] = d["references"]

			print(article_obj)
			results.append(article_obj)
	return results


if __name__ == "__main__":
	print(get_current_topics())



