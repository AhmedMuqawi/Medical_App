from fastapi import APIRouter
import pickle
import wave
import numpy as np
import librosa


router = APIRouter(prefix="/GIT", tags=["GIT diseases"])
