def main(data:str):
    """
    The data is from the file. Return the str(non-digital) characters as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    b=[]
    a=[]
    for character in f:
        a.append(character)
    for i in a:
        if not (i.isdigit()):
            b.append(i)

    return b
    
# Read data from file
f = open('txt_file/data04.txt').read()
print(main(f))