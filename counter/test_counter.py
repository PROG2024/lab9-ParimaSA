"""Write a unit test to verify that Counter is a singleton.

   Also verify that all instances share the same count
   and that the count is not reset to 0 when you invoke 
   count = Counter() 
   after the first time.

   You can use pytest or unittest.
"""
import unittest
from counter import Counter


class TestCounter(unittest.TestCase):
    def setUp(self):
        """Setup two main counter for the test"""
        self.counter1 = Counter()
        self.counter2 = Counter()

    def test_two_counter_is_the_same_instance(self):
        """two Counter should be the same instance"""
        self.assertEqual(self.counter1, self.counter2)

    def test_two_counter_share_the_same_count(self):
        """when any Counter call the increment, count of all Counter should be adding up"""
        self.counter1.increment()
        self.counter1.increment()
        self.assertEqual(self.counter1.count, self.counter2.count)
        self.counter2.increment()
        self.assertEqual(self.counter1.count, self.counter2.count)

    def test_new_counter_have_the_same_count(self):
        """if current Counter has some count, new Counter should have the same count"""
        new_counter = Counter()
        self.counter1.increment()
        self.assertNotEqual(new_counter.count, 0)
        self.assertEqual(new_counter.count, self.counter1.count)

