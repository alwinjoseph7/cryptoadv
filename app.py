from flask import Flask, render_template, request, redirect
import os
import os.path
from nadivsor import calc

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    message=0
    #profit=0.0
    if request.method == "POST":
        print("FORM DATA RECEIVED")
        
        # if "file" not in request.files and "message" not in request.form.get:
        #     return redirect(request.url)
        message = request.form.get("message",type=float)
        # if file.filename == "" and message == "":
        #     return redirect(request.url)
        if message:
            print("Received message: ", message)
            val = calc(message)
            message = val

    return render_template("index.html", message = message)


if(__name__ == "__main__"):
    app.run(debug=True, threaded=True) 