import unittest
import math
from clustering_functions import edist,calc_avg,alloc_dp_to_cluster_no,calc_new_centroid,cluster
from clustering_result import result
 
class TestUM(unittest.TestCase):
 
    def setUp(self):
        pass

    def test_edist(self):
        self.assertEqual(edist((1,2), (3,4)),2.83)
        
    def test_calc_avg(self):
        list1=[(2,1),(3,1),(4,4)]
        self.assertEqual(calc_avg(list1),(3,2))
        list2=[(1,1),(7,4),(8,1)]
        self.assertEqual(calc_avg(list2),(5,2))


    def test_alloc_dp_to_cluster_no(self):
        pop_pm=[(1,2),(1,3),(3,4),(3,3),(6,1),(6,3),(7,2),(8,3),(2,2),(2,4)]
        centroid=[(2,3),(7,2)]
        cluster_dict={0:[],1:[]}
        dict1={0: [(1, 2), (1, 3), (3, 4), (3, 3), (2, 2), (2, 4)], 1: [(6, 1), (6, 3), (7, 2), (8, 3)]}
        self.assertEqual(alloc_dp_to_cluster_no(pop_pm,centroid,cluster_dict,2),dict1)

    def test_calc_new_centroid(self):
       centroid=[(2,3),(7,2)]
       cluster_dict={0: [(1, 2), (1, 3), (3, 4), (3, 3), (2, 2), (2, 4)], 1: [(6, 1), (6, 3), (7, 2), (8, 3)]}
       s1=calc_avg([(1, 2), (1, 3), (3, 4), (3, 3), (2, 2), (2, 4)])
       s2=calc_avg([(6, 1), (6, 3), (7, 2), (8, 3)])
       expected_centroid=[s1,s2]
       self.assertEqual(calc_new_centroid(centroid,cluster_dict,2),expected_centroid)

    def test_cluster_1_iteration(self):
       prev=[(2,2),(8,2)]
       centroid=[(2,3),(7,2)]
       pop_pm=[(1,2),(1,3),(3,4),(3,3),(6,1),(6,3),(7,2),(8,3),(2,2),(2,4)]
       cluster_dict={0:[(0,0),(0,1)],1:[(1,1),(2,2)]}
       dict1={0: [(1, 2), (1, 3), (3, 4), (3, 3), (2, 2), (2, 4)], 1: [(6, 1), (6, 3), (7, 2), (8, 3)]}
       self.assertDictEqual(cluster(prev,centroid,pop_pm,cluster_dict,2)[0],dict1)
       self.assertListEqual(cluster(prev,centroid,pop_pm,cluster_dict,2)[1],centroid)

    def test_cluster_2_iteration(self):
        prev=[(2,2),(8,2)]
        centroid=[(0,1),(0,2)]
        pop_pm=[(1,2),(1,3),(3,4),(3,3),(6,1),(6,3),(7,2),(8,3),(2,2),(2,4)]
        cluster_dict={0:[(0,0),(0,1)],1:[(1,1),(2,2)]}
        dict1={1: [(1, 2), (1, 3), (3, 4), (3, 3), (2, 2), (2, 4)], 0: [(6, 1), (6, 3), (7, 2), (8, 3)]}
        self.assertDictEqual(cluster(prev,centroid,pop_pm,cluster_dict,2)[0],dict1)
        self.assertListEqual(cluster(prev,centroid,pop_pm,cluster_dict,2)[1],centroid)

    def test_result(self):
        cluster_dict={0:[(15000000,0),(5000000,1)],1:[(6000000,1),(8000000,2)]}
        population_dict={"chennai":15000000,"erode":5000000,"vellore":6000000,"coimbatore":8000000}
        list_of_cities_0=["chennai","erode"]
        list_of_cities_1=["vellore","coimbatore"]
        clustered_city={0: ['chennai', 'erode'], 1: ['vellore', 'coimbatore']}
        self.assertDictEqual(result(cluster_dict,population_dict),clustered_city)
     
if __name__ == '__main__':
    unittest.main()





