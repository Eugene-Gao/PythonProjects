def printLTS(l, *args, loggerFunct=None, **kwargs):
    result = listToStr(l, *args, **kwargs)
    if loggerFunct is not None:
        loggerFunct(result)
    else:
        print(result)