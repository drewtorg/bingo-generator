import pystache

lines = open('input.txt', 'r').readlines()
lines = map(str.strip, lines)
template = open('bingo.mustache', 'r').read().replace('\n', '')

data = { 'rows': [] }
count = 0
for i in range(5):
    tiles = { 'tiles': [] }
    for j in range(5):
        line = lines[count]
        is_image = False
        extensions = ['jpg', 'jpeg', 'png']
        for extension in extensions:
            if extension in line:
                is_image = True
                break
        if is_image:
            tiles['tiles'].append({ 'path': line, 'text': None })
        else:
            tiles['tiles'].append({ 'path': None, 'text': line })
            
        count += 1
    data['rows'].append(tiles)

output = open('output.html', 'w')
output.write(pystache.render(template, data))
