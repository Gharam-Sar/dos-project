from flask import Flask, request

import requests

my_app=Flask(__name__)
counter = 1
@my_app.route('/purchase',methods=["PUT"]) #purchase with item from frontend purchase http request
def purchase():

    item=request.args.get('item')#getting params from the request url
    data="tt"
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
    URL = "http://"+ip+":"+port+"/infoPurchace"
    PARAMS = {'item':item}
    try:
        r = requests.get(url = URL, params = PARAMS)#redirecting to the catalog server
    except:
        if counter==2:
            try:
                ip="192.168.1.105" #catalog server ip
                port="5001" #catalog server port
                URL = "http://"+ip+":"+port+"/infoPurchace"  #the catalog server url for serach
                r = requests.get(url = URL, params = PARAMS)#redirecting to the catalog server
            except:
                ip="192.168.1.105" #catalog server ip
                port="5002" #catalog server port
                URL = "http://"+ip+":"+port+"/infoPurchace"  #the catalog server url for serach
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
                URL = "http://"+ip+":"+port+"/infoPurchace"  #the catalog server url for serach
                r = requests.get(url = URL, params = PARAMS)#redirecting to the catalog server
            except:
                ip="192.168.1.105" #catalog server ip
                port="5000" #catalog server port
                URL = "http://"+ip+":"+port+"/infoPurchace"  #the catalog server url for serach
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
                URL = "http://"+ip+":"+port+"/infoPurchace"  #the catalog server url for serach
                r = requests.get(url = URL, params = PARAMS)#redirecting to the catalog server
            except:
                ip="192.168.1.105" #catalog server ip
                port="5001" #catalog server port
                URL = "http://"+ip+":"+port+"/infoPurchace"  #the catalog server url for serach
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



    res=""
    if data == '"0"':
        print("fgg")
        res='your order is out of stock'
    elif data == '"-1"':
        res='your order is Not available'
    else: 
        print("ffff")
        URL = "http://"+ip+":"+port+"/update"
        PARAMS = {'item':item}
        try:
            r = requests.put(url = URL, params = PARAMS)#redirecting to the catalog server
        except:
            if counter==2:
                try:
                    ip="192.168.1.105" #catalog server ip
                    port="5001" #catalog server port
                    URL = "http://"+ip+":"+port+"/update"  #the catalog server url for serach
                    r = requests.put(url = URL, params = PARAMS)#redirecting to the catalog server
                except:
                    ip="192.168.1.105" #catalog server ip
                    port="5002" #catalog server port
                    URL = "http://"+ip+":"+port+"/update"  #the catalog server url for serach
                    try:
                        r = requests.put(url = URL, params = PARAMS)#redirecting to the catalog server
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
                    URL = "http://"+ip+":"+port+"/update"  #the catalog server url for serach
                    r = requests.put(url = URL, params = PARAMS)#redirecting to the catalog server
                except:
                    ip="192.168.1.105" #catalog server ip
                    port="5000" #catalog server port
                    URL = "http://"+ip+":"+port+"/update"  #the catalog server url for serach
                    try:
                        r = requests.put(url = URL, params = PARAMS)#redirecting to the catalog server
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
                    URL = "http://"+ip+":"+port+"/update"  #the catalog server url for serach
                    r = requests.put(url = URL, params = PARAMS)#redirecting to the catalog server
                except:
                    ip="192.168.1.105" #catalog server ip
                    port="5001" #catalog server port
                    URL = "http://"+ip+":"+port+"/update"  #the catalog server url for serach
                    try:
                        r = requests.put(url = URL, params = PARAMS)#redirecting to the catalog server
                    except:
                        data="Sorry, all servers are down, try again later"
                    else:
                        data=r.text
                else:
                    data=r.text
            
        else:
            data=r.text

        res=data
    return str(res),201 #returning the response from the catalog server to the frontend server
@my_app.errorhandler(TypeError)
def handler(error):
    print(error)
    return 'Missing Parameter',400 #returning when an error occurs

def main():
    my_app.run(FLASK_RUN_HOST="localhost", FLASK_RUN_PORT=3000)

if __name__ =='__main__':
    main()
