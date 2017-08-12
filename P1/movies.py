import webbrowser

class Movie():

	# Constructor Method for a Movie
	def __init__(self, movie_title, movie_rating, poster_image, movie_trailer_url):
		self.title = movie_title
		self.rating = movie_rating
		self.artwork = poster_image
		self.trailer = movie_trailer_url

	# Function to open the Youtube Trailer
	def open_trailer(self):
		webbrowser.open(self.trailer)