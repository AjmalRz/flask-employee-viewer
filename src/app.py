from flask import Flask,render_template,request
from flask_mysqldb import MySQL
app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '1234'
app.config['FILE_UPLOADS']=r"D:\PycharmProjects\dataconverter\src\static\upload"
mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/details',methods=['GET','POST'])
def details():
    if request.method == 'POST':
        empid=request.form.get("empid")
        cur=mysql.connection.cursor()
        cur.execute('USE emp;')
        
        cur.execute(f'SELECT name,address,age,gender,salary from data WHERE id={empid}')
        show=cur.fetchall()
        tb=[]
        for sho in show:
            for sh in sho:
                tb.append(sh) 
        name=(tb[0])
        address=tb[1]
        age=tb[2]
        gender=tb[3]
        salary=tb[4]
    return render_template('details.html',name=name,address=address,age=age,gender=gender,salary=salary)
    
