from __future__ import print_function
from goose import Goose 

def get_article_data_goose(url):
	g=Goose()

	article = g.extract(url=url)

	title = article.title
	print(title)
	full_text = article.cleaned_text
	print(full_text)
	short_desc = article.cleaned_text[:250]
	print(short_desc)
	image = article.top_image
	print(image)
	tags = article.tags 
	print(tags)
	videos = article.movies
	print(videos)
	references = article.links
	print(references)
	date = article.publish_date
	print(date)

	return { 	
				"image": image, 
				"tags": tags,
				"videos": videos,
				"references": references
			}