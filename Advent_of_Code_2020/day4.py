"""
PSEUDOCODE
iterate over file
      fill the list with characters between space and ":"
      if
            if the list has 8 elements => valid
            if the lest has 7 elements and not cid => valid
      if you find 2 "\n" in a row, finish

NOTES
each field of the file is made up of 3 digits
field:data field:data ...
"""

def is_document_valid(document):
      """
      TAKES:
      document. A list, containing fields contained in the document
      RETURN:
      boolean, True if the document is valid
      
      EXECUTION:
      if the list has 8 elements => valid
      if the lest has 7 elements and not cid => valid
      """
      if len(document) == 8:
            return True
      elif len(document) == 7 and "cid" not in document:
            return True
      else:
            return False

filename = "day4.txt"
with open(filename, 'r') as file_pass:
      doc_list = []
      count = 0
      for line in file_pass:
            #check if I'm at the end of the document
            if line == '\n':
                  #print(doc_list)
                  #check if the document is valid
                  #print(is_document_valid(doc_list))
                  if is_document_valid(doc_list):
                        count += 1
                  doc_list = []
            else:
                  #slide document to count fields
                  for index, i in enumerate(line):
                        #start of the line: I've certainly a value
                        if index == 0:
                              #0 included, 3 excluded
                              doc_list.append(line[0: 3])
                        if i == ' ':
                              doc_list.append(line[index+1: index+4])
      #file reading ended before I finished, so I must read the last document
      if is_document_valid(doc_list):
            count += 1
            doc_list = []
      print(count)
