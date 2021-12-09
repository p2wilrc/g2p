import csv
import re

SPECIAL_SYMBOLS = ['VOWEL', 'STOP', '\\s', '$', '^']

CHARACTER_SET = re.compile(r'\[([a-z]*?)\]|(?<!\\)([a-z])')

def capitalize(match):

    if match.group(1):
        full_charset = []
        for char in match.group(1):
            full_charset.append(char)
            full_charset.append(char.upper())
        return "[%s]" % ''.join(full_charset)
    elif match.group(2):
        char = match.group(2)
        char_cap = char.upper()
        return "[%s%s]" % (char, char_cap)
    else:
        raise NotImplementedError("Unexpected match failure")

def permute(regex):

    new_regex = CHARACTER_SET.sub(capitalize, regex)

    return new_regex

def main():

    filenames = ['crg-tmd-to-dv.csv', 'crg-tmd-to-dv-morphs.csv',
        'crg-tmd-to-dv-words.csv']

    for filename in filenames:
        with open(filename, 'r', newline='') as infile:
            reader = csv.reader(infile)
            with open(filename + '.new', 'w', newline='') as outfile:
                writer = csv.writer(outfile)
                for row in reader:
                    if len(row) == 0:
                        continue
                    writer.writerow([
                        row[0].lower(),
                        row[1].upper(),
                        permute(row[2]) if len(row) >= 3 else '',
                        permute(row[3]) if len(row) >= 4 else '',
                    ])

if __name__ == "__main__":

    main()
