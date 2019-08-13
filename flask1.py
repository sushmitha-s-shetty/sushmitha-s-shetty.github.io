from flask import Flask,request,render_template
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import io
import base64
app=Flask(__name__)

"""
@app.route('/')
def index():
    return render_template('templates.html')

def compute():
     a=10
     b=20
     c=a+b
     return "the sum of{} and{} two number {}".format(a,b,c)

@app.route('/display',methods=['POST'])
def display():
    name=request.form.get('name')     
    #print(name)
    return "hello"+name

if __name__ =='__main__':
    app.run(debug=True)
"""

@app.route('/')
def index():
    x=np.arange(1,11)
    y=x**2
    plt.plot(x,y)
    img=io.BytesIO()
    plt.savefig(img,front='png')
    graphurl=base64.b64encode(img.getvalue()).decode()
    return graphurl




if __name__ =='__main__':
    app.run(debug=True)