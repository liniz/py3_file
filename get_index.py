import os
import re
import datetime

from bs4 import BeautifulSoup

def get_index(tablespath):
    
    with open('/var/www/html/index.html', 'w', encoding = 'utf-8') as f_2:
        with open('/py3_file/template_0.html', encoding = 'utf-8') as f_1:
            f_2.write(f_1.read())
        f_2.write('index')
        f_2.write('</title>')
        f_2.write("""<!-- Latest compiled and minified CSS -->
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">

        <!-- Optional theme -->
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap-theme.min.css" integrity="sha384-rHyoN1iRsVXV4nD0JutlnGaslCJuC7uwjduW9SVrLvRYooPp2bWYgmgJQIXwl/Sp" crossorigin="anonymous">""")
        f_2.write('</head>')
        f_2.write('<body>')
        f_2.write('<h1>')
        f_2.write('timetables of iii')
        f_2.write('</h1>')
        f_2.write(' | ')
        for i in range(0, len(os.listdir(tablespath))):
            if re.search("[a-zA-Z]+[0-9]+.html", os.listdir(tablespath)[i]):
                name = os.listdir(tablespath)[i]
                f_2.write('<a href="./tables/' + name + '">' + name.replace('.html', '') + '</a> | ')
        f_2.write('last update: ' + datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S'))
        f_2.write(' | ')
        f_2.write('</body>')
        f_2.write('</html>')