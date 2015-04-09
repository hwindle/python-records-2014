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

import os

install_dir = os.path.abspath(".")

def update_css(theme, header="html5"):
    css_path = install_dir + "/web_assets/css/"
    # save the different file names for css files to a list
    css_themes = []
    css_themes = os.listdir(css_path)
    css_themes.sort()
    if not theme:
        print("No CSS theme picked")
        return False
    theme = int(theme)
    #print(css_themes)
    # each int passed in corresponds to a theme... as I may change the them
    # e names in the UI
    theme_chosen = css_path + css_themes[theme - 1]
    try:
        css_file = open(theme_chosen, mode="r", encoding="utf-8")
    except IOError as e:
        print("Css can't be opened\n")
    # css_line = "<link rel='stylesheet' type='text/css' href='" + theme_chosen + "' />\n"
    htmltop = "<!DOCTYPE html>\n<html lang='en'>\n<head>\n<meta charset='utf-8'>\n<title>Database Report</title>\n<meta name='viewport' content='width=device-width, initial-scale=1, maximum-scale=1' />\n"
    if "html5" in header:
        with open(install_dir + "/reports/html/html5_skel_top.html", "w", encoding="utf-8") as fw:
            fw.write(htmltop)
            fw.write("<style type='text/css'>\n")
            fw.write(css_file.read())
            fw.write("</style>\n")
            fw.close()
    return True



def update_js(script, header="html5"):
    js_path = install_dir + "/web_assets/js/"
    scripts_list = []
    scripts_list = os.listdir(js_path)
    scripts_list.sort()
    if not script:
        print("You forgot a script number!")
        return False
    script = int(script)
    print(scripts_list)
    script_chosen = js_path + scripts_list[script - 1]
    try:
        js_file = open(script_chosen, mode="r", encoding="utf-8")
    except IOError as e:
        print("Javascript file can't be opened... \n")
    #js_line = "<script type='text/javascript' src='" + script_chosen + "'></script>\n"
    js_includes = "<script type='text/JavaScript' src='http://ajax.googleapis.com/ajax/libs/jquery/1.11.2/jquery.min.js'></script>\n<script type='text/javascript' src='http://d3js.org/d3.v3.min.js' charset='utf-8'></script>\n"
    if "html5" in header:
        with open(install_dir + "/reports/html/html5_skel_top.html", "a", encoding="utf-8") as fw:
            fw.write(js_includes)
            fw.write("\n<script type='text/javascript'>\n")
            fw.write(js_file.read())
            fw.write("\n</script>\n")
            fw.close()
    return True


if __name__ == "__main__":
    update_css(1)
    update_js(1)


