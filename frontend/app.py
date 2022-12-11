from flask import Flask, request

import requests
import time
import json
my_app=Flask(__name__)
class book:
    def __init__(self, item,title,stock,cost):
        self.item = item
        self.stock = stock
        self.title = title
        self.cost = cost
       
 
cache=[] 

counter = 1
@my_app.route('/search/<string:topic>',methods=["GET"])#search with topic redurects http request to the catalog server
def search(topic):
    global counter
    if counter ==1:
        print("1")
        counter = counter+1
        ip="192.168.1.105" #catalog server ip
        port="5000" #catalog server port
    elif counter ==2:
        print("2")
        counter = counter+1
        ip="192.168.1.105" #catalog server ip
        port="5001" #catalog server port
    elif counter==3:
        print("3")
        counter =1
        ip="192.168.1.105" #catalog server ip
        port="5002" #catalog server port
    URL = "http://"+ip+":"+port+"/queryTopic"  #the catalog server url for serach
    PARAMS = {'topic':topic}
    data="tt"
    try:
        r = requests.get(url = URL, params = PARAMS)#redirecting to the catalog server
    except:
        if counter==2:
            try:
                ip="192.168.1.105" #catalog server ip
                port="5001" #catalog server port
                URL = "http://"+ip+":"+port+"/queryTopic"  #the catalog server url for serach
                r = requests.get(url = URL, params = PARAMS)#redirecting to the catalog server
            except:
                ip="192.168.1.105" #catalog server ip
                port="5002" #catalog server port
                URL = "http://"+ip+":"+port+"/queryTopic"  #the catalog server url for serach
                try:
                    r = requests.get(url = URL, params = PARAMS)#redirecting to the catalog server
                except:
                    data="Sorry, all servers are down, try again later"
                else:
                    data=r.text
            else:
                data=r.text
        elif counter==3:
            try:
                ip="192.168.1.105" #catalog server ip
                port="5002" #catalog server port
                URL = "http://"+ip+":"+port+"/queryTopic"  #the catalog server url for serach
                r = requests.get(url = URL, params = PARAMS)#redirecting to the catalog server
            except:
                ip="192.168.1.105" #catalog server ip
                port="5000" #catalog server port
                URL = "http://"+ip+":"+port+"/queryTopic"  #the catalog server url for serach
                try:
                    r = requests.get(url = URL, params = PARAMS)#redirecting to the catalog server
                except:
                    data="Sorry, all servers are down, try again later"
                else:
                    data=r.text
            else:
                data=r.text
        elif counter==1:
            try:
                ip="192.168.1.105" #catalog server ip
                port="5000" #catalog server port
                URL = "http://"+ip+":"+port+"/queryTopic"  #the catalog server url for serach
                r = requests.get(url = URL, params = PARAMS)#redirecting to the catalog server
            except:
                ip="192.168.1.105" #catalog server ip
                port="5001" #catalog server port
                URL = "http://"+ip+":"+port+"/queryTopic"  #the catalog server url for serach
                try:
                    r = requests.get(url = URL, params = PARAMS)#redirecting to the catalog server
                except:
                    data="Sorry, all servers are down, try again later"
                else:
                    data=r.text
            else:
                data=r.text
        
    else:
        data=r.text
    return str(data),201

@my_app.route('/info/<int:item>',methods=["GET"])#info with item redirects http request to the catalog server
def info(item):
    flag=0
    data="tt"
    ts1 = time.time()
    for obj in cache:
        if item == obj.item:
            res="{"+"\"title\": \""+obj.title+"\", \"stock\": \""+obj.stock+"\", \"cost\": \""+obj.cost+"\"}"
            flag=1
    if flag==0 :   
        global counter
        if counter ==1:
            print("1")
            counter = counter+1
            ip="192.168.1.105" #catalog server ip
            port="5000" #catalog server port
        elif counter ==2:
            print("2")
            counter = counter+1
            ip="192.168.1.105" #catalog server ip
            port="5001" #catalog server port
        elif counter==3:
            print("3")
            counter =1
            ip="192.168.1.105" #catalog server ip
            port="5002" #catalog server port
        URL = "http://"+ip+":"+port+"/queryItem" #the catalog server url for info
        PARAMS = {'item':item}
        try:
            r = requests.get(url = URL, params = PARAMS)#redirecting to the catalog server
        except:
            if counter==2:
                try:
                    ip="192.168.1.105" #catalog server ip
                    port="5001" #catalog server port
                    URL = "http://"+ip+":"+port+"/queryItem"  #the catalog server url for serach
                    r = requests.get(url = URL, params = PARAMS)#redirecting to the catalog server
                except:
                    ip="192.168.1.105" #catalog server ip
                    port="5002" #catalog server port
                    URL = "http://"+ip+":"+port+"/queryItem"  #the catalog server url for serach
                    try:
                        r = requests.get(url = URL, params = PARAMS)#redirecting to the catalog server
                    except:
                        data="Sorry, all servers are down, try again later"
                    else:
                        data=r.text
                else:
                    data=r.text
            elif counter==3:
                try:
                    ip="192.168.1.105" #catalog server ip
                    port="5002" #catalog server port
                    URL = "http://"+ip+":"+port+"/queryItem"  #the catalog server url for serach
                    r = requests.get(url = URL, params = PARAMS)#redirecting to the catalog server
                except:
                    ip="192.168.1.105" #catalog server ip
                    port="5000" #catalog server port
                    URL = "http://"+ip+":"+port+"/queryItem"  #the catalog server url for serach
                    try:
                        r = requests.get(url = URL, params = PARAMS)#redirecting to the catalog server
                    except:
                        data="Sorry, all servers are down, try again later"
                    else:
                        data=r.text
                else:
                    data=r.text
            elif counter==1:
                try:
                    ip="192.168.1.105" #catalog server ip
                    port="5000" #catalog server port
                    URL = "http://"+ip+":"+port+"/queryItem"  #the catalog server url for serach
                    r = requests.get(url = URL, params = PARAMS)#redirecting to the catalog server
                except:
                    ip="192.168.1.105" #catalog server ip
                    port="5001" #catalog server port
                    URL = "http://"+ip+":"+port+"/queryItem"  #the catalog server url for serach
                    try:
                        r = requests.get(url = URL, params = PARAMS)#redirecting to the catalog server
                    except:
                        data="Sorry, all servers are down, try again later"
                    else:
                        data=r.text
                else:
                    data=r.text
            
        else:
            data=r.text

        res=data
        if data != '"Book is not available"':
            temp=json.loads(data)
            stock=temp['stock']
            title=temp['title']
            cost=temp['cost']
            if len(cache) < 4:
                cache.append(book(item,title,stock,cost))
            elif len(cache) == 4:
                cache.pop(0)
                cache.append(book(item,title,stock,cost))    
    ts2 = time.time()
    dif=ts2-ts1
    print("query ")
    print(dif)
    for obj in cache:
        print(obj.item,obj.title, obj.stock, obj.cost)
 

    return str(res),201
