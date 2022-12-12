import pandas as pd


def split_count(x):
    """_summary_

    Args:
        x (pd.Series): the column you want to count

    Returns:
        df (pd.dataframe): result
    """
    assert isinstance(x, pd.Series)
    print(len(x))
    reason_count_dict = {}
    for element in x:
        element_list = element.split(', ')
        for e in element_list:
            if e not in reason_count_dict:
                reason_count_dict[e] = 1
            else:
                reason_count_dict[e] += 1

    # keys of the dict as the row
    df = pd.DataFrame.from_dict(
        reason_count_dict, orient='index', columns=['count'])
    return df


# if __name__ == "__main__":
#     csv_file = pd.read_csv("survey_data.csv")
#     series = csv_file["Is there anything in particular you want to use Python for?"]
#     res = split_count(x=series)
#     print(res)
