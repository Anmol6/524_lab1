def standard_deviation(x):
    n = len(x)
    mean = sum(x) / n
    ssq = sum((y-mean)**2 for y in x)
    stdev = (ssq/n)**0.5
    return(stdev)
