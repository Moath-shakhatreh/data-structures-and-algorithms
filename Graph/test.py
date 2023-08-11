import pytest 
from Graph.graph import Graph

def test_if_Vertex_can_be_successfully_added__to_the_graph():
    g = Graph()
    a = g.add_vertix('A')
    actual = g.breadth_first(a)
    expected = ['A']
    assert actual == expected  
def test_An_edge_can_be_successfully_added_to_the_graph():
    g = Graph()
    a = g.add_vertix('A')
    b = g.add_vertix('B')
    g.add_edge(a,b)
    actual = (g.get_neighbors(a)[0]).vertix.value
    expected = "B"
    assert actual == expected  
def test_A_collection_of_all_vertices_can_be_properly_retrieved_from_the_graph():
    g = Graph()
    a = g.add_vertix('A')
    b = g.add_vertix('B')
    e = g.add_vertix('E')
    c = g.add_vertix('C')
    d = g.add_vertix('D')
    g.add_edge(a,b)
    g.add_edge(a,c)
    g.add_edge(b,d)
    g.add_edge(b,e)
    g.add_edge(e,d)
    g.add_edge(e,c)
    actual = g.breadth_first(a)
    expected = ['A', 'B', 'C', 'D', 'E']
    assert actual == expected

def test_All_appropriate_neighbors_can_be_retrieved_from_the_graph():
    g = Graph()
    a = g.add_vertix('A')
    b = g.add_vertix('B')
    e = g.add_vertix('E')
    c = g.add_vertix('C')
    d = g.add_vertix('D')
    g.add_edge(a,b)
    g.add_edge(a,c)
    g.add_edge(b,d)
    g.add_edge(b,e)
    g.add_edge(e,d)
    g.add_edge(e,c)
    
    actual = (g.get_neighbors(a)[0]).vertix.value
    expected = "B"
    actual_1 = (g.get_neighbors(a)[1]).vertix.value
    expected_1 = "C"
    assert actual == expected  
    assert actual_1 == expected_1 

def test_Neighbors_are_returned_with_the_weight_between_vertices_included():
    g = Graph()
    a = g.add_vertix('A')
    b = g.add_vertix('B')
    g.add_edge(a,b)
    actual = (g.get_neighbors(a)[0]).weight
    expected = 0
    assert actual == expected 

def test_The_proper_size_is_returned_representing_the_number_of_vertices_in_the_graph():
    g = Graph()
    a = g.add_vertix('A')
    b = g.add_vertix('B')
    g.add_edge(a,b)
    actual = g.size()
    expected = 2
    assert actual == expected 

def test_A_graph_with_only_one_vertex_and_edge_can_be_properly_returned():
    g = Graph()
    a = g.add_vertix('A')
    
    actual = g.get_neighbors(a)
    expected = []
    assert actual == expected