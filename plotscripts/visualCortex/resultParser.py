__author__ = 'jules'


import re
from collections import defaultdict
def parseResultFile(path):

    results = {}
    with open(path) as csv_file:
        rows = (re.split('[\t]+', line) for line in csv_file)
        fields = rows.next()[0].split()  # this is needed because the first line is separated with whitespaces and not tabs!
        for row in rows:
            object_name = row[3]
            time = float(row[1])
            value = float(row[5])
            attr_name = row[4]
            if not object_name in results :
                results[object_name] = defaultdict(list)
            results[object_name][attr_name].append( ( time, value) )
    return results