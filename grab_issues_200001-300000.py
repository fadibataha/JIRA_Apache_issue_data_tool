__author__ = 'FFK'
import requests
import json
import timeit

counter=200000
start_at_value=200000
file_writer = open("200001-300000.csv", "a",encoding='utf8')

def writeIssues(p_issues):


    data_row=[]
    for issue in p_issues:
        global counter
        counter+=1
        data_row.append(counter)
        try:
            data_row.append(issue['id'])
        except (TypeError ,KeyError) as e:
            data_row.append("None")
        try:
            data_row.append(issue['key'])
        except (TypeError ,KeyError) as e:
            data_row.append("None")
        try:
            data_row.append(issue['fields']['summary'])
        except (TypeError ,KeyError) as e:
            data_row.append("None")
        try:
            data_row.append(issue['fields']['creator']['displayName'])
        except (TypeError ,KeyError) as e:
            data_row.append("None")
        data_row.append(issue['fields']['workratio'])
        # data_row.append(issue['fields']['components'][0]["id"])
        # data_row.append(issue['fields']['components'][0]["name"])
        try:
            data_row.append(issue['fields']['status']['statusCategory']["name"])
        except (TypeError ,KeyError) as e:
            data_row.append("None")
        try:
            data_row.append(issue['fields']['status']['statusCategory']["key"])
        except (TypeError ,KeyError) as e:
            data_row.append("None")
        try:
            data_row.append(issue['fields']['status']['statusCategory']["id"])
        except (TypeError ,KeyError) as e:
            data_row.append("None")
        try:
            data_row.append(issue['fields']['status']["id"])
        except (TypeError ,KeyError) as e:
            data_row.append("None")
        try:
            data_row.append(issue['fields']['status']["name"])
        except (TypeError ,KeyError) as e:
            data_row.append("None")
        try:
            data_row.append(issue['fields']["updated"])
        except (TypeError ,KeyError) as e:
            data_row.append("None")
        try:
            data_row.append(issue['fields']["timeoriginalestimate"])
        except (TypeError ,KeyError) as e:
            data_row.append("None")
        try:
            data_row.append(issue['fields']["aggregatetimeestimate"])
        except (TypeError ,KeyError) as e:
            data_row.append("None")
        try:
            data_row.append(issue['fields']["aggregatetimeoriginalestimate"])
        except (TypeError ,KeyError) as e:
            data_row.append("None")
        try:
            data_row.append(issue['fields']["timespent"])
        except (TypeError ,KeyError) as e:
            data_row.append("None")
        try:
            data_row.append(issue['fields']["aggregatetimespent"])
        except (TypeError ,KeyError) as e:
            data_row.append("None")
        try:
            data_row.append(issue['fields']["timeestimate"])
        except (TypeError ,KeyError) as e:
            data_row.append("None")

        # resolution condition
        try:
            data_row.append(issue['fields']["resolution"]['name'])
        except (TypeError ,KeyError) as e:
            data_row.append(issue['fields']["resolution"])

        try:
            data_row.append(issue['fields']['project']["id"])
        except (TypeError ,KeyError) as e:
            data_row.append("None")
        try:
            data_row.append(issue['fields']['project']["name"])
        except (TypeError ,KeyError) as e:
            data_row.append("None")

        try:
            data_row.append(issue['fields']["assignee"]['displayName'])
        except (TypeError ,KeyError) as e:
            data_row.append(issue['fields']["assignee"])

        try:
            data_row.append(issue['fields']['aggregateprogress']["total"])
        except (TypeError ,KeyError) as e:
            data_row.append("None")


        #data_row.append(issue['fields']['aggregateprogress']["percent"])

        try:
            data_row.append(issue['fields']['aggregateprogress']["progress"])
        except (TypeError ,KeyError) as e:
            data_row.append("None")
        try:
            data_row.append(issue['fields']['progress']["total"])
        except (TypeError ,KeyError) as e:
            data_row.append("None")

    #    data_row.append(str(issue['fields']['progress']["percent"]))

        try:
            data_row.append(issue['fields']['progress']["progress"])
        except (TypeError ,KeyError) as e:
            data_row.append("None")
        try:
            data_row.append(issue['fields']["created"])
        except (TypeError ,KeyError) as e:
            data_row.append("None")
        try:
            data_row.append(issue['fields']["duedate"])
        except (TypeError ,KeyError) as e:
            data_row.append("None")
        try:
            data_row.append(issue['fields']["priority"]['id'])
        except (TypeError ,KeyError) as e:
            data_row.append("None")
        try:
            data_row.append(issue['fields']["priority"]['name'])
        except (TypeError ,KeyError) as e:
            data_row.append("None")

        try:
            data_row.append(issue['fields']["reporter"]['displayName'])
        except (TypeError ,KeyError) as e:
            data_row.append("None")
        try:
            data_row.append(issue['fields']["issuetype"]['name'])
        except (TypeError ,KeyError) as e:
            data_row.append("None")
        try:
            data_row.append(issue['fields']["issuetype"]['id'])
        except (TypeError ,KeyError) as e:
            data_row.append("None")
        try:
            data_row.append(issue['fields']["issuetype"]['subtask'])
        except (TypeError ,KeyError) as e:
            data_row.append("None")



        for data_item in data_row:
            file_writer.write(str(data_item)+"\t")
        data_row=[]
        file_writer.write("\n")


    return;



start = timeit.default_timer()


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