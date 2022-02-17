#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask


# In[2]:


app2 = Flask(__name__)


# In[3]:


from flask import request, render_template
from keras.models import load_model

@app2.route("/", methods = ["GET", "POST"])
def index():
    if request.method == "POST":
        NPTA = request.form.get("NPTA")
        TLTA = request.form.get("TLTA")
        WCTA = request.form.get("WCTA")
        print(NPTA, TLTA, WCTA)
        model = load_model("bankruptcy")
        pred = model.predict([[float(NPTA), float(TLTA), float(WCTA)]])
        s = "The predicted bankruptcy score is : " + str(pred)
        return(render_template("index2.html", result = s))
    else:
        return(render_template("index2.html", result = "2"))
    


# In[ ]:


if __name__ == "__main__":
    app2.run()


# In[ ]:




