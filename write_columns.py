import csv
def write_columns(data,fname):
    '''
    Write a function that can write the following formula to three columns to a comma-separated file:

    data_value, data_value**2, (data_value+data_value**2)/3.

    Here is your function signature write_columns(data,fname). Your written floating-point values should be formatted to the hundreths place. 
    Your function can only accept lists of integers/floats as input.
    Note that fname is a string and data must be a list.
    '''
    assert isinstance(data,list)
    assert isinstance(fname,str)
    for d in data:
        assert isinstance(d,int) or isinstance(d,float)
    


    with open(fname,'w') as f:
        writer=csv.writer(f,delimiter=',')
        for d in data:
            cal=['{:.2f}'.format(d),'{:.2f}'.format(d**2),'{:.2f}'.format((d+d**2)/3)]
            writer.writerow(cal)