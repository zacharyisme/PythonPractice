import fresh_tomatoes
import media


toy_story = media.Movie("Toy Sotry",
                        "A story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/thumb/1/13/Toy_Story.jpg/220px-Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=Bj4gS1JQzjk")

avatar = media.Movie("Avatar",
                     "A Marine on an alien planet",
                     "http://upload.wikimedia.org/wikipedia/en/thumb/b/b0/Avatar-Teaser-Poster.jpg/220px-Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

furious7 = media.Movie("Furious7",
                       "A team works closely and likes family to sole the challenge and share love with each other.",
                       "http://upload.wikimedia.org/wikipedia/en/thumb/b/b8/Furious_7_poster.jpg/220px-Furious_7_poster.jpg",
                       "https://www.youtube.com/watch?v=Skpu5HaVkOc")

avengers_AgeOfUltron = media.Movie("Avengers: Age of Ultron",
                                   "It is a 2015 American superhero film based on the Marvel Comics superhero team the Avengers",
                                   "http://upload.wikimedia.org/wikipedia/en/thumb/1/1b/Avengers_Age_of_Ultron.jpg/220px-Avengers_Age_of_Ultron.jpg",
                                   "https://www.youtube.com/watch?v=JAUoeqvedMo")

the_water_diviner = media.Movie("The Water Diviner",
                     "A father try to find back his sons after the First World War",
                     "http://upload.wikimedia.org/wikipedia/en/thumb/1/1c/The_Water_Diviner_poster.jpg/220px-The_Water_Diviner_poster.jpg",
                     "https://www.youtube.com/watch?v=c-hU96CwWHI")

#print furious7.title
#furious7.show_trailer()
movies = [toy_story, avatar, furious7, avengers_AgeOfUltron, the_water_diviner]

#fresh_tomatoes.open_movies_page(movies)
#print (media.Movie.VALID_RATINGS)
print (media.Movie.__doc__)