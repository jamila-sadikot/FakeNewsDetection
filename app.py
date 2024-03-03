# from flask import Flask, escape, request, render_template
# import pickle
# from sklearn.feature_extraction.text import TfidfVectorizer


# vector= TfidfVectorizer(stop_words ='english',max_df=0.7)

# model=pickle.load(open("finalized_model.pkl", 'rb'))

# app = Flask(__name__)

# @app.route("/")
# def home():
#     return render_template("index.html")

# @app.route('/prediction',methods=['GET','POST'])
# def prediction():
#     if request.method == "POST":
#     if __name__ == "__main__":
#         app.run()




    # app.run()
    
    
    
    
from flask import Flask, escape, request, render_template
import pickle
# from sklearn.feature_extraction.text import TfidfVectorizer
  
vector = pickle.load(open("vectorizer.pkl", 'rb'))
model = pickle.load(open("finalized_model.pkl", 'rb'))

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/prediction', methods=['GET', 'POST'])
def prediction():
    if request.method == "POST":
        news=str(request.form['news'])
        print(news)
        
        predict=model.predict(vector.transform([news]))
        print(predict)
        
        return render_template("prediction.html", prediction_text="News headline is -> {}".format(predict))[0]
    
    
    else:
        return render_template("prediction.html")

if __name__ == "__main__":
    app.run()
