s = "education"
vowels = ['a','e', 'i', 'o', 'u']

def countvowels(s):
    count = 0
    for c in s:
        if c in vowels:
            count+=1
    return count

print(countvowels(s))