"""A Dictionary test program"""

__author__ = "730621026"

from exercises.ex03.dictionary import invert, favorite_color, count, bin_len


def test_invert0() -> None:
    """Edge case test for invert function"""
    assert invert({}) == {}


def test_invert1() -> None:
    """Use case test for invert function"""
    assert invert({"a": "b"}) == {"b": "a"}


def test_invert2() -> None:
    """2nd Use case test for invert function"""
    assert invert({"five": "four"}) == {"four": "five"}


def test_count0() -> None:
    """Edge case test for count function"""
    assert count([]) == {}


def test_count1() -> None:
    """Use case test for count function"""
    assert count(["five", "five", "four"]) == {"five": 2, "four": 1}


def test_count2() -> None:
    """2nd Use case test for count function"""
    assert count(["five", "four", "four"]) == {"five": 1, "four": 2}


def test_favorite_color0() -> None:
    """Edge case test for favorite_color function"""
    assert favorite_color({}) == ""


def test_favorite_color1() -> None:
    """Use case test for favorite_color function"""
    assert favorite_color({"Jeff": "blue", "James": "blue", "John": "Red"}) == "blue"


def test_favorite_color2() -> None:
    """2nd Use case test for favorite_color function"""
    assert favorite_color({"Jeff": "Blue", "James": "Red"}) == "Blue"


def test_bin_len0() -> None:
    """Edge case test for bin_len function"""
    assert bin_len([]) == {}


def test_bin_len1() -> None:
    """Use case test for bin_len function"""
    assert bin_len(["five", "four"]) == {4: {"five", "four"}}


def test_bin_len2() -> None:
    """2nd Use case test for bin_len function"""
    assert bin_len(["a", "bb"]) == {1: {"a"}, 2: {"bb"}}
