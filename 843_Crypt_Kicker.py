
def simple_cycle(words, phrase):
    word_matches = {word: list(set([encrypted_word for encrypted_word in phrase if len(encrypted_word) == len(word)])) for word in words if len([encrypted_word for encrypted_word in phrase if len(encrypted_word) == len(word)])}
    word_learnt = {word: word_matches[word][0] for word in word_matches if len(word_matches[word]) == 1}
    char_matches = {single_char: [] for single_char in ''.join(words)}
    for letter in char_matches:
        for word in words:
            if letter in word:
                if word in word_matches.keys():
                    for i in word_matches[word]:
                        if i[word.index(letter)] not in char_matches[letter]:
                            char_matches[letter].append(i[word.index(letter)])
    char_learnt = {letter: char_matches[letter][0] for letter in char_matches if len(char_matches[letter]) == 1}
    for word in word_learnt:
        for letter in word:
            char_learnt[letter] = word_learnt[word][word.index(letter)]
    return char_learnt



alphabet = [chr(x) for x in range(ord('a'), ord('z') + 1)]
def bruteforce(words, phrase):

    not_decrypted = True
    locked = [0]*len(alphabet)
    not_locked = alphabet
    aux_array = ' '.join(phrase)

    # iteration = -1

    while len(not_locked): # 0 in locked
        # iteration += 1
        known_chars = simple_cycle(words, aux_array.split())
        # rotate = True
        for known_char, known_value in known_chars.items():
            if known_char in not_locked and known_value in not_locked and known_char != known_value:
                jump = not_locked.index(known_char) - not_locked.index(known_value) % len(not_locked) #         (ord(known_char) - ord(known_value)) % len(alphabet)
                # rotate = False
                break

        # if rotate:
        #     break

        new_array = []
        locked[ord(known_char) - 97] = 1

        for value in aux_array:
            if value != ' ' and value in not_locked:
                if value == known_value:
                    new_array.append(known_char)
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
