from flask import Flask,render_template,redirect, url_for, session,request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "GET":
        return render_template("login.html")

    # POST 才處理登入
    uid = request.form.get("userid")
    username = request.form.get("username")
    password = request.form.get("password")

    if username == "admin" and password == "password":
        return redirect(url_for("dashboard"))
    else:
        return "Invalid credentials. Please try again."

@app.route("/sign_up",methods=["POST"]) #暫時封印
def sign_up():
    username = request.form["username"]
    password = request.form["password"]
    # Here you would typically save the new user to a database
    return "Account created successfully!"

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/new_review",methods=["GET", "POST"])
def new_review():
    if request.method == "GET":
       return render_template("new_review.html") 
    restaurant_name = request.form.get("restaurant_name")
    date = request.form.get("date")
    type_of_food = request.form.get("type_of_food")
    cost = request.form.get("cost")
    review = request.form.get("review")
    # Here you would typically save the review to a database
    # 加入上傳照片功能
    # 接入Google Maps API後，存取place_ID以取得位置或其他資訊
    return "Review submitted successfully!"

@app.route("/diary")
def diary():
    #return render_template("diary.html")
    return "SHOW * FROM reviews WHERE user_id = uid"

@app.route("/food_map")
def food_map():
    #return render_template("food_map.html")
    return "Google Maps API integration to show restaurant locations"

if __name__ == "__main__":    
    app.run(debug=True)