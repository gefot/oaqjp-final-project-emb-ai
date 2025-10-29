import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, headers=header, json=myobj)

    if response.status_code != 200:
            return {"error": f"API request failed with status {response.status_code}"}

    result = response.json()
    emotions = result['emotionPredictions'][0]['emotion']

    # Find the dominant emotion
    dominant_emotion = max(emotions, key=emotions.get)

    # Construct the output dictionary
    output = {
        'anger': emotions.get('anger', 0.0),
        'disgust': emotions.get('disgust', 0.0),
        'fear': emotions.get('fear', 0.0),
        'joy': emotions.get('joy', 0.0),
        'sadness': emotions.get('sadness', 0.0),
        'dominant_emotion': dominant_emotion
    }

    return output

