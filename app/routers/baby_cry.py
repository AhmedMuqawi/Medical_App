from fastapi import APIRouter, UploadFile
import pickle
import wave
import numpy as np
import librosa
from pathlib import Path
# Load the trained model
BASE_DIR = Path(__file__).resolve(strict=True).parent

with open(f"{BASE_DIR}/BabyCry.pkl","rb") as f:
    model = pickle.load(f)

photo = {
    "tired" : "https://res.cloudinary.com/dkeeazjre/image/upload/v1709667113/Photos/jctslebxolctwgsuras5.jpg",
    "belly pain" : "https://res.cloudinary.com/dkeeazjre/image/upload/v1709667122/Photos/tcyaxoef4hww6lhwklzt.jpg",
    "hungry" : "https://res.cloudinary.com/dkeeazjre/image/upload/v1709667131/Photos/x7p2xw9hhs00yijhsoyt.jpg",
    "discomfort" : "https://res.cloudinary.com/dkeeazjre/image/upload/v1709667141/Photos/dwjt39eidjg29abchtof.jpg",
    "burping" : "https://res.cloudinary.com/dkeeazjre/image/upload/v1709667151/Photos/tftrw6gelgl1ucpy0ozb.jpg"

}

router = APIRouter(prefix="/baby_cry_predictor", tags=["Baby Cry Predictor"])

@router.post("/")
def Predicting_emotions(baby_cry_audio:UploadFile):
    try:
        # Read audio data
        with wave.open(baby_cry_audio.file, 'rb') as audio_file:
            audio_data = audio_file.readframes(-1)
            sr = audio_file.getframerate()

        # Extract features
        audio = np.frombuffer(audio_data, dtype=np.int16)
        audio = audio.astype(np.float64)
        mfccs = librosa.feature.mfcc(y=audio, sr=sr)
        mfccs_mean = np.mean(mfccs, axis=1)

        # Make prediction
        prediction = model.predict([mfccs_mean])
        if (prediction[0]=="belly_pain"):
            prediction[0] = "belly pain"

        # Return prediction as string
        return {"feeling" : prediction[0].title(),
                "photo" : photo[prediction[0]]
                }

    except Exception as e:
        # Handle any potential errors during processing
        return {"Error":str(e)}