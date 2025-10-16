def pour_chai(n):
    if n == 0:
        return "All cups poured"
    return pour_chai( n - 1 )