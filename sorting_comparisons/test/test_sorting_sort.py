import pytest 

from sorting_comparisons.sorting_comparisons import Movie,sort_by_most_recent_year,movies,sort_alphabetically_by_title


def test_sorted_by_year():
    sorted_by_year_list = sort_by_most_recent_year(movies)
    clearly_list = []
    for i in sorted_by_year_list :
        clearly_list.append([i.title,i.year])
    actuly = clearly_list
    expected = [['A Quiet Place', 2018], ['The Avengers', 2012], ['Avatar', 2009], ['Anchorman', 2004]]
    assert actuly == expected

def test_sorted_by_title():
    sorted_by_title = sort_alphabetically_by_title(movies)
    clearly_list = []
    for i in sorted_by_title:
        clearly_list.append(i.title)
    actuly = clearly_list
    expected = ['Anchorman', 'Avatar', 'The Avengers', 'A Quiet Place']
    assert actuly == expected