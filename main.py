from flask import Flask, render_template, request
import requests
import bargraph

app = Flask(__name__)


def query(API_URL, headers, payload):
  response = requests.post(API_URL, headers=headers, json=payload)
  return response.json()


def inference_model(text):

  API_URL = "https://api-inference.huggingface.co/models/TheJournal/good_sentiment_model4"
  headers = {"Authorization": "Bearer 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"}

  output = query(API_URL, headers, {
    "inputs": text,
  })
  return output

# def inference_model(text):
  
#   API_URL = "https://api-inference.huggingface.co/models/TheJournal/higher_accuracy_Bert_Model"
#   headers = {"Authorization": "Bearer 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"}	
  
#   output = query(API_URL, headers, {
# 	"inputs": text,

# })
#   return output

# def query(API_URL, headers, payload):
# 	response = requests.post(API_URL, headers=headers, json=payload)
# 	return response.json()




@app.route('/')
def index():
  return render_template('index.html')


@app.route('/index.html')
def new_home():
  return render_template('index.html')


@app.route('/aboutus.html')
def aboutus():
  return render_template('aboutus.html')


@app.route('/model.html', methods=['GET'])
def model():
  return render_template('model.html', showGraph=False)


@app.route('/model.html', methods=['POST'])
def getTweet():
  if request.method == 'POST':
    text = request.form['tweet_text']
    sentiments = inference_model(str(text))
    labels, scores, fig = postProcess(sentiments)
    return render_template('model.html',
                           textarea_data=labels[0:3],
                           showGraph=True,
                           figureData=fig)


def postProcess(modelAns):
  sentiments = modelAns[0]
  labels = [item['label'] for item in sentiments]
  scores = [item['score'] for item in sentiments]
  fig = bargraph.create_bar_graph(labels, scores)
  return labels, scores, fig


@app.errorhandler(Exception)
def handle_error(error):
  return render_template('error.html', error=error)


app.run(host='0.0.0.0', port=81)
