from django.test import TestCase
import numpy as np

from backend.data_processing_core.deep_learning.services.attention_score_service import AttentionScoreService, pair_coords_and_attention_scores, get_attention_scores_for_each_class, get_min_max_with_percentile

class TestAttentionScoreService(TestCase):

    def test_pair_coords_and_attention_scores(self):
        scores ={0:[1,2],1:[1,2]}
        coords=[(0,0),(1,1)]
        data = pair_coords_and_attention_scores(scores,coords)
        
        self.assertTrue('coords' in data, True)
        self.assertTrue(0 in data, True)
        self.assertTrue(1 in data, True)

        for k,v in data.items():
            self.assertEqual(len(v),2)

    def test_get_attention_scores_for_each_class(self):
        A = np.array([[np.random.randint(low=0, high=100, size=10)] for i in range(3)])
        result = get_attention_scores_for_each_class(A)

        for i in range(3):
            self.assertTrue(i in result)
            self.assertEqual(len(result[i]),1)
            self.assertEqual(len(result[i][0]),10)
