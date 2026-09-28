import unittest
from research.core import difference_in_differences as did
class Tests(unittest.TestCase):
 def test_known_effect(self): self.assertEqual(did(100,115,90,95),10)
 def test_common_trend_cancels(self): self.assertEqual(did(100,105,90,95),0)
 def test_additive_shift_invariant(self): self.assertEqual(did(100,115,90,95),did(150,165,140,145))
 def test_nonfinite_rejected(self):
  with self.assertRaises(ValueError): did(1,float('nan'),1,2)

if __name__=="__main__": unittest.main()
