def convert_hex_to_RGB(color_list):
    '''
    Given a list of color hex-codes (e.g., ['#FFAABB']),
    Convert these into a list of RGB-tuples
    :param:list
    :return:list
    '''
    assert isinstance(color_list,list)
    h2d={
        '0':0,
        '1':1,
        '2':2,
        '3':3,
        '4':4,
        '5':5,
        '6':6,
        '7':7,
        '8':8,
        '9':9,
        'A':10,
        'B':11,
        'C':12,
        'D':13,
        'E':14,
        'F':15

    }
    ans=[]
    for color in color_list:
        assert color[0]=="#"
        r_hex=color[1:3]
        g_hex=color[3:5]
        b_hex=color[5:]

        r_rgb=h2d[r_hex[0]]*16+h2d[r_hex[1]]
        g_rgb=h2d[g_hex[0]]*16+h2d[g_hex[1]]
        b_rgb=h2d[b_hex[0]]*16+h2d[b_hex[1]]

        rgb=(r_rgb,g_rgb,b_rgb)

        ans.append(rgb)
    
    return ans