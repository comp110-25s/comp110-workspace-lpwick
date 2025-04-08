"""A Dictionary program"""

__author__ = "730621026"


def invert(input: dict[str, str]) -> dict[str, str]:
    invert_dict: dict[str, str] = dict()
    for pair in input.items():
        key = pair[0]
        value = pair[1]
        if value in invert_dict:
            raise KeyError("Error Duplicate Keys Detected")
        invert_dict[value] = key
    return invert_dict


def count(items: list[str]) -> dict[str, int]:
    result_dict: dict[str, int] = dict()
    for key in items:
        if key in result_dict:
            result_dict[key] += 1
        else:
            result_dict[key] = 1
    return result_dict


def favorite_color(fav_color: dict[str, str]) -> str:
    color_count = {}
    for key in fav_color:
        color = fav_color[key]
        if color in color_count:
            color_count[color] += 1
        else:
            color_count[color] = 1
    max_count = 0
    most_frequent_color = ""
    for color in color_count:
        if color_count[color] > max_count:
            max_count = color_count[color]
            most_frequent_color = color
    return most_frequent_color


def bin_len(strings: list[str]) -> dict[int, set[str]]:
    bins: dict[int, set[str]] = {}
    for string in strings:
        length = len(string)
        if length not in bins:
            bins[length] = set()
        bins[length].add(string)
    return bins
