# constants

HELP = '''Available formatters: plain bold italic header link inline-code ordered-list unordered-list new-line
Special commands: !help !done'''
FORMAT_OPTIONS = ['plain', 'bold', 'italic', 'header', 'link', 'inline-code', 'ordered-list', 'unordered-list', 'new-line']
UNKNOWN = 'Unknown formatting type or command'

# initial
run = True
output = ''

def get_text(prompt='Text:'):
    return input(prompt)

def plain(input):
    return input

def bold(input):
    return '**' + input + '**'

def italic(input):
    return '*' + input + '*'

def inline_code(input):
    return '`' + input + '`'

def link():
    return '[' + get_text('Label:') + ']' +\
            '(' + get_text('URL:') + ')'

def header(input, level):
    return ('#' * level) + ' ' + input

def new_line():
    return '\n'

def md_list(type):
    list_part = ''
    while True:
        nbr_of_rows = int(input('Number of rows:'))
        if nbr_of_rows <= 0:
            print('The number of rows should be greater than zero')
        else:
            break
    for row in range(1, nbr_of_rows + 1):
        list_part += (str(row) + '.' if type == 'order' else '*') + ' ' + get_text('Row #' + str(row) + ':') + '\n'
    return list_part


# loop
while run:
    formatter = input('Choose a formatter:')
    if formatter == '!done':
        file = open('output.md', 'w')
        file.write(output)
        file.close()
        run = False
        break
    elif formatter == '!help':
        print(HELP)
    elif formatter not in FORMAT_OPTIONS:
        print(UNKNOWN)
    elif formatter == 'plain':
        output += plain(get_text())
    elif formatter == 'bold':
        output += bold(get_text())
    elif formatter == 'italic':
        output += italic(get_text())
    elif formatter == 'inline-code':
        output += inline_code(get_text())
    elif formatter == 'link':
        output += link()
    elif formatter == 'header':
        level = int(input('Level:'))
        while level < 1 or level > 6:
            print('The level should be within the range of 1 to 6')
            level = int(input('Level:'))
        output += header(get_text(), level) + '\n'
    elif formatter == 'ordered-list':
        output += md_list('order')
    elif formatter == 'unordered-list':
        output += md_list('un_order')
    elif formatter == 'new-line':
        output += '\n'
    print(output)
