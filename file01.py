def main(data:str):
    """
    The data is from the file. Return data as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    
    f = open('data01.txt')
    s=f.read().split(',')
    return s 


# Read data from file