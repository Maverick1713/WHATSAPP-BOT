from collections import defaultdict
h = defaultdict(list)

def log(number , data):
    h[number].append(data)
    print(h)
