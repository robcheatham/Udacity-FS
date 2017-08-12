import quentin
import movies

# Movie Instances using the 'movies' Class
# Hateful Eight Movie: movie title, movie rating, poster image & trailer
hateful_eight = movies.Movie(
    "The Hateful Eight",
    "7.8/10",
	"https://goo.gl/yz1RWg",
    "https://www.youtube.com/watch?v=6_UI1GzaWv0"
    )

# Inglourious Basterds Movie: movie title, movie rating, poster image & trailer
inglourious_basterds = movies.Movie(
    "Inglourious Basterds",
    "8.3/10",
    "https://goo.gl/rQv6cZ",
    "https://www.youtube.com/watch?v=6AtLlVNsuAc"
    )

# Django Unchained Movie: movie title, movie rating, poster image & trailer
django_unchained = movies.Movie(
    "Django Unchained",
    "8.4/10",
    "https://goo.gl/Zh0ezg",
    "https://www.youtube.com/watch?v=_iH0UBYDI4g"
    )

# Jackie Brown Movie: movie title, movie rating, poster image & trailer
jackie_brown = movies.Movie(
    "Jackie Brown",
    "7.5/10",
    "https://goo.gl/adK6V0",
    "https://www.youtube.com/watch?v=HlAECQzTkfY"
    )

# Pulp Fiction Movie: movie title, movie rating, poster image & trailer
pulp_fiction = movies.Movie(
    "Pulp Fiction",
    "8.9/10",
    "https://goo.gl/VZWHVq",
    "https://www.youtube.com/watch?v=tGpTpVyI_OQ"
    )

# Reservoir Dogs Movie: movie title, movie rating, poster image & trailer
reservoir_dogs = movies.Movie(
    "Reservoir Dogs",
    "8.3/10",
    "https://goo.gl/b42X8h",
    "https://www.youtube.com/watch?v=vayksn4Y93A"
    )

# List for passing to the open movies page function
movie_list = [
    hateful_eight,
    inglourious_basterds,
    django_unchained,
    jackie_brown,
    pulp_fiction,
    reservoir_dogs
    ]

# Generate the page with the Movie List
quentin.open_movies_page(movie_list)
