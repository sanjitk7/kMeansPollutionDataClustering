def result(cluster_dict,population_dict):
    population = list(population_dict.values())
    for i in range(len(population)):
        population[i]=int(population[i].replace(",",""))
    city = list(population_dict.keys())
    clustered_city={}
    
    for j in range(len(cluster_dict.keys())):
        curr_cluster_list_tup=cluster_dict[j]
        temp_list=[]
        for i in range(len(curr_cluster_list_tup)):
            curr_cluster_pop=curr_cluster_list_tup[i][0]
            temp_list.append(city[population.index(curr_cluster_pop)])
        clustered_city[j]=temp_list
    return clustered_city
        
