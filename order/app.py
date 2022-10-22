from flask import Flask, request

import requests

my_app=Flask(__name__)

@my_app.route('/purchase',methods=["PUT"]) #purchase with item from frontend purchase http request
def purchase():
    item=request.args.get('item')#getting params from the request url
    ip="192.168.1.101" #catalog server ip
    port="5000" #catalog server port
    URL = "http://"+ip+":"+port+"/update"
    PARAMS = {'item':item}
    r = requests.put(url = URL, params = PARAMS)
    data=r.text
    return str(data),201 #returning the response from the catalog server to the frontend server
@my_app.errorhandler(TypeError)
def handler(error):
    return 'Missing Parameter',400 #returning when an error occurs

def main():
    my_app.run(FLASK_RUN_HOST="localhost", FLASK_RUN_PORT=3000)

if __name__ =='__main__':
    main()
