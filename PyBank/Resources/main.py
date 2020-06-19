import csv


 
def financial_analysis():
    csv_path = "budget_data.csv"
    #Open the csv file
    with open(csv_path) as csvfile:
        #Define csv reader and separates the strings by comma
        csvreader = csv.reader(csvfile,delimiter = ",")
        csv_header = next(csvreader)
        net_amount = 0
        mean_of_change = []
        prevPL = 0
        months_list = []
        profit_loss_list = [] 
        newPL = 0

        for each in csvreader:
            profit_loss_list.append(int(each[1]))
            months_list.append(str(each[0]))
            net_amount += int(each[1])
            if prevPL == 0:
                prevPL = int(each[1])
                
            else:
                mean_of_change.append(int(each[1]) - prevPL)
                prevPl = int(each[1])
        final = 0
        for i in range(len(profit_loss_list)-1):
            values = int(profit_loss_list[i+1]) - int(profit_loss_list[i])
            if values > final:
                final = values
                new_month_max = months_list[i+1]
        lowest_final = 0
        for i in range (len(profit_loss_list)-1):
            range_of_values = int(profit_loss_list[i+1]) - int(profit_loss_list[i])
            if range_of_values < lowest_final:
                lowest_final = range_of_values 
                new_month_min = months_list[i+1]

        print('Financial Analysis')
        print('----------------------------')
        print("Total months: " + str(len(mean_of_change)+1))
        print("Total $" + str(net_amount))
        print("Average Change: " + str(sum(mean_of_change)/len(mean_of_change)))
        print("Greatest Increase in Profits: " + str(new_month_max) + " " + "($" + str(final) + ")")
        print("Greatest Decrease in Profits: " + str(new_month_min) + " " + "($" + str(lowest_final) + ")")

        new_path = "analysis.txt"
    
        new_file = open(new_path,"w")
        new_file.write('Financial Analysis\n')
        new_file.write('-------------------------\n')
        new_file.write("Total months: " + str(len(mean_of_change)+1) + "\n")
        new_file.write("Total $" + str(net_amount) + "\n")
        new_file.write("Average Change: " + str(round(sum(mean_of_change)/len(mean_of_change),2)) + "\n")
        new_file.write("Greatest Increase in Profits: " + str(new_month_max) + " " + "($" + str(final) + ")" + "\n")
        new_file.write("Greatest Decrease in Profits: " + str(new_month_min) + " " + "($" + str(lowest_final) + ")" + "\n")
        new_file.write('-------------------------\n')

financial_analysis()

