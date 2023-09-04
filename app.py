from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
import mysql.connector as database
app=Flask("Bookmyshow")
@app.get("/register")
def register_form(): 
    return render_template("index.html")
@app.post("/shows")
def create_user(): 
    name=request.form.get("name") 
    confirmed=request.form.get("price") 
    # if confirmed=="on":    
    # confirmed="true"    
    # else:    
    #confirmed="false"    
    connection=database.connect(host="localhost", user="root", database="bookmyshow")
    cursor=connection.cursor() 
    cursor.execute(f"insert into shows values(default,'{name}',{confirmed})") 
    connection.commit()
    connection.close() 
    cursor.close()
    return redirect("/shows")
@app.get("/shows")
def users():
    data=[] 
    #connection open    
    connection=database.connect(host="localhost", user="root", database="bookmyshow") 
    cursor=connection.cursor() 
    cursor.execute("select * from shows")
    rows=cursor.fetchall()
    for row in rows: 
        data.append({"show_id":row[-2],"movie_name":row[1],"ticket_price":row[2]})
        connection.close() 
        cursor.close()
        # return data    
        return render_template("users.html", shows=data)
app.run(debug=True) #connection close
