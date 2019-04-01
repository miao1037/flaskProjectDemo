from flask import Flask,render_template,request,redirect,make_response
import datetime
from  orm import model
from orm import ormmanage as manage
app =Flask(__name__)

# 配置缓存更新时间
app.send_file_max_age_default = datetime.timedelta(seconds=1)
app.debug=True

@app.route('/')
def index():
    # return 'helloword'
    b1 = model.Book(1,"倚天屠龙记",10)
    b2 = model.Book(2,"天龙八部",20)
    b3 = model.Book(3,"鹿鼎记",25)
    user = None
    user = request.cookies.get("id")

    if user:
        print("已经登陆过")
    else:
        print("没有登录")



    return render_template("index.html",booklist = [b1,b2,b3],userinfo = user)


@app.route("/news/<int:num>")
def news(num):

    # print(num,type(num))
    # limit(20,20)
    # pagenews 根据num查询数据库更改
    return render_template("news.html",pagenews=['股票跌了','放假','清明节'])

# 注册
@app.route("/regist",methods = ["GET","POST"])
def regist():
    if request.method == "GET":
        # args = request.args
        # name = args.get("name")
        # value1 = args.get("value1")
        # print(name,value1)
        # print("注册页面，收到get请求")
        return render_template("regist.html")
    elif request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        # print(username,password)
        # print("提取注册表单参数，收到post请求")
        # return "注册成功，请登录！"

        try:
            manage.insertUser(username, password)
            return redirect("/login")
        except:
            redirect("/regist")



#登录
@app.route("/login",methods = ["GET","POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        # 查询数据库
        print(username,password)
        # return "登录成功"
        # 内容需要查询数据库
        # return render_template("list.html",infoarry = [1,2,3,4,5])

        #内容需要查询数据库
        #第一种不带接口
        # return render_template("list.html",infoarry = [1,2,3,4,5])
        #第二种带接口 重定向
        #自动在URL发起请求 请求list

        # 为了让响应可以携带头信息，需要构造响应

        try:
           result = manage.checkUser(username,password)
           res = make_response(redirect("/list"))
           res.set_cookie('id', result, expires=datetime.datetime.now() + datetime.timedelta(days=7))
           return res
        except:
            return redirect("/login")



@app.route("/quit")
def quit():
    res = make_response(redirect("/"))
    res.delete_cookie("id")
    return res


@app.route("/list")
def list():
    user = None
    user = request.cookies.get("name")

    return render_template("list.html",infoarry = [1,2,3,4,5],userinfo = user)



@app.route("/detail/<id>")
def detail(id):

    print("当前商品为",id)

    user = None
    user = request.cookies.get("name")
    #从数据库查询商品详情
    return render_template("detail.html",detail = "qwq",id = id,userinfo = user)


















if __name__=="__main__":
    app.run()





