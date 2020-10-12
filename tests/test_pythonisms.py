from pythonisms import __version__
from pythonisms.linked_list import *

def test_equality():
    first = LinkedList(['t', 'e', 's', 't'])
    second = LinkedList(['t', 'e', 's', 't', 'i', 'n', 'g'])

    assert (first == second) == False


def test_str():
    ll = LinkedList(['t', 'e', 's', 't'])

    assert ll.__str__() == '[ t ] -> [ e ] -> [ s ] -> [ t ] -> None'

def test_get_item():

    ll = LinkedList(['t', 'e', 's', 't'])
    assert ll[0] == 't'
    assert ll[1] == 'e'
    assert ll[2] == 's'
    assert ll[3] == 't'