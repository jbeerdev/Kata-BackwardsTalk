'''
Created on 14/12/2010

@author: jose
'''
import unittest
from numpy.ma.testutils import assert_equal


class Test(unittest.TestCase):

    def setUp(self):
        pass


    def tearDown(self):
        pass

    def testBackwardsTalkWithFrogtekWord(self):
        input = "Frogtek"
        expected_output = "ketgorF"      
        assert_equal(backwardsTalk(input),expected_output)
        
        
    def testBackwardsTalkWithCompositeWords2NoSabes(self):
        input = "No sabes"
        expected_output = "sebas oN"       
        assert_equal(backwardsTalk(input),expected_output) 
        
    def testBackwardsTalkWithCompositeWordsChanante(self):
        input = "No te digo na y te lo digo to"
        expected_output = "ot ogid ol et y an ogid et oN"       
        assert_equal(backwardsTalk(input),expected_output)   
  
def backwardsTalk(input):
    
    reverse_value = ""
    char_list = []
        
    for chars in input:
        char_list.append(chars)
    
    char_list.reverse()   
        
    for reversed_chars in char_list:
        reverse_value = reverse_value+reversed_chars
    
    return reverse_value

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()