import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Konfigurasi Halaman Web
st.set_page_config(page_title="Prediksi Stroke", page_icon="🧠", layout="centered")

# Memuat Model dan Scaler
# Cache digunakan agar model tidak di-load ulang setiap kali ada interaksi di web
@st.cache_resource
def load_components():
    model = joblib.load('model_xgboost_stroke.pkl')
    scaler = joblib.load('scaler_stroke.pkl')
    return model, scaler

model, scaler = load_components()

# Judul dan Deskripsi Aplikasi
st.title("Sistem Prediksi Risiko Stroke")
st.markdown("""
Aplikasi ini memprediksi risiko penyakit stroke berdasarkan data kesehatan pasien. 
Silakan masukkan data pasien pada formulir di bawah ini.
""")
st.divider()

# Membuat Formulir Input dengan layout kolom
col1, col2 = st.columns(2)

with col1:
    st.subheader("Data Demografi")
    age = st.number_input("Umur (Tahun)", min_value=0.0, max_value=120.0, value=45.0, step=1.0)
    gender = st.selectbox("Jenis Kelamin", ["Male", "Female"])
    ever_married = st.selectbox("Pernah Menikah?", ["Yes", "No"])
    work_type = st.selectbox("Tipe Pekerjaan", ["Private", "Self-employed", "Govt_job", "children", "Never_worked"])
    residence_type = st.selectbox("Tipe Tempat Tinggal", ["Urban", "Rural"])

with col2:
    st.subheader("Data Kesehatan")
    bmi = st.number_input("BMI (Body Mass Index)", min_value=10.0, max_value=100.0, value=28.1, step=0.1)
    avg_glucose_level = st.number_input("Rata-rata Level Glukosa", min_value=50.0, max_value=300.0, value=91.8, step=0.1)
    hypertension = st.selectbox("Memiliki Hipertensi?", ["No", "Yes"])
    heart_disease = st.selectbox("Memiliki Penyakit Jantung?", ["No", "Yes"])
    smoking_status = st.selectbox("Status Merokok", ["never smoked", "formerly smoked", "smokes", "Unknown"])

# Tombol Prediksi
st.divider()
submit_button = st.button("Lakukan Analisis Prediksi", use_container_width=True, type="primary")

# Logika Prediksi saat tombol ditekan
if submit_button:
    # Mapping Input UI ke Format OHE (One-Hot Encoding)
    # Fitur harus PERSIS urutannya dengan X_train di Colab
    input_data = {
        'age': age,
        'hypertension': 1 if hypertension == "Yes" else 0,
        'heart_disease': 1 if heart_disease == "Yes" else 0,
        'avg_glucose_level': avg_glucose_level,
        'bmi': bmi,
        'gender_Male': 1 if gender == "Male" else 0,
        'ever_married_Yes': 1 if ever_married == "Yes" else 0,
        'work_type_Never_worked': 1 if work_type == "Never_worked" else 0,
        'work_type_Private': 1 if work_type == "Private" else 0,
        'work_type_Self-employed': 1 if work_type == "Self-employed" else 0,
        'work_type_children': 1 if work_type == "children" else 0,
        'Residence_type_Urban': 1 if residence_type == "Urban" else 0,
        'smoking_status_formerly smoked': 1 if smoking_status == "formerly smoked" else 0,
        'smoking_status_never smoked': 1 if smoking_status == "never smoked" else 0,
        'smoking_status_smokes': 1 if smoking_status == "smokes" else 0
    }
    
    # Konversi ke DataFrame
    df_input = pd.DataFrame([input_data])
    
    # Lakukan Scaling
    scaled_input = scaler.transform(df_input)
    
    # Lakukan Prediksi
    prediction = model.predict(scaled_input)[0]
    probabilitas = model.predict_proba(scaled_input)[0][1]
    
    # Tampilkan Hasil dengan UI
    st.subheader("Hasil Analisis:")
    
    if prediction == 1:
        st.error(f"**Peringatan:** Pasien terdeteksi memiliki **RISIKO TINGGI** terkena stroke.")
        st.write(f"Tingkat Risiko Stroke: **{probabilitas * 100:.2f}%**")
        st.progress(float(probabilitas))
    else:
        st.success(f"**Aman:** Pasien terdeteksi memiliki risiko stroke yang **RENDAH**.")
        st.write(f"Tingkat Risiko Stroke: **{probabilitas * 100:.2f}%**")
        st.progress(float(probabilitas))