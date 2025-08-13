def get_num_words(txt):
    return len(txt.split())
def get_num_characters(txt):
    counts = {}
    for char in txt:
        char = char.lower()
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    return counts
def sort_on(items):
    return items["num"]
def dic_sorter(counts):
    list = []
    for char in counts:
        count = counts[char]
        new_dict = {"char": char, "num": count}
        list.append(new_dict)
    list.sort(reverse=True, key=sort_on)
    return list


    
