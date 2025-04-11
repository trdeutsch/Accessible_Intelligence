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

def responses(fundraiser, response):
    my_dict={}
    response=response.loc[response['What_is_your_name_']==fundraiser,:]
    for column in response:
        for value in response[column]:
            my_dict[column]=value
    return my_dict
responses(input("Enter the fundraiser's name"), result)