import Constant
import random
import math
import copy
def edist(A,B):
    dist=math.sqrt((A[0] - B[0])**2 + (A[1] - B[1])**2)
    return dist
def calc_avg(dp_list,k):
    sum1=0
    sum2=0
    for i in range(len(dp_list)):
        sum1+=dp_list[i][0]
        sum2+=dp_list[i][1]
    x_avg=sum1/k
    y_avg=sum2/k
    return (int(x_avg),int(y_avg))
def diff(prev,curr):
    print("---------------------")
    for i in range(0,len(prev)):
        x=prev[i][0]-curr[i][0]
        y=prev[i][1]-curr[i][1]
        print((x,y))
        
centroid=[]
PM=[39,
81,
63,
38,
73,
103,
100,
63,
105,
104,
63,
62,
85,
85]
SC=[582,
583,
150,
151,
152,
95,
203,
365,
393,
394,
470,
581,
466,
577]
SC_PM=dict(zip(SC,PM))
Pop=[7,8,6,5,2,1,4,10,5,5,10,4,3,6.5]
pop_pm = list(zip(Pop,PM)) # list of datapoints

#Random Centroid Generation
k=2;
for i in range(0,k):
    centroid.append((random.randint(Constant.MIN_POP,Constant.MAX_POP),random.randint(Constant.MIN_PM,Constant.MAX_PM)))
##print("Random Centroids:",centroid)

#cluster initialisation
cluster_dict = {i: [] for i in range(k)}
#initialise prev centroid list
prev_centroid=[]
#LOOP
count_while=0
while(prev_centroid!=centroid):
    count_while+=1;
#Euclidean Distance between the Centroid and DataPoints
    for i in range(0,len(pop_pm)):
        temp=[]
        for j in range(0,k):
            temp.append(edist(pop_pm[i],centroid[j]))
        cen_number=temp.index(min(temp))
        cluster_dict[cen_number].append(pop_pm[i])
    ##print("CLUSTER DICTIONARY : ", cluster_dict)

#Prev Centroid temp
    prev_centroid=copy.deepcopy(centroid)
#Calculate New Centroids from the lists
    for i in range(0,k):
        centroid[i] = calc_avg(cluster_dict[i],k)
   # diff(prev_centroid,centroid)
   # print("iteration number :",count_while)
    print("Updated Centroids :",centroid)  


#Check if new centroid = old centroid - stop: else - iterate agian. 
