
def frequency(content):
    pattern = '[a-zA-Z]+'
    words = findall(pattern, content)
    dictionary = {}
    for w in words:
        if w in dictionary:
            dictionary[w] += 1
        else:
            dictionary[w] = 1
    return dictionary


content = 'In a land far far away called never land'

print(frequency(content))