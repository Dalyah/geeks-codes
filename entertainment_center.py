import fresh_tomatoes
import media


# Movies Data Structure to store Movie Objects
movies= []

# Titanic Movie
movie_1= media.Movie('Titanic',
'https://static.twentytwowords.com/wp-content/uploads/Real-Life-Titanic-Facts-the-Movie-Didnt-Tell-You_AD.jpg',
'https://www.youtube.com/watch?v=2e-eXJ6HgkQ')
movies.append(movie_1);

# Sunset Boulevard Movie
movie_2= media.Movie('Sunset Boulevard',
'http://www.gstatic.com/tv/thumb/v22vodart/1187/p1187_v_v8_ag.jpg',
'https://www.youtube.com/watch?v=imXKJfmdhGM')
movies.append(movie_2)

# The Wizard of Oz Movie
movie_3= media.Movie('The Wizard of Oz',
'http://www.gstatic.com/tv/thumb/v22vodart/5095/p5095_v_v8_ag.jpg',
'https://www.youtube.com/watch?v=c_Ne5g5F-WY')
movies.append(movie_3)

# The Dark Knight Movie
movie_4= media.Movie('The Dark Knight',
'http://www.gstatic.com/tv/thumb/v22vodart/173378/p173378_v_v8_at.jpg',
'https://www.youtube.com/watch?v=yrz8TakoaMo')
movies.append(movie_4)

# Ex Mechina Movie
movie_5= media.Movie('Ex Mechina',
'http://www.gstatic.com/tv/thumb/v22vodart/11007806/p11007806_v_v8_aa.jpg',
'https://www.youtube.com/watch?v=3hAlv0xLJJ4')
movies.append(movie_5)

# Black Panther Movie
movie_6= media.Movie('Blank Panther',
'http://www.gstatic.com/tv/thumb/v22vodart/12878741/p12878741_v_v8_ac.jpg',
'https://www.youtube.com/watch?v=xjDjIWPwcPU')
movies.append(movie_6)


def main():
    # Call open_movies_page(movies) from fresh_tomatoes.py file
    fresh_tomatoes.open_movies_page(movies)


if __name__ == '__main__':
    main()
