def countList(list):
    if list==[]:
        return 1
    element = list[0]
    return element * countList(list[1:])
