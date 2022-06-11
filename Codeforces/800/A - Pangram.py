from string import ascii_lowercase
input();print("YES" if len(set([l.lower() for l in input()])) == len(ascii_lowercase) else "NO")