"""This module is to store favorite movies and play their trailers when selected"""
import webbrowser


class Movie(object):
    """The class is used to initialize the movie object with all its properties including
    movie title, trailer, storyline and poster image. It also has a method to open up a browser to
    show the selected movie's trailer"""

    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """this method opens up a browser window displaying youtube trailer of the movie"""
        webbrowser.open(self.trailer_youtube_url)
