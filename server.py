""" Emotion detection application """
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    '''
        Process GET request from JS client
    '''
    text_to_analyze = request.args.get("textToAnalyze")
    emotions = emotion_detector(text_to_analyze)
    if emotions:
        dominant_emotion = emotions['dominant_emotion']
        emotions.pop('dominant_emotion')
        return f'''For the given statement, the system reponse is {emotions}.
         The dominant emotion is {dominant_emotion}.
        '''
    return "Invalid text! Please try again!"

@app.route("/")
def render_index_page():
    """ Generate home page """
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
