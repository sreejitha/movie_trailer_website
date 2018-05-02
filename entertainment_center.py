"""This module is to create and display favorite movie instances"""

import media
import fresh_tomatoes

MOVIE_1 = media.Movie("Dear Zindagi",
                      "The plot centres on a budding cinematographer named " +
                      "Kaira and her conversations with her psychologist",
                      "https://upload.wikimedia.org/wikipedia/en/9/9e/" +
                      "Dear_Zindagi_poster.jpg",
                      "https://www.youtube.com/watch?v=5DkO7ksXY8E")

MOVIE_2 = media.Movie("Pranayavarnangal",
                      "This films explores the trials and tribulations of " +
                      "college life",
                      "https://upload.wikimedia.org/wikipedia/en/thumb/b/bc/Pranayavarnangal_DVD_Cover.jpg/220px-Pranayavarnangal_DVD_Cover.jpg",   # NOQA
                      "https://www.youtube.com/watch?v=xL1aW1PupEk")  # NOQA

MOVIE_3 = media.Movie("Lagaan",
                      "The story revolves around a small village whose " +
                      "inhabitants are challenged to a game of cricket " +
                      "by their British officer for tax waiver",
                      "https://upload.wikimedia.org/wikipedia/en/thumb/b/b6/Lagaan.jpg/220px-Lagaan.jpg",   # NOQA
                      "https://www.youtube.com/watch?v=rxWhke_3fbQ")   # NOQA

MOVIE_4 = media.Movie("Dil Chahta Hai",
                      "Set in modern-day urban Mumbai and Sydney the story " +
                      "is about a major period of transition in the lives" +
                      "of three young friends.",
                      "https://upload.wikimedia.org/wikipedia/en/thumb/d/db/Dil_Chahta_Hai.jpg/220px-il_Chahta_Hai.jpg",  # NOQA
                      "https://www.youtube.com/watch?v=m13b25V0B10")  # NOQA

MOVIE_5 = media.Movie("Swades",
                      "The film is based on the true life story of a " +
                      "Non-resident Indian returning to his roots",
                      "https://upload.wikimedia.org/wikipedia/en/8/85/Swades_poster.jpg",  # NOQA
                      "https://www.youtube.com/watch?v=vc7AZNWvs0M")  # NOQA

MOVIE_6 = media.Movie("Kal Ho Na Ho",
                      "This movie narrates the story of Naina Catherine " +
                      "Kapur a pessimistic and uptight MBA student who falls "
                      "in love with her neighbour Aman Mathur",
                      "https://upload.wikimedia.org/wikipedia/en/thumb/b/b4/KalHoNaaHo.jpg/220px-KalHoNaaHo.jpg",  # NOQA
                      "https://www.youtube.com/watch?v=tVMAQAsjsOU")  # NOQA


MOVIES = [MOVIE_1, MOVIE_2, MOVIE_3, MOVIE_4, MOVIE_5, MOVIE_6]

fresh_tomatoes.open_movies_page(MOVIES)
