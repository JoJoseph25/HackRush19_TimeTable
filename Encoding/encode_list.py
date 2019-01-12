import math
def _get_bits(n,s,st):
    if len(s)==n:
        st.append(s)
    else:
        _get_bits(n,s+"0",st)
        _get_bits(n,s+"1",st)

def getbits(n):
    stck = []
    _get_bits(n,"",stck)
    return stck

# given ["a", "b", "c"] it should give {"a":"00", "b":"01", "c":"10"}
def encoder(alist):
    length = len(alist)
    n_bits = math.ceil(math.log2(length))
    encodings = getbits(n_bits)
    ret = {item:enc for item, enc in zip(alist,encodings)}
    return ret

