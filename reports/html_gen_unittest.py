#!/usr/bin/env python3

# -*- coding: UTF8 -*-

import html_generator
import unittest

class HtmlGeneratorTests(unittest.TestCase):

    def setUp(self):
        title1 = "1 Item Test"
        title2 = "Several Items Test"
        result_set1 = [[1, "Something", "Co-Op", "Blue", "Clothes", "10.99"]]
        result_set2 = [[1, "Intel I7", "Amazon", "", "IT", "246.90"],
                       [2, "32GB DDR3 1866mhz RAM", "Amazon", "red", "IT", "200.00" ],
                       [3, "Asus socket 1150 motherboard", "Amazon", "green", "IT", "80.00" ],
                       [4, "water cooling kit Coolermaster", "Amazon", "", "IT", "123.86" ],
                       [5, "SanDisk extreme SSD 256GB", "Amazon", "", "IT", "105.86" ],
                       [6, "Western Digital 2TB HDD", "Amazon", "silver", "IT", "75.96" ],
                       [7, "Samsung blu-ray drive", "Amazon", "black", "IT", "60.00" ],
                       [8, "Antec modular 800w PSU", "Amazon", "black", "IT", "100.00" ],
                       [9, "3.5 IcyBox card reader", "Amazon", "black", "IT", "30.00" ],
                       [10, "Coolermaster black ATX case", "Amazon", "black", "IT", "40.00" ],
                       [11, "AMD 7900 graphics card", "Amazon", "", "IT", "100.00" ],
                       [12, "Antec fan controller 5.25\"", "Amazon", "black", "IT", "25.99" ]]
        fieldnames = ["id", "Item", "Store", "Colour", "Category", "Price"]              
        self.returned1 = html_generator.tabular_html(title1, result_set1, fieldnames)
        self.returned2 = html_generator.tabular_html(title2, result_set2, fieldnames)


    def testTabular1(self):
        testhtml = """
        <header>
        <h1>1 Item Test</h1>
        </header>
        <table>
        <thead><th>id</th>
        <th>Item</th>
        <th>Store</th>
        <th>Colour</th>
        <th>Category</th>
        <th>Price</th>
        
        </thead>
        <tbody>
        <tr>
        <td>1</td><td>Something</td><td>Co-Op</td><td>Blue</td><td>Clothes</td><td>10.99</td>
        </tr>
        </tbody>
        </table>
        """
        pass
        #self.assertEqual(testhtml, self.returned1)


    def testTabular2(self):
        testhtml = """
        <header>
        <h1>1 Item Test</h1>
        </header>
        <table>
        <thead><th>id</th>
        <th>Item</th>
        <th>Store</th>
        <th>Colour</th>
        <th>Category</th>
        <th>Price</th>
        
        </thead>
        <tbody>
        <tr>
        <td>1</td><td>Intel I7</td><td>Amazon</td><td></td><td>IT</td><td>246.90</td>
        </tr>
        <tr>
        <td>2</td><td>32GB DDR3 1866mhz RAM</td><td>Amazon</td><td>red</td><td>IT</td><td>200.00</td>
        </tr>
        <tr>
        <td>3</td><td>Asus socket 1150 motherboard</td><td>Amazon</td><td>green</td><td>IT</td><td>80.00</td>
        </tr>
        <tr>
        <td>4</td><td>water cooling kit Coolermaster</td><td>Amazon</td><td></td><td>IT</td><td>123.86</td>
        </tr>
        <tr>
        <td>5</td><td>SanDisk extreme SSD 256GB</td><td>Amazon</td><td></td><td>IT</td><td>105.86</td>
        </tr>
        <tr>
        <td>6</td><td>Western Digital 2TB HDD</td><td>Amazon</td><td>silver</td><td>IT</td><td>75.96</td>
        </tr>
        <tr>
        <td>7</td><td>Samsung blu-ray drive</td><td>Amazon</td><td>black</td><td>IT</td><td>60.00</td>
        </tr>
        <tr>
        <td>8</td><td>Antec modular 800w PSU</td><td>Amazon</td><td>black</td><td>IT</td><td>100.00</td>
        </tr>
        <tr>
        <td>9</td><td>3.5 IcyBox card reader</td><td>Amazon</td><td>black</td><td>IT</td><td>30.00</td>
        </tr>
        <tr>
        <td>10</td><td>Coolermaster black ATX case</td><td>Amazon</td><td>black</td><td>IT</td><td>40.00</td>
        </tr>
        <tr>
        <td>11</td><td>AMD 7900 graphics card</td><td>Amazon</td><td></td><td>IT</td><td>100.00</td>
        </tr>
        <tr>
        <td>12</td><td>Antec fan controller 5.25"</td><td>Amazon</td><td>black</td><td>IT</td><td>25.99</td>
        </tr>
        </tbody>
        </table>
        """
        #self.assertEqual(testhtml, self.returned2)
        if html_generator.construct_page("testnamereport.html", self.returned2):
            print("A report is born...")
        else:
            print("an error.. no report")


if  __name__ == "__main__":
    unittest.main()

 
