from flask import Flask,redirect,render_template,request ,session
import services
from repository import get_db_con
from flask_session import Session

app = Flask(__name__)


@app.route('/')
def home():
    if 'user' in session:
        return render_template('base.html')
    else :
        return render_template('login.html')

@app.route('/create')
def create():
    return render_template('create.html')

@app.route('/migration')
def migrat():
    con = get_db_con()
    if con :
        return "success"
    
    
@app.route('/create-post',methods=['POST','GET'])
def create_post():
    if request.method == 'GET':
        return render_template('create.html')
    
    services.createPost(request.form, request.files)
    return "post create succeess"

# ---------------------------------------------
@app.route('/list-product')
def list_product():
    products = services.getAllProducts()
    return render_template('list_product.html', products=products)


# -------------------------------------------------------
@app.route("/edit/<id>", methods=["GET"])
def edit(id):
    products = services.get_one_product_by_id(id)
    return render_template("edit.html", products=products)
    

@app.route("/edit_submit",methods=['POST'])
def edit_submit():
    id = request.form['id']
    services.update(request.form,request.files,id)
    return redirect('/list-product')

@app.route('/login')
def login():
    return render_template('login.html')

if __name__  == '__main__':
    app.run(debug=True)#,host="192.168.0.182" ,port="3000")