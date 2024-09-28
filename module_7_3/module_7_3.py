import io

from pprint import pprint

class Worrds_finder:
    def __init__(self, *file_names) -> None:
        self.file_names = file_names
    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                words = []
                for line in file:
                    line = line.lower()
                    char = [',', '.', '=', '!', '?', ';', ':']
                    for i in char:
                        line = line.replace(i, '')
                    line = line.replace(' - ', '')
                    words.extend(line.split)
                    
                all_words[file_name] = words
        return all_words
    def find(self, word):
        counters = {}
        for value, key in self.get_all_words().items():
            words_count = key.count(word.lower())
            counters[value] = words_count
        return counters
inder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt')
print(finder1.get_all_words())
print(finder1.find('captain'))
print(finder1.count('captain'))