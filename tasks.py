import time
import json
import os
from functools import reduce
import subprocess
import threading

class Tasks(object):

    def dictionaries(self, dicts):
        self.dicts = dicts

    def dependencies(self, z):
        name_list = [v for item in z for (k, v) in item.items() if k == 'name']
        self.a_list = [v for item in z for (k,v) in item.items() if k == "dependencies"]
        self.b_list = [d for element in self.a_list for i in element for d in z for k, v in d.items() if (k == 'name' and v == i)]   # dictionary list                     
        self.c_list = [v for item in self.b_list for (k, v) in item.items() if k == "dependencies"]
        self.d_list = [d for element in self.c_list for i in element for d in z for k, v in d.items() if (k == 'name' and v == i)] 
        self.e_list = [v for item in self.d_list for (k, v) in item.items() if k == "dependencies"] 
        
        c1 = [element for element in self.e_list if element in self.c_list] 
        c2 =  [element for element in self.c_list if element not in self.e_list]
        c3 = [element for element in self.a_list if element not in self.c_list]
        
        fc = [] 
        [fc.append(item) for element in c1 for item in element if item not in fc]  
        [fc.append(item) for element in c2 for item in element if item not in fc]
        [fc.append(item) for element in c3 for item in element if item not in fc] 
        [fc.append(item) for item in name_list if item not in fc ]
        fc = [element for element in fc if element != 'task7']
        self.fc = fc      
              
    def task(self, task):
        new_dict = [item for item in self.dicts for (k,v) in item.items() if (k == 'name' and v == task)]
        dictionary = new_dict[0] 
        name = dictionary['name']
        self.taskargs = dictionary["arguments"]
        print(f'Started {name}')
    
        for k, v in dictionary.items():

            if (k == 'type' and v == 'exec'):
                print(f'starting {v}')
                subprocess.run(self.taskargs, shell= True)                      

            elif (k == 'type' and v == 'eval'):
                print(f'starting {v}')
                taskarg1 =  self.taskargs.split(';')
                taskarg1 = [element for element in taskarg1 if (element != 'import time' and element != 'import os')]
                for x in taskarg1:
                    eval(x)           
                
        print(f'Ended {name}')
        return  dictionary 


    def tasks(self):

        for item in self.fc:
            self.task(item)
        return 
        

    def task_7(self):
        for item in self.dicts:
            for k, v in item.items():
                if k == 'task':
                    self.task(v)          
        return v              

if __name__ == "__main__":

    def get_json():
        path = '/home/nithin/parellel_programing/scheduler'
        doc = os.path.join(path, 'input1.json')
        with open(doc) as F:
            json_data = json.load(F) 
        
        foo = [v for (k,v) in json_data.items()] 
        tasks = reduce(lambda x, y: x+y , foo )
        return tasks 
    

    def get_dict():
        dicts = get_json()
        rm_key = 'dependencies'
        for items in dicts:
             if rm_key in items:
                 del items[rm_key]
        return dicts         
    
    obj1 = Tasks()
    dicts = get_dict()
    tasks = get_json()
    obj1.dependencies(tasks)
    obj1.dictionaries(dicts)
    t5 = threading.Thread(target=obj1.tasks) 
    t7 = threading.Thread(target=obj1.task_7)
    t5.start()
    t7.start()
    t5.join() 
    t7.join()
    

    
    
       
            
            
   
 









 







                
                
        



