def solve(s):
    print (s.split(" "))
    return (" ".join([x.capitalize() for x in s.split(' ')]))
s = input()
result = solve(s)
print (result)
