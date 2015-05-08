import webbrowser

class Movie(): #Google python style naming convention
    """ This class help to create movie page."""

    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, movie_title, movie_sotryline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_sotryline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)