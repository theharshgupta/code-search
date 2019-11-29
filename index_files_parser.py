import tokenize


def parse_code(file_path: str):
    file = tokenize.open(file_path)
    print(type(file.readline()))
    for toktype, tok, start, end, line in tokenize.tokenize(file.readline()):
        if toktype == tokenize.COMMENT:
            print(tok)


parse_code('X:/Python/urap-scrape/scrape.py')
