import tokenize


def parse_code(file_path: str):
    with open(file_path, 'rb') as file:
        # for x in tokenize.tokenize(readline=file.readline):
        #     print(x)
        # exit()
        # for toktype, tok, start, end, line in tokenize.tokenize(file.readline):
        #     if toktype == tokenize.STRING and '\n' in tok:
        #         print(f"{toktype}, {line}, {tok}")

        for tok in tokenize.tokenize(file.readline):
            print(tokenize.tok_name[tok.type], tokenize.tok_name[tok.exact_type], repr(tok.string))

parse_code('../urap-scrape/scrape.py')
