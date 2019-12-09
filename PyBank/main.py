import os, csv
from statistics import mean
#declare variables
csv_path = "budget_data.csv"
line_count = 0
line_count_2 = 0
total = 0
prev_total = 0
#create dictionary to hold existing values and new values
data = {"date":[],"p_l":[],"change": []}           

#read csv file
with open(csv_path, newline='',encoding="utf-8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_reader)
#code to process csv file line by line to pull values and store it in the dictionary
    for row in csv_reader:
        if(line_count == 0):
            prev_total = int(row[1])
            total = total + int(row[1]) 
            line_count += 1
            data['change'].append(0)
            data['date'].append(str(row[0]))
            data['p_l'].append(int(row[1]))      
        else:
            total = total + int(row[1])
            data['change'].append(int(row[1]) - prev_total)
#capture previous_total to be used on the next iteration
            prev_total = int(row[1])
            line_count += 1
            data['date'].append(str(row[0]))
            data['p_l'].append(int(row[1]))      

    
    max_change = max(data['change'])
    min_change = min(data['change'])
    
    
    #print(data)
    #print(data["date"][0])
    #print(data["p_l"][0])
    #print(data["change"][0])
    #information = zip(date,p_l,change)
    #change_out = [i for i in change]
    #print(f"{change_out}")
    line1 = "Total Months:" + str(line_count) 
    # looping through the data dictionary to get the date with the max and min value
    for line in data['change']:
        #print (data['change'][0])

        #print(max_change)
        #print(line_count_2)
        #print(data['change'][1])

        if(max_change == data['change'][line_count_2]):
           # print(f"Greatest Increase in Profits:{data['date'][line_count_2]} ({data['change'][line_count_2]})")
            max_date = data['date'][line_count_2]
        if(min_change == data['change'][line_count_2]):
            #print(f"Greatest Decrease in Profits:{data['date'][line_count_2]} ({data['change'][line_count_2]})")
            min_date = data['date'][line_count_2]
        
        line_count_2 += 1
cleaned_csv = zip(data['date'],data['p_l'],data['change'])
output_file = os.path.join("homework1.csv")
# export results to csv
with open(output_file,"w",newline="")as datafile:
    writer = csv.writer(datafile)
    #writer.writerow(["Date","Profit/Loss","Change"])
    #writer.writerows(cleaned_csv)
    writer.writerow([f"Financial Analysis"])
    writer.writerow([f"------------------"])
    writer.writerow([line1])
    writer.writerow([f"Total: ${total}"])
    data['change'].pop(0)
    avg_change = mean(data['change'])
    writer.writerow([f"Average Change: {avg_change}"])
    writer.writerow([f"Greatest Increase in Profits:{max_date} ({max_change})"])
    writer.writerow([f"Greatest Decrease in Profits:{min_date} ({min_change})"])
    
#print(information)
    print(f"Financial Analysis")
    print(f"--------------------")                
    print(f"Total Months: {line_count}")
    print(f"Total: ${total}")
    print(f"Average Change: {avg_change}")
    print(f"Greates Increase in Profits: {max_date} ({max_change})")
    print(f"Greatest Decrease in Profits:{min_date} ({min_change})")