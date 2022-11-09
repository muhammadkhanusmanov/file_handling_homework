def main(data:str):
    """
    The data is from the file. Return data as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    s = data.split(',')
    list1=[]
    for i in s:
        list1.append(int(i))
    return list1

texts = open('txt_file/data01.txt').read()
print(main(texts))

# Read data from file