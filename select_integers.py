def select_integers(a,b,c):
    total_diff = b - a
    if total_diff>=c-1:
        each_diff = total_diff//(c-1)
        numbers = list(range(b-each_diff*(c-1), b+1, each_diff))
    else:
        numbers=list(range(a,b+1))+[b]*((c-1)-b+a)
    return numbers
