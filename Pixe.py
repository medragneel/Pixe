from datetime import datetime
import requests

ENDPOINT="https://pixe.la/v1/users"
FILENAME="cred.txt"
class Pixe:
    def create_user(self,usr,token):
        with open(FILENAME,'w') as crd:
            cred=f"{usr}\n{token}"
            crd.write(cred)
            b={
                "token":token, 
                "username":usr, 
                "agreeTermsOfService":"yes",
                "notMinor":"yes",
                "thanksCode":"ThisIsThanksCode"
            }
        res=requests.post(url=ENDPOINT,json=b)
        print(res.text)
        return 'user created'


    def update_user(self,new_token):
        with open(FILENAME,'r') as crd:
            cred=crd.readlines()
            print(cred)
            
            h={
                "X-USER-TOKEN": cred[1]
            }
            b={
               "newToken": new_token
            }
        user= cred[0].strip('\n')
        res=requests.put(url=f"{ENDPOINT}/{user}",headers=h,json=b)
        print(res.text)
        with open(FILENAME,'w') as crd:
            dt=f"{cred[0]}{new_token}"
            crd.write(dt)
        return 'user updated'
    def delete_user(self):
        with open(FILENAME,'r') as crd:
            cred=crd.readlines()
            
            h={
                "X-USER-TOKEN": cred[1]
            }
        user= cred[0].strip('\n')
        res=requests.delete(url=f"{ENDPOINT}/{user}",headers=h)
        print(res.text)
        return 'user deleted'


    def post_pixel(self,id,quantity):
        with open(FILENAME,'r') as crd:
            cred=crd.readlines()
            
            h={
                "X-USER-TOKEN": cred[1]
            }
            dt = datetime.today()
            day= datetime.strftime(dt,'%Y%m%d')
            print(day)
            b={
                "date":day,
                "quantity":quantity
            }
            
        user= cred[0].strip('\n')
        res=requests.post(url=f"{ENDPOINT}/{user}/graphs/{id}",headers=h,json=b)
        print(res.text)
        return 'graph created'


    def update_pixel(self,id,quantity):
        with open(FILENAME,'r') as crd:
            cred=crd.readlines()
            
            h={
                "X-USER-TOKEN": cred[1]
            }
            b={
               "quantity": quantity
            }
            
        dt = datetime.today()
        day= datetime.strftime(dt,'%Y%m%d')
        user= cred[0].strip('\n')
        res=requests.put(url=f"{ENDPOINT}/{user}/graphs/{id}/{day}",headers=h,json=b)
        print(res.text)
        return 'graph updated'

    def delete_pixel(self,id):
        with open(FILENAME,'r') as crd:
            cred=crd.readlines()
            
            h={
                "X-USER-TOKEN": cred[1]
            } 
            
        dt = datetime.today()
        day= datetime.strftime(dt,'%Y%m%d')
        user= cred[0].strip('\n')
        res=requests.delete(url=f"{ENDPOINT}/{user}/graphs/{id}/{day}",headers=h)
        print(res.text)
        return 'graph deleted'

    def create_graph(self,id,name,unit,type,color):
        with open(FILENAME,'r') as crd:
            cred=crd.readlines()
            
            h={
                "X-USER-TOKEN": cred[1]
            }
            b={
                "id":id,
                "name":name,
                "unit":unit,
                "type":type,
                "color":color,
            }
            
        user= cred[0].strip('\n')
        res=requests.post(url=f"{ENDPOINT}/{user}/graphs",headers=h,json=b)
        print(res.text)
        return 'graph created'


    def update_graph(self,id,name,unit,type,color):
        with open(FILENAME,'r') as crd:
            cred=crd.readlines()
            
            h={
                "X-USER-TOKEN": cred[1]
            }
            b={
               "name":name,
                "unit": unit,
                "type":type,
               "color":color,
            }
            
        user= cred[0].strip('\n')
        res=requests.put(url=f"{ENDPOINT}/{user}/graphs/{id}",headers=h,json=b)
        print(res.text)
        return 'graph updated'

    def delete_graph(self,id):
        with open(FILENAME,'r') as crd:
            cred=crd.readlines()
            
            h={
                "X-USER-TOKEN": cred[1]
            } 
        user= cred[0].strip('\n')
        res=requests.delete(url=f"{ENDPOINT}/{user}/graphs/{id}",headers=h)
        print(res.text)
        return 'graph deleted'

    def graph_details(self):
        with open(FILENAME,'r') as crd:
            cred=crd.readlines()
            
            h={
                "X-USER-TOKEN": cred[1]
            } 
        user= cred[0].strip('\n')
        res=requests.get(url=f"{ENDPOINT}/{user}/graphs",headers=h)
        return res.json()
        
