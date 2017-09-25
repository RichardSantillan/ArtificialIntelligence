from sklearn import tree

#[alcohol percent, color of drink]
#amber = 0, red = 1, clear = 2, green = 3
features = [[4.5,0],[11.6,1],[37,2],[40,3]]
color = ["amber","red","clear","green"]

#[beverage type]
labels = ["beer","wine","liquor","liquor"]
word = ""
count = 1

fr = open('beveragedata.txt','r')
text = fr.read()
for char in text:
    if char != " ":
        word += char
    elif(count%3 == 1 and char == " "):
        print("Alcohol %: "+word)
        features.append([float(word),len(color)])
        word = ""
        count+=1
    elif(count%3 == 2 and char == " "):
        print("Color: "+word)
        color.append(word)
        word = ""
        count+=1
    elif(count%3 == 0 and char == " "):
        print("Type: "+word)
        labels.append(word)
        word = ""
        count+=1

hasColor = True;

print(features)
print(labels)

clf = tree.DecisionTreeClassifier()
clf = clf.fit(features,labels)

alcoholContent= float(input('Give the alocohol content (%)?'))
beverageColor = input('Give the color of the beverage?')

fr.close()
fw = open('beveragedata.txt','a')

for i in range(0,len(labels)):
    if beverageColor == color[i]:
        beverageColor == i
        hasColor = True
        break
    else:
        userPrediction2 = 4
        hasColor = False;

if(hasColor):
    print ("Your beverage is a type of")
    print (clf.predict([[alcoholContent,color.index(beverageColor)]]))
else:
    beverageType = input("You beat me! What type of drink was it?")
    fw.write(str(alcoholContent) + ' ' + beverageColor + ' ' + beverageType+' \n');

fw.close()
