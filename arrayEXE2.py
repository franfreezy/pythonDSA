#heros=['spider man','thor','hulk','iron man','captain america']
#1. Length of the list
#2. Add 'black panther' at the end of this list
#3. You realize that you need to add 'black panther' after 'hulk',
#   so remove it from the list first and then add it after 'hulk'
#4. Now you don't like thor and hulk because they get angry easily :)
#   So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
#   Do that with one line of code.
#5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)

#THE IMPLEMENTATION

heros=['spider man','thor','hulk','iron man','captain america']

def part1(heros):
    Length=len(heros)
    return Length


def part2(heros):
    heros.append('black panther')
    return heros
print(part2(heros))
