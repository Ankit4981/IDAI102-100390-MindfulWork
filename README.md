# IDAI102-100390-MindfulWork
MindfulWork is a vibrant wor<div align="center">

# 🧘 MindfulWork
### *Smart Stress Relief for the Modern Workplace*

**by FutureForward Wellness Platform**

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.35%2B-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)
[![Plotly](https://img.shields.io/badge/Plotly-5.22%2B-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)](https://plotly.com)
[![License](https://img.shields.io/badge/License-MIT-06D6A0?style=for-the-badge)](LICENSE)

---

> *"Because your team deserves more than a ping-pong table."*

</div>

---

## 🌈 What is MindfulWork?

**MindfulWork** is a vibrant, data-driven wellness platform built for modern workplaces. It helps employees manage stress, track their mood, book sensory relaxation pod sessions, practise guided breathing, journal their thoughts, and review personalised analytics — all from a single, beautiful dashboard.

Developed as part of the **FutureForward Wellness** initiative, MindfulWork combines behavioural science, biometric data, and AI-assisted recommendations to make workplace wellbeing genuinely effective — and genuinely lovely to look at.

---

## ✨ Features at a Glance

| 🖥️ Page | 💡 What it does |
|---|---|
| 🏠 **Dashboard** | Real-time stress metrics, daily wellness score, team mood overview |
| 🎭 **MoodSync** | Log your current mood with emoji sliders and get personalised suggestions |
| 🛸 **Pod Control** | Book and configure sensory relaxation pod sessions (light, aroma, sound) |
| 🌬️ **Breathe** | Animated guided breathing exercises with live timers |
| 📅 **Scheduler** | Book recurring wellness sessions with smart reminders |
| 📓 **Journal** | Mood-pattern journaling with tag-based insights |
| 📊 **Analytics** | Stress trends, peak-hour charts, aroma effectiveness, team heatmaps |
| 👥 **Personas & Research** | 10 detailed user personas from primary research with 47 employees |

---

## 🎨 Design Philosophy

MindfulWork is built around a **vibrant rainbow food palette** on a deep cosmic background. Every pixel is intentional:

- 🪸 **Coral** `#FF6B6B` — energy & urgency cues
- 🍊 **Orange** `#FF9A3C` — warmth & CTAs  
- 🌟 **Amber** `#FFD166` — metrics & highlights  
- 🍃 **Lime** `#95E06C` — success states  
- 🌿 **Mint** `#06D6A0` — calm & completion  
- 🩵 **Sky** `#74C7EC` — informational  
- 💜 **Lavender** `#C77DFF` — creative & focus  
- 🌸 **Rose** `#FF6EB4` — gentle alerts  

Animations include floating cards, shimmer effects, rainbow progress bars, ripple buttons, and ambient gradient blobs — all running smooth with CSS keyframes, no JavaScript required.

---

## 🚀 Getting Started

### Prerequisites

- Python **3.10+**
- pip

### 1 · Clone the repo

```bash
git clone https://github.com/your-org/mindfulwork.git
cd mindfulwork
```

### 2 · Set up a virtual environment *(recommended)*

```bash
python -m venv venv
source venv/bin/activate        # macOS / Linux
venv\Scripts\activate           # Windows
```

### 3 · Install dependencies

```bash
pip install -r requirements.txt
```

### 4 · Configure environment variables

```bash
cp .env.example .env
# Edit .env and add your secrets (e.g. admin password hash)
```

### 5 · Run the app 🎉

```bash
streamlit run app.py
```

Open your browser at **** and enjoy!

---

## 📦 Dependencies

| Package | Version | Purpose |
|---|---|---|
| `streamlit` | ≥ 1.35 | Web application framework |
| `pandas` | ≥ 2.2 | Data manipulation & analysis |
| `numpy` | ≥ 1.26 | Numerical computing |
| `plotly` | ≥ 5.22 | Interactive charts & graphs |
| `python-dateutil` | ≥ 2.9 | Extended date parsing |
| `bcrypt` | ≥ 4.1 | Secure password hashing |
| `python-dotenv` | ≥ 1.0 | `.env` secrets management |

### Optional add-ons

Uncomment these in `requirements.txt` for extra power:

```
streamlit-option-menu   # Styled nav menus
streamlit-extras        # Handy Streamlit utilities
streamlit-lottie        # Lottie animations
openpyxl                # Excel export
reportlab               # PDF generation
```

---

## 🗂️ Project Structure

```
mindfulwork/
│
├── app.py                  # 🧠 Main Streamlit application (all pages + CSS)
├── requirements.txt        # 📦 Python dependencies
├── README.md               # 📖 You are here!
│
└── assets/                 # 🖼️ Optional: logos, images, Lottie JSON files
```

---

## 👥 User Personas

MindfulWork was designed around **10 research-driven personas** developed through:

- 🗣️ **47 employees** surveyed
- 🎙️ **12 in-depth interviews** conducted
- 🔍 **3 days** of field observation
- ✅ **92%** of employees said they *would use the app*

Personas range from *Riya the IT Developer* (screen fatigue, deadline stress) to *Rohan the Sales Executive* (cold-call anxiety, high rejection pressure) — each with tailored session preferences and unique app needs.

---

## 🔐 Authentication

MindfulWork ships with a built-in login page. Passwords are hashed using **bcrypt** — never stored in plain text.

> ⚠️ **Production note:** Replace the default credential store with a proper database (PostgreSQL, Supabase, etc.) and rotate all secrets before deploying.

---

## 📊 Analytics Highlights

The **Analytics page** surfaces:

- 📈 **7-day stress trends** (line chart with gradient fill)
- 🕐 **Hourly stress heatmap** (peak: 12–1 PM lunch crunch)
- 🌸 **Top 5 most effective aromas** (donut chart)
- 🏢 **Department-wise wellness scores** (bar chart)

All charts are built with **Plotly**, styled to match the dark cosmic theme, and fully responsive.

---

## 🛸 Pod Control Module

Book a **sensory relaxation pod** session in seconds:

1. Choose your session duration (10 / 15 / 30 min)
2. Select ambient lighting colour and intensity
3. Pick an aromatherapy scent (Lavender, Eucalyptus, Citrus, Sandalwood, Rose)
4. Set your soundscape (Ocean, Forest, White Noise, Binaural Beats)
5. Hit **Book Pod** — the AI recommends your optimal slot automatically

---

## 🌬️ Breathing Module

Guided breathwork with three science-backed techniques:

| Technique | Pattern | Best for |
|---|---|---|
| **Box Breathing** | 4-4-4-4 | Focus & calm |
| **4-7-8 Breathing** | 4-7-8 | Anxiety relief |
| **Coherent Breathing** | 5-5 | Heart rate variability |

Animated breathing circle expands and contracts in real time, with a live countdown timer.

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you'd like to change.

1. Fork the repo
2. Create your feature branch: `git checkout -b feature/amazing-feature`
3. Commit your changes: `git commit -m 'Add amazing feature'`
4. Push to the branch: `git push origin feature/amazing-feature`
5. Open a Pull Request 🚀

---

## 📜 License

Distributed under the **MIT License**. See `LICENSE` for more information.

---

<div align="center">

Made with 💜 by the **FutureForward Wellness** team

*Last updated: April 2026*

🧘 **Breathe in. Breathe out. Ship great software.**

</div>kplace wellness platform that helps employees beat stress through guided breathing, mood tracking, sensory pod booking, and personalised analytics. Built with Streamlit and Plotly on a stunning rainbow-themed dashboard, it transforms employee wellbeing from an afterthought into an experience people actually want to use.
