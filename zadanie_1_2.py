
def alfaStr(source: str) -> str:
    """
    Remove from string all characters except english symbols and space
    >>> alfaStr("without changes")
    'without changes'
    >>> alfaStr("without CHANGES symbols")
    'without changes symbols'
    >>> alfaStr("delete. points...")
    'delete points'
    >>> alfaStr("delete non english символов")
    'delete non english '
    >>> alfaStr("remove. ALL: non английских english symbols")
    'remove all non  english symbols'
    """
    return "".join(c.lower() for c in source if 'a' <= c <= "z" or 'A' <= c <='Z' or ' ' == c)


if __name__=="__main__":
    import doctest
    doctest.testmod(verbose=True)
    #print(alfaStr("qwer tyui TGYH . >> йфцы >> ggg"))
