import streamlit as st
import requests
from fpdf import FPDF
from datetime import datetime
import io

# ==========================================================
# UUDEN AJAN VIISAUS - THE NEWBORN'S GAZE V1.3.0
# ==========================================================
st.set_page_config(page_title="Newborn's Gaze", page_icon="⚖️", layout="centered")

# Mobiilioptimointi ja tyylittely
st.markdown("""
    <style>
    .stTextArea textarea { font-size: 16px !important; }
    .stButton button { 
        width: 100%; 
        height: 3.5em; 
        background-color: #1a237e; 
        color: white; 
        border-radius: 15px;
        font-weight: bold;
        border: none;
    }
    .stButton button:hover { background-color: #283593; color: white; }
    .status-box { 
        padding: 20px; 
        border-radius: 15px; 
        background-color: #ffffff; 
        border-left: 5px solid #1a237e;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

def luo_pdf_bytes(tuomio, saastot):
    pdf = FPDF()
    pdf.add_page()
    # Otsikko
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(200, 10, txt="UUDEN AJAN VIISAUS - THE NEWBORN'S GAZE", ln=True, align='C')
    pdf.set_font("Arial", 'I', 10)
    pdf.cell(200, 10, txt="Legal Standard: THE NEWBORN CRITERION", ln=True, align='C')
    pdf.ln(10)
    
    # Säästölaskuri osio
    pdf.set_fill_color(240, 240, 240)
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(0, 10, txt="VIISAUDEN JA SAASTON LASKURI (Arvio):", ln=True, fill=True)
    pdf.set_font("Arial", size=10)
    pdf.multi_cell(0, 8, txt=saastot)
    pdf.ln(10)
    
    # Tuomio
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(0, 10, txt="TUOMIO JA PERUSTELUT:", ln=True)
    pdf.set_font("Arial", size=11)
    
    # Tekstin puhdistus PDF-yhteensopivaksi
    siistitty = tuomio.encode('latin-1', 'replace').decode('latin-1')
    pdf.multi_cell(0, 8, txt=siistitty)
    
    return pdf.output(dest='S').encode('latin-1')

# --- KÄ
