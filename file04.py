def main(data:str):
    """
    The data is from the file. Return the str(non-digital) characters as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    a=[]
    for character in f:
        a.append(character)
    return a
    
# Read data from file
f = open('txt_file/data04.txt').read()
print(main(f))