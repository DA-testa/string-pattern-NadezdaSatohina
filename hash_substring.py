# python3

def hash(s, sz):
    h = 0
    for i in range(0, sz):
        h <<= 8
        h += ord(s[i])
       
    return h

def search(s, sz, nh):
    hh = hash(s, sz)
    mask = 0x100 ** (sz - 1) - 1
    for i in range(0, len(s)):
        if nh == hh:
            yield i

        hh &= mask
        hh <<= 8
       
        if i + sz < len(s):
            hh += ord(s[i + sz])

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    return list(search(text, len(pattern), hash(pattern, len(pattern))))

# this part launches the functions
if __name__ == '__main__':
    input_type = input("")
    if "F" in input_type:
        filename = input("")

        if "test/" not in filename:
            filename = "test/" + filename
        if "test/" in filename:    
            with open(filename) as f:
                pattern = f.readline().strip()
                text = f.readline().strip()
    elif "I" in input_type:
        pattern = input("").strip()
        text = input("").strip()

    print_occurrences(get_occurrences(pattern, text))

