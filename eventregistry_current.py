from __future__ import print_function
from eventregistry import * 
from goose_scraper_news import get_article_data_goose
from article import Article

def get_current_topics():
	er = EventRegistry(apiKey="<INSERT API KEY>")

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
		print(a["isDuplicate"])
		if a["isDuplicate"] == True: 
			continue
		else: 
			title = a["title"]
			date = a["date"]
			full_text = a["body"]
			desc_text = full_text[:250]
			source = a["source"]["title"]
			source_url = a["url"]
			d = get_article_data_goose(source_url)
			image = d["image"]
			tags = d["tags"]
			videos = d["videos"]
			refs = d["references"]
	
			a = Article(title, date, full_text, desc_text, source, source_url, tags, image, videos, refs)
			results.append(a)
	return results


if __name__ == "__main__":
	print(get_current_topics())



