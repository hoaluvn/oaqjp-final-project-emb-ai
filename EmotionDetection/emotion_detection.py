import json
import requests

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    jsobj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json=jsobj, headers=headers)
    if response.status_code == 200:
        myjson = json.loads(response.text)
        emotions = myjson['emotionPredictions'][0]['emotion']
        dominant_score = 0
        dominant_emotion = None
        # Find dominant emotion
        for k in emotions:
            if emotions[k] > dominant_score:
                dominant_score = emotions[k]
                dominant_emotion = k
        emotions['dominant_emotion'] = dominant_emotion
        return emotions
    elif response.status_code == 400:
        return None
