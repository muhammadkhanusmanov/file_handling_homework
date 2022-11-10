def main(data:str):
    """
    The data is from the file. Find the each row length and return the largest row.
    Args:
        data: str
    Returns:
        int: return answer
    """
    a=data.split('\n')
    b=0
    for i in a:
        if b<len(i):
            b=len(i)
    return b

# Read data from file
f=open('txt_file/data10.txt').read()