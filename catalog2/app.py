from flask import Flask, request

import json #to send json opject as a response
import csv #to manipulate data in the csv file
import requests

my_app=Flask(__name__)



@my_app.route('/queryTopic',methods=["GET"]) #query with topic from frontend search http request
def query_topic():
    topic=request.args.get('topic') #getting params from the request url
    file = open('data.csv') #opening file and retrieving the data
    type(file)
    csvreader = csv.reader(file)
    header = []
    header = next(csvreader)
    header
    rows = []
    for row in csvreader:
            rows.append(row)

    file.close()
    flag=0
    value=[]
    for row in rows:
        if row[2] == topic:
            title=row[1]
            id=row[0]
            stock=row[3]
            cost=row[4]
            val = {
                "item_number": id,
                "title": title,
                "stock": stock,
                "cost": cost
            }
            value.append(val)#assempling the json object
            flag=1
    if flag == 0:
        value='Book is not available' 
    return json.dumps(value),201 #returning the json object to the frontend server
   

@my_app.route('/queryItem',methods=["GET"])#query with item from frontend info http request
def query_item():
    item=request.args.get('item')#getting params from the request url
    print(item)
    file = open('data.csv')#opening file and retrieving the data 
    flag=0
    csvreader = csv.reader(file)
    header = []
    header = next(csvreader)
    header
    rows = []
    for row in csvreader:
            rows.append(row)

    file.close()
    for row in rows:
        if row[0] == item:
            title=row[1]
            stock=row[3]
            cost=row[4]
            flag=1
            val = { #assempling the json object
                "title": title,
                "stock": stock,
                "cost": cost
            }
    if flag == 0:
        val='Book is not available'        
    
    return json.dumps(val),201 #returning the json object to the frontend server
@my_app.route('/infoPurchace',methods=["GET"])#query with item from frontend info http request
def info_purchace():
    item=request.args.get('item')#getting params from the request url
    print(item)
    file = open('data.csv')#opening file and retrieving the data 
    flag=0
    csvreader = csv.reader(file)
    header = []
    header = next(csvreader)
    header
    rows = []
    for row in csvreader:
            rows.append(row)

    file.close()

    for row in rows:
        if row[0] == item:            
            stock=row[3]
            flag=1
    if flag == 0:            
        stock="-1"
    print(stock)
    return json.dumps(stock),201 #returning the json object to the frontend server

@my_app.route('/update',methods=["PUT"]) #update with item from order purchase http request
def update():
    # print(request.args)
    res=""
    item=request.args.get('item')#getting params from the request url
    rows = []
    with open("data.csv", 'r') as file:#opening file and retrieving the data
        csvreader = csv.reader(file)
        header = next(csvreader)
        for row in csvreader:
            rows.append(row)
    for row in rows:
        print(row)
    for row in rows:
        if row[0] == item:
            title=row[1]
            stock=row[3]
            if int(stock) == 0:
                            res=title+' is out of stock'
            else:
                            title=row[1]
                            num=int(stock)-1 #decrementing the stock for the item selected 
                            row[3]=num
                            filename = 'data.csv'
                            with open(filename, 'w', newline="") as file:#opening the file to update data
                                csvwriter = csv.writer(file) 
                                csvwriter.writerow(header) 
                                csvwriter.writerows(rows)
                            res='purchased '+title
    mes=""
    try:
        ip="192.168.1.105" #catalog server ip
        port="5000" #order server port
        URL = "http://"+ip+":"+port+"/updateCsv"  #the order server url for purchase
        PARAMS = {'item':item}
        
        r = requests.put(url = URL, params = PARAMS)
        mes=r.text
    except:
        print(mes)
    try:
        ip="192.168.1.105" #catalog server ip
        port="5001" #order server port
        URL = "http://"+ip+":"+port+"/updateCsv"  #the order server url for purchase
        PARAMS = {'item':item}
        
        r = requests.put(url = URL, params = PARAMS)
        mes=r.text

    except:
        print(mes)   

    try:
        ip="192.168.1.105" #catalog server ip
        port="3000" #order server port
        URL = "http://"+ip+":"+port+"/invalidate"  #the order server url for purchase
        PARAMS = {'item':item}

        r = requests.put(url = URL, params = PARAMS)
        mes=r.text
    except:
        print(mes)   

    return str(res+'\n'),201 #returning successful purchase to the order server

@my_app.route('/updateCsv',methods=["PUT"]) #update with item from order purchase http request
def updatecsv():
    res=""
    item=request.args.get('item')#getting params from the request url
    rows = []
    with open("data.csv", 'r') as file:#opening file and retrieving the data
        csvreader = csv.reader(file)
        header = next(csvreader)
        for row in csvreader:
            rows.append(row)
    for row in rows:
        print(row)
    for row in rows:
        if row[0] == item:
            title=row[1]
            stock=row[3]
            title=row[1]
            num=int(stock)-1 #decrementing the stock for the item selected 
            row[3]=num
            filename = 'data.csv'
            with open(filename, 'w', newline="") as file:#opening the file to update data
                csvwriter = csv.writer(file) 
                csvwriter.writerow(header) 
                csvwriter.writerows(rows)
                res='purchased '+title

    return str(res+'\n'),201 #returning successful purchase to the order server

@my_app.errorhandler(TypeError)
def handler(error):
    return 'Missing Parameter',400 #returning when an error occurs


def main():
    my_app.run(debug=True, port=5000)

if __name__ =='__main__':
    main()


