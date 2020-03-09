
def simple_cycle(words, phrase, not_locked):
    # print(' '.join(words))
    # print(' '.join(phrase))
    ## Words with the same length
    word_matches = {word: list(set([encrypted_word for encrypted_word in phrase if len(encrypted_word) == len(word)])) for word in words if len([encrypted_word for encrypted_word in phrase if len(encrypted_word) == len(word)])}
    # print(word_matches)

    ## Remove mismatch with known values
    for word, word_match in word_matches.items():
        for single_match in word_match:
            for i, single_char in enumerate(word):
                if single_char == '-' and single_match[i] != '-':
                    word_matches[word].remove(single_match)
                    break
                if single_char != '-' and single_match[i] == '-':
                    word_matches[word].remove(single_match)
                    break

    ## Words with just one match
    # print(word_matches)
    word_learnt = {word: word_matches[word][0] for word in word_matches if len(word_matches[word]) == 1}

    # Characters that can be matched
    char_matches = {single_char: [] for single_char in [single_char for single_char in ''.join(words)] if single_char in not_locked}
    # print(char_matches)
    # Characters match
    for single_char in char_matches:
        for word in words:
            if single_char in word:
                if word in word_matches.keys():
                    for i in word_matches[word]:
                        if i[word.index(single_char)] not in char_matches[single_char] and i[word.index(single_char)] in not_locked and i != '-':
                            # print(i[word.index(single_char)])
                            char_matches[single_char].append(i[word.index(single_char)])
    # Characters that can be learnt
    # print(char_matches)
    char_learnt = {single_char: char_matches[single_char][0] for single_char in char_matches if len(char_matches[single_char]) == 1}
    # Characters with just one match
    for word in word_learnt:
        for single_char in word:
            if single_char in not_locked and word_learnt[word][word.index(single_char)] != '-':
                char_learnt[single_char] = word_learnt[word][word.index(single_char)]

    return dict(char_learnt)



alphabet = [chr(x) for x in range(ord('a'), ord('z') + 1)]
def bruteforce(words, phrase):

    locked = [0]*len(alphabet)
    not_locked = alphabet
    aux_array = ' '.join(phrase)

    while 1:

        new_array = aux_array
        new_words = ' '.join(words)

        for locked_char in [alphabet[idx] for idx,i in enumerate(locked) if i]:

            new_array = new_array.replace(locked_char, '-')
            new_words = new_words.replace(locked_char, '-')


        known_chars = simple_cycle(new_words.split(), new_array.split(), not_locked)
        # print(known_chars)
        if not known_chars:
            if not new_array.count('-') == len(new_array.replace(' ','')):
                aux_array = ''.join(['*' if elem != ' ' else elem for elem in aux_array])
            break
        for known_char, known_value in known_chars.items():
            if known_char in not_locked and known_value in not_locked and known_char != known_value:
                jump = not_locked.index(known_char) - not_locked.index(known_value) % len(not_locked)
                break

        new_array = []

        for value in aux_array:
            if value != ' ' and value in not_locked:
                if value == known_value:
                    new_array.append(known_char)
                    if not locked[ord(known_char) - 97]:
                        locked[ord(known_char) - 97] = 1
                else:
                    new_array.append(not_locked[(not_locked.index(value) + jump) % len(not_locked)])
            else:
                new_array.append(value)

        not_locked = [letter for letter,lock in zip(alphabet, locked) if not lock]

        aux_array = ''.join(new_array)
        # aux_array = ''.join([chr(((ord(word) - jump) - 97)% len(alphabet) + 97) if word != ' ' and not locked[ord(word) - 97] and word == known_value else word for word in aux_array])
        # print(f'Replacing\t\t{known_char} -> {known_value}')
        # print('\t\t\t'+''.join(alphabet))
        # print('\t\t\t'+''.join([str(i) for i in locked]))
        # print('\t\t\t'+''.join([a for i,a in zip(locked,alphabet) if i]))
        print(f'DECRIPTING ****\t\t{aux_array} \t\tReplacing\t{known_char} -> {known_value}\tLOCKING {known_char.upper()}')
        del known_char

    return aux_array

