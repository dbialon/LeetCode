# https://leetcode.com/problems/unique-morse-code-words/
# return the number of different transformations
# among all words we have.

morse_code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

def print_morse(word):
    print(word, end=" ")
    for letter in word:
        idx = ord(letter.lower()) - ord('a')
        print(morse_code[idx], end="")
    print()

my_list = ["Aga", "gin", "zen", "gig", "msg"]

for word in my_list:
    print_morse(word)

def get_code(word):
    code = ""
    for letter in word:
        idx = ord(letter.lower()) - ord('a')
        code += morse_code[idx]

    return code

codes = []
for word in my_list:
    codes.append(hash(get_code(word)))

unique_codes = set(codes)

print(len(unique_codes))
