from graph_business_trip import __version__
from graph_business_trip.graph_business_trip import *
import pytest


def test_version():
    assert __version__ == '0.1.0'


def test_business_trip(graph, city_names):
    actual = graph, city_names
    excepted = cost
    assert actual == excepted