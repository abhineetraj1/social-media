from flask import*
from flask import request
import datetime as dt
from flask import request
import os
import shutil as sl
import smtplib
def verify_mail(at,u,p):
	try:
	    sttt = smtplib.SMTP('smtp.gmail.com', 587)
	    sttt.starttls()
	    sttt.login("hacker.route.47@gmail.com", "12hin55t")
	    message="From:Abhineet Raj Codes\nSubject:Login verification\nThank you for signing up with Abhineet Raj Codes.\nYou can now login to members area using the details below:\nURL: https://codes.abhineetraj.me\nUsername: "+u+"\nPassword: "+p+"\n\nThank you :)\n\nIf this was not you then you can delete your account here - https://codes.abhineetraj.me/delete\nand report your issue here - https://codes.abhineetraj.me/help"
	    sttt.sendmail("hacker.route.47@gmail.com", at, message)
	    return "Y"
	except:
		return "X"
class arw:
		def add_issue(a):
			open("ISSUES/"+str(dt.datetime.now()).replace(":","").replace(".","")+".txt","a").write(a)
		def add_post(a,b):
				name="static/"+str(dt.datetime.now()).replace(":","").replace(".","")+" "+a
				open(name,"a").write(b)
		def get_content():
				l = os.listdir("static")
				#l.reverse()
				n=0
				k=""
				if (l==None):
					return ""
				else:
					while(len(l)>n):
						k=k+open("static/"+l[n],"r+").read()+"\n"
						n=n+1
					return k
		def create(a,b,c):
			if (a in os.listdir("ACC")):
				return "X"
			else:
				if (verify_mail(c,a,b)=="Y"):
					os.mkdir("ACC/"+a)
					os.mkdir("ACC/"+a+"/"+"Name-"+c)
					os.mkdir("ACC/"+a+"/"+"Password-"+b)
					return "Y"
				else:
					return "x"
		def change_pass(a,b):
			oo=os.listdir(("ACC/"+a))
			if ("Password-" in oo[0]):
				sl.rmtree("ACC/"+a+"/"+oo[0])
				os.mkdir("ACC/"+a+"/"+"Password-"+b)
			else:
				sl.rmtree("ACC/"+a+"/"+oo[1])
				os.mkdir("ACC/"+a+"/"+"Password-"+b)
			return "Y"
		def delete_comment(a):
				bc = os.listdir("static")
				n=0
				while(len(bc)>n):
					if(a == bc[n].split(" ")[1]):
						os.remove("static/"+bc[n])
					else:
						tg=""
					n=n+1
		def delete(a):
			arw.delete_comment(a)
			sl.rmtree("ACC/"+a)
		def verify(a,b):
				if (a in os.listdir("ACC")):
						f = os.listdir("ACC/"+a)
						n=0
						k=[]
						while(len(f) > n):
								if ("Password-"in f[n]):
										if(b == f[n].replace("Password-","")):
												k.append("d")
										else:
												jk=""
								else:
										jk=""
								n=n+1
						if (len(k)>0):
								return "Y"
						else:
								return "Xpassword"
				else:
						return "X"
app = Flask(__name__,static_folder="assets")
@app.route("/")
def main():
		return open("main.html","r+").read()
@app.route("/create",methods=["GET","POST"])
def a():
		if (request.method == "POST"):
				c = request.form["name"]
				a = request.form["username"]
				b = request.form["password"]
				if (len(b)>10):
						if (len(a)<4):
								"<script>setTimeout(m,1);\n\nfunction m(){alert('Please enter the valid username');}</script>" + open("index.html","r+").read()
						else:
								r = arw.create(a,b,c)
								if (r == "X"):
									return "<script>setTimeout(m,1);\n\nfunction m(){alert('Account with this username already exist');}</script>" + open("index.html","r+").read()
								elif(r == "x"):
									return "<script>setTimeout(m,1);\n\nfunction m(){alert('Enter the valid email ID');}</script>" + open("index.html","r+").read()
								else:
									return open("index.html","r+").read() +"<script>alert('Your account has been made , now sign in with those credentials');</script>"
				else:
						return "<script>setTimeout(m,1);\n\nfunction m(){alert('Enter the password of more than 10 digits');}</script>" + open("index.html","r+").read()
		else:
			return open("index.html","r+").read()
