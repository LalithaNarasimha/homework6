# Constants declaration
FILENAME = 'book.txt'
FILENAME2 = 'summary.txt'
MODE_R = 'r'
MODE_W = 'w'

# defining Functions
def get_letter_frequency():
    """Read the 'txt' file and get the letters and their frequency"""
    #local Variables
    alphabet_list = {}
    read_letters = []

    try:
        with open(FILENAME,MODE_R) as names_file:
            for line in names_file:
                read_letters = list(line)
                for letter in read_letters: 
                    if letter.isalpha():
                        letter = letter.upper()
                        if letter in alphabet_list:
                            alphabet_list[letter] += 1
                        else:
                            alphabet_list[letter] = 1
            return alphabet_list
    except IOError as error:
        print(f'I/O error:: {error}')

def create_write_file(alphabet_list):
    """Create and write the number of letters to the file"""
    try:
        with open(FILENAME2,MODE_W) as names_file2:
            for word in sorted(alphabet_list):
                names_file2.write(f'{word} {alphabet_list[word]}\n')     

            if len(alphabet_list) == 26:
                names_file2.write('It has all letters')
            else:
                names_file2.write("It doesn't have all letters")
    except IOError as error:
        print(f'I/O error:: {error}')
        names_file2.write(f'I/O error:: {error}')
    
#main program      
dictionary_list = get_letter_frequency()
create_write_file(dictionary_list)
