
# def backtrack(road):
#     for road_begining, road_options in road.items():
#
#     print(road)
#     return True
#     return True
#     pass




def simple_cycle(words, phrase, not_locked):
    # print(words)
    # print(phrase)
    word_matches = {word: list(set([encrypted_word for encrypted_word in phrase if len(encrypted_word) == len(word)])) for word in words if len([encrypted_word for encrypted_word in phrase if len(encrypted_word) == len(word)])}
    word_learnt = {word: word_matches[word][0] for word in word_matches if len(word_matches[word]) == 1}
    # print(word_matches)
    for word, word_match in word_matches.items():
        for single_match in word_match:
            for i, single_char in enumerate(word):
                if single_char == '-' and single_match[i] != '-':
                    word_matches[word].remove(single_match)
                    break
                if single_char != '-' and single_match[i] == '-':
                    word_matches[word].remove(single_match)
                    break


    # print(word_learnt)
    char_matches = {single_char: [] for single_char in [single_char for single_char in ''.join(words)] if single_char in not_locked}
    for single_char in char_matches:
        for word in words:
            if single_char in word:
                if word in word_matches.keys():
                    for i in word_matches[word]:
                        if i[word.index(single_char)] not in char_matches[single_char] and i[word.index(single_char)] in not_locked:
                            # print(i[word.index(single_char)])
                            char_matches[single_char].append(i[word.index(single_char)])
    char_learnt = {single_char: char_matches[single_char][0] for single_char in char_matches if len(char_matches[single_char]) == 1}
    for word in word_learnt:
        for single_char in word:
            if single_char in not_locked:
                char_learnt[single_char] = word_learnt[word][word.index(single_char)]
    # for word in word_learnt\
    # print(char_matches)
    # print(char_learnt)
    return dict(char_learnt)
    # if char_learnt:
    # else:
    #     for elem_name, elem_vals in word_matches.items():
    #         if len(elem_vals) > 1:
    #             for val in elem_vals:
    #                 path = solve_backtrack(char_matches)
    #                 if path:
    #                     return path



alphabet = [chr(x) for x in range(ord('a'), ord('z') + 1)]
def bruteforce(words, phrase):

    not_decrypted = True
    locked = [0]*len(alphabet)
    not_locked = alphabet
    aux_array = ' '.join(phrase)

    # iteration = -1

    while not_decrypted: # 0 in locked
        # iteration += 1
        new_array = aux_array
        new_words = ' '.join(words)
        # print(new_array)
        # print(new_words)
        # print([alphabet[idx] for idx,i in enumerate(locked) if i])
        for locked_char in [alphabet[idx] for idx,i in enumerate(locked) if i]:

            new_array = new_array.replace(locked_char, '-')
            new_words = new_words.replace(locked_char, '-')


        known_chars = simple_cycle(new_words.split(), new_array.split(), not_locked)
        # print(known_chars)
        # rotate = True
        # print(known_chars)
        for known_char, known_value in known_chars.items():
            if known_char in not_locked and known_value in not_locked and known_char != known_value:
                jump = not_locked.index(known_char) - not_locked.index(known_value) % len(not_locked) #         (ord(known_char) - ord(known_value)) % len(alphabet)
                # rotate = False
                break

        # if rotate:
        #     break

        new_array = []

        for value in aux_array:
            if value != ' ' and value in not_locked:
                if value == known_value:
                    new_array.append(known_char)
                    if not locked[ord(known_char) - 97]:
                        # print('\tLOCKING (%s)' %known_char)
                        locked[ord(known_char) - 97] = 1
                else:
                    new_array.append(not_locked[(not_locked.index(value) + jump) % len(not_locked)]) # ((ord(value) - 97 + jump)) % len(not_locked)])

            else:
                new_array.append(value)

        not_locked = [letter for letter,lock in zip(alphabet, locked) if not lock]


        aux_array = ''.join(new_array)
        # aux_array = ''.join([chr(((ord(word) - jump) - 97)% len(alphabet) + 97) if word != ' ' and not locked[ord(word) - 97] and word == known_value else word for word in aux_array])
        # print(f'Replacing\t\t{known_char} -> {known_value}')
        # print('\t\t\t'+''.join(alphabet))
        # print('\t\t\t'+''.join([str(i) for i in locked]))
        # print('\t\t\t'+''.join([a for i,a in zip(locked,alphabet) if i]))
        print(f'DECRIPTING ****\t\t{aux_array}')
        del known_char


    # input()

    return aux_array


if __name__ == '__main__':

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
    print(f'\n\nWITH THE DICTIONARY\t{" ".join(problem_words)}')
    for phrase in problem_phrases:
        print(f'TRYING TO DECRYPT\t{" ".join(phrase)}')
        test = bruteforce(problem_words,phrase)
        if test:
            print(f'\nDECRIPTION\t\t{test}')
        else:
            print(f'\nDECRIPTION [OK]\t\t{test}')
        input()

        # print(bruteforce(problem_words, phrase))
        # solve_problem(problem_words, phrase)
    # except: pass
