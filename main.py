def main():
    text = ""
    path = "books/frankenstein.txt"

    with open(path) as f:
        text = f.read()

    word_count = word_counter(text)

    letter_count = letter_counter(text.lower())
    
    book_report(path, word_count, letter_count)

    return None

def word_counter(text):
    
    words = text.split()
    
    return len(words)

def letter_counter(text):
    
    letter_count = {}
    
    for letter in text:
        # Probably more efficient to only check isalpha() when letter not already in dictionary
        if not letter.isalpha():
            pass
        elif letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1

    return letter_count

def sort_on(dict):
    return dict["count"]

def book_report(path, words, letters):
    print("---------BEGIN REPORT---------")
    print(f"The document at \"{path}\" contains {words} words.\n")

    letter_list = []
    for letter in letters:
        letter_dict = {"alpha": letter, "count": letters[letter]}
        letter_list.append(letter_dict)
    
    # letter_list[i] = {"alpha": x, "count",n}
    letter_list.sort(reverse=True, key=sort_on)

    for entry in letter_list:
        print(f"{entry["alpha"]} occurs {entry["count"]} times.")
    
    print("---------END REPORT---------")
    return None

main()
