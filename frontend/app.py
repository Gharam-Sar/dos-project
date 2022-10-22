from flask import Flask, request

import requests

my_app=Flask(__name__)


@my_app.route('/search/<string:topic>',methods=["GET"])#search with topic redurects http request to the catalog server
def search(topic):
    ip="192.168.1.101" #catalog server ip
    port="5000" #catalog server port
    URL = "http://"+ip+":"+port+"/queryTopic"  #the catalog server url for serach
    PARAMS = {'topic':topic}
    r = requests.get(url = URL, params = PARAMS)#redirecting to the catalog server
    data=r.text
    return str(data),201
@my_app.route('/info/<int:item>',methods=["GET"])#info with item redurects http request to the catalog server
def info(item):
    ip="192.168.1.101" #catalog server ip
    port="5000" #catalog server port
    URL = "http://"+ip+":"+port+"/queryItem" #the catalog server url for info
    PARAMS = {'item':item}
    r = requests.get(url = URL, params = PARAMS)#redirecting to the catalog server
    data=r.text
    return str(data),201
@my_app.route('/purchase/<int:item>',methods=["PUT"])#purchase with item redurects http request to the order server
def purchase(item):
    ip="192.168.1.106" #order server ip
    port="4000" #order server port
    URL = "http://"+ip+":"+port+"/purchase"  #the order server url for purchase
    PARAMS = {'item':item}
    r = requests.put(url = URL, params = PARAMS)#redirecting to the order server
    data=r.text
    return str(data),201
@my_app.errorhandler(TypeError)
def handler(error):
    return 'Missing Parameter',400 #returning when an error occurs

def main():
    my_app.run(FLASK_RUN_HOST="localhost", FLASK_RUN_PORT=3000)

if __name__ =='__main__':
    main()
