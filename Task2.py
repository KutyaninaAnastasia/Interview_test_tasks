import wikipediaapi
import re

wiki_wiki = wikipediaapi.Wikipedia('ru')


def get_category_members(category_members):
    lst = []
    for c in category_members.values():
        if re.search(r'[A-z\:]', c.title):
            continue
        lst.append(c.title)
    return lst


def count_animals(lst):
    char_dict = {}
    for word in lst:
        first_char = word[0]
        if first_char in char_dict:
            char_dict[first_char] += 1
        else:
            char_dict[first_char] = 1
    return char_dict


cat = wiki_wiki.page("Категория:Животные по алфавиту")
animals = get_category_members(cat.categorymembers)
letters = count_animals(animals)
for letter in letters:
    print(f'{letter}:{letters[letter]}')
