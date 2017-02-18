"""This is the entry point of the program."""


def create_box(height, width, character):
    y = 0
    box = ''
    if (width <1) or (height<1):
        print ('Error, height and width must be >= 1')
    while y < height:
        box = (character * width)
        y +=1 
    return (box + '\n')* height

def extra_space_box(height, width, character):
    y=0
    top_bottom = '' 
    space_blanks = ''
    if (width<1) or (height<1):
        return 'Error, height and width must be >=1'
    while y < height:
        top_bottom = character*width
        y +=1
        space_blanks = (character + ' '*(width-2) + character)
    print (top_bottom + '\n' + (space_blanks + '\n')*(height-2) +  top_bottom + '\n')
    return (top_bottom + '\n' + (space_blanks + '\n')*(height-2) + top_bottom + '\n')
        
    

if __name__ == '__main__':
    create_box(4, 4, '*')