def sentencebot(string):
    # make string to lowecase
    string = string.lower()

    def countsyllables(string):
        # set count on 0
        count = 0
        vowels = "aeiouy"
        # if the string starts with a vowel add count +1
        if string[0] in vowels:
            count += 1
        # iterate over string
        for index in range(1, len(string)):
            if string[index] in vowels and string[index - 1] not in vowels:
                count += 1
        if string.endswith("e"):
            count -= 1
        if count == 0:
            count += 1
        return count

    def count(string):
        # make variable that splits the string and return that
        countwords = len(string.split(" "))
        return countwords

    def rearrange(string):
        # split the string
        words = string.split()
        # sort the words
        sortedwords = sorted(words)
        # convert words back to string
        sortedstring = ', '.join(sortedwords)
        # return the string with the sorted words
        return sortedstring

    # make variable with output and return it bacause otherwise if we just print that the output would give 'None' back
    output = f"it counts {countsyllables(string)} syllables, {count(string)} words and this is the  rearranged string: {rearrange(string)}"
    return output
