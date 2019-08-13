from flask import Flask,request,render_template
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import io
import base64
app=Flask(__name__)

@app.route('/')
def index():
    x=np.arange(1,11)
    y=x**2
    plt.plot(x,y)
    img=io.BytesIO()
    plt.savefig(img,format='png')
    graphurl=base64.b64encode(img.getvalue()).decode()
    return render_template('templates.html',graphInfo=graphurl)




if __name__ =='__main__':
    app.run(debug=True)