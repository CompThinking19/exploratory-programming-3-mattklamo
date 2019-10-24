import re
source = open('1661-0.txt')
sherlock = source.read()
def find_at(book):
    if type(book) != str:
        raise TypeError("Wrong type")
    result = re.findall('\w*at\\b', book)
    words = []
    for element in result:
        if len(element) > 3:
            words.append(element)
    return words
find_at(sherlock)
