import random

class Movie:
    """Class representing a movie."""
    def __init__(self, title, year, genre, plays=0):
        self.title = title
        self.year = year
        self.genre = genre
        self.plays = plays

    def play(self):
        """Increase the number of plays by 1."""
        self.plays += 1

    def __str__(self):
        """String representation of a movie."""
        return f"{self.title} ({self.year})"

    def __repr__(self):
        """Representation for debugging."""
        return f"Movie(title={self.title}, year={self.year}, genre={self.genre}, plays={self.plays})"


class Series(Movie):
    """Class representing a TV series."""
    def __init__(self, title, year, genre, season, episode, plays=0):
        super().__init__(title, year, genre, plays)
        self.season = season
        self.episode = episode

    def __str__(self):
        """String representation of a series."""
        return f"{self.title} S{self.season:02d}E{self.episode:02d}"

    def __repr__(self):
        """Representation for debugging."""
        return (f"Series(title={self.title}, year={self.year}, genre={self.genre}, "
                f"season={self.season}, episode={self.episode}, plays={self.plays})")


library = []


def add_to_library(item):
    """Add a movie or series to the library."""
    library.append(item)


def get_movies():
    """Return a list of movies sorted alphabetically by title."""
    return sorted([item for item in library if isinstance(item, Movie) and not isinstance(item, Series)], 
                  key=lambda x: x.title)


def get_series():
    """Return a list of series sorted alphabetically by title."""
    return sorted([item for item in library if isinstance(item, Series)], 
                  key=lambda x: x.title)


def search(title):
    """Search for a movie or series by title."""
    for item in library:
        if item.title.lower() == title.lower():
            return item
    return None


def generate_views():
    """Randomly add views to a random item in the library."""
    item = random.choice(library)
    views = random.randint(1, 100)
    item.plays += views


def generate_views_multiple(times=10):
    """Generate views multiple times."""
    for _ in range(times):
        generate_views()


def top_titles(n, content_type=None):
    """
    Return the top n titles by number of plays.
    :param n: Number of top titles to return.
    :param content_type: Filter by 'movie' or 'series'. If None, include all.
    """
    if content_type == "movie":
        filtered = get_movies()
    elif content_type == "series":
        filtered = get_series()
    else:
        filtered = library
    return sorted(filtered, key=lambda x: x.plays, reverse=True)[:n]


# Example data
add_to_library(Movie("Pulp Fiction", 1994, "Crime"))
add_to_library(Movie("The Godfather", 1972, "Crime"))
add_to_library(Series("The Simpsons", 1989, "Comedy", 1, 5))
add_to_library(Series("Breaking Bad", 2008, "Drama", 1, 1))
add_to_library(Series("Game of Thrones", 2011, "Fantasy", 1, 1))

# Example usage
print("Movies in library:", get_movies())
print("Series in library:", get_series())

generate_views_multiple()

print("\nTop 3 titles:")
for item in top_titles(3):
    print(f"{item} - Plays: {item.plays}")

print("\nSearch for 'Pulp Fiction':", search("Pulp Fiction"))
print("\nSearch for 'The Simpsons':", search("The Simpsons"))
