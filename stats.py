def get_num_words(text):
    words = text.split()
    word_count = len(words)
    return word_count

def get_num_char(text):
    count = {}
    for char in text:
        char = char.lower()
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    return count

def sort_on(items):
    return items["num"]

def sorted_chars_dict(counts):
    new_list = []
    for char, num in counts.items():
        new_item = {"char": char, "num": num}
        new_list.append(new_item)
    new_list.sort(reverse=True, key=sort_on)
    return new_list