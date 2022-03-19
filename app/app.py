#carregando as bibliotecas
import pandas as pd
import streamlit as st
from minio import Minio
import joblib
import matplotlib.pyplot as plt
from pycaret.classification import load_model, predict_model