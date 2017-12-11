import webbrowser

class Movie():
    """ This classs is used for storing the movie details """
    VALID_RATINGS = ["G", "PG", "PG-13", "R"] # Class variable shared by objects
    
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
