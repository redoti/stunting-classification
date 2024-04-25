import streamlit as st
from sklearn.preprocessing import MinMaxScaler
import joblib

# Fungsi untuk melakukan prediksi
def predict_stunting(data):
    # Load model Decision Tree
    model = joblib.load('model_knn.pkl')

    # Normalisasi data menggunakan MinMaxScaler
    scaler = MinMaxScaler()
    data_normalized = scaler.fit_transform(data)

    # Prediksi stunting atau tidak stunting
    hasil_prediksi = model.predict(data_normalized)
    return hasil_prediksi

# Judul aplikasi
st.title('Prediksi Stunting')

# Form input untuk pengguna
st.write('Masukkan data baru untuk melakukan prediksi:')
age = st.number_input('Age (months)', min_value=0.0)
birth_weight = st.number_input('Birth Weight (kg)', min_value=0.0)
birth_length = st.number_input('Birth Length (cm)', min_value=0.0)
body_weight = st.number_input('Body Weight (kg)', min_value=0.0)
body_length = st.number_input('Body Length (cm)', min_value=0.0)
breastfeeding = st.number_input('Breastfeeding (0 untuk tidak, 1 untuk ya)', min_value=0, max_value=1, step=1)

# Tombol untuk memprediksi
if st.button('Prediksi'):
    # Membuat data baru berdasarkan input pengguna
    data_baru = [[age, birth_weight, birth_length, body_weight, body_length, breastfeeding]]

    # Melakukan prediksi stunting
    hasil_prediksi = predict_stunting(data_baru)

    # Menampilkan hasil prediksi
    if hasil_prediksi[0] == 1:
        st.write('Hasil Prediksi: Stunting')
    else:
        st.write('Hasil Prediksi: Tidak Stunting')