def find_uniques(problem_dict, problem_phrase):

    result = {}

    ## Word length match
    # word_matches = {word: list(set([encrypted_word for encrypted_word in phrase if len(encrypted_word) == len(word)])) for word in words if len([encrypted_word for encrypted_word in phrase if len(encrypted_word) == len(word)])}
    len_equivalent = {word: [e_word for e_word in problem_phrase if len(e_word) == len(word)] for word in problem_dict}
    # print(len_equivalent)
    ## Delete mismatches
    for word, e_words in len_equivalent.items():
        for e_word in e_words:
            if '-' in word or '-' in e_word:
                if not('-' in word and '-' in e_word) or word.count('-') != e_word.count('-'):
                    len_equivalent[word].remove(e_word)
                    break
                for a,b in zip(word, e_word):
                    if a == '-' or b == '-' and a != b:
                        len_equivalent[word].remove(e_word)
                        break
    # print(len_equivalent)
    words_learnt = {word: len_equivalent[word][0] for word in len_equivalent if len(len_equivalent[word]) == 1}
    print(words_learnt)
    for word, meaning in words_learnt.items():
        if meaning:
            for a, b in zip(word, meaning):
                if a != '-':
                    result[a] = b
    # if len(result):
    #     return result


    letter_match = {word: [] for word in list(set(''.join(problem_dict)))}
    ## Letter by letter match
    for word, e_words in len_equivalent.items():
        for e_word in e_words:
            for a, b in zip(word, e_word):
                if a != '-' and b not in letter_match[a]:
                    letter_match[a].append(b)

    print(letter_match)
    letters_learnt = {letter: letter_match[letter][0] for letter in letter_match if len(letter_match[letter]) == 1}
    print(letters_learnt)
    # for letter, l_match in letters_learnt.items():
    #     for letter_2, l_match_2 in letters_learnt.items():
    #         if l_match == l_match_2:
    #             letters_learnt[letter] = ''


    return letters_learnt

def word_breakdown(word):
    # breakdown = {letter: [index for index, let in enumerate(word) if let == letter] for letter in list(set(word))}
    breakdown = {letter: [] for letter in list(set(word))}
    for index, letter in enumerate(word):
        breakdown[letter].append(index)
    return breakdown

def try_2(problem_dict, problem_phrase):

    not_solved = True
    encrypted_phrase = problem_phrase


    word_meaning = {word: [] for word in list(set(''.join(problem_dict)))}
    dict_breakdown = {word: word_breakdown(word) for word in problem_dict}
    # print(dict_breakdown)
    letter_breakdown = {letter: {} for letter in list(set(''.join(problem_dict)))}
    for word_length, breakdown in dict_breakdown.items():
        for letter, vals in breakdown.items():
            if len(word_length) in letter_breakdown[letter].keys():
                for val in vals:
                    if val not in letter_breakdown[letter][len(word_length)]:
                        letter_breakdown[letter][len(word_length)].append(val)
            else:
                letter_breakdown[letter][len(word_length)] = vals
    print(letter_breakdown)

    word_e_meaning = {word: [] for word in list(set(''.join(problem_phrase)))}
    dict_breakdown = {word: word_breakdown(word) for word in problem_phrase}
    e_letter_breakdown = {letter: {} for letter in list(set(''.join(problem_phrase)))}
    for word_length, breakdown in dict_breakdown.items():
        for letter, vals in breakdown.items():
            if len(word_length) in e_letter_breakdown[letter].keys():
                for val in vals:
                    if val not in eletter_breakdown[letter][len(word_length)]:
                        e_letter_breakdown[letter][len(word_length)].append(val)
            else:
                e_letter_breakdown[letter][len(word_length)] = vals

    print()
    print(e_letter_breakdown)






    len_equivalent = {word: [e_word for e_word in problem_phrase if len(e_word) == len(word)] for word in problem_dict}
    phrase_breakdown = {len(word): word_breakdown(word) for word in problem_phrase}



    # print(dict_breakdown)
    # print(phrase_breakdown)

    # if len(word_meaning) != len(word_e_meaning):
    #     return False

    while not_solved:

        pass


if __name__ == '__main__':

    print('hi')
    problem_words = []
    problem_phrases = []
    word_count = int(input())

    for _ in range(word_count):
        try: line = input()
        except: line = ''
        if not(line == ''): problem_words.append(line.strip())
    while line:
        try: line = input()
        except: line = ''
        if not(line == ''):
            problem_phrases.append(line.strip().split())


    # try:
    print(f'\n\nWITH THE DICTIONARY\t{" ".join(problem_words)}\n\t   ______________________________')
    for phrase in problem_phrases:
        print(f'\nTRYING TO DECRYPT\t{" ".join(phrase)}')
        test = try_2(problem_words,phrase)

        print(f'\nDECRIPTION\t\t{test}\n\t   ______________________________')
        # print(f'{test}')
        # print(bruteforce(problem_words, phrase))
        # solve_problem(problem_words, phrase)
    # except: pass
