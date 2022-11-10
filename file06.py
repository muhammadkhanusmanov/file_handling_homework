def main(data:str):
    """
    The data is from the file. Find the each row length and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    lenlist=[]
    a=data.split('\n')
    for i in a:
        lenlist.append(len(i))
    return lenlist
    
# Read data from file
f = open('txt_file/data06.txt').read()
