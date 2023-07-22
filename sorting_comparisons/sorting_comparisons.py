class Movie:
    def __init__(self, title, year, genres):
        self.title = title
        self.year = year
        self.genres = genres

    

def sort_by_most_recent_year(movies):
    '''
    Sort movies in descending order based on the year property
    
    '''
    return sorted(movies, key=lambda movie: movie.year, reverse=True)



def sort_alphabetically_by_title(movies):
    '''
    Function to sort movies alphabetically by title, ignoring leading "A"s, "An"s, or "The"s
    '''

    def custom_title_comparison(movie):
        '''
        Custom comparison function to ignore leading "A"s, "An"s, or "The"s in the movie titles
   
        '''
        ignore_words = ["A", "An", "The"]
        title = movie.title


        def remove_leading_words(title):
            '''
            Function to remove leading words from the title
            
            '''
            words = title.split(" ")
            if words[0] in ignore_words:
                return " ".join(words[1:])
            return title

        modified_title = remove_leading_words(title)
        return modified_title

    return sorted(movies, key=custom_title_comparison)




movies = [
    Movie("The Avengers", 2012, ["Action", "Adventure", "Sci-Fi"]),
    Movie("Avatar", 2009, ["Action", "Adventure", "Fantasy"]),
    Movie("Anchorman", 2004, ["Comedy"]),
    Movie("A Quiet Place", 2018, ["Drama", "Horror", "Sci-Fi"]),
]

if __name__ == "__main__":
    pass

    # print("Sorted by most recent year:")
    # sorted_by_year = sort_by_most_recent_year(movies)
    # for movie in sorted_by_year:
    #     print(f"{movie.title} - {movie.year}")

    # print("\nSorted alphabetically by title (ignoring 'A', 'An', 'The'):")
    # sorted_by_title = sort_alphabetically_by_title(movies)
    # for movie in sorted_by_title:
    #     print(f"{movie.title} - {movie.year}")

    # sorted_by_year_list = sort_by_most_recent_year(movies)
    # clearly_list = []
    # for i in sorted_by_year_list :
    #     clearly_list.append(i.title)
    # print(clearly_list)

    # sorted_by_title = sort_alphabetically_by_title(movies)
    # clearly_list = []
    # for i in sorted_by_title:
    #     clearly_list.append(i.title)
    # print(clearly_list)