import itertools
"""_summary_
You are given a sequence of n lower-case letters and a k-tuple of integers that indicate partition-lengths of the sequence. 
Also, you have a dictionary of commonly used words. 
The n letters represent a phrase of k words where the length of the jth word is the jth element of the tuple.

Here is an example: w = 'trleeohelh' , k=(5,5). Your generator descrambler(w,k) should iteratively yield the output ['hello three','three hello','hello there','there hello']. Note that because both words have 5 characters, it is not possible to definitively know the order of the phrase.

Here are more interesting examples:

>>> list(descrambler('choeounokeoitg',(3,5,6)))
 ['one tough cookie',
  'one ought cookie',
  'neo tough cookie',
  'neo ought cookie']
 >>> list(descrambler('qeodwnsciseuesincereins',(4,7,12)))
 ['wise insider consequences']
"""

def compare(criterion: list, test: str) -> bool:
    """_summary_

    Args:
        criterion (list): _description_
        test (str): _description_

    Returns:
        bool: _description_
    """
    assert isinstance(criterion, list)
    assert isinstance(test, str)
    count_test = [0]*26
    for s in test:
        count_test[ord(s)-ord('a')] += 1
    return True if count_test == criterion else False


def process_file(file_path):
    """_summary_

    Args:
        file_path (_type_): _description_

    Returns:
        _type_: _description_
    """
    assert isinstance(file_path, str)
    common_words = {}
    with open(file=file_path) as f:
        word = "_"
        while word != "":
            word = f.readline().split('\n')[0]
            if word != "":
                if len(word) not in common_words:
                    common_words[len(word)] = set()
                    common_words[len(word)].add(word)
                else:
                    common_words[len(word)].add(word)
    return common_words

def descrambler(w: str, k: tuple) -> list:
    """_summary_

    Args:
        w (str): _description_
        k (tuple): _description_

    Returns:
        list: _description_
    """
    assert isinstance(w, str)
    assert isinstance(k, tuple)
    for x in w:
        assert ord('a')<=ord(x)<ord('z')
    for value in k:
        assert isinstance(value, int) and value >= 1

    common_words = process_file('/tmp/google-10000-english-no-swears.txt')

    #Get the feture of w
    count_alaph = [0]*26
    for alph in w:
        count_alaph[ord(alph)-ord('a')] += 1

    prob_words = []
    
    #Calculate all possible candidates of every element in k
    for value in k:
        word_set = set()
        for word in itertools.permutations(w, value):
            word="".join(word)
            if word in common_words[value]:
                word_set.add(word)
        prob_words.append(list(word_set))
    ans = []
    result = []

    def backtracking(x: list, index):
        """_summary_

        Args:
            x (list): _description_
            index (_type_): _description_
        """
        if index == len(prob_words):
            concat_word = "".join(result)
            #If the concat word has the same feature with criterion, then it is a valid result
            if compare(criterion=count_alaph, test=concat_word):
                ans.append(" ".join(result))
                return
            else:
                return
        curr_wordset = x[index]
        for i in range(len(curr_wordset)):
            result.append(curr_wordset[i])
            backtracking(x, index+1)
            result.pop(-1)

    backtracking(prob_words, 0)
    res=list(set(ans))
    for i in range(len(res)):
        yield res[i]
    


if __name__=='__main__':
    print(descrambler('choeounokeoitg',(3,5,6)))
