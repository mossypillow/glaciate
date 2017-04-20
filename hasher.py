import hashlib

def hashing(file):
    largefile = file
    BLOCKSIZE = 65536
    hashing = hashlib.md5()
    with open(largefile, 'rb') as afile:
        buf = afile.read(BLOCKSIZE)
        while len(buf) > 0:
            hashing.update(buf)
            buf = afile.read(BLOCKSIZE)
    return hashing.hexdigest()
