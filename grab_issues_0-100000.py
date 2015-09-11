__author__ = 'FFK'
import requests
import json
import timeit

counter=0
start_at_value=0
file_writer = open("0-100000.csv", "a",encoding='utf8')

def writeIssues(p_issues):


    data_row=[]
    for issue in p_issues:
        global counter
        counter+=1
        data_row.append(counter)
        try:
            data_row.append(issue['id'])
        except TypeError:
            data_row.append("None")
        try:
            data_row.append(issue['key'])
        except TypeError:
            data_row.append("None")
        try:
            data_row.append(issue['fields']['summary'])
        except TypeError:
            data_row.append("None")
        try:
            data_row.append(issue['fields']['creator']['displayName'])
        except TypeError:
            data_row.append("None")
        data_row.append(issue['fields']['workratio'])
        # data_row.append(issue['fields']['components'][0]["id"])
        # data_row.append(issue['fields']['components'][0]["name"])
        try:
            data_row.append(issue['fields']['status']['statusCategory']["name"])
        except TypeError:
            data_row.append("None")
        try:
            data_row.append(issue['fields']['status']['statusCategory']["key"])
        except TypeError:
            data_row.append("None")
        try:
            data_row.append(issue['fields']['status']['statusCategory']["id"])
        except TypeError:
            data_row.append("None")
        try:
            data_row.append(issue['fields']['status']["id"])
        except TypeError:
            data_row.append("None")
        try:
            data_row.append(issue['fields']['status']["name"])
        except TypeError:
            data_row.append("None")
        try:
            data_row.append(issue['fields']["updated"])
        except TypeError:
            data_row.append("None")
        try:
            data_row.append(issue['fields']["timeoriginalestimate"])
        except TypeError:
            data_row.append("None")
        try:
            data_row.append(issue['fields']["aggregatetimeestimate"])
        except TypeError:
            data_row.append("None")
        try:
            data_row.append(issue['fields']["aggregatetimeoriginalestimate"])
        except TypeError:
            data_row.append("None")
        try:
            data_row.append(issue['fields']["timespent"])
        except TypeError:
            data_row.append("None")
        try:
            data_row.append(issue['fields']["aggregatetimespent"])
        except TypeError:
            data_row.append("None")
        try:
            data_row.append(issue['fields']["timeestimate"])
        except TypeError:
            data_row.append("None")

        # resolution condition
        try:
            data_row.append(issue['fields']["resolution"]['name'])
        except TypeError:
            data_row.append(issue['fields']["resolution"])

        try:
            data_row.append(issue['fields']['project']["id"])
        except TypeError:
            data_row.append("None")
        try:
            data_row.append(issue['fields']['project']["name"])
        except TypeError:
            data_row.append("None")

        try:
            data_row.append(issue['fields']["assignee"]['displayName'])
        except TypeError:
            data_row.append(issue['fields']["assignee"])

        try:
            data_row.append(issue['fields']['aggregateprogress']["total"])
        except TypeError:
            data_row.append("None")


        #data_row.append(issue['fields']['aggregateprogress']["percent"])

        try:
            data_row.append(issue['fields']['aggregateprogress']["progress"])
        except TypeError:
            data_row.append("None")
        try:
            data_row.append(issue['fields']['progress']["total"])
        except TypeError:
            data_row.append("None")

    #    data_row.append(str(issue['fields']['progress']["percent"]))

        try:
            data_row.append(issue['fields']['progress']["progress"])
        except TypeError:
            data_row.append("None")
        try:
            data_row.append(issue['fields']["created"])
        except TypeError:
            data_row.append("None")
        try:
            data_row.append(issue['fields']["duedate"])
        except TypeError:
            data_row.append("None")
        try:
            data_row.append(issue['fields']["priority"]['id'])
        except TypeError:
            data_row.append("None")
        try:
            data_row.append(issue['fields']["priority"]['name'])
        except TypeError:
            data_row.append("None")

        try:
            data_row.append(issue['fields']["reporter"]['displayName'])
        except TypeError:
            data_row.append("None")
        try:
            data_row.append(issue['fields']["issuetype"]['name'])
        except TypeError:
            data_row.append("None")
        try:
            data_row.append(issue['fields']["issuetype"]['id'])
        except TypeError:
            data_row.append("None")
        try:
            data_row.append(issue['fields']["issuetype"]['subtask'])
        except TypeError:
            data_row.append("None")



        for data_item in data_row:
            file_writer.write(str(data_item)+"\t")
        data_row=[]
        file_writer.write("\n")


    return;



start = timeit.default_timer()

#=======================================================
header_fields=[]
header_fields.append("number");
header_fields.append("id");
header_fields.append("Key");
header_fields.append("Summary");
#creator fields
header_fields.append("Creator_name");
header_fields.append("Work_ratio");
#components
# header_fields.append("Components_id");
# header_fields.append("Components_name");
#status_category
header_fields.append("Status_category_name");
header_fields.append("Status_category_key");
header_fields.append("Status_category_id");
#status
header_fields.append("Status_id");
header_fields.append("Status_name");
#time
header_fields.append("Updated");
header_fields.append("Original_estimate");
header_fields.append("Aggregate_estimate");
header_fields.append("aggregate_Time_Original_Estimate");
header_fields.append("Time_spent");
header_fields.append("Aggregate_Time_spent");
header_fields.append("Time_Estimate");
#resolution
header_fields.append("Resolution");
#project
header_fields.append("Project_id");
header_fields.append("Project_name");
#assignee
header_fields.append("Assignee");
#aggregateprogress
header_fields.append("Aggregate_Progress_total");
#header_fields.append("Aggregate_Progress_percent");
header_fields.append("Aggregate_Progress_progress");
header_fields.append("Progress_total");
#header_fields.append("Progress_percent");
header_fields.append("Progress_progress");

#date
header_fields.append("Date_created");
header_fields.append("Due_date");
#priority
header_fields.append("Priority_id");
header_fields.append("Priority_name");
#reporter
header_fields.append("Reporter_name");

#issue
header_fields.append("Issue_type_name");
header_fields.append("Issue_type_id");
header_fields.append("Issue_type_subTask");

#write headers
# for header_field in header_fields:
#     file_writer.write(header_field+"\t")
# file_writer.write("\n")
#======================================================================


request_number_of_issues = requests.get('https://issues.apache.org/jira/rest/api/2/search?jql=&maxResults=0')
total_number_isses = request_number_of_issues.json()['total']




main_request_text = 'https://issues.apache.org/jira/rest/api/2/search?jql=&maxResults=100&startAt='

done= 0



for i in range(start_at_value,start_at_value+100000,100):
    issues_data_array = []
    request_issues_data = requests.get(main_request_text+str(i))
    request_issues_data_json = request_issues_data.json()['issues']
    issues_data_array.append(request_issues_data_json)
    done +=100
    progress=done/total_number_isses*100
    stop_partial = timeit.default_timer()
    print(round(progress,3) , "% done" ,"time elapsed:",round(stop_partial,2),counter )

    all_issues=[]
    for issues_group in issues_data_array:
        all_issues += issues_group
    writeIssues(all_issues)

print ('number of issues fetched',counter-start_at_value,counter,start_at_value)
file_writer.close()
stop = timeit.default_timer()
print (stop - start)