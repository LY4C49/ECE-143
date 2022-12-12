import pandas as pd


def add_month_yr(x):
    """_summary_

    Args:
        x (_type_): _description_

    Returns:
        _type_: _description_
    """
    assert isinstance(x, pd.DataFrame)
    # csv_file=pd.read_csv("survey_data.csv")
    # print(type(x))
    ts_df = x["Timestamp"]
    # print(ts_df)
    month_list = ['Jan', 'Feb', 'Mar', 'Apr', 'May',
                  'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    ts_list = []
    for ts in ts_df:
        date = ts.split(" ")[0]
        mmddyy = date.split("/")
        ts_list.append(str(month_list[int(mmddyy[0])-1]+"-"+mmddyy[2]))
    x['month-yr'] = ts_list
    return x


def count_month_yr(x):
    """_summary_

    Args:
        x (_type_): _description_

    Returns:
        _type_: _description_
    """
    assert isinstance(x, pd.DataFrame)
    df = add_month_yr(x)

    mmyy_df = df["month-yr"]

    mmyy_count = {}

    for my in mmyy_df:
        if my not in mmyy_count:
            mmyy_count[my] = 1
        else:
            mmyy_count[my] += 1

    count_df = pd.DataFrame.from_dict(
        mmyy_count, orient="index", columns=["Timestamp"])
    return count_df

# if __name__=="__main__":
#     print(count_month_yr(pd.read_csv("survey_data.csv")))
