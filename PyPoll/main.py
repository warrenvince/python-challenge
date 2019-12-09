import os, csv
election_data_path = os.path.join("election_data.csv")
#declare dictionary that will hold the records from the csv file
election_data = { "voter_id": [], "county" : [], "candidate" :[]}
line_count = 0
candidate_list=[]
#declare dictionary that will hold the summary value
summary_data = {"candidate":[],"percentage_vote":[],"total_vote":[]}

with open(election_data_path, newline='',encoding = "utf-8") as election_data_file:
    csv_reader = csv.reader(election_data_file, delimiter=",")
    csv_header = next(csv_reader)
# pull records from the csv file into the dictionary
    for row in csv_reader:
        election_data['voter_id'].append(row[0])
        election_data['county'].append(row[1])
        election_data['candidate'].append(row[2])
        line_count += 1
    #print(f"Total Votes : {line_count}")
# pull unique candidate names from the data dictionary
    for ucandidate in election_data['candidate']:
        if (ucandidate) not in candidate_list:
            candidate_list.append(ucandidate)
    votenumber = 0
#  votes are being counted for each unique candidates 
    for candidate in candidate_list:
        candidate_vote = 0
        for countvote in election_data['candidate']:
            if candidate == countvote:
               votenumber += 1
               candidate_vote += 1 
        summary_data['candidate'].append(candidate)
        summary_data['total_vote'].append(candidate_vote)
        #print(candidate_vote)
    print(f"Election Results")
    print(f"----------------")
    print(f"Total Votes : {votenumber}")
    print(f"----------------")
    i=0
    for sm_data in summary_data['total_vote']:
        pctg_vte = (sm_data/votenumber) * 100
        summary_data['percentage_vote'].append(pctg_vte)
        print(f"{summary_data['candidate'][i]}:{round(summary_data['percentage_vote'][i],3)}% ({summary_data['total_vote'][i]})")
        i += 1        
    max_votes = max(summary_data['percentage_vote'])
    max_vote_count = 0
    print(f"-----------------")   
# finding the candidate that has the most vote.
    for line in summary_data['percentage_vote']:
        if(max_votes == summary_data['percentage_vote'][max_vote_count]):
            print(f"Winner is {summary_data['candidate'][max_vote_count]}")
        max_vote_count += 1
    print(f"-----------------")

    #cleansed_summary_data = zip(summary_data['candidate'],summary_data['percentage_vote'], summary_data['total_vote'])
    #print(cleansed_summary_data)
    #print(summary_data)
    #print(candidate_list)
    #print(len(candidate_list))