import math
#Dataset
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
    #select K=3 nearest neighbors
    k=3
    neighbors=distances[:k]
    print("\nNearest Neighbors:")
    votes={}
    for distance,point,label in neighbors:
        print(f"{point} - Distance:{distance:.2f}")
        votes[label]=votes.get(label,0)+1
#majority voting
predicted_class=max(votes,key=votes.get)
print("\nPredicted class:",predicted_class)