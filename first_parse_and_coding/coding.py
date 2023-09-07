coding = {
    ":": 1,
    "(": 2,
    ")": 3,
    ".": 4,
    "*": 5,
    ";": 6,
    ",": 7,
    "#": 8,
    "[": 9,
    "]": 10,
    "Eofgram": 1000,
}


def parse_tokens(text: str) -> [str]:
    tokens = []
    separators = list(coding.keys())
    separators.extend([" ", "\n"])
    tail = ""
    for i in range(len(text)):
        char = text[i]
        if not char in separators:
            tail += char
        else:
            if tail == "":
                if char != " ":
                    tokens.append(char)
                continue
            if tail[0] == "'" and len(tail) == 1:
                tail += char
                continue
            if tail != "":
                tokens.append(tail)
            tail = ""
    return tokens


def encoder(file_path: str):
    with open(file_path, encoding="UTF-8") as file:
        text = file.read()
    tokens = parse_tokens(text)
    counter = {"nonterms": 0, "terms": 0, "semantics": 0}
    result = ""
    for i in range(len(tokens)):
        token = tokens[i]
        if token in coding:
            result += f"{coding[token]}, "

        elif token == "\n":
            result += token
        else:
            if token[0] == "$":
                counter["semantics"] += 1
                coding[token] = 100 + counter["semantics"]
                result += f"{coding[token]}, "
            elif tokens[i + 1] == ":":
                counter["nonterms"] += 1
                coding[token] = 10 + counter["nonterms"]
                result += f"{coding[token]}, "
            else:
                counter["terms"] += 1
                coding[token] = 50 + counter["terms"]
                result += f"{coding[token]}, "
    return result.strip().strip(",")


file_path = input(
    "Введите путь до файла или его имя, если он находится в этой же папке:\n"
)
result = coder(file_path)
with open("result.txt", "w", encoding="UTF-8") as file:
    file.write(result + "\n")
for token in coding:
    print(f"{token}  {coding[token]}")
