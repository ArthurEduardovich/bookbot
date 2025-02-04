def main():
    path = "books/frankenstein.txt"
    text = get_text_book(path) 
    count_symbols = count_char(text) 
    count_characters = count_character(text)
    report_final = report(count_characters)
    #print(report_final)
    
    print(f"--- Begin report of {path} ---")
    print(f"{count_symbols} words found in the document")
    print(' ')
    for char in report_final:
        if char["key"].isalpha():
            print(f"The {f"'{char["key"]}'"} character was found {char["value"]} times")
    
    print("--- End report ---")

def sort_on(dict):
    return dict["value"]

def report(count_characters):
    list_dict = []
    for key, value in count_characters.items():
        list_dict.append({"key": key, "value": value})
    list_dict.sort(reverse=True, key=sort_on)
    return list_dict

def count_character(text):
    lower_text = text.lower()
    unique_dict = {}
    for char in lower_text:
        if char in unique_dict:
            unique_dict[char] += 1
        else:
            unique_dict[char] = 1
    return unique_dict

def count_char(text):
    count = 0
    for char in text.split():
        count += 1
    return count

def get_text_book(path):
    with open(path) as f:
        text_book = f.read()
    return text_book


main()

