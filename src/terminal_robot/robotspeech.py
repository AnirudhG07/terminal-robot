import re

import cv2
from metaphone import doublemetaphone


def exceptional_handling(excep_list: list, word):
    for exc in excep_list:
        if exc in word:
            return False
            break
    return True


def punctuation_handling(word):
    word = word.lower()
    freeword = ""
    for char in word:
        freeword += char if "a" <= char <= "z" else ""
    return freeword


def metaphone(word):
    metaword = ""
    word = word.lower()
    pattern = r"([^aeiou])\1{1,}"

    # Use the sub function to remove double consonants while preserving double vowels
    word = re.sub(pattern, r"\1", word)
    meta = doublemetaphone(word)[0].lower()
    # print(meta)       ###
    if meta[0] == "a" and meta != "a":
        meta = meta[1:]
    # print(meta)       ###
    vowels = "aeiouwxy"

    # Combine consonants from Metaphone and vowels from the word
    consonant_index = 0
    exceptional_listfor_y = ["cry", "dry", "fly", "sly", "try", "wry", "my"]
    exceptional_listfor_e = ["hare", "rte", "we", "qe", "he", "me"]
    pattern2 = r"(sh|th|ch|ph|bh|gn|rh|lh|ck|kn)"
    # Use the sub function to replace all "sh," "th," or "ch" with "q"
    word = re.sub(pattern2, "q", word)

    # print(word)    ###
    if len(word) == 1:
        word = word
    elif word[:2] == "wh":
        meta = "vh" + meta
    else:
        if "dh" in word:
            word = word.replace("dh", "q")
            meta = meta.replace("T", "0")
        if "kh" in word:
            word = word.replace("kh", "k")
        if "gh" in word:
            if word[:2] == "gh":
                word = word.replace("gh", "g")
            elif "igh" in word:
                word = re.sub(r"igh", "ai", word)
            else:
                word = word.replace("gh", "")
        if word[-1] == "e" and exceptional_handling(exceptional_listfor_e, word):
            word = word[:-1]
        if word[-1] == "y" and exceptional_handling(exceptional_listfor_y, word):
            word = word[:-1] + "i"
        if word[0] == "y":
            word = word[1:]
        if word[-1] == "w" and len(word) == 3:
            if word[-2:] == "ew":
                word = word[:-1] + "u"
            else:
                word = word[0] + "a" + word[1:-1]
        if word[-1] == "w" and len(word) != 3:
            if word[-2:] == "ew":
                word = word[:-1] + "u"
            else:
                word = word[:-1]
        if word[0] == "w":
            word = "v" + word[1:]
            meta = "v" + meta
        if word[:2] == "pn" or word[:2] == "ps":
            word = "n" + word[2:]
        else:
            word = word
    # print(word)   ###
    for char in word:
        if char in vowels:
            # If the character is a vowel, add a vowel from the original word
            if char == "y":  #  Y HANDLING
                # if y is at the end of word, then add 'i' else 'ai'
                if word[:2] == "sy" or word[:2] == "qy":
                    char = "i"
                    metaword += char
                else:
                    char = "ai"
                    metaword += char
            elif char == "x":  # X HANDLING
                if word[0] != "x":
                    if "xc" in word:
                        metaword += char
                        meta = meta.replace("ks", "k")
                    else:
                        char = "ks"
                        metaword += char
                        meta = meta.replace("ks", "")
            elif char == "w":
                metaword += "v"
            else:
                word = re.sub(r"ow", "ao", word) if "ow" in word else word
                metaword += char

        else:
            # If the character is not a vowel (i.e., a consonant), add a consonant from the Metaphone representation
            metaword += meta[consonant_index]
            consonant_index += 1

    return metaword


def linearize(sentence):
    punctuation = ["", " ", ".", "!", ",", ", ", "?", ";", ":", '"', '" ', '" ', '"']
    parts = re.split(r"(\s+|\W)", sentence)
    converted_sentence, error_count = "", 0
    # print(parts)   ###
    exceptional_list_dict = {
        "dough": "dou",
        "w": "dablu",
        "A": "a",
        "i": "ai",
        "hi": "ai",
    }
    for part in parts:
        if part not in exceptional_list_dict:
            if part not in punctuation:
                part = punctuation_handling(part)
                try:
                    metaphone_word = metaphone(part)
                except Exception as _:
                    error_count += 1
                    metaphone_word = "oops"
                converted_sentence += metaphone_word
            else:
                converted_sentence += part
        else:
            converted_sentence += exceptional_list_dict[part]
    # print(converted_sentence, error_count)  ###
    return converted_sentence


def display_metaword(metaword):
    # create a mouthdict dictionary having png files for each alphabet

    mouthdict = {
        " ": "robot_m.png",
        ".": "robot_h.png",
        "!": "robot_h.png",
        "?": "robot_h.png",
        ",": "robot_h.png",
        ", ": "robot_h.png",
        "a": "robot_a.png",
        "b": "robot_e.png",
        "c": "robot_e.png",
        "d": "robot_h.png",
        "e": "robot_e.png",
        "f": "robot_m.png",
        "g": "robot_o.png",
        "h": "robot_h.png",
        "i": "robot_h.png",
        "j": "robot_o.png",
        "k": "robot_o.png",
        "l": "robot_s.png",
        "m": "robot_m.png",
        "n": "robot_m.png",
        "o": "robot_o.png",
        "p": "robot_e.png",
        "q": "robot_s.png",
        "r": "robot_o.png",
        "s": "robot_s.png",
        "t": "robot_e.png",
        "u": "robot_u.png",
        "v": "robot_s.png",
        "w": "robot_s.png",
        "x": "robot_s.png",
        "y": "robot_s.png",
        "z": "robot_s.png",
    }

    for char in metaword:
        if char in mouthdict:
            mouth = mouthdict[char]
            # print(mouth)
            cv2.imshow(f"{char}", cv2.imread("./images/" + mouth))
            cv2.waitKey(100)

            cv2.destroyAllWindows()
    return


if __name__ == "__main__":
    input_sent = input("Enter a sentence:")
    key = linearize(input_sent)
    import timeit

    start = timeit.default_timer()
    display_metaword(key)
    stop = timeit.default_timer()
    print(stop - start)
