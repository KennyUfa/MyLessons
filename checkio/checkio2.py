text = '''When I was One
I had just begun
When I was Two
I was nearly new When'''
words = ['i','was', 'three', 'near']

text = text.lower().split()
count ={}
for i in words:
    count[i] = text.count(i)
print(count)



