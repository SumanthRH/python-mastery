from sol_7_3.stock import Stock
import unittest

class TestStock(unittest.TestCase):
    def test_create(self):
        s = Stock("GOOG", 100, 49.1)
        self.assertEqual(s.name, "GOOG")
        self.assertEqual(s.shares, 100)
        self.assertEqual(s.price, 49.1)
    def test_create_keyword(self):
        s = Stock(name="GOOG", shares=100, price=49.1)
        self.assertEqual(s.name, "GOOG")
        self.assertEqual(s.shares, 100)
        self.assertEqual(s.price, 49.1)
    
    def test_cost(self):
        s = Stock("GOOG", 100, 49.1)
        cost = s.cost
        self.assertEqual(cost, s.shares * s.price)
    
    def test_sell(self):
        s = Stock("GOOG", 100, 49.1)
        s.sell(10)
        self.assertEqual(s.shares, 90)
    
    def test_from_row(self):
        row = ["GOOG", "100", "49.1"]
        s = Stock.from_row(row)
        self.assertEqual(s.name, "GOOG")
        self.assertEqual(s.shares, 100)
        self.assertEqual(s.price, 49.1)
    
    def test_repr(self):
        s = Stock("GOOG", 100, 49.1954)
        s_repr = repr(s)
        self.assertEqual(s_repr, "Stock('GOOG', 100, 49.195)")

    def test_eq(self):
        a = Stock("GOOG", 100, 49.1954)
        b = Stock("GOOG", 100, 49.1954)
        c = Stock("GOOG", 120, 49.1954)
        d = Stock("GOG", 100, 49.1954)
        e = Stock("GOOG", 100, 49.1)
        self.assertTrue(a == b)
        for var in [c, d, e]:
            self.assertFalse(b == var)
    
    def test_bad_shares(self):
        s = Stock('GOOG', 100, 490.1)
        with self.assertRaises(TypeError):
            s.shares = '50'
        with self.assertRaises(ValueError):
            s.shares = -10
    
    def test_bad_price(self):
        s = Stock('GOOG', 100, 490.1)
        with self.assertRaises(TypeError):
            s.price = '50'
        with self.assertRaises(ValueError):
            s.price = -10.0

    def test_missing_attr(self):
        s = Stock('GOOG', 100, 490.1)
        with self.assertRaises(AttributeError):
            s.share = 10

if __name__ == "__main__":
    unittest.main()