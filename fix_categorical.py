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


def fix_categorical(x):
    """_summary_

    Args:
        x (_type_): _description_

    Returns:
        _type_: _description_
    """
    #add_month_yr(x)
    t = pd.CategoricalDtype(categories=['Sep-2017', 'Jan-2018', 'Feb-2018',
                            'Mar-2018', 'Apr-2018', 'Sep-2018', 'Oct-2018', 'Jan-2019'], ordered=True)
    x['month-yr'] = x['month-yr'].astype(t)
    x.groupby('month-yr')['Timestamp'].count().to_frame().sort_index()
    return x


if __name__ == "__main__":
    x = pd.read_csv('survey_data.csv')
    b = fix_categorical(x)
    print(b)
