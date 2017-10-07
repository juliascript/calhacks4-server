
from flask import Flask
from flask import jsonify
from article import Article
from article_preview import ArticlePreview

app = Flask(__name__)

# Main Feed Route
@app.route('/feed')
def main_feed():
	article_previews = gen_article_previews()
	article_previews = list(map(lambda article_preview: article_preview.__dict__, article_previews))
	json = jsonify(article_previews)
	return json

# View for individual article
@app.route('/feed/<article_id>')
def show_article(article_id):
	# show article stuff here NO FUNCTIONALITY RIGHT NOW
	return jsonify('wow')

def main():
	app.run()

# PRIVATE TEST GENERATING ARTICLES ONLY TEST FOR NOW
def gen_article_previews():
	article = Article(
		"This is a title",
		"October 7th, 2017",
		"https://images.unsplash.com/photo-1497829352618-8528e15d7ce7?dpr=1&auto=compress,format&fit=crop&w=3302&h=&q=80&cs=tinysrgb&crop=",
		"This is a short description for the article tell us how far to truncate this shit, should be good man. fjeowoifwejo efwoijoiewfj oefwjoijewfoi fweojfeowij oiewfj ofwejfo iejofewjofiewjoifewjo fewoj feowij fewoj fewoijfe wojf ewoijfewo efwjofew oijfew ojfwe ",
		["link1", "link2", "link3"])
	article_preview = ArticlePreview(article)
	return [article_preview] * 5

main()
