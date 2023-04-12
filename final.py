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
        return
    
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
        return
    
def userChoice():
    """ Prompts the user to choose their search preference of genre or actor
    
    Returns:
        choice (str): The user's search preference

    """
    return choice

def movieRecs(choice, title, genre, actor):
    """ Recommends movies based on user's choice of genre or actor
    
    Args:
        choice (str): The user's search choice of genre or actor
        title (str): The movie title searched for
        genre (str): The movie genre searched for
        actor (str): The actor searched for
    
    Returns:
        recs (list): A list of recommended movies that match the users choice

    """
    return

def main():
    """ The main method pulls all of the methods and functions to runs the code

    """
    return