import requests
response=requests.get("https://gitlab.com/api/v4/users/nanuchi/projects")
resp=response.json()
for project in resp:
    print (f"Project Name {project['name']}\n Url {project['web_url']}\n")