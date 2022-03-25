from flask import Flask, jsonify, render_template,request
from connection1 import mydb

mycursor = mydb.cursor()

app = Flask(__name__)
app.secret_key = "andhisnameisjohncena"

@app.route("/")
def home():
    return render_template("index.html") #"Department Names : FINANCE, AUDIT, MARKETING, PRODUCTION"        

@app.route("/department/q=<name>", methods=["POST", "GET"])
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
        #print(result[0][0])
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
    elif request.method=="POST":
        return name.json()

if __name__ == "__main__":
    app.run(debug=True)