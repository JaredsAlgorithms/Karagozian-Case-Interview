import json

path = "/home/jared/Projects/Karagozian-Case-Interview/inputs/word_search_02.json"

with open(path, "r", encoding="utf-8") as fil_ptr:
    content = json.load(fil_ptr)

match content:
    case {
        "dimensions": (ROW, COL),
        "board": board,
        "mode": mode,
        "word_count": count,
        "words": words,
    }:
        board = list(map(list, board.split("|")))
        assert len(words) == count

    case _:
        raise Exception("parsing error")

