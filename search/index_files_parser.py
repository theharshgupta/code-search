import tokenize
import pandas as pd


def parse_code(file_path: str):
    """Function to extract docstring and function string by tokenizing
    :param file_path: python file that has to be tokenized
    :return: None
    """
    result = []
    with open(file_path, 'rb') as file:

        tokens = list(tokenize.tokenize(file.readline))
        for index_token, token in enumerate(tokens):
            data = {}
            if token.type == tokenize.STRING and '"""' in token.string:
                # print(f"{tokens[index_token-10:index_token+10]}")
                # print(f"FUNCTION: {tokens[index_token-2].line}")
                if 'def' in tokens[index_token - 2].line:
                    line_function = tokens[index_token - 2].line
                    line_docstring = token.line
                    data["filename"] = file_path
                    data["function"] = line_function.replace('\n', '').replace('def', '').replace(':', '').strip()
                    data["docstring"] = line_docstring.replace('\n', '').replace('\"\"\"', '').replace('  ', ' ').strip()
                    result.append(data)
    return result


def parse_test(file_path: str):
    """
    function just for testing using dataframe 
    :param file_path: the filename and filepath
    :return: None
    """
    with open(file_path, 'rb') as file:
        df = pd.DataFrame().from_records(list(tokenize.tokenize(file.readline)))
        df.columns = ['type', 'token', 'start', 'end', 'line']
        for g in df.groupby('line'):
            if 'def' in g[0]:
                print(g[1].to_string())
        # print(df.to_string())

        # for token in tokenize.tokenize(file.readline):
        #     print(token)
        #     print(f"start {token.start} end {token.end}")

# Mac path
# parse_code('../urap-scrape/scrape.py')
# Windows path
