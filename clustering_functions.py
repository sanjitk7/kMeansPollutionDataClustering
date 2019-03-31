import math
import copy
def edist(A,B):
    dist=math.sqrt((A[0] - B[0])**2 + (A[1] - B[1])**2)
    return round(dist,2)


def calc_avg(dp_list):
    sum1=0
    sum2=0
    for i in range(len(dp_list)):
        sum1+=dp_list[i][0]
        sum2+=dp_list[i][1]
    x_avg=sum1/len(dp_list)
    y_avg=sum2/len(dp_list)
    return (round(x_avg),round(y_avg))


def diff(prev,curr):
    print("Prev in diff :",prev,"Curr in diff ",curr)
    for i in range(0,len(prev)):
        x=prev[i][0]-curr[i][0]
        y=prev[i][1]-curr[i][1]
        print((x,y))
        
def alloc_dp_to_cluster_no(pop_pm,centroid,cluster_dict,k):
    for i in range(0,len(pop_pm)):
        temp=[]
        for j in range(0,k):
            temp.append(edist(pop_pm[i],centroid[j]))
        cen_number=temp.index(min(temp))
        cluster_dict[cen_number].append(pop_pm[i])
        #print("CLUSTER DICTIONARY : ", cluster_dict)        
    return cluster_dict

def calc_new_centroid(centroid,cluster_dict,k):
        for i in range(0,k):
            centroid[i] = calc_avg(cluster_dict[i])
        return centroid


def cluster(prev_centroid,centroid,pop_pm,cluster_dict,k):
    count_while=0
    while(prev_centroid!=centroid):
        #print("Prev Cen :",prev_centroid)
        #print("Curr Cen :",centroid)
        #Clean Original Centroid dict
        for i in range(k):
            cluster_dict[i]=[]
        
        #Euclidean Distance between the Centroid and DataPoints
        cluster_dict=alloc_dp_to_cluster_no(pop_pm,centroid,cluster_dict,k)

        #Prev Centroid temp
        prev_centroid=copy.deepcopy(centroid)
        
        #Calculate New Centroids from the lists
        centroid=calc_new_centroid(centroid,cluster_dict,k)

        count_while+=1
        diff(prev_centroid,centroid)
        #print("iteration number :",count_while)
        #print("Updated Centroids :",centroid)
        #print("Clusters Current :",cluster_dict)
        #print("---------------------")
    return cluster_dict,centroid


        
