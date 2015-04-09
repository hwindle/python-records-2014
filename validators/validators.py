#!/usr/bin/env python3

# -*- coding: UTF8 -*-

from PyQt4.QtCore import *
#from PyQt4.QtSql import *

class Validator():

    def __init__(self):
        """

        """
        super(Validator, self).__init__()


    def postcode(self, dirtyStr):
        """
        Checks whether dirtyStr is a valid postcode,
        
        Test:
        NE30 6QR 
        SR2 9TD 
        CA13 7PT 
        SE10 0BD
        WC2E 7DH
        """

        ukPostcodePat = QRegExp(r"^(?:(?:[A-PR-UWYZ][0-9]{1,2}|[A-PR-UWYZ][A-HK-Y][0-9]{1,2}|[A-PR-UWYZ][0-9][A-HJKSTUW]|[A-PR-UWYZ][A-HK-Y][0-9][ABEHMNPRV-Y]) [0-9][ABD-HJLNP-UW-Z]{2}|GIR 0AA)$")            
        """
        Splitting the above pattern up:
        The first group in between (?: (the inner group is for the 1st postcode half.
        The letters Q,V,X aren't used in the 1st letter, hence [A-PR-UWYZ]
        After the or symbol '|', we have the same pattern again 
        but for the second letter in a postcode, which doesn't have the letters I-K.
        A similar pattern appears a third time for dealing with London postcode districts.

        Second Portion (after the 1st subgroup and literal space):
        The only letters to appear in the 
        first letter of the second half are A, B, C, D, E, F, G, H, J, K, S, T, U and W.
        """
        if dirtyStr:
            dirty = str(dirtyStr)
            string = dirty.upper().strip() 
            if ukPostcodePat.exactMatch(string):
                return string
            else:
                return False
        else:
            return False


    def uk_landline(self, dirtyStr):
        """
        Checks whether dirtyStr is a UK landline phone number, like 0115 913 4284.

        Test:
        +44 (0113) 930 3040
        44 (0112) 903 2299
        +44 (0119) 9442329
        (0115) 930 2429
        (0115) 9302429
        0114 922 2019
        0113 9322018
        +44 208 896 5000
        0844 561 6789
        """
        ukLandlinePat = QRegExp(r"[+]?[44 ]*[(]?[0-9]{3,4}[)]? [0-9 ]{3,4}[0-9]{4}")
        if dirtyStr:
            dirty = str(dirtyStr)
            string = dirty.strip()
            if ukLandlinePat.exactMatch(string):
                return string
            else:
                return False
        return False        


    def uk_mobile_no(self, dirtyStr):
        """
        Checks whether dirtyStr is a UK mobile phone number.

        Test:
        07792 232445
        +44 7792 232445
        +44 07792 232445
        07434 249019
        07566 110293
        07624 109457 # Manx numbers
        07924 239192
        07911 385712 # wifi numbers 
        """
        ukMobilePat = QRegExp(r"[+]?[44 ]*[0-9]{4,5} [0-9]{6}")
        if dirtyStr:
            dirty = str(dirtyStr)
            string = dirty.strip()
            if ukMobilePat.exactMatch(string):
                return string
            else:
                return False
        return False


    def ni_number(self, dirtyStr):
        """
        Checks whether dirtyStr is a valid National Insurance number.

        Test:
        AH 384791 A
        JC 389721 B
        II 394741 A (invalid)
        TN 387111 E (invalid)
        NW 981234 D
        PL 378191 C 

        """
        niNumberPat = QRegExp(r"(?:(?:[^OO|CR|FY|MW|NC|PP|PZ|TN][A-C|E|G-H|J-P|R-T|W-Z]{1}[A-C|E|G-H|J-N|P|R-T|W-Z]{1}) [0-9]{6} [A-D]{1})") 
        # Prefix not in: OO CR FY MW NC PP PZ TN, suffix A-D only.
        if dirtyStr:
            dirty = str(dirtyStr)
            string = dirty.upper().strip()
            if niNumberPat.exactMatch(string):
                return string
            else:
                return False
        return False


    def credit_card_no(self, dirtyStr):
        """
        Checks whether dirtyStr is a valid credit card number.

        Test:
        1234 0000 5678 9123 (invalid)
        4099 4539 8920 3245 (Visa)
        5212 1029 9013 3487 (Mastercard)
        3470203781100189 (Amex)
        3470-2037-8110-0189 
        3681 1901 1245 2322 (Diners)
        3011 8913 2381 3891 (Diners or invalid)
        2131 1908 3104 3445 (JCB or invalid)
        """
        import re
        creditCardPat = QRegExp(r"[0-9]{16}")
        if dirtyStr:
            dirty = str(dirtyStr)
            string = dirty.strip()
            ''.join(re.split(r"[ -]", string))
            #print(string)
            if creditCardPat.exactMatch(string):
                if string[0:3] == "0000" or string[4:7] == "0000" or string[8:11] == "0000" or string[12:] == "0000":
                    return False
                return string
            else:
                return False
        return False


    def debit_card_no(self, dirtyStr):
        """
        Checks whether dirtyStr is a valid debit card number.

        Tests:
        0000 0000 0000 0000 (invalid)
        0801 2930 4455 1235 
        9018 4892 0118 3890
        """
        debitCardPat = QRegExp(r"[0-9]{16}")
        if dirtyStr:
            dirty = str(dirtyStr)
            spacedStr = dirty.strip()
            string = spacedStr.replace(" ", "")
            if debitCardPat.exactMatch(string):
                if string[0:3] == "0000" or string[4:7] == "0000" or string[8:11] == "0000" or string[12:] == "0000":
                    return False
                return string
            else:
                return False
        return False


    def sort_code_no(self, dirtyStr):
        """
        Checks whether dirtyStr is a valid bank sort code.
 
        Tests:
        3901231 (too long)
        55-33-09 
        34 31 11 
        45019 (too short)
        456798
        """
        sortCodePat = QRegExp(r"\d{6}|(\d{2}[- ]?){2}\d{2}")
        if dirtyStr:
            dirty = str(dirtyStr)
            string = dirty.strip()
            if sortCodePat.exactMatch(string):
                return string
            else:
                return False
        return False
  

    def bank_account_no(self, dirtyStr):
        """
        Checks whether dirtyStr is an 8 digit bank account number.

        Tests:
        0000 1111 (invalid)
        471034901 (too long)
        80141 (too short)
        2567 1901
        2589 0019 
        45911090
        9011-3892
        """
        bankAccountPat = QRegExp(r"[1-9]{1}\d{3}[ ]?\d{4}")
        if dirtyStr:
            dirty = str(dirtyStr)
            spacedStr = dirty.strip()
            string = spacedStr.replace("-", "")
            if bankAccountPat.exactMatch(string):
                return string
            else:
                return False
        return False


    def sci_number(self, dirtyStr):
        """
        Checks whether the dirtyStr string is a scientific number.

        Tests: 
        5.3421 e-02
        2×10e0
        3×10e2
        4.321768×10e3
        −5.3×10e4
        6.72×10e9
        2×10e−1
        7.51×10e−9
        """
        sciNumberPat = QRegExp(r"[-|+]?[0-9]{1}[.]?[0-9]{0,12}[ x*]*[e|E|10e|10E|10^].[-|+]?[0-9]*")
        if dirtyStr:
            dirty = str(dirtyStr)
            string = dirty.strip()
            if sciNumberPat.exactMatch(string):
                return string
            else:
                return False
        return False


    def isbn_number(self, dirtyStr):
        """
        Checks whether the dirtyStr is a isbn book number.

        Tests:
        9788175257665
        9780306406157
        978-0-306-40615-7

        Checksum:
        For example, the ISBN-13 check digit of 978-0-306-40615-? is calculated as follows:
        s = 9×1 + 7×3 + 8×1 + 0×3 + 3×1 + 0×3 + 6×1 + 4×3 + 0×1 + 6×3 + 1×1 + 5×3
        =   9 +  21 +   8 +   0 +   3 +   0 +   6 +  12 +   0 +  18 +   1 +  15
        = 93
        93 / 10 = 9 remainder 3
        10 –  3 = 7
        """
        isbnPat = QRegExp(r"\d{13}")
        if dirtyStr:
            dirty = str(dirtyStr)
            string = dirty.strip().replace("-", "")
            if isbnPat.exactMatch(string):
                lastNum = string[:-1] 
                for char in string:
                    i = 0
                    if (i % 2) != 0:
                        times = 3
                    else:
                        times = 1
                    isbnlist = []
                    isbnlist.append( int(char) * times )
                    i += 1
                for num in isbnlist:
                    isbnTotal += num
                checksum = 10 - (isbnTotal % 10)   
                if checksum == lastNum:
                    return string
                else:
                    return False
        return False              # no string entered


    def social_security_no(self, dirtyStr):
        """
        checks whether the string is a valid US social security number.

        Tests:
        000-45-9817 (invalid)
        123-00-9102 (invalid)
        124-90-0000 (invalid)
        666 or 900-999 in the first group invalid
        078-05-1120 (invalid)
        890-12-9801
        555-90-2356
        """
        socialPat = QRegExp(r"(?:[^000|666|900-999][0-9]{3})[-]?(?:[^00][0-9]{2})[-]?(?:[^0000][0-9]{4})") 
        if dirtyStr:
            dirty = str(dirtyStr)
            string = dirty.strip()
            if string.replace("-", "") == "078051120":
                return False          # Woolworths social security no.
            elif socialPat.exactMatch(string):
                return string
        return False


    def zip_codes(self, dirtyStr):
        """
        Checks whether the string is a valid US zip code.

        Tests:
        11029
        90192
        08690
        32311
        280112 (invalid)
        2981 (invalid)
        """
        zipCodePat = QRegExp(r"\d{5}")
        if dirtyStr:
            dirty = str(dirtyStr)
            string = dirty.strip()
            if zipCodePat.exactMatch(string):
                return string
            else:
                return False
        return False


    def website(self, dirtyStr):
        """
        Checks whether dirtyStr is a valid website address.
    
        Tests:
        yell.com
        www.yell.com
        ww.mysite.com (invalid)
        www.something.de
        http://www.bbc.com
        https://www.abank.co.uk
        ftp://weird.things.edu
        forum.somesite.com
        """
        websitePat = QRegExp(r"(?:[http://|https://|ftp://]+)[www.]?[a-z0-9]+[.]?[a-z0-9]+[/?=.a-z]+")
        if dirtyStr:
            dirty = str(dirtyStr)
            if "http" or "ftp" not in dirty:
                clean1 = dirty.lower().strip()
                clean2 = clean1.replace("ww.", "www.")
                string = "http://" + clean2
            if websitePat.exactMatch(string):
                return string
            else:
                return False
        return False


    def file_path(self, dirtyStr):
        """
        Checks whether dirtyStr is a file path.

        Tests:
        c:\Windows\Wallpaper\file1.jpg
        Z:\Documents and settings\Ray\somefile.doc
        D:\Music\Pearl Jam\
        /usr/share/wallpaper/file1.jpg
        /home/ray/somefile.doc
        /mnt/cdrom/Music/Pearl Jam
        """
        import os
        if dirtyStr:
            dirty = str(dirtyStr)
            string = dirty.strip()
        else:
            return False
        if os.path.isdir(string) or os.path.isfile(string):
            return string
        else:
            return False


    def email_address(self, dirtyStr):
        """
        Checks for a valid email address

        Tests:
        me@example.com
        regex@comp.sci.edu
        @something (invalid)
        two19@hotmail.co.uk
        bar.ba@test.co.uk
        notanemailaddress (invalid)
        """
        emailAddressPat = QRegExp(r"[a-z0-9.-_].*@[a-z0-9-_].*[.a-z]+")
        if dirtyStr:
            dirty = str(dirtyStr)
            string = dirty.strip().lower()
            if emailAddressPat.exactMatch(string):
                return string
            else:
                return False
        return False


