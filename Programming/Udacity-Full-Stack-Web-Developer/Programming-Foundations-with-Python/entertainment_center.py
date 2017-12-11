import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story", "Story of a boy whose toys come to life",
                        "http://ia.media-imdb.com/images/M/MV5BMTgwMjI4MzU5N15BMl5BanBnXkFtZTcwMTMyNTk3OA@@._V1_UY268_CR9,0,182,268_AL_.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")
# print toy_story.storyline
# toy_story.show_trailer()

avatar = media.Movie("Avatar", "Marine on a Alien planet",
                        "http://ia.media-imdb.com/images/M/MV5BMTYwOTEwNjAzMl5BMl5BanBnXkFtZTcwODc5MTUwMw@@._V1_UX182_CR0,0,182,268_AL_.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

school_of_rock = media.Movie("School of Rock", "Crazy teacher prepares School for rock show",
                        "http://ia.media-imdb.com/images/M/MV5BMjEwOTMzNjYzMl5BMl5BanBnXkFtZTcwNjczMTQyMQ@@._V1_UX182_CR0,0,182,268_AL_.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

ratatouille = media.Movie("Ratatouille", "Rat is a master chef",
                        "http://ia.media-imdb.com/images/M/MV5BMTMzODU0NTkxMF5BMl5BanBnXkFtZTcwMjQ4MzMzMw@@._V1_UX182_CR0,0,182,268_AL_.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

midnight_in_paris = media.Movie("Midnight in Paris", "Love in Paris",
                        "http://ia.media-imdb.com/images/M/MV5BMTM4NjY1MDQwMl5BMl5BanBnXkFtZTcwNTI3Njg3NA@@._V1_UX182_CR0,0,182,268_AL_.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

hunger_games = media.Movie("Hunger Games", "A reality show in real life",
                        "http://ia.media-imdb.com/images/M/MV5BMjA4NDg3NzYxMF5BMl5BanBnXkFtZTcwNTgyNzkyNw@@._V1_UX182_CR0,0,182,268_AL_.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

movies_list = [toy_story, avatar, school_of_rock, ratatouille, midnight_in_paris, hunger_games]
# fresh_tomatoes.open_movies_page(movies_list)

print(media.Movie.__doc__)
print(media.Movie.__name__)
print(media.Movie.__module__)
