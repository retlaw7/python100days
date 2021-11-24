sentence = "supercalifragilisticexpealidocious"
newline = ""
position = -1
for char in sentence:
    newline += sentence[position]
    position -=1
print(sentence)
print(newline)
