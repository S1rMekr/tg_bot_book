import os
import sys

BOOK_PATH = 'book/book.txt'
PAGE_SIZE = 1050

book: dict[int, str] = {}


def _get_part_text(text:str, start: int, size: int) -> tuple[str, int]:
    znaki = [',', '.', '!', ':', ';', '?']
    number = 0
    if text[::-1] in znaki:
        size-=2
    code = text[start:size+start]
    code_r = text[start:size+start][::-1]
    for i in code_r:
        number+=1
        if i in znaki:
            number-=1
            break
    return (code[:-number], len(code[:-number])) if number>=1 else (code, len(code))


def prepare_book(path: str) -> None:
    with open(path, 'r', encoding='utf-8') as f:
        text = ''.join(f.readlines())
    start = 0
    index = 1
    while len(text) > 0:
        part_text = _get_part_text(text, start, PAGE_SIZE)[0].lstrip('\n ').rstrip('\n')
        size = _get_part_text(text, start, PAGE_SIZE)[1]
        text = text[size+1:]
        book[index] = part_text
        index+=1
        
    


prepare_book(os.path.join(sys.path[0], os.path.normpath(BOOK_PATH)))
