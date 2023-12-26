
person1=input("Enter Your Name:")
person2=input("Enter Your Crush Name:")

name1=person1.lower()
name2=person2.lower()

nameToCount=""

for i in name1:
    if i in name2:
        name2=name2.replace(i,'',1)
        name1=name1.replace(i,'',1)

length=len(name1)+len(name2)

flames=['Friends','Love','Attraction','Marriage','Enemies','Siblings']

count=1
index=0

while True:
    if index == len(flames):
        index = 0

    if count % length == 0:
        flames.pop(index)
        index-=1

    count += 1
    index += 1

    if len(flames) == 1:
        break

print(f"The relationship between {person1} and {person2} is '{flames[0].upper()}'")
