import requests
from bs4 import BeautifulSoup
import time
import unittest


class Movie:
    """A Movie Class that stores data for a particular movie"""

    def __init__(self, title, genre, summary, actors):
        self.title = title
        self.genre = genre
        self.summary = summary
        self.actors = actors

    def __str__(self):
        return f"{self.title} ({self.genre}) - {self.summary}\nLead Actor: {self.actors}\n"


    def scrape_movies(genre):
        """Scrapes data from Imdb database"""
        movies = [] #empty list of movie objects
        url = 'https://www.imdb.com/search/title/?title_type=feature&genres={}&start={}' #url for scraping data
        databasepage = 1
        while databasepage <= 10: #loop through databse up to 10th page
            resp = requests.get(url.format(genre, (databasepage-1)*50)) #request to url with genre and page
            if resp.status_code != 200: #if no response is gotten, we break
                break
            resp = requests.get(url.format(genre, databasepage*50)) #sends another request with the next page
            s = BeautifulSoup(resp.content, 'html.parser') #parses the HTML content
            #extracts this information using CSS selectors
            titles = [tit.get_text().strip() for tit in s.select('.lister-item-header a')]
            genres = [gen.get_text().strip() for gen in s.select('.genre')]
            summaries = [summ.get_text().strip() for summ in s.select('.ratings-bar+ .text-muted')]
            actors = [act.get_text().strip() for act in s.select('.lister-item-content .ghost + a')]
            #makes a movie object for each movie and adds it to the list
            movies += [Movie(tit, gen, summ, act) for tit, gen, summ, act in zip(titles, genres, summaries, actors)]
            if s.select('.lister-page-next.disabled'): #if there isnt a next page button, break the loop
                break
            databasepage+=1 #increment page and wait 5 seconds before going to the next one and scraping it
            time.sleep(5)

        return movies #return list



    def extractGenres(genre, movies):
        """Extracts movies of a user-specified genre"""
        genre_movies = []
        for movie in movies:
            if genre in movie.genre:
                genre_movies.append(movie)
        return genre_movies


    def extractMovieActors(actor, movies):
        """Extracts movies of a user-specified actor/actress"""
        actor_movies = []
        for movie in movies:
            if actor in movie.actors:
                actor_movies.append(movie)
        return actor_movies


    def userChoice():
        """Asks the user for favorite genre and actor/actress"""
        genre = input("Enter your desired genre: ")
        actor = input("Enter your preferred actor/actress: ")
        return genre, actor


    def movieRecs(genre, actor):
        """Recommends movies based on the user's preferred genre and actor/actress"""
        url = 'https://www.imdb.com/search/title/?title_type=feature&genres={}&start={}'
        movies = Movie.scrape_movies(genre)

        if genre:
            movies = Movie.extractGenres(genre, movies)

        if actor:
            movies = Movie.extractMovieActors(actor, movies)

        return movies


def main():
    genre, actor = Movie.userChoice()
    movies = Movie.movieRecs(genre, actor)

    print('\nRecommended Movies:')
    for movie in movies:
        print(movie)


if __name__ == '__main__':
    main()

class TestScrapeData(unittest.TestCase):
    def testscrapeData(self):
        m=Movie.scrape_movies('Horror',1)
        self.assertIsInstance(m,list)
        self.assertTrue(all(isinstance(mo,Movie) for mo in m))
        self.assertEqual(len(m,50))
