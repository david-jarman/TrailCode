def uniqueCharacters(string):
    characterMap = {}
    
    for character in string:
        if character in characterMap:
            return False
        else:
            characterMap[character] = True

    return True

def uniqueCharacterWithoutDataStructures(string):
    checker = int(0)
    
    for character in string:
        val = ord(character) - ord('a')
        if checker & (1 << val) > 0:
            return False
        else:
            checker |= 1 << val

    return True
        

exampleOne = "abcdefggh"
exampleTwo = "abcdefgh"
exampleThree = ""
exampleFour = "abca"
exampleFive = "abcdefghijklmnopqrstuvwxyzABCDEF123!"

print "example one"
print uniqueCharacters(exampleOne)
print uniqueCharacterWithoutDataStructures(exampleOne)

print "example two"
print uniqueCharacters(exampleTwo)
print uniqueCharacterWithoutDataStructures(exampleTwo)

print "example three"
print uniqueCharacters(exampleThree)
print uniqueCharacterWithoutDataStructures(exampleThree)

print "example four"
print uniqueCharacters(exampleFour)
print uniqueCharacterWithoutDataStructures(exampleFour)

print "example five"
print uniqueCharacters(exampleFive)
