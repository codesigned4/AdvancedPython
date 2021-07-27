import requests

class Github:
    def __init__(self):
        self.apiURL="https://api.github.com"
        self.token="dkljfPOEOkjdjfmcmaqwekd956"
    
    def getUser(self,username):
        response=requests.get(self.apiURL+"/users/"+username)
        return response.json()#json import edip json.loads() methodunu kullanmakla aynı şey 
    
    def getRepositories(self,username):
        result=requests.get(self.apiURL+"/users/"+username+"/repos")
        return result.json()
    
    def creteRepository(self,name):
        response=requests.post(self.apiURL+"/user/repos?access_token="+self.token,json={
            "name":name,
            "private":True,
            })
        return response.json()  
        

github=Github()

while True:
    secim=input("1- Find User\n2- Get Repositories\n3- Create Repositories\n4- Exit\nSeçim: ")

    if secim=="4":
        break

    else:
        if secim=="1":
            username=input("Username: ")
            result=github.getUser(username)
            print(f"name: {result['name']} public repos: {result['public_repos']} followers: {result['followers']}")
       
        elif secim=="2":
            username=input("Username: ")
            result=github.getRepositories(username)
            for repo in result:
                print(repo["name"])
            

        elif secim=="3":
            name=input("Repository Name: ")
            result=github.creteRepository(name)
            print(result)
        
        else:
            print("Geçerli bir seçim yapınız!")