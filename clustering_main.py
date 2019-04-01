import Constant
import random
import clustering_functions
import input_data_processing

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

def main(k):
    #clean data for use
    population_dict,pm10_dict = input_data_processing.prep_data();

    pop_pm = list()
    for state in population_dict:
        pop_pm.append((int(population_dict[state].replace(",","")),int(pm10_dict[state])))

    #print(pop_pm)
    #pop_pm = list(zip(Pop,PM)) # list of datapoints

    centroid=[]
    #Random Centroid Generation
    for i in range(0,k):
        centroid.append((random.randint(Constant.MIN_POP,Constant.MAX_POP),random.randint(Constant.MIN_PM,Constant.MAX_PM)))
    #print("Random Centroids:",centroid)

    #cluster initialisation
    cluster_dict = {i: [] for i in range(k)}
    #initialise prev centroid list
    prev_centroid=[]
    #LOOP
    cluster_dict,cen_res=clustering_functions.cluster(prev_centroid,centroid,pop_pm,cluster_dict,k)
    #Check if new centroid = old centroid - stop: else - iterate agian.
    #print( cluster_dict,"\n CEN:",cen_res)
    return cluster_dict,cen_res