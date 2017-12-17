import pystache
from random import shuffle

lines = open('input.txt', 'r').readlines()
lines = map(str.strip, lines)
template = open('bingo.mustache', 'r').read().replace('\n', '')

data = { 'boards': [] }
for i in range(2):
    count = 0
    shuffle(lines)
    board = { 'rows': [] }
    for j in range(4):
        row = { 'tiles': [] }
        for k in range(4):
            line = lines[count]
            is_image = False
            extensions = ['jpg', 'jpeg', 'png']
            for extension in extensions:
                if extension in line:
                    is_image = True
                    break
            if is_image:
                row['tiles'].append({ 'path': line, 'text': None })
            else:
                row['tiles'].append({ 'path': None, 'text': line })
                
            count += 1
        board['rows'].append(row)
    data['boards'].append(board)

print pystache.render(template, data)
