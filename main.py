def count_character(my_string):
    character_count = {}
    lower_case = my_string.lower()

    for characters in lower_case:
        if characters.isalpha():
            if characters in character_count: # if a character exist +1
                character_count[characters] += 1
            else: #if character not in dict create one
                character_count[characters] = 1

    sorted_characters = dict(sorted(character_count.items(), key=lambda item: item[1], reverse=True))
    for characters, count in sorted_characters.items():
        print(f"The '{characters}' was found {count} times")

def main():
    path_to_file = 'books/frankenstein.txt'

    with open(path_to_file, 'r') as f:
        file_contents = f.read()
    words = file_contents.split()
    count = len(words)
    print(file_contents)
    print(f"--- Begin report of {path_to_file} ---")
    print(f"{count} words found in the document")
    print()
    count_character(file_contents)
    print()
    print(f"--- End report ---")

# Call the main function to execute the program
if __name__ == "__main__":
    main()
