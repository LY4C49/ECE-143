import os
import readline
import sys


class file_operation:
    def __init__(self, fname) -> None:
        """_summary_

        Args:
            fname (_type_): _description_
        """
        assert isinstance(fname, str)
        self.filename = fname
        self.surfix = fname.split(".")[-1]
        self.openFile = open(file=self.filename)
        self.lineReader = self.openFile.readlines()
        self.lineNumber = len(self.lineReader)
        self.fileSize = os.path.getsize(self.filename)
        print(self.surfix, self.lineNumber, self.fileSize)

    def get_line(self, n):
        if n < self.lineNumber:
            content = self.lineReader[n]
            line_size = sys.getsizeof(content)
            return content
        else:
            return False


def split_by_n(fname, n=3):
    """_summary_

    Args:
        fname (_type_): _description_
        n (int, optional): _description_. Defaults to 3.
    """
    assert isinstance(fname, str)
    assert isinstance(n, int) and n > 0
    file = file_operation(fname=fname)
    appox_size = int(file.fileSize/n)
    line_ptr = 0
    for i in range(n):
        new_fname = file.filename+"_" + str(i).zfill(3)+"."+file.surfix
        with open(new_fname, "wt") as f:
            while (os.path.getsize(new_fname) <= appox_size):
                if line_ptr <= file.lineNumber:
                    line = file.get_line(line_ptr)
                    if line:
                        f.write(line)
                    line_ptr += 1
                else:
                    break

    # print(appox_size)


if __name__ == "__main__":
    split_by_n("pg5200.txt", 3)
    print(os.path.getsize("pg5200.txt_000.txt"), os.path.getsize(
        "pg5200.txt_001.txt"), os.path.getsize("pg5200.txt_002.txt"))
