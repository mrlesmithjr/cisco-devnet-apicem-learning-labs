import requests   # We use Python external "requests" module to do HTTP query
import json
import sys

#All APIC-EM configuration is in apicem_config.py
import apicem_config  # APIC-EM IP is assigned in apicem_config.py
from tabulate import tabulate # Pretty-print tabular data in Python

# It's used to get rid of certificate warning messages when using Python 3.
# For more information please refer to: https://urllib3.readthedocs.org/en/latest/security.html
#requests.packages.urllib3.disable_warnings() # Disable warning message

def get_X_auth_token(ip=apicem_config.ip,ver=apicem_config.version,uname=apicem_config.username,pword=apicem_config.password):
    """
    This function returns a new service ticket.
    Passing ip, version,username and password when use as standalone function
    to overwrite the configuration above.
    """

    # JSON input for the post ticket API request
    r_json = {
    "username": uname,
    "password": pword
    }
    # url for the post ticket API request
    post_url = "https://"+ip+"/api/"+ver+"/ticket"
    # All APIC-EM REST API query and response content type is JSON
    headers = {'content-type': 'application/json'}
    # POST request and response
    try:
        r = requests.post(post_url, data = json.dumps(r_json), headers=headers,verify=False)
        # remove '#' if need to print out response
        # print (r.text)

        # return service ticket
        return r.json()["response"]["serviceTicket"]
    except:
        # Something wrong, cannot get service ticket
        print ("Status: %s"%r.status_code)
        print ("Response: %s"%r.text)
        sys.exit ()

def get(ip=apicem_config.ip,ver=apicem_config.version,uname=apicem_config.username,pword=apicem_config.password,api='',params=''):
    """
    To simplify requests.get with default configuration.Return is the same as requests.get
    """
    ticket = get_X_auth_token()
    headers = {"X-Auth-Token": ticket}
    url = "https://"+ip+"/api/"+ver+"/"+api
    print ("\nExecuting GET '%s'\n"%url)
    try:
    # The request and response of "GET /network-device" API
        resp= requests.get(url,headers=headers,params=params,verify = False)
        return(resp)
    except:
       print ("Something wrong to GET /",api)
       sys.exit()

def post(ip=apicem_config.ip,ver=apicem_config.version,uname=apicem_config.username,pword=apicem_config.password,api='',data=''):
    """
    To simplify requests.post with default configuration.Return is the same as requests.post
    """
    ticket = get_X_auth_token()
    headers = {"content-type" : "application/json","X-Auth-Token": ticket}
    url = "https://"+ip+"/api/"+ver+"/"+api
    print ("\nExecuting POST '%s'\n"%url)
    try:
    # The request and response of "POST /network-device" API
        resp= requests.post(url,json.dumps(data),headers=headers,verify = False)
        return(resp)
    except:
       print ("Something wrong to POST /",api)
       sys.exit()

def put(ip=apicem_config.ip,ver=apicem_config.version,uname=apicem_config.username,pword=apicem_config.password,api='',data=''):
    """
    To simplify requests.put with default configuration.Return is the same as requests.put
    """
    ticket = get_X_auth_token()
    headers = {"content-type" : "application/json","X-Auth-Token": ticket}
    url = "https://"+ip+"/api/"+ver+"/"+api
    print ("\nExecuting PUT '%s'\n"%url)
    try:
    # The request and response of "PUT /network-device" API
        resp= requests.put(url,json.dumps(data),headers=headers,verify = False)
        return(resp)
    except:
       print ("Something wrong to PUT /",api)
       sys.exit()

def delete(ip=apicem_config.ip,ver=apicem_config.version,uname=apicem_config.username,pword=apicem_config.password,api='',params=''):
    """
    To simplify requests.delete with default configuration.Return is the same as requests.delete
    """
    ticket = get_X_auth_token()
    headers = {"X-Auth-Token": ticket,'content-type': 'application/json'}
    url = "https://"+ip+"/api/"+ver+"/"+api
    print ("\nExecuting DELETE '%s'\n"%url)
    try:
    # The request and response of "DELETE /network-device" API
        resp= requests.delete(url,headers=headers,params=params,verify = False)
        return(resp)
    except:
       print ("Something wrong to DELETE /",api)
       sys.exit()
