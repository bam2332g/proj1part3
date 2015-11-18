"""
Columbia W4111 Intro to databases
Homework 2
Data Analysis and Relational Algebra
Eugene Wu 2015
Brandon Martinez 2015 - bam2189
"""




def main(file_path, year):
    import csv
    
    with open(file_path) as csvfile:
        reader = csv.DictReader(csvfile)
        c = 0
        #print type(reader)
        for row in reader:
#                print(type(row))
#                print(row)
#                print(type(row.get(None)[0]))                
            if((row.get(None)[0] == 'QB') or 
               (row.get(None)[0] == 'WR') or
               (row.get(None)[0] == 'TE') or
               (row.get(None)[0] == 'RB')):
                #is a list
#               print('hello')
#               print(row.get(None))
                pb_name = row.get(None)[1]
                output = (pb_name, year)
                with open("pb.txt", "a") as text_file:
                    text_file.write("{0}, {1}\n".format(*output))
   
    """
    @param data the output of load_data()
    @return the number of  distinct types of items (by `description` attribute) in this dataset
    """

if __name__ == '__main__':
    import sys
    print(sys.argv[1])
    year = sys.argv[2]
    main(sys.argv[1], year)

