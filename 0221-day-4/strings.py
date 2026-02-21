s = "abcabc" # s = ['a', 'b', 'c']
print(s[1])
print(s[-1])

print(s[0:3])
print(s[0::2])
print(s[::-1])

word = "racecar"
print(word == word[::-1])

w = "a.b.c.d.e"
u = w.split('.')

print(u)

v = '.'.join(u)
print(v)

chrs = ['M', 'i', 'c', 'h', 'a', 'e', 'l']

name = ''.join(chrs)
print(name)