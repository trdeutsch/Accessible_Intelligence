from google.cloud import bigquery
from google.oauth2 import service_account

credentials=service_account.Credentials.from_service_account_file('/Users/tranduc/Downloads/credentials.json', 
                                                                  scopes=['https://www.googleapis.com/auth/cloud-platform',
                                                                          "https://www.googleapis.com/auth/drive",
                                                                          "https://www.googleapis.com/auth/bigquery",])
project='accessible-intelligence-456411'

client=bigquery.Client(credentials=credentials, project=project)
query='select * from accessible-intelligence-456411.fundraising_form.responses'
query_job=client.query(query)
result=query_job.result()

result=result.to_dataframe()

def responses(name, answer):
    my_dict={}
    answer=answer.loc[answer['What_is_your_name_']==name,:]
    for column in answer:
        for value in answer[column]:
            my_dict[column]=value
    return my_dict
responses('Sarah Williams', result)