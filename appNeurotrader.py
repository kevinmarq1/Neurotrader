import streamlit as st
import json

st.set_page_config(page_title="NeuroTrader", layout="centered")

st.title("🧠 NeuroTrader Dashboard")
st.write("Bienvenido a la app de predicción financiera basada en modelos de machine learning.")

# Función para cargar resultados desde archivo JSON
def load_results(filename):
    with open(filename, "r") as f:
        return json.load(f)

# Diccionario de modelos y sus archivos
model_files = {
    "RFC/SGD": "results_rfc.json",
    "LSTM": "results_lstm.json",
    "FinBERT (NLP)": "results_nlp.json",
    "XGBoost": "results_xgb.json"
}

# Botones para cada modelo
selected_model = st.sidebar.radio("Selecciona un modelo", list(model_files.keys()))

# Mostrar resultados
results = load_results(model_files[selected_model])

st.subheader(f"📊 Resultados del modelo: {selected_model}")
st.markdown(f"**Fecha de inferencia:** {results.get('fecha', 'Desconocida')}")
st.markdown(f"**Predicción:** {results.get('prediccion', 'Sin datos')}")
st.markdown(f"**Probabilidades:** {results.get('probabilidades', 'Sin datos')}")
st.markdown(f"**Explicación:** {results.get('explicacion', 'Sin explicación disponible')}")

# Mostrar noticia si es FinBERT
if selected_model == "FinBERT (NLP)" and "noticia" in results:
    st.markdown("📰 **Noticia analizada:**")
    st.write(results["noticia"])

# Mostrar valores de referencia si existen
if "valores_referencia" in results:
    st.markdown("📌 **Valores de referencia:**")
    for k, v in results["valores_referencia"].items():
        st.write(f"- {k}: {v}")
