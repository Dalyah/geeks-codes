# Movie Class
class Movie:
    """Movie class containes the attributes of a single movie.

    Attributes:
        title (String): the title of the movie.
        poster_img_url (String): the URL of the movie poster.
        trailer_youtube_url (String): the URL of the movie trailer on YouTube.
        
    """
    def __init__(self, title, poster_image_url, trailer_youtube_url):
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
