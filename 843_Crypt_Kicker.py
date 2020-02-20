
def solve_problem(words, phrase):
    matches = {word: list(set([encrypted_word for encrypted_word in phrase if len(encrypted_word) == len(word)])) for word in words}

    meanings = {letter: [] for letter in ''.join(words)}

    for letter in meanings.keys():
        for word in words:
            if letter in word:
                for i in matches[word]:
                    if i[word.index(letter)] not in meanings[letter]:
                        meanings[letter].append(i[word.index(letter)])


    not_solved = True
    known_values = {}
    while not_solved:
        print(f'WHILE \n{meanings}\n__________________________')
        if not(False in [len(val) == 1 for val in meanings.values()]):
            print(f'_____________MAIN_____________\n{meanings}\n_____________MAIN_____________') ## STEP 1
            not_solved = True
        for key in meanings:
            val = meanings[key]
            if len(val) == 1:
                print(f'{key} {val}')
                val = val[0]
                meanings[key] = val
                known_values[key] = val
                for key_2 in meanings:
                    if key_2 != key:
                        val_2 = meanings[key_2]
                        print(f'               {key_2} {val_2}')
                        if val in val_2:
                            meanings[key_2].remove(val)
                        if len(meanings[key_2]) == 0: ## failed decrypt
                            return ' '.join(['*'*len(word) for word in phrase])
        print(f'\nST2\n{matches}\n___________________________________________\n{meanings}\n___________________________________________\n{known_values}\n') ## STEP 2
        for val in list(known_values):
            for key in list(matches):
                if val in key:
                    print(f'DEBUG {key} {matches[key]}')
                    if len(matches[key]) == 1:
                        for elem, val_e in zip(key, matches[key][0]):
                            print(f'DEBUG 2 {elem} {val_e}')
                            meanings[elem] = val_e
                            known_values[elem] = val_e
                            for elem_2 in meanings:
                                if elem_2 != elem:
                                    val_2 = meanings[elem_2]
                                    print(f'               {elem_2} {val_2}')
                                    if val_e in val_2:
                                        meanings[elem_2].remove(val_e)
                                    if len(meanings[elem_2]) == 0: ## failed decrypt
                                        return ' '.join(['*'*len(word) for word in phrase])
                        matches.pop(key)
        print(f'\nST3\n{matches}\n___________________________________________\n{meanings}\n___________________________________________\n{known_values}\n') ## STEP 2
        for key in list(matches):
            if len(matches[key]) == 1:
                print(f'DEBUG 2 {key} {matches[key]}')
                for elem, val_e in zip(key, matches[key][0]):
                    meanings[elem] = val_e
                    known_values[elem] = val_e
                    for elem_2 in meanings:
                        if elem_2 != elem:
                            val_2 = meanings[elem_2]
                            print(f'               {elem_2} {val_2}')
                            if val_e in val_2:
                                meanings[elem_2].remove(val_e)
                            if len(meanings[elem_2]) == 0: ## failed decrypt
                                return ' '.join(['*'*len(word) for word in phrase])
                matches.pop(key)
        print(f'\nST4\n{matches}\n___________________________________________\n{meanings}\n___________________________________________\n{known_values}\n') ## STEP 2
        print([item for sublist in matches.values() for item in sublist])
        ## RESOLVER PARA TODAS LA POSIBLES COMBINACIONES n*n
        if len(list(set([item for sublist in matches.values() for item in sublist]))) == len(matches.keys()):
            print('hello')
        input()
    return ' '.join([' '.join(phrase).replace(key, meaning) for key, meaning in meanings.items()])


def bruteforce(words, phrase):

    # print(phrase)

    error = ' '.join(['*'*len(word) for word in phrase])

    ## matches contains {word: Encrypted words with same length}
    matches = {word: list(set([encrypted_word for encrypted_word in phrase if len(encrypted_word) == len(word)])) for word in words}
    meanings = {letter: [] for letter in ''.join(words)}


    for letter in meanings.keys():
        for word in words:
            if letter in word:
                for i in matches[word]:
                    if i[word.index(letter)] not in meanings[letter]:
                        meanings[letter].append(i[word.index(letter)])

    known_values = {value: meanings[value][0] for value in meanings if len(meanings[value]) == 1}
    print(known_values)
    for key in meanings:
        val = meanings[key]
        if len(val) == 1:
            val = val[0]
            meanings[key] = val
            known_values[key] = val
            for key_2 in meanings:
                if key_2 != key:
                    val_2 = meanings[key_2]
                    if val in val_2:
                        meanings[key_2].remove(val)
                    if len(meanings[key_2]) == 0: ## failed decrypt
                        return ' '.join(['*'*len(word) for word in phrase])
    # print(f'\nST2\n{matches}\n___________________________________________\n{meanings}\n___________________________________________\n{known_values}\n') ## STEP 2
    for val in list(known_values):
        for key in list(matches):
            if val in key:
                if len(matches[key]) == 1:
                    for elem, val_e in zip(key, matches[key][0]):
                        meanings[elem] = val_e
                        known_values[elem] = val_e
                        for elem_2 in meanings:
                            if elem_2 != elem:
                                val_2 = meanings[elem_2]
                                print(val_2)
                                print(type(val_2))
                                if val_e in val_2:
                                    meanings[elem_2].remove(val_e)
                                if len(meanings[elem_2]) == 0: ## failed decrypt
                                    return ' '.join(['*'*len(word) for word in phrase])
                    matches.pop(key)
    for key in list(matches):
        if len(matches[key]) == 1:
            for elem, val_e in zip(key, matches[key][0]):
                meanings[elem] = val_e
                known_values[elem] = val_e
                for elem_2 in meanings:
                    if elem_2 != elem:
                        val_2 = meanings[elem_2]
                        if val_e in val_2:
                            meanings[elem_2].remove(val_e)
                        if len(meanings[elem_2]) == 0: ## failed decrypt
                            return ' '.join(['*'*len(word) for word in phrase])
            matches.pop(key)



    not_decrypted = {elem: values for elem, values in meanings.items() if len(values) > 1}


    return [matches, meanings, known_values, not_decrypted]

