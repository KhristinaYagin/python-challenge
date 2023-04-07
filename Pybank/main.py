import os
import csv

#Path to collect data from the resource folder
budget_csv = os.path.join("..", "Pybank", "Resources", "budget_data.csv")

months= 0
net_change_list = []
greatest_increase=["", 0]
greatest_decrease=["", 9999999999999999999999]
total_net = 0
prev_net = 0 
net_change =0

with open ("C:/Users/yagin/OneDrive/Desktop/python-challenge/Pybank/Resources/budget_data.csv", "r" ) as d:
    reader= csv.reader(d)

    header = next (reader)
    # print(header)

    first_row=next(reader)
    #print(first_row)
    months = months + 1
    total_net = total_net + int(first_row[1])
    prev_net =  int(first_row[1])
    #print(months)
    #print(total_net)


    for row in reader:
        months = months + 1
        total_net = total_net + int(first_row[1])   
       
        net_change  = int(row[1]) - prev_net 
        net_change_list.append ( net_change )


        if  net_change > greatest_increase[1]:
            greatest_increase[1] = net_change 
            greatest_increase[0] = row[0]

        if  net_change < greatest_decrease[1]:
            greatest_decrease[1] = net_change 
            greatest_decrease[0] = row[0]

net_monthly_change_ave = sum(net_change_list)/len(net_change_list)


output = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {months}\n"
    f"Total: ${total_net}\n"
    f"Average Change: ${net_monthly_change_ave:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")

print(output)

with open ("C:/Users/yagin/OneDrive/Desktop/python-challenge/Pybank/Resources/PyBank_output.txt", "w") as text_file:
    text_file.write(output)










