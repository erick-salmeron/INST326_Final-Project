""" INST326 Final Project Deliverable

Purpose: Having trouble finding a movie to watch? Use this program that 
         will recommmend you different movies based on your search 
         preferance of searching by genre or by actor.

"""

def scrapeData(url):
    """ Scrape data from website and return movie data
    
    Args:
        url (str): The website URL that is being scraped
    
    Returns:
        data (list): A list of movie data extracted from the website
    """
    return

class Movie:
    """ A Movie class that stores data for a particular movie
    
    Attributes:
        title (str): The title of the movie
        genre (str): The genre of the movie
        summary (str): The summary/description of the movie
        actors (list): A list of actors starring in the movie

    """
    
    def __init__(self, title, genre, summary, actors):
        """ Initializes the attributes used for the Movie class
        
        Args:
            title (str): The title of the movie
            genre (str): The genre of the movie
            summary (str): The summary/description of the movie
            actors (list): A list of actors in the movie

        """
        self.title = title
        self.genre = genre
        self.summary = summary
        self.actors = actors
    
    def extractTitles(title):
        """ Extracts movie titles from url based on if it fits the genre or actor
        
        Args:
            title (str): The title that is being extracted
        
        Returns:
            titles (list): A list of movie titles that fit the genre or actor searched for

        """
        return
    
    def extractGenres(genre):
        """ Extracts movies with same genres from a url
        
        Args:
            genre (str): The genre to that is being searched for
        
        Returns:
            genre (list): A list of movies that have the same genre searched for 

        """
    
        return
    
    def extractSummary(summary):
        """ Extracts movie summaries from url
        
        Args:
            summary (str): The summary of the movie
        
        Returns:
            summary (str): The summary of the movie
            
        """
        return

    def extractMovieActors(actors):
        """ Extracts the actors in the movie from url parsed
        
        Args:
            actors (str): The name of the actor that is being looked for from the url
        
        Returns:
            actors (list): A list of movies that match the actor which is picked
        """
        movies = []
    
        for movie in scrapeData(url):
            if actors in movie.actors:
                movies.append(movie)
        return movies
    
def userChoice():
    """ Prompts the user to choose their search preference of genre or actor
    
    Returns:
        choice (str): The user's search preference

    """
    while True:
        choice = input("Would you like to search by genre or actor? Enter 'genre' or 'actor': ")
        if choice == 'genre':
            return choice
        elif choice == 'actor':
            return choice
        else: 
            print("Invalid choice. Please enter 'genre' or 'actor': ")

def movieRecs(choice, genre, actor):
    """ Recommends movies based on user's choice of genre or actor
    
    Args:
        choice (str): The user's search choice of genre or actor
        genre (str): The movie genre searched for
        actor (str): The actor searched for
    
    Returns:
        recs (list): A list of recommended movies that match the users choice

    """
    if choice == 'genre':
        recommendations = Movie.extractGenres(genre)

    else:
        recommendations = Movie.extractMovieActors(actor)

    titles = []
    for movie in recommendations:
        titles.append(Movie.extractTitles(title))
    
    return recommendations

def main():
    """ The main method pulls all of the methods and functions to runs the code
    """
     
    userChoice = userChoice()

    if userChoice =='genre':
        genre = input('Enter a movie genre:')
        reccomendations = Movie.extractGenres(genre)
    else:
        actor = input('Enter an actor/actress name:')
        reccomendations = Movie.extractMovieActors(actor)


    recommended_movies = movieRecs(userChoice,title, genre, actor)
    

    print('We recommend the following movies:')
    for movie in recommended_movies:
        print(f"{movie.title}")


# Unit Test for userChoice
assert userChoice("genre") == "genre"
assert userChoice("actor") == "actor"
assert userChoice("invalid") == None

# Unit Test for movieRecs
assert movieRecs("genre", "", 'Science Fiction', '') == ["65", "Black Panther"]
assert movieRecs("actor", "", "", "Leonardo DiCaprio") == ["Killers of the Flower Moon", "Don't Look Up", "Speed"]
assert movieRecs("genre", "", "", "") == []


#Test Function/Unit test for extractMovieActors
def test_extractMovieActors():
    #Instances of movies
    movie1 = Movie("The Dark Knight", "Action", "Batman fights crime in Gotham City", ["Christian Bale", "Heath Ledger"])
    movie2 = Movie("Interstellar", "Sci-Fi", "A team of astronauts travel through a wormhole", ["Matthew McConaughey", "Anne Hathaway"])
    movie3 = Movie("The Prestige", "Drama", "Two magicians engage in a competitive rivalry", ["Christian Bale", "Hugh Jackman"])
    movie4 = Movie("Inception", "Action", "A thief steals corporate secrets through dream-sharing technology", ["Leonardo DiCaprio", "Tom Hardy"])
    
    allMovies = [movie1, movie2, movie3, movie4]


    assert Movie.extractMovieActors("Christian Bale", allMovies) == [movie1, movie3]

    assert Movie.extractMovieActors("Angelina Jolie", allMovies) == []
