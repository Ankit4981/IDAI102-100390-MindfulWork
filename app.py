import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime, timedelta
import random
import time

# ══════════════════════════════════════════════════
#  PAGE CONFIG
# ══════════════════════════════════════════════════
st.set_page_config(
    page_title="MindfulWork – Smart Stress Relief",
    page_icon="🧘",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ══════════════════════════════════════════════════
#  GLOBAL CSS — Vibrant Rainbow / Warm Food Palette
# ══════════════════════════════════════════════════
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;1,400&family=Nunito:wght@300;400;500;600;700&display=swap');

/* ═══════════════════════════════════════
   CSS VARIABLES — Rainbow food palette
═══════════════════════════════════════ */
:root {
    --c-coral:    #FF6B6B;
    --c-orange:   #FF9A3C;
    --c-amber:    #FFD166;
    --c-lime:     #95E06C;
    --c-mint:     #06D6A0;
    --c-sky:      #74C7EC;
    --c-lavender: #C77DFF;
    --c-rose:     #FF6EB4;
    --c-peach:    #FFAD60;
    --c-berry:    #E040FB;
    --bg-dark:    #1a0f2e;
    --bg-mid:     #231535;
    --bg-card:    rgba(255,255,255,0.04);
    --text-main:  #f5f0ff;
    --text-muted: #b8a9d4;
    --text-dim:   #7a6d99;
}

/* ═══════════════════════════════════════
   KEYFRAME ANIMATIONS
═══════════════════════════════════════ */
@keyframes fadeInUp {
    from { opacity: 0; transform: translateY(24px); }
    to   { opacity: 1; transform: translateY(0); }
}
@keyframes fadeInDown {
    from { opacity: 0; transform: translateY(-20px); }
    to   { opacity: 1; transform: translateY(0); }
}
@keyframes fadeInLeft {
    from { opacity: 0; transform: translateX(-24px); }
    to   { opacity: 1; transform: translateX(0); }
}
@keyframes glowPulse {
    0%, 100% { box-shadow: 0 0 18px rgba(255,107,107,0.2), 0 0 40px rgba(255,154,60,0.08); }
    50%       { box-shadow: 0 0 30px rgba(255,209,102,0.3), 0 0 60px rgba(6,214,160,0.15); }
}
@keyframes shimmer {
    0%   { background-position: -200% center; }
    100% { background-position:  200% center; }
}
@keyframes float {
    0%, 100% { transform: translateY(0px); }
    50%       { transform: translateY(-6px); }
}
@keyframes rotateGlow {
    0%   { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
}
@keyframes particleDrift {
    0%   { transform: translate(0,0) scale(1);   opacity: 0.6; }
    50%  { transform: translate(20px,-30px) scale(1.1); opacity: 1; }
    100% { transform: translate(-10px,10px) scale(0.9); opacity: 0.4; }
}
@keyframes borderRainbow {
    0%   { border-color: rgba(255,107,107,0.5); }
    25%  { border-color: rgba(255,209,102,0.5); }
    50%  { border-color: rgba(6,214,160,0.5); }
    75%  { border-color: rgba(116,199,236,0.5); }
    100% { border-color: rgba(255,107,107,0.5); }
}
@keyframes countUp {
    from { opacity: 0; transform: scale(0.7); }
    to   { opacity: 1; transform: scale(1); }
}
@keyframes slideInRight {
    from { opacity: 0; transform: translateX(30px); }
    to   { opacity: 1; transform: translateX(0); }
}
@keyframes breatheCircle {
    0%, 100% { transform: scale(1);    opacity: 0.7; }
    50%       { transform: scale(1.15); opacity: 1;   }
}
@keyframes gradientShift {
    0%   { background-position: 0%   50%; }
    50%  { background-position: 100% 50%; }
    100% { background-position: 0%   50%; }
}
@keyframes rainbowText {
    0%   { background-position: 0%   50%; }
    50%  { background-position: 100% 50%; }
    100% { background-position: 0%   50%; }
}
@keyframes warmPulse {
    0%, 100% { text-shadow: 0 0 8px rgba(255,154,60,0.6), 0 0 20px rgba(255,107,107,0.3); }
    50%       { text-shadow: 0 0 16px rgba(255,209,102,0.9), 0 0 40px rgba(255,154,60,0.5); }
}
@keyframes ripple {
    0%   { transform: scale(0.8); opacity: 1;   }
    100% { transform: scale(2.2); opacity: 0;   }
}
@keyframes scanLine {
    0%   { top: -10%; }
    100% { top: 110%; }
}

/* ═══════════════════════════════════════
   BASE
═══════════════════════════════════════ */
html, body, [class*="css"] { font-family: 'Nunito', sans-serif; }

.stApp {
    background: linear-gradient(135deg, #1a0f2e 0%, #231535 35%, #1e1040 65%, #150d25 100%);
    color: var(--text-main);
    background-size: 400% 400%;
    animation: gradientShift 25s ease infinite;
}

/* Animated ambient rainbow blobs */
.stApp::before {
    content: '';
    position: fixed;
    top: 0; left: 0; right: 0; bottom: 0;
    background-image:
        radial-gradient(circle at 15% 20%, rgba(255,107,107,0.07) 0%, transparent 40%),
        radial-gradient(circle at 85% 75%, rgba(6,214,160,0.07) 0%, transparent 40%),
        radial-gradient(circle at 50% 10%, rgba(255,209,102,0.05) 0%, transparent 35%),
        radial-gradient(circle at 80% 20%, rgba(199,125,255,0.05) 0%, transparent 30%),
        radial-gradient(circle at 20% 80%, rgba(116,199,236,0.05) 0%, transparent 30%);
    pointer-events: none;
    z-index: 0;
    animation: particleDrift 15s ease-in-out infinite alternate;
}

/* ═══════════════════════════════════════
   SIDEBAR
═══════════════════════════════════════ */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #120a22 0%, #1a0f2e 50%, #1e1040 100%) !important;
    border-right: 1px solid rgba(255,154,60,0.2) !important;
    box-shadow: 4px 0 30px rgba(0,0,0,0.5) !important;
    animation: fadeInLeft 0.6s ease-out;
}
[data-testid="stSidebar"] * { color: #e8d5ff !important; }
[data-testid="stSidebar"] .stRadio label {
    font-size: 15px !important; font-weight: 500 !important;
    padding: 8px 12px !important;
    border-radius: 10px !important;
    transition: all 0.2s ease !important;
    border: 1px solid transparent !important;
}
[data-testid="stSidebar"] .stRadio label:hover {
    background: rgba(255,154,60,0.1) !important;
    border-color: rgba(255,154,60,0.25) !important;
    padding-left: 18px !important;
}

/* ═══════════════════════════════════════
   METRIC CARDS — rainbow glow
═══════════════════════════════════════ */
[data-testid="metric-container"] {
    background: rgba(255,255,255,0.04) !important;
    border: 1px solid rgba(255,154,60,0.3) !important;
    border-radius: 18px !important;
    padding: 18px !important;
    backdrop-filter: blur(12px) !important;
    transition: all 0.3s ease !important;
    animation: fadeInUp 0.5s ease-out both, glowPulse 5s ease-in-out infinite !important;
    position: relative;
    overflow: hidden;
}
[data-testid="metric-container"]::before {
    content: '';
    position: absolute;
    top: 0; left: -100%;
    width: 60%; height: 100%;
    background: linear-gradient(90deg, transparent, rgba(255,154,60,0.08), transparent);
    animation: shimmer 3s infinite;
}
[data-testid="metric-container"]:hover {
    transform: translateY(-4px) !important;
    border-color: rgba(255,209,102,0.6) !important;
    box-shadow: 0 10px 40px rgba(255,154,60,0.2) !important;
}
[data-testid="metric-container"] label { color: var(--text-muted) !important; font-size: 13px !important; }
[data-testid="metric-container"] [data-testid="stMetricValue"] {
    background: linear-gradient(135deg, #FF9A3C, #FFD166);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    font-size: 28px !important; font-weight: 800 !important;
    animation: countUp 0.6s cubic-bezier(0.175,0.885,0.32,1.275) !important;
}
[data-testid="metric-container"] [data-testid="stMetricDelta"] { font-size: 12px !important; }

/* ═══════════════════════════════════════
   BUTTONS — warm rainbow gradient
═══════════════════════════════════════ */
.stButton > button {
    background: linear-gradient(135deg, #FF6B6B, #FF9A3C, #FFD166) !important;
    background-size: 200% 200% !important;
    color: #fff !important;
    border: none !important;
    border-radius: 14px !important;
    font-family: 'Nunito', sans-serif !important;
    font-weight: 700 !important;
    font-size: 14px !important;
    padding: 11px 26px !important;
    transition: all 0.3s cubic-bezier(0.175,0.885,0.32,1.275) !important;
    box-shadow: 0 4px 20px rgba(255,107,107,0.4), 0 0 0 0 transparent !important;
    letter-spacing: 0.3px !important;
    position: relative !important;
    overflow: hidden !important;
    animation: gradientShift 4s ease infinite !important;
    text-shadow: 0 1px 3px rgba(0,0,0,0.25) !important;
}
.stButton > button::after {
    content: '' !important;
    position: absolute !important;
    inset: 0 !important;
    background: linear-gradient(135deg, rgba(255,255,255,0.18), transparent) !important;
    border-radius: inherit !important;
}
.stButton > button:hover {
    transform: translateY(-3px) scale(1.03) !important;
    box-shadow: 0 12px 40px rgba(255,107,107,0.5), 0 0 20px rgba(255,209,102,0.3) !important;
    animation: gradientShift 1.5s ease infinite !important;
}
.stButton > button:active {
    transform: translateY(-1px) scale(0.99) !important;
}

/* ═══════════════════════════════════════
   INPUTS
═══════════════════════════════════════ */
.stTextInput input, .stTextArea textarea {
    background: rgba(26,15,46,0.85) !important;
    border: 1px solid rgba(199,125,255,0.3) !important;
    border-radius: 12px !important;
    color: var(--text-main) !important;
    font-family: 'Nunito', sans-serif !important;
    transition: all 0.25s ease !important;
}
.stTextInput input:focus, .stTextArea textarea:focus {
    border-color: #FF9A3C !important;
    box-shadow: 0 0 0 3px rgba(255,154,60,0.15), 0 0 20px rgba(255,154,60,0.1) !important;
    background: rgba(35,21,53,0.9) !important;
}

/* ═══════════════════════════════════════
   SLIDERS
═══════════════════════════════════════ */
.stSlider [data-baseweb="slider"] { padding: 0 !important; }
.stSlider [data-testid="stThumbValue"] { color: #FFD166 !important; }
.stSlider [data-baseweb="slider"] [role="slider"] {
    background: linear-gradient(135deg, #FF9A3C, #FFD166) !important;
    box-shadow: 0 0 12px rgba(255,154,60,0.6) !important;
    transition: transform 0.2s ease !important;
}

/* ═══════════════════════════════════════
   TABS
═══════════════════════════════════════ */
.stTabs [data-baseweb="tab-list"] {
    background: rgba(26,15,46,0.7) !important;
    border-radius: 14px !important;
    padding: 5px !important;
    gap: 5px !important;
    border: 1px solid rgba(199,125,255,0.2) !important;
    backdrop-filter: blur(10px) !important;
}
.stTabs [data-baseweb="tab"] {
    background: transparent !important;
    border-radius: 10px !important;
    color: var(--text-muted) !important;
    font-family: 'Nunito', sans-serif !important;
    font-weight: 600 !important;
    font-size: 13px !important;
    transition: all 0.25s ease !important;
}
.stTabs [data-baseweb="tab"]:hover {
    background: rgba(255,154,60,0.1) !important;
    color: #FFD166 !important;
}
.stTabs [aria-selected="true"] {
    background: linear-gradient(135deg, rgba(255,107,107,0.2), rgba(255,154,60,0.15)) !important;
    color: #FF9A3C !important;
    border: 1px solid rgba(255,154,60,0.4) !important;
    box-shadow: 0 4px 14px rgba(255,107,107,0.2) !important;
}

/* ═══════════════════════════════════════
   PROGRESS BAR — rainbow
═══════════════════════════════════════ */
.stProgress > div > div {
    background: linear-gradient(90deg, #FF6B6B, #FF9A3C, #FFD166, #95E06C, #06D6A0) !important;
    background-size: 300% 100% !important;
    border-radius: 6px !important;
    animation: shimmer 2.5s linear infinite !important;
    box-shadow: 0 0 12px rgba(255,154,60,0.5) !important;
}

/* ═══════════════════════════════════════
   EXPANDER
═══════════════════════════════════════ */
.streamlit-expanderHeader {
    background: rgba(255,154,60,0.06) !important;
    border: 1px solid rgba(255,154,60,0.2) !important;
    border-radius: 12px !important;
    color: var(--text-main) !important;
    transition: all 0.25s ease !important;
}
.streamlit-expanderHeader:hover {
    background: rgba(255,154,60,0.12) !important;
    border-color: rgba(255,209,102,0.4) !important;
}
.streamlit-expanderContent {
    border: 1px solid rgba(199,125,255,0.15) !important;
    border-top: none !important;
    border-radius: 0 0 12px 12px !important;
    background: rgba(26,15,46,0.6) !important;
    animation: fadeInDown 0.3s ease-out !important;
}

/* ═══════════════════════════════════════
   SELECTBOX
═══════════════════════════════════════ */
[data-baseweb="select"] > div {
    background: rgba(26,15,46,0.85) !important;
    border: 1px solid rgba(199,125,255,0.3) !important;
    border-radius: 12px !important;
    color: var(--text-main) !important;
    transition: border-color 0.25s ease !important;
}
[data-baseweb="select"] > div:hover { border-color: rgba(255,154,60,0.55) !important; }

/* ═══════════════════════════════════════
   DIVIDER
═══════════════════════════════════════ */
hr {
    border: none !important;
    height: 1px !important;
    background: linear-gradient(90deg, transparent, rgba(255,107,107,0.4), rgba(255,209,102,0.4), rgba(6,214,160,0.4), transparent) !important;
    margin: 20px 0 !important;
}

/* ═══════════════════════════════════════
   DATAFRAME
═══════════════════════════════════════ */
[data-testid="stDataFrame"] {
    border-radius: 14px !important;
    overflow: hidden !important;
    border: 1px solid rgba(255,154,60,0.25) !important;
    animation: fadeInUp 0.5s ease-out !important;
}

/* ═══════════════════════════════════════
   CUSTOM CARDS — warm glow
═══════════════════════════════════════ */
.mw-card {
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(199,125,255,0.2);
    border-radius: 20px;
    padding: 22px 26px;
    margin-bottom: 16px;
    backdrop-filter: blur(10px);
    transition: all 0.3s cubic-bezier(0.175,0.885,0.32,1.275);
    animation: fadeInUp 0.5s ease-out both;
    position: relative;
    overflow: hidden;
}
.mw-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0;
    width: 100%; height: 2px;
    background: linear-gradient(90deg, #FF6B6B, #FF9A3C, #FFD166, #95E06C, #06D6A0, #C77DFF, #FF6B6B);
    background-size: 300% 100%;
    animation: shimmer 4s linear infinite;
}
.mw-card:hover {
    transform: translateY(-4px);
    border-color: rgba(255,154,60,0.45);
    box-shadow: 0 12px 40px rgba(255,107,107,0.15), 0 0 0 1px rgba(255,154,60,0.1);
}

.mw-card-accent {
    background: linear-gradient(135deg, rgba(255,107,107,0.08), rgba(255,154,60,0.05), rgba(255,209,102,0.04));
    border: 1px solid rgba(255,154,60,0.3);
    border-radius: 20px;
    padding: 22px 26px;
    margin-bottom: 16px;
    position: relative;
    overflow: hidden;
    animation: fadeInUp 0.5s ease-out both, borderRainbow 6s ease-in-out infinite;
}
.mw-card-accent::after {
    content: '';
    position: absolute;
    top: -50%; left: -50%;
    width: 200%; height: 200%;
    background: conic-gradient(from 0deg at 50% 50%, transparent 0%, rgba(255,107,107,0.02) 20%, rgba(255,209,102,0.02) 40%, rgba(6,214,160,0.02) 60%, transparent 80%);
    animation: rotateGlow 16s linear infinite;
    pointer-events: none;
}

/* ═══════════════════════════════════════
   HERO TITLE — full rainbow
═══════════════════════════════════════ */
.hero-title {
    font-family: 'Playfair Display', serif;
    font-size: 38px;
    font-weight: 700;
    background: linear-gradient(90deg, #FF6B6B 0%, #FF9A3C 20%, #FFD166 40%, #95E06C 60%, #06D6A0 75%, #C77DFF 90%, #FF6B6B 100%);
    background-size: 250% auto;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    line-height: 1.2;
    margin-bottom: 6px;
    animation: fadeInDown 0.7s ease-out, rainbowText 6s linear infinite;
}

/* ═══════════════════════════════════════
   SECTION TITLE — warm amber
═══════════════════════════════════════ */
.section-title {
    font-family: 'Playfair Display', serif;
    font-size: 24px;
    font-weight: 700;
    background: linear-gradient(90deg, #FF9A3C, #FFD166);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin-bottom: 4px;
    animation: fadeInLeft 0.5s ease-out;
}

/* ═══════════════════════════════════════
   TAGS & BADGES — colorful
═══════════════════════════════════════ */
.tag {
    display: inline-block;
    padding: 4px 14px;
    border-radius: 20px;
    font-size: 12px;
    font-weight: 700;
    margin: 2px;
    transition: transform 0.2s ease;
}
.tag:hover { transform: scale(1.05); }
.tag-low  { background: rgba(6,214,160,0.15); color: #06D6A0; border: 1px solid rgba(6,214,160,0.4); }
.tag-med  { background: rgba(255,209,102,0.15); color: #FFD166; border: 1px solid rgba(255,209,102,0.4); }
.tag-high {
    background: rgba(255,107,107,0.15); color: #FF6B6B; border: 1px solid rgba(255,107,107,0.4);
    animation: glowPulse 2s ease-in-out infinite;
}

.badge {
    display: inline-block;
    padding: 5px 15px;
    border-radius: 20px;
    font-size: 13px;
    font-weight: 600;
    background: linear-gradient(135deg, rgba(255,107,107,0.12), rgba(255,154,60,0.08));
    border: 1px solid rgba(255,154,60,0.35);
    color: #FFD166;
    margin: 3px;
    transition: all 0.25s ease;
    animation: fadeInUp 0.4s ease-out both;
}
.badge:hover {
    background: linear-gradient(135deg, rgba(255,107,107,0.25), rgba(255,154,60,0.18));
    transform: translateY(-2px) scale(1.04);
    box-shadow: 0 4px 14px rgba(255,107,107,0.3);
}

/* ═══════════════════════════════════════
   FLOATING ORBS — rainbow
═══════════════════════════════════════ */
.orb {
    position: fixed;
    border-radius: 50%;
    pointer-events: none;
    z-index: 0;
    filter: blur(70px);
    opacity: 0.15;
}
.orb-1 {
    width: 350px; height: 350px;
    background: radial-gradient(circle, #FF6B6B, #FF9A3C, transparent);
    top: 5%; right: 3%;
    animation: float 9s ease-in-out infinite;
}
.orb-2 {
    width: 250px; height: 250px;
    background: radial-gradient(circle, #06D6A0, #74C7EC, transparent);
    bottom: 15%; left: 5%;
    animation: float 12s ease-in-out infinite reverse;
}
.orb-3 {
    width: 180px; height: 180px;
    background: radial-gradient(circle, #C77DFF, #FF6EB4, transparent);
    top: 55%; left: 45%;
    animation: float 15s ease-in-out infinite;
}
.orb-4 {
    width: 200px; height: 200px;
    background: radial-gradient(circle, #FFD166, #95E06C, transparent);
    bottom: 40%; right: 10%;
    animation: float 11s ease-in-out infinite;
}

/* ═══════════════════════════════════════
   LOGIN SPECIFIC — Redesigned
═══════════════════════════════════════ */
.login-glow {
    animation: float 4s ease-in-out infinite, warmPulse 3s ease-in-out infinite;
    display: inline-block;
    filter: drop-shadow(0 0 30px rgba(255,154,60,0.7));
}
.login-card {
    background: linear-gradient(160deg, rgba(30,18,52,0.95) 0%, rgba(26,15,46,0.92) 100%);
    border: 1px solid rgba(255,154,60,0.25);
    border-radius: 28px;
    padding: 42px 44px 36px;
    backdrop-filter: blur(24px);
    animation: fadeInUp 0.8s ease-out, glowPulse 6s ease-in-out infinite;
    box-shadow: 0 24px 70px rgba(0,0,0,0.55), 0 0 0 1px rgba(255,107,107,0.07), inset 0 1px 0 rgba(255,255,255,0.04);
    position: relative;
    overflow: hidden;
}
.login-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0;
    width: 100%; height: 3px;
    background: linear-gradient(90deg, #FF6B6B, #FF9A3C, #FFD166, #95E06C, #06D6A0, #74C7EC, #C77DFF, #FF6EB4, #FF6B6B);
    background-size: 300% 100%;
    animation: shimmer 4s linear infinite;
}
.login-card::after {
    content: '';
    position: absolute;
    bottom: 0; left: 20%; right: 20%;
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(255,154,60,0.15), transparent);
}

/* Avatar grid improved */
.avatar-grid-row {
    display: grid;
    grid-template-columns: repeat(8, 1fr);
    gap: 8px;
    margin-bottom: 8px;
}
.avatar-btn {
    aspect-ratio: 1;
    border-radius: 14px;
    border: 2px solid rgba(199,125,255,0.12);
    background: rgba(255,255,255,0.04);
    font-size: 22px;
    display: flex; align-items: center; justify-content: center;
    cursor: pointer;
    transition: all 0.22s cubic-bezier(0.175,0.885,0.32,1.275);
    position: relative;
    padding: 8px;
}
.avatar-btn:hover {
    border-color: rgba(255,154,60,0.5);
    background: rgba(255,154,60,0.1);
    transform: translateY(-2px) scale(1.08);
    box-shadow: 0 6px 18px rgba(255,107,107,0.2);
}
.avatar-btn.selected {
    border-color: #FF9A3C;
    background: linear-gradient(135deg, rgba(255,107,107,0.18), rgba(255,154,60,0.12));
    box-shadow: 0 0 0 3px rgba(255,154,60,0.22), 0 6px 22px rgba(255,107,107,0.25);
    transform: scale(1.06);
}
.avatar-btn.selected::after {
    content: '✓';
    position: absolute;
    top: -5px; right: -5px;
    width: 16px; height: 16px;
    border-radius: 50%;
    background: #FF9A3C;
    color: #fff;
    font-size: 9px;
    font-weight: 900;
    display: flex; align-items: center; justify-content: center;
    line-height: 16px;
    text-align: center;
    box-shadow: 0 2px 8px rgba(255,107,107,0.5);
}

/* Demo credentials pill */
.demo-pill {
    display: flex;
    align-items: center;
    gap: 8px;
    background: rgba(255,209,102,0.07);
    border: 1px solid rgba(255,209,102,0.2);
    border-radius: 12px;
    padding: 10px 14px;
    margin-bottom: 16px;
    font-size: 12px;
    color: #b8a9d4;
    animation: fadeInDown 0.5s 0.3s ease-out both;
}
.demo-pill strong { color: #FFD166; }
.demo-pill .demo-dot {
    width: 7px; height: 7px; border-radius: 50%;
    background: #FFD166; flex-shrink: 0;
    box-shadow: 0 0 8px rgba(255,209,102,0.6);
    animation: glowPulse 2s infinite;
}

/* Strength bar inline */
.pw-strength-wrap {
    margin-top: 6px;
    height: 4px;
    background: rgba(255,255,255,0.06);
    border-radius: 3px;
    overflow: hidden;
}

/* Tab switcher — clickable rows */
.auth-switcher {
    display: flex;
    gap: 8px;
    margin-bottom: 26px;
}
.auth-switch-btn {
    flex: 1;
    padding: 11px 0;
    border-radius: 13px;
    font-size: 14px;
    font-weight: 700;
    font-family: 'Nunito', sans-serif;
    letter-spacing: 0.3px;
    cursor: pointer;
    transition: all 0.25s ease;
    text-align: center;
    border: 1.5px solid rgba(199,125,255,0.15);
    background: rgba(255,255,255,0.03);
    color: #7a6d99;
}
.auth-switch-btn.active {
    background: linear-gradient(135deg, rgba(255,107,107,0.2), rgba(255,154,60,0.14));
    border-color: rgba(255,154,60,0.45);
    color: #FFD166;
    box-shadow: 0 4px 18px rgba(255,107,107,0.18), inset 0 1px 0 rgba(255,255,255,0.06);
}

/* Field label tweak */
.field-hint {
    font-size: 11px;
    color: #7a6d99;
    margin-top: 3px;
}

/* ═══════════════════════════════════════
   PERSONA CARD HOVER
═══════════════════════════════════════ */
.persona-card {
    transition: all 0.35s cubic-bezier(0.175,0.885,0.32,1.275);
    cursor: pointer;
}
.persona-card:hover {
    transform: translateY(-6px) scale(1.01);
    box-shadow: 0 16px 50px rgba(255,107,107,0.2) !important;
}

/* ═══════════════════════════════════════
   ALERTS
═══════════════════════════════════════ */
.stAlert {
    border-radius: 14px !important;
    backdrop-filter: blur(8px) !important;
    animation: fadeInUp 0.4s ease-out !important;
}

/* ═══════════════════════════════════════
   SCROLLBAR — rainbow
═══════════════════════════════════════ */
::-webkit-scrollbar { width: 5px; }
::-webkit-scrollbar-track { background: rgba(26,15,46,0.5); }
::-webkit-scrollbar-thumb {
    background: linear-gradient(#FF6B6B, #FF9A3C, #FFD166);
    border-radius: 4px;
}
::-webkit-scrollbar-thumb:hover { background: linear-gradient(#FFD166, #06D6A0); }

/* ═══════════════════════════════════════
   RIPPLE ANIMATION UTILITY
═══════════════════════════════════════ */
.ripple-container { position: relative; }
.ripple-ring {
    position: absolute;
    border: 2px solid rgba(255,154,60,0.4);
    border-radius: 50%;
    animation: ripple 2s ease-out infinite;
}

/* ═══════════════════════════════════════
   CAPTION / SMALL TEXT
═══════════════════════════════════════ */
.stCaption, small, caption { color: var(--text-dim) !important; }
</style>

<!-- Floating rainbow ambient orbs -->
<div class="orb orb-1"></div>
<div class="orb orb-2"></div>
<div class="orb orb-3"></div>
<div class="orb orb-4"></div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════
#  SESSION STATE — Persistent Data
# ══════════════════════════════════════════════════
def init_state():
    defaults = {
        "logged_in": False,
        "user_name": "Riya Sharma",
        "user_role": "IT Developer",
        "user_email": "riya.sharma@futureforward.com",
        "user_avatar": "👩‍💻",
        "registered_users": {},
        "stress_level": 56,
        "mood": "😰 Anxious",
        "streak": 5,
        "total_sessions": 18,
        "journal_entries": [
            {"date": "2025-04-17", "stress_before": 4, "stress_after": 2, "mood": "😌 Calmer", "note": "Ocean sounds really helped. Felt tension in shoulders release after 5 min.", "tags": ["#relaxed", "#focused"]},
            {"date": "2025-04-16", "stress_before": 5, "stress_after": 2, "mood": "🧠 Focused", "note": "Blue light + lavender combo was perfect before my 3PM presentation.", "tags": ["#productive", "#confident"]},
            {"date": "2025-04-15", "stress_before": 3, "stress_after": 1, "mood": "😊 Refreshed", "note": "Short 10-min breathing session before lunch — felt recharged all afternoon.", "tags": ["#refreshed", "#energized"]},
        ],
        "booked_sessions": [],
        "pod_light": "Cool Blue 🔵",
        "pod_music": "🌊 Ocean Waves",
        "pod_aroma": "🌿 Lavender",
        "pod_duration": 15,
        "breathe_cycles": 0,
        "weekly_stress": [72, 65, 81, 58, 56, 30, 22],
        "badges": ["🔥 5-Day Streak", "🌊 Ocean Master", "🫁 Breathwork Pro", "📓 Reflective Soul"],
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v

init_state()

# ══════════════════════════════════════════════════
#  HELPER: STRESS COLOR
# ══════════════════════════════════════════════════
def stress_color(val):
    if val <= 35: return "#06D6A0"
    if val <= 65: return "#FFD166"
    return "#FF6B6B"

def stress_label(val):
    if val <= 35: return ("Low Stress", "tag-low")
    if val <= 65: return ("Moderate Stress", "tag-med")
    return ("High Stress", "tag-high")

# ══════════════════════════════════════════════════
#  AUTH PAGE  (Login + Register)
# ══════════════════════════════════════════════════
def _auth_background():
    st.markdown("""
    <style>
    .login-bg {
        position: fixed; inset: 0; z-index: 0; pointer-events: none;
        background-image:
            linear-gradient(rgba(255,107,107,0.03) 1px, transparent 1px),
            linear-gradient(90deg, rgba(255,154,60,0.03) 1px, transparent 1px);
        background-size: 60px 60px;
        animation: particleDrift 20s ease-in-out infinite alternate;
    }
    .corner-glow-tl {
        position: fixed; top: -100px; left: -100px;
        width: 420px; height: 420px; border-radius: 50%;
        background: radial-gradient(circle, rgba(255,107,107,0.14) 0%, rgba(255,154,60,0.07) 45%, transparent 70%);
        animation: float 10s ease-in-out infinite; z-index: 0; pointer-events: none;
    }
    .corner-glow-br {
        position: fixed; bottom: -80px; right: -80px;
        width: 360px; height: 360px; border-radius: 50%;
        background: radial-gradient(circle, rgba(6,214,160,0.12) 0%, rgba(116,199,236,0.07) 45%, transparent 70%);
        animation: float 13s ease-in-out infinite reverse; z-index: 0; pointer-events: none;
    }
    .corner-glow-tl2 {
        position: fixed; bottom: -60px; left: -60px;
        width: 280px; height: 280px; border-radius: 50%;
        background: radial-gradient(circle, rgba(199,125,255,0.1) 0%, transparent 70%);
        animation: float 9s ease-in-out infinite; z-index: 0; pointer-events: none;
    }
    .particle { position: fixed; border-radius: 50%; pointer-events: none; z-index: 0; }
    .p1 { width:8px;  height:8px;  background:#FF6B6B; top:15%; left:10%; opacity:.7; animation:float 7s  ease-in-out infinite; }
    .p2 { width:5px;  height:5px;  background:#FFD166; top:40%; left:85%; opacity:.6; animation:float 9s  ease-in-out infinite reverse; }
    .p3 { width:9px;  height:9px;  background:#06D6A0; top:70%; left:20%; opacity:.5; animation:float 11s ease-in-out infinite; }
    .p4 { width:6px;  height:6px;  background:#C77DFF; top:25%; left:60%; opacity:.6; animation:float 8s  ease-in-out infinite reverse; }
    .p5 { width:4px;  height:4px;  background:#FF9A3C; top:80%; left:75%; opacity:.7; animation:float 6s  ease-in-out infinite; }
    .p6 { width:7px;  height:7px;  background:#74C7EC; top:55%; left:45%; opacity:.5; animation:float 10s ease-in-out infinite; }
    .p7 { width:5px;  height:5px;  background:#FF6EB4; top:88%; left:35%; opacity:.6; animation:float 8s  ease-in-out infinite reverse; }
    .p8 { width:6px;  height:6px;  background:#95E06C; top:10%; left:70%; opacity:.5; animation:float 12s ease-in-out infinite; }

    /* Auth tab removed — now using proper Streamlit buttons */
    .strength-bar-wrap {
        height: 5px;
        background: rgba(255,255,255,0.06);
        border-radius: 3px;
        overflow: hidden;
        margin-top: 6px;
    }
    @keyframes popIn {
        0%   { transform: scale(0) rotate(-20deg); opacity: 0; }
        70%  { transform: scale(1.15) rotate(5deg); }
        100% { transform: scale(1) rotate(0deg); opacity: 1; }
    }
    .success-tick { animation: popIn 0.5s cubic-bezier(0.175,0.885,0.32,1.275) both; }
    </style>
    <div class="login-bg"></div>
    <div class="corner-glow-tl"></div>
    <div class="corner-glow-br"></div>
    <div class="corner-glow-tl2"></div>
    <div class="particle p1"></div><div class="particle p2"></div>
    <div class="particle p3"></div><div class="particle p4"></div>
    <div class="particle p5"></div><div class="particle p6"></div>
    <div class="particle p7"></div><div class="particle p8"></div>
    """, unsafe_allow_html=True)


def _rainbow_divider():
    st.markdown("""
    <div style='display:flex; align-items:center; gap:12px; margin:18px 0'>
      <div style='flex:1; height:1px;
        background:linear-gradient(90deg, transparent, rgba(255,107,107,0.55), rgba(255,209,102,0.55))'></div>
      <span style='font-size:15px; line-height:1;
        background:linear-gradient(90deg,#FF9A3C,#FFD166,#95E06C);
        -webkit-background-clip:text; -webkit-text-fill-color:transparent;
        background-clip:text; filter:drop-shadow(0 0 6px rgba(255,154,60,0.5))'>✦</span>
      <div style='flex:1; height:1px;
        background:linear-gradient(90deg, rgba(255,209,102,0.55), rgba(6,214,160,0.55), transparent)'></div>
    </div>
    """, unsafe_allow_html=True)


def _logo_header(subtitle="Smart Stress Relief Pod System"):
    st.markdown(f"""
    <div style='text-align:center; margin-bottom:20px'>
      <div style='position:relative; display:inline-block; margin-bottom:14px'>
        <div style='font-size:68px; line-height:1' class='login-glow'>🧘</div>
        <div style='position:absolute; top:50%; left:50%; transform:translate(-50%,-50%);
          width:96px; height:96px; border-radius:50%;
          border:2px solid rgba(255,107,107,0.35);
          animation:ripple 2.5s ease-out infinite;'></div>
        <div style='position:absolute; top:50%; left:50%; transform:translate(-50%,-50%);
          width:96px; height:96px; border-radius:50%;
          border:2px solid rgba(255,209,102,0.2);
          animation:ripple 2.5s ease-out 0.9s infinite;'></div>
      </div>
      <div class='hero-title' style='font-size:42px; text-align:center'>MindfulWork</div>
      <p style='color:#b8a9d4; font-size:13px; margin-top:2px; letter-spacing:2px;
        text-transform:uppercase; font-weight:300'>{subtitle}</p>
      <p style='color:#7a6d99; font-size:11px; margin-top:2px; letter-spacing:1px'>
        by FutureForward Wellness</p>
    </div>
    """, unsafe_allow_html=True)


def _security_footer():
    st.markdown("""
    <div style='text-align:center; margin-top:20px; padding-top:14px;
      border-top:1px solid rgba(199,125,255,0.1)'>
      <div style='display:flex; justify-content:center; gap:20px; margin-bottom:8px; flex-wrap:wrap'>
        <div style='display:flex; align-items:center; gap:5px; font-size:11px; color:#7a6d99'>
          <span style='width:6px;height:6px;border-radius:50%;background:#FF6B6B;
            display:inline-block;animation:glowPulse 2s infinite'></span>
          End-to-end encrypted
        </div>
        <div style='display:flex; align-items:center; gap:5px; font-size:11px; color:#7a6d99'>
          <span style='width:6px;height:6px;border-radius:50%;background:#FFD166;
            display:inline-block;animation:glowPulse 2s 0.7s infinite'></span>
          HIPAA compliant
        </div>
        <div style='display:flex; align-items:center; gap:5px; font-size:11px; color:#7a6d99'>
          <span style='width:6px;height:6px;border-radius:50%;background:#06D6A0;
            display:inline-block;animation:glowPulse 2s 1.4s infinite'></span>
          Data private
        </div>
      </div>
      <p style='color:#7a6d99; font-size:10px; margin:0'>
        Powered by FutureForward Wellness Platform</p>
    </div>
    """, unsafe_allow_html=True)


def _pw_strength(pw):
    if not pw: return 0, "—", "#7a6d99"
    score = 0
    if len(pw) >= 8:  score += 1
    if len(pw) >= 12: score += 1
    if any(c.isupper() for c in pw):  score += 1
    if any(c.isdigit() for c in pw):  score += 1
    if any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in pw): score += 1
    labels = ["", "Weak", "Fair", "Good", "Strong", "Excellent"]
    colors = ["", "#FF6B6B", "#FF9A3C", "#FFD166", "#95E06C", "#06D6A0"]
    return score, labels[min(score, 5)], colors[min(score, 5)]


def _login_form():
    _logo_header()
    _rainbow_divider()

    # Demo credentials hint
    st.markdown("""
    <div class='demo-pill'>
      <div class='demo-dot'></div>
      <span><strong>Demo&nbsp;</strong> email: <strong>riya.sharma@futureforward.com</strong> &nbsp;·&nbsp; password: <strong>password</strong></span>
    </div>""", unsafe_allow_html=True)

    with st.form("login_form", clear_on_submit=False):
        email = st.text_input("📧  Employee Email",
            placeholder="yourname@company.com",
            value="riya.sharma@futureforward.com")
        password = st.text_input("🔐  Password",
            type="password", placeholder="••••••••", value="password")

        col_rem, col_forgot = st.columns([1, 1])
        with col_rem:
            st.checkbox("Remember me", value=True)
        with col_forgot:
            st.markdown(
                "<div style='text-align:right; padding-top:6px'>"
                "<span style='font-size:12px; color:#FF9A3C; cursor:pointer'>Forgot password?</span>"
                "</div>", unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        submitted = st.form_submit_button("✨  Sign In to MindfulWork", use_container_width=True)

        if submitted:
            users = st.session_state.get("registered_users", {})
            if email in users and users[email]["password"] == password:
                u = users[email]
                st.session_state.logged_in   = True
                st.session_state.user_name   = u["name"]
                st.session_state.user_role   = u["role"]
                st.session_state.user_avatar = u.get("avatar", "👤")
            else:
                st.error("❌  Invalid email or password. Try the demo account or create a new one.")
                return
        else:
            return

    _security_footer()
    st.rerun()


def _register_form():
    _logo_header("Create Your Wellness Account")
    _rainbow_divider()

    AVATARS = ["👩‍💻","👨‍💻","🧑‍💼","👩‍💼","👨‍🎨","👩‍🎨","🧑‍⚕️","👩‍⚕️",
               "🧘","🏃","💪","🌟","🦋","🌺","🎯","⚡"]

    # ── Improved Avatar Selection ──
    st.markdown("""
    <div style='font-size:13px; color:#b8a9d4; font-weight:700; margin-bottom:10px;
      display:flex; align-items:center; gap:7px'>
      <span style='font-size:16px'>🎨</span>
      <span>Choose Your Avatar</span>
      <span style='font-size:11px; color:#7a6d99; font-weight:400; margin-left:4px'>— click to select</span>
    </div>""", unsafe_allow_html=True)

    if "reg_avatar" not in st.session_state:
        st.session_state.reg_avatar = AVATARS[0]

    # Row 1
    av_cols_1 = st.columns(8)
    for idx in range(8):
        av = AVATARS[idx]
        with av_cols_1[idx]:
            is_sel = st.session_state.reg_avatar == av
            border = "border: 2px solid #FF9A3C; background: linear-gradient(135deg,rgba(255,107,107,0.18),rgba(255,154,60,0.12)); box-shadow: 0 0 0 3px rgba(255,154,60,0.2), 0 4px 16px rgba(255,107,107,0.2);" if is_sel else "border: 2px solid rgba(199,125,255,0.12); background: rgba(255,255,255,0.04);"
            tick   = "<span style='position:absolute;top:-5px;right:-5px;width:14px;height:14px;border-radius:50%;background:#FF9A3C;color:#fff;font-size:8px;font-weight:900;display:flex;align-items:center;justify-content:center;box-shadow:0 2px 6px rgba(255,107,107,0.5)'>✓</span>" if is_sel else ""
            st.markdown(
                f"<div style='position:relative;border-radius:14px;{border}padding:8px;text-align:center;font-size:22px;transition:all .22s;'>{av}{tick}</div>",
                unsafe_allow_html=True)
            if st.button(av, key=f"av_{idx}", use_container_width=True):
                st.session_state.reg_avatar = av
                st.rerun()

    # Row 2
    av_cols_2 = st.columns(8)
    for idx in range(8, 16):
        av = AVATARS[idx]
        with av_cols_2[idx - 8]:
            is_sel = st.session_state.reg_avatar == av
            border = "border: 2px solid #FF9A3C; background: linear-gradient(135deg,rgba(255,107,107,0.18),rgba(255,154,60,0.12)); box-shadow: 0 0 0 3px rgba(255,154,60,0.2), 0 4px 16px rgba(255,107,107,0.2);" if is_sel else "border: 2px solid rgba(199,125,255,0.12); background: rgba(255,255,255,0.04);"
            tick   = "<span style='position:absolute;top:-5px;right:-5px;width:14px;height:14px;border-radius:50%;background:#FF9A3C;color:#fff;font-size:8px;font-weight:900;display:flex;align-items:center;justify-content:center;box-shadow:0 2px 6px rgba(255,107,107,0.5)'>✓</span>" if is_sel else ""
            st.markdown(
                f"<div style='position:relative;border-radius:14px;{border}padding:8px;text-align:center;font-size:22px;transition:all .22s;'>{av}{tick}</div>",
                unsafe_allow_html=True)
            if st.button(av, key=f"av_{idx}", use_container_width=True):
                st.session_state.reg_avatar = av
                st.rerun()

    # Selected preview
    sel = st.session_state.reg_avatar
    st.markdown(f"""
    <div style='display:flex; align-items:center; gap:10px; margin:12px 0 6px;
      background:rgba(255,154,60,0.07); border:1px solid rgba(255,154,60,0.18);
      border-radius:12px; padding:10px 14px; animation:fadeInUp 0.3s ease-out'>
      <span style='font-size:28px; filter:drop-shadow(0 0 8px rgba(255,154,60,0.5))'>{sel}</span>
      <div>
        <div style='font-size:12px; color:#FF9A3C; font-weight:700'>Selected Avatar</div>
        <div style='font-size:11px; color:#7a6d99'>This will appear on your profile and sessions</div>
      </div>
    </div>""", unsafe_allow_html=True)

    st.markdown("<div style='height:10px'></div>", unsafe_allow_html=True)

    with st.form("register_form", clear_on_submit=False):
        c1, c2 = st.columns(2)
        with c1:
            first_name = st.text_input("👤  First Name *", placeholder="Riya")
        with c2:
            last_name  = st.text_input("   Last Name *",  placeholder="Sharma")

        reg_email = st.text_input("📧  Work Email *", placeholder="yourname@company.com")
        emp_id    = st.text_input("🪪  Employee ID *", placeholder="e.g. FW-2025",
                                  help="Issued by your HR department")

        c3, c4 = st.columns(2)
        with c3:
            department = st.selectbox("🏢  Department *", [
                "IT / Engineering", "Marketing", "HR",
                "Finance", "Operations", "Legal", "Design", "Sales"])
        with c4:
            gender = st.selectbox("🧬  Gender (optional)", [
                "Prefer not to say", "Female", "Male", "Non-binary", "Other"])

        c5, c6 = st.columns(2)
        with c5:
            stress_goal = st.selectbox("🎯  Wellness Goal", [
                "Reduce daily stress", "Better sleep", "Improve focus",
                "Manage anxiety", "Build resilience", "General wellbeing"])
        with c6:
            session_pref = st.selectbox("⏱  Preferred Session", [
                "10 min (micro)", "15 min", "20 min", "30 min (deep)", "Flexible"])

        reg_password = st.text_input("🔐  Create Password *",
            type="password", placeholder="Min 8 characters")
        confirm_pw   = st.text_input("🔒  Confirm Password *",
            type="password", placeholder="Re-enter password")

        agree      = st.checkbox("✅  I agree to the Privacy Policy and Wellness Data Terms")
        newsletter = st.checkbox("📬  Send me weekly wellness tips & pod updates", value=True)

        st.markdown("<br>", unsafe_allow_html=True)
        submit_reg = st.form_submit_button(
            "🌟  Create My MindfulWork Account", use_container_width=True)

        if submit_reg:
            errors = []
            if not first_name.strip():   errors.append("First name is required.")
            if not last_name.strip():    errors.append("Last name is required.")
            if not reg_email.strip() or "@" not in reg_email:
                errors.append("A valid work email is required.")
            if reg_email in st.session_state.get("registered_users", {}):
                errors.append("An account with this email already exists — please sign in.")
            if not emp_id.strip():       errors.append("Employee ID is required.")
            if len(reg_password) < 8:    errors.append("Password must be at least 8 characters.")
            if reg_password != confirm_pw: errors.append("Passwords do not match.")
            if not agree:                errors.append("Please accept the Privacy Policy to continue.")

            if errors:
                for e in errors:
                    st.error(f"❌  {e}")
            else:
                full_name = f"{first_name.strip()} {last_name.strip()}"
                st.session_state.registered_users[reg_email] = {
                    "password":      reg_password,
                    "name":          full_name,
                    "role":          department,
                    "employee_id":   emp_id,
                    "avatar":        st.session_state.reg_avatar,
                    "goal":          stress_goal,
                    "session_pref":  session_pref,
                    "newsletter":    newsletter,
                }
                st.session_state.logged_in   = True
                st.session_state.user_name   = full_name
                st.session_state.user_role   = department
                st.session_state.user_avatar = st.session_state.reg_avatar
                st.session_state.streak      = 0
                st.session_state.badges      = ["🌟 New Member", "🎉 Welcome!"]
                st.session_state.auth_page   = "login"
                st.success(f"🎉  Welcome to MindfulWork, {first_name}! Your account has been created.")
                st.balloons()
                time.sleep(1)
                st.rerun()

    _security_footer()


def login_page():
    _auth_background()

    is_reg = st.session_state.get("auth_page", "login") == "register"
    col1, col2, col3 = st.columns([0.5, 2, 0.5] if is_reg else [1, 1.5, 1])

    with col2:
        st.markdown("<br>", unsafe_allow_html=True)

        # Card wrapper open
        st.markdown("<div class='login-card'>", unsafe_allow_html=True)

        # ── Proper clickable tab switcher ──
        tab_col1, tab_col2 = st.columns(2)
        with tab_col1:
            active_l = "active" if not is_reg else ""
            st.markdown(
                f"<div class='auth-switch-btn {active_l}'>🔑&nbsp;&nbsp;Sign In</div>",
                unsafe_allow_html=True,
            )
            if st.button("Sign In", key="tab_login", use_container_width=True,
                         type="primary" if not is_reg else "secondary"):
                st.session_state.auth_page = "login"
                st.rerun()
        with tab_col2:
            active_r = "active" if is_reg else ""
            st.markdown(
                f"<div class='auth-switch-btn {active_r}'>🌟&nbsp;&nbsp;Register</div>",
                unsafe_allow_html=True,
            )
            if st.button("Register", key="tab_register", use_container_width=True,
                         type="primary" if is_reg else "secondary"):
                st.session_state.auth_page = "register"
                st.rerun()

        st.markdown("<div style='height:6px'></div>", unsafe_allow_html=True)

        if not is_reg:
            _login_form()
        else:
            _register_form()

        # Card wrapper close
        st.markdown("</div>", unsafe_allow_html=True)



# ══════════════════════════════════════════════════
#  SIDEBAR
# ══════════════════════════════════════════════════
def render_sidebar():
    with st.sidebar:
        st.markdown(f"""
        <div style='text-align:center; padding:24px 0 18px; animation: fadeInDown 0.6s ease-out'>
          <div style='position:relative; display:inline-block'>
            <div style='font-size:46px; animation: float 4s ease-in-out infinite; filter:drop-shadow(0 0 20px rgba(255,154,60,0.6))'>🧘</div>
            <div style='position:absolute; top:50%; left:50%; transform:translate(-50%,-50%);
              width:65px; height:65px; border-radius:50%;
              border:1px solid rgba(255,107,107,0.35);
              animation:ripple 3s ease-out infinite;'></div>
          </div>
          <div style='font-family:"Playfair Display",serif; font-size:21px; font-weight:700; margin-top:8px;
            background:linear-gradient(90deg,#FF9A3C,#FFD166); -webkit-background-clip:text; -webkit-text-fill-color:transparent; background-clip:text;'>MindfulWork</div>
          <div style='font-size:11px; color:#7a6d99; margin-top:2px; letter-spacing:1px; text-transform:uppercase'>Smart Stress Relief</div>
        </div>
        <div style='height:1px; background:linear-gradient(90deg,transparent,rgba(255,107,107,0.4),rgba(255,209,102,0.4),rgba(6,214,160,0.4),transparent); margin-bottom:18px'></div>
        <div style='background:linear-gradient(135deg,rgba(255,107,107,0.08),rgba(255,154,60,0.05)); border:1px solid rgba(255,154,60,0.25); border-radius:16px; padding:16px; margin-bottom:20px; text-align:center; animation: glowPulse 5s ease-in-out infinite; position:relative; overflow:hidden'>
          <div style='position:absolute;top:0;left:-100%;width:60%;height:100%;background:linear-gradient(90deg,transparent,rgba(255,154,60,0.06),transparent);animation:shimmer 4s infinite'></div>
          <div style='font-size:30px; animation: float 3s ease-in-out infinite'>{st.session_state.get("user_avatar","👤")}</div>
          <div style='font-weight:700; font-size:15px; color:#f5f0ff; margin-top:8px'>{st.session_state.user_name}</div>
          <div style='font-size:11px; color:#b8a9d4; letter-spacing:0.5px'>{st.session_state.user_role}</div>
          <div style='margin-top:12px'>
            <span class='badge' style='animation: glowPulse 2.5s ease-in-out infinite'>🔥 {st.session_state.streak}-Day Streak</span>
          </div>
        </div>
        """, unsafe_allow_html=True)

        page = st.radio("Navigation", [
            "🏠  Dashboard",
            "🤖  MoodSync AI",
            "🪑  Pod Control",
            "🫁  Breathe With Me",
            "📅  Pod Scheduler",
            "📓  Session Journal",
            "📊  Analytics",
            "👥  Personas & Research",
        ], label_visibility="collapsed")

        sl, sl_class = stress_label(st.session_state.stress_level)
        sc = stress_color(st.session_state.stress_level)
        stress_pct = st.session_state.stress_level
        st.markdown(f"""
        <div style='margin-top:24px; padding:16px; background:rgba(255,154,60,0.06); border-radius:14px; border:1px solid rgba(199,125,255,0.2); animation: borderGlow 5s ease-in-out infinite'>
          <div style='font-size:10px; color:#7a6d99; text-transform:uppercase; letter-spacing:1.5px; margin-bottom:10px'>⚡ Live Stress Level</div>
          <div style='display:flex; align-items:center; justify-content:space-between; margin-bottom:10px'>
            <div style='font-size:36px; font-weight:800; color:{sc}; text-shadow:0 0 20px {sc}60; animation: countUp 0.5s ease-out'>{st.session_state.stress_level}</div>
            <span class='tag {sl_class}'>{sl}</span>
          </div>
          <!-- Animated stress bar -->
          <div style='height:6px; background:rgba(255,255,255,0.06); border-radius:3px; overflow:hidden'>
            <div style='height:100%; width:{stress_pct}%; background:linear-gradient(90deg,{sc},{sc}88); border-radius:3px; transition:width 0.8s ease; box-shadow:0 0 8px {sc}60; animation:shimmer 2s infinite'></div>
          </div>
          <div style='font-size:10px; color:#7a6d99; margin-top:6px; text-align:right'>/100</div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("🚪 Sign Out", use_container_width=True):
            st.session_state.logged_in = False
            st.rerun()

        return page

# ══════════════════════════════════════════════════
#  PAGE 1: DASHBOARD
# ══════════════════════════════════════════════════
def page_dashboard():
    hour = datetime.now().hour
    greeting = 'Morning' if hour < 12 else 'Afternoon' if hour < 18 else 'Evening'
    greeting_emoji = '🌅' if hour < 12 else '☀️' if hour < 18 else '🌙'

    st.markdown(f"""
    <div class='mw-card-accent' style='padding:28px 32px; margin-bottom:24px'>
      <div style='display:flex; align-items:center; justify-content:space-between; flex-wrap:wrap; gap:16px'>
        <div>
          <div style='font-size:12px; color:#7a6d99; text-transform:uppercase; letter-spacing:2px; margin-bottom:6px; animation:fadeInDown 0.5s ease-out'>{greeting_emoji} Good {greeting}</div>
          <div class='hero-title'>{st.session_state.user_name.split()[0]} 👋</div>
          <p style='color:#b8a9d4; margin:4px 0 0; font-size:15px; animation:fadeInLeft 0.7s ease-out'>Your wellness snapshot for {datetime.now().strftime("%A, %d %B %Y")}</p>
        </div>
        <div style='text-align:right; animation:slideInRight 0.6s ease-out'>
          <div style='font-size:11px; color:#7a6d99; margin-bottom:4px; text-transform:uppercase; letter-spacing:1px'>Current Mood</div>
          <div style='font-size:28px'>{st.session_state.mood.split()[0]}</div>
          <div style='font-size:13px; color:#b8a9d4'>{" ".join(st.session_state.mood.split()[1:])}</div>
        </div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    # ── KPI Row ──
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("🧠 Stress Level", f"{st.session_state.stress_level}/100", "-8 from yesterday")
    with col2:
        st.metric("🏅 Sessions This Week", "3", "+1 vs last week")
    with col3:
        st.metric("📉 Avg Reduction", "42%", "+7% this week")
    with col4:
        st.metric("🔥 Streak", f"{st.session_state.streak} days", "Keep going!")

    st.markdown("<br>", unsafe_allow_html=True)
    col_left, col_right = st.columns([1.3, 1])

    with col_left:
        # ── Weekly stress chart ──
        st.markdown("<div class='section-title'>📈 Weekly Stress Trend</div>", unsafe_allow_html=True)
        days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        stress_vals = st.session_state.weekly_stress
        colors_bar = [stress_color(v) for v in stress_vals]

        fig = go.Figure()
        fig.add_trace(go.Bar(
            x=days, y=stress_vals,
            marker_color=colors_bar,
            marker_line_width=0,
            hovertemplate="<b>%{x}</b><br>Stress: %{y}/100<extra></extra>",
        ))
        fig.add_trace(go.Scatter(
            x=days, y=stress_vals, mode='lines+markers',
            line=dict(color='rgba(255,209,102,0.6)', width=2, dash='dot'),
            marker=dict(color='#FFD166', size=6),
            hoverinfo='skip',
        ))
        fig.update_layout(
            paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
            font=dict(family='Nunito', color='#b8a9d4'),
            xaxis=dict(gridcolor='rgba(255,154,60,0.1)', showline=False, tickfont=dict(color='#b8a9d4')),
            yaxis=dict(gridcolor='rgba(255,154,60,0.1)', range=[0, 100], tickfont=dict(color='#b8a9d4')),
            margin=dict(l=0, r=0, t=10, b=0), height=240,
            showlegend=False,
        )
        st.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False})

        # ── Simulate stress update ──
        st.markdown("<div class='section-title' style='font-size:18px'>🎛 Adjust Live Stress (simulate wearable)</div>", unsafe_allow_html=True)
        new_stress = st.slider("Current Stress Level", 0, 100, st.session_state.stress_level, label_visibility="collapsed")
        if new_stress != st.session_state.stress_level:
            st.session_state.stress_level = new_stress
            st.rerun()

    with col_right:
        # ── Stress Gauge ──
        st.markdown("<div class='section-title'>🔵 Stress Gauge</div>", unsafe_allow_html=True)
        gauge_color = stress_color(st.session_state.stress_level)
        fig_gauge = go.Figure(go.Indicator(
            mode="gauge+number+delta",
            value=st.session_state.stress_level,
            delta={'reference': 64, 'increasing': {'color': "#FF6B6B"}, 'decreasing': {'color': "#FF9A3C"}},
            gauge={
                'axis': {'range': [0, 100], 'tickfont': {'color': '#b8a9d4'}, 'tickcolor': '#b8a9d4'},
                'bar': {'color': gauge_color, 'thickness': 0.25},
                'bgcolor': 'rgba(26,15,46,0.85)',
                'borderwidth': 0,
                'steps': [
                    {'range': [0, 35], 'color': 'rgba(6,214,160,0.15)'},
                    {'range': [35, 65], 'color': 'rgba(255,209,102,0.15)'},
                    {'range': [65, 100], 'color': 'rgba(255,107,107,0.15)'},
                ],
                'threshold': {'line': {'color': gauge_color, 'width': 3}, 'thickness': 0.85, 'value': st.session_state.stress_level}
            },
            number={'font': {'color': gauge_color, 'size': 48, 'family': 'Nunito'}, 'suffix': '/100'},
            title={'text': stress_label(st.session_state.stress_level)[0], 'font': {'color': '#b8a9d4', 'size': 14}},
        ))
        fig_gauge.update_layout(
            paper_bgcolor='rgba(0,0,0,0)', height=280,
            margin=dict(l=20, r=20, t=30, b=20),
            font=dict(family='Nunito'),
        )
        st.plotly_chart(fig_gauge, use_container_width=True, config={"displayModeBar": False})

        # ── AI Banner ──
        if st.session_state.stress_level >= 50:
            ai_msg = "High stress detected! A 15-min Lavender + Ocean Calm session is recommended before your next meeting."
        elif st.session_state.stress_level >= 35:
            ai_msg = "Moderate stress — consider a quick 10-min Breathe With Me session or a brief pod booking."
        else:
            ai_msg = "Stress is low! 🎉 Great time to do a journaling session and track your wellness win."
        st.markdown(f"""
        <div class='mw-card' style='border:1px solid rgba(255,107,107,0.4); margin-top:12px; position:relative; overflow:hidden'>
          <div style='position:absolute;top:0;right:0;width:80px;height:80px;background:radial-gradient(circle,rgba(255,154,60,0.08),transparent);border-radius:50%;transform:translate(20px,-20px)'></div>
          <div style='display:flex; gap:12px; align-items:flex-start'>
            <div style='position:relative'>
              <span style='font-size:28px; animation:float 3s ease-in-out infinite; display:block'>🤖</span>
              <div style='position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);width:40px;height:40px;border-radius:50%;border:1px solid rgba(255,154,60,0.35);animation:ripple 2s ease-out infinite'></div>
            </div>
            <div>
              <div style='font-weight:700; color:#FF9A3C; font-size:13px; margin-bottom:6px; text-shadow:0 0 12px rgba(255,154,60,0.45); letter-spacing:0.5px'>⚡ MoodSync AI Suggestion</div>
              <div style='font-size:13px; color:#d4c5f0; line-height:1.7'>{ai_msg}</div>
            </div>
          </div>
        </div>
        """, unsafe_allow_html=True)

    # ── Today's sessions ──
    st.markdown("---")
    st.markdown("<div class='section-title'>🪑 Today's Pod Availability</div>", unsafe_allow_html=True)
    pods_data = {
        "Pod": ["Pod A – Ocean Calm", "Pod B – Focus Flow", "Pod C – Forest Breathe"],
        "Status": ["🟢 Available Now", "🔵 Booked (3:30 PM)", "🟢 Available (5:00 PM)"],
        "Duration": ["20 min", "15 min", "25 min"],
        "Theme": ["Ocean + Lavender + Blue Light", "Rain + Eucalyptus + Green Light", "Forest + Sandalwood + Warm Amber"],
        "Stress Relief": ["⭐⭐⭐⭐⭐", "⭐⭐⭐⭐", "⭐⭐⭐⭐⭐"],
    }
    df_pods = pd.DataFrame(pods_data)
    st.dataframe(df_pods, use_container_width=True, hide_index=True)

    # ── Badges ──
    st.markdown("---")
    st.markdown("<div class='section-title'>🏅 Your Badges</div>", unsafe_allow_html=True)
    badge_html = "".join([f"<span class='badge'>{b}</span>" for b in st.session_state.badges])
    st.markdown(f"<div style='margin-top:8px'>{badge_html}</div>", unsafe_allow_html=True)


# ══════════════════════════════════════════════════
#  PAGE 2: MOODSYNC AI
# ══════════════════════════════════════════════════
def page_moodsync():
    st.markdown("<div class='hero-title'>🤖 MoodSync AI</div>", unsafe_allow_html=True)
    st.markdown("<p style='color:#b8a9d4'>AI-powered pod personalization based on your real-time stress profile</p>", unsafe_allow_html=True)
    st.markdown("---")

    col1, col2 = st.columns([1, 1.2])

    with col1:
        st.markdown("<div class='section-title' style='font-size:18px'>How are you feeling right now?</div>", unsafe_allow_html=True)
        mood = st.radio("Select Mood", [
            "😰 Anxious", "😤 Frustrated", "😔 Low", "😐 Neutral",
            "😊 Okay", "😴 Tired", "🤯 Overwhelmed", "😌 Calm"
        ], index=0, key="mood_select", label_visibility="collapsed")
        st.session_state.mood = mood

        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("<div class='section-title' style='font-size:18px'>Input Sources</div>", unsafe_allow_html=True)
        src1 = st.checkbox("⌚ Wearable device (heart rate + HRV)", value=True)
        src2 = st.checkbox("📝 Manual survey (self-reported)", value=True)
        src3 = st.checkbox("🎤 Voice tone analysis", value=False)

        st.markdown("<br>", unsafe_allow_html=True)
        generate = st.button("✨ Generate AI Recommendation", use_container_width=True)

    with col2:
        # AI Logic based on mood + stress
        mood_configs = {
            "😰 Anxious":     {"light": "🔵 Cool Blue",   "music": "🌊 Ocean Waves",  "aroma": "🌿 Lavender",    "dur": 15, "why": "Reduces cortisol; blue light lowers heart rate variability"},
            "😤 Frustrated":  {"light": "💜 Soft Violet", "music": "🌧 Gentle Rain",  "aroma": "🍃 Eucalyptus", "dur": 20, "why": "Violet spectrum calms aggression; eucalyptus clears mental fog"},
            "😔 Low":         {"light": "🟡 Warm Amber",  "music": "🎹 Soft Piano",   "aroma": "🌹 Rose",        "dur": 25, "why": "Warm light boosts serotonin; rose has proven mood-lifting properties"},
            "😐 Neutral":     {"light": "🟢 Forest Green","music": "🌲 Forest Sounds","aroma": "🪵 Sandalwood", "dur": 10, "why": "Biophilic design maintains balance and prevents stress build-up"},
            "😊 Okay":        {"light": "🔵 Cool Blue",   "music": "🌊 Ocean Waves",  "aroma": "🍋 Citrus",     "dur": 10, "why": "Citrus boosts energy; maintain your positive state proactively"},
            "😴 Tired":       {"light": "🟡 Warm Amber",  "music": "🌧 Gentle Rain",  "aroma": "🌿 Lavender",   "dur": 30, "why": "Warm light signals wind-down; lavender promotes deep rest"},
            "🤯 Overwhelmed": {"light": "💜 Soft Violet", "music": "🌊 Ocean Waves",  "aroma": "🍃 Eucalyptus", "dur": 20, "why": "Ocean sounds + eucalyptus proven to reduce cognitive load by 28%"},
            "😌 Calm":        {"light": "🟢 Forest Green","music": "🎹 Soft Piano",   "aroma": "🪵 Sandalwood", "dur": 10, "why": "Maintain your calm state with a restorative micro-session"},
        }
        cfg = mood_configs.get(mood, mood_configs["😐 Neutral"])

        if generate:
            with st.spinner("Analyzing stress patterns..."):
                time.sleep(1.2)

        st.markdown("<div class='section-title' style='font-size:18px'>🎯 AI-Generated Pod Configuration</div>", unsafe_allow_html=True)
        st.markdown(f"""
        <div class='mw-card-accent' style='position:relative; overflow:hidden'>
          <div style='position:absolute;top:-20px;right:-20px;width:120px;height:120px;border-radius:50%;background:radial-gradient(circle,rgba(255,154,60,0.1),transparent);animation:breatheCircle 4s ease-in-out infinite'></div>
          <div style='font-size:11px; color:#7a6d99; margin-bottom:16px; text-transform:uppercase; letter-spacing:1.5px; display:flex; align-items:center; gap:8px'>
            <span style='width:6px;height:6px;border-radius:50%;background:#FF9A3C;display:inline-block;animation:glowPulse 2s infinite'></span>
            Based on stress level {st.session_state.stress_level}/100 · Mood: {mood}
          </div>
          <div style='display:grid; grid-template-columns:1fr 1fr; gap:12px'>
            <div style='background:rgba(26,15,46,0.6);border:1px solid rgba(199,125,255,0.2);border-radius:14px;padding:16px;transition:all 0.3s ease;animation:fadeInUp 0.4s ease-out'>
              <div style='font-size:10px;color:#7a6d99;margin-bottom:6px;text-transform:uppercase;letter-spacing:1px'>💡 LIGHTING</div>
              <div style='font-size:19px;font-weight:700;color:#f5f0ff'>{cfg['light']}</div>
            </div>
            <div style='background:rgba(26,15,46,0.6);border:1px solid rgba(199,125,255,0.2);border-radius:14px;padding:16px;transition:all 0.3s ease;animation:fadeInUp 0.5s ease-out'>
              <div style='font-size:10px;color:#7a6d99;margin-bottom:6px;text-transform:uppercase;letter-spacing:1px'>🎵 MUSIC</div>
              <div style='font-size:19px;font-weight:700;color:#f5f0ff'>{cfg['music']}</div>
            </div>
            <div style='background:rgba(26,15,46,0.6);border:1px solid rgba(199,125,255,0.2);border-radius:14px;padding:16px;transition:all 0.3s ease;animation:fadeInUp 0.6s ease-out'>
              <div style='font-size:10px;color:#7a6d99;margin-bottom:6px;text-transform:uppercase;letter-spacing:1px'>🌸 AROMA</div>
              <div style='font-size:19px;font-weight:700;color:#f5f0ff'>{cfg['aroma']}</div>
            </div>
            <div style='background:rgba(26,15,46,0.6);border:1px solid rgba(199,125,255,0.2);border-radius:14px;padding:16px;transition:all 0.3s ease;animation:fadeInUp 0.7s ease-out'>
              <div style='font-size:10px;color:#7a6d99;margin-bottom:6px;text-transform:uppercase;letter-spacing:1px'>⏱ DURATION</div>
              <div style='font-size:19px;font-weight:700;color:#FF9A3C'>{cfg['dur']} min</div>
            </div>
          </div>
          <div style='margin-top:16px;background:rgba(255,107,107,0.07);border-radius:12px;padding:14px;font-size:13px;color:#b8a9d4;line-height:1.7;border:1px solid rgba(6,214,160,0.15)'>
            💡 <b style='color:#FF9A3C'>Why this works:</b> {cfg['why']}
          </div>
        </div>
        """, unsafe_allow_html=True)

        # Apply to session state
        st.session_state.pod_light = cfg['light']
        st.session_state.pod_music = cfg['music']
        st.session_state.pod_aroma = cfg['aroma']
        st.session_state.pod_duration = cfg['dur']

    # ── Mood history chart ──
    st.markdown("---")
    st.markdown("<div class='section-title'>📊 Mood Pattern History (This Week)</div>", unsafe_allow_html=True)
    mood_data = {
        "Day": ["Mon AM", "Mon PM", "Tue AM", "Tue PM", "Wed AM", "Thu AM", "Thu PM", "Fri AM"],
        "Mood": ["😤 Frustrated", "😌 Calm", "😰 Anxious", "😐 Neutral", "🤯 Overwhelmed", "😰 Anxious", "😊 Okay", "😰 Anxious"],
        "Stress": [72, 38, 65, 45, 81, 67, 42, 56],
    }
    df_mood = pd.DataFrame(mood_data)
    fig_mood = px.line(df_mood, x="Day", y="Stress", markers=True,
        color_discrete_sequence=["#FF9A3C"],
        labels={"Stress": "Stress Level", "Day": ""},
    )
    fig_mood.update_traces(
        line=dict(width=3), marker=dict(size=10, color="#FFD166", line=dict(color="#FF9A3C", width=2)),
        hovertemplate="<b>%{x}</b><br>Stress: %{y}<extra></extra>",
    )
    fig_mood.update_layout(
        paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
        font=dict(family='Nunito', color='#b8a9d4'), height=220,
        margin=dict(l=0,r=0,t=10,b=0),
        xaxis=dict(gridcolor='rgba(255,154,60,0.1)', showline=False),
        yaxis=dict(gridcolor='rgba(255,154,60,0.1)', range=[0,100]),
    )
    st.plotly_chart(fig_mood, use_container_width=True, config={"displayModeBar": False})

    st.info("📊 **Pattern Detected:** You consistently spike stress on weekday mornings. MoodSync recommends a 7:45 AM pod session every Mon–Fri.")


# ══════════════════════════════════════════════════
#  PAGE 3: POD CONTROL
# ══════════════════════════════════════════════════
def page_pod():
    st.markdown("<div class='hero-title'>🪑 Pod Control Center</div>", unsafe_allow_html=True)
    st.markdown("<p style='color:#b8a9d4'>Manually fine-tune your Smart Stress Relief Pod settings</p>", unsafe_allow_html=True)
    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("<div class='section-title' style='font-size:18px'>💡 Light Therapy</div>", unsafe_allow_html=True)
        light = st.selectbox("Light Color", [
            "🔵 Cool Blue", "💜 Soft Violet", "🟢 Forest Green", "🟡 Warm Amber", "🌸 Rose Glow", "⬜ Pure White"
        ], index=["🔵 Cool Blue","💜 Soft Violet","🟢 Forest Green","🟡 Warm Amber","🌸 Rose Glow","⬜ Pure White"].index(
            st.session_state.pod_light) if st.session_state.pod_light in ["🔵 Cool Blue","💜 Soft Violet","🟢 Forest Green","🟡 Warm Amber","🌸 Rose Glow","⬜ Pure White"] else 0)
        brightness = st.slider("Brightness", 10, 100, 40, format="%d%%")
        light_effects = {
            "🔵 Cool Blue": ("Lowers cortisol, reduces heart rate variability", "#4FC3F7"),
            "💜 Soft Violet": ("Calms aggression, promotes introspection", "#9575CD"),
            "🟢 Forest Green": ("Biophilic response, restores mental energy", "#81C784"),
            "🟡 Warm Amber": ("Boosts serotonin, ideal for wind-down", "#FFB74D"),
            "🌸 Rose Glow": ("Mood lift, gentle warmth, reduces loneliness", "#F48FB1"),
            "⬜ Pure White": ("Alertness and clarity, full-spectrum stimulation", "#ECF0F1"),
        }
        effect, hex_col = light_effects.get(light, ("", "#FF9A3C"))
        st.markdown(f"""
        <div class='mw-card' style='border-left:4px solid {hex_col}; padding:12px 16px; margin-top:4px'>
          <span style='font-size:12px; color:#b8a9d4'>🔬 Science: {effect}</span>
        </div>
        """, unsafe_allow_html=True)
        st.session_state.pod_light = light

        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("<div class='section-title' style='font-size:18px'>🌸 Aroma Diffuser</div>", unsafe_allow_html=True)
        aroma = st.selectbox("Scent", ["🌿 Lavender", "🍃 Eucalyptus", "🌹 Rose", "🍋 Citrus", "🪵 Sandalwood", "🌸 Ylang Ylang"])
        intensity = st.select_slider("Diffuser Intensity", ["Subtle", "Light", "Medium", "Strong", "Intense"], value="Medium")
        aroma_effects = {
            "🌿 Lavender": "Anxiety & stress relief — reduces cortisol by up to 35%",
            "🍃 Eucalyptus": "Clears mental fog, improves respiratory flow and alertness",
            "🌹 Rose": "Emotional balance, reduces depression symptoms, mood lift",
            "🍋 Citrus": "Energizing, boosts dopamine, combats afternoon fatigue",
            "🪵 Sandalwood": "Grounding, reduces anxiety, promotes mental clarity",
            "🌸 Ylang Ylang": "Lowers blood pressure, calming, reduces nervous tension",
        }
        st.caption(f"🔬 {aroma_effects.get(aroma,'')}")
        st.session_state.pod_aroma = aroma

    with col2:
        st.markdown("<div class='section-title' style='font-size:18px'>🎵 Music & Sound</div>", unsafe_allow_html=True)
        music = st.selectbox("Sound Profile", ["🌊 Ocean Waves", "🌧 Gentle Rain", "🌲 Forest Sounds", "🎹 Soft Piano", "🎵 432 Hz Binaural", "🤫 Silence"])
        volume = st.slider("Volume", 0, 100, 65, format="%d%%")
        bpm = st.slider("BPM (entrainment)", 55, 90, 74,
            help="Brain entrainment — your heart rate gradually synchronizes to the music BPM. 60-72 BPM ideal for relaxation.")
        music_notes = {
            "🌊 Ocean Waves": "Broadband noise masks office sounds; rhythmic pattern slows breathing",
            "🌧 Gentle Rain": "Pink noise variant; 40% better focus than silence in studies",
            "🌲 Forest Sounds": "Biophilic audio; reduces stress hormone cortisol by 16%",
            "🎹 Soft Piano": "432 Hz tuning promotes emotional release and inner peace",
            "🎵 432 Hz Binaural": "Hemispheric synchronization; deepens meditation states",
            "🤫 Silence": "Complete silence for those with high sensory sensitivity",
        }
        st.caption(f"🔬 {music_notes.get(music,'')}")
        st.session_state.pod_music = music

        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("<div class='section-title' style='font-size:18px'>⏱ Session Settings</div>", unsafe_allow_html=True)
        duration = st.select_slider("Duration", [5, 10, 15, 20, 25, 30, 45, 60], value=st.session_state.pod_duration, format_func=lambda x: f"{x} min")
        st.session_state.pod_duration = duration

        chair_mode = st.selectbox("🪑 Biometric Chair Mode", ["Light Vibration", "Medium Massage", "Deep Tissue", "Heat Only", "Off"])

        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown(f"""
        <div class='mw-card-accent'>
          <div style='font-size:13px; color:#b8a9d4; margin-bottom:10px; font-weight:600'>🚀 Current Session Config</div>
          <div style='font-size:14px; color:#f5f0ff; line-height:2'>
            💡 {light} @ {brightness}% brightness<br>
            🎵 {music} @ {volume}% vol · {bpm} BPM<br>
            🌸 {aroma} · {intensity} intensity<br>
            ⏱ {duration} min · Chair: {chair_mode}
          </div>
        </div>
        """, unsafe_allow_html=True)

        if st.button("▶ Start Pod Session", use_container_width=True):
            with st.spinner("Initializing pod..."):
                time.sleep(1.5)
            st.success(f"✅ Pod A started! Enjoy your {duration}-minute {music.split()[1]} session. 🧘")
            st.balloons()


# ══════════════════════════════════════════════════
#  PAGE 4: BREATHE WITH ME
# ══════════════════════════════════════════════════
def page_breathe():
    st.markdown("<div class='hero-title'>🫁 Breathe With Me</div>", unsafe_allow_html=True)
    st.markdown("<p style='color:#b8a9d4'>Guided micro-meditation with scientifically-backed breathing techniques</p>", unsafe_allow_html=True)
    st.markdown("---")

    col1, col2 = st.columns([1, 1.2])

    with col1:
        st.markdown("<div class='section-title' style='font-size:18px'>🧘 Choose Technique</div>", unsafe_allow_html=True)
        technique = st.selectbox("Technique", [
            "4-7-8 Relaxation", "Box Breathing (4-4-4-4)",
            "Triangle (4-4-4)", "2-4 Quick Calm", "Diaphragmatic Breathing"
        ])
        techniques_info = {
            "4-7-8 Relaxation": {"in":4, "hold":7, "out":8, "desc":"Activates the parasympathetic nervous system. Dr. Andrew Weil's signature technique for fast anxiety relief.", "best":"Anxiety, pre-meeting stress, sleep prep"},
            "Box Breathing (4-4-4-4)": {"in":4, "hold":4, "out":4, "desc":"Used by US Navy SEALs under high-pressure situations. Brings clarity and emotional regulation.", "best":"High stress, overwhelm, focus preparation"},
            "Triangle (4-4-4)": {"in":4, "hold":4, "out":4, "desc":"Simple 3-phase technique. Easy for beginners — no extended holds required.", "best":"Beginners, mild stress, daily maintenance"},
            "2-4 Quick Calm": {"in":2, "hold":0, "out":4, "desc":"Extended exhale activates the vagus nerve instantly. Fast acting — results in under 2 minutes.", "best":"Acute stress spikes, pre-presentation"},
            "Diaphragmatic Breathing": {"in":5, "hold":2, "out":6, "desc":"Deep belly breathing that maximizes oxygen exchange and activates the relaxation response.", "best":"Chronic stress, tiredness, end of day reset"},
        }
        info = techniques_info[technique]
        st.markdown(f"""
        <div class='mw-card' style='margin-top:10px'>
          <div style='font-size:13px; color:#d4c5f0; line-height:1.7;margin-bottom:10px'>{info['desc']}</div>
          <div style='font-size:12px; color:#7a6d99'>⭐ <b>Best for:</b> {info['best']}</div>
          <div style='display:flex; gap:10px; margin-top:12px; font-size:13px; color:#FF9A3C; font-weight:600'>
            <span style='background:rgba(255,154,60,0.1);padding:4px 12px;border-radius:8px'>In: {info['in']}s</span>
            {"<span style='background:rgba(255,154,60,0.1);padding:4px 12px;border-radius:8px'>Hold: "+str(info['hold'])+"s</span>" if info['hold'] > 0 else ""}
            <span style='background:rgba(255,154,60,0.1);padding:4px 12px;border-radius:8px'>Out: {info['out']}s</span>
          </div>
        </div>
        """, unsafe_allow_html=True)

        cycles_target = st.slider("Target Cycles", 3, 10, 5)
        st.markdown("<br>", unsafe_allow_html=True)

        if st.button("▶ Start Breathing Session", use_container_width=True):
            st.markdown("<br>", unsafe_allow_html=True)
            progress_bar = st.progress(0)
            status_text = st.empty()
            cycle_display = st.empty()

            phases = []
            if info['in'] > 0: phases.append(("🌬 Inhale", info['in'], "Breathe in slowly through your nose..."))
            if info['hold'] > 0: phases.append(("⏸ Hold", info['hold'], "Hold your breath gently..."))
            phases.append(("💨 Exhale", info['out'], "Release slowly through your mouth..."))

            for cycle in range(cycles_target):
                for phase_name, count, instruction in phases:
                    for i in range(count, 0, -1):
                        status_text.markdown(f"""
                        <div class='mw-card-accent' style='text-align:center; padding:40px 30px; position:relative; overflow:hidden'>
                          <!-- Animated background rings -->
                          <div style='position:absolute; top:50%; left:50%; transform:translate(-50%,-50%);
                            width:{80 + (5-i)*20}px; height:{80 + (5-i)*20}px; border-radius:50%;
                            border:2px solid rgba(255,154,60,{0.1 + (5-i)*0.05});
                            transition:all 0.8s ease;'></div>
                          <div style='position:absolute; top:50%; left:50%; transform:translate(-50%,-50%);
                            width:{140 + (5-i)*20}px; height:{140 + (5-i)*20}px; border-radius:50%;
                            border:1px solid rgba(255,209,102,{0.06 + (5-i)*0.02});
                            transition:all 0.8s ease;'></div>

                          <div style='font-size:48px; margin-bottom:12px; animation:float 2s ease-in-out infinite'>🫁</div>
                          <div style='font-family:"Playfair Display",serif; font-size:30px; color:#FF9A3C; font-weight:700; text-shadow:0 0 20px rgba(255,209,102,0.5)'>{phase_name}</div>
                          <div style='font-size:72px; font-weight:800; background:linear-gradient(135deg,#FF9A3C,#95E06C); -webkit-background-clip:text; -webkit-text-fill-color:transparent; background-clip:text; margin:8px 0; animation:countUp 0.3s ease-out'>{i}</div>
                          <div style='font-size:15px; color:#b8a9d4; font-style:italic'>{instruction}</div>
                          <div style='font-size:12px; color:#7a6d99; margin-top:12px; letter-spacing:1px; text-transform:uppercase'>Cycle {cycle+1} of {cycles_target}</div>
                          <!-- Ripple rings -->
                          <div style='position:absolute; top:50%; left:50%; transform:translate(-50%,-50%);
                            width:200px; height:200px; border-radius:50%;
                            border:2px solid rgba(255,154,60,0.22);
                            animation:ripple 2s ease-out infinite;'></div>
                        </div>
                        """, unsafe_allow_html=True)
                        progress_bar.progress(int((cycle / cycles_target) * 100))
                        time.sleep(1)

            status_text.markdown(f"""
            <div class='mw-card-accent' style='text-align:center; padding:40px 30px; position:relative; overflow:hidden'>
              <div style='position:absolute; top:50%; left:50%; transform:translate(-50%,-50%);
                width:250px; height:250px; border-radius:50%;
                background:radial-gradient(circle, rgba(255,154,60,0.08), transparent);
                animation:breatheCircle 3s ease-in-out infinite;'></div>
              <div style='font-size:60px; margin-bottom:8px; animation:float 3s ease-in-out infinite'>🎉</div>
              <div style='font-family:"Playfair Display",serif; font-size:28px; color:#FF9A3C; font-weight:700; margin-top:8px; text-shadow:0 0 20px rgba(255,209,102,0.5)'>
                Session Complete!
              </div>
              <div style='font-size:15px; color:#b8a9d4; margin-top:10px'>{cycles_target} cycles of {technique} completed ✦</div>
              <div style='margin-top:16px; display:inline-block; padding:8px 20px; background:rgba(255,154,60,0.1); border:1px solid rgba(255,154,60,0.35); border-radius:20px; font-size:13px; color:#FF9A3C'>
                🧠 Parasympathetic nervous system activated
              </div>
            </div>
            """, unsafe_allow_html=True)
            progress_bar.progress(100)
            st.session_state.breathe_cycles += cycles_target
            if st.session_state.breathe_cycles >= 20 and "🫁 Breathwork Pro" not in st.session_state.badges:
                st.session_state.badges.append("🫁 Breathwork Pro")
            st.balloons()

    with col2:
        st.markdown("<div class='section-title' style='font-size:18px'>📊 Science Behind Breathing</div>", unsafe_allow_html=True)
        science_data = {
            "Technique": ["4-7-8 Relax", "Box Breathing", "2-4 Calm", "Triangle", "Diaphragmatic"],
            "Stress Reduction": [42, 38, 31, 28, 35],
            "Time to Effect (min)": [2, 3, 1, 2.5, 4],
            "HRV Improvement (%)": [22, 18, 14, 16, 20],
        }
        df_sci = pd.DataFrame(science_data)
        fig_sci = px.bar(df_sci, x="Technique", y="Stress Reduction",
            color="Stress Reduction", color_continuous_scale=["#C77DFF", "#FF9A3C", "#FFD166"],
            labels={"Stress Reduction": "Stress Reduction (%)"},
            text="Stress Reduction"
        )
        fig_sci.update_traces(texttemplate="%{text}%", textposition="outside", marker_line_width=0)
        fig_sci.update_layout(
            paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
            font=dict(family='Nunito', color='#b8a9d4'), height=260,
            margin=dict(l=0,r=0,t=20,b=0), showlegend=False,
            coloraxis_showscale=False,
            xaxis=dict(gridcolor='rgba(255,154,60,0.1)', tickfont=dict(size=11)),
            yaxis=dict(gridcolor='rgba(255,154,60,0.1)', range=[0,55]),
        )
        st.plotly_chart(fig_sci, use_container_width=True, config={"displayModeBar": False})

        st.markdown("<div class='section-title' style='font-size:18px; margin-top:8px'>🏅 Your Breathing Stats</div>", unsafe_allow_html=True)
        st.metric("Total Cycles This Month", st.session_state.breathe_cycles + 47, "+12 vs last month")
        st.metric("Avg Stress Reduction per Session", "38%", "+5%")
        st.metric("Favourite Technique", "4-7-8 Relaxation", "Used 12x this month")


# ══════════════════════════════════════════════════
#  PAGE 5: SCHEDULER
# ══════════════════════════════════════════════════
def page_scheduler():
    st.markdown("<div class='hero-title'>📅 Pod Scheduler</div>", unsafe_allow_html=True)
    st.markdown("<p style='color:#b8a9d4'>Book your Smart Stress Relief Pod session in advance</p>", unsafe_allow_html=True)
    st.markdown("---")

    col1, col2 = st.columns([1.2, 1])

    with col1:
        with st.form("booking_form"):
            st.markdown("<div class='section-title' style='font-size:18px'>New Booking</div>", unsafe_allow_html=True)

            pod = st.selectbox("Select Pod", ["🪑 Pod A – Ocean Calm", "🪑 Pod B – Focus Flow", "🪑 Pod C – Forest Breathe"])
            date = st.date_input("Date", value=datetime.now().date(), min_value=datetime.now().date())

            time_slots = ["9:00 AM", "9:30 AM", "10:00 AM", "10:30 AM", "11:00 AM", "11:30 AM",
                          "12:00 PM", "12:30 PM", "1:00 PM", "1:30 PM", "2:00 PM", "2:30 PM",
                          "3:00 PM", "3:30 PM", "4:00 PM", "4:30 PM", "5:00 PM"]
            taken = ["9:00 AM", "9:30 AM", "1:30 PM", "12:00 PM"]  # simulated
            available = [t for t in time_slots if t not in taken]
            selected_time = st.selectbox("Available Time Slot", available)

            duration = st.select_slider("Session Duration", [10, 15, 20, 25, 30, 45], value=15, format_func=lambda x: f"{x} minutes")

            ai_config = st.checkbox("🤖 Let MoodSync AI auto-configure pod settings", value=True)
            reminder = st.checkbox("🔔 Remind me 15 minutes before", value=True)

            notes = st.text_area("Personal Notes (optional)", placeholder="e.g. 'Before quarterly review — need deep calm'", height=80)

            submitted = st.form_submit_button("✅ Confirm Booking", use_container_width=True)
            if submitted:
                booking = {
                    "pod": pod.split("–")[1].strip(),
                    "date": str(date),
                    "time": selected_time,
                    "duration": duration,
                    "ai_config": ai_config,
                    "notes": notes,
                }
                st.session_state.booked_sessions.append(booking)
                st.success(f"✅ Booked! {pod} on {date} at {selected_time} for {duration} min.")
                if ai_config:
                    st.info("🤖 MoodSync AI will auto-configure your pod 5 minutes before the session.")

    with col2:
        st.markdown("<div class='section-title' style='font-size:18px'>📋 Upcoming Bookings</div>", unsafe_allow_html=True)

        all_bookings = [
            {"Pod": "Ocean Calm", "Date": "Today", "Time": "3:30 PM", "Duration": "15 min", "Status": "🔵 Confirmed"},
            {"Pod": "Focus Flow", "Date": "Tomorrow", "Time": "9:00 AM", "Duration": "20 min", "Status": "🔵 Confirmed"},
        ] + [
            {"Pod": b["pod"], "Date": b["date"], "Time": b["time"], "Duration": f"{b['duration']} min", "Status": "🟢 New"}
            for b in st.session_state.booked_sessions
        ]
        if all_bookings:
            df_book = pd.DataFrame(all_bookings)
            st.dataframe(df_book, use_container_width=True, hide_index=True)
        else:
            st.info("No upcoming bookings. Use the form to book your first session!")

        st.markdown("---")
        st.markdown("<div class='section-title' style='font-size:18px'>📊 Availability Heatmap</div>", unsafe_allow_html=True)

        slots = ["9AM","10AM","11AM","12PM","1PM","2PM","3PM","4PM","5PM"]
        pods = ["Pod A", "Pod B", "Pod C"]
        np.random.seed(42)
        availability = np.random.randint(0, 2, size=(3, 9))
        availability[0][1] = 0
        availability[1][4] = 0

        fig_heat = go.Figure(go.Heatmap(
            z=availability, x=slots, y=pods,
            colorscale=[[0, "#FF6B6B"], [1, "#FF9A3C"]],
            showscale=False,
            text=[["✓" if v else "✗" for v in row] for row in availability],
            texttemplate="%{text}", textfont={"size": 14},
            hovertemplate="<b>%{y}</b> at <b>%{x}</b>: %{text}<extra></extra>",
        ))
        fig_heat.update_layout(
            paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
            font=dict(family='Nunito', color='#b8a9d4'),
            height=180, margin=dict(l=60,r=0,t=10,b=0),
            xaxis=dict(tickfont=dict(size=11)), yaxis=dict(tickfont=dict(size=11)),
        )
        st.plotly_chart(fig_heat, use_container_width=True, config={"displayModeBar": False})
        st.caption("🟢 Green = Available · 🔴 Red = Booked")


# ══════════════════════════════════════════════════
#  PAGE 6: JOURNAL
# ══════════════════════════════════════════════════
def page_journal():
    st.markdown("<div class='hero-title'>📓 Session Journal</div>", unsafe_allow_html=True)
    st.markdown("<p style='color:#b8a9d4'>Reflect on your sessions and track your stress reduction journey</p>", unsafe_allow_html=True)
    st.markdown("---")

    tab1, tab2 = st.tabs(["✍️ New Entry", "📚 Past Entries"])

    with tab1:
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("<div class='section-title' style='font-size:18px'>Rate Your Stress</div>", unsafe_allow_html=True)
            stress_before = st.slider("😰 Stress BEFORE session", 1, 5, 4,
                format="%d/5", help="1 = Very Low, 5 = Very High")
            stress_after = st.slider("😌 Stress AFTER session", 1, 5, 2,
                format="%d/5", help="1 = Very Low, 5 = Very High")
            reduction = ((stress_before - stress_after) / stress_before) * 100
            delta_color = "normal" if reduction > 0 else "inverse"
            st.metric("📉 Stress Reduction", f"{reduction:.0f}%",
                delta=f"{stress_before - stress_after} levels down",
                delta_color=delta_color)

        with col2:
            st.markdown("<div class='section-title' style='font-size:18px'>Post-Session Mood</div>", unsafe_allow_html=True)
            post_mood = st.selectbox("How do you feel now?", [
                "😌 Calmer", "😊 Refreshed", "🧠 Focused", "😴 Sleepy",
                "🌟 Energized", "😐 Same as before", "😤 Still stressed"
            ])
            session_date = st.date_input("Session Date", value=datetime.now().date())
            what_worked = st.multiselect("What worked best?", [
                "🌊 Ocean sounds", "🌿 Lavender aroma", "🔵 Blue light",
                "🪑 Biometric chair", "🫁 Breathing exercise", "🎵 Music",
                "⏱ Session duration", "🤖 AI recommendations"
            ], default=["🌊 Ocean sounds", "🌿 Lavender aroma"])

        st.markdown("<div class='section-title' style='font-size:18px; margin-top:12px'>📝 Your Reflection</div>", unsafe_allow_html=True)
        reflection = st.text_area("Write freely about your session experience...",
            placeholder="How did you feel during the session? What surprised you? What would you change?",
            height=130)

        tags_input = st.text_input("Tags (comma separated)", placeholder="#relaxed, #focused, #productive")
        tags = [t.strip() for t in tags_input.split(",") if t.strip()]

        if st.button("💾 Save Journal Entry", use_container_width=True):
            if reflection:
                entry = {
                    "date": str(session_date),
                    "stress_before": stress_before,
                    "stress_after": stress_after,
                    "mood": post_mood,
                    "note": reflection,
                    "tags": tags,
                }
                st.session_state.journal_entries.insert(0, entry)
                st.success("✅ Journal entry saved! MoodSync AI will use this to improve future recommendations.")
                st.balloons()
            else:
                st.warning("Please write a reflection before saving.")

    with tab2:
        st.markdown("<div class='section-title' style='font-size:18px'>📚 All Entries</div>", unsafe_allow_html=True)

        if not st.session_state.journal_entries:
            st.info("No journal entries yet. Complete a session and write your first reflection!")
        else:
            for i, entry in enumerate(st.session_state.journal_entries):
                reduction_pct = ((entry['stress_before'] - entry['stress_after']) / entry['stress_before'] * 100)
                color = stress_color(entry['stress_after'] * 20)
                tags_html = "".join([f"<span class='badge' style='font-size:11px'>{t}</span>" for t in entry.get('tags', [])])
                with st.expander(f"📅 {entry['date']}  ·  {entry['mood']}  ·  ↓{reduction_pct:.0f}% stress"):
                    st.markdown(f"""
                    <div style='display:flex; gap:20px; margin-bottom:12px'>
                      <div>
                        <span style='font-size:12px; color:#7a6d99'>BEFORE</span><br>
                        <span style='font-size:22px; font-weight:700; color:#FFD166'>{'⭐'*entry['stress_before']}</span>
                      </div>
                      <div style='font-size:28px; color:#FF9A3C; align-self:center'>→</div>
                      <div>
                        <span style='font-size:12px; color:#7a6d99'>AFTER</span><br>
                        <span style='font-size:22px; font-weight:700; color:{color}'>{'⭐'*entry['stress_after']}</span>
                      </div>
                      <div style='margin-left:auto; text-align:right'>
                        <div style='font-size:24px; font-weight:800; color:#FF9A3C'>-{reduction_pct:.0f}%</div>
                        <div style='font-size:11px; color:#7a6d99'>reduction</div>
                      </div>
                    </div>
                    <div style='font-size:14px; color:#d4c5f0; line-height:1.7; margin-bottom:10px'>{entry['note']}</div>
                    <div>{tags_html}</div>
                    """, unsafe_allow_html=True)


# ══════════════════════════════════════════════════
#  PAGE 7: ANALYTICS
# ══════════════════════════════════════════════════
def page_analytics():
    st.markdown("<div class='hero-title'>📊 Wellness Analytics</div>", unsafe_allow_html=True)
    st.markdown("<p style='color:#b8a9d4'>Deep insights into your stress patterns and session effectiveness</p>", unsafe_allow_html=True)
    st.markdown("---")

    # ── KPIs ──
    c1, c2, c3, c4 = st.columns(4)
    with c1: st.metric("Total Sessions", "18", "+3 this week")
    with c2: st.metric("Avg Stress Reduction", "41%", "+6% vs last month")
    with c3: st.metric("Hours in Pod", "4.5 hrs", "This month")
    with c4: st.metric("Wellness Score", "72/100", "+9 points")

    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)

    with col1:
        # 30-day stress trend
        st.markdown("<div class='section-title' style='font-size:18px'>📈 30-Day Stress Trend</div>", unsafe_allow_html=True)
        np.random.seed(7)
        dates = [datetime.now() - timedelta(days=x) for x in range(29, -1, -1)]
        trend = 80 - np.cumsum(np.random.normal(1, 8, 30))
        trend = np.clip(trend, 15, 95)
        sessions_days = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29]

        fig_trend = go.Figure()
        fig_trend.add_trace(go.Scatter(
            x=dates, y=trend, fill='tozeroy',
            fillcolor='rgba(255,154,60,0.08)',
            line=dict(color='#FF9A3C', width=2.5),
            hovertemplate="<b>%{x|%b %d}</b><br>Stress: %{y:.0f}<extra></extra>",
            name="Stress Level"
        ))
        for d in sessions_days:
            fig_trend.add_vline(x=dates[d], line_dash="dot", line_color="rgba(255,154,60,0.3)")

        fig_trend.add_hline(y=65, line_dash="dash", line_color="rgba(255,209,102,0.4)", annotation_text="High threshold")
        fig_trend.add_hline(y=35, line_dash="dash", line_color="rgba(255,154,60,0.45)", annotation_text="Low threshold")

        fig_trend.update_layout(
            paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
            font=dict(family='Nunito', color='#b8a9d4'), height=260,
            margin=dict(l=0,r=0,t=10,b=0), showlegend=False,
            xaxis=dict(gridcolor='rgba(255,154,60,0.08)', showline=False, tickformat="%b %d"),
            yaxis=dict(gridcolor='rgba(255,154,60,0.08)', range=[0,100]),
        )
        st.plotly_chart(fig_trend, use_container_width=True, config={"displayModeBar": False})

    with col2:
        # Feature effectiveness radar
        st.markdown("<div class='section-title' style='font-size:18px'>🎯 Feature Effectiveness Radar</div>", unsafe_allow_html=True)
        categories = ["MoodSync AI", "Breathe With Me", "Pod Scheduler", "Journal", "Stress Dashboard"]
        values = [88, 92, 74, 85, 79]

        fig_radar = go.Figure(go.Scatterpolar(
            r=values + [values[0]],
            theta=categories + [categories[0]],
            fill='toself',
            fillcolor='rgba(255,154,60,0.12)',
            line=dict(color='#FF9A3C', width=2),
            marker=dict(color='#FFD166', size=8),
        ))
        fig_radar.update_layout(
            polar=dict(
                bgcolor='rgba(26,15,46,0.5)',
                radialaxis=dict(visible=True, range=[0,100], gridcolor='rgba(255,154,60,0.22)', tickfont=dict(color='#7a6d99', size=10)),
                angularaxis=dict(gridcolor='rgba(255,154,60,0.22)', tickfont=dict(color='#b8a9d4', size=12)),
            ),
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(family='Nunito', color='#b8a9d4'),
            height=260, margin=dict(l=40,r=40,t=20,b=20), showlegend=False,
        )
        st.plotly_chart(fig_radar, use_container_width=True, config={"displayModeBar": False})

    # ── Session breakdown ──
    col3, col4 = st.columns(2)
    with col3:
        st.markdown("<div class='section-title' style='font-size:18px'>🕐 Peak Stress Hours</div>", unsafe_allow_html=True)
        hours = list(range(8, 19))
        stress_by_hour = [55, 72, 68, 58, 65, 81, 74, 56, 62, 48, 41]
        fig_hour = go.Figure(go.Bar(
            x=[f"{h}:00" for h in hours], y=stress_by_hour,
            marker_color=[stress_color(v) for v in stress_by_hour],
            hovertemplate="<b>%{x}</b><br>Avg stress: %{y}<extra></extra>",
        ))
        fig_hour.update_layout(
            paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
            font=dict(family='Nunito', color='#b8a9d4'), height=220,
            margin=dict(l=0,r=0,t=10,b=0),
            xaxis=dict(gridcolor='rgba(255,154,60,0.1)'),
            yaxis=dict(gridcolor='rgba(255,154,60,0.1)', range=[0,100]),
        )
        st.plotly_chart(fig_hour, use_container_width=True, config={"displayModeBar": False})
        st.caption("🔴 Peak stress: 12 PM–1 PM lunch crunch. Recommended pod slot: 11:45 AM")

    with col4:
        st.markdown("<div class='section-title' style='font-size:18px'>🌸 Most Effective Aromas</div>", unsafe_allow_html=True)
        aromas = ["Lavender", "Eucalyptus", "Citrus", "Sandalwood", "Rose"]
        effectivness = [42, 35, 28, 31, 26]
        fig_aroma = px.pie(
            values=effectivness, names=aromas,
            color_discrete_sequence=["#FF9A3C", "#FFD166", "#95E06C", "#b8a9d4", "#FF6B6B"],
            hole=0.45,
        )
        fig_aroma.update_traces(
            textfont_size=12, textfont_family="Nunito",
            hovertemplate="<b>%{label}</b><br>Effectiveness: %{value}%<extra></extra>",
        )
        fig_aroma.update_layout(
            paper_bgcolor='rgba(0,0,0,0)', height=220,
            font=dict(family='Nunito', color='#b8a9d4'),
            margin=dict(l=0,r=0,t=10,b=0),
            legend=dict(font=dict(color='#b8a9d4', size=11), bgcolor='rgba(0,0,0,0)'),
        )
        st.plotly_chart(fig_aroma, use_container_width=True, config={"displayModeBar": False})


# ══════════════════════════════════════════════════
#  PAGE 8: PERSONAS & RESEARCH
# ══════════════════════════════════════════════════
def page_personas():
    st.markdown("<div class='hero-title'>👥 Personas & Research</div>", unsafe_allow_html=True)
    st.markdown("<p style='color:#b8a9d4'>10 detailed user personas developed through primary research with 47 employees</p>", unsafe_allow_html=True)
    st.markdown("---")

    personas = [
        {"name": "Riya Sharma", "age": 28, "role": "IT Developer", "emoji": "👩‍💻",
         "stress": 72, "triggers": "Tight deadlines, screen fatigue, back-to-back meetings",
         "pref": "Ocean sounds, blue light, lavender", "need": "Quick 15-min pod before presentations"},
        {"name": "Aarav Mehta", "age": 35, "role": "Marketing Manager", "emoji": "📊",
         "stress": 78, "triggers": "Client presentations, multitasking, high KPI pressure",
         "pref": "Breathwork, violet light, eucalyptus", "need": "Auto AI pod config before meetings"},
        {"name": "Priya Nair", "age": 24, "role": "Graduate Intern", "emoji": "🎓",
         "stress": 60, "triggers": "New environment, imposter syndrome, information overload",
         "pref": "Guided meditation, soft music, journaling", "need": "Beginner-friendly sessions with guidance"},
        {"name": "Sameer Joshi", "age": 40, "role": "HR Executive", "emoji": "🏢",
         "stress": 65, "triggers": "Workload, employee conflicts, administrative burden",
         "pref": "Silence, aroma therapy, biometric chair", "need": "Stress data for wellness program ROI"},
        {"name": "Neha Kulkarni", "age": 32, "role": "Product Designer", "emoji": "🎨",
         "stress": 58, "triggers": "Creative blocks, perfectionism, feedback cycles",
         "pref": "Forest sounds, green light, sandalwood", "need": "Mood-pattern journal for creative insights"},
        {"name": "Vikram Gupta", "age": 45, "role": "Finance Lead", "emoji": "💼",
         "stress": 81, "triggers": "Quarter-end pressure, regulatory compliance, deadlines",
         "pref": "White noise, minimal sensory input, short sessions", "need": "10-min micro-sessions at lunch"},
        {"name": "Sunita Rao", "age": 38, "role": "Operations Manager", "emoji": "⚙️",
         "stress": 69, "triggers": "Supply chain issues, team coordination, remote management",
         "pref": "Lavender, warm amber light, ambient music", "need": "Recurring weekly booking with reminders"},
        {"name": "Aryan Kapoor", "age": 22, "role": "Sales Trainee", "emoji": "📱",
         "stress": 55, "triggers": "Rejection, target pressure, peer comparison",
         "pref": "Energizing citrus, upbeat calm music, affirmations", "need": "Gamified badges to stay motivated"},
        {"name": "Deepa Singh", "age": 50, "role": "Legal Counsel", "emoji": "⚖️",
         "stress": 74, "triggers": "Case complexity, ethical dilemmas, long hours",
         "pref": "Absolute silence, aroma only, dim lighting", "need": "Complete sensory-quiet pod sessions"},
        {"name": "Rohan D'Souza", "age": 29, "role": "Sales Executive", "emoji": "📞",
         "stress": 83, "triggers": "Cold calls, rejection rates, constant pressure",
         "pref": "Citrus scent, short energy reset, positive affirmations", "need": "Between-call 10-min micro-sessions"},
    ]

    # ── Filter ──
    col_f1, col_f2 = st.columns([1, 1])
    with col_f1:
        stress_filter = st.select_slider("Filter by Stress Level", ["Any", "Low (≤40)", "Medium (41-70)", "High (71+)"], value="Any")
    with col_f2:
        sort_by = st.selectbox("Sort by", ["Stress Level ↓", "Stress Level ↑", "Age ↑", "Name A-Z"])

    # Filter logic
    filtered = personas.copy()
    if stress_filter == "Low (≤40)": filtered = [p for p in filtered if p["stress"] <= 40]
    elif stress_filter == "Medium (41-70)": filtered = [p for p in filtered if 41 <= p["stress"] <= 70]
    elif stress_filter == "High (71+)": filtered = [p for p in filtered if p["stress"] >= 71]

    if sort_by == "Stress Level ↓": filtered.sort(key=lambda x: x["stress"], reverse=True)
    elif sort_by == "Stress Level ↑": filtered.sort(key=lambda x: x["stress"])
    elif sort_by == "Age ↑": filtered.sort(key=lambda x: x["age"])
    elif sort_by == "Name A-Z": filtered.sort(key=lambda x: x["name"])

    # ── Persona Cards ──
    st.markdown(f"<br><div style='color:#7a6d99; font-size:13px; margin-bottom:16px'>Showing {len(filtered)} of {len(personas)} personas</div>", unsafe_allow_html=True)

    for i in range(0, len(filtered), 2):
        cols = st.columns(2)
        for j, col in enumerate(cols):
            if i + j < len(filtered):
                p = filtered[i + j]
                sc = stress_color(p["stress"])
                sl, sl_class = stress_label(p["stress"])
                with col:
                    st.markdown(f"""
                    <div class='mw-card persona-card' style='min-height:200px; animation-delay:{(i+j)*0.1}s'>
                      <div style='display:flex; align-items:center; gap:14px; margin-bottom:14px'>
                        <div style='font-size:36px; background:linear-gradient(135deg,rgba(255,154,60,0.12),rgba(6,214,160,0.08)); width:60px; height:60px; border-radius:50%; display:flex; align-items:center; justify-content:center; border:2px solid rgba(255,154,60,0.3); flex-shrink:0; animation:float {3 + (i+j)*0.5}s ease-in-out infinite; box-shadow:0 0 16px rgba(6,214,160,0.15)'>{p['emoji']}</div>
                        <div>
                          <div style='font-weight:700; font-size:17px; color:#f5f0ff'>{p['name']}</div>
                          <div style='font-size:12px; color:#b8a9d4'>{p['role']} · Age {p['age']}</div>
                          <div style='margin-top:6px'><span class='tag {sl_class}'>{sl}: {p['stress']}/100</span></div>
                        </div>
                        <!-- Stress mini-bar -->
                        <div style='margin-left:auto; text-align:right'>
                          <div style='font-size:22px; font-weight:800; color:{sc}'>{p['stress']}</div>
                          <div style='width:40px; height:4px; background:rgba(255,255,255,0.06); border-radius:2px; overflow:hidden; margin-top:4px'>
                            <div style='height:100%; width:{p["stress"]}%; background:{sc}; border-radius:2px; box-shadow:0 0 6px {sc}60'></div>
                          </div>
                        </div>
                      </div>
                      <div style='font-size:11px; color:#7a6d99; margin-bottom:4px; text-transform:uppercase; letter-spacing:0.8px'>😰 Stress Triggers</div>
                      <div style='font-size:13px; color:#d4c5f0; margin-bottom:10px; line-height:1.5'>{p['triggers']}</div>
                      <div style='font-size:11px; color:#7a6d99; margin-bottom:4px; text-transform:uppercase; letter-spacing:0.8px'>💆 Preferences</div>
                      <div style='font-size:13px; color:#d4c5f0; margin-bottom:10px; line-height:1.5'>{p['pref']}</div>
                      <div style='font-size:11px; color:#7a6d99; margin-bottom:4px; text-transform:uppercase; letter-spacing:0.8px'>🎯 App Need</div>
                      <div style='font-size:13px; color:#FF9A3C; font-weight:600; background:rgba(255,154,60,0.06); padding:8px 12px; border-radius:8px; border-left:3px solid rgba(255,154,60,0.45)'>{p['need']}</div>
                    </div>
                    """, unsafe_allow_html=True)

    # ── Research Summary ──
    st.markdown("---")
    st.markdown("<div class='section-title'>📋 Research Summary</div>", unsafe_allow_html=True)

    research_cols = st.columns(4)
    research_stats = [
        ("47", "Employees Surveyed"),
        ("12", "In-depth Interviews"),
        ("3 days", "Field Observation"),
        ("92%", "Would Use the App"),
    ]
    for col, (num, label) in zip(research_cols, research_stats):
        with col:
            st.markdown(f"""
            <div class='mw-card' style='text-align:center; padding:20px'>
              <div style='font-size:34px; font-weight:800; color:#FF9A3C'>{num}</div>
              <div style='font-size:13px; color:#b8a9d4; margin-top:4px'>{label}</div>
            </div>
            """, unsafe_allow_html=True)


# ══════════════════════════════════════════════════
#  MAIN ROUTER
# ══════════════════════════════════════════════════
def main():
    if not st.session_state.logged_in:
        login_page()
    else:
        page = render_sidebar()

        if   "Dashboard"       in page: page_dashboard()
        elif "MoodSync"        in page: page_moodsync()
        elif "Pod Control"     in page: page_pod()
        elif "Breathe"         in page: page_breathe()
        elif "Scheduler"       in page: page_scheduler()
        elif "Journal"         in page: page_journal()
        elif "Analytics"       in page: page_analytics()
        elif "Personas"        in page: page_personas()

if __name__ == "__main__":
    main()