def get_num_words(text):
    words = text.split()
    return len(words)

def get_char_counts(text):
    text = text.lower()
    counts = {}
    for char in text:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    return counts

def sort_char_counts(char_counts):
    sorted_list = []
    for char, count in char_counts.items():
        sorted_list.append({"char": char, "count": count})
    sorted_list.sort(key=lambda item: item["count"], reverse=True)
    return sorted_list
