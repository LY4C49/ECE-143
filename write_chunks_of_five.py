def write_chunks_of_five(words,fname):
    '''
    Using corpus of 10,000 common English words, 
    create a new file that consists of each consecutive non-overlapping sequence of five lines merged into one line. 
    Here are the first 10 lines of ouptut corresponding to the above sample corpus:
    '''
    assert isinstance(words,list)
    assert isinstance(fname,str)

    with open(fname,'w') as f:
        line=[]
        for i,word in enumerate(words):
            if i%5==0 and i!=0:
                line_word=" ".join(line)
                f.write(line_word+"\n")
                line=[]
            line.append(word)
        
        line_word=" ".join(line)
        f.write(line_word+"\n")

