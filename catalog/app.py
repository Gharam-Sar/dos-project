from flask import Flask, request

import json #to send json opject as a response
import csv #to manipulate data in the csv file
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

    value=[]
    for row in rows:
        if row[2] == topic:
            title=row[1]
            id=row[0]
            val = {
                "item_number": id,
                "title": title,
            }
            value.append(val)#assempling the json object
    return json.dumps(value),201 #returning the json object to the frontend server
   

@my_app.route('/queryItem',methods=["GET"])#query with item from frontend info http request
def query_item():
    item=request.args.get('item')#getting params from the request url
    print(item)
    file = open('data.csv')#opening file and retrieving the data 

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
    val = { #assempling the json object
        "title": title,
        "stock": stock,
        "cost": cost
    }
    return json.dumps(val),201 #returning the json object to the frontend server

@my_app.route('/update',methods=["PUT"]) #update with item from order purchase http request
def update():
    print(request.args)
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
            num=int(stock)-1 #decrementing the stock for the item selected 
            row[3]=num
            print(row[3])
    filename = 'data.csv'
    with open(filename, 'w', newline="") as file:#opening the file to update data
        csvwriter = csv.writer(file) 
        csvwriter.writerow(header) 
        csvwriter.writerows(rows)
    print(header)
    print(rows)    

    return str('purchased '+title+'\n'),201 #returning successful purchase to the order server


@my_app.errorhandler(TypeError)
def handler(error):
    return 'Missing Parameter',400 #returning when an error occurs


def main():
    my_app.run(debug=True, port=5000)

if __name__ =='__main__':
    main()


