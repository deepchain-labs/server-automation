# import json
from django.shortcuts import render
import time
from numpy import True_

import requests
def index(request):
    if request.method == 'POST':
        # subdomainename = request.POST.get('subdomainename')
        # dns = request.POST.get('ipaddress')
#         {
#     "Host":"app4",
#     "Address" : "192.64.115.91",
#     "RecordType": "A",
#     "TTL": "100",
#     "hostName":"localhost",
#     "port":"5000"
# }
        dns= request.POST.get('dns')
        project_name=request.POST.get('subdomainename')+"-"+dns+"-com"
        payload = {
            'Host': request.POST.get('subdomainename'),
            'Address': request.POST.get('ipaddress'),
            'TTL': "100",
            "RecordType": "A",
            'hostName': project_name,
            'port':"80"
            
        }
        print(project_name)
        server_command= "sudo /home/alamin/storage/scripts/server_setup.sh -a  " + project_name
        print(server_command)
        configure_webserver={
            "command": server_command
        }
        # git_data={
        #     "name": project_name,
        #     "description":"this is form application.",
        #     "private": True
        # }
        # restart_webserver={
        #     "command": "sudo docker restart nginxproxymanager && sudo docker restart webserver"
        # }
        # clone_repo={
        #     "command": "cd /home/alamin/Documents/dcl-deploy-project/ && sudo git clone  https://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@github.com/DeepchainLabs/"+project_name+".git"
        # }
        # add_code_in_repo={
        #     "command": "cd /home/alamin/Documents/dcl-deploy-project/"+project_name+"/ && sudo cp -r /home/alamin/Public/meyawo/public_html/* ./  && sudo git add . && sudo git commit -m 'first commit from server' && sudo git bramch -M master && sudo git push origin master"
        # }
        endpoint_url = "https://api.dns.deepchainlabs.com/namecheap/domains/dns/"+dns+"/com"
        # github_api= "https://dev.geo.deepchainlabs.com/github/repositories"
        server_api_ssh="https://storage.deepchainlabs.com/ssh-command/15e07c93-e1d6-427c-b240-da49db6f84f9"
        # project_name=subdomainename+"-"+dns+"-com"
        time.sleep(3)
        # data_new=json.dumps(payload)
        # headers = {'Content-Type': 'application/json'}
        response = requests.post(endpoint_url, json=payload)
        # restart_server= requests.post(server_api_ssh, json=restart_webserver)
        # print(restart_server)
        # time.sleep(2)
        # create_git_repo= requests.post(github_api, json=git_data)
        # time.sleep(2)
        # clone_git_repo= requests.post(server_api_ssh, json=clone_repo)
        # time.sleep(2)
        # add_template_git_repo= requests.post(server_api_ssh, json=add_code_in_repo)
        # if response.status_code == 200:
            
            # time.sleep(2)
        time.sleep(4)
        response2 = requests.post(server_api_ssh, json=configure_webserver)
        # git_response=requests.post(github_api, json=git_data)
        # print("")
        # print(response)
        time.sleep(4)
        print(response.json)
        # print(response2.json)
        return render(request, 'output.html', {'output': server_command, 'error': ""})

    return render(request,'index.html')
