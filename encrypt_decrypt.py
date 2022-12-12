from concurrent.futures import process


class CodeBook:
    def __init__(self, fname) -> None:
        assert isinstance(fname, str)
        self.source_book = open(fname)
        self.word_position = {}
        self.punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        self.read_handler = self.source_book.readlines()

    def generate_wordPosition(self):
        read_handler = self.read_handler
        for i in range(len(read_handler)):
            origin_line = read_handler[i]
            process_line = self.process_line(origin_line)
            # print(process_line)
            for pos, word in enumerate(process_line):
                if word not in self.word_position:
                    self.word_position[word] = [(i+1, pos+1)]
                else:
                    self.word_position[word].append((i+1, pos+1))

    def _removePunc(self, str):
        for ele in str:
            if ele in self.punc:
                str = str.replace(ele, "")
        return str

    def process_line(self, line):
        processed = self._removePunc(line).lower().split("\n")[0].split(" ")
        if "" in processed:
            processed.remove("")
        if " " in processed:
            processed.remove(" ")
        return processed


def encrypt_message(message, fname):
    """_summary_

    Args:
        message (_type_): _description_
        fname (_type_): _description_

    Returns:
        _type_: _description_
    """
    assert isinstance(message, str)
    assert isinstance(fname, str)
    codeBook = CodeBook(fname=fname)
    codeBook.generate_wordPosition()
    used_position = set()
    encrypted = []
    message = message.split(" ")
    for word in message:
        if word in codeBook.word_position:
            candidates = codeBook.word_position[word]
            for c in candidates:
                if c not in used_position:
                    encrypted.append(c)
                    used_position.add(c)
                    break
    return encrypted


def decrypt_message(inlist, fname):
    """_summary_

    Args:
        inlist (_type_): _description_
        fname (_type_): _description_
    """
    assert isinstance(inlist, list)
    assert isinstance(fname, str)
    codeBook = CodeBook(fname=fname)
    decrypted = []
    for en_word in inlist:
        row, offset = en_word
        line = codeBook.read_handler[row-1]
        processed_line = codeBook.process_line(line=line)
        de_word = processed_line[offset-1]
        decrypted.append(de_word)
    return " ".join(decrypted)


if __name__ == "__main__":
    cb = CodeBook("pg5200.txt")
    cb.generate_wordPosition()
    let_list = cb.word_position["let"]
    print((1394, 2) in let_list)
    pwd = encrypt_message(
        "let us not say we met late at the night about the secret", "pg5200.txt")
    print(pwd)
    res = decrypt_message(pwd, "pg5200.txt")
    print(res)
