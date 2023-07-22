import pytest



movies = [
    Movie("The Avengers", 2012, ["Action", "Adventure", "Sci-Fi"]),
    Movie("Avatar", 2009, ["Action", "Adventure", "Fantasy"]),
    Movie("Anchorman", 2004, ["Comedy"]),
    Movie("A Quiet Place", 2018, ["Drama", "Horror", "Sci-Fi"]),
]

def test_sorted_by_year():
    sorted_by_year_list = sort_by_most_recent_year(movies)
    clearly_list = []
    for i in sorted_by_year_list :
        clearly_list.add(sorted_by_year_list[i].title)
    actuly = clearly_list
    expected = ["A Quiet Place","The Avengers","Avatar","Anchorman"]
    assert actuly == expected