@app.route("/contact", methods=["GET","POST"])
def mn3():
	if (request.method == "GET"):
		return arw.read("404.html")
	else:
		w=request.files["file"]
		name="contact/"+str(dt.datetime.now()).replace(":","").replace(".","").replace("-","")
		os.mkdir(name)
		msg = request.form["name"]+"\n"+request.form["email"]+"\n"+request.form["message"]
		open(name+"/data.txt","w+").write(msg)
		if (w.filename==""):
			t=""
		else:
			w.save(name+"/"+w.filename)
		return "<script>alert('Your message has been sent!');</script>" + '<script>var a = document.createElement("a");a.href="http://abhineetraj.me/contact.html";a.click();</script>'

@app.route("/login",methods=["GET","POST"])
def b():
		if (request.method == "POST"):
				g = arw.verify(request.form["username"],request.form["password"])
				if (g == "X"):
						return "<script>alert('There is no such account')</script>" + open("index.html","r+").read()
				elif (g=="Xpassword"):
						return "<script>alert('Your password is wrong');</script>" + open("index.html","r+").read()
				else:
						return "<script>localStorage.setItem('username',"+"'"+request.form["username"]+"'"+")</script>"+(open("post.html","r+").read()).replace('cttntbntt',arw.get_content())
		else:
			 return open("index.html","r+").read()
@app.route("/change_pss",methods=["GET","POST"])
def b1():
		if (request.method == "POST"):
			g = arw.change_pass(request.form["username"],request.form["password"])
			return (open("post.html","r+").read()).replace('cttntbntt',arw.get_content())+"<script>alert('Your password has been changed');</script>"
		else:
			return open("reset.html","r+").read()
tcca="""
Make sure you are 15+ and know the basics of tech and coding related stuffs.
"""
@app.route("/tc",methods=["GET"])
def mm():
    return tcca
@app.route("/post",methods=["GET","POST"])
def c():
		if (request.method == "POST"):
				if (len(request.form["text"])>3000):
						return "<script>alert('Don't exceed the limit of 3000 characters);</script>"+open("post.html","r+").read()
				elif (len(request.form["text"])<5):
						return "<script>alert('Enter the valid information');</script>"+open("post.html","r+").read()
				else:
						arw.add_post(request.form["username"],request.form["text"])
						return (open("post.html","r+").read()).replace('cttntbntt',arw.get_content())
		else:
				return (open("post.html","r+").read()).replace('cttntbntt',arw.get_content())
@app.route("/refresh",methods=["GET"])
def e():
	return (open("post.html","r+").read()).replace('cttntbntt',arw.get_content())
@app.route("/delete",methods=["GET","POST"])
def d():
		if (request.method== "POST"):
				if(arw.verify(request.form["username"],request.form["password"])=="Y"):
						arw.delete(request.form["username"])
						arw.delete_comment(request.form["username"])
						return open("delete_arg.html","r+").read()
				else:
						return "<script>setTimeout(m,1);\n\nfunction m(){alert('Your password or username is wrong');}</script>" + open("delete.html","r+").read()
		else:
				return open("delete.html","r+").read()
@app.route("/delete_comment",methods=["GET","POST"])
def g():
	if (request.method == "POST"):
		if (request.form["text"] in os.listdir("ACC")):
			arw.delete_comment(request.form["text"])
			return "<script>alert('Your all comments are deleted.');</script>"+ (open("post.html","r+").read()).replace('cttntbntt',arw.get_content())
		else:
			return "ERROR 501"
	else:
		return (open("post.html","r+").read()).replace('cttntbntt',arw.get_content())
@app.route("/help",methods=["GET","POST"])
def f():
	if (request.method == "POST"):
		arw.add_issue(request.form["text"])
		return "<script>alert('Your report has been submitted');</script>"+(open("post.html","r+").read()).replace('cttntbntt',arw.get_content())
	else:
		return open("help.html","r").read()
if "__main__" == __name__:
	app.run()