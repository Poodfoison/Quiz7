'''def JTOI():
    f = open('E:\python\Chapter7\quiz7A\WORD.TXT', 'w')
    f.write('WELL, THIS IS A WORD BY ITSELF. YOU COULD STRETCH THIS TO BE A SENTENCE')
    f.close()
    return f.read()
'''


f = open('E:\python\Chapter7\quiz7A\WORD.TXT', 'w')
f.write('WELL, THIS IS A WORD BY ITSELF. YOU COULD STRETCH THIS TO BE A SENTENCE')
f.close()

f = open('E:\python\Chapter7\quiz7A\WORD.TXT', 'rt')
print(f.read())
