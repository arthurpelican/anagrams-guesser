from itertools import permutations

def main() :
    raw_words = open("words.txt").readlines()

    words = set()
    for word in raw_words :
        words.add(word[0:-1])

    anagram = input("Enter your anagram ")

    anagram_permutations = permutations(anagram)

    for permutation in anagram_permutations :
        formated_permutation = ""
        for letter in permutation :
            formated_permutation += letter

        if formated_permutation in words :
            solution = formated_permutation
        
    print(f"the solution is {solution}")

if __name__ == "__main__" :
    main()