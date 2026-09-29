import math
#same dataset as Assignment 42-1


data=[
    ("A",1,2,"Red"),
    ("B",2,3,"Red"),
    ("C",3,1,"Blue"),
    ("D",6,5,"Blue")
]
#Accept input from user
x=float(input("Enter X coordinate: "))
y=float(input("Enter Y coordinate: "))
#calculate Euclidean distance
distances=[] 
for point,px,py,label in data:
    distance=math.sqrt((x - px)**2 + (y - py)**2)
    distances.append((distance,point,label))
    #sort distances in ascending order
    distances.sort()
    print("\nPrediction Results")
    #test different k values
    for k in [1,3,5]:
        if k > len(data):
            print(f"k ={k}-> Not possible""(only 4 data points)")
            continue
        neighbors=distances[:k]
        votes={}
    for distance,point,label in neighbors:
        votes[label]=votes.get(label,0)+1
        predicted_class=max(votes,key=votes.get)
        print(f"k = -> {predicted_class}")



    