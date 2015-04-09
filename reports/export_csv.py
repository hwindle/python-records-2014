#!/usr/bin/env python3

# -*- coding: UTF8 -*-

"""
/********************************************************
* Records - an easy to use database client, opens sqlite3 databases. 
* You can also search, create queries and reports easily.
* Part of Paradise Office
* Copyright (c) Hazel Windle
* 
*
* This program is free  software; you can redistribute it and/or
* modify it under the terms of the GNU General Public License
* as published by the Free Software Foundation; either version 2
* of the License, or (at your option) any later version.
*
* This program is distributed in the hope that it will be useful,
* but WITHOUT ANY WARRANTY; without even the implied warranty of
* MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
* GNU General Public License for more details.
*
* You should have received a copy of the GNU General Public License
* along with this program; if not, write to the Free Software
* Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
* Also add information on how to contact you by electronic and paper mail.
*
**********************************************************/
"""

import csv

def export_csv(table, result_set, delimiter='|'):
    """
    Takes in a results set from the sql/select_query function.
    Each record is a list within a list.
    """
    csvname = table + ".csv"
    allowed_del = (":", "|", "\t", " ")
    if delimiter not in allowed_del:
        return False
    with open(csvname, "w", newline="\n") as filehandle:
        writeout = csv.writer(filehandle, delimiter=delimiter, quotechar='"', quoting=csv.QUOTE_MINIMAL)
        i = 0
        rowcount = len(result_set)
        while i < rowcount:
            writeout.writerow(result_set[i])
            i += 1
        return csvname
