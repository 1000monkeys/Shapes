def isFloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False
