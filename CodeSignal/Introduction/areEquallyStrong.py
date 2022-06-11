def solution(yourLeft, yourRight, friendsLeft, friendsRight):
    guyone = [yourLeft, yourRight]
    guytwo = [friendsLeft, friendsRight]
    return max(guyone) == max(guytwo) and min(guyone) == min(guytwo)