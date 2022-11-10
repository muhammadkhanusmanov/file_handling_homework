def main(data:str):
    """
    The data is from the file. Find the number of digital and str(non-digital) data and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    i=0
    for a in data:
        if a.isdigit():
            i+=1
    return [i,len(data)-i]
    
# Read data from file
f = open('txt_file/data05.txt').read()
