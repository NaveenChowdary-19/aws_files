import csv
'''with open('Naveen-Python/Names.csv','r') as csv_file:
    csv_reader=csv.reader(csv_file)
    
    for line in csv_reader:
        print(line)

-------------------    
o/p ===   ['Naveen', 'Chowdary', 'Naveen@fgg.com']
['Ragh', 'Thiru', 'GGff@hhgh.com']
['Shiv', 'chowd', 'Shihjhg@hg.com']

'''




'''with open('Naveen-Python/Names.csv','r') as csv_file:
    csv_reader=csv.reader(csv_file)
    
    next(csv_reader)
    
    for line in csv_reader:
        print(line)
        
o/p===    ['Naveen', ' Chowdary', ' Naveen@fgg.com']
           ['Ragh', ' Thiru', ' GGff@hhgh.com']
           ['Shiv', ' chowd', ' Shihjhg@hg.com']

'''






'''with open('Naveen-Python/Names.csv','r') as csv_file:
    csv_reader=csv.reader(csv_file)
    
    
    with open('Naveen-Python/New_Names.csv','w') as Newcsv_file:
        csv_writer = csv.writer(Newcsv_file,delimiter='\t')
    
        for line in csv_reader:
            csv_writer.writerow(line)
        
        #creates New file As Newcsv_file 
     
'''   
  
  
  
  
  
   

'''with open('Naveen-Python/New_Names.csv','r') as csv_file:
    csv_reader=csv.reader(csv_file,delimiter='\t')
    
    for line in csv_reader:
        print(line)
        
o/p   ===  ['F_Name', 'L_Name', 'Email']
           ['Naveen', ' Chowdary', ' Naveen@fgg.com']
           ['Ragh', ' Thiru', ' GGff@hhgh.com']
           ['Shiv', ' chowd', ' Shihjhg@hg.com']

'''







'''
with open('Naveen-Python/New_Names.csv','r') as csv_file:
    csv_reader=csv.DictReader(csv_file,delimiter='\t')

    for line in csv_reader:
        print(line['Email'])

o/p   ===  OrderedDict([('F_Name', 'Naveen'), ('L_Name', ' Chowdary'), ('Email', ' Naveen@fgg.com')])
           OrderedDict([('F_Name', 'Ragh'), ('L_Name', ' Thiru'), ('Email', ' GGff@hhgh.com')])
           OrderedDict([('F_Name', 'Shiv'), ('L_Name', ' chowd'), ('Email', ' Shihjhg@hg.com')])
  
'''






'''with open('Naveen-Python/New_Names.csv','r') as csv_file:
    csv_reader=csv.DictReader(csv_file,delimiter='\t')

    for line in csv_reader:
        print(line['Email'])
   
 o/p   ===   Naveen@fgg.com
             GGff@hhgh.com
             Shihjhg@hg.com

'''





 
with open('Naveen-Python/New_Names.csv','r') as csv_file:
    csv_reader=csv.DictReader(csv_file)
    
    with open('New_Names.csv','w') as Newcsv_file:
        fieldnames=['Fi_Name','La_Name','E_mail']
        
        csv_writer = csv.DictWriter(Newcsv_file,fieldnames=fieldnames,delimiter='\t')
        
        csv_writer.writeheader()
    
        for line in csv_reader:
            #del line['Email']
            csv_writer.writerow(line)
    







'''with open('Naveen-Python/New_Names.csv','r') as csv_file:
    csv_reader=csv.DictReader(csv_file,delimiter='\t')

    for line in csv_reader:
        print(dict(line))
        
o/p  --  ==    {'F_Name': 'Naveen', 'L_Name': ' Chowdary', 'Email': ' Naveen@fgg.com'}
               {'F_Name': 'Ragh', 'L_Name': ' Thiru', 'Email': ' GGff@hhgh.com'}
               {'F_Name': 'Shiv', 'L_Name': ' chowd', 'Email': ' Shihjhg@hg.com'}



'''

'''with open('Naveen-Python/New_Names.csv','r') as csv_file:
    csv_reader=csv.DictReader(csv_file,delimiter='\t')

    for line in csv_reader:
        print(dict(line))
   
'''



