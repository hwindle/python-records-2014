#!/usr/bin/env python3

import os

def tabular_html(title, result_set, fieldnames):
    """
    Title could be a table name or query name - or whatever the user wants to call it.

    The result set is from the select_sql list of lists, with row 2 field 1 being accessed 
    as: result_set[1][0] 
    """
    # check for a title
    if not title:
        print("No title!")
        return False
    # set heading html up.
    heading = ""
    heading += "\n</head>\n<body>\n\n<header>\n<h1>" + title + "</h1>\n</header>\n"
    tablestart = ""
    tablestart += "<table>\n<thead>"
    # get the fieldnames from small function in sql directory
    for i in range(len(fieldnames)):
        tablestart += "<th>" + fieldnames[i] + "</th>\n"
    tablestart += "\n</thead>\n<tbody>"
    # two nested loops going through the results set 2d array
    tablerows = ""
    for row in result_set:
        tablerows += "\n<tr>\n"
        for field in row:
            tablerows += "<td>" + str(field) + "</td>"
        tablerows += "\n</tr>"
    # end of table
    tableend = "\n</tbody>\n</table>\n"
    wholehtml = ""
    wholehtml += heading + tablestart + tablerows + tableend
    return wholehtml


def construct_page(filename, middledata, skel="HTML5"):
    install_dir = os.path.abspath(".") + "/reports/"
    if skel == "xhtml":
        skeltop = open(install_dir + "html/xhtml_skel_top.html", mode="r", encoding="utf-8")
        skelbtm = open(install_dir + "html/xhtml_skel_btm.html", mode="r", encoding="utf-8")
    else:
        skeltop = open(install_dir + "html/html5_skel_top.html", mode="r", encoding="utf-8")
        skelbtm = open(install_dir + "html/html5_skel_btm.html", mode="r", encoding="utf-8") 
    # make sure the filename/path is valid
    if not ".html" in filename: 
        filename += ".html"
    if not filename: filename = "testreport.html"

    try:
        with open(filename, mode="w", encoding="utf-8") as outfile:
            outfile.write(skeltop.read())
            outfile.write(middledata)
            outfile.write(skelbtm.read())
            #print("Finished writing")
    except IOError as e:
        print("Writing the HTML reports file has failed I'm afraid.")
    finally:
        skeltop.close()
        skelbtm.close()
        outfile.close()
        print("Closed things")
        # html5_skel_top.html fiddled about with by another small Python script to change CSS and JS prettiness selections.
