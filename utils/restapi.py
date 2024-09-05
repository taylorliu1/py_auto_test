import base64
import requests
import pprint
import argparse
import re
from urllib3.exceptions import InsecureRequestWarning
import json

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

class APIRequest(object):
    def __init__(self,host, user, password):
        self.HOST = host
        self.USER = user
        self.PASSWORD = password

    @property
    def access_token(self):
        url = "https://{}/api/rest".format(self.HOST)
        credentials = self.USER + ':' + self.PASSWORD
        token = base64.b64encode(credentials.encode())
        return token
    
    @property
    def access_token_pflex(self):
        url = 'https://{}/rest/auth/login'.format(self.HOST)
        headers ={
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        data = {
            "username": self.USER,
            "password": self.PASSWORD
        }
        response = requests.post(url, json=data, headers=headers,verify=False).json()
        return response['access_token']


    def run(self, method, endpoint, params=None, data=None):
        params = params or dict(select='*')
        #params.update(name='eq.NAS_nfs')
        # url = 'https://{}:443/rest/{}/{}'.format(self.HOST, self.VERSION, endpoint)
        url = 'https://{}/{}'.format(self.HOST, endpoint)
        headers = dict(Authorization="Basic {}".format(self.access_token.decode('utf8')))
        headers.update({"Accept": "application/json"})
        headers.update({"Content-Type": "application/json"})
        print("url: {}\nmethod: {}\ndata: {}".format(url, method, data))
        response = requests.request(method, url, json=data, params=params, headers=headers, verify=False)
        if self.is_json(response.content):
            response = response.json()
        print('-' * 60)
        pprint.pprint(response)
        return response.status_code
    
    def run_pflex(self, method, endpoint, params=None, data=None):
        params = params or dict(select='*')
        #params.update(name='eq.NAS_nfs')
        # url = 'https://{}:443/rest/{}/{}'.format(self.HOST, self.VERSION, endpoint)
        url = 'https://{}/{}'.format(self.HOST, endpoint)
        headers = dict(Authorization="Bearer {}".format(self.access_token_pflex))
        headers.update({"Accept": "application/json"})
        headers.update({"Content-Type": "application/json"})
        if data is None and method=='POST':
            data={}
        print("url: {}\nmethod: {}\ndata: {}".format(url, method, data))
        response = requests.request(method, url, json=data, params=params, headers=headers, verify=False)
        if self.is_json(response.content):
            response = response.json()
        # print('-' * 60)
        # pprint.pprint(response)
        return response
    
    def is_json(self,response):
        try:
            json_object = json.loads(response)
        except ValueError as e:
            return False
        return True

    def generate_data(self,data_list):
        if not data_list:
            return

        data = {}
        for line in data_list:
            match = re.match('^(\w+)=(.*)$', line)
            if not match:
                raise ValueError('Please pass right data format, e.g. filed=value, {}'.format(line))
            pattern = re.compile(r'^[0-9]*$')
            value = match.group(2).strip()
            if pattern.search(value):
                value = int(value)
            data[match.group(1).strip()] = value
        return data


