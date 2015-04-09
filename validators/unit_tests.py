#!/usr/bin/env python3

# -*- coding: UTF8 -*-

import validators
import unittest

class ValidatorTests(unittest.TestCase):

     def setUp(self):
         self.check = validators.Validator()
         #result = self.postcodeTest()
         #print("Postcodes: ", result)
         #result = self.ukLandlineTest
         #print("UK Landline telephone: ", result)
         

     def testPostcode(self):
         testInputs = ["NE30 6QR", 
                       "de7 5de  ", 
                       "SR2 9TD", 
                       "CA13 7PT",
                       "SE10 0BD",
                       "WC2E 7DH",
                       "",
                       "7unweus" ] # Test cases
         correctOutputs = ["NE30 6QR",
                           "DE7 5DE",
                           "SR2 9TD",
                           "CA13 7PT",
                           "SE10 0BD",
                           "WC2E 7DH",
                           False,
                           False ] # Correct outputs
         testValues = [] # output from the postcode checker
         for i in range(len(testInputs)):
             testValues.append(self.check.postcode(testInputs[i]))
             self.assertEqual(testValues[i], correctOutputs[i])


     def testUKLandline(self):
         testInputs = ["+44 (0113) 930 3040",
                      "44 (0112) 903 2299",
                      "+44 (0119) 9442329",
                      "(0115) 930 2429",
                      "(0115) 9302429",
                      "0114 922 2019",
                      "0113 9322018",
                      "+44 208 896 5000",
                      "0844 561 6789",
                      " ",
                      "telephone"] # test cases
         correctOutputs = ["+44 (0113) 930 3040",
                          "44 (0112) 903 2299",
                          "+44 (0119) 9442329",
                          "(0115) 930 2429", 
                          "(0115) 9302429",
                          "0114 922 2019",
                          "0113 9322018",
                          "+44 208 896 5000",
                          "0844 561 6789",
                          False,
                          False] # correct outputs
         testValues = [] # output from landline no checker
         for i in range(len(testInputs)):
             testValues.append(self.check.uk_landline(testInputs[i]))
             self.assertEqual(testValues[i], correctOutputs[i])


     def testMobileNumber(self):
         testInputs = ["07792 232445",
                       "+44 7792 232445",
                       "+44 07792 232445",
                       "07434 249019",
                       "07566 110293",
                       "07624 109457",
                       "07924 239192",
                       "07911 385712",
                       " ",
                       "fieoha"] # test cases
         correctOutputs = ["07792 232445",
                           "+44 7792 232445",
                           "+44 07792 232445",
                           "07434 249019",
                           "07566 110293",
                           "07624 109457",
                           "07924 239192",
                           "07911 385712",
                           False,
                           False] # correct outputs
         testValues = [] # output from mobile no checker
         for i in range(len(testInputs)):
             testValues.append(self.check.uk_mobile_no(testInputs[i]))
             self.assertEqual(testValues[i], correctOutputs[i])


     def testNINumber(self):
         testInputs = ["AC 384791 A",
                       "JC 389721 B",
                       "NW 981234 D",
                       "PL 378191 C",
                       "pl 378191 c",
                       "II 394741 A",
                       "TN 387111 E",
                       "33 320981 3",
                       " "] # test cases
         correctOutputs = ["AC 384791 A",
                           "JC 389721 B",
                           "NW 981234 D",
                           "PL 378191 C",
                           "PL 378191 C",
                           False,
                           False,
                           False,
                           False] 
         testValues = [] # output from the NI No checker
         for i in range(len(testInputs)):
             testValues.append(self.check.ni_number(testInputs[i]))
             self.assertEqual(testValues[i], correctOutputs[i])


     def testCreditCard(self):
         testInputs = ["4199 4539 8920 3245",
                       "5212 1029 9013 3487",
                       "3470203781100189",
                       "3470-2037-8110-0189",
                       "3681 1901 1245 2322",
                       "2131 1908 3104 3445",
                       "1234 0000 5678 9123",
                       "",
                       "hello"] # test cases
         correctOutputs = ["4199453989203245",
                           "5212102990133487",
                           "3470203781100189",
                           "3470203781100189",
                           "3681190112452322",
                           "2131190831043445",
                           False,
                           False,
                           False]
         testValues = [] # output from the function to test
         for i in range(len(testInputs)):
             testValues.append(self.check.credit_card_no(testInputs[i]))
             self.assertEqual(testValues[i], correctOutputs[i])


     def testDebitCard(self):
         testInputs = ["9801 2930 4455 1235",
                       "9018 4892 0118 3890",
                       "0000 0000 0000 0000",
                       " ",
                       "tuierray"] # test cases
         correctOutputs = ["9801293044551235",
                           "9018489201183890",
                           False,
                           False,
                           False]
         testValues = [] # output from the function to test        
         for i in range(len(testInputs)):
             testValues.append(self.check.debit_card_no(testInputs[i]))
             self.assertEqual(testValues[i], correctOutputs[i])


     def testSortCode(self):
         testInputs = ["3901231", "45019",
                       "55-33-09", "34 31 11",
                       "456798"] # test cases
         correctOutputs = [False, False,
                           "55-33-09", "34 31 11",
                           "456798"]
         testValues = [] # output from the function to test
         for i in range(len(testInputs)):
             testValues.append(self.check.sort_code_no(testInputs[i]))
             self.assertEqual(testValues[i], correctOutputs[i])
     

     def testBankAccount(self): 
         testInputs = ["2567 1901", "2589 0019",
                       "45911090",  "9011-3892",
                       "0000 1111", "471034901",
                       "80141"] # test cases
         correctOutputs = ["2567 1901", "2589 0019",
                           "45911090",  "90113892",
                           False, False, False]
         testValues = [] # output from the function to test
         for i in range(len(testInputs)):
             testValues.append(self.check.bank_account_no(testInputs[i]))
             self.assertEqual(testValues[i], correctOutputs[i])


     def testSciNumber(self):
         testInputs = ["5.3421 e-02", "3x10e2",
                       "3 x 10 e2", "4.321768 x 10e3",
                       "-5.3x10e4", "6.72x10e9", 
                       "2 x 10e-1", "7.51 x 10e-9",
                       "hello", ""] # test cases
         correctOutputs = ["5.3421 e-02", "3x10e2",
                           "3 x 10 e2", "4.321768 x 10e3", 
                           "-5.3x10e4", "6.72x10e9",
                           "2 x 10e-1", "7.51 x 10e-9",
                           False, False]
         testValues = [] # output from the function to test
         for i in range(len(testInputs)):
             testValues.append(self.check.sci_number(testInputs[i]))
             self.assertEqual(testValues[i], correctOutputs[i])


     def testISBNNumber(self):
         testInputs = [
                       "9780306406157",
                       "978-0-306-40615-7"] # test cases
         correctOutputs = [
                           "9780306406157",
                           "9780306406157"]
         testValues = [] # output from the function to test
         for i in range(len(testInputs)):
             testValues.append(self.check.isbn_number(testInputs))
             self.assertEqual(testValues[i], correctOutputs[i])


     def testSocialSecurity(self):
         testInputs = [
                       "890-12-9801",
                       "555-90-2356",
                       "666-10-9012",
                       "078-05-1120",
                       "000-45-9817",
                       "123-00-9102",
                       "124-90-0000"] # test cases
         correctOutputs = [ "890-12-9801",
                           "555-90-2356", False,
                           False, False, False,
                           False]
         testValues = [] # output from the function to test
         for i in range(len(testInputs)):
             testValues.append(self.check.social_security_no(testInputs))
             self.assertEqual(testValues[i], correctOutputs[i])


     def testZipCode(self):
         testInputs = ["90192",
                       "08690", "32311",
                       "280112", "2981"] # test cases
         correctOutputs = ["90192",
                           "08690", "32311",
                           False, False]
         testValues = [] # output from the function to test
         for i in range(len(testInputs)):
             testValues.append(self.check.zip_codes(testInputs))
             self.assertEqual(testValues[i], correctOutputs[i])


     def testWebsite(self):
         testInputs = [
                       "www.yell.com",
                       "ww.mysite.com",
                       "www.something.de",
                       "http://www.bbc.com",
                       "https://www.abank.co.uk",
                       "ftp://weird.things.edu",
                       "forum.somesite.com",
                       " ",
                       "3749081274"] # test cases
         correctOutputs = ["http://www.yell.com",
                           "http://www.something.de",
                           "http://www.bbc.com",
                           "https://www.abank.co.uk",
                           "ftp://weird.things.edu",
                           "http://forum.somesite.com",
                           False, False]
         testValues = [] # output from the function to test
         for i in range(len(testInputs)):
             testValues.append(self.check.website(testInputs))
             self.assertEqual(testValues[i], correctOutputs[i])


     def testFilePath(self):
         testInputs = [
                       "Z:\Documents and settings\Ray\somefile.doc",
                       "D:\Music\Pearl Jam",
                       "/usr/share/wallpaper/file1.jpg",
                       "/home/ray/somefile.doc",
                       "/mnt/cdrom/Music/Pearl Jam", " ", "238947 "] # test cases
         correctOutputs = [
                           "Z:\Documents and settings\Ray\somefile.doc",
                           "D:\Music\Pearl Jam",
                           "/usr/share/wallpaper/file1.jpg",
                           "/home/ray/somefile.doc",
                           "/mnt/cdrom/Music/Pearl Jam", 
                           False, False]
         testValues = [] # output from the function to test
         for i in range(len(testInputs)):
             testValues.append(self.check.file_path(testInputs))
             self.assertEqual(testValues[i], correctOutputs[i])


     def testEmailAddress(self):
         testInputs = ["regex@comp.sci.edu",
                       "two19@hotmail.co.uk  ", "bar.ba@test.co.uk",
                       "@something", "notanemailaddress", "first_second@linux-paradise.co.uk"]
         correctOutputs = ["regex@comp.sci.edu",
                           "two19@hotmail.co.uk", "bar.ba@test.co.uk",
                           False, False, "first_second@linux-paradise.co.uk"]
         testValues = [] 
         for i in range(len(testInputs)):
             testValues.append(self.check.email_address(testInputs))
             self.assertEqual(testValues[i], correctOutputs[i])



if __name__ == '__main__':    
    unittest.main()
