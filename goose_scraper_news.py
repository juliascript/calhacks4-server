from __future__ import print_function
from goose import Goose 

def get_article_data_goose(url):
	res = {}
	g=Goose()

	article = g.extract(url=url)

	title = article.title
	res["title"] = title

	full_text = article.cleaned_text
	res["full_text"] = full_text

	short_desc = article.cleaned_text[:250]
	res["short_desc"] = short_desc

	if article.infos["image"]:
		image_url = article.infos["image"]["url"]
		res["image_url"] = image_url
	
	tags = article.tags 
	res["tags"] = tags

	videos = article.movies
	res["videos"] = videos

	references = article.links
	res["references"] = references
	
	date = article.publish_date
	res["date"] = date

	return res

if __name__ == "__main__":
	get_article_data_goose("http://www.newsweek.com/las-vegas-fox-news-nra-679317")