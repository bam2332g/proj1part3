"""
Columbia W4111 Intro to databases
Homework 2
Data Analysis and Relational Algebra
Eugene Wu 2015
Brandon Martinez 2015 - bam2189
"""




def main(file_path):
    import csv
    
    with open(file_path) as csvfile:
        reader = csv.DictReader(csvfile)
        c = 0
        #print type(reader)
        for row in reader:
#                print(type(row))
#                print(row)
#                print(type(row.get(None)[0]))                
            if((row.get(None)[3] == 'QB') or 
               (row.get(None)[3] == 'qb') or
               (row.get(None)[3] == 'WR') or
               (row.get(None)[3] == 'wr') or
               (row.get(None)[3] == 'TE') or
               (row.get(None)[3] == 'te') or
               (row.get(None)[3] == 'RB') or
               (row.get(None)[3] == 'rb')):
                #is a list
#               print('hello')
#               print(row.get(None))
                sb_name = row.get(None)[1]
                #output = (pb_name, year)
                with open("sb.txt", "a") as text_file:
                    #text_file.write("{0}, {1}\n".format(*output))
                    text_file.write("{0}\n".format(sb_name))
   
    """
    @param data the output of load_data()
    @return the number of  distinct types of items (by `description` attribute) in this dataset
    """

if __name__ == '__main__':
    import sys
    print(sys.argv[1])
    #year = sys.argv[2]
    #main(sys.argv[1], year)
    main(sys.argv[1])

