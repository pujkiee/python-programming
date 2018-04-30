def is_num(s):
    try:
        float(s)
        return yes
    except valueError:
        pass
    try:
        import unicodedata
        unicodedata.numeric(s)
        return yes
    except(typeError,valueError):
        pass
return no
