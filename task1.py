#Program reads the text from the file article.txt
#calculate total word count
#calculate total character count
#calculate average word count
#calculate average sentence length
#show the word distribution of all words ending in 'ly'
#list top 10 longest words
#write to summary file

import os
import re

FILENAME1 = 'article.txt'
FILENAME2 = 'summary.txt'
MODE_W = 'w'
MODE_R = 'r'

def removeSpecialChars(p_word):
    """ regular expression operator will retain 'a-z''A-Z''0-9' """
    regex = re.compile('[^a-zA-Z0-9]')
    return regex.sub('', p_word)

def getLetters(p_word):
    """ regular expression operator will retain 'a-z''A-Z' """
    regex = re.compile('[^a-zA-Z]')
    return regex.sub('', p_word)

def get_word_count(p_content):
    """ get total words in the article """
    #check for special characters, filter and get the word count
    new_word_list = []
    total_words = p_content.split()
    
    for word in total_words:
        new_word = removeSpecialChars(word)
        if new_word.isalnum():
            new_word_list.append(new_word)
    return len(new_word_list)

def get_char_count(p_content):
    """ get character count """
    #check for characters in 'a-z' or 'A-Z', get characters count
    total_chars = p_content.split()
    charLength = 0
    for char in total_chars:
        charLength += len(getLetters(char))
    return charLength

def get_word_length(p_content):
    #get length of each word, remove special character
    w_len = 0
    total_words = p_content.split()
    for word in total_words:
        w_len += len(removeSpecialChars(word))
    return w_len

def get_sen_len(p_content):
    #split the sentence having '.:', get the length
    sentence_list = []
    sentence_list = p_content.split('.:')
    return len(sentence_list)

def write_to_file(p_record,p_end_words,p_long_words):
    with open(FILENAME2,MODE_W) as file_summary:
        #write word count
        file_summary.write(f'Total word count:{p_record[0]}')

        #write character count
        file_summary.write(f'\nTotal character count:{p_record[1]}')

        #write avg word count = total word_len/total words
        avg_word_len = p_record[3]/p_record[0]
        file_summary.write(f'\nThe average word length: {avg_word_len:.2f}')

        #write avg sentence length = total words/total sentences
        avg_sen_len = p_record[0]/p_record[2]
        file_summary.write(f'\nThe average sentence length: {avg_sen_len:.2f}\n')

        #write the word distribution of words ending with 'ly'
        file_summary.write(f'\nThe word distribution of all words ending in "ly"')
        for word , num in sorted(p_end_words.items()):
            file_summary.write(f'\n{word} :{num}')

        #list top 10 longest words
        file_summary.write(f'\nThe list of top 10 longest words in descending order:\n')
        for text in p_long_words:
                file_summary.write(f'{text},')


def main():
    ending_words = {}
    long_words = []
    word_count = 0
    char_count = 0
    sentence_count = 0
    word_len = 0
    sorted_list = []
    #read from article.txt file
    with open(FILENAME1,MODE_R) as file_article:
        for line in file_article:
            text_content = line.rstrip('\n')
            word_count += get_word_count(text_content)
            word_len += get_word_length(text_content)
            char_count += get_char_count(text_content)
            sentence_count += get_sen_len(text_content)
            
            words_list = text_content.split()  

            for word in words_list:
                #show the word distribution of all words ending in 'ly'
                filteredWord = getLetters(word).lower()
                if filteredWord.endswith('ly'):
                    ending_words[filteredWord] = ending_words.get(filteredWord,0) + 1
                #get top 10 longest words
                long_words.append(getLetters(word).lower())
        
        sorted_list = list(set(long_words))    
        sorted_list.sort(key = len, reverse=True)
        # write to summary file
        record = (word_count,char_count,sentence_count,word_len)
        write_to_file(record,ending_words,sorted_list[:10])
            
#main
if os.path.isfile(FILENAME1):
    main()
else:
    print(f'{FILENAME1} is not found in your directory')
