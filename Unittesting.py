#Program 1: Simplistic Test
##import unittest
##class SimplisticTest(unittest.TestCase):
##    def test(self):
##        a = 'a'
##        b = 'a'
##        self.assertEqual(a, b)
##if __name__=="__main__":
##    unittest.main()


#Program 2: Test for Error
##import unittest
##class TestCase1(unittest.TestCase):
##    def test_method(self):
##        assertEqual(2,1)
##if __name__=="__main__":
##    unittest.main()

#Program 3: Test for Fail
##import unittest
##class TestCase1(unittest.TestCase):
##    def test_method(self):
##        self.assertEqual(2,1)
##if __name__=="__main__":
##    unittest.main()

#Program 4: Test for OK
##import unittest
##class TestCase1(unittest.TestCase):
##    def test_method(self):
##        self.assertEqual(1,1)
##
##if __name__=="__main__":
##    unittest.main()

#Program 5: Test using Verbosity.
##import unittest
##class TestCase1(unittest.TestCase):
##    def test_method(self):
##        self.assertEqual(1,1)
##
##if __name__=="__main__":
##    unittest.main(verbosity=2)


#Program 6: Test using verboisity when the test fail; displaying the additional usefull error message.
##import unittest
##class TestCase1(unittest.TestCase):
##    def test_method(self):
##        self.assertEqual(1,2,"The given numbers are not equal")
##
##if __name__=="__main__":
##    unittest.main(verbosity=2)

#Program 7: Test by taking the user defined input to check the equality.
##import unittest
##class TestCase1(unittest.TestCase):
##    def test_method(self):
##        a=int(input( ))
##        b=int(input( ))
##        self.assertEqual(a,b,"The given numbers are not equal")
##
##if __name__=="__main__":
##    unittest.main(verbosity=2)


#Program 8: assertEqual/assertNotEqual/assertTrue/assertFalse/ assertLess

##import unittest
##
##class CheckNumbers(unittest.TestCase):
###test with status error
##    def test_int_float(self):
##        self.assertNotEqual(1,1.0)
###test with status pass
##    def test_str_float(self):
##        self.assertEqual(1,1.0)
##
##    def test_assert_true(self):
##        self.assertTrue((4+3)<0,"Not equal")
##
##    def test_assert_false(self):
##        self.assertFalse((4+3)<0)
##    def test_assert_false(self):
##        self.assertLess(4,3)
##
##if __name__=="__main__":
##    print(__name__)
##    unittest.main(verbosity=2)


#Program 9: Asserting Truth
##import unittest
##
##class TruthTest(unittest.TestCase):
##
##    def testAssertTrue(self):
##        self.assertTrue(True)
##
##    def testAssertFalse(self):
##        self.assertFalse(False)
##if __name__=="__main__":
##    #print(__name__)
##    unittest.main(verbosity=2)



#Program 10: Testing Equality
##import unittest
##
##class EqualityTest(unittest.TestCase):
##
##    def testExpectEqual(self):
##        self.assertEqual(1, 3 - 2)
##
##    def testExpectEqualFails(self):
##        self.assertEqual(2, 3 - 2)
##
##    def testExpectNotEqual(self):
##        self.assertNotEqual(2, 3 - 2)
##
##    def testExpectNotEqualFails(self):
##        self.assertNotEqual(1, 3 - 2)
##if __name__=="__main__":
##    #print(__name__)
##    unittest.main(verbosity=2)


#Program 11: Almost Equal
##import unittest
##
##class AlmostEqualTest(unittest.TestCase):
##
##    def testEqual(self):
##        self.assertEqual(1.1, 3.3 - 2.2)
##
##    def testAlmostEqual(self):
##        self.assertAlmostEqual(1.1, 3.3 - 2.2, places=1)
##
##    def testNotAlmostEqual(self):
##        self.assertNotAlmostEqual(1.1, 3.3 - 2.0, places=1)
##
##if __name__=="__main__":
##    #print(__name__)
##    unittest.main(verbosity=2)