@my_app.route('/purchase/<int:item>',methods=["PUT"])#purchase with item redurects http request to the order server
def purchase(item):
    data="tt"
    flag=0
    res=""
    ts1 = time.time()
    for obj in cache:
        if item == obj.item:
            if obj.stock == "0":
                res="your order is out of stock"
                flag=1
    if flag==0:
        global counter
        if counter ==1:
            print("1")
            counter = counter+1
            ip="192.168.1.105" #catalog server ip
            port="4000" #order server port
        elif counter ==2:
            print("2")
            counter = counter+1
            ip="192.168.1.105" #catalog server ip
            port="4001" #order server port
        elif counter==3:
            print("3")
            counter =1
            ip="192.168.1.105" #catalog server ip
            port="4002" #order server port

        URL = "http://"+ip+":"+port+"/purchase"  #the order server url for purchase
        PARAMS = {'item':item}
        try:
            r = requests.put(url = URL, params = PARAMS)#redirecting to the order server
        except:
            if counter==2:
                try:
                    ip="192.168.1.105" #order server ip
                    port="4001" #order server port
                    URL = "http://"+ip+":"+port+"/purchase"  #the order server url 
                    r = requests.put(url = URL, params = PARAMS)#redirecting to the order server
                except:
                    ip="192.168.1.105" #order server ip
                    port="4002" #order server port
                    URL = "http://"+ip+":"+port+"/purchase"  #the order server url 
                    try:
                        r = requests.put(url = URL, params = PARAMS)#redirecting to the order server
                    except:
                        data="Sorry, all servers are down, try again later"
                    else:
                        data=r.text
                else:
                    data=r.text
            elif counter==3:
                try:
                    ip="192.168.1.105" #order server ip
                    port="4002" #order server port
                    URL = "http://"+ip+":"+port+"/purchase"  #the order server url 
                    r = requests.put(url = URL, params = PARAMS)#redirecting to the order server
                except:
                    ip="192.168.1.105" #order server ip
                    port="4000" #order server port
                    URL = "http://"+ip+":"+port+"/purchase"  #the order server url 
                    try:
                        r = requests.put(url = URL, params = PARAMS)#redirecting to the order server
                    except:
                        data="Sorry, all servers are down, try again later"
                    else:
                        data=r.text
                else:
                    data=r.text
            elif counter==1:
                try:
                    ip="192.168.1.105" #order server ip
                    port="4000" #order server port
                    URL = "http://"+ip+":"+port+"/purchase"  #the order server url 
                    r = requests.put(url = URL, params = PARAMS)#redirecting to the order server
                except:
                    ip="192.168.1.105" #order server ip
                    port="4001" #order server port
                    URL = "http://"+ip+":"+port+"/purchase"  #the order server url 
                    try:
                        r = requests.put(url = URL, params = PARAMS)#redirecting to the order server
                    except:
                        data="Sorry, all servers are down, try again later"
                    else:
                        data=r.text
                else:
                    data=r.text
            
        else:
            data=r.text
        res=data
        
    ts2 = time.time()
    dif=ts2-ts1
    print("purchase ")
    print(dif)
    return str(res),201

@my_app.route('/invalidate',methods=["PUT"]) #update with item from order purchase http request
def updatecsv():
    item=request.args.get('item')#getting params from the request url
    print(item)
    print("ii")
    for obj in cache:
        print(obj.item)
        if item == str(obj.item):
            i=cache.index(obj)
            print("gg")
            print(i)
            print(obj.item)
            cache.pop(i)
    for obj in cache:
        print(obj.item,obj.title, obj.stock, obj.cost)
 
    return str("ok"),201 #returning successful purchase to the order server

@my_app.errorhandler(TypeError)
def handler(error):
    print(error)
    return 'Missing Parameter',400 #returning when an error occurs

def main():
    my_app.run(FLASK_RUN_HOST="localhost", FLASK_RUN_PORT=3000)

if __name__ =='__main__':
    main()
