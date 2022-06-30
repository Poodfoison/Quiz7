def count_words():
    f = open('notes.txt', 'rt')
    data = f.read()
    words = data.lower().count('the')
    return f"The output should be {words}"