class encryption_dict:

    def __init__(self, word_dictionary, encrypted_message):
        self.encrypted = True
        self.word_dictionary = word_dictionary
        self.encrypted_message = encrypted_message
        force_message = bruteforce(self.word_dictionary, self.encrypted_message)
        if '*' in force_message:
            self.encrypted = False
            self.encrypted_message = force_message
        self.known_values = force_message[2]
        print(force_message[-1])
        print(force_message[-2])
        if len(force_message[-1]) == 1:
            self.encrypted = False


    def get_decrypted(self):
        if '*' in self.encrypted_message:
            return self.encrypted_message
        temp_message = ' '.join(self.encrypted_message)
        for encrypt,decrypt in self.known_values.items():
            temp_message = temp_message.replace(decrypt, encrypt)
        return(temp_message)


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
def hard_decrypt(words, phrase):
    # unkown_alphabet = [chr(x) for x in range(ord('a'), ord('z') + 1)]
    spc = 32
    not_decrypted = True
    locked = [0]*len(alphabet)
    aux_array = ' '.join(phrase)

    # while locked.count(1) < len(list(set([word for word in ''.join(phrase)]))):
    # print(known_chars)
    # for known_char, known_value in known_chars.items():
    #     if known_char == known_value:
    #         locked[ord(known_char) - 97] = 1
    #         print(f'LOCKED {known_char}')
    #         unkown_alphabet.remove(known_char)
    iteration = -1
    # for known_char, known_value in known_chars.items():
    while iteration < 50: # 0 in locked
        iteration += 1
        known_chars = simple_cycle(words, aux_array.split())
        for known_char, known_value in known_chars.items():
            if not locked[ord(known_char) - 97]:
                jump = (ord(known_char) - ord(known_value)) % len(alphabet)
                break
        # known_char = list(known_chars.keys())[iteration%len(known_chars)]
        # known_value = list(known_chars.values())[iteration%len(known_chars)]
        # print(f'\nITERATION {iteration}:\t\t{known_chars}')
        # print(f'\nLOCKING\t\t{known_char} == {known_value}')
        # jump = (ord(known_char) - ord(known_value)) % len(alphabet)
        # print(f'\nLOCKING\t\t{known_char} == {known_value} : {jump}')

        # aux_array = ''.join([chr((ord(word) + jump) % len(alphabet) + 97) if word != ' ' and not locked[ord(word) - 97] else word for word in aux_array])
        new_array = []
        not_locked = [letter for letter,lock in zip(alphabet, locked) if not lock]

        # print(not_locked)

        # abcdefghijklmnopqrstuvwxyz
        for value in aux_array:
            # print(value)
            # print('--\t' + ''.join(new_array))
            if value != ' ' and value in not_locked:
                if value == known_value:
                    new_array.append(known_char)
                else:
                    # print(value)
                    # if value in known_chars.values():
                        # if value != known_chars[list(known_chars.keys())[list(known_chars.values()).index(value)]]:
                        # print()
                        # print(f'{value} -> {not_locked[(ord(value) - 97 + jump) % len(not_locked)]}')
                        # print(known_chars)
                        # print(list(known_chars.values()))
                        # print(list(known_chars.values()).index(value))
                        # print(list(known_chars.keys())[list(known_chars.values()).index(value)])
                        # known_chars[list(known_chars.keys())[list(known_chars.values()).index(value)]] = not_locked[(ord(value) - 97 + jump) % len(not_locked)]
                        # print(known_chars)
                        # print()
                        # mydict.keys()[mydict.values().index(16)]

                    # print(f'2 {value} for {not_locked[(ord(value) + jump) % len(not_locked)]}')
                    new_array.append(not_locked[(ord(value) - 97 + jump) % len(not_locked)])

            else:
                new_array.append(value)


        # input()

        aux_array = ''.join(new_array)
        # aux_array = ''.join([chr(((ord(word) - jump) - 97)% len(alphabet) + 97) if word != ' ' and not locked[ord(word) - 97] and word == known_value else word for word in aux_array])

        # for chars in known_chars:
        #     if chars != known_char:
        #         known_chars[chars] = ''

        locked[ord(known_char) - 97] = 1
        # print('\t\t\t'+''.join(alphabet))
        # print('\t\t\t'+''.join([str(i) for i in locked]))
        # print('\t\t\t'+''.join(alphabet))
        print(f'DECRIPTING ****\t\t{aux_array}')
        # chr((ord('t')-97+0)%26+97)

    input()


    while locked.count(1) < len(list(set([word for word in ''.join(words)]))):
        good_chars = simple_cycle(words, aux_array.split())
        print(f'TRYING TO LOCK\t\t{good_chars}')
        for chara in good_chars:
            jump = min((ord(chara)-ord(good_chars[chara])) % 26, (ord(chara)+ord(good_chars[chara])) % 26)
            print(f'{chara} > {good_chars[chara]} : {jump}')
            if not locked[ord(chara) - 97] and jump:
                for letter in aux_array:
                    letter = ''.join([chr(((ord(word) - 97 + jump) % 26) + 97) if not locked[ord(word) - 97] and not locked[(ord(word) + jump - 97) % 26] else chr((ord(word) + jump) % 26 + 97) for word in aux_array])
                for chars in good_chars:
                    if chars != chara:
                        good_chars[chars] = chr(((ord(good_chars[chars]) - 97 + jump)%26) + 97)
                print(f'{locked} \t\t{aux_array}')
                locked[ord(chara) - 97] = 1
                print(f'LOCKING {chara}={good_chars[chara]}\t\t{aux_array}')
                print(locked)

            #     # aux_array = ''.join([chr(((ord(word) + ord(chara) - ord(good_chars[chara])) % len(alphabet)) + 97) if ord(word) != spc and not locked[ord(word)-97] else word for word in ' '.join(phrase)])
            #     for letter in aux_array:
            #         if not locked[ord(letter) - 97]:
            #             aux_array = aux_array.replace(letter, chr(((ord(letter) + ord(chara) - ord(good_chars[chara])) % len(alphabet)) + 97))
            #         else:
            #             pass
        # for i in range(len(alphabet)):
        #     aux_array = ''.join([chr(((ord(word)+i) % len(alphabet)) + 97) if ord(word) != spc and not locked[ord(word)-97] else word for word in ' '.join(phrase)])
        #     for word in aux_array.split():
        #         for letter in word:
        #             if letter in good_chars and not locked[ord(letter) - 97]:
        #                 for g_word in words:
        #                     if letter in g_word and len(g_word) == len(word) and word.index(letter) == g_word.index(letter):
        #                         locked[ord(letter) - 97] = 1
        #                         print(f'LOCKING {letter}\t\t{aux_array}')
        # print(f'{locked}')
        # print(f'{aux_array}')
        # # input()
        # depth = 50
        # locked = [0]*26
        # while locked.count(1) < len(list(set([word for word in ''.join(words)]))) and depth:
        #     for i in range(iteration, len(alphabet) + iteration):
        #         aux_array = ''.join([chr(((ord(word)+i) % len(alphabet)) + 97) if ord(word) != spc and not locked[ord(word)-97] else word for word in ' '.join(phrase)])
        #         for word in aux_array.split()[-iteration:]+aux_array.split()[:-iteration]:
        #             for letter in word[:-iteration]+word[-iteration:]:
        #                 if not locked[ord(letter) - 97]:
        #                     for g_word in words:
        #                         if letter in g_word and len(g_word) == len(word) and word.index(letter) == g_word.index(letter):
        #
        #                             # if locked[ord(letter) - 97] == 1 error?
        #                             locked[ord(letter) - 97] = 1
        #                             print(f'LOCKING {letter}\t\t{aux_array}')
        #                             depth += 5
        #         print(f'\t\t{iteration}\t{aux_array}')
        #         # input()
        #
        #     depth -= 1
        # iteration += 1


    return True


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
            # problem_phrases = problem_phrases + [(word) for word in line.strip().split()]

    # try:
    print(f'\n\nWITH THE DICTIONARY\t{" ".join(problem_words)}')
    for phrase in problem_phrases:
        print(f'TRYING TO DECRYPT\t{" ".join(phrase)}')
        test = hard_decrypt(problem_words,phrase)
        if test:
            print(f'\nDECRIPTION\t\t{test}')
        else:
            print(f'\nDECRIPTION [OK]\t\t{test}')
        input()

        # print(bruteforce(problem_words, phrase))
        # solve_problem(problem_words, phrase)
    # except: pass
