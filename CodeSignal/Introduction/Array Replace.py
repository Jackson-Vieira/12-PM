def solution(inputArray, elemToReplace, substitutionElem):
    return [substitutionElem if elm == elemToReplace else elm for elm in inputArray]
