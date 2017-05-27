import os, re

def kill_old_tables(c_list, tablespath):
    if c_list and tablespath:
        
        c_html_list = []

        for classname in c_list:
            c_html_list.append(classname + '.html')
        
        all_list = []
        for i in range(0, len(os.listdir(tablespath))):
            if re.search("[a-zA-Z]+[0-9]+.html", os.listdir(tablespath)[i]):
                name = os.listdir(tablespath)[i]
            all_list.append(name)
        
        del_set = set(all_list) - set(c_html_list)
        for del_html in del_set:
            os.remove(tablespath + del_html)
        
        
    else:
        print('error message: null value')