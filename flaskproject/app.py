import os.path
from flask import Flask, Response, g, render_template, jsonify
from flaskproject.queries import availability

app = Flask(__name__)
app.config.from_object(__name__)
app.debug=True
 


@app.route('/')
def root():  
    return render_template('DublinBikes.html')
    


@app.route("/test/<int:stand_no>", methods=['GET'])
def avail(stand_no):      
    #print("stand no is: %d" % stand_no)
    return availability(stand_no)


        
        
if __name__ == '__main__':  
    app.run(port=8080)
