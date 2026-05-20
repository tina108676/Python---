from flask import Flask,render_template,redirect, url_for,request

app = Flask(__name__)

@app.route("/")
def index():
    ann = request.args.get("ann")
    return render_template("index.html", announce=ann)
    #登入、註冊按鈕，分別前往/login、/sign_up頁面
    #確認變數announce，若不為空，依announce類型(=="new_account_created")顯示成功創建新帳號訊息
    #^詳見底下/sign_up

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    # 1. 帳號、密碼輸入欄(先用admin(2)和password)及登入(提交)按鈕
    # 2. 註冊按鈕，前往/sign_up頁面
    #確認有無回傳變數error，內容為登入失敗訊息(字串)
    #見下方else

    #admin2為飲控模式ON使用者

    uid = request.form.get("userid")
    password = request.form.get("password")

    if (uid == "admin" or uid == "admin2") and password == "password":
        return redirect(url_for("dashboard", user=uid))

    else:
        return render_template("login.html", error="Invalid credentials. Please try again.")

@app.route("/sign_up",methods=["POST"]) 
def sign_up():
    uid = request.form["userid"]
    username = request.form["username"]
    password = request.form["password"]
    #帳號、使用者名稱、密碼輸入欄(測試時new_user以外帳號視為已被使用)及註冊(提交)按鈕
    #確認有無回傳變數error，內容為註冊失敗訊息(字串)

    if uid=="new_user":
        return redirect(url_for("index", ann="new_account_created"))
    else:
        return render_template("sign_up.html", error="Account already exists. Please try again.")
    
@app.route("/dashboard")
def dashboard():
    user = request.args.get("user")
    ann = request.args.get("ann")
    return render_template("dashboard.html", user=user, announce=ann)
    #主要按鈕：新增日記、查看日記、找餐廳，分別前往/new_review、/diary、/food_map頁面
    #熱量紀錄按鈕，如果user=="admin2"(飲控使用者)才啟用，前往/calorie_intake頁面
    #登出、設定按鈕，分別前往/、/setting頁面
    #確認變數announce，若不為空，依announce類型(=="review_submitted")顯示成功新增日記訊息
    #前往除home page(登出)以外頁面都需要付上query string告知uid(變數名稱為user)
    #例(AI生成)：<a href="{{ url_for('profile', user=current_user_id) }}">Go to Profile</a>


@app.route("/new_review",methods=["GET", "POST"])
def new_review():
    user = request.args.get("user")
    if request.method == "GET":
       return render_template("new_review.html") 
    #餐廳名稱、日期、區域、類型、花費(人均)、評語的輸入欄(或選單)，變數名稱如下
    #如果可以加入上傳照片功能，刪除下方3+3個引號啟用
    restaurant_name = request.form.get("restaurant_name")
    date = request.form.get("date")
    type_of_food = request.form.get("type_of_food")
    cost = request.form.get("cost")
    review = request.form.get("review")
    '''
    picture = request.form.get("picture")
    '''
    # 加入上傳照片功能
    # Here you would typically save the review to a database
    # 接入Google Maps API後，存取place_ID以取得位置或其他資訊
    if user == "admin":
        return redirect(url_for("dashboard", user=user, ann="review_submitted"))
    elif user == "admin2":
        return redirect(url_for("calorie_intake", user=user))

@app.route("/diary")
def diary():
    #return render_template("diary.html")
    return "SHOW * FROM reviews WHERE user_id = uid"

@app.route("/food_map")
def food_map():
    #return render_template("food_map.html")
    return "Google Maps API integration to show restaurant locations"

@app.route("/calorie_intake")
def calorie_intake():
    return "404 :("

@app.route("/setting")
def setting():
    return "404 :("

if __name__ == "__main__":    
    app.run(debug=True)