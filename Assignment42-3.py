import math
#Dataset
data=[
    (2,60,"Fail"),
    (5,80,"Pass"),
    (6,85,"Pass"),
    (1,50,"Fail")
]
#Accept input from user
hours=float(input("Enter study hours: "))
attendance=float(input("Enter Attendance: "))
#calculate Euclidean distance
distances=[] 
for study_hours,attend,result in data:
    distance=math.sqrt((hours - study_hours)**2 + (attendance - attend)**2)
    distances.append((distance,result))
    #sort distances 
    distances.sort()
    #select K=3 nearest neighbors
    k=3
    neighbors=distances[:k]
    #majority voting
    votes={}
    for distance,result in neighbors:
        votes[result]=votes.get(result,0)+1
        predicted_result=max(votes,key=votes.get)
        print("\nPredicted Result:",predicted_result)