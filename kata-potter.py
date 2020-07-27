import unittest

PRIX_LIVRE = 8
DISCOUNTS = {2: 0.95, 3: 0.90, 4: 0.80, 5: 0.75}

def prix(list_livre):
  """ renvoie le prix d'une liste de livre"""
  sets= livre_groupe(list_livre)
  optimisation_prix(sets)
  return sum(calcul_prix(qty) for qty in sets)

def livre_groupe(livres):
  """renvoie une liste de quantitée de livre""" 
  set_sizes = []
  while livres:
    set_livres = set(livres)
    set_sizes.append(len(set_livres))
    for livre in set_livres:
      livres.remove(livre)
  return set_sizes

def optimisation_prix(sets):
  """optimisation dans le cas ou il y a 5 livres et 3 livres pour faire 2*4 livres"""
  while 5 in sets and 3 in sets:
    sets.remove(5)
    sets.remove(3)
    sets.append(4)
    sets.append(4)

def calcul_prix(qty):
  """renvoie le prix pour une quantitée de livre avec ristourne"""
  return PRIX_LIVRE * qty * DISCOUNTS.get(qty, 1)

class TestPotter(unittest.TestCase):
  def testBasics(self):
    self.assertEqual(0, prix([]))
    self.assertEqual(8, prix([0]))
    self.assertEqual(8, prix([1]))
    self.assertEqual(8, prix([2]))
    self.assertEqual(8, prix([3]))
    self.assertEqual(8, prix([4]))
    self.assertEqual(8 * 2, prix([0, 0]))
    self.assertEqual(8 * 3, prix([1, 1, 1]))
    
  def testSimpleDiscounts(self):
    self.assertEqual(8 * 2 * 0.95, prix([0, 1]))
    self.assertEqual(8 * 3 * 0.9, prix([0, 2, 4]))
    self.assertEqual(8 * 4 * 0.8, prix([0, 1, 2, 4]))
    self.assertEqual(8 * 5 * 0.75, prix([0, 1, 2, 3, 4]))
    
  def testSeveralDiscounts(self):
    self.assertEqual(8 + (8 * 2 * 0.95), prix([0, 0, 1]))
    self.assertEqual(2 * (8 * 2 * 0.95), prix([0, 0, 1, 1]))
    self.assertEqual((8 * 4 * 0.8) + (8 * 2 * 0.95), prix([0, 0, 1, 2, 2, 3]))
    self.assertEqual(8 + (8 * 5 * 0.75), prix([0, 1, 1, 2, 3, 4]))
    
  def testEdgeCases(self):
    self.assertEqual(2 * (8 * 4 * 0.8), prix([0, 0, 1, 1, 2, 2, 3, 4]))
    self.assertEqual(3 * (8 * 5 * 0.75) + 2 * (8 * 4 * 0.8), 
      prix([0, 0, 0, 0, 0, 
            1, 1, 1, 1, 1, 
            2, 2, 2, 2, 
            3, 3, 3, 3, 3, 
            4, 4, 4, 4]))

if __name__ == '__main__':
  unittest.main()
