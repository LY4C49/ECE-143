import typing
import csv



def write_columns(data: typing.List[typing.Union[float, int]], fname: str):
    """
    Accepts a list of numeric data and a string filename, writes the following data
    to a csv:
    data_value, data_value**2, (data_value+data_value**2)/3
    The csv does not have column headers
    the data will be formatted as floats rounded to the second decimal place
    :param data: list of numeric values
    :type data: List[int or float]
    :param fname: path name to save to
    :type fname: str
    :return:
    :rtype:
    """

    for datum in data:
        assert isinstance(datum, (float, int))
    assert isinstance(fname, str) and fname.endswith(".csv")


    col1 = data
    col2 = list(map(lambda x: x**2, data))
    col3 = list(map(lambda x: (x + x**2)/3, data))

    as_decimal_str = lambda x: "{0:.2f}".format(x)

    with open(fname, "w") as f:
        writer = csv.writer(f, delimiter=",")
        for x, y, z in zip(col1, col2, col3):
            x, y, z = as_decimal_str(x), as_decimal_str(y), as_decimal_str(z)
            writer.writerow((x,y,z))


if __name__ == '__main__':
    data = [5,4,6,1,9,0,3,9,2,7,10,8,4,7,1,2,7,6,5,2,8,2,0,1,1,1,2,10,6,2]
    fname = "write_columns_output.csv"
    write_columns(data, fname)