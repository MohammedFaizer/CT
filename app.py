# importing Flask and other modules
from flask import Flask, request, render_template
import pymongo
import app2
# Flask constructor
app = Flask(__name__)
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabases"]
mycol = mydb["customerss"]
# A decorator used to tell the application
# which URL is associated function
@app.route('/', methods =['GET', 'POST'])
def gfg():
   if request.method == "POST":
      first_name = request.form.get('fname')
      last_name = request.form.get('lname')
      mydict = { "name":first_name, "address":last_name }
      mycol.insert_one(mydict)
      app2.main()
      return render_template("iopk.html")
      
   return render_template("index.h")
if __name__=='__main__':
   app.run()




