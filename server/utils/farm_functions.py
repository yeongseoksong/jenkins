import requests
from datetime import datetime,timezone
import json

class GeneralAgent():
    """This is a General Agent
    Examples:
        >>> agent = GeneralAgent()
    """    
    def __init__(self):
        ###Insert test DEVELOPER ID/PW (api/v2/developer)
        self.TEST_DEV_ID="attnkareT_dev7000"
        self.TEST_DEV_PW="12121212"

        ###Insert Hippo-Platform URL:Port
        self.SERVER_URL_PORT = 'http://dev.hippotnc.com:4007/api/v2'
        

    def login_developer(self):
        '''
        This is login function. If you don't have developer user Id, you need to register developer user first.
        Args:
            self (instance): generalAgent class instance
        Returns:
            str: access_token
        Examples:
            >>> agent = GeneralAgent()
            >>> access_token = agent.login_developer()
        Raises:
            Exception: return and print error msg
        '''
        try:
            uri=f'{self.SERVER_URL_PORT}/session'
            
            payload = json.dumps({
                "user": {
                    "uid": self.TEST_DEV_ID,
                    "password": self.TEST_DEV_PW
                }
            })
            
            headers = {
                'Content-Type': 'application/json'
            }
        

            response = requests.request("POST", uri, headers=headers, data=payload).json()         
            access_token=response['data']['access_token']
            
            return access_token
        
        except Exception as e:
            print(e)
            return e
        


    def read_data(self, body, access_token):
        '''
        This is a function fetching data from a job.
        Args:
            self (instance): generalAgent class instance
            body (json) : Json object that comes from HP
            access_token (str) : access_token of TEST_DEV
        Returns:
            json: response
            
        Examples:
            >>> agent = GeneralAgent()
            >>> response = agent.read_data(body, access_token)
        Raises:
            Exception: return and print error msg
        '''
        try: 
#             type            = body['type']
#             job_id          = body['job_id']
#             service_type    = body['service_type']
#             subscription_id = body['subscription_id']
#             user_id         = body['user_id']
#             cmd             = body['body']['cmd']
            
            uri=f'{self.SERVER_URL_PORT}/data'
            payload = json.dumps({
                "type" : 0,
                "subscription_id": body['subscription_id'],
                "service_type_cd": body['job']['service_type'],
                "from_ts": 0,
                "to_ts": int(datetime.now(timezone.utc).timestamp()),
                "filter": {
                    "payload.job_id" : body['job_id']
                },
                "skip": 0,
                "limit": 10,
                "order": "desc"
            })
            headers = {
                'Content-Type': 'application/json',
                'Authorization': access_token
            }

            response = requests.request("POST", uri, headers=headers, data=payload)#.json()
            return response

        except Exception as e:
            print(f"Error (read data): {e}")
            return e


    def preprocess_data(self, response):
        '''
        This is preprocess data function.
        Args:
            self (instance) : generalAgent class instance
            response (json) : response from reading data function
        Returns:
            json : preprocessed data
        Examples:
            >>> agent = GeneralAgent()
            >>> preprocessed_data = agent.preprocess_data(response)
        Raises:
            Exception: return and print error msg
        '''
        try: 
            preprocessed_data=[]

            for datas in response: # response is play datas set
                for data_meta in datas['payload']['data']:
                # {'data': {'601': {'x':~,'y':~},'602':{},'603':{} .... }}
                    cur_data=datas['payload']['data'][data_meta]
                    print(cur_data)
                    if  ('Result' in cur_data) :
                        preprocessed_data.append(cur_data['Result'])
                    
                    else:
                        print('Error (preprocess_data) : data[] is not exist')
            print(f'preprocessed_data : {preprocessed_data}')
            return preprocessed_data
        except Exception as e:
                print(f"Error (preprocess_data): {e}")
                return e

    
    def analyze_job(self, preprocessed_data):
        try: 
            result=sum(preprocessed_data)
            return result
        except Exception as e:
                print(f"Error (analyze_job): {e}")
                return e
     
        
    def callback_results(self, results, body, access_token):  
        '''
        This is a function that sends job execution result.
        Args:
            self (instance) : generalAgent class instance
            body (json) : Json object that comes from HP
            access_token (str) : access_token of TEST_DEV
        Examples:
            >>> agent = GeneralAgent()
            >>> agent.callback_results(body, access_token)
        Raises:
            Exception: return and print error msg
        '''
            
        try: 
            uri = f"{self.SERVER_URL_PORT}/dev/eval-result"
        
            payload = json.dumps({
                "job": {
                    "user_id": body['user_id'],
                    "subscription_id": int(body['subscription_id']),
                    "job_id": body['job_id'],
                    "result": {
                        "user_data": [ results
                            #Insert User data
                        ],                                                                                                                                                                                                    
                        "score": [
                            #Insert Score
                        ],
                        "avg_pent": [
                            #Insert Avg_pent
                        ],
                        "overall_text": "",
                        "subs": [
                            #Insert subs
                            {
                            "title": "title",
                            "score": 99,
                            "sentence": "asdfasdf"
                            }
                        ]
                    }
                }
            }, indent=3)

#             print(payload)
            headers = {
                'Content-Type': 'application/json',
                'Authorization': access_token
            }

            response = requests.request("POST", uri, headers=headers, data=payload).json()
            print(f"callback results: {response}")

        except Exception as e:
            print(e)
