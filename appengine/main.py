
import os
import MySQLdb
import webapp2
from webapp2_extras import json
import json as jason


from topic import Topic
from article import Article
import test_data

# These environment variables are configured in app.yaml.
CLOUDSQL_CONNECTION_NAME = os.environ.get('CLOUDSQL_CONNECTION_NAME')
CLOUDSQL_USER = os.environ.get('CLOUDSQL_USER')
CLOUDSQL_PASSWORD = os.environ.get('CLOUDSQL_PASSWORD')

def connect_to_cloudsql():
    # When deployed to App Engine, the `SERVER_SOFTWARE` environment variable
    # will be set to 'Google App Engine/version'.
    if os.getenv('SERVER_SOFTWARE', '').startswith('Google App Engine/'):
        # Connect using the unix socket located at
        # /cloudsql/cloudsql-connection-name.
        cloudsql_unix_socket = os.path.join(
            '/cloudsql', CLOUDSQL_CONNECTION_NAME)

        db = MySQLdb.connect(
            unix_socket=cloudsql_unix_socket,
            user=CLOUDSQL_USER,
            passwd=CLOUDSQL_PASSWORD)

    # If the unix socket is unavailable, then try to connect using TCP. This
    # will work if you're running a local MySQL server or using the Cloud SQL
    # proxy, for example:
    #
    #   $ cloud_sql_proxy -instances=your-connection-name=tcp:3306
    #
    else:
    	print("BRUH THIS SHOULDN'T HAPPEN MANNNN")
        db = MySQLdb.connect(
            host='127.0.0.1', user=CLOUDSQL_USER, passwd=CLOUDSQL_PASSWORD)

    return db


"""Main page user lands on when going to endpoint"""
class MainPage(webapp2.RequestHandler):
	def get(self):
		self.response.headers['Content-Type'] = 'text/plain'
		self.response.write('Yo whats up dude, go to /topics for topics. You can also go to /topics/<id> with any id to test that')

"""Route for indexing all articles."""
class TopicsPage(webapp2.RequestHandler):
	def get(self):

		db = connect_to_cloudsql()
		cursor = db.cursor(MySQLdb.cursors.DictCursor)
		cursor.execute("USE topics")
		cursor.execute("SELECT * FROM topics")
		rows = cursor.fetchall()

		topics = []
		for row in rows:
			topic_string = row["json_string"]
			topic_id = row["entryID"]
			try:
				topic_dict = jason.loads(topic_string)
				title = topic_dict['label']
				summary = topic_dict['kl_summary']
				articles = list(map(lambda x: Article(x), topic_dict['articles']))
				topic = Topic(topic_id, title, summary, articles)

				topics.append(topic)
			except ValueError:
				continue

			
		topic_response = list(map(lambda x: x.small_topic(), topics))
		self.response.headers['Content-Type'] = 'application/json'
		self.response.write(json.encode(topic_response))

	def post(self):
		topic_string = self.request.POST['topic']

		data = topic_string.encode('utf-8')
		db = connect_to_cloudsql()
		cursor = db.cursor()
		cursor.execute("USE topics")
		cursor.execute("INSERT INTO topics (json_string) VALUES (%s)", [data])
		db.commit()
		db.close()

		self.response.headers['Content-Type'] = 'application/json'
		self.response.write(json.encode({'message': 'Thanks bro'}))

"""Route for showing a specific article. You need to pass in article id"""
class TopicPage(webapp2.RequestHandler):
	def get(self, topic_id):

		db = connect_to_cloudsql()
		cursor = db.cursor(MySQLdb.cursors.DictCursor)
		cursor.execute("USE topics")
		cursor.execute("SELECT * FROM topics WHERE entryID = %s", [topic_id])
		rows = cursor.fetchall()

		if rows.count == 0:
			self.response.headers['Content-Type'] = 'application/json'
			self.response.write(json.encode({}))
			return

		row = rows[0]
		topic_string = row["json_string"]
		topic_id = row["entryID"]
		try:
			topic_dict = jason.loads(topic_string)
			title = topic_dict['label']
			summary = topic_dict['kl_summary']
			articles = list(map(lambda x: Article(x), topic_dict['articles']))
			topic = Topic(topic_id, title, summary, articles)
			self.response.headers['Content-Type'] = 'application/json'
			self.response.write(json.encode(topic.large_topic()))
		except ValueError:
			self.response.headers['Content-Type'] = 'application/json'
			self.response.write(json.encode({}))

app = webapp2.WSGIApplication([
	('/', MainPage),
	('/topics', TopicsPage),
	('/topics/(.+)', TopicPage)
], debug=True)
