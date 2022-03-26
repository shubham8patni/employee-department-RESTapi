from flask import Flask, jsonify, render_template,request, Response
from connection1 import mydb
import requests
import json

mycursor = mydb.cursor()

app = Flask(__name__)
app.secret_key = "andhisnameisjohncena"

@app.route("/")
def home():
    return render_template("index.html") #"Department Names : FINANCE, AUDIT, MARKETING, PRODUCTION"        


@app.route("/call")
def call():
    
    api_url = "http://employee-department-restapi.herokuapp.com/create"
    #api_url = "http://127.0.0.1:5000/create"
    create = {
                "employee_id" : "7004",
                "employee_name": "Bruce" ,
                "designation": "salesman",
                "salary": "65024",
                "manager_id" : "68139",
                "hire_date" : "18-5-21",
                "department_name" : "Production"
            }

    headers =  {"Content-Type":"application/json"}
    response = requests.post(api_url, data=json.dumps(create), headers=headers)
    # print("2",response.json())
    print("3 status of query : ", response.status_code)
    return response.json()

@app.route("/create", methods=["POST"])
def create():
    if request.method=="POST":
        record = json.loads(request.data)
        query="select * from employees where emp_id = '"+ record["employee_id"] +"'"
        mycursor.execute(query)
        result = mycursor.fetchall()
        if len(result)>0:
            resp={
                "error" : "Record alrady exists!"
            }
            return resp
        else:
            dep_name= record["department_name"].upper()
            query1 = "select dep_id from departments where dep_name = '"+ dep_name +"'"
            mycursor.execute(query1)
            result = mycursor.fetchall()
            print(result[0][0])

            query = "INSERT INTO employees (emp_id, emp_name, job_name, manager_id, hire_date, salary, commission, dep_id) values(%s, %s, %s, %s, %s, %s, %s, %s)"
            val = (record["employee_id"],record["employee_name"], record["designation"], record["manager_id"],record["hire_date"],record["salary"], "", result[0][0])
            mycursor.execute(query, val)
            mydb.commit()

            return record,201, {'Content-Type': 'application/json'}


@app.route("/department/q=<name>", methods=["GET"])
def listbydepartment(name):
    if request.method == "GET":
        valid = ["AUDIT", "MARKETING", "PRODUCTION", "FINANCE", "audit", "marketing", "production", "finance" ]
        name = name.upper()
        if name not in valid:
            ans = {
                "output": "Invalid department name!"
            }
            ans = jsonify(ans)
            return  ans
            
        query = "select * from employees where dep_id = (select dep_id from departments where dep_name = '"+ name +"')"
        mycursor.execute(query)
        result = mycursor.fetchall()
        
        fin_ans = []
        
        for i in result:
        
            ans = {
                "employee_id" : i[0],
                "employee_name": i[1],
                "designation": i[2],
                "salary": i[5]
                
            }
            fin_ans.append(ans)

        ans = jsonify(fin_ans)
        return ans


@app.route("/department", methods=["GET"])
def listdepartment():
    if request.method == "GET":
            
        query = "select * from employees order by dep_id ASC"
        mycursor.execute(query)
        result = mycursor.fetchall()
        #print(result[0][0])
        fin_ans = []
        
        for i in result:
            if(i[7]=="2001"):
                dep = "AUDIT"
            elif("3001"== i[7]):
                dep = "MARKETING"
            elif("4001"== i[7]):
                dep = "PRODUCTION"
            elif("1001"==i[7]):
                 dep = "FINANCE"
            ans = {
                
                "employee_id" : i[0],
                "employee_name": i[1],
                "designation": i[2],
                "salary": i[5],
                "department": dep
            }
            fin_ans.append(ans)

        ans = jsonify(fin_ans)
        return ans
    

if __name__ == "__main__":
    app.run(debug=True)