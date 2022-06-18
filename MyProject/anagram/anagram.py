"""
File: anagram.py
Name: Leah
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""
import pdb
import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop
dictionary = {}
result_lst = []


def main():
    print("Welcome to stanCode ''Anagram Generator'' (or -1 to quit)")

    ch = input('Find anagrams for: ')

    default = 1
    ch_dict = {}
    for c in ch:
        if c in ch_dict:
            ch_dict[c] += 1
        else:
            ch_dict[c] = default

    start = time.time()
    read_dictionary(ch, ch_dict)
    find_anagrams(ch)
    end = time.time()
    print(f"{len(result_lst)} anagrams: {result_lst}")
    print(f'The speed of your anagram algorithm: {end-start} seconds.')
    print('----------------------------------')

    """
    permutation = list(permutations(ch, len(ch)))
    result_lst = []
    for ele in permutation:
        str_c = ''.join(ele)
    if str_c in dictionary:
        result_lst.append(str_c)
    """


def read_dictionary(ch, ch_dict):
    default = 0
    temp_dict = {}
    with open(FILE, 'r') as f:
        for line in f:
            word = line.strip()
            if len(word) == len(ch):
                temp_dict[word] = default
        ch_dict = sorted(ch_dict.items(), key=lambda ele: ele[1], reverse=True)

        for temp_str in temp_dict:
            count = 0
            for temp_c in temp_str:
                if temp_c is ch_dict[0][0]:
                    count += 1
                    if count == ch_dict[0][1]:
                        dictionary[temp_str] = default
                        default += 1
                    else:
                        pass
                else:
                    pass


def find_anagrams(ch):
    """
    :param ch: input string
    :return: the anagram(s) are found
    """
    if ch == "":
        return
    elif len(ch) == 1:
        result_lst.append(ch)
        print('Searching......')
        print('Found: ', ch)
    else:
        for c_idx, each_c in enumerate(ch):
            if c_idx >= 1:
                if ch[c_idx] != ch[c_idx-1]:
                    rest_s = ch[:c_idx] + ch[c_idx+1:]
                    find_anagrams_helper(each_c, rest_s)
                else:
                    pass
            else:
                rest_s = ch[:c_idx]+ch[c_idx+1:]
                find_anagrams_helper(each_c, rest_s)


def find_anagrams_helper(sub_s, rest_s):
    # pdb.set_trace()
    if (rest_s == "") and (sub_s in dictionary) and (sub_s not in result_lst):
        result_lst.append(sub_s)
        print('Searching......')
        print('Found: ', sub_s)
        return

    if len(rest_s) == 1:
        if has_prefix(sub_s + rest_s):
            find_anagrams_helper(sub_s+rest_s, "")
            return
        else:
            return

    for c_idx, each_c in enumerate(rest_s):
        if c_idx < (len(rest_s)-1):  # 上限減一，i+1才不會炸裂
            if rest_s[c_idx] != rest_s[c_idx+1]:
                if has_prefix(sub_s + each_c):
                    find_anagrams_helper(sub_s + each_c, rest_s[:c_idx] + rest_s[c_idx + 1:])
            else:
                pass
        else:
            if has_prefix(sub_s + each_c):
                find_anagrams_helper(sub_s + each_c, rest_s[:c_idx] + rest_s[c_idx + 1:])


def has_prefix(sub_s):
    """
    :param sub_s: check the string whether in dictionary or not
    :return: True or False
    """
    for dict_str in dictionary:
        if dict_str.startswith(sub_s):
            return dict_str.startswith(sub_s)
    return False


if __name__ == '__main__':
    main()
