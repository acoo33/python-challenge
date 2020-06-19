import csv

def vote_analysis():

    file_path = 'election_data.csv'
    with open(file_path) as csvfile:
        csvreader = csv.reader(csvfile,delimiter = ',')
        csv_header = next(csvreader)
        tot_num = 0
        khan_count = 0
        correy_count = 0
        li_count = 0
        otooley_count = 0
        for i in csvreader:
            tot_num+=1 
            if (i[2]) == 'Khan':
                khan_count += 1
            elif (i[2]) == 'Correy':
                correy_count += 1
            elif (i[2]) == 'Li':
                li_count += 1
            elif (i[2]) == "O'Tooley":
                otooley_count += 1


    per_khan = khan_count/tot_num
    khan_formatted = '{:.3%}'.format(per_khan)
    per_correy = correy_count/tot_num
    correy_formatted = '{:.3%}'.format(per_correy)
    per_li = li_count/tot_num
    li_formatted = '{:.3%}'.format(per_li)
    per_otooley = otooley_count/tot_num
    otooley_formatted = '{:.3%}'.format(per_otooley)

   
    
    
    
    print('Election Results')
    print('-------------------------')
    print('Total Votes: ' + str(tot_num))
    print('-------------------------')
    print('Khan: ' + str(khan_formatted) + '(' + str(khan_count) + ')')
    print('Correy: ' + str(correy_formatted)+ '(' + str(correy_count) + ')')
    print('Li: ' + str(li_formatted)+ '(' + str(li_count)+ ')')
    print('O\'Tooley: ' + str(otooley_formatted) + '(' + str(otooley_count) + ')')
    print('-------------------------')
    print('Winner: Khan')
    print('-------------------------')

    new_path = "vote_analysis.txt"
    new_file = open(new_path,"w")
    new_file.write('Election Results\n')
    new_file.write('-------------------------\n')
    new_file.write('Total Votes: ' + str(tot_num)+'\n')
    new_file.write('-------------------------\n')
    new_file.write('Khan: ' + str(khan_formatted) + '(' + str(khan_count) + ')' + '\n')
    new_file.write('Correy: ' + str(correy_formatted) + '(' + str(correy_count) + ')' + '\n')
    new_file.write('Li: ' + str(li_formatted) + '(' + str(li_count)+ ')' + '\n')
    new_file.write('O\'Tooley: ' + str(otooley_formatted) +  '(' + str(otooley_count) + ')' + '\n')
    new_file.write('-------------------------\n')
    new_file.write('Winner: Khan\n')
    new_file.write('-------------------------\n')

        
vote_analysis()


