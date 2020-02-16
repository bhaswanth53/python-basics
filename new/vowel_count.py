def vowel_check(word) :
    vowels = ['a', 'o', 'u', 'i', 'e', 'y']
    count = 0
    for i in word :
        if(i in vowels) :
            count += 1
    return count

num = int(input())

results = []
words = []

for i in range(num):
    word = input()
    words.append(word)

for item in words :
    x = vowel_check(item)
    results.append(x)

for i in results :
    print(i, end=' ')