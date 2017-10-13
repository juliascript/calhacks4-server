
def gen_test_articles():
	return [gen_test_article()] * 10

def gen_test_article():
	return {
		'title': 'This is an article title',
		'date': 'October 7th, 2017',
		'description': 'This is an article description this will probably be longer and stuff hey man very cool wow nice',
		'image_url': 'https://images.unsplash.com/photo-1497829352618-8528e15d7ce7?dpr=1&auto=compress,format&fit=crop&w=3302&h=&q=80&cs=tinysrgb&crop='
	}
