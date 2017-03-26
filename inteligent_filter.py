def IN_FI(TREE, template):
    """
    This is a filter to extract the data we want from our
    decripted files. Example of input:
    print(INT_filter([['p','Hello',0],['h1','World',1],['div','!',2]],
               {'filter':[['p',1],['h1',2]]}))
    And the output is:
    [['p', 'Hello', 0], ['h1', 'World', 1]]

    The first value is the data, the second is the filter data.
    When you parse data through send a array of arrays that contain
    three values. two string and one number. Example:
    [
        ['p', 'hello world', 0],
        ['h1 style="..."', 'I love you!', 1]
    ]
    """
    #extracted data varible
    datafilterd = []
    tl = 0
    while tl != len(template['filter']):
        x = 0
        while x != len(TREE):
            if TREE[x][0][0:template['filter'][tl][1]] == template['filter'][tl][0]:
                datafilterd.append(TREE[x])
            x += 1
        tl += 1

    #returns extracted data varible
    return datafilterd

if __name__ == '__main__':
    print(INT_filter([['p','Hello',0],['h1','World',1],['div','!',2]],
               {'filter':[['p',1],['h1',2]]}))
