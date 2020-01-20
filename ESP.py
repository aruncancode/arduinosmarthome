import requests, json
from bs4 import BeautifulSoup

class ESP:
    def __init__(self,name,ip):
        self.name=name
        self.ip = ip
        self.components = {}
        self.status = {}

    def return_value(self,url,key):
        state = requests.get(url)
        state = BeautifulSoup(state.text, 'html.parser').get_text()
        json_acceptable_string1 = state.replace("'", "\"")
        state = json.loads(json_acceptable_string1)
        state = state[key]
        return state
    
    def update_status(self, component, state):
            self.status[component] = state

    def request_page(self,component, state):
        try:
            pin = self.components[component]
            requests.get(self.ip + "digital/" + pin + "/" + state)
            self.update_status(component, state)
        except: 
            ConnectionError
    
    
    def esp_status(self):
        try:
            status = self.return_value(self.ip, 'connected')
            return status
        except:
            ConnectionError
   
    def boot_status(self, component):
        pin = self.components[component]
        try:
            status = self.return_value(self.ip + 'digital/' + pin +"/r", 'return_value')
            self.update_status(component, status)
            return status
        except:
            ConnectionError
    


#hi 