#Program 12: Containers
##import textwrap
##import unittest
##
##
##class ContainerEqualityTest(unittest.TestCase):
##
##    def testCount(self):
##        self.assertCountEqual(
##            [1, 2, 3, 2],
##            [1, 3, 2, 3],
##        )
##
##    def testDict(self):
##        self.assertDictEqual(
##            {'a': 1, 'b': 2},
##            {'a': 1, 'b': 3},
##        )
##
##    def testList(self):
##        self.assertListEqual(
##            [1, 2, 3],
##            [1, 3, 2],
##        )
##
##    def testMultiLineString(self):
##        self.assertMultiLineEqual(
##            textwrap.dedent("""
##            This string
##            has more than one
##            line.
##            """),
##            textwrap.dedent("""
##            This string has
##            more than two
##            lines.
##            """),
##        )
##
##    def testSequence(self):
##        self.assertSequenceEqual(
##            [1, 2, 3],
##            [1, 3, 2],
##        )
##
##    def testSet(self):
##        self.assertSetEqual(
##            set([1, 2, 3]),
##            set([1, 3, 2, 4]),
##        )
##
##    def testTuple(self):
##        self.assertTupleEqual(
##            (1, 'a'),
##            (1, 'b'),
##        )
##
##if __name__=="__main__":
##    #print(__name__)
##    unittest.main(verbosity=2)



#Program 13: Containers membership
##import unittest
##class ContainerMembershipTest(unittest.TestCase):
##
##    def testDict(self):
##        self.assertIn(4, {1: 'a', 2: 'b', 3: 'c'})
##
##    def testList(self):
##        self.assertIn(4, [1, 2, 3])
##
##    def testSet(self):
##        self.assertIn(4, set([1, 2, 3]))
##
##if __name__=="__main__":
##    #print(__name__)
##    unittest.main(verbosity=2)


#Program 14: Skipping Tests (Usage of decorators “@”)
#The decorators skipIf() and skipUnless( ) can be used to check a condition before skipping.
#example 14: Skipping Tests

##import sys
##import unittest
##
##class SkippingTest(unittest.TestCase):
##
##    @unittest.skip('always skipped')
##    def test(self):
##        self.assertTrue(False)
##
##    @unittest.skipIf(sys.version_info[0] > 2,
##                     'only runs on python 2')
##    def test_python2_only(self):
##        self.assertTrue(False)
##
##    @unittest.skipUnless(sys.platform == 'Darwin',
##                         'only runs on macOS')
##    def test_macos_only(self):
##        self.assertTrue(True)
##
##    def test_raise_skiptest(self):
##        raise unittest.SkipTest('skipping via exception')
##
##if __name__=="__main__":
##    #print(__name__)
##    unittest.main(verbosity=2)


#Program 15: Simple Math Operations
#Developer code: mymath.py
##def add(a, b):
##    return a + b
## 
## 
##def subtract(a, b):
##    return a - b
## 
## 
##def multiply(a, b):
##    return a * b
## 
## 
##def divide(numerator, denominator):
##    return float(numerator) / denominator
####


##Testing Code: testing_mymath.py
##import mymath
##import unittest
## 
##class TestAdd(unittest.TestCase):
##    """
##    Test the add function from the mymath library
##    """
## 
##    def test_add_integers(self):
##        """
##        Test that the addition of two integers returns the correct total
##        """
##        result = mymath.add(1, 2)
##        self.assertEqual(result, 3)
## 
##    def test_add_floats(self):
##        """
##        Test that the addition of two floats returns the correct result
##        """
##        result = mymath.add(10.5, 2)
##        self.assertEqual(result, 12.5)
## 
##    def test_add_strings(self):
##        """
##        Test the addition of two strings returns the two string as one
##        concatenated string
##        """
##        result = mymath.add('abc', 'def')
##        self.assertEqual(result, 'abcdef')
## 
## 
##if __name__ == '__main__':
##    unittest.main()





















