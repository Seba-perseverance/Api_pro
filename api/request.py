import requests

class solicitudes():
    def __init__(self,url):
        self.url=url
    
    def get(self):
        response = requests.get(self.url)
        print(response.json())
        print(response.status_code)
    def get_id(self,id):
        response = requests.get(f'{self.url}/{id}')
        print(response.json())
        print(response.status_code)
    def post(self,name,cargo):
        employee = { "name": name , "cargo":cargo}
        headers = {"Content-type": "application/json"}
        response = requests.post(self.url, json=employee, headers=headers)
        print(response.content)
        print(response.headers)
        print(response.status_code) 
    def put(self,id,name):
        employee = { "name": name }
        headers = {"Content-type": "application/json"}
        response = requests.put(f'{self.url}/{id}', json=employee, headers=headers)
        print(response.json())
        print(response.status_code)
    def delete(self,id):
        response = requests.delete(f'{self.url}/{id}')
        print(response.json())
        print(response.status_code)
u="http://localhost:5000/employees"
u=solicitudes(u)
u.get()