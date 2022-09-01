import unittest
import bubblesort as st

class Project_Test(unittest.TestCase):
    def test_bsort(self):
       testList = [4,3,2,1]
       expected = [1,2,3,4]
       actual = st.bubblesort(testList)
       self.assertEqual(actual,expected)
       
    def test_desc(self):
        testList = [1,2,5,4,3]
        expected = [5,4,3,2,1]
        actual = st.bubblesort(testList)
        self.assertEqual(actual,expected)
        
    def test_empty(self):
        testList = []
        expected = []
        actual = st.bubblesort(testList)
        self.assertEqual(actual,expected)    