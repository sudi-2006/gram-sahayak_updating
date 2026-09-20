import streamlit as st
import math
from datetime import datetime
import json
import urllib.request
import urllib.parse
import zipfile
import io
import os
import pandas as pd
import streamlit.components.v1 as components

# ============================================================
# GRAM SAHAYAK
# Business & Financial Guidance for Rural Micro-Entrepreneurs
# ============================================================

st.set_page_config(
    page_title="Gram Sahayak",
    page_icon="🌾",
    layout="wide"
)

# -----------------------------
# CUSTOM CSS
# -----------------------------
st.markdown("""
<style>
    .main {
        background: #f7faf7;
    }

    .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
        max-width: 1400px;
    }

    .hero {
        padding: 1.5rem 1.8rem;
        border-radius: 20px;
        background: linear-gradient(135deg, #eef8ef, #f8fbf5);
        border: 1px solid #dbeadd;
        margin-bottom: 1.5rem;
    }

    .hero h1 {
        font-size: 3rem;
        margin-bottom: 0.3rem;
    }

    .hero p {
        font-size: 1.15rem;
        color: #4b5563;
    }

    .card {
        background: white;
        border: 1px solid #e5e7eb;
        border-radius: 16px;
        padding: 1.15rem;
        margin-bottom: 1rem;
        box-shadow: 0 3px 12px rgba(0,0,0,0.04);
    }

    .recommendation {
        background: linear-gradient(135deg, #f0f8f1, #ffffff);
        border-left: 6px solid #2e7d32;
        border-radius: 14px;
        padding: 1.2rem;
        margin-bottom: 1rem;
    }

    .score {
        font-size: 1.8rem;
        font-weight: 700;
    }

    .small-note {
        color: #6b7280;
        font-size: 0.88rem;
    }

    .tag {
        display: inline-block;
        padding: 0.3rem 0.65rem;
        border-radius: 999px;
        background: #eef6ff;
        margin-right: 0.35rem;
        font-size: 0.82rem;
    }

    .footer {
        text-align: center;
        color: #6b7280;
        padding: 2rem 0 0.5rem;
    }


    /* ===== NATIONAL-FINALE VISUAL SYSTEM ===== */
    @keyframes gradientShift {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    @keyframes floatUp {
        0%, 100% { transform: translateY(0) rotate(0deg); }
        50% { transform: translateY(-10px) rotate(2deg); }
    }
    @keyframes pulseGlow {
        0%, 100% { box-shadow: 0 0 0 0 rgba(46,125,50,.10); }
        50% { box-shadow: 0 0 0 10px rgba(46,125,50,0); }
    }
    @keyframes reveal {
        from { opacity: 0; transform: translateY(12px); }
        to { opacity: 1; transform: translateY(0); }
    }
    @keyframes shine {
        from { transform: translateX(-120%); }
        to { transform: translateX(120%); }
    }
    .animated-hero {
        position: relative;
        overflow: hidden;
        padding: 2.2rem 2.3rem;
        border-radius: 28px;
        color: #17351b;
        background: linear-gradient(120deg, #e9f7e8, #f7fbef, #e6f4f2, #eef8ef);
        background-size: 300% 300%;
        animation: gradientShift 12s ease infinite, reveal .7s ease both;
        border: 1px solid #d6e8d5;
        box-shadow: 0 16px 45px rgba(35,83,39,.10);
        margin-bottom: 1.25rem;
    }
    .animated-hero h1 { font-size: 3.25rem; margin: 0; line-height: 1.05; }
    .animated-hero p { font-size: 1.12rem; color: #52645a; margin: .6rem 0 0; max-width: 820px; }
    .hero-badge { display:inline-block; margin-top:1rem; padding:.45rem .8rem; border-radius:999px; background:rgba(255,255,255,.72); border:1px solid rgba(60,110,64,.12); font-size:.85rem; font-weight:700; }
    .hero-orb { position:absolute; border-radius:50%; filter:blur(1px); opacity:.55; animation:floatUp 5s ease-in-out infinite; pointer-events:none; }
    .hero-orb.one { width:95px; height:95px; right:8%; top:15%; background:rgba(102,187,106,.20); }
    .hero-orb.two { width:55px; height:55px; right:23%; bottom:12%; background:rgba(255,193,7,.18); animation-delay:1.2s; }
    .hero-orb.three { width:35px; height:35px; right:4%; bottom:25%; background:rgba(33,150,243,.16); animation-delay:2s; }
    .page-banner { display:flex; align-items:center; gap:1rem; padding:1rem 1.2rem; border-radius:18px; background:linear-gradient(90deg,#ffffff,#f3faf2); border:1px solid #e1ebe0; margin-bottom:1.1rem; animation:reveal .55s ease both; }
    .page-icon { width:48px; height:48px; display:flex; align-items:center; justify-content:center; border-radius:15px; background:#eaf5ea; font-size:1.55rem; animation:pulseGlow 3s infinite; }
    .page-banner h2 { margin:0; font-size:1.55rem; }
    .page-banner p { margin:.15rem 0 0; color:#65736a; font-size:.92rem; }
    .feature-card { position:relative; overflow:hidden; min-height:145px; background:rgba(255,255,255,.92); border:1px solid #e2eae1; border-radius:20px; padding:1.2rem; box-shadow:0 8px 24px rgba(0,0,0,.045); animation:reveal .65s ease both; }
    .feature-card::after { content:""; position:absolute; width:55%; height:140%; top:-20%; left:-90%; background:linear-gradient(90deg,transparent,rgba(255,255,255,.65),transparent); transform:skewX(-18deg); animation:shine 7s ease-in-out infinite; }
    .feature-icon { font-size:2rem; animation:floatUp 4s ease-in-out infinite; }
    .metric-strip { padding:.7rem .9rem; border-radius:16px; background:#ffffff; border:1px solid #e6ece5; box-shadow:0 4px 16px rgba(0,0,0,.035); }
    .status-pill { display:inline-block; padding:.35rem .7rem; border-radius:999px; font-size:.8rem; font-weight:700; background:#edf7ed; color:#2e6b34; }
    .weather-card { border-radius:22px; padding:1.3rem; background:linear-gradient(135deg,#eef8ff,#f7fbff); border:1px solid #dceaf5; box-shadow:0 10px 28px rgba(40,90,130,.07); animation:reveal .6s ease both; }
    .weather-temp { font-size:3rem; font-weight:800; line-height:1; }
    .map-card { border-radius:22px; padding:1rem; background:linear-gradient(135deg,#f8fbf7,#ffffff); border:1px solid #e2e9e1; box-shadow:0 10px 30px rgba(0,0,0,.045); }
    .voice-card { border-radius:24px; padding:1.5rem; background:linear-gradient(135deg,#f7f0ff,#fff9ff); border:1px solid #eadcf5; animation:reveal .6s ease both; }
    .voice-mic { width:90px; height:90px; border-radius:50%; margin:auto; display:flex; align-items:center; justify-content:center; font-size:2.4rem; background:#ffffff; box-shadow:0 0 0 0 rgba(124,77,255,.16); animation:pulseGlow 2.4s infinite; }
    .timeline-step { border-left:3px solid #8ab98e; padding:0 0 1rem 1rem; margin-left:.4rem; animation:reveal .5s ease both; }
    .risk-chip { display:inline-block; padding:.35rem .65rem; border-radius:999px; margin:.2rem; background:#fff4e8; border:1px solid #f3dfc8; font-size:.8rem; }
    div[data-testid="stMetric"] { animation:reveal .55s ease both; }
    .stButton > button { border-radius:12px; transition:transform .18s ease, box-shadow .18s ease; }
    .stButton > button:hover { transform:translateY(-2px); box-shadow:0 7px 18px rgba(0,0,0,.08); }
    .card, .recommendation, .metric-strip, .map-card { animation:reveal .55s ease both; transition:transform .22s ease, box-shadow .22s ease, border-color .22s ease; }
    .card:hover, .recommendation:hover, .metric-strip:hover, .map-card:hover { transform:translateY(-4px); box-shadow:0 14px 32px rgba(35,83,39,.10); border-color:#cfe1cf; }
    div[data-baseweb="tab-list"] { gap:.35rem; }
    button[data-baseweb="tab"] { border-radius:12px 12px 0 0; transition:all .2s ease; }
    button[data-baseweb="tab"]:hover { transform:translateY(-2px); }
    div[data-testid="stDataFrame"] { animation:reveal .65s ease both; border-radius:16px; overflow:hidden; }
    div[data-testid="stSelectbox"], div[data-testid="stMultiSelect"], div[data-testid="stNumberInput"], div[data-testid="stTextInput"] { animation:reveal .5s ease both; }
    @media (prefers-reduced-motion: reduce) {
        *, *::before, *::after { animation-duration:0.01ms !important; animation-iteration-count:1 !important; scroll-behavior:auto !important; transition-duration:0.01ms !important; }
    }
    [data-testid="stSidebar"] { border-right:1px solid #e3ebe2; }
    [data-testid="stSidebar"] .stRadio > div { gap:.25rem; }

</style>
""", unsafe_allow_html=True)


# -----------------------------
# TRANSLATIONS
# -----------------------------
TEXT = {
    "English": {
        "language": "Language", "location": "Market Location", "navigate": "Navigate",
        "home": "Home", "market": "Market Prices", "schemes": "Government Schemes",
        "finance": "Financial Assistant", "business": "Business Recommendation", "action_plan": "Smart Action Plan",
        "welcome": "Welcome to Gram Sahayak",
        "subtitle": "Business & Financial Guidance for Rural Micro-Entrepreneurs",
        "home_desc": "A simple digital assistant designed to help rural micro-entrepreneurs explore local business opportunities, understand sample market conditions, estimate finances and discover relevant government schemes.",
        "crops": "Crops Covered", "locations": "Locations", "schemes_count": "Schemes",
        "business_models": "Business Models", "selected_market": "Selected Market",
        "demo_market": "Current demonstration market", "market_disclaimer": "Market prices shown in this prototype are sample data and are not live mandi/API prices.",
        "what_can": "What you can do", "explore": "Explore Markets", "explore_desc": "Compare sample prices across a wider set of crops and locations.",
        "plan": "Plan Finances", "plan_desc": "Estimate profit, revenue, costs and loan EMI before making a decision.",
        "find": "Find a Business", "find_desc": "Get a structured business shortlist based on capital, resources, interests and location.",
        "how": "How Gram Sahayak Works", "how_desc": "Your inputs → local context → rule-based business matching → financial planning → relevant scheme suggestions → practical next steps.",
        "market_title": "Market Prices", "market_desc": "Sample market information for **{location}**. Use it for demonstration and planning only; verify current local mandi prices before making financial decisions.",
        "filter": "Filter by crop category", "all": "All", "board": "Crop Market Board", "showing": "Showing {count} crops for the selected demonstration market: {location}",
        "selected_crop": "Selected Crop", "choose_crop": "Choose a crop", "crop": "Crop", "sample_price": "Sample Price", "trend": "Trend",
        "increasing": "Increasing", "stable": "Stable", "decreasing": "Decreasing",
        "market_note": "Important: locally grown crop profiles and location-adjusted prices are controlled demonstration data, not live market feeds.",
        "scheme_title": "Government Schemes", "scheme_desc": "Explore schemes that may be relevant to rural entrepreneurs, farmers, vendors, food processors and artisans.",
        "search": "Search schemes", "placeholder": "Example: food, loan, farmer, artisan", "best_for": "Best for",
        "key": "Key information", "why": "Why it may help", "source": "Official source",
        "scheme_warning": "Scheme eligibility, loan approval, subsidy availability and applicable conditions depend on the official guidelines and the applicant's circumstances. Verify details through the relevant Government of India/state portal or bank before applying.",
        "finance_title": "Financial Assistant", "profit_tab": "📊 Profit Calculator", "emi_tab": "🏦 Loan EMI Calculator",
        "profit_est": "Profit Estimator", "quantity": "Quantity", "purchase": "Purchase cost per unit", "selling": "Selling price per unit",
        "other": "Other costs", "total_cost": "Total Cost", "revenue": "Revenue", "profit": "Estimated Profit",
        "positive": "This example produces a positive estimated profit.", "break_even": "This example is approximately at break-even.",
        "loss": "This example produces an estimated loss. Review price and costs.",
        "loan": "Loan amount", "rate": "Annual interest rate (%)", "period": "Loan period (years)", "monthly": "Monthly EMI",
        "total_payment": "Total Payment", "interest": "Total Interest", "loan_note": "Actual loan terms, interest rates, fees and approval depend on the lender.",
        "business_title": "Business Recommendation", "business_desc": "Tell Gram Sahayak about your situation. The prototype will score business models using capital, multiple available resources, interest, location-based water context, experience and location.",
        "capital": "💰 Available capital (₹)", "resource": "🧰 Available resources (select all that apply)",
        "local_crops_title": "Locally grown crops in this location",
        "local_crops_note": "These are prototype local-crop profiles. Prices are location-adjusted sample prices, not live mandi prices.",
        "show_all_crops": "Show all demonstration crops",
        "eligibility": "Eligibility",
        "documents": "Documents commonly required", "interest_input": "❤️ Main business interest",
        "water": "💧 Location-based water availability", "experience": "🎯 Your experience", "good": "Good", "limited": "Limited",
        "not_applicable": "Not applicable", "not_sure": "Not sure", "beginner": "Beginner", "some": "Some experience", "experienced": "Experienced",
        "location_note": "📍 Recommendation will be adjusted for the selected market: **{location}**",
        "generate": "🔍 Generate Business Recommendations", "three": "Here are the three strongest prototype matches for your inputs.",
        "match": "Match", "investment": "Indicative investment", "model": "Business model", "why_match": "Why this matches",
        "risk": "Key risk", "steps": "Suggested first steps", "relevant": "Potentially relevant schemes",
        "next_action": "📌 Suggested next action", "below": "Your current capital is below the typical starting range for **{business}**. Consider a smaller pilot, savings, eligible financing or a lower-capital business model.",
        "next": "A practical next step is to prepare a simple cost sheet for **{business}** and compare it with expected local demand before investing.",
        "limit": "Prototype limitation: this is a rule-based recommendation engine using demonstration business profiles. It is not a live AI model and does not guarantee profitability.",
        "footer": "🌾 Gram Sahayak • Prototype for rural micro-entrepreneur business guidance",
        "footer_note": "Demo market data • Rule-based recommendations • Verify official scheme information before decisions",
    },
    "Hindi": {
        "language": "भाषा", "location": "बाज़ार स्थान", "navigate": "नेविगेट करें",
        "home": "होम", "market": "बाज़ार भाव", "schemes": "सरकारी योजनाएँ", "finance": "वित्तीय सहायक", "business": "व्यवसाय सुझाव", "action_plan": "स्मार्ट कार्य योजना",
        "welcome": "ग्राम सहायक में आपका स्वागत है", "subtitle": "ग्रामीण सूक्ष्म उद्यमियों के लिए व्यवसाय और वित्तीय मार्गदर्शन",
        "home_desc": "ग्रामीण सूक्ष्म उद्यमियों को स्थानीय व्यवसाय के अवसर समझने, नमूना बाज़ार स्थिति देखने, वित्त का अनुमान लगाने और उपयोगी सरकारी योजनाएँ खोजने में मदद करने वाला डिजिटल सहायक।",
        "crops": "शामिल फसलें", "locations": "स्थान", "schemes_count": "योजनाएँ", "business_models": "व्यवसाय मॉडल",
        "selected_market": "चयनित बाज़ार", "demo_market": "वर्तमान प्रदर्शन बाज़ार", "market_disclaimer": "इस प्रोटोटाइप में दिखाए गए बाज़ार भाव नमूना डेटा हैं और लाइव मंडी/API भाव नहीं हैं।",
        "what_can": "आप क्या कर सकते हैं", "explore": "बाज़ार देखें", "explore_desc": "अलग-अलग फसलों और स्थानों के नमूना भावों की तुलना करें।",
        "plan": "वित्त की योजना बनाएं", "plan_desc": "निर्णय लेने से पहले लाभ, राजस्व, लागत और ऋण EMI का अनुमान लगाएं।",
        "find": "व्यवसाय खोजें", "find_desc": "पूंजी, संसाधन, रुचि और स्थान के आधार पर व्यवसायों की सूची पाएं।",
        "how": "ग्राम सहायक कैसे काम करता है", "how_desc": "आपकी जानकारी → स्थानीय संदर्भ → नियम-आधारित व्यवसाय मिलान → वित्तीय योजना → संबंधित योजना सुझाव → अगले व्यावहारिक कदम।",
        "market_title": "बाज़ार भाव", "market_desc": "**{location}** के लिए नमूना बाज़ार जानकारी। इसका उपयोग केवल प्रदर्शन और योजना के लिए करें; वित्तीय निर्णय से पहले वर्तमान स्थानीय मंडी भाव की पुष्टि करें।",
        "filter": "फसल श्रेणी से फ़िल्टर करें", "all": "सभी", "board": "फसल बाज़ार बोर्ड", "showing": "चयनित प्रदर्शन बाज़ार {location} के लिए {count} फसलें दिखाई जा रही हैं",
        "selected_crop": "चयनित फसल", "choose_crop": "फसल चुनें", "crop": "फसल", "sample_price": "नमूना भाव", "trend": "रुझान",
        "increasing": "बढ़ रहा है", "stable": "स्थिर", "decreasing": "घट रहा है", "market_note": "महत्वपूर्ण: स्थानीय फसल प्रोफाइल और स्थान-समायोजित भाव नियंत्रित प्रदर्शन डेटा हैं, लाइव बाज़ार डेटा नहीं।",
        "scheme_title": "सरकारी योजनाएँ", "scheme_desc": "ग्रामीण उद्यमियों, किसानों, विक्रेताओं, खाद्य प्रसंस्करण इकाइयों और कारीगरों के लिए उपयोगी योजनाएँ देखें।",
        "search": "योजनाएँ खोजें", "placeholder": "उदाहरण: भोजन, ऋण, किसान, कारीगर", "best_for": "किसके लिए", "key": "मुख्य जानकारी", "why": "यह कैसे मदद कर सकती है", "source": "आधिकारिक स्रोत",
        "scheme_warning": "योजना की पात्रता, ऋण स्वीकृति, सब्सिडी और शर्तें आधिकारिक दिशानिर्देश तथा आवेदक की स्थिति पर निर्भर करती हैं। आवेदन से पहले संबंधित सरकारी पोर्टल या बैंक से जानकारी सत्यापित करें।",
        "finance_title": "वित्तीय सहायक", "profit_tab": "📊 लाभ कैलकुलेटर", "emi_tab": "🏦 ऋण EMI कैलकुलेटर",
        "profit_est": "लाभ अनुमान", "quantity": "मात्रा", "purchase": "प्रति इकाई खरीद लागत", "selling": "प्रति इकाई बिक्री मूल्य", "other": "अन्य लागत",
        "total_cost": "कुल लागत", "revenue": "राजस्व", "profit": "अनुमानित लाभ", "positive": "इस उदाहरण में अनुमानित लाभ सकारात्मक है।",
        "break_even": "यह उदाहरण लगभग ब्रेक-ईवन पर है।", "loss": "इस उदाहरण में अनुमानित नुकसान है। मूल्य और लागत की समीक्षा करें।",
        "loan": "ऋण राशि", "rate": "वार्षिक ब्याज दर (%)", "period": "ऋण अवधि (वर्ष)", "monthly": "मासिक EMI", "total_payment": "कुल भुगतान", "interest": "कुल ब्याज",
        "loan_note": "वास्तविक ऋण शर्तें, ब्याज दर, शुल्क और स्वीकृति ऋणदाता पर निर्भर करते हैं।",
        "business_title": "व्यवसाय सुझाव", "business_desc": "अपनी स्थिति के बारे में ग्राम सहायक को बताएं। प्रोटोटाइप पूंजी, संसाधन, रुचि, पानी, अनुभव और स्थान के आधार पर व्यवसायों का स्कोर करेगा।",
        "capital": "💰 उपलब्ध पूंजी (₹)", "resource": "🧰 उपलब्ध संसाधन (सभी लागू विकल्प चुनें)",
        "local_crops_title": "इस स्थान में स्थानीय रूप से उगाई जाने वाली फसलें",
        "local_crops_note": "ये प्रोटोटाइप स्थानीय-फसल प्रोफाइल हैं। भाव स्थान-समायोजित नमूना भाव हैं, लाइव मंडी भाव नहीं।",
        "show_all_crops": "सभी प्रदर्शन फसलें दिखाएँ",
        "eligibility": "पात्रता",
        "documents": "आमतौर पर आवश्यक दस्तावेज़", "interest_input": "❤️ मुख्य व्यवसाय रुचि", "water": "💧 स्थान-आधारित पानी की उपलब्धता",
        "experience": "🎯 आपका अनुभव", "good": "अच्छी", "limited": "सीमित", "not_applicable": "लागू नहीं", "not_sure": "पता नहीं",
        "beginner": "शुरुआती", "some": "कुछ अनुभव", "experienced": "अनुभवी", "location_note": "📍 चुने गए बाज़ार के अनुसार सुझाव बदला जाएगा: **{location}**",
        "generate": "🔍 व्यवसाय सुझाव बनाएं", "three": "आपकी जानकारी के आधार पर तीन सबसे मजबूत प्रोटोटाइप सुझाव ये हैं।", "match": "मिलान",
        "investment": "अनुमानित निवेश", "model": "व्यवसाय मॉडल", "why_match": "यह क्यों उपयुक्त है", "risk": "मुख्य जोखिम", "steps": "सुझाए गए शुरुआती कदम", "relevant": "संभावित संबंधित योजनाएँ",
        "next_action": "📌 सुझाया गया अगला कदम", "below": "आपकी वर्तमान पूंजी **{business}** के सामान्य शुरुआती निवेश से कम है। छोटे पायलट, बचत, पात्र वित्तपोषण या कम पूंजी वाले व्यवसाय पर विचार करें।",
        "next": "अगला व्यावहारिक कदम **{business}** की सरल लागत सूची बनाना और निवेश से पहले अपेक्षित स्थानीय मांग से उसकी तुलना करना है।",
        "limit": "प्रोटोटाइप सीमा: यह प्रदर्शन व्यवसाय प्रोफाइल पर आधारित नियम-आधारित सिफारिश इंजन है। यह लाइव AI मॉडल नहीं है और लाभ की गारंटी नहीं देता।",
        "footer": "🌾 ग्राम सहायक • ग्रामीण सूक्ष्म उद्यम व्यवसाय मार्गदर्शन प्रोटोटाइप", "footer_note": "डेमो बाज़ार डेटा • नियम-आधारित सुझाव • निर्णय से पहले आधिकारिक योजना जानकारी सत्यापित करें",
    },
    "Kannada": {
        "language": "ಭಾಷೆ", "location": "ಮಾರುಕಟ್ಟೆ ಸ್ಥಳ", "navigate": "ನ್ಯಾವಿಗೇಟ್ ಮಾಡಿ",
        "home": "ಮುಖಪುಟ", "market": "ಮಾರುಕಟ್ಟೆ ಬೆಲೆಗಳು", "schemes": "ಸರ್ಕಾರಿ ಯೋಜನೆಗಳು", "finance": "ಹಣಕಾಸು ಸಹಾಯಕ", "business": "ವ್ಯವಹಾರ ಶಿಫಾರಸು", "action_plan": "ಸ್ಮಾರ್ಟ್ ಕಾರ್ಯ ಯೋಜನೆ",
        "welcome": "ಗ್ರಾಮ ಸಹಾಯಕಕ್ಕೆ ಸ್ವಾಗತ", "subtitle": "ಗ್ರಾಮೀಣ ಸಣ್ಣ ಉದ್ಯಮಿಗಳಿಗೆ ವ್ಯವಹಾರ ಮತ್ತು ಹಣಕಾಸು ಮಾರ್ಗದರ್ಶನ",
        "home_desc": "ಗ್ರಾಮೀಣ ಸಣ್ಣ ಉದ್ಯಮಿಗಳಿಗೆ ಸ್ಥಳೀಯ ವ್ಯವಹಾರ ಅವಕಾಶಗಳನ್ನು ತಿಳಿದುಕೊಳ್ಳಲು, ಮಾದರಿ ಮಾರುಕಟ್ಟೆ ಪರಿಸ್ಥಿತಿಯನ್ನು ಅರ್ಥಮಾಡಿಕೊಳ್ಳಲು, ಹಣಕಾಸು ಅಂದಾಜು ಮಾಡಲು ಮತ್ತು ಸಂಬಂಧಿತ ಸರ್ಕಾರಿ ಯೋಜನೆಗಳನ್ನು ಹುಡುಕಲು ಸಹಾಯ ಮಾಡುವ ಡಿಜಿಟಲ್ ಸಹಾಯಕ.",
        "crops": "ಒಳಗೊಂಡ ಬೆಳೆಗಳು", "locations": "ಸ್ಥಳಗಳು", "schemes_count": "ಯೋಜನೆಗಳು", "business_models": "ವ್ಯವಹಾರ ಮಾದರಿಗಳು",
        "selected_market": "ಆಯ್ಕೆ ಮಾಡಿದ ಮಾರುಕಟ್ಟೆ", "demo_market": "ಪ್ರಸ್ತುತ ಪ್ರದರ್ಶನ ಮಾರುಕಟ್ಟೆ", "market_disclaimer": "ಈ ಪ್ರೋಟೋಟೈಪ್‌ನಲ್ಲಿರುವ ಮಾರುಕಟ್ಟೆ ಬೆಲೆಗಳು ಮಾದರಿ ಡೇಟಾ ಮಾತ್ರ; ಇವು ಲೈವ್ ಮಂಡಿ/API ಬೆಲೆಗಳಲ್ಲ.",
        "what_can": "ನೀವು ಏನು ಮಾಡಬಹುದು", "explore": "ಮಾರುಕಟ್ಟೆಗಳನ್ನು ನೋಡಿ", "explore_desc": "ವಿವಿಧ ಬೆಳೆಗಳು ಮತ್ತು ಸ್ಥಳಗಳ ಮಾದರಿ ಬೆಲೆಗಳನ್ನು ಹೋಲಿಸಿ.",
        "plan": "ಹಣಕಾಸು ಯೋಜಿಸಿ", "plan_desc": "ನಿರ್ಧಾರಕ್ಕೂ ಮೊದಲು ಲಾಭ, ಆದಾಯ, ವೆಚ್ಚ ಮತ್ತು ಸಾಲದ EMI ಅಂದಾಜಿಸಿ.",
        "find": "ವ್ಯವಹಾರ ಹುಡುಕಿ", "find_desc": "ಬಂಡವಾಳ, ಸಂಪನ್ಮೂಲ, ಆಸಕ್ತಿ ಮತ್ತು ಸ್ಥಳದ ಆಧಾರದ ಮೇಲೆ ವ್ಯವಹಾರಗಳ ಪಟ್ಟಿಯನ್ನು ಪಡೆಯಿರಿ.",
        "how": "ಗ್ರಾಮ ಸಹಾಯಕ ಹೇಗೆ ಕೆಲಸ ಮಾಡುತ್ತದೆ", "how_desc": "ನಿಮ್ಮ ಮಾಹಿತಿ → ಸ್ಥಳೀಯ ಸಂದರ್ಭ → ನಿಯಮಾಧಾರಿತ ವ್ಯವಹಾರ ಹೊಂದಾಣಿಕೆ → ಹಣಕಾಸು ಯೋಜನೆ → ಸಂಬಂಧಿತ ಯೋಜನೆ ಸಲಹೆಗಳು → ಮುಂದಿನ ಪ್ರಾಯೋಗಿಕ ಹಂತಗಳು.",
        "market_title": "ಮಾರುಕಟ್ಟೆ ಬೆಲೆಗಳು", "market_desc": "**{location}** ಗಾಗಿ ಮಾದರಿ ಮಾರುಕಟ್ಟೆ ಮಾಹಿತಿ. ಇದನ್ನು ಪ್ರದರ್ಶನ ಮತ್ತು ಯೋಜನೆಗಾಗಿ ಮಾತ್ರ ಬಳಸಿ; ಹಣಕಾಸು ನಿರ್ಧಾರಕ್ಕೂ ಮೊದಲು ಪ್ರಸ್ತುತ ಸ್ಥಳೀಯ ಮಂಡಿ ಬೆಲೆಗಳನ್ನು ಪರಿಶೀಲಿಸಿ.",
        "filter": "ಬೆಳೆ ವರ್ಗದ ಮೂಲಕ ಫಿಲ್ಟರ್ ಮಾಡಿ", "all": "ಎಲ್ಲಾ", "board": "ಬೆಳೆ ಮಾರುಕಟ್ಟೆ ಫಲಕ", "showing": "ಆಯ್ಕೆ ಮಾಡಿದ ಪ್ರದರ್ಶನ ಮಾರುಕಟ್ಟೆ {location} ಗಾಗಿ {count} ಬೆಳೆಗಳನ್ನು ತೋರಿಸಲಾಗುತ್ತಿದೆ",
        "selected_crop": "ಆಯ್ಕೆ ಮಾಡಿದ ಬೆಳೆ", "choose_crop": "ಬೆಳೆ ಆಯ್ಕೆ ಮಾಡಿ", "crop": "ಬೆಳೆ", "sample_price": "ಮಾದರಿ ಬೆಲೆ", "trend": "ಪ್ರವೃತ್ತಿ",
        "increasing": "ಏರಿಕೆ", "stable": "ಸ್ಥಿರ", "decreasing": "ಇಳಿಕೆ", "market_note": "ಮುಖ್ಯ: ಸ್ಥಳೀಯ ಬೆಳೆ ಪ್ರೊಫೈಲ್‌ಗಳು ಮತ್ತು ಸ್ಥಳ-ಹೊಂದಾಣಿಕೆಯ ಬೆಲೆಗಳು ನಿಯಂತ್ರಿತ ಪ್ರದರ್ಶನ ಡೇಟಾ; ಲೈವ್ ಮಾರುಕಟ್ಟೆ ಫೀಡ್ ಅಲ್ಲ.",
        "scheme_title": "ಸರ್ಕಾರಿ ಯೋಜನೆಗಳು", "scheme_desc": "ಗ್ರಾಮೀಣ ಉದ್ಯಮಿಗಳು, ರೈತರು, ಮಾರಾಟಗಾರರು, ಆಹಾರ ಸಂಸ್ಕರಣಾ ಘಟಕಗಳು ಮತ್ತು ಕರಕುಶಲಗಾರರಿಗೆ ಸಂಬಂಧಿಸಿದ ಯೋಜನೆಗಳನ್ನು ನೋಡಿ.",
        "search": "ಯೋಜನೆಗಳನ್ನು ಹುಡುಕಿ", "placeholder": "ಉದಾಹರಣೆ: ಆಹಾರ, ಸಾಲ, ರೈತ, ಕರಕುಶಲಗಾರ", "best_for": "ಯಾರಿಗೆ ಸೂಕ್ತ", "key": "ಮುಖ್ಯ ಮಾಹಿತಿ", "why": "ಇದು ಹೇಗೆ ಸಹಾಯ ಮಾಡಬಹುದು", "source": "ಅಧಿಕೃತ ಮೂಲ",
        "scheme_warning": "ಯೋಜನೆಯ ಅರ್ಹತೆ, ಸಾಲ ಅನುಮೋದನೆ, ಸಬ್ಸಿಡಿ ಮತ್ತು ಷರತ್ತುಗಳು ಅಧಿಕೃತ ಮಾರ್ಗಸೂಚಿಗಳು ಮತ್ತು ಅರ್ಜಿದಾರರ ಪರಿಸ್ಥಿತಿಯ ಮೇಲೆ ಅವಲಂಬಿತವಾಗಿವೆ. ಅರ್ಜಿ ಸಲ್ಲಿಸುವ ಮೊದಲು ಸಂಬಂಧಿತ ಸರ್ಕಾರಿ ಪೋರ್ಟಲ್ ಅಥವಾ ಬ್ಯಾಂಕ್ ಮೂಲಕ ವಿವರಗಳನ್ನು ಪರಿಶೀಲಿಸಿ.",
        "finance_title": "ಹಣಕಾಸು ಸಹಾಯಕ", "profit_tab": "📊 ಲಾಭ ಕ್ಯಾಲ್ಕುಲೇಟರ್", "emi_tab": "🏦 ಸಾಲ EMI ಕ್ಯಾಲ್ಕುಲೇಟರ್",
        "profit_est": "ಲಾಭ ಅಂದಾಜು", "quantity": "ಪ್ರಮಾಣ", "purchase": "ಪ್ರತಿ ಘಟಕ ಖರೀದಿ ವೆಚ್ಚ", "selling": "ಪ್ರತಿ ಘಟಕ ಮಾರಾಟ ಬೆಲೆ", "other": "ಇತರೆ ವೆಚ್ಚಗಳು",
        "total_cost": "ಒಟ್ಟು ವೆಚ್ಚ", "revenue": "ಆದಾಯ", "profit": "ಅಂದಾಜು ಲಾಭ", "positive": "ಈ ಉದಾಹರಣೆಯಲ್ಲಿ ಅಂದಾಜು ಲಾಭ ಧನಾತ್ಮಕವಾಗಿದೆ.",
        "break_even": "ಈ ಉದಾಹರಣೆ ಸುಮಾರು ಬ್ರೇಕ್-ಈವನ್ ಸ್ಥಿತಿಯಲ್ಲಿದೆ.", "loss": "ಈ ಉದಾಹರಣೆಯಲ್ಲಿ ಅಂದಾಜು ನಷ್ಟವಿದೆ. ಬೆಲೆ ಮತ್ತು ವೆಚ್ಚಗಳನ್ನು ಪರಿಶೀಲಿಸಿ.",
        "loan": "ಸಾಲದ ಮೊತ್ತ", "rate": "ವಾರ್ಷಿಕ ಬಡ್ಡಿ ದರ (%)", "period": "ಸಾಲದ ಅವಧಿ (ವರ್ಷಗಳು)", "monthly": "ಮಾಸಿಕ EMI", "total_payment": "ಒಟ್ಟು ಪಾವತಿ", "interest": "ಒಟ್ಟು ಬಡ್ಡಿ",
        "loan_note": "ನಿಜವಾದ ಸಾಲದ ಷರತ್ತುಗಳು, ಬಡ್ಡಿದರ, ಶುಲ್ಕಗಳು ಮತ್ತು ಅನುಮೋದನೆ ಸಾಲದಾತರ ಮೇಲೆ ಅವಲಂಬಿತವಾಗಿವೆ.",
        "business_title": "ವ್ಯವಹಾರ ಶಿಫಾರಸು", "business_desc": "ನಿಮ್ಮ ಪರಿಸ್ಥಿತಿಯನ್ನು ಗ್ರಾಮ ಸಹಾಯಕಕ್ಕೆ ತಿಳಿಸಿ. ಪ್ರೋಟೋಟೈಪ್ ಬಂಡವಾಳ, ಸಂಪನ್ಮೂಲ, ಆಸಕ್ತಿ, ನೀರಿನ ಲಭ್ಯತೆ, ಅನುಭವ ಮತ್ತು ಸ್ಥಳದ ಆಧಾರದ ಮೇಲೆ ವ್ಯವಹಾರಗಳಿಗೆ ಅಂಕ ನೀಡುತ್ತದೆ.",
        "capital": "💰 ಲಭ್ಯವಿರುವ ಬಂಡವಾಳ (₹)", "resource": "🧰 ಲಭ್ಯವಿರುವ ಸಂಪನ್ಮೂಲಗಳು (ಅನ್ವಯಿಸುವ ಎಲ್ಲವನ್ನು ಆಯ್ಕೆ ಮಾಡಿ)",
        "local_crops_title": "ಈ ಸ್ಥಳದಲ್ಲಿ ಸ್ಥಳೀಯವಾಗಿ ಬೆಳೆಯುವ ಬೆಳೆಗಳು",
        "local_crops_note": "ಇವು ಪ್ರೋಟೋಟೈಪ್ ಸ್ಥಳೀಯ-ಬೆಳೆ ಪ್ರೊಫೈಲ್‌ಗಳು. ಬೆಲೆಗಳು ಸ್ಥಳ-ಹೊಂದಾಣಿಕೆಯ ಮಾದರಿ ಬೆಲೆಗಳು; ಲೈವ್ ಮಂಡಿ ಬೆಲೆಗಳಲ್ಲ.",
        "show_all_crops": "ಎಲ್ಲಾ ಪ್ರದರ್ಶನ ಬೆಳೆಗಳನ್ನು ತೋರಿಸಿ",
        "eligibility": "ಅರ್ಹತೆ",
        "documents": "ಸಾಮಾನ್ಯವಾಗಿ ಅಗತ್ಯವಿರುವ ದಾಖಲೆಗಳು", "interest_input": "❤️ ಮುಖ್ಯ ವ್ಯವಹಾರ ಆಸಕ್ತಿ", "water": "💧 ಸ್ಥಳ ಆಧಾರಿತ ನೀರಿನ ಲಭ್ಯತೆ",
        "experience": "🎯 ನಿಮ್ಮ ಅನುಭವ", "good": "ಉತ್ತಮ", "limited": "ಸೀಮಿತ", "not_applicable": "ಅನ್ವಯಿಸುವುದಿಲ್ಲ", "not_sure": "ಖಚಿತವಿಲ್ಲ",
        "beginner": "ಆರಂಭಿಕ", "some": "ಸ್ವಲ್ಪ ಅನುಭವ", "experienced": "ಅನುಭವ ಹೊಂದಿರುವವರು", "location_note": "📍 ಆಯ್ಕೆ ಮಾಡಿದ ಮಾರುಕಟ್ಟೆಗೆ ಅನುಗುಣವಾಗಿ ಶಿಫಾರಸು ಬದಲಾಗುತ್ತದೆ: **{location}**",
        "generate": "🔍 ವ್ಯವಹಾರ ಶಿಫಾರಸುಗಳನ್ನು ರಚಿಸಿ", "three": "ನಿಮ್ಮ ಮಾಹಿತಿಗೆ ಹೊಂದುವ ಮೂರು ಉತ್ತಮ ಪ್ರೋಟೋಟೈಪ್ ಶಿಫಾರಸುಗಳು ಇಲ್ಲಿವೆ.", "match": "ಹೊಂದಾಣಿಕೆ",
        "investment": "ಅಂದಾಜು ಹೂಡಿಕೆ", "model": "ವ್ಯವಹಾರ ಮಾದರಿ", "why_match": "ಇದು ಏಕೆ ಹೊಂದಿಕೊಳ್ಳುತ್ತದೆ", "risk": "ಮುಖ್ಯ ಅಪಾಯ", "steps": "ಸೂಚಿಸಿದ ಆರಂಭಿಕ ಹಂತಗಳು", "relevant": "ಸಂಬಂಧಿತವಾಗಿರಬಹುದಾದ ಯೋಜನೆಗಳು",
        "next_action": "📌 ಸೂಚಿಸಿದ ಮುಂದಿನ ಕ್ರಮ", "below": "ನಿಮ್ಮ ಪ್ರಸ್ತುತ ಬಂಡವಾಳವು **{business}** ಗೆ ಸಾಮಾನ್ಯ ಆರಂಭಿಕ ಹೂಡಿಕೆಗಿಂತ ಕಡಿಮೆಯಾಗಿದೆ. ಸಣ್ಣ ಪೈಲಟ್, ಉಳಿತಾಯ, ಅರ್ಹ ಹಣಕಾಸು ಅಥವಾ ಕಡಿಮೆ ಬಂಡವಾಳದ ವ್ಯವಹಾರವನ್ನು ಪರಿಗಣಿಸಿ.",
        "next": "ಮುಂದಿನ ಪ್ರಾಯೋಗಿಕ ಹಂತವೆಂದರೆ **{business}** ಗಾಗಿ ಸರಳ ವೆಚ್ಚಪಟ್ಟಿ ತಯಾರಿಸಿ, ಹೂಡಿಕೆ ಮಾಡುವ ಮೊದಲು ನಿರೀಕ್ಷಿತ ಸ್ಥಳೀಯ ಬೇಡಿಕೆಯೊಂದಿಗೆ ಹೋಲಿಸುವುದು.",
        "limit": "ಪ್ರೋಟೋಟೈಪ್ ಮಿತಿ: ಇದು ಪ್ರದರ್ಶನ ವ್ಯವಹಾರ ಪ್ರೊಫೈಲ್‌ಗಳನ್ನು ಬಳಸುವ ನಿಯಮಾಧಾರಿತ ಶಿಫಾರಸು ಎಂಜಿನ್. ಇದು ಲೈವ್ AI ಮಾದರಿ ಅಲ್ಲ ಮತ್ತು ಲಾಭದ ಖಾತರಿ ನೀಡುವುದಿಲ್ಲ.",
        "footer": "🌾 ಗ್ರಾಮ ಸಹಾಯಕ • ಗ್ರಾಮೀಣ ಸಣ್ಣ ಉದ್ಯಮ ವ್ಯವಹಾರ ಮಾರ್ಗದರ್ಶನ ಪ್ರೋಟೋಟೈಪ್", "footer_note": "ಡೆಮೊ ಮಾರುಕಟ್ಟೆ ಡೇಟಾ • ನಿಯಮಾಧಾರಿತ ಶಿಫಾರಸುಗಳು • ನಿರ್ಧಾರಕ್ಕೂ ಮೊದಲು ಅಧಿಕೃತ ಯೋಜನೆ ಮಾಹಿತಿಯನ್ನು ಪರಿಶೀಲಿಸಿ",
    }
}

# Display translations for the crop/category/trend content.
DATA_TR = {
    "Hindi": {
        "Increasing":"बढ़ रहा है","Stable":"स्थिर","Decreasing":"घट रहा है",
        "Vegetable":"सब्ज़ी","Leafy":"पत्तेदार","Cereal":"अनाज","Oilseed":"तिलहन","Pulse":"दलहन","Commercial":"व्यावसायिक","Spice":"मसाला","Horticulture":"बागवानी","Fruit":"फल",
        "Tomato":"टमाटर","Onion":"प्याज़","Potato":"आलू","Carrot":"गाजर","Beans":"बीन्स","Brinjal":"बैंगन","Cabbage":"पत्तागोभी","Cauliflower":"फूलगोभी","Capsicum":"शिमला मिर्च","Green Chilli":"हरी मिर्च","Lady Finger":"भिंडी","Bottle Gourd":"लौकी","Bitter Gourd":"करेला","Cucumber":"खीरा","Pumpkin":"कद्दू","Drumstick":"सहजन","Peas":"मटर","Beetroot":"चुकंदर","Radish":"मूली","Spinach":"पालक","Coriander":"धनिया","Fenugreek Leaves":"मेथी","Maize":"मक्का","Wheat":"गेहूँ","Rice":"चावल","Ragi":"रागी","Jowar":"ज्वार","Bajra":"बाजरा","Groundnut":"मूंगफली","Sunflower":"सूरजमुखी","Soybean":"सोयाबीन","Tur":"तूर दाल","Green Gram":"मूंग","Black Gram":"उड़द","Bengal Gram":"चना","Cotton":"कपास","Sugarcane":"गन्ना","Turmeric":"हल्दी","Chilli":"मिर्च","Ginger":"अदरक","Garlic":"लहसुन","Coconut":"नारियल","Banana":"केला","Mango":"आम","Papaya":"पपीता","Guava":"अमरूद"
    },
    "Kannada": {
        "Increasing":"ಏರಿಕೆ","Stable":"ಸ್ಥಿರ","Decreasing":"ಇಳಿಕೆ",
        "Vegetable":"ತರಕಾರಿ","Leafy":"ಸೊಪ್ಪು","Cereal":"ಧಾನ್ಯ","Oilseed":"ಎಣ್ಣೆಬೀಜ","Pulse":"ಬೇಳೆ","Commercial":"ವಾಣಿಜ್ಯ","Spice":"ಮಸಾಲೆ","Horticulture":"ತೋಟಗಾರಿಕೆ","Fruit":"ಹಣ್ಣು",
        "Tomato":"ಟೊಮ್ಯಾಟೊ","Onion":"ಈರುಳ್ಳಿ","Potato":"ಆಲೂಗಡ್ಡೆ","Carrot":"ಕ್ಯಾರೆಟ್","Beans":"ಬೀನ್ಸ್","Brinjal":"ಬದನೆಕಾಯಿ","Cabbage":"ಎಲೆಕೋಸು","Cauliflower":"ಹೂಕೋಸು","Capsicum":"ಕ್ಯಾಪ್ಸಿಕಂ","Green Chilli":"ಹಸಿರು ಮೆಣಸಿನಕಾಯಿ","Lady Finger":"ಬೆಂಡೆಕಾಯಿ","Bottle Gourd":"ಸೋರೆಕಾಯಿ","Bitter Gourd":"ಹಾಗಲಕಾಯಿ","Cucumber":"ಸೌತೆಕಾಯಿ","Pumpkin":"ಕುಂಬಳಕಾಯಿ","Drumstick":"ನುಗ್ಗೆಕಾಯಿ","Peas":"ಬಟಾಣಿ","Beetroot":"ಬೀಟ್ರೂಟ್","Radish":"ಮೂಲಂಗಿ","Spinach":"ಪಾಲಕ್ ಸೊಪ್ಪು","Coriander":"ಕೊತ್ತಂಬರಿ ಸೊಪ್ಪು","Fenugreek Leaves":"ಮೆಂತ್ಯ ಸೊಪ್ಪು","Maize":"ಮೆಕ್ಕೆಜೋಳ","Wheat":"ಗೋಧಿ","Rice":"ಅಕ್ಕಿ","Ragi":"ರಾಗಿ","Jowar":"ಜೋಳ","Bajra":"ಸಜ್ಜೆ","Groundnut":"ಕಡಲೆಕಾಯಿ","Sunflower":"ಸೂರ್ಯಕಾಂತಿ","Soybean":"ಸೋಯಾಬೀನ್","Tur":"ತೊಗರಿ","Green Gram":"ಹೆಸರುಕಾಳು","Black Gram":"ಉದ್ದು","Bengal Gram":"ಕಡಲೆ","Cotton":"ಹತ್ತಿ","Sugarcane":"ಕಬ್ಬು","Turmeric":"ಅರಿಶಿನ","Chilli":"ಮೆಣಸಿನಕಾಯಿ","Ginger":"ಶುಂಠಿ","Garlic":"ಬೆಳ್ಳುಳ್ಳಿ","Coconut":"ತೆಂಗಿನಕಾಯಿ","Banana":"ಬಾಳೆಹಣ್ಣು","Mango":"ಮಾವು","Papaya":"ಪಪ್ಪಾಯಿ","Guava":"ಸೀಬೆಹಣ್ಣು"
    }
}

def tr_data(value):
    return DATA_TR.get(language, {}).get(value, value)

def tr(key, **kwargs):
    value = TEXT[language].get(key, TEXT["English"].get(key, key))
    return value.format(**kwargs) if kwargs else value


# ============================================================
# GLOBAL UI TRANSLATIONS
# These cover labels/content outside the original TEXT table so
# changing the sidebar language updates the whole application.
# ============================================================
UI_TR = {
    "English": {
        "location_name": {}, "season": {"Kharif":"Kharif","Rabi":"Rabi","Summer":"Summer"},
        "water": {"Good":"Good","Medium":"Medium","Limited":"Limited"},
        "local_crop": "Local crop", "selected_resources": "Selected resources",
        "select_resource": "Please select at least one resource for a more accurate recommendation.",
        "water_for": "Water availability for {location}",
        "animal_advisory": "Animal & Breed Advisory", "animal": "Animal", "breed": "Location-based breed suggestion",
        "why_suggestion": "Why this suggestion", "care": "Basic care suggestions",
        "animal_note": "Breed suggestions are regional prototype guidance. Confirm breed availability, suitability, vaccination and treatment plans with the local veterinary/Animal Husbandry department.",
        "farming_title":"Seasonal & Location-Based Farming Advisor",
        "farming_desc":"The prototype recommends crops using the selected Karnataka location, season and a rule-based suitability score.",
        "farming_season":"Farming season", "farming_location":"Location", "farming_recommend":"Recommended crops for this location and season",
        "farming_note":"Prototype suitability score only — not a guaranteed yield or profit prediction. Confirm soil, irrigation, weather and local agriculture advice before planting.",
        "why_here":"Why here", "main_risk":"Main risk", "harvest":"Harvest window", "water_need":"Water need", "base_potential":"Base potential",
        "no_crop":"No strong prototype crop match was found for this location and season. Try another season and verify with local agricultural guidance.",
        "farming_example":"Example: the prototype can rank a water-demanding commercial crop such as sugarcane higher in locations with a suitable water profile, while recommending drought-tolerant crops such as tur, jowar or bengal gram for drier northern Karnataka locations. This is a rule-based demonstration, not a claim that one crop can never grow in another location.",
        "local_profile":"included in the prototype's local-crop profile for {location}",
        "show_all_reason":"shown because you selected Show all demonstration crops.",
        "no_category":"No crop is available for this category in the current prototype profile.",
        "business_risk_outlook":"Business Success & Risk Outlook", "planning_est":"These are prototype planning estimates, not historical success rates or guaranteed predictions.",
        "success_potential":"Estimated success potential", "first_results":"Likely first positive results", "higher_risk":"Higher-risk period", "stabilisation":"Stabilisation period",
        "success_context":"Actual results depend on demand, costs, weather, water, management, competition and market prices.",
        "official_verify":"Verify details through the relevant Government of India/state portal or bank before applying.",
        "compare_harvest":"Harvest", "compare_location":"Location fit", "compare_suitability":"Suitability",
        "included":"Included", "not_in_profile":"Not in profile", "required":"Required", "not_central":"Not central",
        "prototype":"Prototype", "demo_data":"Demonstration data",
    },
    "Hindi": {
        "location_name": {"Hubballi":"हुब्बल्ली","Dharwad":"धारवाड़","Belagavi":"बेलगावी","Bengaluru":"बेंगलुरु","Mysuru":"मैसूरु","Shivamogga":"शिवमोग्गा","Davanagere":"दावणगेरे","Gadag":"गदग","Haveri":"हावेरी","Vijayapura":"विजयपुर","Kalaburagi":"कलबुर्गी","Raichur":"रायचूर","Tumakuru":"तुमकुरु","Chitradurga":"चित्रदुर्ग"},
        "season": {"Kharif":"खरीफ","Rabi":"रबी","Summer":"गर्मी"}, "water": {"Good":"अच्छी","Medium":"मध्यम","Limited":"सीमित"},
        "local_crop":"स्थानीय फसल", "selected_resources":"चयनित संसाधन", "select_resource":"अधिक सटीक सुझाव के लिए कम से कम एक संसाधन चुनें।",
        "water_for":"{location} के लिए पानी की उपलब्धता", "animal_advisory":"पशु और नस्ल सलाह", "animal":"पशु", "breed":"स्थान-आधारित नस्ल सुझाव", "why_suggestion":"यह सुझाव क्यों", "care":"बुनियादी देखभाल सुझाव",
        "animal_note":"नस्ल सुझाव क्षेत्रीय प्रोटोटाइप मार्गदर्शन हैं। नस्ल की उपलब्धता, उपयुक्तता, टीकाकरण और उपचार योजना की पुष्टि स्थानीय पशु चिकित्सा/पशुपालन विभाग से करें।",
        "farming_title":"मौसम और स्थान आधारित खेती सलाहकार", "farming_desc":"प्रोटोटाइप चयनित कर्नाटक स्थान, मौसम और नियम-आधारित उपयुक्तता स्कोर के आधार पर फसल सुझाव देता है।", "farming_season":"खेती का मौसम", "farming_location":"स्थान", "farming_recommend":"इस स्थान और मौसम के लिए सुझाई गई फसलें",
        "farming_note":"यह केवल प्रोटोटाइप उपयुक्तता स्कोर है — उपज या लाभ की गारंटी नहीं। बुवाई से पहले मिट्टी, सिंचाई, मौसम और स्थानीय कृषि सलाह की पुष्टि करें।", "why_here":"यहाँ क्यों", "main_risk":"मुख्य जोखिम", "harvest":"कटाई अवधि", "water_need":"पानी की जरूरत", "base_potential":"आधार क्षमता",
        "no_crop":"इस स्थान और मौसम के लिए कोई मजबूत प्रोटोटाइप फसल मिलान नहीं मिला। दूसरा मौसम आज़माएं और स्थानीय कृषि सलाह से पुष्टि करें।",
        "farming_example":"उदाहरण: प्रोटोटाइप उपयुक्त पानी वाले स्थानों में गन्ने जैसी अधिक पानी वाली व्यावसायिक फसल को ऊपर रख सकता है, जबकि उत्तरी कर्नाटक के अपेक्षाकृत शुष्क स्थानों में तूर, ज्वार या चना जैसी कम पानी वाली फसलों को सुझा सकता है। यह नियम-आधारित प्रदर्शन है; इसका अर्थ यह नहीं कि कोई फसल दूसरे स्थान पर कभी नहीं उग सकती।",
        "local_profile":"{location} के प्रोटोटाइप स्थानीय-फसल प्रोफाइल में शामिल है", "show_all_reason":"क्योंकि आपने सभी प्रदर्शन फसलें दिखाने का विकल्प चुना है।", "no_category":"वर्तमान प्रोटोटाइप प्रोफाइल में इस श्रेणी के लिए कोई फसल उपलब्ध नहीं है।",
        "business_risk_outlook":"व्यवसाय सफलता और जोखिम दृष्टिकोण", "planning_est":"ये प्रोटोटाइप योजना अनुमान हैं, ऐतिहासिक सफलता दर या गारंटीकृत भविष्यवाणी नहीं।", "success_potential":"अनुमानित सफलता क्षमता", "first_results":"पहले सकारात्मक परिणाम की संभावित अवधि", "higher_risk":"अधिक जोखिम अवधि", "stabilisation":"स्थिरता अवधि", "success_context":"वास्तविक परिणाम मांग, लागत, मौसम, पानी, प्रबंधन, प्रतिस्पर्धा और बाजार भाव पर निर्भर करते हैं।",
        "compare_harvest":"कटाई", "compare_location":"स्थान मिलान", "compare_suitability":"उपयुक्तता", "included":"प्रोफाइल में शामिल", "not_in_profile":"प्रोफाइल में नहीं", "required":"आवश्यक", "not_central":"मुख्य नहीं", "prototype":"प्रोटोटाइप", "demo_data":"प्रदर्शन डेटा"
    },
    "Kannada": {
        "location_name": {"Hubballi":"ಹುಬ್ಬಳ್ಳಿ","Dharwad":"ಧಾರವಾಡ","Belagavi":"ಬೆಳಗಾವಿ","Bengaluru":"ಬೆಂಗಳೂರು","Mysuru":"ಮೈಸೂರು","Shivamogga":"ಶಿವಮೊಗ್ಗ","Davanagere":"ದಾವಣಗೆರೆ","Gadag":"ಗದಗ","Haveri":"ಹಾವೇರಿ","Vijayapura":"ವಿಜಯಪುರ","Kalaburagi":"ಕಲಬುರಗಿ","Raichur":"ರಾಯಚೂರು","Tumakuru":"ತುಮಕೂರು","Chitradurga":"ಚಿತ್ರದುರ್ಗ"},
        "season": {"Kharif":"ಖರೀಫ್","Rabi":"ರಬಿ","Summer":"ಬೇಸಿಗೆ"}, "water": {"Good":"ಉತ್ತಮ","Medium":"ಮಧ್ಯಮ","Limited":"ಸೀಮಿತ"},
        "local_crop":"ಸ್ಥಳೀಯ ಬೆಳೆ", "selected_resources":"ಆಯ್ಕೆ ಮಾಡಿದ ಸಂಪನ್ಮೂಲಗಳು", "select_resource":"ಹೆಚ್ಚು ನಿಖರವಾದ ಸಲಹೆಗಾಗಿ ಕನಿಷ್ಠ ಒಂದು ಸಂಪನ್ಮೂಲವನ್ನು ಆಯ್ಕೆಮಾಡಿ.",
        "water_for":"{location} ನೀರಿನ ಲಭ್ಯತೆ", "animal_advisory":"ಪ್ರಾಣಿ ಮತ್ತು ತಳಿ ಸಲಹೆ", "animal":"ಪ್ರಾಣಿ", "breed":"ಸ್ಥಳ ಆಧಾರಿತ ತಳಿ ಸಲಹೆ", "why_suggestion":"ಈ ಸಲಹೆ ಏಕೆ", "care":"ಮೂಲಭೂತ ಆರೈಕೆ ಸಲಹೆಗಳು",
        "animal_note":"ತಳಿ ಸಲಹೆಗಳು ಪ್ರಾದೇಶಿಕ ಪ್ರೋಟೋಟೈಪ್ ಮಾರ್ಗದರ್ಶನ ಮಾತ್ರ. ತಳಿ ಲಭ್ಯತೆ, ಸೂಕ್ತತೆ, ಲಸಿಕೆ ಮತ್ತು ಚಿಕಿತ್ಸಾ ಯೋಜನೆಯನ್ನು ಸ್ಥಳೀಯ ಪಶುವೈದ್ಯ/ಪಶುಸಂಗೋಪನಾ ಇಲಾಖೆಯಿಂದ ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ.",
        "farming_title":"ಋತು ಮತ್ತು ಸ್ಥಳ ಆಧಾರಿತ ಕೃಷಿ ಸಲಹೆಗಾರ", "farming_desc":"ಪ್ರೋಟೋಟೈಪ್ ಆಯ್ಕೆ ಮಾಡಿದ ಕರ್ನಾಟಕ ಸ್ಥಳ, ಋತು ಮತ್ತು ನಿಯಮಾಧಾರಿತ ಸೂಕ್ತತೆ ಅಂಕದ ಆಧಾರದ ಮೇಲೆ ಬೆಳೆ ಸಲಹೆ ನೀಡುತ್ತದೆ.", "farming_season":"ಕೃಷಿ ಋತು", "farming_location":"ಸ್ಥಳ", "farming_recommend":"ಈ ಸ್ಥಳ ಮತ್ತು ಋತುವಿಗೆ ಶಿಫಾರಸು ಮಾಡಿದ ಬೆಳೆಗಳು",
        "farming_note":"ಇದು ಕೇವಲ ಪ್ರೋಟೋಟೈಪ್ ಸೂಕ್ತತೆ ಅಂಕ — ಇಳುವರಿ ಅಥವಾ ಲಾಭದ ಖಾತರಿ ಅಲ್ಲ. ಬಿತ್ತನೆಗೆ ಮೊದಲು ಮಣ್ಣು, ನೀರಾವರಿ, ಹವಾಮಾನ ಮತ್ತು ಸ್ಥಳೀಯ ಕೃಷಿ ಸಲಹೆಯನ್ನು ಪರಿಶೀಲಿಸಿ.", "why_here":"ಇಲ್ಲಿ ಏಕೆ", "main_risk":"ಮುಖ್ಯ ಅಪಾಯ", "harvest":"ಕೊಯ್ಲು ಅವಧಿ", "water_need":"ನೀರಿನ ಅಗತ್ಯ", "base_potential":"ಮೂಲ ಸಾಮರ್ಥ್ಯ",
        "no_crop":"ಈ ಸ್ಥಳ ಮತ್ತು ಋತುವಿಗೆ ಬಲವಾದ ಪ್ರೋಟೋಟೈಪ್ ಬೆಳೆ ಹೊಂದಾಣಿಕೆ ಕಂಡುಬಂದಿಲ್ಲ. ಬೇರೆ ಋತುವನ್ನು ಪ್ರಯತ್ನಿಸಿ ಮತ್ತು ಸ್ಥಳೀಯ ಕೃಷಿ ಮಾರ್ಗದರ್ಶನವನ್ನು ಪರಿಶೀಲಿಸಿ.",
        "farming_example":"ಉದಾಹರಣೆ: ಸೂಕ್ತ ನೀರಿನ ಪರಿಸ್ಥಿತಿ ಇರುವ ಸ್ಥಳಗಳಲ್ಲಿ ಕಬ್ಬಿನಂತಹ ಹೆಚ್ಚು ನೀರು ಬೇಕಾದ ವಾಣಿಜ್ಯ ಬೆಳೆಯನ್ನು ಪ್ರೋಟೋಟೈಪ್ ಮೇಲಕ್ಕೆ ತರಬಹುದು; ಉತ್ತರ ಕರ್ನಾಟಕದ ಒಣ ಪ್ರದೇಶಗಳಲ್ಲಿ ತೊಗರಿ, ಜೋಳ ಅಥವಾ ಕಡಲೆಯಂತಹ ಕಡಿಮೆ ನೀರಿನ ಬೆಳೆಗಳನ್ನು ಸೂಚಿಸಬಹುದು. ಇದು ನಿಯಮಾಧಾರಿತ ಪ್ರದರ್ಶನ ಮಾತ್ರ; ಬೇರೆ ಸ್ಥಳದಲ್ಲಿ ಬೆಳೆ ಎಂದಿಗೂ ಬೆಳೆಯುವುದಿಲ್ಲ ಎಂಬ ಅರ್ಥವಲ್ಲ.",
        "local_profile":"{location} ಪ್ರೋಟೋಟೈಪ್ ಸ್ಥಳೀಯ-ಬೆಳೆ ಪ್ರೊಫೈಲ್‌ನಲ್ಲಿ ಸೇರಿದೆ", "show_all_reason":"ನೀವು ಎಲ್ಲಾ ಪ್ರದರ್ಶನ ಬೆಳೆಗಳನ್ನು ತೋರಿಸುವ ಆಯ್ಕೆಯನ್ನು ಆರಿಸಿದ್ದರಿಂದ ತೋರಿಸಲಾಗಿದೆ.", "no_category":"ಪ್ರಸ್ತುತ ಪ್ರೋಟೋಟೈಪ್ ಪ್ರೊಫೈಲ್‌ನಲ್ಲಿ ಈ ವರ್ಗಕ್ಕೆ ಯಾವುದೇ ಬೆಳೆ ಲಭ್ಯವಿಲ್ಲ.",
        "business_risk_outlook":"ವ್ಯವಹಾರ ಯಶಸ್ಸು ಮತ್ತು ಅಪಾಯದ ದೃಷ್ಟಿಕೋನ", "planning_est":"ಇವು ಪ್ರೋಟೋಟೈಪ್ ಯೋಜನಾ ಅಂದಾಜುಗಳು; ಐತಿಹಾಸಿಕ ಯಶಸ್ಸಿನ ದರ ಅಥವಾ ಖಾತರಿ ಭವಿಷ್ಯವಾಣಿ ಅಲ್ಲ.", "success_potential":"ಅಂದಾಜು ಯಶಸ್ಸಿನ ಸಾಮರ್ಥ್ಯ", "first_results":"ಮೊದಲ ಸಕಾರಾತ್ಮಕ ಫಲಿತಾಂಶದ ಸಾಧ್ಯ ಅವಧಿ", "higher_risk":"ಹೆಚ್ಚಿನ ಅಪಾಯದ ಅವಧಿ", "stabilisation":"ಸ್ಥಿರೀಕರಣ ಅವಧಿ", "success_context":"ನಿಜವಾದ ಫಲಿತಾಂಶಗಳು ಬೇಡಿಕೆ, ವೆಚ್ಚ, ಹವಾಮಾನ, ನೀರು, ನಿರ್ವಹಣೆ, ಸ್ಪರ್ಧೆ ಮತ್ತು ಮಾರುಕಟ್ಟೆ ಬೆಲೆಗಳ ಮೇಲೆ ಅವಲಂಬಿತವಾಗಿವೆ.",
        "compare_harvest":"ಕೊಯ್ಲು", "compare_location":"ಸ್ಥಳ ಹೊಂದಾಣಿಕೆ", "compare_suitability":"ಸೂಕ್ತತೆ", "included":"ಪ್ರೊಫೈಲ್‌ನಲ್ಲಿ ಸೇರಿದೆ", "not_in_profile":"ಪ್ರೊಫೈಲ್‌ನಲ್ಲಿ ಇಲ್ಲ", "required":"ಅಗತ್ಯ", "not_central":"ಮುಖ್ಯವಲ್ಲ", "prototype":"ಪ್ರೋಟೋಟೈಪ್", "demo_data":"ಪ್ರದರ್ಶನ ಡೇಟಾ"
    }
}

def ui(key, **kwargs):
    value = UI_TR.get(language, UI_TR["English"]).get(key, UI_TR["English"].get(key, key))
    if isinstance(value, dict):
        return value
    return value.format(**kwargs) if kwargs else value

def ui_data(value, kind="location_name"):
    table = UI_TR.get(language, UI_TR["English"]).get(kind, {})
    return table.get(value, value)


CROP_TEXT_TR = {
    "Hindi": {
        "Price fluctuations, pests and excess rain":"कीमतों में उतार-चढ़ाव, कीट और अधिक बारिश", "Price volatility and storage losses":"कीमतों में अस्थिरता और भंडारण में नुकसान", "Disease, heat and price variation":"रोग, गर्मी और कीमतों में बदलाव", "Rainfall variation and pest pressure":"वर्षा में बदलाव और कीटों का दबाव", "Moisture stress and market price variation":"नमी की कमी और बाजार कीमतों में बदलाव", "Dry spells and pest pressure":"सूखे की अवधि और कीटों का दबाव", "Moisture stress and pod pests":"नमी की कमी और फली के कीट", "Long crop duration and rainfall variability":"लंबी फसल अवधि और वर्षा में बदलाव", "Dry spells and fungal disease":"सूखे की अवधि और फफूंद रोग", "Water stress and price variation":"पानी की कमी और कीमतों में बदलाव", "Excess rain, pests and market price":"अधिक बारिश, कीट और बाजार भाव", "Pests, rainfall variability and price risk":"कीट, वर्षा में बदलाव और कीमत का जोखिम", "High water requirement and long capital lock-in":"अधिक पानी की जरूरत और लंबे समय तक पूंजी का बंधना", "Rhizome disease and price variation":"कंद रोग और कीमतों में बदलाव", "Pests, disease and price volatility":"कीट, रोग और कीमतों में अस्थिरता", "Water requirement and rainfall timing":"पानी की जरूरत और वर्षा का समय", "Wind, water requirement and disease":"तेज हवा, पानी की जरूरत और रोग"
    },
    "Kannada": {
        "Price fluctuations, pests and excess rain":"ಬೆಲೆ ಏರಿಳಿತ, ಕೀಟಗಳು ಮತ್ತು ಅಧಿಕ ಮಳೆ", "Price volatility and storage losses":"ಬೆಲೆ ಅಸ್ಥಿರತೆ ಮತ್ತು ಸಂಗ್ರಹಣಾ ನಷ್ಟ", "Disease, heat and price variation":"ರೋಗ, ಬಿಸಿಲು ಮತ್ತು ಬೆಲೆ ಬದಲಾವಣೆ", "Rainfall variation and pest pressure":"ಮಳೆಯ ಬದಲಾವಣೆ ಮತ್ತು ಕೀಟಗಳ ಒತ್ತಡ", "Moisture stress and market price variation":"ತೇವಾಂಶ ಕೊರತೆ ಮತ್ತು ಮಾರುಕಟ್ಟೆ ಬೆಲೆ ಬದಲಾವಣೆ", "Dry spells and pest pressure":"ಒಣ ಅವಧಿ ಮತ್ತು ಕೀಟಗಳ ಒತ್ತಡ", "Moisture stress and pod pests":"ತೇವಾಂಶ ಕೊರತೆ ಮತ್ತು ಕಾಯಿಕೀಟಗಳು", "Long crop duration and rainfall variability":"ದೀರ್ಘ ಬೆಳೆ ಅವಧಿ ಮತ್ತು ಮಳೆಯ ಬದಲಾವಣೆ", "Dry spells and fungal disease":"ಒಣ ಅವಧಿ ಮತ್ತು ಶಿಲೀಂಧ್ರ ರೋಗ", "Water stress and price variation":"ನೀರಿನ ಕೊರತೆ ಮತ್ತು ಬೆಲೆ ಬದಲಾವಣೆ", "Excess rain, pests and market price":"ಅಧಿಕ ಮಳೆ, ಕೀಟಗಳು ಮತ್ತು ಮಾರುಕಟ್ಟೆ ಬೆಲೆ", "Pests, rainfall variability and price risk":"ಕೀಟಗಳು, ಮಳೆಯ ಬದಲಾವಣೆ ಮತ್ತು ಬೆಲೆ ಅಪಾಯ", "High water requirement and long capital lock-in":"ಹೆಚ್ಚಿನ ನೀರಿನ ಅಗತ್ಯ ಮತ್ತು ದೀರ್ಘಕಾಲ ಬಂಡವಾಳ ಸಿಲುಕುವುದು", "Rhizome disease and price variation":"ಗೆಡ್ಡೆ ರೋಗ ಮತ್ತು ಬೆಲೆ ಬದಲಾವಣೆ", "Pests, disease and price volatility":"ಕೀಟಗಳು, ರೋಗ ಮತ್ತು ಬೆಲೆ ಅಸ್ಥಿರತೆ", "Water requirement and rainfall timing":"ನೀರಿನ ಅಗತ್ಯ ಮತ್ತು ಮಳೆಯ ಸಮಯ", "Wind, water requirement and disease":"ಗಾಳಿ, ನೀರಿನ ಅಗತ್ಯ ಮತ್ತು ರೋಗ"
    }
}

def crop_text(value):
    return CROP_TEXT_TR.get(language, {}).get(value, value)


# -----------------------------
# PRIORITY 2: TRANSLATIONS + VISUAL HELPERS
# -----------------------------
P2_TR = {
    "English": {
        "hub":"Rural Intelligence Hub", "hub_desc":"Weather, opportunity mapping, voice accessibility and livestock planning in one visual dashboard.",
        "weather":"Weather & Farming Advisory", "weather_desc":"Live weather from Open-Meteo when internet access is available, combined with Gram Sahayak's prototype crop context.",
        "map":"Karnataka Opportunity Map", "map_desc":"A visual prototype map showing location-level opportunity signals from the app's local crop, business and water profiles.",
        "voice":"Voice Assistant", "voice_desc":"Browser-based voice interaction for rural accessibility. Allow microphone access in Chrome or Edge.",
        "livestock":"Livestock Business Planner", "livestock_desc":"Estimate herd/flock size, setup cost, recurring cost and simple monthly economics before scaling.",
        "refresh":"Refresh weather", "forecast":"7-day forecast", "current":"Current conditions", "feels":"Feels like", "humidity":"Humidity", "wind":"Wind", "rain":"Rain chance", "source":"Weather source", "live":"Live API data", "fallback":"Fallback/demo data",
        "weather_note":"Weather is fetched dynamically from Open-Meteo. If the network/API is unavailable, the app shows a clearly labelled fallback message rather than inventing live weather.",
        "today_advice":"Today's advisory", "crop_signal":"Crop signal", "water_signal":"Water context", "map_selected":"Selected location", "opportunity":"Opportunity signals", "opportunity_index":"Prototype opportunity index", "local_crops":"Local crop profiles", "businesses":"Business profiles", "water":"Water availability", "map_note":"This map is a prototype decision-support visualization, not an official district ranking or investment recommendation.",
        "voice_start":"Start listening", "voice_stop":"Stop listening", "voice_hint":"Try: market prices, weather, crops, schemes, or water.", "voice_browser":"Voice recognition depends on browser support and microphone permission. Your speech is processed by the browser's speech-recognition service.", "voice_reply":"Assistant response", "voice_not_supported":"Speech recognition is not supported by this browser. Try the latest Chrome or Edge.",
        "animal_business":"Animal business", "animal_type":"Animal type", "breed":"Suggested breed/profile", "herd":"Starting animals/birds", "setup":"Initial setup cost per animal/bird (₹)", "monthly":"Monthly operating cost per animal/bird (₹)", "income":"Monthly income per animal/bird (₹)", "months":"Planning period (months)", "setup_total":"Estimated setup cost", "monthly_total":"Estimated monthly operating cost", "monthly_income":"Estimated monthly income", "monthly_margin":"Estimated monthly operating margin", "break_even":"Simple payback estimate", "planner_note":"Illustrative planning model only. Actual feed, animal purchase, medicine, mortality, milk/egg/meat yield and selling price vary by breed, season, location and management.",
        "animal_care":"Core care checklist", "market_link":"Market + location context", "next":"Suggested next step", "map_open":"Open map below", "no_weather":"Weather data unavailable right now.", "risk":"Risk flag", "low":"Low", "medium":"Medium", "high":"High", "economics":"Livestock economics", "illustrative_warning":"The current illustrative assumptions do not cover monthly operating cost. Review inputs before scaling.", "date":"Date", "weather_col":"Weather", "min_temp":"Min °C", "max_temp":"Max °C", "rain_percent":"Rain %", "rain_mm":"Rain mm", "other_profiles":"other profile(s)", "validate":"Open Market Prices + Smart Action Plan to validate the opportunity with current inputs.", "voice_title":"Gram Sahayak Voice", "listening":"🎧 Listening...", "microphone_error":"Microphone error", "browser_note":"Voice recognition depends on browser support and microphone permission."
    },
    "Hindi": {
        "hub":"ग्रामीण इंटेलिजेंस हब", "hub_desc":"मौसम, अवसर मानचित्र, वॉइस सुविधा और पशुपालन योजना एक ही डैशबोर्ड में।", "weather":"मौसम और खेती सलाह", "weather_desc":"इंटरनेट उपलब्ध होने पर Open-Meteo से लाइव मौसम और ग्राम सहायक के प्रोटोटाइप फसल संदर्भ का संयोजन।", "map":"कर्नाटक अवसर मानचित्र", "map_desc":"स्थानीय फसल, व्यवसाय और पानी प्रोफाइल से बने स्थान-स्तरीय अवसर संकेतों का दृश्य प्रोटोटाइप।", "voice":"वॉइस सहायक", "voice_desc":"ग्रामीण पहुंच के लिए ब्राउज़र आधारित वॉइस सुविधा। Chrome या Edge में माइक्रोफोन की अनुमति दें।", "livestock":"पशुपालन व्यवसाय योजनाकार", "livestock_desc":"बढ़ाने से पहले पशु/पक्षी संख्या, सेटअप लागत, मासिक लागत और सरल आय-व्यय का अनुमान लगाएं।", "refresh":"मौसम रिफ्रेश करें", "forecast":"7-दिन का पूर्वानुमान", "current":"वर्तमान स्थिति", "feels":"महसूस तापमान", "humidity":"नमी", "wind":"हवा", "rain":"बारिश की संभावना", "source":"मौसम स्रोत", "live":"लाइव API डेटा", "fallback":"फॉलबैक/डेमो डेटा", "weather_note":"मौसम Open-Meteo से गतिशील रूप से लिया जाता है। नेटवर्क/API उपलब्ध न होने पर स्पष्ट रूप से फॉलबैक संदेश दिखाया जाता है।", "today_advice":"आज की सलाह", "crop_signal":"फसल संकेत", "water_signal":"पानी संदर्भ", "map_selected":"चयनित स्थान", "opportunity":"अवसर संकेत", "opportunity_index":"प्रोटोटाइप अवसर सूचकांक", "local_crops":"स्थानीय फसल प्रोफाइल", "businesses":"व्यवसाय प्रोफाइल", "water":"पानी उपलब्धता", "map_note":"यह मानचित्र प्रोटोटाइप निर्णय-सहायता दृश्य है; यह आधिकारिक जिला रैंकिंग या निवेश सलाह नहीं है।", "voice_start":"सुनना शुरू करें", "voice_stop":"सुनना बंद करें", "voice_hint":"कहें: बाज़ार भाव, मौसम, फसल, योजनाएँ या पानी।", "voice_browser":"वॉइस सुविधा ब्राउज़र सपोर्ट और माइक्रोफोन अनुमति पर निर्भर है।", "voice_reply":"सहायक का उत्तर", "voice_not_supported":"इस ब्राउज़र में स्पीच रिकग्निशन समर्थित नहीं है। नवीनतम Chrome या Edge आज़माएं।", "animal_business":"पशु व्यवसाय", "animal_type":"पशु प्रकार", "breed":"सुझाई गई नस्ल/प्रोफाइल", "herd":"शुरुआती पशु/पक्षी", "setup":"प्रति पशु/पक्षी शुरुआती लागत (₹)", "monthly":"प्रति पशु/पक्षी मासिक लागत (₹)", "income":"प्रति पशु/पक्षी मासिक आय (₹)", "months":"योजना अवधि (महीने)", "setup_total":"अनुमानित सेटअप लागत", "monthly_total":"अनुमानित मासिक संचालन लागत", "monthly_income":"अनुमानित मासिक आय", "monthly_margin":"अनुमानित मासिक परिचालन मार्जिन", "break_even":"सरल भुगतान-अवधि अनुमान", "planner_note":"यह केवल उदाहरणात्मक योजना मॉडल है। चारा, पशु खरीद, दवा, मृत्यु दर, दूध/अंडे/मांस उत्पादन और बिक्री मूल्य बदल सकते हैं।", "animal_care":"मुख्य देखभाल सूची", "market_link":"बाज़ार + स्थान संदर्भ", "next":"अगला व्यावहारिक कदम", "map_open":"नीचे मानचित्र देखें", "no_weather":"अभी मौसम डेटा उपलब्ध नहीं है।", "risk":"जोखिम संकेत", "low":"कम", "medium":"मध्यम", "high":"उच्च", "economics":"पशुपालन आर्थिक अनुमान", "illustrative_warning":"वर्तमान उदाहरणात्मक मान्यताएँ मासिक संचालन लागत को कवर नहीं करतीं। बढ़ाने से पहले इनपुट की समीक्षा करें।", "date":"तारीख", "weather_col":"मौसम", "min_temp":"न्यूनतम °C", "max_temp":"अधिकतम °C", "rain_percent":"बारिश %", "rain_mm":"बारिश मिमी", "other_profiles":"अन्य प्रोफाइल", "validate":"वर्तमान इनपुट के साथ अवसर को सत्यापित करने के लिए बाज़ार भाव + स्मार्ट कार्य योजना खोलें।", "voice_title":"ग्राम सहायक वॉइस", "listening":"🎧 सुन रहा है...", "microphone_error":"माइक्रोफोन त्रुटि", "browser_note":"वॉइस रिकग्निशन ब्राउज़र सपोर्ट और माइक्रोफोन अनुमति पर निर्भर है।"
    },
    "Kannada": {
        "hub":"ಗ್ರಾಮೀಣ ಇಂಟೆಲಿಜೆನ್ಸ್ ಹಬ್", "hub_desc":"ಹವಾಮಾನ, ಅವಕಾಶ ನಕ್ಷೆ, ಧ್ವನಿ ಸೌಲಭ್ಯ ಮತ್ತು ಪಶುಸಂಗೋಪನಾ ಯೋಜನೆ ಒಂದೇ ಡ್ಯಾಶ್‌ಬೋರ್ಡ್‌ನಲ್ಲಿ।", "weather":"ಹವಾಮಾನ ಮತ್ತು ಕೃಷಿ ಸಲಹೆ", "weather_desc":"ಇಂಟರ್ನೆಟ್ ಲಭ್ಯವಿದ್ದಾಗ Open-Meteo ನಿಂದ ಲೈವ್ ಹವಾಮಾನವನ್ನು ಪ್ರೋಟೋಟೈಪ್ ಬೆಳೆ ಸಂದರ್ಭದೊಂದಿಗೆ ಸಂಯೋಜಿಸುತ್ತದೆ.", "map":"ಕರ್ನಾಟಕ ಅವಕಾಶ ನಕ್ಷೆ", "map_desc":"ಸ್ಥಳೀಯ ಬೆಳೆ, ವ್ಯವಹಾರ ಮತ್ತು ನೀರಿನ ಪ್ರೊಫೈಲ್‌ಗಳಿಂದ ಸ್ಥಳಮಟ್ಟದ ಅವಕಾಶ ಸೂಚನೆಗಳ ದೃಶ್ಯ ಪ್ರೋಟೋಟೈಪ್.", "voice":"ಧ್ವನಿ ಸಹಾಯಕ", "voice_desc":"ಗ್ರಾಮೀಣ ಬಳಕೆದಾರರ ಪ್ರವೇಶಕ್ಕಾಗಿ ಬ್ರೌಸರ್ ಆಧಾರಿತ ಧ್ವನಿ ಸೌಲಭ್ಯ. Chrome ಅಥವಾ Edge ನಲ್ಲಿ ಮೈಕ್ರೋಫೋನ್ ಅನುಮತಿಸಿ.", "livestock":"ಪಶುಸಂಗೋಪನಾ ವ್ಯವಹಾರ ಯೋಜಕ", "livestock_desc":"ವಿಸ್ತರಿಸುವ ಮೊದಲು ಪ್ರಾಣಿಗಳು/ಪಕ್ಷಿಗಳ ಸಂಖ್ಯೆ, ಆರಂಭಿಕ ವೆಚ್ಚ, ಮಾಸಿಕ ವೆಚ್ಚ ಮತ್ತು ಸರಳ ಆದಾಯ-ವೆಚ್ಚ ಅಂದಾಜು ಮಾಡಿ.", "refresh":"ಹವಾಮಾನ ರಿಫ್ರೆಶ್", "forecast":"7 ದಿನಗಳ ಮುನ್ಸೂಚನೆ", "current":"ಪ್ರಸ್ತುತ ಸ್ಥಿತಿ", "feels":"ಅನುಭವಿಸುವ ತಾಪಮಾನ", "humidity":"ಆರ್ದ್ರತೆ", "wind":"ಗಾಳಿ", "rain":"ಮಳೆಯ ಸಾಧ್ಯತೆ", "source":"ಹವಾಮಾನ ಮೂಲ", "live":"ಲೈವ್ API ಡೇಟಾ", "fallback":"ಫಾಲ್‌ಬ್ಯಾಕ್/ಡೆಮೊ ಡೇಟಾ", "weather_note":"ಹವಾಮಾನವನ್ನು Open-Meteo ನಿಂದ ಡೈನಾಮಿಕ್ ಆಗಿ ಪಡೆಯಲಾಗುತ್ತದೆ. ನೆಟ್‌ವರ್ಕ್/API ಲಭ್ಯವಿಲ್ಲದಿದ್ದರೆ ಸ್ಪಷ್ಟ ಫಾಲ್‌ಬ್ಯಾಕ್ ಸಂದೇಶ ತೋರಿಸಲಾಗುತ್ತದೆ.", "today_advice":"ಇಂದಿನ ಸಲಹೆ", "crop_signal":"ಬೆಳೆ ಸೂಚನೆ", "water_signal":"ನೀರಿನ ಸಂದರ್ಭ", "map_selected":"ಆಯ್ಕೆ ಮಾಡಿದ ಸ್ಥಳ", "opportunity":"ಅವಕಾಶ ಸೂಚನೆಗಳು", "opportunity_index":"ಪ್ರೋಟೋಟೈಪ್ ಅವಕಾಶ ಸೂಚ್ಯಂಕ", "local_crops":"ಸ್ಥಳೀಯ ಬೆಳೆ ಪ್ರೊಫೈಲ್‌ಗಳು", "businesses":"ವ್ಯವಹಾರ ಪ್ರೊಫೈಲ್‌ಗಳು", "water":"ನೀರಿನ ಲಭ್ಯತೆ", "map_note":"ಈ ನಕ್ಷೆ ಪ್ರೋಟೋಟೈಪ್ ನಿರ್ಧಾರ-ಸಹಾಯ ದೃಶ್ಯೀಕರಣ; ಅಧಿಕೃತ ಜಿಲ್ಲಾ ರ‍್ಯಾಂಕಿಂಗ್ ಅಥವಾ ಹೂಡಿಕೆ ಸಲಹೆ ಅಲ್ಲ.", "voice_start":"ಕೇಳಲು ಪ್ರಾರಂಭಿಸಿ", "voice_stop":"ಕೇಳುವುದನ್ನು ನಿಲ್ಲಿಸಿ", "voice_hint":"ಹೇಳಿ: ಮಾರುಕಟ್ಟೆ ಬೆಲೆ, ಹವಾಮಾನ, ಬೆಳೆ, ಯೋಜನೆಗಳು ಅಥವಾ ನೀರು.", "voice_browser":"ಧ್ವನಿ ಸೌಲಭ್ಯ ಬ್ರೌಸರ್ ಬೆಂಬಲ ಮತ್ತು ಮೈಕ್ರೋಫೋನ್ ಅನುಮತಿಗೆ ಅವಲಂಬಿತವಾಗಿದೆ.", "voice_reply":"ಸಹಾಯಕನ ಉತ್ತರ", "voice_not_supported":"ಈ ಬ್ರೌಸರ್‌ನಲ್ಲಿ ಸ್ಪೀಚ್ ರೆಕಗ್ನಿಷನ್ ಬೆಂಬಲಿತವಿಲ್ಲ. ಇತ್ತೀಚಿನ Chrome ಅಥವಾ Edge ಪ್ರಯತ್ನಿಸಿ.", "animal_business":"ಪಶು ವ್ಯವಹಾರ", "animal_type":"ಪ್ರಾಣಿ ಪ್ರಕಾರ", "breed":"ಸೂಚಿಸಿದ ತಳಿ/ಪ್ರೊಫೈಲ್", "herd":"ಆರಂಭಿಕ ಪ್ರಾಣಿಗಳು/ಪಕ್ಷಿಗಳು", "setup":"ಪ್ರತಿ ಪ್ರಾಣಿ/ಪಕ್ಷಿಗೆ ಆರಂಭಿಕ ವೆಚ್ಚ (₹)", "monthly":"ಪ್ರತಿ ಪ್ರಾಣಿ/ಪಕ್ಷಿಗೆ ಮಾಸಿಕ ವೆಚ್ಚ (₹)", "income":"ಪ್ರತಿ ಪ್ರಾಣಿ/ಪಕ್ಷಿಗೆ ಮಾಸಿಕ ಆದಾಯ (₹)", "months":"ಯೋಜನಾ ಅವಧಿ (ತಿಂಗಳು)", "setup_total":"ಅಂದಾಜು ಆರಂಭಿಕ ವೆಚ್ಚ", "monthly_total":"ಅಂದಾಜು ಮಾಸಿಕ ನಿರ್ವಹಣಾ ವೆಚ್ಚ", "monthly_income":"ಅಂದಾಜು ಮಾಸಿಕ ಆದಾಯ", "monthly_margin":"ಅಂದಾಜು ಮಾಸಿಕ ಕಾರ್ಯಾಚರಣಾ ಮಾರ್ಜಿನ್", "break_even":"ಸರಳ ಪಾವತಿ ಅವಧಿ ಅಂದಾಜು", "planner_note":"ಇದು ಉದಾಹರಣಾತ್ಮಕ ಯೋಜನಾ ಮಾದರಿ ಮಾತ್ರ. ಮೇವು, ಪ್ರಾಣಿ ಖರೀದಿ, ಔಷಧಿ, ಸಾವು, ಹಾಲು/ಮೊಟ್ಟೆ/ಮಾಂಸ ಉತ್ಪಾದನೆ ಮತ್ತು ಮಾರಾಟ ಬೆಲೆ ಬದಲಾಗಬಹುದು.", "animal_care":"ಮುಖ್ಯ ಆರೈಕೆ ಪಟ್ಟಿ", "market_link":"ಮಾರುಕಟ್ಟೆ + ಸ್ಥಳ ಸಂದರ್ಭ", "next":"ಮುಂದಿನ ಪ್ರಾಯೋಗಿಕ ಹೆಜ್ಜೆ", "map_open":"ಕೆಳಗಿನ ನಕ್ಷೆ ನೋಡಿ", "no_weather":"ಈಗ ಹವಾಮಾನ ಡೇಟಾ ಲಭ್ಯವಿಲ್ಲ.", "risk":"ಅಪಾಯ ಸೂಚನೆ", "low":"ಕಡಿಮೆ", "medium":"ಮಧ್ಯಮ", "high":"ಹೆಚ್ಚು", "economics":"ಪಶುಸಂಗೋಪನಾ ಆರ್ಥಿಕ ಅಂದಾಜು", "illustrative_warning":"ಪ್ರಸ್ತುತ ಉದಾಹರಣಾತ್ಮಕ ಅಂದಾಜುಗಳು ಮಾಸಿಕ ನಿರ್ವಹಣಾ ವೆಚ್ಚವನ್ನು ಭರಿಸುವುದಿಲ್ಲ. ವಿಸ್ತರಿಸುವ ಮೊದಲು ಇನ್‌ಪುಟ್‌ಗಳನ್ನು ಪರಿಶೀಲಿಸಿ.", "date":"ದಿನಾಂಕ", "weather_col":"ಹವಾಮಾನ", "min_temp":"ಕನಿಷ್ಠ °C", "max_temp":"ಗರಿಷ್ಠ °C", "rain_percent":"ಮಳೆ %", "rain_mm":"ಮಳೆ ಮಿಮೀ", "other_profiles":"ಇತರ ಪ್ರೊಫೈಲ್‌ಗಳು", "validate":"ಪ್ರಸ್ತುತ ಇನ್‌ಪುಟ್‌ಗಳೊಂದಿಗೆ ಅವಕಾಶವನ್ನು ಪರಿಶೀಲಿಸಲು ಮಾರುಕಟ್ಟೆ ಬೆಲೆ + ಸ್ಮಾರ್ಟ್ ಕಾರ್ಯ ಯೋಜನೆ ತೆರೆಯಿರಿ.", "voice_title":"ಗ್ರಾಮ ಸಹಾಯಕ ಧ್ವನಿ", "listening":"🎧 ಕೇಳುತ್ತಿದೆ...", "microphone_error":"ಮೈಕ್ರೋಫೋನ್ ದೋಷ", "browser_note":"ಧ್ವನಿ ಗುರುತಿಸುವಿಕೆ ಬ್ರೌಸರ್ ಬೆಂಬಲ ಮತ್ತು ಮೈಕ್ರೋಫೋನ್ ಅನುಮತಿಗೆ ಅವಲಂಬಿತವಾಗಿದೆ."
    }
}

def p2(key, **kwargs):
    value = P2_TR.get(language, P2_TR["English"]).get(key, P2_TR["English"].get(key, key))
    return value.format(**kwargs) if kwargs else value

def page_banner(icon, title, desc):
    st.markdown(f'''<div class="page-banner"><div class="page-icon">{icon}</div><div><h2>{title}</h2><p>{desc}</p></div></div>''', unsafe_allow_html=True)

def weather_code_text(code):
    names={
        0:"Clear sky",1:"Mainly clear",2:"Partly cloudy",3:"Overcast",45:"Fog",48:"Depositing rime fog",
        51:"Light drizzle",53:"Moderate drizzle",55:"Dense drizzle",61:"Slight rain",63:"Moderate rain",65:"Heavy rain",
        71:"Slight snow",73:"Moderate snow",75:"Heavy snow",80:"Rain showers",81:"Moderate rain showers",82:"Heavy rain showers",
        95:"Thunderstorm",96:"Thunderstorm with hail",99:"Thunderstorm with heavy hail"
    }
    return names.get(int(code), "Variable conditions")

def weather_icon(code):
    code=int(code)
    if code==0: return "☀️"
    if code in (1,2): return "🌤️"
    if code in (3,45,48): return "☁️"
    if code in (51,53,55,61,63,65,80,81,82): return "🌧️"
    if code in (95,96,99): return "⛈️"
    if code in (71,73,75): return "❄️"
    return "🌦️"

def weather_text(value):
    trmap={
        "Hindi":{"Clear sky":"साफ आकाश","Mainly clear":"मुख्यतः साफ","Partly cloudy":"आंशिक बादल","Overcast":"बादल छाए","Fog":"कोहरा","Slight rain":"हल्की बारिश","Moderate rain":"मध्यम बारिश","Heavy rain":"तेज़ बारिश","Rain showers":"बारिश की बौछारें","Thunderstorm":"गरज के साथ बारिश"},
        "Kannada":{"Clear sky":"ಸ್ವಚ್ಛ ಆಕಾಶ","Mainly clear":"ಮುಖ್ಯವಾಗಿ ಸ್ವಚ್ಛ","Partly cloudy":"ಭಾಗಶಃ ಮೋಡ","Overcast":"ಮೋಡ ಕವಿದ","Fog":"ಮಂಜು","Slight rain":"ಸಣ್ಣ ಮಳೆ","Moderate rain":"ಮಧ್ಯಮ ಮಳೆ","Heavy rain":"ಭಾರಿ ಮಳೆ","Rain showers":"ಮಳೆಯ ತುಂತುರು","Thunderstorm":"ಗುಡುಗು ಸಹಿತ ಮಳೆ"}
    }
    return trmap.get(language,{}).get(value,value)

LOCATION_COORDS = {
    "Hubballi":(15.3647,75.1240),"Dharwad":(15.4589,75.0078),"Belagavi":(15.8497,74.4977),"Bengaluru":(12.9716,77.5946),
    "Mysuru":(12.2958,76.6394),"Shivamogga":(13.9299,75.5681),"Davanagere":(14.4644,75.9218),"Gadag":(15.4167,75.6167),
    "Haveri":(14.7951,75.3991),"Vijayapura":(16.8302,75.7100),"Kalaburagi":(17.3297,76.8343),"Raichur":(16.2120,77.3439),
    "Tumakuru":(13.3392,77.1130),"Chitradurga":(14.2306,76.3980)
}

@st.cache_data(ttl=1800, show_spinner=False)
def fetch_weather(location_name):
    lat, lon = LOCATION_COORDS[location_name]
    params=urllib.parse.urlencode({"latitude":lat,"longitude":lon,"current":"temperature_2m,relative_humidity_2m,apparent_temperature,precipitation,weather_code,wind_speed_10m","daily":"weather_code,temperature_2m_max,temperature_2m_min,precipitation_probability_max,precipitation_sum","timezone":"auto","forecast_days":7})
    url=f"https://api.open-meteo.com/v1/forecast?{params}"
    try:
        req=urllib.request.Request(url, headers={"User-Agent":"Gram-Sahayak/1.0"})
        with urllib.request.urlopen(req, timeout=8) as response:
            data=json.loads(response.read().decode("utf-8"))
        return {"ok":True,"data":data,"source":"live"}
    except Exception as exc:
        return {"ok":False,"data":None,"source":"fallback","error":str(exc)[:120]}

def opportunity_score(location_name):
    local=len(local_crops_for_location(location_name))
    business_fit=sum(1 for b in BUSINESSES if location_name in b.get("locations",[]))
    water=location_water(location_name)
    water_score={"Good":18,"Medium":12,"Limited":7}[water]
    score=min(100, round(local*4 + business_fit*3 + water_score))
    return score, local, business_fit, water

def opportunity_advice(location_name):
    score, local, biz, water = opportunity_score(location_name)
    crop_list=local_crops_for_location(location_name)
    top_crop=tr_data(crop_list[0]) if crop_list else "—"
    if water=="Good": water_msg="Good water context supports a wider set of water-dependent activities."
    elif water=="Medium": water_msg="Medium water context makes water-efficient planning important."
    else: water_msg="Limited water context makes drought-aware crops and lower-water businesses more relevant."
    return score, top_crop, water_msg

def livestock_defaults(business_name):
    defaults={
        "Dairy / Milk-Based Business":(5,65000,9000,12500),
        "Goat / Sheep Rearing":(10,11000,1100,2200),
        "Poultry Farming":(100,500,150,260)
    }
    return defaults.get(business_name,(10,10000,1000,2000))

# -----------------------------
# USER LANGUAGE PREFERENCE
# Initialize BEFORE any call to tr() so the sidebar itself can be translated safely.
# -----------------------------
if "preferred_language" not in st.session_state:
    st.session_state["preferred_language"] = "English"
language = st.session_state["preferred_language"]


# ============================================================
# EXTERNAL DATA SOURCES
# ============================================================
KAGGLE_CROP_URL = "https://www.kaggle.com/api/v1/datasets/download/atharvaingle/crop-recommendation-dataset"
MANDI_RESOURCE_ID = "9ef84268-d588-465a-a308-a864a43d0070"
MANDI_API_URL = f"https://api.data.gov.in/resource/{MANDI_RESOURCE_ID}"
FAO_SOILFER_URL = "https://www.fao.org/in-action/soilfer/in-action/crop-suitability-assessment/en"

@st.cache_data(ttl=86400, show_spinner=False)
def load_kaggle_crop_dataset():
    """Load the public Kaggle Crop Recommendation Dataset."""
    try:
        req = urllib.request.Request(
            KAGGLE_CROP_URL,
            headers={"User-Agent": "Gram-Sahayak/1.0"}
        )
        with urllib.request.urlopen(req, timeout=20) as response:
            content = response.read()

        with zipfile.ZipFile(io.BytesIO(content)) as zf:
            csv_names = [n for n in zf.namelist() if n.lower().endswith(".csv")]
            if not csv_names:
                return None, "No CSV file was found in the Kaggle download."
            with zf.open(csv_names[0]) as f:
                df = pd.read_csv(f)

        required = {"N", "P", "K", "temperature", "humidity", "ph", "rainfall", "label"}
        if not required.issubset(df.columns):
            return None, f"Unexpected Kaggle columns: {list(df.columns)}"

        return df, None
    except Exception as exc:
        return None, str(exc)[:220]

def crop_recommendations_from_kaggle(df, values, k=7, top_n=5):
    """Simple nearest-neighbour recommendation using the Kaggle dataset."""
    features = ["N", "P", "K", "temperature", "humidity", "ph", "rainfall"]
    work = df[features + ["label"]].copy()
    work[features] = work[features].apply(pd.to_numeric, errors="coerce")
    work = work.dropna()

    # Standardise each feature so rainfall/temperature/etc. do not dominate distance.
    means = work[features].mean()
    stds = work[features].std().replace(0, 1)
    x = (work[features] - means) / stds
    q = pd.Series(values, index=features)
    q = (q - means) / stds

    distances = ((x - q) ** 2).sum(axis=1) ** 0.5
    nearest = work.loc[distances.nsmallest(min(k, len(distances))).index].copy()
    nearest["distance"] = distances.loc[nearest.index]

    scores = {}
    for label, group in nearest.groupby("label"):
        scores[label] = float((1 / (group["distance"] + 0.001)).sum())

    total = sum(scores.values()) or 1
    ranked = sorted(scores.items(), key=lambda x: x[1], reverse=True)[:top_n]
    return [(crop, round(score / total * 100, 1)) for crop, score in ranked]

def get_data_gov_api_key():
    """Read the official data.gov.in API key from Streamlit secrets or env."""
    try:
        key = st.secrets.get("DATA_GOV_API_KEY", "")
    except Exception:
        key = ""
    return key or os.environ.get("DATA_GOV_API_KEY", "")

MANDI_DISTRICT_MAP = {
    "Hubballi": "Dharwad",
    "Dharwad": "Dharwad",
    "Belagavi": "Belagavi",
    "Bengaluru": "Bengaluru Urban",
    "Mysuru": "Mysuru",
    "Shivamogga": "Shivamogga",
    "Davanagere": "Davanagere",
    "Gadag": "Gadag",
    "Haveri": "Haveri",
    "Vijayapura": "Vijayapura",
    "Kalaburagi": "Kalaburagi",
    "Raichur": "Raichur",
    "Tumakuru": "Tumakuru",
    "Chitradurga": "Chitradurga",
}

@st.cache_data(ttl=900, show_spinner=False)
def fetch_mandi_data(location_name):
    """Fetch current Karnataka mandi records from the official OGD API."""
    api_key = get_data_gov_api_key()
    if not api_key:
        return None, "DATA_GOV_API_KEY is not configured."

    district = MANDI_DISTRICT_MAP.get(location_name, location_name)
    params = {
        "api-key": api_key,
        "format": "json",
        "limit": 1000,
        "offset": 0,
        "filters[state]": "Karnataka",
        "filters[district]": district,
    }
    url = MANDI_API_URL + "?" + urllib.parse.urlencode(params)

    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Gram-Sahayak/1.0"})
        with urllib.request.urlopen(req, timeout=20) as response:
            payload = json.loads(response.read().decode("utf-8"))

        records = payload.get("records", [])
        if not records:
            return pd.DataFrame(), None

        df = pd.DataFrame(records)
        wanted = ["state", "district", "market", "commodity", "variety",
                  "grade", "arrival_date", "min_price", "max_price", "modal_price"]
        keep = [c for c in wanted if c in df.columns]
        df = df[keep].copy()

        for col in ["min_price", "max_price", "modal_price"]:
            if col in df.columns:
                df[col] = pd.to_numeric(df[col], errors="coerce")

        return df, None
    except Exception as exc:
        return None, str(exc)[:220]

def render_data_sources():
    st.markdown("### 🔗 Integrated data sources")
    st.markdown(
        "- **Kaggle Crop Recommendation Dataset** — soil N/P/K, temperature, humidity, pH and rainfall inputs.\n"
        "- **FAO SoilFER** — crop suitability methodology/reference using soil, climate and terrain context.\n"
        "- **data.gov.in Mandi Prices** — official daily mandi records when the API key is configured.\n"
        "- **PM MUDRA Yojana, PMEGP and PMFME** — official scheme information already used in the Government Schemes section."
    )
    st.caption("External datasets are fetched at runtime where an API/download is available; the app does not fabricate live values.")


# -----------------------------
# SIDEBAR
# -----------------------------
with st.sidebar:
    st.markdown("## 🌾 Gram Sahayak")
    st.divider()

    LANGUAGE_NAMES = {
        "English": "English",
        "Hindi": "हिंदी",
        "Kannada": "ಕನ್ನಡ"
    }

    language = st.selectbox(
        "🌐 " + tr("language"),
        ["English", "Hindi", "Kannada"],
        index=["English", "Hindi", "Kannada"].index(st.session_state["preferred_language"]),
        format_func=lambda x: LANGUAGE_NAMES[x],
        key="preferred_language"
    )

    locations = [
        "Hubballi", "Dharwad", "Belagavi", "Bengaluru", "Mysuru", "Shivamogga",
        "Davanagere", "Gadag", "Haveri", "Vijayapura", "Kalaburagi", "Raichur",
        "Tumakuru", "Chitradurga"
    ]

    location = st.selectbox("📍 " + tr("location"), locations, format_func=lambda x: ui_data(x, "location_name"))

    st.divider()

    page_values = ["Home", "Market Prices", "Government Schemes", "Financial Assistant", "Business Recommendation", "Smart Action Plan", "Rural Intelligence Hub"]
    page_labels = {
        "Home": "🏠 " + tr("home"),
        "Market Prices": "📈 " + tr("market"),
        "Government Schemes": "🏛️ " + tr("schemes"),
        "Financial Assistant": "💰 " + tr("finance"),
        "Business Recommendation": "💡 " + tr("business"),
        "Smart Action Plan": "🧠 " + tr("action_plan"),
        "Rural Intelligence Hub": "🌟 " + p2("hub")
    }

    page = st.radio(
        tr("navigate"),
        page_values,
        format_func=lambda x: page_labels[x]
    )

T = TEXT[language]
# ============================================================
# MARKET DATA
# ============================================================

# Demo/sample prices. These are NOT live mandi/API prices.
CROP_DATA = {
    "Tomato": {"price": 30, "unit": "kg", "trend": "Increasing", "category": "Vegetable"},
    "Onion": {"price": 35, "unit": "kg", "trend": "Stable", "category": "Vegetable"},
    "Potato": {"price": 28, "unit": "kg", "trend": "Stable", "category": "Vegetable"},
    "Carrot": {"price": 40, "unit": "kg", "trend": "Increasing", "category": "Vegetable"},
    "Beans": {"price": 55, "unit": "kg", "trend": "Increasing", "category": "Vegetable"},

    # 30+ additional crops
    "Brinjal": {"price": 32, "unit": "kg", "trend": "Stable", "category": "Vegetable"},
    "Cabbage": {"price": 24, "unit": "kg", "trend": "Stable", "category": "Vegetable"},
    "Cauliflower": {"price": 38, "unit": "kg", "trend": "Increasing", "category": "Vegetable"},
    "Capsicum": {"price": 62, "unit": "kg", "trend": "Increasing", "category": "Vegetable"},
    "Green Chilli": {"price": 58, "unit": "kg", "trend": "Increasing", "category": "Vegetable"},
    "Lady Finger": {"price": 45, "unit": "kg", "trend": "Stable", "category": "Vegetable"},
    "Bottle Gourd": {"price": 30, "unit": "kg", "trend": "Stable", "category": "Vegetable"},
    "Bitter Gourd": {"price": 48, "unit": "kg", "trend": "Increasing", "category": "Vegetable"},
    "Cucumber": {"price": 30, "unit": "kg", "trend": "Stable", "category": "Vegetable"},
    "Pumpkin": {"price": 22, "unit": "kg", "trend": "Stable", "category": "Vegetable"},
    "Drumstick": {"price": 70, "unit": "kg", "trend": "Increasing", "category": "Vegetable"},
    "Peas": {"price": 65, "unit": "kg", "trend": "Increasing", "category": "Vegetable"},
    "Beetroot": {"price": 36, "unit": "kg", "trend": "Stable", "category": "Vegetable"},
    "Radish": {"price": 26, "unit": "kg", "trend": "Stable", "category": "Vegetable"},
    "Spinach": {"price": 25, "unit": "kg", "trend": "Increasing", "category": "Leafy"},
    "Coriander": {"price": 55, "unit": "kg", "trend": "Increasing", "category": "Leafy"},
    "Fenugreek Leaves": {"price": 48, "unit": "kg", "trend": "Stable", "category": "Leafy"},

    "Maize": {"price": 24, "unit": "kg", "trend": "Stable", "category": "Cereal"},
    "Wheat": {"price": 30, "unit": "kg", "trend": "Stable", "category": "Cereal"},
    "Rice": {"price": 42, "unit": "kg", "trend": "Stable", "category": "Cereal"},
    "Ragi": {"price": 38, "unit": "kg", "trend": "Increasing", "category": "Cereal"},
    "Jowar": {"price": 34, "unit": "kg", "trend": "Increasing", "category": "Cereal"},
    "Bajra": {"price": 32, "unit": "kg", "trend": "Stable", "category": "Cereal"},

    "Groundnut": {"price": 75, "unit": "kg", "trend": "Increasing", "category": "Oilseed"},
    "Sunflower": {"price": 58, "unit": "kg", "trend": "Stable", "category": "Oilseed"},
    "Soybean": {"price": 48, "unit": "kg", "trend": "Stable", "category": "Oilseed"},
    "Tur": {"price": 105, "unit": "kg", "trend": "Increasing", "category": "Pulse"},
    "Green Gram": {"price": 92, "unit": "kg", "trend": "Stable", "category": "Pulse"},
    "Black Gram": {"price": 88, "unit": "kg", "trend": "Stable", "category": "Pulse"},
    "Bengal Gram": {"price": 70, "unit": "kg", "trend": "Stable", "category": "Pulse"},

    "Cotton": {"price": 72, "unit": "kg", "trend": "Increasing", "category": "Commercial"},
    "Sugarcane": {"price": 3.6, "unit": "kg", "trend": "Stable", "category": "Commercial"},
    "Turmeric": {"price": 145, "unit": "kg", "trend": "Increasing", "category": "Spice"},
    "Chilli": {"price": 190, "unit": "kg", "trend": "Increasing", "category": "Spice"},
    "Ginger": {"price": 105, "unit": "kg", "trend": "Increasing", "category": "Spice"},
    "Garlic": {"price": 120, "unit": "kg", "trend": "Stable", "category": "Spice"},
    "Coconut": {"price": 38, "unit": "piece", "trend": "Stable", "category": "Horticulture"},
    "Banana": {"price": 42, "unit": "kg", "trend": "Stable", "category": "Fruit"},
    "Mango": {"price": 65, "unit": "kg", "trend": "Increasing", "category": "Fruit"},
    "Papaya": {"price": 38, "unit": "kg", "trend": "Stable", "category": "Fruit"},
    "Guava": {"price": 55, "unit": "kg", "trend": "Increasing", "category": "Fruit"},
}

# Location multiplier = demonstration of location-sensitive pricing.
# It is intentionally labelled as sample data, not live mandi data.
LOCATION_FACTOR = {
    "Hubballi": 1.00,
    "Dharwad": 0.98,
    "Belagavi": 1.03,
    "Bengaluru": 1.18,
    "Mysuru": 1.08,
    "Shivamogga": 1.02,
    "Davanagere": 0.97,
    "Gadag": 0.95,
    "Haveri": 0.96,
    "Vijayapura": 0.94,
    "Kalaburagi": 0.96,
    "Raichur": 0.95,
    "Tumakuru": 1.05,
    "Chitradurga": 0.96,
}


# ------------------------------------------------------------
# LOCATION-WISE LOCAL CROPS
# These are prototype/demo crop profiles for the selected Karnataka
# locations. They are NOT a live agricultural production database.
# ------------------------------------------------------------
LOCAL_CROPS = {
    "Hubballi": ["Tomato", "Onion", "Maize", "Jowar", "Groundnut", "Chilli", "Cotton", "Ragi"],
    "Dharwad": ["Onion", "Maize", "Soybean", "Cotton", "Chilli", "Jowar", "Groundnut", "Wheat", "Ragi"],
    "Belagavi": ["Sugarcane", "Maize", "Soybean", "Groundnut", "Onion", "Turmeric", "Banana", "Chilli", "Cotton", "Wheat"],
    "Bengaluru": ["Tomato", "Ragi", "Beans", "Carrot", "Cabbage", "Cauliflower", "Capsicum", "Green Chilli", "Potato", "Mango", "Banana"],
    "Mysuru": ["Rice", "Ragi", "Sugarcane", "Tomato", "Banana", "Coconut", "Turmeric", "Maize", "Onion", "Mango"],
    "Shivamogga": ["Rice", "Maize", "Tomato", "Ginger", "Chilli", "Banana", "Coconut", "Arecanut" if "Arecanut" in CROP_DATA else "Banana"],
    "Davanagere": ["Maize", "Rice", "Cotton", "Chilli", "Jowar", "Onion", "Groundnut", "Wheat"],
    "Gadag": ["Jowar", "Groundnut", "Cotton", "Sunflower", "Onion", "Bengal Gram", "Tur", "Chilli"],
    "Haveri": ["Cotton", "Maize", "Chilli", "Soybean", "Groundnut", "Rice", "Jowar", "Onion", "Turmeric"],
    "Vijayapura": ["Jowar", "Tur", "Bengal Gram", "Sunflower", "Groundnut", "Sugarcane", "Wheat", "Chilli", "Onion"],
    "Kalaburagi": ["Tur", "Bengal Gram", "Jowar", "Soybean", "Sunflower", "Cotton", "Groundnut", "Onion"],
    "Raichur": ["Rice", "Cotton", "Jowar", "Tur", "Chilli", "Groundnut", "Sunflower", "Banana"],
    "Tumakuru": ["Ragi", "Groundnut", "Maize", "Coconut", "Tomato", "Onion", "Sunflower", "Tur"],
    "Chitradurga": ["Ragi", "Groundnut", "Jowar", "Maize", "Sunflower", "Onion", "Tur", "Cotton"],
}

def local_crops_for_location(location):
    return [crop for crop in LOCAL_CROPS.get(location, []) if crop in CROP_DATA]

def location_crop_price(crop, location):
    """Return a location-adjusted demo price. Not a live mandi price."""
    base = CROP_DATA[crop]["price"]
    location_factor = LOCATION_FACTOR.get(location, 1.0)

    # Small prototype premium for crops listed as locally grown.
    # This demonstrates local-market adjustment; it is not a statistical model.
    local_bonus = 1.04 if crop in LOCAL_CROPS.get(location, []) else 1.0
    return base * location_factor * local_bonus


# ------------------------------------------------------------
# LOCATION-BASED WATER AVAILABILITY (DEMO ADVISORY DATA)
# Water is now derived from location instead of user input.
# These are prototype classifications, not live groundwater data.
# ------------------------------------------------------------
LOCATION_WATER = {
    "Hubballi": "Medium",
    "Dharwad": "Medium",
    "Belagavi": "Good",
    "Bengaluru": "Good",
    "Mysuru": "Good",
    "Shivamogga": "Good",
    "Davanagere": "Medium",
    "Gadag": "Limited",
    "Haveri": "Medium",
    "Vijayapura": "Limited",
    "Kalaburagi": "Limited",
    "Raichur": "Medium",
    "Tumakuru": "Medium",
    "Chitradurga": "Limited",
}

# ------------------------------------------------------------
# SEASON + LOCATION CROP ADVISOR
# Prototype agronomic rules: use as a demonstration only and
# verify crop suitability with local agriculture experts/soil tests.
# ------------------------------------------------------------
CROP_ADVISORY = {
    "Tomato": {"seasons": ["Kharif", "Rabi", "Summer"], "locations": ["Bengaluru", "Mysuru", "Belagavi", "Dharwad", "Hubballi", "Haveri", "Shivamogga", "Tumakuru"], "water": "Medium", "harvest": "3–4 months", "success": 82, "risk": "Price fluctuations, pests and excess rain"},
    "Onion": {"seasons": ["Kharif", "Rabi"], "locations": ["Dharwad", "Hubballi", "Davanagere", "Vijayapura", "Kalaburagi", "Raichur", "Belagavi"], "water": "Medium", "harvest": "4–5 months", "success": 80, "risk": "Price volatility and storage losses"},
    "Potato": {"seasons": ["Rabi", "Summer"], "locations": ["Belagavi", "Dharwad", "Hassan", "Mysuru", "Chitradurga"], "water": "Medium", "harvest": "3–4 months", "success": 78, "risk": "Disease, heat and price variation"},
    "Maize": {"seasons": ["Kharif", "Rabi", "Summer"], "locations": ["Davanagere", "Haveri", "Dharwad", "Belagavi", "Tumakuru", "Shivamogga", "Mysuru"], "water": "Medium", "harvest": "3–4 months", "success": 84, "risk": "Rainfall variation and pest pressure"},
    "Ragi": {"seasons": ["Kharif", "Rabi"], "locations": ["Bengaluru", "Tumakuru", "Chitradurga", "Mysuru", "Dharwad"], "water": "Limited", "harvest": "3–4 months", "success": 86, "risk": "Moisture stress and market price variation"},
    "Jowar": {"seasons": ["Kharif", "Rabi"], "locations": ["Vijayapura", "Kalaburagi", "Raichur", "Gadag", "Dharwad", "Haveri"], "water": "Limited", "harvest": "3–4 months", "success": 85, "risk": "Dry spells and pest pressure"},
    "Bengal Gram": {"seasons": ["Rabi"], "locations": ["Kalaburagi", "Vijayapura", "Raichur", "Gadag", "Dharwad"], "water": "Limited", "harvest": "4–5 months", "success": 88, "risk": "Moisture stress and pod pests"},
    "Tur": {"seasons": ["Kharif"], "locations": ["Kalaburagi", "Vijayapura", "Raichur", "Gadag", "Dharwad"], "water": "Limited", "harvest": "5–7 months", "success": 88, "risk": "Long crop duration and rainfall variability"},
    "Groundnut": {"seasons": ["Kharif", "Summer"], "locations": ["Tumakuru", "Chitradurga", "Raichur", "Dharwad", "Belagavi"], "water": "Limited", "harvest": "4–5 months", "success": 82, "risk": "Dry spells and fungal disease"},
    "Sunflower": {"seasons": ["Kharif", "Rabi", "Summer"], "locations": ["Raichur", "Kalaburagi", "Vijayapura", "Dharwad", "Gadag"], "water": "Limited", "harvest": "3–4 months", "success": 80, "risk": "Water stress and price variation"},
    "Soybean": {"seasons": ["Kharif"], "locations": ["Kalaburagi", "Vijayapura", "Dharwad", "Belagavi", "Raichur"], "water": "Limited", "harvest": "3–4 months", "success": 84, "risk": "Excess rain, pests and market price"},
    "Cotton": {"seasons": ["Kharif"], "locations": ["Kalaburagi", "Raichur", "Vijayapura", "Dharwad", "Gadag", "Haveri"], "water": "Limited", "harvest": "6–8 months", "success": 79, "risk": "Pests, rainfall variability and price risk"},
    "Sugarcane": {"seasons": ["Kharif", "Summer"], "locations": ["Belagavi", "Bagalkot", "Vijayapura", "Mysuru", "Mandya", "Dharwad"], "water": "Good", "harvest": "10–15 months", "success": 76, "risk": "High water requirement and long capital lock-in"},
    "Turmeric": {"seasons": ["Kharif"], "locations": ["Belagavi", "Haveri", "Dharwad", "Shivamogga", "Mysuru"], "water": "Medium", "harvest": "7–9 months", "success": 80, "risk": "Rhizome disease and price variation"},
    "Chilli": {"seasons": ["Kharif", "Rabi"], "locations": ["Byadgi/Haveri", "Dharwad", "Raichur", "Kalaburagi", "Belagavi"], "water": "Medium", "harvest": "5–7 months", "success": 78, "risk": "Pests, disease and price volatility"},
    "Rice": {"seasons": ["Kharif", "Rabi"], "locations": ["Shivamogga", "Davanagere", "Mysuru", "Mandya", "Raichur", "Haveri"], "water": "Good", "harvest": "4–5 months", "success": 83, "risk": "Water requirement and rainfall timing"},
    "Banana": {"seasons": ["Kharif", "Rabi", "Summer"], "locations": ["Belagavi", "Vijayapura", "Dharwad", "Mysuru", "Raichur"], "water": "Good", "harvest": "9–12 months", "success": 80, "risk": "Wind, water requirement and disease"},
}

SEASON_MONTHS = {
    "Kharif": [6, 7, 8, 9, 10],
    "Rabi": [10, 11, 12, 1, 2, 3],
    "Summer": [3, 4, 5],
}

def current_season():
    month = datetime.now().month
    for season, months in SEASON_MONTHS.items():
        if month in months:
            return season
    return "Kharif"

def location_water(location):
    return LOCATION_WATER.get(location, "Medium")

def crop_suitability(crop, location, season):
    info = CROP_ADVISORY.get(crop)
    if not info:
        return 0
    score = info["success"]
    if location in info["locations"]:
        score += 8
    else:
        score -= 15
    if season in info["seasons"]:
        score += 7
    else:
        score -= 18
    return max(0, min(100, score))

def best_crops_for_location(location, season, limit=5):
    ranked = []
    for crop, info in CROP_ADVISORY.items():
        score = crop_suitability(crop, location, season)
        if score >= 60:
            ranked.append((crop, score, info))
    ranked.sort(key=lambda x: x[1], reverse=True)
    return ranked[:limit]

# Estimated business outlook is a prototype planning estimate, not a
# real statistical success probability.
BUSINESS_OUTLOOK = {
    "Vegetable Cultivation": {"success_period": "3–6 months", "stable_period": "6–12 months", "risk_period": "first 3–6 months", "base_success": 72},
    "Small Food Processing Unit": {"success_period": "4–8 months", "stable_period": "8–18 months", "risk_period": "first 6–12 months", "base_success": 68},
    "Grocery & Daily-Needs Store": {"success_period": "3–6 months", "stable_period": "6–12 months", "risk_period": "first 3–6 months", "base_success": 75},
    "Street Food / Snack Business": {"success_period": "1–3 months", "stable_period": "3–6 months", "risk_period": "first 1–3 months", "base_success": 74},
    "Dairy / Milk-Based Business": {"success_period": "3–6 months", "stable_period": "6–12 months", "risk_period": "first 3–6 months", "base_success": 70},
    "Goat / Sheep Rearing": {"success_period": "6–12 months", "stable_period": "12–24 months", "risk_period": "first 6–12 months", "base_success": 66},
    "Poultry Farming": {"success_period": "2–4 months", "stable_period": "6–12 months", "risk_period": "first 2–4 months", "base_success": 69},
    "Local Delivery & Transport Service": {"success_period": "3–6 months", "stable_period": "6–12 months", "risk_period": "first 3–6 months", "base_success": 73},
    "Tailoring & Garment Service": {"success_period": "3–6 months", "stable_period": "6–12 months", "risk_period": "first 3–6 months", "base_success": 76},
    "Handicrafts & Local Products": {"success_period": "4–8 months", "stable_period": "8–18 months", "risk_period": "first 6–12 months", "base_success": 64},
    "Farm Input & Agri Service Centre": {"success_period": "4–8 months", "stable_period": "8–18 months", "risk_period": "first 6–12 months", "base_success": 67},
    "Small Repair & Service Centre": {"success_period": "2–5 months", "stable_period": "6–12 months", "risk_period": "first 2–5 months", "base_success": 77},
}

# ============================================================
# BUSINESS PROFILES
# ============================================================

BUSINESSES = [
    {
        "name": "Vegetable Cultivation",
        "capital": (25000, 250000),
        "resources": ["Land", "Water", "Agricultural tools"],
        "interests": ["Farming", "Agriculture", "Vegetables"],
        "locations": ["Hubballi", "Dharwad", "Belagavi", "Shivamogga", "Haveri",
                      "Davanagere", "Gadag", "Vijayapura", "Kalaburagi", "Raichur", "Tumakuru"],
        "investment": "₹25,000 – ₹2.5 lakh",
        "model": "Grow vegetables → sell to local markets, retailers, hotels or direct customers.",
        "risk": "Weather, water availability and price fluctuations.",
        "steps": [
            "Select crops based on local demand and water availability.",
            "Estimate seed, labour, irrigation and transport costs.",
            "Plan more than one sales channel instead of depending on a single buyer."
        ],
        "schemes": ["Kisan Credit Card", "PMEGP", "Agriculture Infrastructure Fund"]
    },
    {
        "name": "Small Food Processing Unit",
        "capital": (75000, 1000000),
        "resources": ["Kitchen/Workspace", "Food processing equipment", "Raw materials"],
        "interests": ["Food", "Cooking", "Processing", "Snacks"],
        "locations": locations,
        "investment": "₹75,000 – ₹10 lakh+",
        "model": "Convert local produce into higher-value products such as flour, snacks, pickles, spice mixes or packaged foods.",
        "risk": "Food safety, packaging, shelf life and market access.",
        "steps": [
            "Choose one product with a clear local customer segment.",
            "Calculate raw material, packaging, labour and selling costs.",
            "Test a small batch before investing in larger equipment."
        ],
        "schemes": ["PMFME", "MUDRA", "PMEGP"]
    },
    {
        "name": "Grocery & Daily-Needs Store",
        "capital": (100000, 700000),
        "resources": ["Shop space", "Working capital", "Supplier network"],
        "interests": ["Retail", "Shopping", "Customer service", "Trading"],
        "locations": locations,
        "investment": "₹1 lakh – ₹7 lakh",
        "model": "Sell essential household products with repeat local demand.",
        "risk": "Competition, inventory management and credit sales.",
        "steps": [
            "Start with fast-moving essentials instead of excessive inventory.",
            "Track daily sales and stock movement.",
            "Add high-demand local products after observing customer behaviour."
        ],
        "schemes": ["MUDRA", "PMEGP"]
    },
    {
        "name": "Street Food / Snack Business",
        "capital": (30000, 300000),
        "resources": ["Kitchen equipment", "Small stall/shop", "Food preparation skills"],
        "interests": ["Food", "Cooking", "Customer service"],
        "locations": locations,
        "investment": "₹30,000 – ₹3 lakh",
        "model": "Sell affordable snacks or meals at a high-footfall local location.",
        "risk": "Location dependency, hygiene and daily demand variation.",
        "steps": [
            "Choose a small menu with good margins.",
            "Test demand at different times of the day.",
            "Maintain hygiene, consistent quality and simple bookkeeping."
        ],
        "schemes": ["PM SVANidhi", "MUDRA", "PMEGP"]
    },
    {
        "name": "Dairy / Milk-Based Business",
        "capital": (100000, 800000),
        "resources": ["Cattle", "Fodder", "Water", "Shelter"],
        "interests": ["Dairy", "Livestock", "Agriculture"],
        "locations": locations,
        "investment": "₹1 lakh – ₹8 lakh",
        "model": "Milk production with possible value addition such as curd, paneer or ghee.",
        "risk": "Animal health, feed costs and milk-price changes.",
        "steps": [
            "Estimate feed and veterinary costs before buying animals.",
            "Identify a reliable local milk buyer.",
            "Maintain records of milk yield and animal health."
        ],
        "schemes": ["MUDRA", "Kisan Credit Card", "PMEGP"]
    },
    {
        "name": "Goat / Sheep Rearing",
        "capital": (60000, 500000),
        "resources": ["Land", "Shelter", "Livestock care"],
        "interests": ["Livestock", "Farming", "Animal husbandry"],
        "locations": locations,
        "investment": "₹60,000 – ₹5 lakh",
        "model": "Rear animals for meat, breeding or local livestock markets.",
        "risk": "Disease, feed costs and market-price fluctuations.",
        "steps": [
            "Start with a manageable herd size.",
            "Plan vaccination and veterinary care.",
            "Build a buyer network before scaling."
        ],
        "schemes": ["MUDRA", "Kisan Credit Card", "PMEGP"]
    },
    {
        "name": "Poultry Farming",
        "capital": (80000, 600000),
        "resources": ["Shelter", "Water", "Poultry equipment"],
        "interests": ["Poultry", "Livestock", "Farming"],
        "locations": locations,
        "investment": "₹80,000 – ₹6 lakh",
        "model": "Egg or broiler production for nearby markets.",
        "risk": "Feed costs, disease and price volatility.",
        "steps": [
            "Choose egg or meat production based on local demand.",
            "Calculate feed cost per bird.",
            "Maintain biosecurity and veterinary schedules."
        ],
        "schemes": ["MUDRA", "Kisan Credit Card", "PMEGP"]
    },
    {
        "name": "Local Delivery & Transport Service",
        "capital": (75000, 600000),
        "resources": ["Two-wheeler/vehicle", "Mobile phone", "Driving skills"],
        "interests": ["Transport", "Delivery", "Customer service"],
        "locations": locations,
        "investment": "₹75,000 – ₹6 lakh",
        "model": "Deliver groceries, farm inputs, medicines or local goods within nearby villages/towns.",
        "risk": "Fuel costs, vehicle maintenance and route density.",
        "steps": [
            "Map villages and shops that need regular delivery.",
            "Start with a defined service radius.",
            "Use simple digital records for orders, fuel and collections."
        ],
        "schemes": ["MUDRA", "PMEGP"]
    },
    {
        "name": "Tailoring & Garment Service",
        "capital": (30000, 250000),
        "resources": ["Sewing machine", "Workspace", "Tailoring skills"],
        "interests": ["Tailoring", "Fashion", "Handicrafts"],
        "locations": locations,
        "investment": "₹30,000 – ₹2.5 lakh",
        "model": "Alterations, stitching, school uniforms, traditional clothing and small-batch garments.",
        "risk": "Competition and seasonal demand.",
        "steps": [
            "Start with alterations and high-demand local garments.",
            "Build repeat customers through reliable delivery.",
            "Add machines only when order volume justifies them."
        ],
        "schemes": ["PM Vishwakarma", "MUDRA", "PMEGP"]
    },
    {
        "name": "Handicrafts & Local Products",
        "capital": (25000, 300000),
        "resources": ["Craft skills", "Raw materials", "Workspace"],
        "interests": ["Handicrafts", "Art", "Crafts"],
        "locations": locations,
        "investment": "₹25,000 – ₹3 lakh",
        "model": "Make baskets, decor, traditional products or locally distinctive handmade goods.",
        "risk": "Demand discovery and inconsistent order volume.",
        "steps": [
            "Identify one product with a clear customer segment.",
            "Create a small catalogue and sample products.",
            "Explore local fairs, retailers and digital selling channels."
        ],
        "schemes": ["PM Vishwakarma", "PMEGP", "MUDRA"]
    },
    {
        "name": "Farm Input & Agri Service Centre",
        "capital": (150000, 1000000),
        "resources": ["Shop", "Agriculture knowledge", "Supplier network"],
        "interests": ["Agriculture", "Retail", "Advisory"],
        "locations": locations,
        "investment": "₹1.5 lakh – ₹10 lakh+",
        "model": "Supply seeds, tools, irrigation accessories and farm-related services.",
        "risk": "Inventory, licensing requirements and seasonal demand.",
        "steps": [
            "Identify the crops and farm needs of nearby villages.",
            "Stock fast-moving inputs first.",
            "Follow all applicable licences and quality requirements."
        ],
        "schemes": ["ACABC", "MUDRA", "PMEGP"]
    },
    {
        "name": "Small Repair & Service Centre",
        "capital": (40000, 300000),
        "resources": ["Repair tools", "Workspace", "Technical skill"],
        "interests": ["Repair", "Technology", "Machines", "Electronics"],
        "locations": locations,
        "investment": "₹40,000 – ₹3 lakh",
        "model": "Repair phones, appliances, agricultural equipment or other locally needed items.",
        "risk": "Skill dependency and availability of spare parts.",
        "steps": [
            "Choose one repair category based on local demand.",
            "Keep commonly required spare parts.",
            "Build trust through transparent pricing and service records."
        ],
        "schemes": ["MUDRA", "PMEGP"]
    },
]

SCHEME_TR = {
    "Hindi": {
        "best": {
            "New micro-enterprises in manufacturing and eligible service/non-farm activities.":"विनिर्माण और पात्र सेवा/गैर-कृषि गतिविधियों वाले नए सूक्ष्म उद्यम।",
            "Small businesses needing working capital or business expansion finance.":"कार्यशील पूंजी या व्यवसाय विस्तार के लिए वित्त की जरूरत वाले छोटे व्यवसाय।",
            "Eligible street vendors.":"पात्र स्ट्रीट वेंडर।",
            "Micro food-processing businesses and eligible SHGs/FPOs/cooperatives.":"सूक्ष्म खाद्य-प्रसंस्करण व्यवसाय और पात्र SHG/FPO/सहकारी संस्थाएँ।",
            "Farmers and eligible agricultural/allied activities.":"किसान और पात्र कृषि/संबद्ध गतिविधियाँ।",
            "Post-harvest infrastructure and eligible community farming assets.":"फसल कटाई के बाद की अवसंरचना और पात्र सामुदायिक कृषि परिसंपत्तियाँ।",
            "Eligible agriculture-trained entrepreneurs providing farm-related services.":"पात्र कृषि-प्रशिक्षित उद्यमी जो कृषि संबंधी सेवाएँ देते हैं।",
            "Rural women-led Self Help Groups and rural livelihoods.":"ग्रामीण महिलाओं के नेतृत्व वाले स्वयं सहायता समूह और ग्रामीण आजीविका।",
            "Eligible traditional artisans and craftspeople.":"पात्र पारंपरिक कारीगर और शिल्पकार।",
            "Eligible farmers and agricultural energy/solar applications.":"पात्र किसान और कृषि ऊर्जा/सौर अनुप्रयोग।"
        },
        "desc": {
            "A credit-linked government programme that supports new micro-enterprises through bank finance and margin-money subsidy. It is designed to create self-employment and employment opportunities, especially for rural and aspiring entrepreneurs.":"यह बैंक वित्त और मार्जिन-मनी सब्सिडी के माध्यम से नए सूक्ष्म उद्यमों को सहायता देने वाला क्रेडिट-लिंक्ड सरकारी कार्यक्रम है। इसका उद्देश्य विशेष रूप से ग्रामीण और नए उद्यमियों के लिए स्वरोजगार और रोजगार के अवसर बनाना है।",
            "Provides collateral-free institutional credit for eligible micro enterprises in manufacturing, trading, services and allied agricultural activities.":"विनिर्माण, व्यापार, सेवा और संबद्ध कृषि गतिविधियों वाले पात्र सूक्ष्म उद्यमों के लिए बिना जमानत संस्थागत ऋण उपलब्ध कराता है।",
            "A micro-credit and support programme for street vendors. The restructured scheme includes progressive working-capital loans, digital adoption incentives and broader livelihood support.":"स्ट्रीट वेंडरों के लिए सूक्ष्म ऋण और सहायता कार्यक्रम। पुनर्गठित योजना में क्रमिक कार्यशील पूंजी ऋण, डिजिटल अपनाने के प्रोत्साहन और व्यापक आजीविका सहायता शामिल है।",
            "Supports formalisation, upgrading and capacity building for micro food-processing enterprises. Eligible individual units can receive credit-linked capital subsidy subject to scheme conditions.":"सूक्ष्म खाद्य-प्रसंस्करण उद्यमों के औपचारिकीकरण, उन्नयन और क्षमता निर्माण में सहायता करता है। पात्र व्यक्तिगत इकाइयों को योजना की शर्तों के अनुसार क्रेडिट-लिंक्ड पूंजी सब्सिडी मिल सकती है।",
            "Provides formal credit access for agricultural and allied working-capital needs, subject to lending and eligibility conditions.":"कृषि और संबद्ध कार्यशील पूंजी जरूरतों के लिए पात्रता और ऋण शर्तों के अनुसार औपचारिक ऋण सुविधा प्रदान करता है।",
            "Provides financing support for eligible agriculture infrastructure such as post-harvest management and community farming assets.":"फसल कटाई के बाद प्रबंधन और सामुदायिक कृषि परिसंपत्तियों जैसी पात्र कृषि अवसंरचना के लिए वित्तीय सहायता प्रदान करता है।",
            "Supports trained agricultural professionals/eligible candidates in setting up agri-clinics and agri-business centres that provide advisory and agricultural services to farmers.":"प्रशिक्षित कृषि पेशेवरों/पात्र उम्मीदवारों को किसानों के लिए सलाह और कृषि सेवाएँ देने वाले एग्री-क्लिनिक और एग्री-बिजनेस केंद्र स्थापित करने में सहायता करता है।",
            "A rural livelihoods programme that works through Self Help Groups and community institutions to improve access to finance, skills, enterprise support and sustainable livelihoods.":"स्वयं सहायता समूहों और सामुदायिक संस्थाओं के माध्यम से वित्त, कौशल, उद्यम सहायता और टिकाऊ आजीविका तक पहुँच बेहतर करने वाला ग्रामीण आजीविका कार्यक्रम।",
            "Supports eligible traditional artisans and craftspeople with recognition, skill development, toolkit support, credit and market-oriented assistance under the scheme.":"पात्र पारंपरिक कारीगरों और शिल्पकारों को पहचान, कौशल विकास, टूलकिट, ऋण और बाजार-उन्मुख सहायता प्रदान करता है।",
            "Supports solar-energy-related interventions in agriculture, including eligible solar pumps and other components under the scheme.":"कृषि में सौर ऊर्जा से जुड़े उपायों, पात्र सौर पंपों और योजना के अन्य घटकों को सहायता देता है।"
        }
    },
    "Kannada": {
        "best": {
            "New micro-enterprises in manufacturing and eligible service/non-farm activities.":"ಉತ್ಪಾದನೆ ಮತ್ತು ಅರ್ಹ ಸೇವೆ/ಕೃಷಿಯೇತರ ಚಟುವಟಿಕೆಗಳ ಹೊಸ ಸಣ್ಣ ಉದ್ಯಮಗಳು.",
            "Small businesses needing working capital or business expansion finance.":"ಕಾರ್ಯನಿರ್ವಹಣಾ ಬಂಡವಾಳ ಅಥವಾ ವ್ಯವಹಾರ ವಿಸ್ತರಣೆಗೆ ಹಣಕಾಸು ಬೇಕಿರುವ ಸಣ್ಣ ವ್ಯವಹಾರಗಳು.",
            "Eligible street vendors.":"ಅರ್ಹ ಬೀದಿ ವ್ಯಾಪಾರಿಗಳು.",
            "Micro food-processing businesses and eligible SHGs/FPOs/cooperatives.":"ಸಣ್ಣ ಆಹಾರ ಸಂಸ್ಕರಣಾ ವ್ಯವಹಾರಗಳು ಮತ್ತು ಅರ್ಹ SHG/FPO/ಸಹಕಾರಿ ಸಂಸ್ಥೆಗಳು.",
            "Farmers and eligible agricultural/allied activities.":"ರೈತರು ಮತ್ತು ಅರ್ಹ ಕೃಷಿ/ಸಂಬಂಧಿತ ಚಟುವಟಿಕೆಗಳು.",
            "Post-harvest infrastructure and eligible community farming assets.":"ಕೊಯ್ಲಿನ ನಂತರದ ಮೂಲಸೌಕರ್ಯ ಮತ್ತು ಅರ್ಹ ಸಮುದಾಯ ಕೃಷಿ ಆಸ್ತಿಗಳು.",
            "Eligible agriculture-trained entrepreneurs providing farm-related services.":"ಕೃಷಿ ತರಬೇತಿ ಪಡೆದ ಅರ್ಹ ಉದ್ಯಮಿಗಳು ಮತ್ತು ಕೃಷಿ ಸಂಬಂಧಿತ ಸೇವಾ ಪೂರೈಕೆದಾರರು.",
            "Rural women-led Self Help Groups and rural livelihoods.":"ಗ್ರಾಮೀಣ ಮಹಿಳೆಯರ ನೇತೃತ್ವದ ಸ್ವಸಹಾಯ ಗುಂಪುಗಳು ಮತ್ತು ಗ್ರಾಮೀಣ ಜೀವನೋಪಾಯ.",
            "Eligible traditional artisans and craftspeople.":"ಅರ್ಹ ಸಾಂಪ್ರದಾಯಿಕ ಕುಶಲಕರ್ಮಿಗಳು ಮತ್ತು ಶಿಲ್ಪಿಗಳು.",
            "Eligible farmers and agricultural energy/solar applications.":"ಅರ್ಹ ರೈತರು ಮತ್ತು ಕೃಷಿ ಶಕ್ತಿ/ಸೌರ ಅನ್ವಯಿಕೆಗಳು."
        },
        "desc": {
            "A credit-linked government programme that supports new micro-enterprises through bank finance and margin-money subsidy. It is designed to create self-employment and employment opportunities, especially for rural and aspiring entrepreneurs.":"ಬ್ಯಾಂಕ್ ಹಣಕಾಸು ಮತ್ತು ಮಾರ್ಜಿನ್-ಮನಿ ಸಬ್ಸಿಡಿ ಮೂಲಕ ಹೊಸ ಸಣ್ಣ ಉದ್ಯಮಗಳಿಗೆ ಬೆಂಬಲ ನೀಡುವ ಕ್ರೆಡಿಟ್-ಲಿಂಕ್ಡ್ ಸರ್ಕಾರಿ ಕಾರ್ಯಕ್ರಮ. ವಿಶೇಷವಾಗಿ ಗ್ರಾಮೀಣ ಮತ್ತು ಹೊಸ ಉದ್ಯಮಿಗಳಿಗೆ ಸ್ವಯಂ ಉದ್ಯೋಗ ಹಾಗೂ ಉದ್ಯೋಗಾವಕಾಶಗಳನ್ನು ಸೃಷ್ಟಿಸುವುದು ಇದರ ಉದ್ದೇಶ.",
            "Provides collateral-free institutional credit for eligible micro enterprises in manufacturing, trading, services and allied agricultural activities.":"ಉತ್ಪಾದನೆ, ವ್ಯಾಪಾರ, ಸೇವೆ ಮತ್ತು ಸಂಬಂಧಿತ ಕೃಷಿ ಚಟುವಟಿಕೆಗಳ ಅರ್ಹ ಸಣ್ಣ ಉದ್ಯಮಗಳಿಗೆ ಜಾಮೀನು ಇಲ್ಲದ ಸಂಸ್ಥಾತ್ಮಕ ಸಾಲ ಒದಗಿಸುತ್ತದೆ.",
            "A micro-credit and support programme for street vendors. The restructured scheme includes progressive working-capital loans, digital adoption incentives and broader livelihood support.":"ಬೀದಿ ವ್ಯಾಪಾರಿಗಳಿಗೆ ಸೂಕ್ಷ್ಮ ಸಾಲ ಮತ್ತು ಬೆಂಬಲ ಕಾರ್ಯಕ್ರಮ. ಪರಿಷ್ಕೃತ ಯೋಜನೆಯಲ್ಲಿ ಹಂತ ಹಂತದ ಕಾರ್ಯನಿರ್ವಹಣಾ ಬಂಡವಾಳ ಸಾಲ, ಡಿಜಿಟಲ್ ಬಳಕೆಗೆ ಪ್ರೋತ್ಸಾಹ ಮತ್ತು ಜೀವನೋಪಾಯ ಬೆಂಬಲ ಸೇರಿವೆ.",
            "Supports formalisation, upgrading and capacity building for micro food-processing enterprises. Eligible individual units can receive credit-linked capital subsidy subject to scheme conditions.":"ಸಣ್ಣ ಆಹಾರ ಸಂಸ್ಕರಣಾ ಉದ್ಯಮಗಳ ಔಪಚಾರಿಕೀಕರಣ, ಉನ್ನತೀಕರಣ ಮತ್ತು ಸಾಮರ್ಥ್ಯ ವೃದ್ಧಿಗೆ ಬೆಂಬಲ ನೀಡುತ್ತದೆ. ಅರ್ಹ ವೈಯಕ್ತಿಕ ಘಟಕಗಳಿಗೆ ಯೋಜನೆಯ ಷರತ್ತುಗಳಂತೆ ಕ್ರೆಡಿಟ್-ಲಿಂಕ್ಡ್ ಬಂಡವಾಳ ಸಬ್ಸಿಡಿ ದೊರೆಯಬಹುದು.",
            "Provides formal credit access for agricultural and allied working-capital needs, subject to lending and eligibility conditions.":"ಕೃಷಿ ಮತ್ತು ಸಂಬಂಧಿತ ಕಾರ್ಯನಿರ್ವಹಣಾ ಬಂಡವಾಳ ಅಗತ್ಯಗಳಿಗೆ ಸಾಲ ಮತ್ತು ಅರ್ಹತಾ ಷರತ್ತುಗಳಂತೆ ಅಧಿಕೃತ ಸಾಲ ಸೌಲಭ್ಯ ಒದಗಿಸುತ್ತದೆ.",
            "Provides financing support for eligible agriculture infrastructure such as post-harvest management and community farming assets.":"ಕೊಯ್ಲಿನ ನಂತರದ ನಿರ್ವಹಣೆ ಮತ್ತು ಸಮುದಾಯ ಕೃಷಿ ಆಸ್ತಿಗಳಂತಹ ಅರ್ಹ ಕೃಷಿ ಮೂಲಸೌಕರ್ಯಕ್ಕೆ ಹಣಕಾಸು ಬೆಂಬಲ ನೀಡುತ್ತದೆ.",
            "Supports trained agricultural professionals/eligible candidates in setting up agri-clinics and agri-business centres that provide advisory and agricultural services to farmers.":"ತರಬೇತಿ ಪಡೆದ ಕೃಷಿ ವೃತ್ತಿಪರರು/ಅರ್ಹ ಅಭ್ಯರ್ಥಿಗಳು ರೈತರಿಗೆ ಸಲಹೆ ಮತ್ತು ಕೃಷಿ ಸೇವೆ ನೀಡುವ ಅಗ್ರಿ-ಕ್ಲಿನಿಕ್ ಮತ್ತು ಅಗ್ರಿ-ಬಿಸಿನೆಸ್ ಕೇಂದ್ರಗಳನ್ನು ಸ್ಥಾಪಿಸಲು ಬೆಂಬಲ ನೀಡುತ್ತದೆ.",
            "A rural livelihoods programme that works through Self Help Groups and community institutions to improve access to finance, skills, enterprise support and sustainable livelihoods.":"ಸ್ವಸಹಾಯ ಗುಂಪುಗಳು ಮತ್ತು ಸಮುದಾಯ ಸಂಸ್ಥೆಗಳ ಮೂಲಕ ಹಣಕಾಸು, ಕೌಶಲ್ಯ, ಉದ್ಯಮ ಬೆಂಬಲ ಮತ್ತು ಶಾಶ್ವತ ಜೀವನೋಪಾಯಕ್ಕೆ ಪ್ರವೇಶವನ್ನು ಸುಧಾರಿಸುವ ಗ್ರಾಮೀಣ ಜೀವನೋಪಾಯ ಕಾರ್ಯಕ್ರಮ.",
            "Supports eligible traditional artisans and craftspeople with recognition, skill development, toolkit support, credit and market-oriented assistance under the scheme.":"ಅರ್ಹ ಸಾಂಪ್ರದಾಯಿಕ ಕುಶಲಕರ್ಮಿಗಳು ಮತ್ತು ಶಿಲ್ಪಿಗಳಿಗೆ ಮಾನ್ಯತೆ, ಕೌಶಲ್ಯ ಅಭಿವೃದ್ಧಿ, ಟೂಲ್‌ಕಿಟ್, ಸಾಲ ಮತ್ತು ಮಾರುಕಟ್ಟೆ ಆಧಾರಿತ ಸಹಾಯ ನೀಡುತ್ತದೆ.",
            "Supports solar-energy-related interventions in agriculture, including eligible solar pumps and other components under the scheme.":"ಅರ್ಹ ಸೌರ ಪಂಪ್‌ಗಳು ಮತ್ತು ಯೋಜನೆಯ ಇತರ ಘಟಕಗಳನ್ನು ಒಳಗೊಂಡಂತೆ ಕೃಷಿಯಲ್ಲಿ ಸೌರಶಕ್ತಿ ಸಂಬಂಧಿತ ಕ್ರಮಗಳಿಗೆ ಬೆಂಬಲ ನೀಡುತ್ತದೆ."
        }
    }
}

# Scheme names, key points, reasons and official-source labels.
SCHEME_NAME_TR = {
    "Hindi": {
        "PMEGP – Prime Minister's Employment Generation Programme": "PMEGP – प्रधानमंत्री रोजगार सृजन कार्यक्रम",
        "Pradhan Mantri MUDRA Yojana (PMMY)": "प्रधानमंत्री मुद्रा योजना (PMMY)",
        "PM SVANidhi": "PM SVANidhi – प्रधानमंत्री स्ट्रीट वेंडर्स आत्मनिर्भर निधि",
        "PMFME – Pradhan Mantri Formalisation of Micro Food Processing Enterprises": "PMFME – प्रधानमंत्री सूक्ष्म खाद्य प्रसंस्करण उद्यम औपचारिकीकरण योजना",
        "Kisan Credit Card (KCC)": "किसान क्रेडिट कार्ड (KCC)",
        "Agriculture Infrastructure Fund (AIF)": "कृषि अवसंरचना कोष (AIF)",
        "Agri-Clinics and Agri-Business Centres (ACABC)": "एग्री-क्लिनिक और एग्री-बिजनेस सेंटर (ACABC)",
        "DAY-NRLM – Deendayal Antyodaya Yojana": "DAY-NRLM – दीनदयाल अंत्योदय योजना",
        "PM Vishwakarma": "PM विश्वकर्मा",
        "PM-KUSUM": "PM-कुसुम"
    },
    "Kannada": {
        "PMEGP – Prime Minister's Employment Generation Programme": "PMEGP – ಪ್ರಧಾನ ಮಂತ್ರಿ ಉದ್ಯೋಗ ಸೃಜನ ಕಾರ್ಯಕ್ರಮ",
        "Pradhan Mantri MUDRA Yojana (PMMY)": "ಪ್ರಧಾನ ಮಂತ್ರಿ ಮುದ್ರಾ ಯೋಜನೆ (PMMY)",
        "PM SVANidhi": "PM SVANidhi – ಪ್ರಧಾನ ಮಂತ್ರಿ ಬೀದಿ ವ್ಯಾಪಾರಿಗಳ ಆತ್ಮನಿರ್ಭರ ನಿಧಿ",
        "PMFME – Pradhan Mantri Formalisation of Micro Food Processing Enterprises": "PMFME – ಪ್ರಧಾನ ಮಂತ್ರಿ ಸೂಕ್ಷ್ಮ ಆಹಾರ ಸಂಸ್ಕರಣಾ ಉದ್ಯಮಗಳ ಔಪಚಾರಿಕೀಕರಣ ಯೋಜನೆ",
        "Kisan Credit Card (KCC)": "ಕಿಸಾನ್ ಕ್ರೆಡಿಟ್ ಕಾರ್ಡ್ (KCC)",
        "Agriculture Infrastructure Fund (AIF)": "ಕೃಷಿ ಮೂಲಸೌಕರ್ಯ ನಿಧಿ (AIF)",
        "Agri-Clinics and Agri-Business Centres (ACABC)": "ಅಗ್ರಿ-ಕ್ಲಿನಿಕ್ ಮತ್ತು ಅಗ್ರಿ-ಬಿಸಿನೆಸ್ ಕೇಂದ್ರಗಳು (ACABC)",
        "DAY-NRLM – Deendayal Antyodaya Yojana": "DAY-NRLM – ದೀನದಯಾಳ್ ಅಂತ್ಯೋದಯ ಯೋಜನೆ",
        "PM Vishwakarma": "PM ವಿಶ್ವಕರ್ಮ",
        "PM-KUSUM": "PM-ಕುಸುಮ್"
    }
}

SCHEME_EXTRA_TR = {
    "Hindi": {
        "key": {
            "For new enterprises; applicant generally must be 18+. Project and eligibility conditions apply.": "नए उद्यमों के लिए; आवेदक सामान्यतः 18+ होना चाहिए। परियोजना और पात्रता की शर्तें लागू होती हैं।",
            "Shishu up to ₹50,000; Kishor above ₹50,000 to ₹5 lakh; Tarun above ₹5 lakh to ₹10 lakh; Tarun Plus above ₹10 lakh to ₹20 lakh for eligible repeat borrowers.": "शिशु ₹50,000 तक; किशोर ₹50,000 से अधिक से ₹5 लाख तक; तरुण ₹5 लाख से अधिक से ₹10 लाख तक; पात्र दोबारा ऋण लेने वालों के लिए तरुण प्लस ₹10 लाख से ₹20 लाख तक।",
            "Loan tranches can go up to ₹15,000, ₹25,000 and ₹50,000, subject to scheme conditions. Lending period has been extended to March 31, 2030.": "योजना की शर्तों के अनुसार ऋण की किश्तें ₹15,000, ₹25,000 और ₹50,000 तक हो सकती हैं। ऋण अवधि 31 मार्च 2030 तक बढ़ाई गई है।",
            "Individual micro food-processing units may receive 35% credit-linked capital subsidy up to ₹10 lakh, subject to eligibility and guidelines.": "पात्रता और दिशानिर्देशों के अनुसार व्यक्तिगत सूक्ष्म खाद्य-प्रसंस्करण इकाइयों को ₹10 लाख तक 35% क्रेडिट-लिंक्ड पूंजी सब्सिडी मिल सकती है।",
            "Can support eligible crop and allied agricultural credit requirements through participating financial institutions.": "भाग लेने वाली वित्तीय संस्थाओं के माध्यम से पात्र फसल और संबद्ध कृषि ऋण आवश्यकताओं को पूरा करने में सहायता कर सकता है।",
            "Eligible loans can receive interest subvention of 3% per year on the loan component up to ₹2 crore, subject to scheme conditions.": "योजना की शर्तों के अनुसार पात्र ऋण के ₹2 करोड़ तक के ऋण घटक पर प्रति वर्ष 3% ब्याज सहायता मिल सकती है।",
            "Eligibility, training, project cost and subsidy provisions depend on the current ACABC guidelines.": "पात्रता, प्रशिक्षण, परियोजना लागत और सब्सिडी के प्रावधान वर्तमान ACABC दिशानिर्देशों पर निर्भर करते हैं।",
            "Support is delivered through the rural livelihood mission structure and applicable state-level mechanisms.": "सहायता ग्रामीण आजीविका मिशन की संरचना और लागू राज्य-स्तरीय व्यवस्थाओं के माध्यम से दी जाती है।",
            "Benefits and eligible trades are subject to the official scheme guidelines.": "लाभ और पात्र व्यवसाय आधिकारिक योजना दिशानिर्देशों के अधीन हैं।",
            "Component, subsidy and implementation conditions vary and are administered through the relevant authorities.": "घटक, सब्सिडी और कार्यान्वयन की शर्तें अलग-अलग हो सकती हैं और संबंधित प्राधिकरणों द्वारा लागू की जाती हैं।"
        },
        "why": {
            "Useful when the entrepreneur is starting a new eligible micro-enterprise and needs structured project finance.": "जब उद्यमी नया पात्र सूक्ष्म उद्यम शुरू कर रहा हो और उसे संरचित परियोजना वित्त की आवश्यकता हो, तब उपयोगी।",
            "Useful for shops, services, food businesses, livestock-related activities and other eligible micro businesses.": "दुकानों, सेवाओं, खाद्य व्यवसायों, पशुपालन संबंधी गतिविधियों और अन्य पात्र सूक्ष्म व्यवसायों के लिए उपयोगी।",
            "Especially relevant for small street food, vending and mobile retail businesses.": "छोटे स्ट्रीट फूड, वेंडिंग और मोबाइल रिटेल व्यवसायों के लिए विशेष रूप से उपयोगी।",
            "A strong match for spice processing, pickles, snacks, flour, local food products and value-added agricultural produce.": "मसाला प्रसंस्करण, अचार, स्नैक्स, आटा, स्थानीय खाद्य उत्पाद और मूल्यवर्धित कृषि उपज के लिए विशेष रूप से उपयोगी।",
            "Useful when the main business is farming or an eligible allied agricultural activity.": "जब मुख्य व्यवसाय खेती या पात्र संबद्ध कृषि गतिविधि हो, तब उपयोगी।",
            "Useful for storage, grading, primary processing and other eligible agricultural infrastructure.": "भंडारण, ग्रेडिंग, प्राथमिक प्रसंस्करण और अन्य पात्र कृषि अवसंरचना के लिए उपयोगी।",
            "Useful for agriculture advisory, farm services, input-related services and other eligible agri-business models.": "कृषि सलाह, कृषि सेवाओं, इनपुट संबंधी सेवाओं और अन्य पात्र कृषि-व्यवसाय मॉडलों के लिए उपयोगी।",
            "Useful for group enterprises, food processing, handicrafts and other SHG-based rural businesses.": "समूह उद्यमों, खाद्य प्रसंस्करण, हस्तशिल्प और अन्य SHG-आधारित ग्रामीण व्यवसायों के लिए उपयोगी।",
            "Relevant to tailoring and eligible traditional craft/artisan businesses.": "सिलाई और पात्र पारंपरिक कारीगर व्यवसायों के लिए उपयोगी।",
            "Relevant where reliable agricultural energy and irrigation are important to the business model.": "जहाँ विश्वसनीय कृषि ऊर्जा और सिंचाई व्यवसाय मॉडल के लिए महत्वपूर्ण हैं, वहाँ उपयोगी।"
        },
        "source": {
            "KVIC / Ministry of MSME": "KVIC / सूक्ष्म, लघु और मध्यम उद्यम मंत्रालय",
            "Department of Financial Services, Ministry of Finance": "वित्तीय सेवा विभाग, वित्त मंत्रालय",
            "Ministry of Housing & Urban Affairs / Government of India": "आवास और शहरी कार्य मंत्रालय / भारत सरकार",
            "Ministry of Food Processing Industries": "खाद्य प्रसंस्करण उद्योग मंत्रालय",
            "Government of India / Department of Financial Services": "भारत सरकार / वित्तीय सेवा विभाग",
            "Department of Agriculture & Farmers Welfare": "कृषि एवं किसान कल्याण विभाग",
            "MANAGE / Ministry of Agriculture & Farmers Welfare": "MANAGE / कृषि एवं किसान कल्याण मंत्रालय",
            "Ministry of Rural Development": "ग्रामीण विकास मंत्रालय",
            "Government of India": "भारत सरकार",
            "Ministry of New and Renewable Energy": "नवीन और नवीकरणीय ऊर्जा मंत्रालय"
        }
    },
    "Kannada": {
        "key": {
            "For new enterprises; applicant generally must be 18+. Project and eligibility conditions apply.": "ಹೊಸ ಉದ್ಯಮಗಳಿಗೆ; ಅರ್ಜಿದಾರರು ಸಾಮಾನ್ಯವಾಗಿ 18+ ಆಗಿರಬೇಕು. ಯೋಜನೆ ಮತ್ತು ಅರ್ಹತಾ ಷರತ್ತುಗಳು ಅನ್ವಯಿಸುತ್ತವೆ.",
            "Shishu up to ₹50,000; Kishor above ₹50,000 to ₹5 lakh; Tarun above ₹5 lakh to ₹10 lakh; Tarun Plus above ₹10 lakh to ₹20 lakh for eligible repeat borrowers.": "ಶಿಶು ₹50,000 ವರೆಗೆ; ಕಿಶೋರ್ ₹50,000 ಕ್ಕಿಂತ ಹೆಚ್ಚು ₹5 ಲಕ್ಷದವರೆಗೆ; ತರುಣ ₹5 ಲಕ್ಷಕ್ಕಿಂತ ಹೆಚ್ಚು ₹10 ಲಕ್ಷದವರೆಗೆ; ಅರ್ಹ ಮರುಸಾಲಗಾರರಿಗೆ ತರುಣ್ ಪ್ಲಸ್ ₹10 ಲಕ್ಷದಿಂದ ₹20 ಲಕ್ಷದವರೆಗೆ.",
            "Loan tranches can go up to ₹15,000, ₹25,000 and ₹50,000, subject to scheme conditions. Lending period has been extended to March 31, 2030.": "ಯೋಜನೆಯ ಷರತ್ತುಗಳಿಗೆ ಒಳಪಟ್ಟು ಸಾಲದ ಹಂತಗಳು ₹15,000, ₹25,000 ಮತ್ತು ₹50,000 ವರೆಗೆ ಇರಬಹುದು. ಸಾಲ ನೀಡುವ ಅವಧಿಯನ್ನು ಮಾರ್ಚ್ 31, 2030 ರವರೆಗೆ ವಿಸ್ತರಿಸಲಾಗಿದೆ.",
            "Individual micro food-processing units may receive 35% credit-linked capital subsidy up to ₹10 lakh, subject to eligibility and guidelines.": "ಅರ್ಹತೆ ಮತ್ತು ಮಾರ್ಗಸೂಚಿಗಳಿಗೆ ಒಳಪಟ್ಟು ವೈಯಕ್ತಿಕ ಸಣ್ಣ ಆಹಾರ ಸಂಸ್ಕರಣಾ ಘಟಕಗಳಿಗೆ ₹10 ಲಕ್ಷದವರೆಗೆ 35% ಕ್ರೆಡಿಟ್-ಲಿಂಕ್ಡ್ ಬಂಡವಾಳ ಸಬ್ಸಿಡಿ ದೊರೆಯಬಹುದು.",
            "Can support eligible crop and allied agricultural credit requirements through participating financial institutions.": "ಭಾಗವಹಿಸುವ ಹಣಕಾಸು ಸಂಸ್ಥೆಗಳ ಮೂಲಕ ಅರ್ಹ ಬೆಳೆ ಮತ್ತು ಸಂಬಂಧಿತ ಕೃಷಿ ಸಾಲ ಅಗತ್ಯಗಳಿಗೆ ಬೆಂಬಲ ನೀಡಬಹುದು.",
            "Eligible loans can receive interest subvention of 3% per year on the loan component up to ₹2 crore, subject to scheme conditions.": "ಯೋಜನೆಯ ಷರತ್ತುಗಳಿಗೆ ಒಳಪಟ್ಟು ಅರ್ಹ ಸಾಲದ ₹2 ಕೋಟಿವರೆಗಿನ ಸಾಲ ಘಟಕದ ಮೇಲೆ ವರ್ಷಕ್ಕೆ 3% ಬಡ್ಡಿ ಸಹಾಯ ದೊರೆಯಬಹುದು.",
            "Eligibility, training, project cost and subsidy provisions depend on the current ACABC guidelines.": "ಅರ್ಹತೆ, ತರಬೇತಿ, ಯೋಜನಾ ವೆಚ್ಚ ಮತ್ತು ಸಬ್ಸಿಡಿ ನಿಯಮಗಳು ಪ್ರಸ್ತುತ ACABC ಮಾರ್ಗಸೂಚಿಗಳ ಮೇಲೆ ಅವಲಂಬಿತವಾಗಿವೆ.",
            "Support is delivered through the rural livelihood mission structure and applicable state-level mechanisms.": "ಬೆಂಬಲವನ್ನು ಗ್ರಾಮೀಣ ಜೀವನೋಪಾಯ ಮಿಷನ್ ವ್ಯವಸ್ಥೆ ಮತ್ತು ಅನ್ವಯಿಸುವ ರಾಜ್ಯ ಮಟ್ಟದ ವ್ಯವಸ್ಥೆಗಳ ಮೂಲಕ ನೀಡಲಾಗುತ್ತದೆ.",
            "Benefits and eligible trades are subject to the official scheme guidelines.": "ಲಾಭಗಳು ಮತ್ತು ಅರ್ಹ ವೃತ್ತಿಗಳು ಅಧಿಕೃತ ಯೋಜನಾ ಮಾರ್ಗಸೂಚಿಗಳಿಗೆ ಒಳಪಟ್ಟಿರುತ್ತವೆ.",
            "Component, subsidy and implementation conditions vary and are administered through the relevant authorities.": "ಘಟಕ, ಸಬ್ಸಿಡಿ ಮತ್ತು ಅನುಷ್ಠಾನದ ಷರತ್ತುಗಳು ಬದಲಾಗಬಹುದು ಮತ್ತು ಸಂಬಂಧಿತ ಅಧಿಕಾರಿಗಳ ಮೂಲಕ ನಿರ್ವಹಿಸಲಾಗುತ್ತದೆ."
        },
        "why": {
            "Useful when the entrepreneur is starting a new eligible micro-enterprise and needs structured project finance.": "ಉದ್ಯಮಿಯು ಹೊಸ ಅರ್ಹ ಸಣ್ಣ ಉದ್ಯಮವನ್ನು ಆರಂಭಿಸುತ್ತಿರುವಾಗ ಮತ್ತು ಯೋಜಿತ ಹಣಕಾಸಿನ ಅಗತ್ಯವಿರುವಾಗ ಉಪಯುಕ್ತ.",
            "Useful for shops, services, food businesses, livestock-related activities and other eligible micro businesses.": "ಅಂಗಡಿಗಳು, ಸೇವೆಗಳು, ಆಹಾರ ವ್ಯವಹಾರಗಳು, ಜಾನುವಾರು ಸಂಬಂಧಿತ ಚಟುವಟಿಕೆಗಳು ಮತ್ತು ಇತರ ಅರ್ಹ ಸಣ್ಣ ವ್ಯವಹಾರಗಳಿಗೆ ಉಪಯುಕ್ತ.",
            "Especially relevant for small street food, vending and mobile retail businesses.": "ಸಣ್ಣ ಸ್ಟ್ರೀಟ್ ಫುಡ್, ಬೀದಿ ವ್ಯಾಪಾರ ಮತ್ತು ಮೊಬೈಲ್ ಚಿಲ್ಲರೆ ವ್ಯವಹಾರಗಳಿಗೆ ವಿಶೇಷವಾಗಿ ಉಪಯುಕ್ತ.",
            "A strong match for spice processing, pickles, snacks, flour, local food products and value-added agricultural produce.": "ಮಸಾಲೆ ಸಂಸ್ಕರಣೆ, ಉಪ್ಪಿನಕಾಯಿ, ತಿಂಡಿಗಳು, ಹಿಟ್ಟು, ಸ್ಥಳೀಯ ಆಹಾರ ಉತ್ಪನ್ನಗಳು ಮತ್ತು ಮೌಲ್ಯವರ್ಧಿತ ಕೃಷಿ ಉತ್ಪನ್ನಗಳಿಗೆ ಉತ್ತಮವಾಗಿ ಹೊಂದಿಕೊಳ್ಳುತ್ತದೆ.",
            "Useful when the main business is farming or an eligible allied agricultural activity.": "ಮುಖ್ಯ ವ್ಯವಹಾರ ಕೃಷಿ ಅಥವಾ ಅರ್ಹ ಸಂಬಂಧಿತ ಕೃಷಿ ಚಟುವಟಿಕೆಯಾಗಿರುವಾಗ ಉಪಯುಕ್ತ.",
            "Useful for storage, grading, primary processing and other eligible agricultural infrastructure.": "ಸಂಗ್ರಹಣೆ, ವರ್ಗೀಕರಣ, ಪ್ರಾಥಮಿಕ ಸಂಸ್ಕರಣೆ ಮತ್ತು ಇತರ ಅರ್ಹ ಕೃಷಿ ಮೂಲಸೌಕರ್ಯಗಳಿಗೆ ಉಪಯುಕ್ತ.",
            "Useful for agriculture advisory, farm services, input-related services and other eligible agri-business models.": "ಕೃಷಿ ಸಲಹೆ, ಕೃಷಿ ಸೇವೆಗಳು, ಇನ್‌ಪುಟ್ ಸಂಬಂಧಿತ ಸೇವೆಗಳು ಮತ್ತು ಇತರ ಅರ್ಹ ಕೃಷಿ ವ್ಯವಹಾರ ಮಾದರಿಗಳಿಗೆ ಉಪಯುಕ್ತ.",
            "Useful for group enterprises, food processing, handicrafts and other SHG-based rural businesses.": "ಗುಂಪು ಉದ್ಯಮಗಳು, ಆಹಾರ ಸಂಸ್ಕರಣೆ, ಕರಕುಶಲ ಮತ್ತು ಇತರ SHG ಆಧಾರಿತ ಗ್ರಾಮೀಣ ವ್ಯವಹಾರಗಳಿಗೆ ಉಪಯುಕ್ತ.",
            "Relevant to tailoring and eligible traditional craft/artisan businesses.": "ಹೊಲಿಗೆ ಮತ್ತು ಅರ್ಹ ಸಾಂಪ್ರದಾಯಿಕ ಕರಕುಶಲ/ಕುಶಲಕರ್ಮಿ ವ್ಯವಹಾರಗಳಿಗೆ ಸಂಬಂಧಿಸಿದೆ.",
            "Relevant where reliable agricultural energy and irrigation are important to the business model.": "ವಿಶ್ವಾಸಾರ್ಹ ಕೃಷಿ ಶಕ್ತಿ ಮತ್ತು ನೀರಾವರಿ ವ್ಯವಹಾರ ಮಾದರಿಗೆ ಮುಖ್ಯವಾಗಿರುವಲ್ಲಿ ಉಪಯುಕ್ತ."
        },
        "source": {
            "KVIC / Ministry of MSME": "KVIC / ಸೂಕ್ಷ್ಮ, ಸಣ್ಣ ಮತ್ತು ಮಧ್ಯಮ ಉದ್ಯಮಗಳ ಸಚಿವಾಲಯ",
            "Department of Financial Services, Ministry of Finance": "ಹಣಕಾಸು ಸೇವೆಗಳ ಇಲಾಖೆ, ಹಣಕಾಸು ಸಚಿವಾಲಯ",
            "Ministry of Housing & Urban Affairs / Government of India": "ವಸತಿ ಮತ್ತು ನಗರ ವ್ಯವಹಾರಗಳ ಸಚಿವಾಲಯ / ಭಾರತ ಸರ್ಕಾರ",
            "Ministry of Food Processing Industries": "ಆಹಾರ ಸಂಸ್ಕರಣಾ ಕೈಗಾರಿಕೆಗಳ ಸಚಿವಾಲಯ",
            "Government of India / Department of Financial Services": "ಭಾರತ ಸರ್ಕಾರ / ಹಣಕಾಸು ಸೇವೆಗಳ ಇಲಾಖೆ",
            "Department of Agriculture & Farmers Welfare": "ಕೃಷಿ ಮತ್ತು ರೈತರ ಕಲ್ಯಾಣ ಇಲಾಖೆ",
            "MANAGE / Ministry of Agriculture & Farmers Welfare": "MANAGE / ಕೃಷಿ ಮತ್ತು ರೈತರ ಕಲ್ಯಾಣ ಸಚಿವಾಲಯ",
            "Ministry of Rural Development": "ಗ್ರಾಮೀಣ ಅಭಿವೃದ್ಧಿ ಸಚಿವಾಲಯ",
            "Government of India": "ಭಾರತ ಸರ್ಕಾರ",
            "Ministry of New and Renewable Energy": "ಹೊಸ ಮತ್ತು ನವೀಕರಿಸಬಹುದಾದ ಇಂಧನ ಸಚಿವಾಲಯ"
        }
    }
}


def stext(kind, value):
    """Return translated government-scheme text for the selected language."""
    return SCHEME_TR.get(language, {}).get(kind, {}).get(value, value)


def scheme_extra(kind, value):
    """Return translated scheme key/reason/source text for the selected language."""
    return SCHEME_EXTRA_TR.get(language, {}).get(kind, {}).get(value, value)





# ============================================================
# GOVERNMENT SCHEMES
# ============================================================

def scheme_name(value):
    """Return the translated display name for a government scheme."""
    return SCHEME_NAME_TR.get(language, {}).get(value, value)


SCHEMES = [
    {
        "name": "PMEGP – Prime Minister's Employment Generation Programme",
        "best_for": "New micro-enterprises in manufacturing and eligible service/non-farm activities.",
        "description": "A credit-linked government programme that supports new micro-enterprises through bank finance and margin-money subsidy. It is designed to create self-employment and employment opportunities, especially for rural and aspiring entrepreneurs.",
        "key": "For new enterprises; applicant generally must be 18+. Project and eligibility conditions apply.",
        "why": "Useful when the entrepreneur is starting a new eligible micro-enterprise and needs structured project finance.",
        "source": "KVIC / Ministry of MSME"
    },
    {
        "name": "Pradhan Mantri MUDRA Yojana (PMMY)",
        "best_for": "Small businesses needing working capital or business expansion finance.",
        "description": "Provides collateral-free institutional credit for eligible micro enterprises in manufacturing, trading, services and allied agricultural activities.",
        "key": "Shishu up to ₹50,000; Kishor above ₹50,000 to ₹5 lakh; Tarun above ₹5 lakh to ₹10 lakh; Tarun Plus above ₹10 lakh to ₹20 lakh for eligible repeat borrowers.",
        "why": "Useful for shops, services, food businesses, livestock-related activities and other eligible micro businesses.",
        "source": "Department of Financial Services, Ministry of Finance"
    },
    {
        "name": "PM SVANidhi",
        "best_for": "Eligible street vendors.",
        "description": "A micro-credit and support programme for street vendors. The restructured scheme includes progressive working-capital loans, digital adoption incentives and broader livelihood support.",
        "key": "Loan tranches can go up to ₹15,000, ₹25,000 and ₹50,000, subject to scheme conditions. Lending period has been extended to March 31, 2030.",
        "why": "Especially relevant for small street food, vending and mobile retail businesses.",
        "source": "Ministry of Housing & Urban Affairs / Government of India"
    },
    {
        "name": "PMFME – Pradhan Mantri Formalisation of Micro Food Processing Enterprises",
        "best_for": "Micro food-processing businesses and eligible SHGs/FPOs/cooperatives.",
        "description": "Supports formalisation, upgrading and capacity building for micro food-processing enterprises. Eligible individual units can receive credit-linked capital subsidy subject to scheme conditions.",
        "key": "Individual micro food-processing units may receive 35% credit-linked capital subsidy up to ₹10 lakh, subject to eligibility and guidelines.",
        "why": "A strong match for spice processing, pickles, snacks, flour, local food products and value-added agricultural produce.",
        "source": "Ministry of Food Processing Industries"
    },
    {
        "name": "Kisan Credit Card (KCC)",
        "best_for": "Farmers and eligible agricultural/allied activities.",
        "description": "Provides formal credit access for agricultural and allied working-capital needs, subject to lending and eligibility conditions.",
        "key": "Can support eligible crop and allied agricultural credit requirements through participating financial institutions.",
        "why": "Useful when the main business is farming or an eligible allied agricultural activity.",
        "source": "Government of India / Department of Financial Services"
    },
    {
        "name": "Agriculture Infrastructure Fund (AIF)",
        "best_for": "Post-harvest infrastructure and eligible community farming assets.",
        "description": "Provides financing support for eligible agriculture infrastructure such as post-harvest management and community farming assets.",
        "key": "Eligible loans can receive interest subvention of 3% per year on the loan component up to ₹2 crore, subject to scheme conditions.",
        "why": "Useful for storage, grading, primary processing and other eligible agricultural infrastructure.",
        "source": "Department of Agriculture & Farmers Welfare"
    },
    {
        "name": "Agri-Clinics and Agri-Business Centres (ACABC)",
        "best_for": "Eligible agriculture-trained entrepreneurs providing farm-related services.",
        "description": "Supports trained agricultural professionals/eligible candidates in setting up agri-clinics and agri-business centres that provide advisory and agricultural services to farmers.",
        "key": "Eligibility, training, project cost and subsidy provisions depend on the current ACABC guidelines.",
        "why": "Useful for agriculture advisory, farm services, input-related services and other eligible agri-business models.",
        "source": "MANAGE / Ministry of Agriculture & Farmers Welfare"
    },
    {
        "name": "DAY-NRLM – Deendayal Antyodaya Yojana",
        "best_for": "Rural women-led Self Help Groups and rural livelihoods.",
        "description": "A rural livelihoods programme that works through Self Help Groups and community institutions to improve access to finance, skills, enterprise support and sustainable livelihoods.",
        "key": "Support is delivered through the rural livelihood mission structure and applicable state-level mechanisms.",
        "why": "Useful for group enterprises, food processing, handicrafts and other SHG-based rural businesses.",
        "source": "Ministry of Rural Development"
    },
    {
        "name": "PM Vishwakarma",
        "best_for": "Eligible traditional artisans and craftspeople.",
        "description": "Supports eligible traditional artisans and craftspeople with recognition, skill development, toolkit support, credit and market-oriented assistance under the scheme.",
        "key": "Benefits and eligible trades are subject to the official scheme guidelines.",
        "why": "Relevant to tailoring and eligible traditional craft/artisan businesses.",
        "source": "Government of India"
    },
    {
        "name": "PM-KUSUM",
        "best_for": "Eligible farmers and agricultural energy/solar applications.",
        "description": "Supports solar-energy-related interventions in agriculture, including eligible solar pumps and other components under the scheme.",
        "key": "Component, subsidy and implementation conditions vary and are administered through the relevant authorities.",
        "why": "Relevant where reliable agricultural energy and irrigation are important to the business model.",
        "source": "Ministry of New and Renewable Energy"
    }
] 

# ------------------------------------------------------------
# SCHEME ELIGIBILITY + DOCUMENTS
# The information below is a concise prototype summary based on
# official government scheme material. Requirements can vary by
# applicant, lender, state and current guidelines.
# ------------------------------------------------------------
SCHEME_DETAILS = {
    "PMEGP": {
        "eligibility": "Generally for individuals aged 18+ starting a new eligible micro-enterprise. For projects above the prescribed PMEGP thresholds, minimum educational qualification conditions apply. Existing units are generally not eligible except specified cases under the scheme guidelines.",
        "documents": [
            "Aadhaar card",
            "Passport-size photographs",
            "Caste / special-category certificate, if applicable",
            "Rural-area certificate, if applicable",
            "Highest educational qualification certificate, where applicable",
            "EDP / skill-development training certificate, if completed",
            "Project report",
            "Other documents requested during application or bank appraisal"
        ]
    },
    "MUDRA": {
        "eligibility": "Eligible non-corporate micro enterprises in manufacturing, trading, services and allied agricultural activities such as dairy, poultry and beekeeping. Both new and existing eligible businesses may be considered subject to lender assessment.",
        "documents": [
            "Identity proof",
            "Address proof",
            "Passport-size photograph",
            "Applicant signature",
            "Business / enterprise proof and address, where applicable",
            "Bank account / financial information as requested by the lender",
            "Business plan / project details, where requested",
            "Any additional documents required by the lending institution"
        ]
    },
    "PM SVANidhi": {
        "eligibility": "Eligible street vendors, including surveyed vendors and eligible vendors who can obtain a Certificate/ID of Vending or Letter of Recommendation through the prescribed process.",
        "documents": [
            "Certificate of Vending / vendor ID, or Letter of Recommendation where applicable",
            "Aadhaar card",
            "Voter ID, Driving Licence, MNREGA card or PAN as applicable",
            "Vendor-related proof where required",
            "Bank account details / KYC documents",
            "Any additional document requested by the lending or local authority"
        ]
    },
    "PMFME": {
        "eligibility": "Eligible micro food-processing enterprises and other eligible categories under PMFME. For individual units, the scheme guidelines include conditions such as age, ownership, micro-enterprise status, contribution and eligible food-processing activity.",
        "documents": [
            "PAN card",
            "Aadhaar copy and photograph of promoters / guarantors as applicable",
            "Address proof",
            "Proof of site ownership / rent / lease",
            "Recent bank statement / passbook",
            "Machinery and equipment estimates / quotations",
            "Project report / DPR where applicable",
            "Education or other supporting documents where applicable"
        ]
    },
    "Kisan Credit Card": {
        "eligibility": "Farmers including owner cultivators, eligible tenant farmers, oral lessees and sharecroppers; eligible SHGs/JLGs of farmers may also qualify, subject to bank and scheme conditions.",
        "documents": [
            "KCC application form",
            "Passport-size photographs",
            "Identity proof such as Aadhaar / Driving Licence / Voter ID / Passport",
            "Address proof",
            "Certified proof of landholding, where applicable",
            "Cropping pattern and acreage",
            "Security documents if applicable to the loan limit",
            "Any other document required by the bank"
        ]
    },
    "Agriculture Infrastructure Fund": {
        "eligibility": "Eligible beneficiaries may include farmers, FPOs, PACS, SHGs, agri-entrepreneurs and other eligible entities undertaking permitted agriculture infrastructure projects, subject to the current AIF guidelines and lender appraisal.",
        "documents": [
            "Aadhaar / identity documents of promoters",
            "PAN details",
            "Bank and existing credit-facility details",
            "Land / site ownership or lease documents, where applicable",
            "Project report / DPR",
            "Entity registration documents, if applicable",
            "Financial statements / GST information, where applicable",
            "Project-specific documents requested by the lender"
        ]
    },
    "ACABC": {
        "eligibility": "Primarily for eligible agriculture and allied-sector graduates / qualified candidates who complete the prescribed training and establish eligible Agri-Clinic or Agri-Business Centre activities under current ACABC guidelines.",
        "documents": [
            "Aadhaar / identity proof",
            "Educational qualification / agriculture or allied-sector certificate",
            "Training certificate, where applicable",
            "PAN and bank details",
            "Project report / business plan",
            "Land / premises or project-related documents, where applicable",
            "Any documents requested by the training institute, nodal agency or bank"
        ]
    },
    "DAY-NRLM": {
        "eligibility": "Rural livelihood support is delivered mainly through eligible Self Help Groups, their federations and community institutions under the applicable state rural livelihood mission structure.",
        "documents": [
            "Aadhaar / identity documents of members as applicable",
            "SHG / group records and registration details, where applicable",
            "Bank account details",
            "Group resolution / meeting records, where required",
            "Business or livelihood plan, where applicable",
            "Any state-level documents required by the rural livelihood mission"
        ]
    },
    "PM Vishwakarma": {
        "eligibility": "Eligible traditional artisans and craftspeople working in notified trades, subject to the scheme's age, family, occupation and other conditions.",
        "documents": [
            "Aadhaar card / Aadhaar-linked mobile details",
            "Basic identity and address information",
            "Bank account details",
            "Trade / artisan details and self-declaration as required",
            "Any verification or supporting document requested through the official registration process"
        ]
    },
    "PM-KUSUM": {
        "eligibility": "Eligible farmers and other permitted agricultural-energy beneficiaries for the relevant PM-KUSUM component, subject to component, state and implementation conditions.",
        "documents": [
            "Aadhaar / identity proof",
            "Land ownership / lease or project-site proof, where applicable",
            "Bank account details",
            "Agricultural / pump / electricity-related details as applicable",
            "Quotation or project documents where required",
            "Any additional documents requested by the implementing authority"
        ]
    }
}

SCHEME_CODE_TO_NAME = {
    "PMEGP": "PMEGP – Prime Minister's Employment Generation Programme",
    "MUDRA": "Pradhan Mantri MUDRA Yojana (PMMY)",
    "PM SVANidhi": "PM SVANidhi",
    "PMFME": "PMFME – Pradhan Mantri Formalisation of Micro Food Processing Enterprises",
    "Kisan Credit Card": "Kisan Credit Card (KCC)",
    "Agriculture Infrastructure Fund": "Agriculture Infrastructure Fund (AIF)",
    "ACABC": "Agri-Clinics and Agri-Business Centres (ACABC)",
    "DAY-NRLM": "DAY-NRLM – Deendayal Antyodaya Yojana",
    "PM Vishwakarma": "PM Vishwakarma",
    "PM-KUSUM": "PM-KUSUM"
}

def get_scheme_details(scheme_code_or_name):
    for code, details in SCHEME_DETAILS.items():
        if scheme_code_or_name == code or code in scheme_code_or_name:
            return details
    return None

# ============================================================
# HELPER FUNCTIONS
# ============================================================

def money(value):
    return f"₹{value:,.0f}"

def calculate_match(business, capital, resources, interest, water, experience, location):
    score = 0
    reasons = []

    low, high = business["capital"]

    # Capital fit
    if capital >= high:
        score += 30
        reasons.append("Your available capital comfortably covers the indicative investment range.")
    elif capital >= low:
        score += 25
        reasons.append("Your capital fits the lower-to-middle part of the indicative investment range.")
    elif capital >= low * 0.5:
        score += 12
        reasons.append("Your capital is below the typical starting range, so a smaller pilot may be needed.")
    else:
        score += 3
        reasons.append("Capital is currently limited for this model.")

    # Multiple-resource fit
    selected_resources = [
        r for r in resources
        if r != "Not sure / I have limited resources"
    ]
    business_resources = business["resources"]

    selected_lower = {r.lower() for r in selected_resources}
    matched = [r for r in business_resources if r.lower() in selected_lower]
    missing = [r for r in business_resources if r.lower() not in selected_lower]

    if matched:
        resource_score = round(20 * len(matched) / len(business_resources))
        score += resource_score
        reasons.append(
            "Matched resources: " + ", ".join(matched) + "."
        )
    elif not selected_resources:
        score += 3
        reasons.append("No specific resource was selected, so additional resources may be needed.")
    else:
        score += 5
        reasons.append("Your selected resources do not directly cover the main resources for this model.")

    if missing and matched:
        reasons.append(
            "Additional resources may be needed: " + ", ".join(missing) + "."
        )

    # Interest fit
    interest_lower = interest.lower()
    if any(x.lower() in interest_lower for x in business["interests"]):
        score += 20
        reasons.append("The business matches your stated interest.")
    else:
        score += 7

    # Water fit is derived from the selected location, not entered by the user.
    local_water = location_water(location)
    if "Water" in business["resources"] or "water" in business["name"].lower():
        if local_water == "Good":
            score += 10
            reasons.append(f"{location} has a prototype-rated good water context for this model.")
        elif local_water == "Medium":
            score += 7
            reasons.append(f"{location} has a prototype-rated medium water context; irrigation planning is important.")
        else:
            score += 3
            reasons.append(f"{location} has a prototype-rated limited water context; choose a water-efficient model or irrigation plan.")
    else:
        score += 8

    # Experience
    if experience == "Some experience":
        score += 10
        reasons.append("Your existing experience reduces the learning curve.")
    elif experience == "Experienced":
        score += 10
        reasons.append("Your experience is a strong fit for execution.")
    else:
        score += 5
        reasons.append("A small pilot and basic training are recommended before scaling.")

    # Location
    if location in business["locations"]:
        score += 10
        reasons.append(f"{location} is included in the prototype's suitable-location profile.")
    else:
        score += 5

    return min(score, 100), reasons


def scheme_for_business(business):
    return business["schemes"]





# Global copies used by Smart Action Plan so its compare/profile UI
# is translated even when the Business Recommendation page has not run.
P1_BUSINESS_CONTENT_TR = {'Hindi': {'investment': {'₹25,000 – ₹2.5 lakh': '₹25,000 – ₹2.5 लाख',
                          '₹75,000 – ₹10 lakh+': '₹75,000 – ₹10 लाख+',
                          '₹1 lakh – ₹7 lakh': '₹1 लाख – ₹7 लाख',
                          '₹30,000 – ₹3 lakh': '₹30,000 – ₹3 लाख',
                          '₹1 lakh – ₹8 lakh': '₹1 लाख – ₹8 लाख',
                          '₹60,000 – ₹5 lakh': '₹60,000 – ₹5 लाख',
                          '₹80,000 – ₹6 lakh': '₹80,000 – ₹6 लाख',
                          '₹75,000 – ₹6 lakh': '₹75,000 – ₹6 लाख',
                          '₹30,000 – ₹2.5 lakh': '₹30,000 – ₹2.5 लाख',
                          '₹25,000 – ₹3 lakh': '₹25,000 – ₹3 लाख',
                          '₹1.5 lakh – ₹10 lakh+': '₹1.5 लाख – ₹10 लाख+',
                          '₹40,000 – ₹3 lakh': '₹40,000 – ₹3 लाख'},
           'model': {'Grow vegetables → sell to local markets, retailers, hotels or direct customers.': 'सब्ज़ियाँ उगाएँ → स्थानीय बाजारों, खुदरा विक्रेताओं, '
                                                                                                        'होटलों या सीधे ग्राहकों को बेचें।',
                     'Convert local produce into higher-value products such as flour, snacks, pickles, spice mixes or packaged foods.': 'स्थानीय उपज को आटा, '
                                                                                                                                        'स्नैक्स, अचार, मसाला '
                                                                                                                                        'मिश्रण या पैकेज्ड '
                                                                                                                                        'खाद्य जैसे अधिक मूल्य '
                                                                                                                                        'वाले उत्पादों में '
                                                                                                                                        'बदलें।',
                     'Sell essential household products with repeat local demand.': 'नियमित स्थानीय मांग वाले आवश्यक घरेलू उत्पाद बेचें।',
                     'Sell affordable snacks or meals at a high-footfall local location.': 'अधिक ग्राहक आने वाली स्थानीय जगह पर किफायती स्नैक्स या भोजन बेचें।',
                     'Milk production with possible value addition such as curd, paneer or ghee.': 'दूध का उत्पादन करें और दही, पनीर या घी जैसे मूल्यवर्धित '
                                                                                                   'उत्पाद बनाएं।',
                     'Rear animals for meat, breeding or local livestock markets.': 'मांस, प्रजनन या स्थानीय पशु बाजारों के लिए पशुओं का पालन करें।',
                     'Egg or broiler production for nearby markets.': 'नजदीकी बाजारों के लिए अंडे या ब्रॉयलर का उत्पादन करें।',
                     'Deliver groceries, farm inputs, medicines or local goods within nearby villages/towns.': 'नजदीकी गांवों/कस्बों में किराना, कृषि इनपुट, '
                                                                                                               'दवाइयाँ या स्थानीय सामान पहुँचाएँ।',
                     'Alterations, stitching, school uniforms, traditional clothing and small-batch garments.': 'कपड़ों की अल्टरशन, सिलाई, स्कूल यूनिफॉर्म, '
                                                                                                                'पारंपरिक कपड़े और छोटे बैच के परिधान तैयार '
                                                                                                                'करें।',
                     'Make baskets, decor, traditional products or locally distinctive handmade goods.': 'टोकरी, सजावटी सामान, पारंपरिक उत्पाद या स्थानीय '
                                                                                                         'विशेषता वाले हस्तनिर्मित सामान बनाएँ।',
                     'Supply seeds, tools, irrigation accessories and farm-related services.': 'बीज, उपकरण, सिंचाई सामग्री और कृषि संबंधी सेवाएँ उपलब्ध कराएँ।',
                     'Repair phones, appliances, agricultural equipment or other locally needed items.': 'मोबाइल, उपकरण, कृषि मशीनरी या स्थानीय रूप से आवश्यक '
                                                                                                         'अन्य वस्तुओं की मरम्मत करें।'},
           'risk': {'Weather, water availability and price fluctuations.': 'मौसम, पानी की उपलब्धता और कीमतों में उतार-चढ़ाव।',
                    'Food safety, packaging, shelf life and market access.': 'खाद्य सुरक्षा, पैकेजिंग, शेल्फ लाइफ और बाजार तक पहुँच।',
                    'Competition, inventory management and credit sales.': 'प्रतिस्पर्धा, स्टॉक प्रबंधन और उधार बिक्री।',
                    'Location dependency, hygiene and daily demand variation.': 'स्थान पर निर्भरता, स्वच्छता और दैनिक मांग में बदलाव।',
                    'Animal health, feed costs and milk-price changes.': 'पशु स्वास्थ्य, चारे की लागत और दूध की कीमतों में बदलाव।',
                    'Disease, feed costs and market-price fluctuations.': 'बीमारी, चारे की लागत और बाजार कीमतों में उतार-चढ़ाव।',
                    'Feed costs, disease and price volatility.': 'चारे की लागत, बीमारी और कीमतों में अस्थिरता।',
                    'Fuel costs, vehicle maintenance and route density.': 'ईंधन की लागत, वाहन रखरखाव और मार्ग की मांग।',
                    'Competition and seasonal demand.': 'प्रतिस्पर्धा और मौसमी मांग।',
                    'Demand discovery and inconsistent order volume.': 'मांग का पता लगाना और ऑर्डर की मात्रा में अस्थिरता।',
                    'Inventory, licensing requirements and seasonal demand.': 'स्टॉक, लाइसेंस की आवश्यकताएँ और मौसमी मांग।',
                    'Skill dependency and availability of spare parts.': 'कौशल पर निर्भरता और स्पेयर पार्ट्स की उपलब्धता।'},
           'steps': {'Select crops based on local demand and water availability.': 'स्थानीय मांग और पानी की उपलब्धता के आधार पर फसलें चुनें।',
                     'Estimate seed, labour, irrigation and transport costs.': 'बीज, श्रम, सिंचाई और परिवहन की लागत का अनुमान लगाएँ।',
                     'Plan more than one sales channel instead of depending on a single buyer.': 'एक ही खरीदार पर निर्भर रहने के बजाय एक से अधिक बिक्री चैनल '
                                                                                                 'रखें।',
                     'Choose one product with a clear local customer segment.': 'स्पष्ट स्थानीय ग्राहक वर्ग वाला एक उत्पाद चुनें।',
                     'Calculate raw material, packaging, labour and selling costs.': 'कच्चे माल, पैकेजिंग, श्रम और बिक्री लागत की गणना करें।',
                     'Test a small batch before investing in larger equipment.': 'बड़े उपकरणों में निवेश करने से पहले छोटे बैच का परीक्षण करें।',
                     'Start with fast-moving essentials instead of excessive inventory.': 'अधिक स्टॉक रखने के बजाय तेजी से बिकने वाली आवश्यक वस्तुओं से शुरुआत '
                                                                                          'करें।',
                     'Track daily sales and stock movement.': 'दैनिक बिक्री और स्टॉक की आवाजाही का रिकॉर्ड रखें।',
                     'Add high-demand local products after observing customer behaviour.': 'ग्राहकों के व्यवहार को देखकर अधिक मांग वाले स्थानीय उत्पाद जोड़ें।',
                     'Choose a small menu with good margins.': 'अच्छे मार्जिन वाला छोटा मेन्यू चुनें।',
                     'Test demand at different times of the day.': 'दिन के अलग-अलग समय पर मांग का परीक्षण करें।',
                     'Maintain hygiene, consistent quality and simple bookkeeping.': 'स्वच्छता, समान गुणवत्ता और सरल लेखा-जोखा बनाए रखें।',
                     'Estimate feed and veterinary costs before buying animals.': 'पशु खरीदने से पहले चारे और पशु चिकित्सा की लागत का अनुमान लगाएँ।',
                     'Identify a reliable local milk buyer.': 'एक भरोसेमंद स्थानीय दूध खरीदार की पहचान करें।',
                     'Maintain records of milk yield and animal health.': 'दूध उत्पादन और पशु स्वास्थ्य का रिकॉर्ड रखें।',
                     'Start with a manageable herd size.': 'संभालने योग्य झुंड के आकार से शुरुआत करें।',
                     'Plan vaccination and veterinary care.': 'टीकाकरण और पशु चिकित्सा देखभाल की योजना बनाएँ।',
                     'Build a buyer network before scaling.': 'विस्तार करने से पहले खरीदारों का नेटवर्क बनाएँ।',
                     'Choose egg or meat production based on local demand.': 'स्थानीय मांग के आधार पर अंडा या मांस उत्पादन चुनें।',
                     'Calculate feed cost per bird.': 'प्रति पक्षी चारे की लागत की गणना करें।',
                     'Maintain biosecurity and veterinary schedules.': 'जैव-सुरक्षा और पशु चिकित्सा कार्यक्रम बनाए रखें।',
                     'Map villages and shops that need regular delivery.': 'नियमित डिलीवरी की जरूरत वाले गांवों और दुकानों की सूची बनाएँ।',
                     'Start with a defined service radius.': 'एक निश्चित सेवा क्षेत्र से शुरुआत करें।',
                     'Use simple digital records for orders, fuel and collections.': 'ऑर्डर, ईंधन और भुगतान संग्रह के लिए सरल डिजिटल रिकॉर्ड रखें।',
                     'Start with alterations and high-demand local garments.': 'अल्टरशन और अधिक मांग वाले स्थानीय परिधानों से शुरुआत करें।',
                     'Build repeat customers through reliable delivery.': 'विश्वसनीय सेवा देकर नियमित ग्राहकों का आधार बनाएँ।',
                     'Add machines only when order volume justifies them.': 'ऑर्डर की मात्रा पर्याप्त होने पर ही मशीनें बढ़ाएँ।',
                     'Create a small catalogue and sample products.': 'एक छोटा कैटलॉग और नमूना उत्पाद तैयार करें।',
                     'Explore local fairs, retailers and digital selling channels.': 'स्थानीय मेलों, खुदरा विक्रेताओं और डिजिटल बिक्री चैनलों का उपयोग करें।',
                     'Identify the crops and farm needs of nearby villages.': 'नजदीकी गांवों की फसलों और कृषि जरूरतों की पहचान करें।',
                     'Stock fast-moving inputs first.': 'पहले तेजी से बिकने वाले कृषि इनपुट रखें।',
                     'Follow all applicable licences and quality requirements.': 'सभी लागू लाइसेंस और गुणवत्ता आवश्यकताओं का पालन करें।',
                     'Choose one repair category based on local demand.': 'स्थानीय मांग के आधार पर एक मरम्मत श्रेणी चुनें।',
                     'Keep commonly required spare parts.': 'आमतौर पर आवश्यक स्पेयर पार्ट्स रखें।',
                     'Build trust through transparent pricing and service records.': 'पारदर्शी कीमत और सेवा रिकॉर्ड के माध्यम से भरोसा बनाएँ।'}},
 'Kannada': {'investment': {'₹25,000 – ₹2.5 lakh': '₹25,000 – ₹2.5 ಲಕ್ಷ',
                            '₹75,000 – ₹10 lakh+': '₹75,000 – ₹10 ಲಕ್ಷ+',
                            '₹1 lakh – ₹7 lakh': '₹1 ಲಕ್ಷ – ₹7 ಲಕ್ಷ',
                            '₹30,000 – ₹3 lakh': '₹30,000 – ₹3 ಲಕ್ಷ',
                            '₹1 lakh – ₹8 lakh': '₹1 ಲಕ್ಷ – ₹8 ಲಕ್ಷ',
                            '₹60,000 – ₹5 lakh': '₹60,000 – ₹5 ಲಕ್ಷ',
                            '₹80,000 – ₹6 lakh': '₹80,000 – ₹6 ಲಕ್ಷ',
                            '₹75,000 – ₹6 lakh': '₹75,000 – ₹6 ಲಕ್ಷ',
                            '₹30,000 – ₹2.5 lakh': '₹30,000 – ₹2.5 ಲಕ್ಷ',
                            '₹25,000 – ₹3 lakh': '₹25,000 – ₹3 ಲಕ್ಷ',
                            '₹1.5 lakh – ₹10 lakh+': '₹1.5 ಲಕ್ಷ – ₹10 ಲಕ್ಷ+',
                            '₹40,000 – ₹3 lakh': '₹40,000 – ₹3 ಲಕ್ಷ'},
             'model': {'Grow vegetables → sell to local markets, retailers, hotels or direct customers.': 'ತರಕಾರಿಗಳನ್ನು ಬೆಳೆಸಿ → ಸ್ಥಳೀಯ ಮಾರುಕಟ್ಟೆಗಳು, ಚಿಲ್ಲರೆ '
                                                                                                          'ವ್ಯಾಪಾರಿಗಳು, ಹೋಟೆಲ್\u200cಗಳು ಅಥವಾ ನೇರ ಗ್ರಾಹಕರಿಗೆ '
                                                                                                          'ಮಾರಾಟ ಮಾಡಿ.',
                       'Convert local produce into higher-value products such as flour, snacks, pickles, spice mixes or packaged foods.': 'ಸ್ಥಳೀಯ '
                                                                                                                                          'ಉತ್ಪನ್ನಗಳನ್ನು '
                                                                                                                                          'ಹಿಟ್ಟು, ತಿಂಡಿಗಳು, '
                                                                                                                                          'ಉಪ್ಪಿನಕಾಯಿ, ಮಸಾಲೆ '
                                                                                                                                          'ಮಿಶ್ರಣಗಳು ಅಥವಾ '
                                                                                                                                          'ಪ್ಯಾಕೇಜ್ ಮಾಡಿದ '
                                                                                                                                          'ಆಹಾರದಂತಹ ಹೆಚ್ಚಿನ '
                                                                                                                                          'ಮೌಲ್ಯದ ಉತ್ಪನ್ನಗಳಾಗಿ '
                                                                                                                                          'ಪರಿವರ್ತಿಸಿ.',
                       'Sell essential household products with repeat local demand.': 'ನಿರಂತರ ಸ್ಥಳೀಯ ಬೇಡಿಕೆಯಿರುವ ಅಗತ್ಯ ಗೃಹೋಪಯೋಗಿ ಉತ್ಪನ್ನಗಳನ್ನು ಮಾರಾಟ ಮಾಡಿ.',
                       'Sell affordable snacks or meals at a high-footfall local location.': 'ಹೆಚ್ಚು ಜನ ಸಂಚಾರವಿರುವ ಸ್ಥಳದಲ್ಲಿ ಕೈಗೆಟುಕುವ ತಿಂಡಿಗಳು ಅಥವಾ ಊಟವನ್ನು '
                                                                                             'ಮಾರಾಟ ಮಾಡಿ.',
                       'Milk production with possible value addition such as curd, paneer or ghee.': 'ಹಾಲು ಉತ್ಪಾದಿಸಿ ಮತ್ತು ಮೊಸರು, ಪನೀರ್ ಅಥವಾ ತುಪ್ಪದಂತಹ '
                                                                                                     'ಮೌಲ್ಯವರ್ಧಿತ ಉತ್ಪನ್ನಗಳನ್ನು ತಯಾರಿಸಿ.',
                       'Rear animals for meat, breeding or local livestock markets.': 'ಮಾಂಸ, ಸಂತಾನೋತ್ಪತ್ತಿ ಅಥವಾ ಸ್ಥಳೀಯ ಜಾನುವಾರು ಮಾರುಕಟ್ಟೆಗಳಿಗಾಗಿ ಪ್ರಾಣಿಗಳನ್ನು '
                                                                                      'ಸಾಕಿ.',
                       'Egg or broiler production for nearby markets.': 'ಹತ್ತಿರದ ಮಾರುಕಟ್ಟೆಗಳಿಗಾಗಿ ಮೊಟ್ಟೆ ಅಥವಾ ಬ್ರಾಯ್ಲರ್ ಉತ್ಪಾದನೆ ಮಾಡಿ.',
                       'Deliver groceries, farm inputs, medicines or local goods within nearby villages/towns.': 'ಹತ್ತಿರದ ಗ್ರಾಮಗಳು/ಪಟ್ಟಣಗಳಲ್ಲಿ ದಿನಸಿ, ಕೃಷಿ '
                                                                                                                 'ಇನ್\u200cಪುಟ್\u200cಗಳು, ಔಷಧಿಗಳು ಅಥವಾ ಸ್ಥಳೀಯ '
                                                                                                                 'ಸರಕುಗಳನ್ನು ವಿತರಿಸಿ.',
                       'Alterations, stitching, school uniforms, traditional clothing and small-batch garments.': 'ಬಟ್ಟೆ ಬದಲಾವಣೆ, ಹೊಲಿಗೆ, ಶಾಲಾ ಸಮವಸ್ತ್ರ, '
                                                                                                                  'ಸಾಂಪ್ರದಾಯಿಕ ಉಡುಪುಗಳು ಮತ್ತು ಸಣ್ಣ ಪ್ರಮಾಣದ '
                                                                                                                  'ಉಡುಪುಗಳನ್ನು ತಯಾರಿಸಿ.',
                       'Make baskets, decor, traditional products or locally distinctive handmade goods.': 'ಬುಟ್ಟಿಗಳು, ಅಲಂಕಾರಿಕ ವಸ್ತುಗಳು, ಸಾಂಪ್ರದಾಯಿಕ '
                                                                                                           'ಉತ್ಪನ್ನಗಳು ಅಥವಾ ಸ್ಥಳೀಯ ವಿಶೇಷತೆಯ ಕೈತಯಾರಿಕಾ '
                                                                                                           'ವಸ್ತುಗಳನ್ನು ತಯಾರಿಸಿ.',
                       'Supply seeds, tools, irrigation accessories and farm-related services.': 'ಬೀಜಗಳು, ಉಪಕರಣಗಳು, ನೀರಾವರಿ ಸಾಮಗ್ರಿಗಳು ಮತ್ತು ಕೃಷಿ ಸಂಬಂಧಿತ '
                                                                                                 'ಸೇವೆಗಳನ್ನು ಒದಗಿಸಿ.',
                       'Repair phones, appliances, agricultural equipment or other locally needed items.': 'ಮೊಬೈಲ್\u200cಗಳು, ಉಪಕರಣಗಳು, ಕೃಷಿ ಯಂತ್ರೋಪಕರಣಗಳು ಅಥವಾ '
                                                                                                           'ಸ್ಥಳೀಯವಾಗಿ ಅಗತ್ಯವಿರುವ ಇತರ ವಸ್ತುಗಳನ್ನು ದುರಸ್ತಿ '
                                                                                                           'ಮಾಡಿ.'},
             'risk': {'Weather, water availability and price fluctuations.': 'ಹವಾಮಾನ, ನೀರಿನ ಲಭ್ಯತೆ ಮತ್ತು ಬೆಲೆ ಏರಿಳಿತಗಳು.',
                      'Food safety, packaging, shelf life and market access.': 'ಆಹಾರ ಸುರಕ್ಷತೆ, ಪ್ಯಾಕೇಜಿಂಗ್, ಸಂಗ್ರಹ ಅವಧಿ ಮತ್ತು ಮಾರುಕಟ್ಟೆ ಪ್ರವೇಶ.',
                      'Competition, inventory management and credit sales.': 'ಸ್ಪರ್ಧೆ, ದಾಸ್ತಾನು ನಿರ್ವಹಣೆ ಮತ್ತು ಸಾಲದ ಮಾರಾಟ.',
                      'Location dependency, hygiene and daily demand variation.': 'ಸ್ಥಳದ ಅವಲಂಬನೆ, ಸ್ವಚ್ಛತೆ ಮತ್ತು ದೈನಂದಿನ ಬೇಡಿಕೆಯ ಬದಲಾವಣೆ.',
                      'Animal health, feed costs and milk-price changes.': 'ಜಾನುವಾರುಗಳ ಆರೋಗ್ಯ, ಮೇವು ವೆಚ್ಚ ಮತ್ತು ಹಾಲಿನ ಬೆಲೆ ಬದಲಾವಣೆಗಳು.',
                      'Disease, feed costs and market-price fluctuations.': 'ರೋಗ, ಮೇವು ವೆಚ್ಚ ಮತ್ತು ಮಾರುಕಟ್ಟೆ ಬೆಲೆ ಏರಿಳಿತಗಳು.',
                      'Feed costs, disease and price volatility.': 'ಮೇವು ವೆಚ್ಚ, ರೋಗ ಮತ್ತು ಬೆಲೆ ಅಸ್ಥಿರತೆ.',
                      'Fuel costs, vehicle maintenance and route density.': 'ಇಂಧನ ವೆಚ್ಚ, ವಾಹನ ನಿರ್ವಹಣೆ ಮತ್ತು ಮಾರ್ಗದ ಬೇಡಿಕೆ.',
                      'Competition and seasonal demand.': 'ಸ್ಪರ್ಧೆ ಮತ್ತು ಋತುಮಾನ ಬೇಡಿಕೆ.',
                      'Demand discovery and inconsistent order volume.': 'ಬೇಡಿಕೆಯನ್ನು ಗುರುತಿಸುವುದು ಮತ್ತು ಆರ್ಡರ್ ಪ್ರಮಾಣದ ಅಸ್ಥಿರತೆ.',
                      'Inventory, licensing requirements and seasonal demand.': 'ದಾಸ್ತಾನು, ಪರವಾನಗಿ ಅಗತ್ಯತೆಗಳು ಮತ್ತು ಋತುಮಾನ ಬೇಡಿಕೆ.',
                      'Skill dependency and availability of spare parts.': 'ಕೌಶಲ್ಯದ ಅವಲಂಬನೆ ಮತ್ತು ಸ್ಪೇರ್ ಪಾರ್ಟ್ಸ್ ಲಭ್ಯತೆ.'},
             'steps': {'Select crops based on local demand and water availability.': 'ಸ್ಥಳೀಯ ಬೇಡಿಕೆ ಮತ್ತು ನೀರಿನ ಲಭ್ಯತೆಯ ಆಧಾರದ ಮೇಲೆ ಬೆಳೆಗಳನ್ನು ಆಯ್ಕೆ ಮಾಡಿ.',
                       'Estimate seed, labour, irrigation and transport costs.': 'ಬೀಜ, ಕಾರ್ಮಿಕ, ನೀರಾವರಿ ಮತ್ತು ಸಾರಿಗೆ ವೆಚ್ಚಗಳನ್ನು ಅಂದಾಜಿಸಿ.',
                       'Plan more than one sales channel instead of depending on a single buyer.': 'ಒಬ್ಬ ಖರೀದಿದಾರನ ಮೇಲೆ ಅವಲಂಬಿಸದೆ ಒಂದಕ್ಕಿಂತ ಹೆಚ್ಚು ಮಾರಾಟ '
                                                                                                   'ಮಾರ್ಗಗಳನ್ನು ಯೋಜಿಸಿ.',
                       'Choose one product with a clear local customer segment.': 'ಸ್ಪಷ್ಟ ಸ್ಥಳೀಯ ಗ್ರಾಹಕ ವರ್ಗವಿರುವ ಒಂದು ಉತ್ಪನ್ನವನ್ನು ಆಯ್ಕೆ ಮಾಡಿ.',
                       'Calculate raw material, packaging, labour and selling costs.': 'ಕಚ್ಚಾ ವಸ್ತು, ಪ್ಯಾಕೇಜಿಂಗ್, ಕಾರ್ಮಿಕ ಮತ್ತು ಮಾರಾಟ ವೆಚ್ಚಗಳನ್ನು ಲೆಕ್ಕಿಸಿ.',
                       'Test a small batch before investing in larger equipment.': 'ದೊಡ್ಡ ಉಪಕರಣಗಳಲ್ಲಿ ಹೂಡಿಕೆ ಮಾಡುವ ಮೊದಲು ಸಣ್ಣ ಬ್ಯಾಚ್ ಪರೀಕ್ಷಿಸಿ.',
                       'Start with fast-moving essentials instead of excessive inventory.': 'ಹೆಚ್ಚು ದಾಸ್ತಾನು ಇಡುವ ಬದಲು ವೇಗವಾಗಿ ಮಾರಾಟವಾಗುವ ಅಗತ್ಯ ವಸ್ತುಗಳಿಂದ '
                                                                                            'ಆರಂಭಿಸಿ.',
                       'Track daily sales and stock movement.': 'ದೈನಂದಿನ ಮಾರಾಟ ಮತ್ತು ದಾಸ್ತಾನು ಚಲನವಲನವನ್ನು ದಾಖಲಿಸಿ.',
                       'Add high-demand local products after observing customer behaviour.': 'ಗ್ರಾಹಕರ ವರ್ತನೆಯನ್ನು ಗಮನಿಸಿದ ನಂತರ ಹೆಚ್ಚು ಬೇಡಿಕೆಯ ಸ್ಥಳೀಯ '
                                                                                             'ಉತ್ಪನ್ನಗಳನ್ನು ಸೇರಿಸಿ.',
                       'Choose a small menu with good margins.': 'ಉತ್ತಮ ಲಾಭಾಂಶವಿರುವ ಸಣ್ಣ ಮೆನು ಆಯ್ಕೆ ಮಾಡಿ.',
                       'Test demand at different times of the day.': 'ದಿನದ ವಿವಿಧ ಸಮಯಗಳಲ್ಲಿ ಬೇಡಿಕೆಯನ್ನು ಪರೀಕ್ಷಿಸಿ.',
                       'Maintain hygiene, consistent quality and simple bookkeeping.': 'ಸ್ವಚ್ಛತೆ, ಸ್ಥಿರ ಗುಣಮಟ್ಟ ಮತ್ತು ಸರಳ ಲೆಕ್ಕಪತ್ರವನ್ನು ಕಾಪಾಡಿ.',
                       'Estimate feed and veterinary costs before buying animals.': 'ಜಾನುವಾರುಗಳನ್ನು ಖರೀದಿಸುವ ಮೊದಲು ಮೇವು ಮತ್ತು ಪಶುವೈದ್ಯಕೀಯ ವೆಚ್ಚಗಳನ್ನು '
                                                                                    'ಅಂದಾಜಿಸಿ.',
                       'Identify a reliable local milk buyer.': 'ವಿಶ್ವಾಸಾರ್ಹ ಸ್ಥಳೀಯ ಹಾಲು ಖರೀದಿದಾರರನ್ನು ಗುರುತಿಸಿ.',
                       'Maintain records of milk yield and animal health.': 'ಹಾಲಿನ ಉತ್ಪಾದನೆ ಮತ್ತು ಜಾನುವಾರುಗಳ ಆರೋಗ್ಯದ ದಾಖಲೆಗಳನ್ನು ಇಡಿ.',
                       'Start with a manageable herd size.': 'ನಿರ್ವಹಿಸಬಹುದಾದ ಹಿಂಡಿನ ಗಾತ್ರದಿಂದ ಆರಂಭಿಸಿ.',
                       'Plan vaccination and veterinary care.': 'ಲಸಿಕೆ ಮತ್ತು ಪಶುವೈದ್ಯಕೀಯ ಆರೈಕೆಯ ಯೋಜನೆ ಮಾಡಿ.',
                       'Build a buyer network before scaling.': 'ವಿಸ್ತರಿಸುವ ಮೊದಲು ಖರೀದಿದಾರರ ಜಾಲವನ್ನು ನಿರ್ಮಿಸಿ.',
                       'Choose egg or meat production based on local demand.': 'ಸ್ಥಳೀಯ ಬೇಡಿಕೆಯ ಆಧಾರದ ಮೇಲೆ ಮೊಟ್ಟೆ ಅಥವಾ ಮಾಂಸ ಉತ್ಪಾದನೆಯನ್ನು ಆಯ್ಕೆ ಮಾಡಿ.',
                       'Calculate feed cost per bird.': 'ಪ್ರತಿ ಪಕ್ಷಿಯ ಮೇವು ವೆಚ್ಚವನ್ನು ಲೆಕ್ಕಿಸಿ.',
                       'Maintain biosecurity and veterinary schedules.': 'ಜೈವಿಕ ಭದ್ರತೆ ಮತ್ತು ಪಶುವೈದ್ಯಕೀಯ ವೇಳಾಪಟ್ಟಿಯನ್ನು ಕಾಪಾಡಿ.',
                       'Map villages and shops that need regular delivery.': 'ನಿಯಮಿತ ವಿತರಣೆಯ ಅಗತ್ಯವಿರುವ ಗ್ರಾಮಗಳು ಮತ್ತು ಅಂಗಡಿಗಳನ್ನು ಗುರುತಿಸಿ.',
                       'Start with a defined service radius.': 'ನಿರ್ದಿಷ್ಟ ಸೇವಾ ವ್ಯಾಪ್ತಿಯಿಂದ ಆರಂಭಿಸಿ.',
                       'Use simple digital records for orders, fuel and collections.': 'ಆರ್ಡರ್\u200cಗಳು, ಇಂಧನ ಮತ್ತು ಪಾವತಿ ಸಂಗ್ರಹಕ್ಕಾಗಿ ಸರಳ ಡಿಜಿಟಲ್ ದಾಖಲೆಗಳನ್ನು '
                                                                                       'ಬಳಸಿ.',
                       'Start with alterations and high-demand local garments.': 'ಬಟ್ಟೆ ಬದಲಾವಣೆ ಮತ್ತು ಹೆಚ್ಚು ಬೇಡಿಕೆಯ ಸ್ಥಳೀಯ ಉಡುಪುಗಳಿಂದ ಆರಂಭಿಸಿ.',
                       'Build repeat customers through reliable delivery.': 'ವಿಶ್ವಾಸಾರ್ಹ ಸೇವೆಯ ಮೂಲಕ ಮರುಬರುವ ಗ್ರಾಹಕರನ್ನು ನಿರ್ಮಿಸಿ.',
                       'Add machines only when order volume justifies them.': 'ಆರ್ಡರ್ ಪ್ರಮಾಣವು ಸಮರ್ಥಿಸಿದಾಗ ಮಾತ್ರ ಯಂತ್ರಗಳನ್ನು ಹೆಚ್ಚಿಸಿ.',
                       'Create a small catalogue and sample products.': 'ಸಣ್ಣ ಕ್ಯಾಟಲಾಗ್ ಮತ್ತು ಮಾದರಿ ಉತ್ಪನ್ನಗಳನ್ನು ತಯಾರಿಸಿ.',
                       'Explore local fairs, retailers and digital selling channels.': 'ಸ್ಥಳೀಯ ಜಾತ್ರೆಗಳು, ಚಿಲ್ಲರೆ ವ್ಯಾಪಾರಿಗಳು ಮತ್ತು ಡಿಜಿಟಲ್ ಮಾರಾಟ ಮಾರ್ಗಗಳನ್ನು '
                                                                                       'ಅನ್ವೇಷಿಸಿ.',
                       'Identify the crops and farm needs of nearby villages.': 'ಹತ್ತಿರದ ಗ್ರಾಮಗಳ ಬೆಳೆಗಳು ಮತ್ತು ಕೃಷಿ ಅಗತ್ಯಗಳನ್ನು ಗುರುತಿಸಿ.',
                       'Stock fast-moving inputs first.': 'ಮೊದಲು ವೇಗವಾಗಿ ಮಾರಾಟವಾಗುವ ಕೃಷಿ ಇನ್\u200cಪುಟ್\u200cಗಳನ್ನು ಸಂಗ್ರಹಿಸಿ.',
                       'Follow all applicable licences and quality requirements.': 'ಅನ್ವಯವಾಗುವ ಎಲ್ಲಾ ಪರವಾನಗಿ ಮತ್ತು ಗುಣಮಟ್ಟದ ಅವಶ್ಯಕತೆಗಳನ್ನು ಪಾಲಿಸಿ.',
                       'Choose one repair category based on local demand.': 'ಸ್ಥಳೀಯ ಬೇಡಿಕೆಯ ಆಧಾರದ ಮೇಲೆ ಒಂದು ದುರಸ್ತಿ ವಿಭಾಗವನ್ನು ಆಯ್ಕೆ ಮಾಡಿ.',
                       'Keep commonly required spare parts.': 'ಸಾಮಾನ್ಯವಾಗಿ ಅಗತ್ಯವಿರುವ ಸ್ಪೇರ್ ಪಾರ್ಟ್ಸ್\u200cಗಳನ್ನು ಇಟ್ಟುಕೊಳ್ಳಿ.',
                       'Build trust through transparent pricing and service records.': 'ಪಾರದರ್ಶಕ ಬೆಲೆ ಮತ್ತು ಸೇವಾ ದಾಖಲೆಗಳ ಮೂಲಕ ವಿಶ್ವಾಸವನ್ನು ನಿರ್ಮಿಸಿ.'}}}
P1_RESOURCE_TR = {'Hindi': {'Land': 'ज़मीन',
           'Water': 'पानी',
           'Shop space': 'दुकान की जगह',
           'Kitchen/Workspace': 'रसोई/कार्यस्थल',
           'Cattle': 'पशु',
           'Sewing machine': 'सिलाई मशीन',
           'Vehicle': 'वाहन',
           'Repair tools': 'मरम्मत के औज़ार',
           'Craft skills': 'कारीगरी कौशल',
           'Agriculture knowledge': 'कृषि ज्ञान',
           'Fodder': 'चारा',
           'Shelter': 'शेड/आश्रय',
           'Agricultural tools': 'कृषि उपकरण',
           'Food processing equipment': 'खाद्य प्रसंस्करण उपकरण',
           'Raw materials': 'कच्चा माल',
           'Kitchen equipment': 'रसोई उपकरण',
           'Small stall/shop': 'छोटा स्टॉल/दुकान',
           'Food preparation skills': 'खाना बनाने का कौशल',
           'Livestock care': 'पशु देखभाल',
           'Poultry equipment': 'पोल्ट्री उपकरण',
           'Two-wheeler/vehicle': 'दो-पहिया/वाहन',
           'Mobile phone': 'मोबाइल फोन',
           'Driving skills': 'ड्राइविंग कौशल',
           'Workspace': 'कार्यस्थल',
           'Tailoring skills': 'सिलाई कौशल',
           'Shop': 'दुकान',
           'Working capital': 'कार्यशील पूंजी',
           'Supplier network': 'आपूर्तिकर्ता नेटवर्क',
           'Technical skill': 'तकनीकी कौशल',
           'Not sure / I have limited resources': 'पता नहीं / मेरे पास सीमित संसाधन हैं'},
 'Kannada': {'Land': 'ಭೂಮಿ',
             'Water': 'ನೀರು',
             'Shop space': 'ಅಂಗಡಿ ಸ್ಥಳ',
             'Kitchen/Workspace': 'ಅಡುಗೆಮನೆ/ಕೆಲಸದ ಸ್ಥಳ',
             'Cattle': 'ಜಾನುವಾರು',
             'Sewing machine': 'ಹೊಲಿಗೆ ಯಂತ್ರ',
             'Vehicle': 'ವಾಹನ',
             'Repair tools': 'ದುರಸ್ತಿ ಉಪಕರಣಗಳು',
             'Craft skills': 'ಕರಕುಶಲ ಕೌಶಲ್ಯ',
             'Agriculture knowledge': 'ಕೃಷಿ ಜ್ಞಾನ',
             'Fodder': 'ಮೇವು',
             'Shelter': 'ಶೆಡ್/ಆಶ್ರಯ',
             'Agricultural tools': 'ಕೃಷಿ ಉಪಕರಣಗಳು',
             'Food processing equipment': 'ಆಹಾರ ಸಂಸ್ಕರಣಾ ಉಪಕರಣಗಳು',
             'Raw materials': 'ಕಚ್ಚಾ ವಸ್ತುಗಳು',
             'Kitchen equipment': 'ಅಡುಗೆ ಉಪಕರಣಗಳು',
             'Small stall/shop': 'ಸಣ್ಣ ಸ್ಟಾಲ್/ಅಂಗಡಿ',
             'Food preparation skills': 'ಆಹಾರ ತಯಾರಿಕಾ ಕೌಶಲ್ಯ',
             'Livestock care': 'ಜಾನುವಾರು ಆರೈಕೆ',
             'Poultry equipment': 'ಕೋಳಿ ಸಾಕಣೆ ಉಪಕರಣಗಳು',
             'Two-wheeler/vehicle': 'ಎರಡು ಚಕ್ರದ ವಾಹನ/ವಾಹನ',
             'Mobile phone': 'ಮೊಬೈಲ್ ಫೋನ್',
             'Driving skills': 'ಚಾಲನಾ ಕೌಶಲ್ಯ',
             'Workspace': 'ಕೆಲಸದ ಸ್ಥಳ',
             'Tailoring skills': 'ಹೊಲಿಗೆ ಕೌಶಲ್ಯ',
             'Shop': 'ಅಂಗಡಿ',
             'Working capital': 'ಕಾರ್ಯನಿರ್ವಹಣಾ ಬಂಡವಾಳ',
             'Supplier network': 'ಪೂರೈಕೆದಾರರ ಜಾಲ',
             'Technical skill': 'ತಾಂತ್ರಿಕ ಕೌಶಲ್ಯ',
             'Not sure / I have limited resources': 'ಖಚಿತವಿಲ್ಲ / ನನ್ನ ಬಳಿ ಸೀಮಿತ ಸಂಪನ್ಮೂಲಗಳಿವೆ'}}

def p1_business_content(kind, value):
    return P1_BUSINESS_CONTENT_TR.get(language, {}).get(kind, {}).get(value, value)

def p1_resource_text(value):
    return P1_RESOURCE_TR.get(language, {}).get(value, value)

# ============================================================
# PRIORITY 1 — SMART ACTION PLAN
# All UI text for this module is translated from the selected language.
# ============================================================
P1_TR = {
    "English": {
        "title":"Smart Action Plan", "desc":"Turn your location, season, resources, business interest and finances into one practical decision plan.",
        "today":"What Should I Do Today?", "today_desc":"A single view combining local context, farming options, business fit, risks, schemes and next actions.",
        "context":"Your current context", "season":"Season", "water_context":"Water context", "location":"Location",
        "top_crops":"Crop options to explore", "business_option":"Business option to explore", "next_steps":"Today's practical steps",
        "step1":"Check local demand and verify today's mandi price before spending money.",
        "step2":"Check water, labour, input availability and the total starting cost.",
        "step3":"Compare at least two options and run a small financial scenario before scaling.",
        "step4":"Check potentially relevant government schemes and document readiness.",
        "why_title":"Why This Recommendation?", "why_desc":"See exactly which factors contributed to the business matching score.",
        "choose_business":"Choose a business", "score_breakdown":"Score breakdown", "capital_fit":"Capital fit", "resource_fit":"Resource fit", "interest_fit":"Interest fit", "water_fit":"Water fit", "experience_fit":"Experience fit", "location_fit":"Location fit", "total":"Total", "out_of":"out of 100",
        "matched_resources":"Matched resources", "missing_resources":"Additional resources may be needed", "no_resources":"No matching resources selected",
        "risk_title":"Risk Alerts", "risk_desc":"Flags are based on the prototype's rules and your selected inputs.", "high":"High attention", "medium":"Needs attention", "low":"Lower attention",
        "capital_alert":"Capital is below the indicative starting range.", "water_alert":"This option has a higher water requirement than the current location context.", "season_alert":"This crop is outside its prototype recommended season.", "market_alert":"Market prices in this prototype are demonstration data, not live mandi prices.", "long_crop":"This crop has a long harvest period, so capital may remain locked for longer.", "risk_none":"No major rule-based alert was triggered by the selected inputs.",
        "compare_title":"Compare Two Options", "compare_desc":"Compare two crops or two businesses side by side without forcing a single answer.", "option_type":"Compare", "businesses":"Businesses", "crops":"Crops", "option_a":"Option A", "option_b":"Option B", "comparison":"Comparison", "difference":"Difference / context", "same":"Same / similar", "compare_note":"Use the differences to decide what you want to investigate further; the prototype does not guarantee outcomes.",
        "scheme_title":"Scheme Document Readiness", "scheme_desc":"Select a scheme and tick documents you already have. This is a preparation checklist, not an eligibility decision.", "scheme":"Scheme", "documents_have":"Documents I already have", "readiness":"Document readiness", "ready":"ready", "missing":"Missing / not checked", "eligibility_check":"Eligibility still needs to be verified from the official scheme guidelines.",
        "sim_title":"Business & Farming Simulator", "sim_desc":"Test simple scenarios by changing price, quantity and costs. This is a planning calculator, not a forecast.", "business_sim":"Business simulator", "farm_sim":"Farming simulator", "units":"Units / output", "sale_price":"Selling price per unit", "variable_cost":"Variable cost per unit", "fixed_cost":"Other / fixed costs", "revenue":"Revenue", "cost":"Total cost", "profit":"Estimated profit", "scenario":"Scenario", "normal":"Normal", "price_down":"Selling price -10%", "cost_up":"Variable cost +15%", "both":"Price -10% and variable cost +15%", "baseline":"Baseline", "scenario_result":"Scenario result", "farm_area":"Area (acres)", "yield_per_acre":"Expected output per acre", "farm_price":"Expected selling price per unit", "farm_cost":"Estimated total cost", "farm_note":"Enter your own realistic local assumptions; do not treat the result as guaranteed profit.",
        "disclaimer":"Prototype decision support: rules and demonstration data are illustrative. Verify live market information, local agricultural advice, scheme rules and financing terms before acting.",
        "generate":"Generate plan", "selected":"Selected", "profile":"Decision profile"
    },
    "Hindi": {
        "title":"स्मार्ट कार्य योजना", "desc":"आपके स्थान, मौसम, संसाधन, व्यवसाय रुचि और वित्त को एक व्यावहारिक निर्णय योजना में बदलें।",
        "today":"आज मुझे क्या करना चाहिए?", "today_desc":"स्थानीय संदर्भ, खेती विकल्प, व्यवसाय उपयुक्तता, जोखिम, योजनाएँ और अगले कदम एक जगह देखें।", "context":"आपका वर्तमान संदर्भ", "season":"मौसम", "water_context":"पानी की स्थिति", "location":"स्थान", "top_crops":"देखने योग्य फसल विकल्प", "business_option":"देखने योग्य व्यवसाय", "next_steps":"आज के व्यावहारिक कदम",
        "step1":"पैसा लगाने से पहले स्थानीय मांग और आज के मंडी भाव की पुष्टि करें।", "step2":"पानी, मजदूर, इनपुट की उपलब्धता और कुल शुरुआती लागत देखें।", "step3":"कम से कम दो विकल्पों की तुलना करें और बड़ा निवेश करने से पहले छोटा वित्तीय परिदृश्य चलाएँ।", "step4":"संभावित सरकारी योजनाओं और दस्तावेज़ की तैयारी जाँचें।",
        "why_title":"यह सुझाव क्यों?", "why_desc":"देखें कि व्यवसाय मिलान स्कोर में कौन-कौन से कारक जुड़े हैं।", "choose_business":"व्यवसाय चुनें", "score_breakdown":"स्कोर विवरण", "capital_fit":"पूंजी मिलान", "resource_fit":"संसाधन मिलान", "interest_fit":"रुचि मिलान", "water_fit":"पानी मिलान", "experience_fit":"अनुभव मिलान", "location_fit":"स्थान मिलान", "total":"कुल", "out_of":"100 में से", "matched_resources":"मेल खाने वाले संसाधन", "missing_resources":"कुछ अतिरिक्त संसाधनों की आवश्यकता हो सकती है", "no_resources":"कोई मेल खाने वाला संसाधन नहीं चुना गया",
        "risk_title":"जोखिम चेतावनियाँ", "risk_desc":"चेतावनियाँ प्रोटोटाइप नियमों और आपके चुने हुए इनपुट पर आधारित हैं।", "high":"अधिक ध्यान", "medium":"ध्यान दें", "low":"कम ध्यान", "capital_alert":"पूंजी अनुमानित शुरुआती सीमा से कम है।", "water_alert":"इस विकल्प की पानी की जरूरत वर्तमान स्थान की स्थिति से अधिक है।", "season_alert":"यह फसल प्रोटोटाइप के सुझाए मौसम से बाहर है।", "market_alert":"इस प्रोटोटाइप में बाजार भाव प्रदर्शन डेटा हैं, लाइव मंडी भाव नहीं।", "long_crop":"इस फसल की कटाई अवधि लंबी है, इसलिए पूंजी अधिक समय तक लगी रह सकती है।", "risk_none":"चुने गए इनपुट से कोई बड़ा नियम-आधारित जोखिम संकेत नहीं मिला।",
        "compare_title":"दो विकल्पों की तुलना", "compare_desc":"दो फसलों या दो व्यवसायों की साथ-साथ तुलना करें; किसी एक को जबरन चुनने की जरूरत नहीं।", "option_type":"तुलना", "businesses":"व्यवसाय", "crops":"फसलें", "option_a":"विकल्प A", "option_b":"विकल्प B", "comparison":"तुलना", "difference":"अंतर / संदर्भ", "same":"समान / मिलते-जुलते", "compare_note":"अंतर के आधार पर आगे जाँच करें; प्रोटोटाइप परिणाम की गारंटी नहीं देता।",
        "scheme_title":"योजना दस्तावेज़ तैयारी", "scheme_desc":"एक योजना चुनें और जो दस्तावेज़ आपके पास हैं उन्हें टिक करें। यह तैयारी सूची है, पात्रता निर्णय नहीं।", "scheme":"योजना", "documents_have":"मेरे पास मौजूद दस्तावेज़", "readiness":"दस्तावेज़ तैयारी", "ready":"तैयार", "missing":"बाकी / जाँच नहीं हुई", "eligibility_check":"पात्रता की पुष्टि आधिकारिक योजना दिशानिर्देश से करनी होगी।",
        "sim_title":"व्यवसाय और खेती सिमुलेटर", "sim_desc":"मूल्य, मात्रा और लागत बदलकर सरल परिदृश्य जाँचें। यह योजना कैलकुलेटर है, भविष्यवाणी नहीं।", "business_sim":"व्यवसाय सिमुलेटर", "farm_sim":"खेती सिमुलेटर", "units":"इकाई / उत्पादन", "sale_price":"प्रति इकाई बिक्री मूल्य", "variable_cost":"प्रति इकाई परिवर्तनीय लागत", "fixed_cost":"अन्य / स्थिर लागत", "revenue":"राजस्व", "cost":"कुल लागत", "profit":"अनुमानित लाभ", "scenario":"परिदृश्य", "normal":"सामान्य", "price_down":"बिक्री मूल्य -10%", "cost_up":"परिवर्तनीय लागत +15%", "both":"मूल्य -10% और परिवर्तनीय लागत +15%", "baseline":"आधार स्थिति", "scenario_result":"परिदृश्य परिणाम", "farm_area":"क्षेत्रफल (एकड़)", "yield_per_acre":"प्रति एकड़ अपेक्षित उत्पादन", "farm_price":"प्रति इकाई अपेक्षित बिक्री मूल्य", "farm_cost":"अनुमानित कुल लागत", "farm_note":"अपनी स्थानीय और वास्तविक मान्यताएँ डालें; परिणाम को निश्चित लाभ न मानें।", "disclaimer":"प्रोटोटाइप निर्णय सहायता: नियम और प्रदर्शन डेटा उदाहरणात्मक हैं। कार्रवाई से पहले लाइव बाजार जानकारी, स्थानीय कृषि सलाह, योजना नियम और वित्तीय शर्तों की पुष्टि करें।", "generate":"योजना बनाएं", "selected":"चयनित", "profile":"निर्णय प्रोफाइल"
    },
    "Kannada": {
        "title":"ಸ್ಮಾರ್ಟ್ ಕಾರ್ಯ ಯೋಜನೆ", "desc":"ನಿಮ್ಮ ಸ್ಥಳ, ಋತು, ಸಂಪನ್ಮೂಲ, ವ್ಯವಹಾರ ಆಸಕ್ತಿ ಮತ್ತು ಹಣಕಾಸನ್ನು ಒಂದು ಪ್ರಾಯೋಗಿಕ ನಿರ್ಧಾರ ಯೋಜನೆಯಾಗಿ ಪರಿವರ್ತಿಸಿ.",
        "today":"ಇಂದು ನಾನು ಏನು ಮಾಡಬೇಕು?", "today_desc":"ಸ್ಥಳೀಯ ಪರಿಸ್ಥಿತಿ, ಕೃಷಿ ಆಯ್ಕೆಗಳು, ವ್ಯವಹಾರ ಹೊಂದಾಣಿಕೆ, ಅಪಾಯಗಳು, ಯೋಜನೆಗಳು ಮತ್ತು ಮುಂದಿನ ಕ್ರಮಗಳನ್ನು ಒಂದೇ ಸ್ಥಳದಲ್ಲಿ ನೋಡಿ.", "context":"ನಿಮ್ಮ ಪ್ರಸ್ತುತ ಪರಿಸ್ಥಿತಿ", "season":"ಋತು", "water_context":"ನೀರಿನ ಪರಿಸ್ಥಿತಿ", "location":"ಸ್ಥಳ", "top_crops":"ಪರಿಶೀಲಿಸಬಹುದಾದ ಬೆಳೆ ಆಯ್ಕೆಗಳು", "business_option":"ಪರಿಶೀಲಿಸಬಹುದಾದ ವ್ಯವಹಾರ", "next_steps":"ಇಂದಿನ ಪ್ರಾಯೋಗಿಕ ಕ್ರಮಗಳು",
        "step1":"ಹಣ ಹೂಡುವ ಮೊದಲು ಸ್ಥಳೀಯ ಬೇಡಿಕೆ ಮತ್ತು ಇಂದಿನ ಮಾರುಕಟ್ಟೆ ಬೆಲೆಯನ್ನು ಪರಿಶೀಲಿಸಿ.", "step2":"ನೀರು, ಕಾರ್ಮಿಕರು, ಇನ್‌ಪುಟ್ ಲಭ್ಯತೆ ಮತ್ತು ಒಟ್ಟು ಆರಂಭಿಕ ವೆಚ್ಚವನ್ನು ಪರಿಶೀಲಿಸಿ.", "step3":"ಕನಿಷ್ಠ ಎರಡು ಆಯ್ಕೆಗಳನ್ನು ಹೋಲಿಸಿ ಮತ್ತು ದೊಡ್ಡ ಹೂಡಿಕೆ ಮಾಡುವ ಮೊದಲು ಸಣ್ಣ ಹಣಕಾಸು ಪರಿಸ್ಥಿತಿಯನ್ನು ಪರೀಕ್ಷಿಸಿ.", "step4":"ಸಂಬಂಧಿತ ಸರ್ಕಾರಿ ಯೋಜನೆಗಳು ಮತ್ತು ದಾಖಲೆ ಸಿದ್ಧತೆಯನ್ನು ಪರಿಶೀಲಿಸಿ.",
        "why_title":"ಈ ಸಲಹೆ ಏಕೆ?", "why_desc":"ವ್ಯವಹಾರ ಹೊಂದಾಣಿಕೆ ಅಂಕದಲ್ಲಿ ಯಾವ ಅಂಶಗಳು ಸೇರಿವೆ ಎಂಬುದನ್ನು ನೋಡಿ.", "choose_business":"ವ್ಯವಹಾರ ಆಯ್ಕೆಮಾಡಿ", "score_breakdown":"ಅಂಕಗಳ ವಿವರ", "capital_fit":"ಬಂಡವಾಳ ಹೊಂದಾಣಿಕೆ", "resource_fit":"ಸಂಪನ್ಮೂಲ ಹೊಂದಾಣಿಕೆ", "interest_fit":"ಆಸಕ್ತಿ ಹೊಂದಾಣಿಕೆ", "water_fit":"ನೀರಿನ ಹೊಂದಾಣಿಕೆ", "experience_fit":"ಅನುಭವ ಹೊಂದಾಣಿಕೆ", "location_fit":"ಸ್ಥಳ ಹೊಂದಾಣಿಕೆ", "total":"ಒಟ್ಟು", "out_of":"100ರಲ್ಲಿ", "matched_resources":"ಹೊಂದಾಣಿಕೆಯ ಸಂಪನ್ಮೂಲಗಳು", "missing_resources":"ಕೆಲವು ಹೆಚ್ಚುವರಿ ಸಂಪನ್ಮೂಲಗಳು ಬೇಕಾಗಬಹುದು", "no_resources":"ಹೊಂದಾಣಿಕೆಯ ಸಂಪನ್ಮೂಲ ಆಯ್ಕೆ ಮಾಡಿಲ್ಲ",
        "risk_title":"ಅಪಾಯ ಎಚ್ಚರಿಕೆಗಳು", "risk_desc":"ಎಚ್ಚರಿಕೆಗಳು ಪ್ರೋಟೋಟೈಪ್ ನಿಯಮಗಳು ಮತ್ತು ನಿಮ್ಮ ಆಯ್ಕೆ ಮಾಡಿದ ಮಾಹಿತಿಯ ಮೇಲೆ ಆಧಾರಿತವಾಗಿವೆ.", "high":"ಹೆಚ್ಚಿನ ಗಮನ", "medium":"ಗಮನ ಅಗತ್ಯ", "low":"ಕಡಿಮೆ ಗಮನ", "capital_alert":"ಬಂಡವಾಳವು ಅಂದಾಜು ಆರಂಭಿಕ ವ್ಯಾಪ್ತಿಗಿಂತ ಕಡಿಮೆಯಿದೆ.", "water_alert":"ಈ ಆಯ್ಕೆಗೆ ಪ್ರಸ್ತುತ ಸ್ಥಳದ ನೀರಿನ ಪರಿಸ್ಥಿತಿಗಿಂತ ಹೆಚ್ಚಿನ ನೀರು ಬೇಕಾಗುತ್ತದೆ.", "season_alert":"ಈ ಬೆಳೆ ಪ್ರೋಟೋಟೈಪ್ ಸೂಚಿಸಿರುವ ಋತುವಿನ ಹೊರಗಿದೆ.", "market_alert":"ಈ ಪ್ರೋಟೋಟೈಪ್‌ನ ಮಾರುಕಟ್ಟೆ ಬೆಲೆಗಳು ಪ್ರದರ್ಶನ ಡೇಟಾ; ಲೈವ್ ಮಾರುಕಟ್ಟೆ ಬೆಲೆಗಳಲ್ಲ.", "long_crop":"ಈ ಬೆಳೆಗೆ ದೀರ್ಘ ಕೊಯ್ಲು ಅವಧಿಯಿದೆ; ಆದ್ದರಿಂದ ಬಂಡವಾಳ ಹೆಚ್ಚು ಕಾಲ ಸಿಲುಕಿರಬಹುದು.", "risk_none":"ಆಯ್ಕೆ ಮಾಡಿದ ಮಾಹಿತಿಯಿಂದ ಪ್ರಮುಖ ನಿಯಮ-ಆಧಾರಿತ ಅಪಾಯ ಕಂಡುಬಂದಿಲ್ಲ.",
        "compare_title":"ಎರಡು ಆಯ್ಕೆಗಳನ್ನು ಹೋಲಿಸಿ", "compare_desc":"ಎರಡು ಬೆಳೆಗಳು ಅಥವಾ ಎರಡು ವ್ಯವಹಾರಗಳನ್ನು ಪಕ್ಕಪಕ್ಕದಲ್ಲಿ ಹೋಲಿಸಿ; ಒಂದನ್ನು ಬಲವಂತವಾಗಿ ಆಯ್ಕೆ ಮಾಡಬೇಕಿಲ್ಲ.", "option_type":"ಹೋಲಿಕೆ", "businesses":"ವ್ಯವಹಾರಗಳು", "crops":"ಬೆಳೆಗಳು", "option_a":"ಆಯ್ಕೆ A", "option_b":"ಆಯ್ಕೆ B", "comparison":"ಹೋಲಿಕೆ", "difference":"ವ್ಯತ್ಯಾಸ / ಸಂದರ್ಭ", "same":"ಒಂದೇ / ಸಮಾನ", "compare_note":"ವ್ಯತ್ಯಾಸಗಳನ್ನು ಬಳಸಿ ಮುಂದೇನು ಪರಿಶೀಲಿಸಬೇಕು ಎಂದು ನಿರ್ಧರಿಸಿ; ಪ್ರೋಟೋಟೈಪ್ ಫಲಿತಾಂಶದ ಭರವಸೆ ನೀಡುವುದಿಲ್ಲ.",
        "scheme_title":"ಯೋಜನೆ ದಾಖಲೆ ಸಿದ್ಧತೆ", "scheme_desc":"ಯೋಜನೆಯನ್ನು ಆಯ್ಕೆ ಮಾಡಿ ಮತ್ತು ನಿಮ್ಮ ಬಳಿ ಇರುವ ದಾಖಲೆಗಳನ್ನು ಟಿಕ್ ಮಾಡಿ. ಇದು ಸಿದ್ಧತಾ ಪಟ್ಟಿ, ಅರ್ಹತಾ ನಿರ್ಧಾರವಲ್ಲ.", "scheme":"ಯೋಜನೆ", "documents_have":"ನನ್ನ ಬಳಿ ಇರುವ ದಾಖಲೆಗಳು", "readiness":"ದಾಖಲೆ ಸಿದ್ಧತೆ", "ready":"ಸಿದ್ಧ", "missing":"ಬಾಕಿ / ಪರಿಶೀಲಿಸಿಲ್ಲ", "eligibility_check":"ಅರ್ಹತೆಯನ್ನು ಅಧಿಕೃತ ಯೋಜನಾ ಮಾರ್ಗಸೂಚಿಗಳಿಂದ ಪರಿಶೀಲಿಸಬೇಕು.",
        "sim_title":"ವ್ಯವಹಾರ ಮತ್ತು ಕೃಷಿ ಸಿಮ್ಯುಲೇಟರ್", "sim_desc":"ಬೆಲೆ, ಪ್ರಮಾಣ ಮತ್ತು ವೆಚ್ಚಗಳನ್ನು ಬದಲಿಸಿ ಸರಳ ಪರಿಸ್ಥಿತಿಗಳನ್ನು ಪರೀಕ್ಷಿಸಿ. ಇದು ಯೋಜನಾ ಕ್ಯಾಲ್ಕುಲೇಟರ್, ಭವಿಷ್ಯವಾಣಿ ಅಲ್ಲ.", "business_sim":"ವ್ಯವಹಾರ ಸಿಮ್ಯುಲೇಟರ್", "farm_sim":"ಕೃಷಿ ಸಿಮ್ಯುಲೇಟರ್", "units":"ಘಟಕಗಳು / ಉತ್ಪಾದನೆ", "sale_price":"ಪ್ರತಿ ಘಟಕ ಮಾರಾಟ ಬೆಲೆ", "variable_cost":"ಪ್ರತಿ ಘಟಕ ಬದಲಾಯಿಸಬಹುದಾದ ವೆಚ್ಚ", "fixed_cost":"ಇತರೆ / ಸ್ಥಿರ ವೆಚ್ಚ", "revenue":"ಆದಾಯ", "cost":"ಒಟ್ಟು ವೆಚ್ಚ", "profit":"ಅಂದಾಜು ಲಾಭ", "scenario":"ಪರಿಸ್ಥಿತಿ", "normal":"ಸಾಮಾನ್ಯ", "price_down":"ಮಾರಾಟ ಬೆಲೆ -10%", "cost_up":"ಬದಲಾಯಿಸಬಹುದಾದ ವೆಚ್ಚ +15%", "both":"ಬೆಲೆ -10% ಮತ್ತು ಬದಲಾಯಿಸಬಹುದಾದ ವೆಚ್ಚ +15%", "baseline":"ಮೂಲ ಸ್ಥಿತಿ", "scenario_result":"ಪರಿಸ್ಥಿತಿ ಫಲಿತಾಂಶ", "farm_area":"ವಿಸ್ತೀರ್ಣ (ಎಕರೆ)", "yield_per_acre":"ಪ್ರತಿ ಎಕರೆಗೆ ನಿರೀಕ್ಷಿತ ಉತ್ಪಾದನೆ", "farm_price":"ಪ್ರತಿ ಘಟಕ ನಿರೀಕ್ಷಿತ ಮಾರಾಟ ಬೆಲೆ", "farm_cost":"ಅಂದಾಜು ಒಟ್ಟು ವೆಚ್ಚ", "farm_note":"ನಿಮ್ಮ ಸ್ಥಳೀಯ ಮತ್ತು ವಾಸ್ತವಿಕ ಅಂದಾಜುಗಳನ್ನು ನಮೂದಿಸಿ; ಫಲಿತಾಂಶವನ್ನು ಖಚಿತ ಲಾಭವೆಂದು ಪರಿಗಣಿಸಬೇಡಿ.", "disclaimer":"ಪ್ರೋಟೋಟೈಪ್ ನಿರ್ಧಾರ ಸಹಾಯ: ನಿಯಮಗಳು ಮತ್ತು ಪ್ರದರ್ಶನ ಡೇಟಾ ಉದಾಹರಣಾತ್ಮಕ. ಕ್ರಮ ಕೈಗೊಳ್ಳುವ ಮೊದಲು ಲೈವ್ ಮಾರುಕಟ್ಟೆ ಮಾಹಿತಿ, ಸ್ಥಳೀಯ ಕೃಷಿ ಸಲಹೆ, ಯೋಜನಾ ನಿಯಮಗಳು ಮತ್ತು ಹಣಕಾಸು ಷರತ್ತುಗಳನ್ನು ಪರಿಶೀಲಿಸಿ.", "generate":"ಯೋಜನೆ ರಚಿಸಿ", "selected":"ಆಯ್ಕೆ", "profile":"ನಿರ್ಧಾರ ಪ್ರೊಫೈಲ್"
    }
}

def p1(key, **kwargs):
    value = P1_TR.get(language, P1_TR["English"]).get(key, P1_TR["English"].get(key, key))
    return value.format(**kwargs) if kwargs else value

P1_BUSINESS_TR = {
    "Hindi": {
        "Vegetable Cultivation":"सब्ज़ी की खेती", "Small Food Processing Unit":"छोटी खाद्य प्रसंस्करण इकाई", "Grocery & Daily-Needs Store":"किराना और दैनिक जरूरतों की दुकान", "Street Food / Snack Business":"स्ट्रीट फूड / स्नैक व्यवसाय", "Dairy / Milk-Based Business":"डेयरी / दूध आधारित व्यवसाय", "Goat / Sheep Rearing":"बकरी / भेड़ पालन", "Poultry Farming":"पोल्ट्री फार्मिंग", "Local Delivery & Transport Service":"स्थानीय डिलीवरी और परिवहन सेवा", "Tailoring & Garment Service":"सिलाई और परिधान सेवा", "Handicrafts & Local Products":"हस्तशिल्प और स्थानीय उत्पाद", "Farm Input & Agri Service Centre":"कृषि इनपुट और कृषि सेवा केंद्र", "Small Repair & Service Centre":"छोटा मरम्मत और सेवा केंद्र"
    },
    "Kannada": {
        "Vegetable Cultivation":"ತರಕಾರಿ ಕೃಷಿ", "Small Food Processing Unit":"ಸಣ್ಣ ಆಹಾರ ಸಂಸ್ಕರಣಾ ಘಟಕ", "Grocery & Daily-Needs Store":"ಕಿರಾಣಿ ಮತ್ತು ದೈನಂದಿನ ಅಗತ್ಯಗಳ ಅಂಗಡಿ", "Street Food / Snack Business":"ಸ್ಟ್ರೀಟ್ ಫುಡ್ / ತಿಂಡಿ ವ್ಯವಹಾರ", "Dairy / Milk-Based Business":"ಡೈರಿ / ಹಾಲು ಆಧಾರಿತ ವ್ಯವಹಾರ", "Goat / Sheep Rearing":"ಮೇಕೆ / ಕುರಿ ಸಾಕಣೆ", "Poultry Farming":"ಕೋಳಿ ಸಾಕಣೆ", "Local Delivery & Transport Service":"ಸ್ಥಳೀಯ ವಿತರಣೆ ಮತ್ತು ಸಾರಿಗೆ ಸೇವೆ", "Tailoring & Garment Service":"ಹೊಲಿಗೆ ಮತ್ತು ಉಡುಪು ಸೇವೆ", "Handicrafts & Local Products":"ಕರಕುಶಲ ಮತ್ತು ಸ್ಥಳೀಯ ಉತ್ಪನ್ನಗಳು", "Farm Input & Agri Service Centre":"ಕೃಷಿ ಇನ್‌ಪುಟ್ ಮತ್ತು ಕೃಷಿ ಸೇವಾ ಕೇಂದ್ರ", "Small Repair & Service Centre":"ಸಣ್ಣ ದುರಸ್ತಿ ಮತ್ತು ಸೇವಾ ಕೇಂದ್ರ"
    }
}

def p1_business_name(name):
    return P1_BUSINESS_TR.get(language, {}).get(name, name)

SCHEME_ELIGIBILITY_TR = {
    "Hindi": {
        "Generally for individuals aged 18+ starting a new eligible micro-enterprise. For projects above the prescribed PMEGP thresholds, minimum educational qualification conditions apply. Existing units are generally not eligible except specified cases under the scheme guidelines.": "आम तौर पर 18+ आयु वाले व्यक्ति जो नया पात्र सूक्ष्म उद्यम शुरू कर रहे हैं। निर्धारित PMEGP सीमा से ऊपर की परियोजनाओं के लिए न्यूनतम शैक्षणिक योग्यता की शर्तें लागू होती हैं। योजना दिशानिर्देशों में बताए गए मामलों को छोड़कर मौजूदा इकाइयाँ सामान्यतः पात्र नहीं होती हैं।",
        "Eligible non-corporate micro enterprises in manufacturing, trading, services and allied agricultural activities such as dairy, poultry and beekeeping. Both new and existing eligible businesses may be considered subject to lender assessment.": "डेयरी, पोल्ट्री और मधुमक्खी पालन जैसी विनिर्माण, व्यापार, सेवा और संबद्ध कृषि गतिविधियों वाले पात्र गैर-कॉरपोरेट सूक्ष्म उद्यम। ऋणदाता के मूल्यांकन के अनुसार नए और मौजूदा पात्र व्यवसायों पर विचार किया जा सकता है।",
        "Eligible street vendors, including surveyed vendors and eligible vendors who can obtain a Certificate/ID of Vending or Letter of Recommendation through the prescribed process.": "सर्वेक्षित विक्रेताओं सहित पात्र स्ट्रीट वेंडर तथा निर्धारित प्रक्रिया से वेंडिंग प्रमाणपत्र/आईडी या अनुशंसा पत्र प्राप्त करने वाले पात्र विक्रेता।",
        "Eligible micro food-processing enterprises and other eligible categories under PMFME. For individual units, the scheme guidelines include conditions such as age, ownership, micro-enterprise status, contribution and eligible food-processing activity.": "PMFME के अंतर्गत पात्र सूक्ष्म खाद्य-प्रसंस्करण उद्यम और अन्य पात्र श्रेणियाँ। व्यक्तिगत इकाइयों के लिए आयु, स्वामित्व, सूक्ष्म-उद्यम स्थिति, अंशदान और पात्र खाद्य-प्रसंस्करण गतिविधि जैसी शर्तें लागू होती हैं।",
        "Farmers including owner cultivators, eligible tenant farmers, oral lessees and sharecroppers; eligible SHGs/JLGs of farmers may also qualify, subject to bank and scheme conditions.": "भूमि के मालिक-किसानों सहित पात्र किरायेदार किसान, मौखिक पट्टेदार और बटाईदार किसान; किसानों के पात्र SHG/JLG भी बैंक और योजना की शर्तों के अनुसार पात्र हो सकते हैं।",
        "Eligible beneficiaries may include farmers, FPOs, PACS, SHGs, agri-entrepreneurs and other eligible entities undertaking permitted agriculture infrastructure projects, subject to the current AIF guidelines and lender appraisal.": "पात्र लाभार्थियों में किसान, FPO, PACS, SHG, कृषि उद्यमी और अनुमत कृषि अवसंरचना परियोजनाएँ करने वाली अन्य पात्र संस्थाएँ शामिल हो सकती हैं, जो वर्तमान AIF दिशानिर्देश और ऋणदाता मूल्यांकन के अधीन हैं।",
        "Primarily for eligible agriculture and allied-sector graduates / qualified candidates who complete the prescribed training and establish eligible Agri-Clinic or Agri-Business Centre activities under current ACABC guidelines.": "मुख्यतः पात्र कृषि और संबद्ध क्षेत्र के स्नातकों/योग्य उम्मीदवारों के लिए जो निर्धारित प्रशिक्षण पूरा करके वर्तमान ACABC दिशानिर्देशों के अनुसार पात्र एग्री-क्लिनिक या एग्री-बिजनेस सेंटर गतिविधि स्थापित करते हैं।",
        "Rural livelihood support is delivered mainly through eligible Self Help Groups, their federations and community institutions under the applicable state rural livelihood mission structure.": "ग्रामीण आजीविका सहायता मुख्यतः पात्र स्वयं सहायता समूहों, उनके महासंघों और संबंधित राज्य ग्रामीण आजीविका मिशन संरचना के अंतर्गत सामुदायिक संस्थाओं के माध्यम से दी जाती है।",
        "Eligible traditional artisans and craftspeople working in notified trades, subject to the scheme's age, family, occupation and other conditions.": "अधिसूचित ट्रेडों में काम करने वाले पात्र पारंपरिक कारीगर और शिल्पकार, योजना की आयु, परिवार, व्यवसाय और अन्य शर्तों के अधीन।",
        "Eligible farmers and other permitted agricultural-energy beneficiaries for the relevant PM-KUSUM component, subject to component, state and implementation conditions.": "संबंधित PM-KUSUM घटक के लिए पात्र किसान और अन्य अनुमत कृषि-ऊर्जा लाभार्थी, जो घटक, राज्य और कार्यान्वयन शर्तों के अधीन हैं।"
    },
    "Kannada": {
        "Generally for individuals aged 18+ starting a new eligible micro-enterprise. For projects above the prescribed PMEGP thresholds, minimum educational qualification conditions apply. Existing units are generally not eligible except specified cases under the scheme guidelines.": "ಸಾಮಾನ್ಯವಾಗಿ 18+ ವಯಸ್ಸಿನ ಹೊಸ ಅರ್ಹ ಸಣ್ಣ ಉದ್ಯಮವನ್ನು ಆರಂಭಿಸುವ ವ್ಯಕ್ತಿಗಳಿಗೆ. ನಿಗದಿತ PMEGP ಮಿತಿಗಿಂತ ಹೆಚ್ಚಿನ ಯೋಜನೆಗಳಿಗೆ ಕನಿಷ್ಠ ಶೈಕ್ಷಣಿಕ ಅರ್ಹತಾ ಷರತ್ತುಗಳು ಅನ್ವಯಿಸುತ್ತವೆ. ಯೋಜನೆ ಮಾರ್ಗಸೂಚಿಯಲ್ಲಿ ನಿರ್ದಿಷ್ಟಪಡಿಸಿದ ಸಂದರ್ಭಗಳನ್ನು ಹೊರತುಪಡಿಸಿ ಅಸ್ತಿತ್ವದಲ್ಲಿರುವ ಘಟಕಗಳು ಸಾಮಾನ್ಯವಾಗಿ ಅರ್ಹವಲ್ಲ.",
        "Eligible non-corporate micro enterprises in manufacturing, trading, services and allied agricultural activities such as dairy, poultry and beekeeping. Both new and existing eligible businesses may be considered subject to lender assessment.": "ಡೈರಿ, ಕೋಳಿ ಸಾಕಣೆ ಮತ್ತು ಜೇನು ಸಾಕಣೆ ಸೇರಿದಂತೆ ಉತ್ಪಾದನೆ, ವ್ಯಾಪಾರ, ಸೇವೆ ಮತ್ತು ಸಂಬಂಧಿತ ಕೃಷಿ ಚಟುವಟಿಕೆಗಳ ಅರ್ಹ ಕಾರ್ಪೊರೇಟ್ ಅಲ್ಲದ ಸಣ್ಣ ಉದ್ಯಮಗಳು. ಸಾಲದಾತರ ಪರಿಶೀಲನೆಗೆ ಒಳಪಟ್ಟು ಹೊಸ ಮತ್ತು ಅಸ್ತಿತ್ವದಲ್ಲಿರುವ ಅರ್ಹ ವ್ಯವಹಾರಗಳನ್ನು ಪರಿಗಣಿಸಬಹುದು.",
        "Eligible street vendors, including surveyed vendors and eligible vendors who can obtain a Certificate/ID of Vending or Letter of Recommendation through the prescribed process.": "ಸಮೀಕ್ಷೆಗೊಂಡ ಬೀದಿ ವ್ಯಾಪಾರಿಗಳು ಸೇರಿದಂತೆ ಅರ್ಹ ಬೀದಿ ವ್ಯಾಪಾರಿಗಳು ಮತ್ತು ನಿಗದಿತ ಪ್ರಕ್ರಿಯೆಯ ಮೂಲಕ ಮಾರಾಟ ಪ್ರಮಾಣಪತ್ರ/ಐಡಿ ಅಥವಾ ಶಿಫಾರಸು ಪತ್ರ ಪಡೆಯಬಹುದಾದ ಅರ್ಹ ವ್ಯಾಪಾರಿಗಳು.",
        "Eligible micro food-processing enterprises and other eligible categories under PMFME. For individual units, the scheme guidelines include conditions such as age, ownership, micro-enterprise status, contribution and eligible food-processing activity.": "PMFME ಅಡಿಯಲ್ಲಿ ಅರ್ಹ ಸಣ್ಣ ಆಹಾರ ಸಂಸ್ಕರಣಾ ಉದ್ಯಮಗಳು ಮತ್ತು ಇತರ ಅರ್ಹ ವರ್ಗಗಳು. ವೈಯಕ್ತಿಕ ಘಟಕಗಳಿಗೆ ವಯಸ್ಸು, ಮಾಲೀಕತ್ವ, ಸಣ್ಣ ಉದ್ಯಮ ಸ್ಥಿತಿ, ಕೊಡುಗೆ ಮತ್ತು ಅರ್ಹ ಆಹಾರ ಸಂಸ್ಕರಣಾ ಚಟುವಟಿಕೆಗಳಂತಹ ಷರತ್ತುಗಳು ಅನ್ವಯಿಸುತ್ತವೆ.",
        "Farmers including owner cultivators, eligible tenant farmers, oral lessees and sharecroppers; eligible SHGs/JLGs of farmers may also qualify, subject to bank and scheme conditions.": "ಭೂ ಮಾಲೀಕ ರೈತರು, ಅರ್ಹ ಬಾಡಿಗೆ ರೈತರು, ಮೌಖಿಕ ಗುತ್ತಿಗೆದಾರರು ಮತ್ತು ಪಾಲು ಬೆಳೆಗಾರರು ಸೇರಿದಂತೆ ರೈತರು; ರೈತರ ಅರ್ಹ SHG/JLGಗಳು ಬ್ಯಾಂಕ್ ಮತ್ತು ಯೋಜನೆ ಷರತ್ತುಗಳಿಗೆ ಒಳಪಟ್ಟು ಅರ್ಹರಾಗಬಹುದು.",
        "Eligible beneficiaries may include farmers, FPOs, PACS, SHGs, agri-entrepreneurs and other eligible entities undertaking permitted agriculture infrastructure projects, subject to the current AIF guidelines and lender appraisal.": "ಅರ್ಹ ಫಲಾನುಭವಿಗಳಲ್ಲಿ ರೈತರು, FPOಗಳು, PACS, SHGಗಳು, ಕೃಷಿ ಉದ್ಯಮಿಗಳು ಮತ್ತು ಅನುಮತಿಸಲಾದ ಕೃಷಿ ಮೂಲಸೌಕರ್ಯ ಯೋಜನೆಗಳನ್ನು ಕೈಗೊಳ್ಳುವ ಇತರ ಅರ್ಹ ಸಂಸ್ಥೆಗಳು ಸೇರಬಹುದು; ಪ್ರಸ್ತುತ AIF ಮಾರ್ಗಸೂಚಿ ಮತ್ತು ಸಾಲದಾತರ ಪರಿಶೀಲನೆ ಅನ್ವಯಿಸುತ್ತದೆ.",
        "Primarily for eligible agriculture and allied-sector graduates / qualified candidates who complete the prescribed training and establish eligible Agri-Clinic or Agri-Business Centre activities under current ACABC guidelines.": "ಮುಖ್ಯವಾಗಿ ಅರ್ಹ ಕೃಷಿ ಮತ್ತು ಸಂಬಂಧಿತ ಕ್ಷೇತ್ರದ ಪದವೀಧರರು/ಅರ್ಹ ಅಭ್ಯರ್ಥಿಗಳಿಗೆ; ಅವರು ನಿಗದಿತ ತರಬೇತಿಯನ್ನು ಪೂರ್ಣಗೊಳಿಸಿ ಪ್ರಸ್ತುತ ACABC ಮಾರ್ಗಸೂಚಿಗಳಂತೆ ಅರ್ಹ ಅಗ್ರಿ-ಕ್ಲಿನಿಕ್ ಅಥವಾ ಅಗ್ರಿ-ಬಿಸಿನೆಸ್ ಕೇಂದ್ರ ಚಟುವಟಿಕೆಗಳನ್ನು ಸ್ಥಾಪಿಸಬೇಕು.",
        "Rural livelihood support is delivered mainly through eligible Self Help Groups, their federations and community institutions under the applicable state rural livelihood mission structure.": "ಗ್ರಾಮೀಣ ಜೀವನೋಪಾಯ ಬೆಂಬಲವನ್ನು ಮುಖ್ಯವಾಗಿ ಅರ್ಹ ಸ್ವಸಹಾಯ ಗುಂಪುಗಳು, ಅವುಗಳ ಒಕ್ಕೂಟಗಳು ಮತ್ತು ಅನ್ವಯಿಸುವ ರಾಜ್ಯ ಗ್ರಾಮೀಣ ಜೀವನೋಪಾಯ ಮಿಷನ್ ವ್ಯವಸ್ಥೆಯ ಸಮುದಾಯ ಸಂಸ್ಥೆಗಳ ಮೂಲಕ ನೀಡಲಾಗುತ್ತದೆ.",
        "Eligible traditional artisans and craftspeople working in notified trades, subject to the scheme's age, family, occupation and other conditions.": "ಅಧಿಸೂಚಿತ ವೃತ್ತಿಗಳಲ್ಲಿ ಕೆಲಸ ಮಾಡುವ ಅರ್ಹ ಸಾಂಪ್ರದಾಯಿಕ ಕುಶಲಕರ್ಮಿಗಳು ಮತ್ತು ಶಿಲ್ಪಿಗಳು; ಯೋಜನೆಯ ವಯಸ್ಸು, ಕುಟುಂಬ, ವೃತ್ತಿ ಮತ್ತು ಇತರ ಷರತ್ತುಗಳಿಗೆ ಒಳಪಟ್ಟಿರುತ್ತಾರೆ.",
        "Eligible farmers and other permitted agricultural-energy beneficiaries for the relevant PM-KUSUM component, subject to component, state and implementation conditions.": "ಸಂಬಂಧಿತ PM-KUSUM ಘಟಕಕ್ಕೆ ಅರ್ಹ ರೈತರು ಮತ್ತು ಇತರ ಅನುಮತಿಸಲಾದ ಕೃಷಿ-ಶಕ್ತಿ ಫಲಾನುಭವಿಗಳು; ಘಟಕ, ರಾಜ್ಯ ಮತ್ತು ಅನುಷ್ಠಾನ ಷರತ್ತುಗಳಿಗೆ ಒಳಪಟ್ಟಿರುತ್ತಾರೆ."
    }
}

DETAIL_WORD_TR = {
    "Hindi": {
        "identity":"पहचान", "documents":"दस्तावेज़", "document":"दस्तावेज़", "promoters":"प्रवर्तक", "guarantors":"गारंटर", "applicant":"आवेदक", "applicable":"लागू", "where applicable":"जहाँ लागू हो", "if applicable":"यदि लागू हो", "required":"आवश्यक", "requested":"मांगा गया", "bank":"बैंक", "lender":"ऋणदाता", "financial":"वित्तीय", "information":"जानकारी", "business":"व्यवसाय", "enterprise":"उद्यम", "proof":"प्रमाण", "details":"विवरण", "account":"खाता", "land":"भूमि", "ownership":"स्वामित्व", "lease":"लीज़", "site":"स्थल", "project":"परियोजना", "report":"रिपोर्ट", "machinery":"मशीनरी", "equipment":"उपकरण", "estimates":"अनुमान", "quotations":"कोटेशन", "education":"शैक्षणिक", "qualification":"योग्यता", "training":"प्रशिक्षण", "certificate":"प्रमाणपत्र", "photograph":"फोटो", "signature":"हस्ताक्षर", "address":"पता", "income":"आय", "financial statements":"वित्तीय विवरण", "GST information":"GST जानकारी", "registration":"पंजीकरण", "records":"रिकॉर्ड", "group":"समूह", "members":"सदस्य", "resolution":"प्रस्ताव", "meeting":"बैठक", "trade":"व्यवसाय/ट्रेड", "artisan":"कारीगर", "self-declaration":"स्व-घोषणा", "verification":"सत्यापन", "supporting":"सहायक", "agricultural":"कृषि", "pump":"पंप", "electricity":"बिजली", "quotation":"कोटेशन", "implementing authority":"कार्यान्वयन प्राधिकरण", "KCC application form":"KCC आवेदन फॉर्म", "PAN card":"PAN कार्ड", "Aadhaar copy":"आधार प्रति", "Aadhaar-linked mobile details":"आधार से जुड़े मोबाइल विवरण", "bank account":"बैंक खाता", "passbook":"पासबुक", "Driving Licence":"ड्राइविंग लाइसेंस", "Voter ID":"मतदाता पहचान पत्र", "Passport":"पासपोर्ट", "MNREGA card":"मनरेगा कार्ड", "vendor ID":"विक्रेता आईडी", "Letter of Recommendation":"अनुशंसा पत्र"},
    "Kannada": {
        "identity":"ಗುರುತು", "documents":"ದಾಖಲೆಗಳು", "document":"ದಾಖಲೆ", "promoters":"ಪ್ರವರ್ತಕರು", "guarantors":"ಜಾಮೀನುದಾರರು", "applicant":"ಅರ್ಜಿದಾರ", "applicable":"ಅನ್ವಯಿಸಿದರೆ", "where applicable":"ಅನ್ವಯಿಸಿದಲ್ಲಿ", "if applicable":"ಅನ್ವಯಿಸಿದರೆ", "required":"ಅಗತ್ಯ", "requested":"ಕೋರಿದ", "bank":"ಬ್ಯಾಂಕ್", "lender":"ಸಾಲದಾತ", "financial":"ಹಣಕಾಸು", "information":"ಮಾಹಿತಿ", "business":"ವ್ಯವಹಾರ", "enterprise":"ಉದ್ಯಮ", "proof":"ಪುರಾವೆ", "details":"ವಿವರಗಳು", "account":"ಖಾತೆ", "land":"ಭೂಮಿ", "ownership":"ಮಾಲೀಕತ್ವ", "lease":"ಲೀಸ್", "site":"ಸ್ಥಳ", "project":"ಯೋಜನೆ", "report":"ವರದಿ", "machinery":"ಯಂತ್ರೋಪಕರಣ", "equipment":"ಉಪಕರಣಗಳು", "estimates":"ಅಂದಾಜುಗಳು", "quotations":"ಕೋಟೇಶನ್‌ಗಳು", "education":"ಶೈಕ್ಷಣಿಕ", "qualification":"ಅರ್ಹತೆ", "training":"ತರಬೇತಿ", "certificate":"ಪ್ರಮಾಣಪತ್ರ", "photograph":"ಫೋಟೋ", "signature":"ಸಹಿ", "address":"ವಿಳಾಸ", "income":"ಆದಾಯ", "financial statements":"ಹಣಕಾಸು ಹೇಳಿಕೆಗಳು", "GST information":"GST ಮಾಹಿತಿ", "registration":"ನೋಂದಣಿ", "records":"ದಾಖಲೆಗಳು", "group":"ಗುಂಪು", "members":"ಸದಸ್ಯರು", "resolution":"ನಿರ್ಣಯ", "meeting":"ಸಭೆ", "trade":"ವೃತ್ತಿ/ಟ್ರೇಡ್", "artisan":"ಕುಶಲಕರ್ಮಿ", "self-declaration":"ಸ್ವಯಂ ಘೋಷಣೆ", "verification":"ಪರಿಶೀಲನೆ", "supporting":"ಪೂರಕ", "agricultural":"ಕೃಷಿ", "pump":"ಪಂಪ್", "electricity":"ವಿದ್ಯುತ್", "quotation":"ಕೋಟೇಶನ್", "implementing authority":"ಅನುಷ್ಠಾನ ಪ್ರಾಧಿಕಾರ", "KCC application form":"KCC ಅರ್ಜಿ ನಮೂನೆ", "PAN card":"PAN ಕಾರ್ಡ್", "Aadhaar copy":"ಆಧಾರ್ ಪ್ರತಿ", "Aadhaar-linked mobile details":"ಆಧಾರ್‌ಗೆ ಲಿಂಕ್ ಮಾಡಿದ ಮೊಬೈಲ್ ವಿವರಗಳು", "bank account":"ಬ್ಯಾಂಕ್ ಖಾತೆ", "passbook":"ಪಾಸ್‌ಬುಕ್", "Driving Licence":"ಚಾಲನಾ ಪರವಾನಗಿ", "Voter ID":"ಮತದಾರರ ಗುರುತಿನ ಚೀಟಿ", "Passport":"ಪಾಸ್‌ಪೋರ್ಟ್", "MNREGA card":"ಮನರೇಗಾ ಕಾರ್ಡ್", "vendor ID":"ವ್ಯಾಪಾರಿ ಐಡಿ", "Letter of Recommendation":"ಶಿಫಾರಸು ಪತ್ರ"}
}

def scheme_document_text(value):
    exact = p1_detail_text(value)
    if exact != value:
        return exact
    result=value
    for src,dst in sorted(DETAIL_WORD_TR.get(language, {}).items(), key=lambda x: len(x[0]), reverse=True):
        result=result.replace(src,dst)
    return result

PERIOD_TR={
    "Hindi":{"month":"महीने","months":"महीने","first":"पहले","3–6 months":"3–6 महीने","6–12 months":"6–12 महीने"},
    "Kannada":{"month":"ತಿಂಗಳು","months":"ತಿಂಗಳು","first":"ಮೊದಲ","3–6 months":"3–6 ತಿಂಗಳು","6–12 months":"6–12 ತಿಂಗಳು"}
}

def period_text(value):
    result=value
    for src,dst in sorted(PERIOD_TR.get(language, {}).items(), key=lambda x: len(x[0]), reverse=True):
        result=result.replace(src,dst)
    return result

def scheme_eligibility_text(value):
    return SCHEME_ELIGIBILITY_TR.get(language, {}).get(value, value)

def p1_detail_text(value):
    # Common document labels used throughout the existing scheme module.
    common = {
        "Hindi": {"Aadhaar card":"आधार कार्ड", "Passport-size photographs":"पासपोर्ट आकार के फोटो", "Bank account details":"बैंक खाते का विवरण", "Project report":"परियोजना रिपोर्ट", "Caste / special-category certificate, if applicable":"जाति / विशेष श्रेणी प्रमाणपत्र, यदि लागू हो", "Rural-area certificate, if applicable":"ग्रामीण क्षेत्र प्रमाणपत्र, यदि लागू हो", "Highest educational qualification certificate, where applicable":"उच्चतम शैक्षणिक योग्यता प्रमाणपत्र, जहाँ लागू हो", "Other documents requested during application or bank appraisal":"आवेदन या बैंक मूल्यांकन में मांगे गए अन्य दस्तावेज़", "Aadhaar / identity proof":"आधार / पहचान प्रमाण", "Land ownership / lease or project-site proof, where applicable":"भूमि स्वामित्व / लीज या परियोजना स्थल का प्रमाण, जहाँ लागू हो", "Bank account details":"बैंक खाते का विवरण"},
        "Kannada": {"Aadhaar card":"ಆಧಾರ್ ಕಾರ್ಡ್", "Passport-size photographs":"ಪಾಸ್‌ಪೋರ್ಟ್ ಗಾತ್ರದ ಫೋಟೋಗಳು", "Bank account details":"ಬ್ಯಾಂಕ್ ಖಾತೆ ವಿವರಗಳು", "Project report":"ಯೋಜನಾ ವರದಿ", "Caste / special-category certificate, if applicable":"ಜಾತಿ / ವಿಶೇಷ ವರ್ಗ ಪ್ರಮಾಣಪತ್ರ, ಅನ್ವಯಿಸಿದರೆ", "Rural-area certificate, if applicable":"ಗ್ರಾಮೀಣ ಪ್ರದೇಶ ಪ್ರಮಾಣಪತ್ರ, ಅನ್ವಯಿಸಿದರೆ", "Highest educational qualification certificate, where applicable":"ಅತ್ಯುನ್ನತ ಶೈಕ್ಷಣಿಕ ಅರ್ಹತಾ ಪ್ರಮಾಣಪತ್ರ, ಅನ್ವಯಿಸಿದರೆ", "Other documents requested during application or bank appraisal":"ಅರ್ಜಿಯಲ್ಲಿ ಅಥವಾ ಬ್ಯಾಂಕ್ ಪರಿಶೀಲನೆಯಲ್ಲಿ ಕೇಳಬಹುದಾದ ಇತರೆ ದಾಖಲೆಗಳು", "Aadhaar / identity proof":"ಆಧಾರ್ / ಗುರುತಿನ ಪುರಾವೆ", "Land ownership / lease or project-site proof, where applicable":"ಭೂ ಮಾಲೀಕತ್ವ / ಲೀಸ್ ಅಥವಾ ಯೋಜನಾ ಸ್ಥಳದ ಪುರಾವೆ, ಅನ್ವಯಿಸಿದರೆ"}
    }
    return common.get(language, {}).get(value, value)

def p1_score_breakdown(business, capital, resources, interest, water, experience, location):
    low, high = business["capital"]
    if capital >= high: cap=30
    elif capital >= low: cap=25
    elif capital >= low*0.5: cap=12
    else: cap=3
    selected=[r for r in resources if r != "Not sure / I have limited resources"]
    br=business["resources"]
    matched=[r for r in selected if any(r.strip().lower()==x.strip().lower() for x in br)]
    res=round(20*len(matched)/len(br)) if matched else (3 if not selected else 5)
    intr=20 if interest in business["interests"] else 5
    wat=10 if (water=="Good" or "Water" not in br) else 6
    exp=10 if experience=="Experienced" else (8 if experience=="Some experience" else 5)
    loc=10 if location in business["locations"] else 2
    return {"capital":cap,"resource":res,"interest":intr,"water":wat,"experience":exp,"location":loc}, matched

def p1_risk_alerts(business, capital, location, selected_crop=None, season=None):
    alerts=[]
    if capital < business["capital"][0]: alerts.append(("high", p1("capital_alert")))
    water=location_water(location)
    if "Water" in business["resources"] and water=="Limited": alerts.append(("high", p1("water_alert")))
    if selected_crop:
        info=CROP_ADVISORY.get(selected_crop)
        if info:
            if season and season not in info["seasons"]: alerts.append(("medium", p1("season_alert")))
            if info["water"]=="Good" and water=="Limited": alerts.append(("high", p1("water_alert")))
            if info["harvest"].startswith(("9","10","6","7","8")): alerts.append(("medium", p1("long_crop")))
    alerts.append(("medium", p1("market_alert")))
    return alerts

def p1_compare_rows(kind, a, b, location, season):
    rows=[]
    if kind=="Businesses":
        A=next(x for x in BUSINESSES if x["name"]==a); B=next(x for x in BUSINESSES if x["name"]==b)
        rows=[(p1("capital_fit"), p1_business_content("investment", A["investment"]), p1_business_content("investment", B["investment"])), (p1("water_fit"), ui("required") if "Water" in A["resources"] else ui("not_central"), ui("required") if "Water" in B["resources"] else ui("not_central")), (p1("location_fit"), ui("included") if location in A["locations"] else ui("not_in_profile"), ui("included") if location in B["locations"] else ui("not_in_profile")), (p1("risk_title"), p1_business_content("risk", A["risk"]), p1_business_content("risk", B["risk"]))]
    else:
        A=CROP_ADVISORY[a]; B=CROP_ADVISORY[b]
        rows=[(p1("season"), ", ".join(ui_data(x, "season") for x in A["seasons"]), ", ".join(ui_data(x, "season") for x in B["seasons"])), (p1("water_context"), ui_data(A["water"], "water"), ui_data(B["water"], "water")), (ui("compare_harvest"), A["harvest"], B["harvest"]), ("Location fit", ui("included") if location in A["locations"] else ui("not_in_profile"), ui("included") if location in B["locations"] else ui("not_in_profile")), (ui("compare_suitability"), f"{crop_suitability(a,location,season)}%", f"{crop_suitability(b,location,season)}%"), (p1("risk_title"), p1_business_content("risk", A["risk"]), p1_business_content("risk", B["risk"]))]
    return rows

# ============================================================
# LOCATION-BASED ANIMAL BREED & CARE ADVISOR
# ============================================================
# These are prototype location associations for the hackathon demo.
# They are advisory suggestions, not a substitute for local veterinary advice.
# Breed associations are kept regional rather than claiming that a breed is
# the only or universally best choice for that location.
ANIMAL_ADVISORY = {
    "Dairy / Milk-Based Business": {
        "default": {
            "animal": "Dairy cattle",
            "breed": "Suitable local/crossbred dairy cattle selected with the local veterinary department",
            "why": "Breed choice should consider local climate, feed availability, milk market and veterinary support.",
            "care": [
                "Provide clean drinking water throughout the day.",
                "Give balanced feed with adequate green fodder, dry fodder and minerals.",
                "Keep the shed clean, dry, shaded and well ventilated.",
                "Follow vaccination, deworming and reproductive-health schedules advised by a veterinarian.",
                "Record milk yield, feed costs, breeding dates and animal health."
            ]
        },
        "Shivamogga": {
            "animal": "Dairy cattle",
            "breed": "Malnad Gidda",
            "why": "ICAR identifies Malnad Gidda as a cattle breed from the Western Ghats of Karnataka and notes its use for milk and manure.",
            "care": [
                "Provide clean water and good-quality local fodder.",
                "Keep animals in a clean, dry and well-ventilated shed, especially during wet weather.",
                "Maintain regular vaccination, deworming and veterinary check-ups.",
                "Monitor body condition, milk yield and signs of disease daily."
            ]
        },
        "Hubballi": {
            "animal": "Dairy cattle",
            "breed": "Krishna Valley / locally adapted dairy cattle",
            "why": "Krishna Valley cattle are associated with Karnataka and have been included in Karnataka cattle-development and conservation work.",
            "care": [
                "Plan fodder supply before increasing herd size.",
                "Provide shade, ventilation and clean water during hot periods.",
                "Vaccinate and deworm according to local veterinary advice.",
                "Maintain milk-yield and feed-cost records for each animal."
            ]
        },
        "Dharwad": {
            "animal": "Dairy cattle",
            "breed": "Krishna Valley / locally adapted dairy cattle",
            "why": "Krishna Valley cattle are associated with Karnataka and are relevant to the broader North Karnataka livestock context.",
            "care": [
                "Use locally available green and dry fodder with mineral supplementation as advised.",
                "Provide shade and continuous access to clean water.",
                "Keep housing clean and dry and isolate sick animals.",
                "Follow veterinary vaccination and deworming schedules."
            ]
        },
        "Belagavi": {
            "animal": "Dairy cattle",
            "breed": "Krishna Valley / locally adapted dairy cattle",
            "why": "Krishna Valley cattle are a Karnataka cattle genetic resource and are relevant to North Karnataka livestock systems.",
            "care": [
                "Balance fodder, concentrate and minerals according to animal stage and milk yield.",
                "Provide clean water and heat protection.",
                "Maintain hygienic milking practices.",
                "Vaccinate and seek veterinary help promptly when animals show illness."
            ]
        },
        "Haveri": {
            "animal": "Dairy cattle",
            "breed": "Krishna Valley / locally adapted dairy cattle",
            "why": "A locally adapted cattle type can reduce management mismatch; confirm the final breed choice with the local veterinary officer.",
            "care": [
                "Keep adequate fodder reserves for dry periods.",
                "Provide shade, clean water and good ventilation.",
                "Maintain clean milking and housing routines.",
                "Keep vaccination, deworming and health records."
            ]
        },
        "Vijayapura": {
            "animal": "Dairy cattle",
            "breed": "Locally adapted North Karnataka dairy cattle / Krishna Valley type",
            "why": "The hotter, drier setting makes locally adapted cattle and reliable water/fodder planning important.",
            "care": [
                "Prioritize shade and reliable drinking water during hot months.",
                "Store dry fodder and plan green-fodder availability.",
                "Use veterinary-recommended vaccination and deworming schedules.",
                "Avoid overcrowding and keep the shed well ventilated."
            ]
        },
        "Kalaburagi": {
            "animal": "Dairy cattle",
            "breed": "Deoni / locally adapted North Karnataka cattle",
            "why": "Deoni is a recognized cattle type associated with the North Karnataka–Marathwada region; final selection should be based on local availability and veterinary advice.",
            "care": [
                "Provide extra heat protection and plenty of clean water in hot weather.",
                "Plan dry-fodder storage before summer.",
                "Maintain vaccination, deworming and breeding records.",
                "Check animals daily for fever, poor appetite, lameness or reduced milk yield."
            ]
        },
        "Raichur": {
            "animal": "Dairy cattle",
            "breed": "Locally adapted North Karnataka dairy cattle / Krishna Valley type",
            "why": "Local climate, fodder and water availability should guide the final breed selection.",
            "care": [
                "Provide shade and frequent access to clean water.",
                "Store dry fodder for periods of shortage.",
                "Keep housing clean and well ventilated.",
                "Follow local veterinary vaccination and deworming advice."
            ]
        },
        "Gadag": {
            "animal": "Dairy cattle",
            "breed": "Locally adapted North Karnataka dairy cattle / Krishna Valley type",
            "why": "The advisory prioritizes locally adapted cattle with careful fodder and water planning.",
            "care": [
                "Plan water and fodder before purchasing animals.",
                "Provide shade and ventilation during hot weather.",
                "Maintain clean milking and housing practices.",
                "Use regular veterinary health checks."
            ]
        },
        "Davanagere": {
            "animal": "Dairy cattle",
            "breed": "Locally adapted dairy cattle / Krishna Valley type",
            "why": "The final breed should be selected according to local feed resources, climate and milk market.",
            "care": [
                "Maintain balanced feeding and clean water access.",
                "Keep the shed dry, clean and ventilated.",
                "Follow vaccination and deworming schedules.",
                "Track milk yield and treatment history."
            ]
        },
        "Tumakuru": {
            "animal": "Dairy cattle",
            "breed": "Hallikar / locally adapted dairy cattle",
            "why": "Hallikar is a Karnataka cattle breed; for a milk-focused unit, confirm whether the selected animals fit the intended milk-production system.",
            "care": [
                "Choose healthy animals with good body condition and verified health history.",
                "Provide clean water and sufficient fodder.",
                "Keep housing shaded, dry and ventilated.",
                "Use a veterinarian for vaccination, breeding and disease treatment."
            ]
        },
        "Chitradurga": {
            "animal": "Dairy cattle",
            "breed": "Hallikar / locally adapted cattle",
            "why": "Hallikar is a recognized Karnataka cattle breed; the final choice should match whether the enterprise is milk, breeding or draught focused.",
            "care": [
                "Ensure water and fodder availability before expanding the herd.",
                "Protect animals from heat and provide shade.",
                "Keep the shed clean and dry.",
                "Follow veterinary vaccination and deworming schedules."
            ]
        }
    },
    "Goat / Sheep Rearing": {
        "default": {
            "animal": "Goat / sheep",
            "breed": "Locally adapted meat or dual-purpose goat/sheep breed",
            "why": "Choose animals that match the local climate, fodder, disease pressure and nearby market.",
            "care": [
                "Provide a dry, raised or well-drained shelter with good ventilation.",
                "Provide clean water and adequate green/dry fodder.",
                "Follow vaccination and deworming schedules advised by a veterinarian.",
                "Quarantine newly purchased animals before mixing them with the flock.",
                "Keep records of breeding, births, deaths, treatments and weight gain."
            ]
        },
        "Hubballi": {"animal":"Sheep","breed":"Madgyal sheep (Karnataka/Maharashtra region)","why":"ICAR-NBAGR lists Madgyal sheep with a home tract spanning Maharashtra and Karnataka.","care":["Use a dry, ventilated night shelter.","Provide clean water and adequate fodder; avoid sudden feed changes.","Follow local vaccination and deworming advice.","Separate sick animals quickly and maintain flock records."]},
        "Dharwad": {"animal":"Sheep","breed":"Madgyal sheep (Karnataka/Maharashtra region)","why":"ICAR-NBAGR lists Madgyal sheep with a home tract spanning Maharashtra and Karnataka.","care":["Keep the flock dry and protected from heavy rain.","Provide clean water and balanced fodder.","Follow veterinary vaccination and deworming schedules.","Record breeding, lambing and health events."]},
        "Belagavi": {"animal":"Sheep","breed":"Madgyal sheep (Karnataka/Maharashtra region)","why":"Madgyal is a registered sheep breed whose home tract includes Karnataka and Maharashtra.","care":["Provide dry shelter and good drainage.","Maintain clean water and regular feeding.","Follow local veterinary vaccination and parasite-control advice.","Quarantine newly purchased sheep before flock entry."]},
        "Vijayapura": {"animal":"Sheep","breed":"Madgyal / locally adapted Deccan sheep","why":"The advisory prioritizes a locally adapted sheep type; Madgyal has a Karnataka/Maharashtra home tract according to ICAR-NBAGR.","care":["Use a dry, well-ventilated shelter.","Plan fodder and water carefully during dry periods.","Follow vaccination and deworming schedules.","Monitor body condition and separate sick animals."]},
        "Kalaburagi": {"animal":"Sheep","breed":"Locally adapted Deccan sheep / Madgyal type","why":"For a dry North Karnataka setting, locally adapted sheep with reliable fodder and veterinary support are preferable; confirm breed availability locally.","care":["Provide shade and reliable water during hot weather.","Store dry fodder for lean periods.","Maintain parasite control and vaccination with veterinary guidance.","Keep the shelter clean and dry."]},
        "Raichur": {"animal":"Sheep","breed":"Locally adapted Deccan sheep / Madgyal type","why":"A locally adapted flock can fit dry conditions better when fodder, water and veterinary support are planned.","care":["Provide shade and water in hot weather.","Maintain dry shelter and good drainage.","Follow vaccination and deworming schedules.","Record flock health and weight gain."]},
        "Gadag": {"animal":"Sheep","breed":"Locally adapted Deccan sheep / Madgyal type","why":"Dryland conditions make hardy, locally adapted sheep and careful fodder planning important.","care":["Maintain dry shelter and shade.","Store fodder before dry periods.","Provide clean water daily.","Use veterinary advice for vaccination and parasite control."]},
        "Haveri": {"animal":"Sheep","breed":"Madgyal / locally adapted Karnataka sheep","why":"Madgyal has a Karnataka/Maharashtra home tract; final breed choice should consider local availability and farm conditions.","care":["Keep the flock dry during wet periods.","Provide balanced fodder and clean water.","Follow vaccination and deworming schedules.","Quarantine newly purchased animals."]},
        "Davanagere": {"animal":"Sheep","breed":"Locally adapted Karnataka/Deccan sheep","why":"Select a breed that fits local fodder availability, climate and meat-market demand.","care":["Provide clean water and a dry shelter.","Maintain a regular parasite-control programme.","Avoid overcrowding.","Keep breeding and health records."]},
        "Tumakuru": {"animal":"Sheep / goat","breed":"Locally adapted Karnataka sheep or goat","why":"The best choice depends on local fodder, water and market demand; confirm availability with the local livestock department.","care":["Provide a dry, ventilated shelter.","Give clean water and balanced fodder.","Follow veterinary vaccination and deworming advice.","Quarantine new animals."]},
        "Chitradurga": {"animal":"Sheep","breed":"Locally adapted Deccan sheep","why":"Dryland conditions make locally adapted sheep and fodder planning important.","care":["Provide shade and clean water.","Store dry fodder for lean periods.","Maintain dry shelter and parasite control.","Record flock health and breeding performance."]},
        "Mysuru": {"animal":"Goat / sheep","breed":"Locally adapted Karnataka goat or sheep","why":"Select based on the local market and fodder system rather than choosing a breed only by name.","care":["Keep housing clean, dry and ventilated.","Provide clean water and balanced fodder.","Follow veterinary vaccination and deworming schedules.","Monitor body condition and isolate sick animals."]},
        "Bengaluru": {"animal":"Goat / sheep","breed":"Locally adapted goat/sheep for peri-urban demand","why":"For peri-urban units, market access, housing space, feed cost and waste management are especially important.","care":["Maintain clean, well-drained housing.","Provide clean water and adequate feed.","Control parasites and follow veterinary schedules.","Maintain strict hygiene and waste management."]},
        "Shivamogga": {"animal":"Goat / sheep","breed":"Locally adapted Karnataka goat/sheep","why":"Higher-rainfall areas need extra attention to dry housing, drainage and parasite control.","care":["Keep shelters dry and well drained.","Avoid prolonged wetness of hooves and bedding.","Follow deworming and vaccination advice.","Provide clean water and balanced fodder."]}
    },
    "Poultry Farming": {
        "default": {
            "animal": "Chicken",
            "breed": "Giriraja / suitable backyard or commercial poultry variety",
            "why": "Giriraja has been used in Karnataka backyard poultry programmes; final variety should match the egg/meat objective and local market.",
            "care": [
                "Provide clean, dry, well-ventilated housing with protection from predators.",
                "Use balanced feed and continuous access to clean water.",
                "Follow a veterinarian-recommended vaccination programme.",
                "Maintain biosecurity, clean equipment and controlled visitor access.",
                "Separate sick birds and keep records of mortality, feed and egg/meat output."
            ]
        },
        "Shivamogga": {"animal":"Chicken","breed":"Giriraja / suitable backyard poultry variety","why":"ICAR programmes in Karnataka have distributed Giriraja birds and promoted scientific backyard poultry management.","care":["Use dry, ventilated housing and good drainage.","Provide balanced feed and clean water.","Follow vaccination and biosecurity schedules.","Monitor birds daily for illness and mortality."]},
        "Bengaluru": {"animal":"Chicken","breed":"Giriraja or another approved backyard/commercial variety","why":"Choose the variety based on available space, production goal and local market demand.","care":["Use hygienic housing with good ventilation.","Control smell, waste and flies in peri-urban areas.","Maintain vaccination and biosecurity.","Track feed cost and egg/meat output."]},
        "Hubballi": {"animal":"Chicken","breed":"Giriraja / suitable dual-purpose variety","why":"Giriraja is used in Karnataka backyard poultry programmes and can be considered for a small mixed enterprise.","care":["Provide dry shelter, balanced feed and clean water.","Follow vaccination and biosecurity routines.","Protect chicks from cold/heat stress.","Record feed use, mortality and production."]},
        "Dharwad": {"animal":"Chicken","breed":"Giriraja / suitable dual-purpose variety","why":"A dual-purpose backyard variety can fit a small rural unit when local demand and veterinary support are available.","care":["Maintain clean, dry housing.","Provide balanced feed and water.","Follow vaccination schedules.","Separate sick birds and maintain flock records."]}
    }
}

ANIMAL_TEXT_TR = {
    "Hindi": {
        "Dairy cattle":"दूध देने वाले पशु", "Chicken":"मुर्गी", "Goat / sheep":"बकरी / भेड़",
        "Suitable local/crossbred dairy cattle selected with the local veterinary department":"स्थानीय पशु चिकित्सा विभाग की सलाह से चुने गए उपयुक्त स्थानीय/क्रॉसब्रेड दूध देने वाले पशु",
        "Dairy cattle": "दूध देने वाले पशु",
        "Provide clean drinking water throughout the day.":"पूरे दिन साफ पीने का पानी दें।", "Give balanced feed with adequate green fodder, dry fodder and minerals.":"पर्याप्त हरे चारे, सूखे चारे और खनिजों के साथ संतुलित आहार दें।", "Keep the shed clean, dry, shaded and well ventilated.":"शेड को साफ, सूखा, छायादार और हवादार रखें।", "Follow vaccination, deworming and reproductive-health schedules advised by a veterinarian.":"पशु चिकित्सक की सलाह के अनुसार टीकाकरण, कृमिनाशक और प्रजनन स्वास्थ्य कार्यक्रम का पालन करें।", "Record milk yield, feed costs, breeding dates and animal health.":"दूध उत्पादन, चारा लागत, प्रजनन तिथि और पशु स्वास्थ्य का रिकॉर्ड रखें।",
        "Breed choice should consider local climate, feed availability, milk market and veterinary support.":"नस्ल चुनते समय स्थानीय जलवायु, चारे की उपलब्धता, दूध बाजार और पशु चिकित्सा सहायता को ध्यान में रखें।",
        "Keep the shed clean, dry and well ventilated, especially during wet weather.":"विशेषकर बारिश के मौसम में शेड को साफ, सूखा और हवादार रखें।", "Maintain regular vaccination, deworming and veterinary check-ups.":"नियमित टीकाकरण, कृमिनाशक और पशु चिकित्सा जांच कराएं।", "Monitor body condition, milk yield and signs of disease daily.":"हर दिन शरीर की स्थिति, दूध उत्पादन और बीमारी के संकेत देखें।",
        "Dairy cattle": "दूध देने वाले पशु", "Goat / sheep":"बकरी / भेड़",
        "Locally adapted meat or dual-purpose goat/sheep breed":"स्थानीय परिस्थितियों के अनुकूल मांस या दोहरे उपयोग की बकरी/भेड़ नस्ल", "Choose animals that match the local climate, fodder, disease pressure and nearby market.":"स्थानीय जलवायु, चारे, रोग जोखिम और नजदीकी बाजार के अनुसार पशु चुनें।",
        "Provide a dry, raised or well-drained shelter with good ventilation.":"अच्छी हवा वाली सूखी, ऊंची या अच्छी जल निकासी वाली जगह उपलब्ध कराएं।", "Provide clean water and adequate green/dry fodder.":"साफ पानी और पर्याप्त हरा/सूखा चारा दें।", "Follow vaccination and deworming schedules advised by a veterinarian.":"पशु चिकित्सक की सलाह के अनुसार टीकाकरण और कृमिनाशक कार्यक्रम का पालन करें।", "Quarantine newly purchased animals before mixing them with the flock.":"नए खरीदे पशुओं को झुंड में मिलाने से पहले अलग रखें।", "Keep records of breeding, births, deaths, treatments and weight gain.":"प्रजनन, जन्म, मृत्यु, उपचार और वजन बढ़ने का रिकॉर्ड रखें।",
        "Chicken":"मुर्गी", "Provide clean, dry, well-ventilated housing with protection from predators.":"शिकारियों से सुरक्षा के साथ साफ, सूखा और हवादार आवास दें।", "Use balanced feed and continuous access to clean water.":"संतुलित आहार और लगातार साफ पानी उपलब्ध रखें।", "Follow a veterinarian-recommended vaccination programme.":"पशु चिकित्सक द्वारा सुझाए गए टीकाकरण कार्यक्रम का पालन करें।", "Maintain biosecurity, clean equipment and controlled visitor access.":"जैव-सुरक्षा, साफ उपकरण और नियंत्रित आगंतुक प्रवेश बनाए रखें।", "Separate sick birds and keep records of mortality, feed and egg/meat output.":"बीमार पक्षियों को अलग रखें और मृत्यु, चारा तथा अंडा/मांस उत्पादन का रिकॉर्ड रखें।"
    },
    "Kannada": {
        "Dairy cattle":"ಹಾಲು ಕೊಡುವ ಜಾನುವಾರು", "Chicken":"ಕೋಳಿ", "Goat / sheep":"ಮೇಕೆ / ಕುರಿ",
        "Suitable local/crossbred dairy cattle selected with the local veterinary department":"ಸ್ಥಳೀಯ ಪಶುವೈದ್ಯ ಇಲಾಖೆಯ ಸಲಹೆಯೊಂದಿಗೆ ಆಯ್ಕೆ ಮಾಡಿದ ಸೂಕ್ತ ಸ್ಥಳೀಯ/ಕ್ರಾಸ್‌ಬ್ರೀಡ್ ಹಾಲು ಜಾನುವಾರು",
        "Provide clean drinking water throughout the day.":"ದಿನವಿಡೀ ಸ್ವಚ್ಛ ಕುಡಿಯುವ ನೀರನ್ನು ಒದಗಿಸಿ.", "Give balanced feed with adequate green fodder, dry fodder and minerals.":"ಸಾಕಷ್ಟು ಹಸಿರು ಮೇವು, ಒಣ ಮೇವು ಮತ್ತು ಖನಿಜಗಳೊಂದಿಗೆ ಸಮತೋಲನ ಆಹಾರ ನೀಡಿ.", "Keep the shed clean, dry, shaded and well ventilated.":"ಶೆಡ್ ಅನ್ನು ಸ್ವಚ್ಛ, ಒಣ, ನೆರಳಿನ ಮತ್ತು ಗಾಳಿಯಾಡುವಂತೆ ಇಡಿ.", "Follow vaccination, deworming and reproductive-health schedules advised by a veterinarian.":"ಪಶುವೈದ್ಯರು ಸೂಚಿಸುವ ಲಸಿಕೆ, ಹುಳು ನಿವಾರಣೆ ಮತ್ತು ಸಂತಾನೋತ್ಪತ್ತಿ ಆರೋಗ್ಯ ವೇಳಾಪಟ್ಟಿಯನ್ನು ಪಾಲಿಸಿ.", "Record milk yield, feed costs, breeding dates and animal health.":"ಹಾಲಿನ ಉತ್ಪಾದನೆ, ಮೇವು ವೆಚ್ಚ, ಸಂತಾನೋತ್ಪತ್ತಿ ದಿನಾಂಕ ಮತ್ತು ಜಾನುವಾರು ಆರೋಗ್ಯದ ದಾಖಲೆ ಇಡಿ.",
        "Breed choice should consider local climate, feed availability, milk market and veterinary support.":"ತಳಿ ಆಯ್ಕೆ ಮಾಡುವಾಗ ಸ್ಥಳೀಯ ಹವಾಮಾನ, ಮೇವು ಲಭ್ಯತೆ, ಹಾಲಿನ ಮಾರುಕಟ್ಟೆ ಮತ್ತು ಪಶುವೈದ್ಯ ಸಹಾಯವನ್ನು ಪರಿಗಣಿಸಿ.", "Maintain regular vaccination, deworming and veterinary check-ups.":"ನಿಯಮಿತ ಲಸಿಕೆ, ಹುಳು ನಿವಾರಣೆ ಮತ್ತು ಪಶುವೈದ್ಯಕೀಯ ತಪಾಸಣೆಗಳನ್ನು ಮಾಡಿ.", "Monitor body condition, milk yield and signs of disease daily.":"ಪ್ರತಿದಿನ ದೇಹದ ಸ್ಥಿತಿ, ಹಾಲಿನ ಉತ್ಪಾದನೆ ಮತ್ತು ರೋಗದ ಲಕ್ಷಣಗಳನ್ನು ಗಮನಿಸಿ.",
        "Locally adapted meat or dual-purpose goat/sheep breed":"ಸ್ಥಳೀಯ ಪರಿಸ್ಥಿತಿಗೆ ಹೊಂದಿಕೊಂಡ ಮಾಂಸ ಅಥವಾ ದ್ವಿ-ಉದ್ದೇಶದ ಮೇಕೆ/ಕುರಿ ತಳಿ", "Choose animals that match the local climate, fodder, disease pressure and nearby market.":"ಸ್ಥಳೀಯ ಹವಾಮಾನ, ಮೇವು, ರೋಗದ ಅಪಾಯ ಮತ್ತು ಹತ್ತಿರದ ಮಾರುಕಟ್ಟೆಗೆ ಹೊಂದುವ ಪ್ರಾಣಿಗಳನ್ನು ಆಯ್ಕೆಮಾಡಿ.", "Provide a dry, raised or well-drained shelter with good ventilation.":"ಉತ್ತಮ ಗಾಳಿಯಾಟವಿರುವ ಒಣ, ಎತ್ತರದ ಅಥವಾ ಉತ್ತಮ ನೀರು ಹರಿವು ಇರುವ ಆಶ್ರಯ ಒದಗಿಸಿ.", "Provide clean water and adequate green/dry fodder.":"ಸ್ವಚ್ಛ ನೀರು ಮತ್ತು ಸಾಕಷ್ಟು ಹಸಿರು/ಒಣ ಮೇವು ನೀಡಿ.", "Follow vaccination and deworming schedules advised by a veterinarian.":"ಪಶುವೈದ್ಯರ ಸಲಹೆಯಂತೆ ಲಸಿಕೆ ಮತ್ತು ಹುಳು ನಿವಾರಣೆ ವೇಳಾಪಟ್ಟಿಯನ್ನು ಪಾಲಿಸಿ.", "Quarantine newly purchased animals before mixing them with the flock.":"ಹೊಸದಾಗಿ ಖರೀದಿಸಿದ ಪ್ರಾಣಿಗಳನ್ನು ಹಿಂಡಿಗೆ ಸೇರಿಸುವ ಮೊದಲು ಪ್ರತ್ಯೇಕವಾಗಿ ಇಡಿ.", "Keep records of breeding, births, deaths, treatments and weight gain.":"ಸಂತಾನೋತ್ಪತ್ತಿ, ಜನನ, ಸಾವು, ಚಿಕಿತ್ಸೆ ಮತ್ತು ತೂಕದ ಹೆಚ್ಚಳದ ದಾಖಲೆ ಇಡಿ.",
        "Provide clean, dry, well-ventilated housing with protection from predators.":"ಶಿಕಾರಿಗಳಿಂದ ರಕ್ಷಣೆ ಇರುವ ಸ್ವಚ್ಛ, ಒಣ ಮತ್ತು ಗಾಳಿಯಾಡುವ ವಾಸಸ್ಥಳ ಒದಗಿಸಿ.", "Use balanced feed and continuous access to clean water.":"ಸಮತೋಲನ ಆಹಾರ ಮತ್ತು ನಿರಂತರ ಸ್ವಚ್ಛ ನೀರಿನ ಲಭ್ಯತೆ ಒದಗಿಸಿ.", "Follow a veterinarian-recommended vaccination programme.":"ಪಶುವೈದ್ಯರು ಸೂಚಿಸಿದ ಲಸಿಕೆ ಕಾರ್ಯಕ್ರಮವನ್ನು ಪಾಲಿಸಿ.", "Maintain biosecurity, clean equipment and controlled visitor access.":"ಜೈವಿಕ ಭದ್ರತೆ, ಸ್ವಚ್ಛ ಉಪಕರಣಗಳು ಮತ್ತು ನಿಯಂತ್ರಿತ ಭೇಟಿ ವ್ಯವಸ್ಥೆ ಕಾಪಾಡಿ.", "Separate sick birds and keep records of mortality, feed and egg/meat output.":"ಅನಾರೋಗ್ಯದ ಪಕ್ಷಿಗಳನ್ನು ಪ್ರತ್ಯೇಕಿಸಿ ಮತ್ತು ಸಾವು, ಮೇವು ಹಾಗೂ ಮೊಟ್ಟೆ/ಮಾಂಸ ಉತ್ಪಾದನೆಯ ದಾಖಲೆ ಇಡಿ."
    }
}

def animal_text(value):
    return ANIMAL_TEXT_TR.get(language, {}).get(value, value)

def get_animal_advisory(business_name, location):
    profile = ANIMAL_ADVISORY.get(business_name)
    if not profile:
        return None
    return profile.get(location, profile.get("default"))



# ============================================================
# PRIORITY 2 — RURAL INTELLIGENCE HUB
# ============================================================

if page == "Rural Intelligence Hub":
    st.markdown(f'''<div class="animated-hero"><div class="hero-orb one"></div><div class="hero-orb two"></div><div class="hero-orb three"></div><h1>🌾 {p2("hub")}</h1><p>{p2("hub_desc")}</p><span class="hero-badge">⚡ {p2("live")} + 🧠 {ui("prototype")}</span></div>''', unsafe_allow_html=True)

    hub_tabs = st.tabs(["🌦️ " + p2("weather"), "🗺️ " + p2("map"), "🎙️ " + p2("voice"), "🐄 " + p2("livestock")])

    # ---------------- WEATHER ----------------
    with hub_tabs[0]:
        page_banner("🌦️", p2("weather"), p2("weather_desc"))
        wx = fetch_weather(location)
        if wx["ok"]:
            current_w=wx["data"]["current"]
            daily=wx["data"]["daily"]
            temp=current_w.get("temperature_2m",0); feels=current_w.get("apparent_temperature",0)
            code=current_w.get("weather_code",0); humidity=current_w.get("relative_humidity_2m",0); wind=current_w.get("wind_speed_10m",0)
            st.markdown(f'''<div class="weather-card"><div class="status-pill">🟢 {p2("live")}</div><div style="margin-top:.8rem"><span style="font-size:2.4rem">{weather_icon(code)}</span> <span class="weather-temp">{temp:.0f}°C</span></div><h3>{weather_text(weather_code_text(code))}</h3><p>{ui_data(location,"location_name")} • {datetime.now().strftime("%d %b %Y")}</p></div>''', unsafe_allow_html=True)
            a,b,c,d=st.columns(4)
            a.metric(p2("feels"),f"{feels:.0f}°C"); b.metric(p2("humidity"),f"{humidity}%"); c.metric(p2("wind"),f"{wind:.0f} km/h"); d.metric(p2("rain"),f"{daily['precipitation_probability_max'][0]}%")
            st.markdown(f"### 📅 {p2('forecast')}")
            rows=[]
            for i,date in enumerate(daily["time"]):
                rows.append({p2("date"):date,p2("weather_col"):f"{weather_icon(daily['weather_code'][i])} {weather_text(weather_code_text(daily['weather_code'][i]))}",p2("min_temp"):round(daily['temperature_2m_min'][i],1),p2("max_temp"):round(daily['temperature_2m_max'][i],1),p2("rain_percent"):daily['precipitation_probability_max'][i],p2("rain_mm"):round(daily['precipitation_sum'][i],1)})
            st.dataframe(pd.DataFrame(rows), use_container_width=True, hide_index=True)

            st.markdown(f"### 🌱 {p2('today_advice')}")
            top=best_crops_for_location(location,current_season(),limit=3)
            if top:
                crop=top[0][0]
                risk=crop_text(CROP_ADVISORY[crop]["risk"])
                st.markdown(f'''<div class="feature-card"><div class="feature-icon">🌱</div><h4>{tr_data(crop)} — {crop_suitability(crop,location,current_season())}% {ui('compare_suitability').lower()}</h4><p><b>{p2('crop_signal')}:</b> {weather_text(weather_code_text(code))}. {p2('water_signal')}: {ui_data(location_water(location),'water')}.</p><p><b>{ui('main_risk')}:</b> {risk}</p></div>''', unsafe_allow_html=True)
            st.caption(p2("weather_note"))
        else:
            st.warning(p2("no_weather"))
            st.markdown(f"<div class='feature-card'><div class='feature-icon'>🛰️</div><h4>{p2('fallback')}</h4><p>{p2('weather_note')}</p></div>", unsafe_allow_html=True)
        if st.button("🔄 " + p2("refresh"), key="p2_weather_refresh"):
            fetch_weather.clear()
            st.rerun()

    # ---------------- OPPORTUNITY MAP ----------------
    with hub_tabs[1]:
        page_banner("🗺️", p2("map"), p2("map_desc"))
        map_rows=[]
        for loc,(lat,lon) in LOCATION_COORDS.items():
            score,local,biz,water=opportunity_score(loc)
            map_rows.append({"Location":ui_data(loc,"location_name"),"latitude":lat,"longitude":lon,"Opportunity index":score,"Local crops":local,"Business profiles":biz,"Water":ui_data(water,"water")})
        map_df=pd.DataFrame(map_rows)
        st.markdown(f"<div class='map-card'><h4>📍 {p2('map_selected')}: {ui_data(location,'location_name')}</h4><p>{p2('map_note')}</p></div>", unsafe_allow_html=True)
        st.map(map_df[["latitude","longitude"]], zoom=6, use_container_width=True)
        score,local,biz,water=opportunity_score(location)
        a,b,c,d=st.columns(4)
        a.metric(p2("opportunity_index"),score); b.metric(p2("local_crops"),local); c.metric(p2("businesses"),biz); d.metric(p2("water"),ui_data(water,"water"))
        st.markdown(f"### 💡 {p2('opportunity')}")
        s,top_crop,water_msg=opportunity_advice(location)
        st.markdown(f'''<div class="feature-card"><div class="feature-icon">🌾</div><h4>{ui_data(location,"location_name")}: {s}/100</h4><p><b>{p2('local_crops')}:</b> {top_crop} + {max(local-1,0)} {p2("other_profiles")}.</p><p>{water_msg}</p><p><b>{p2('next')}:</b> {p2("validate")}</p></div>''', unsafe_allow_html=True)
        st.dataframe(map_df, use_container_width=True, hide_index=True)

    # ---------------- VOICE ----------------
    with hub_tabs[2]:
        page_banner("🎙️", p2("voice"), p2("voice_desc"))

        VOICE_LANGS = ["English", "Hindi", "Kannada"]
        VOICE_LANG_CODES = {"English": "en-IN", "Hindi": "hi-IN", "Kannada": "kn-IN"}
        VOICE_LANG_LABELS = {"English": "English", "Hindi": "हिंदी", "Kannada": "ಕನ್ನಡ"}

        # ---- multilingual helpers (independent of the sidebar language) ----
        def v_data(value, lang):
            return value if lang == "English" else DATA_TR.get(lang, {}).get(value, value)

        def v_ui(value, kind, lang):
            return UI_TR.get(lang, UI_TR["English"]).get(kind, {}).get(value, value)

        def v_crop_text(value, lang):
            return value if lang == "English" else CROP_TEXT_TR.get(lang, {}).get(value, value)

        def v_business(name, lang):
            return name if lang == "English" else P1_BUSINESS_TR.get(lang, {}).get(name, name)

        def v_scheme_name(name, lang):
            return name if lang == "English" else SCHEME_NAME_TR.get(lang, {}).get(name, name)

        def v_scheme_extra(kind, value, lang):
            return value if lang == "English" else SCHEME_EXTRA_TR.get(lang, {}).get(kind, {}).get(value, value)

        def v_scheme_text(kind, value, lang):
            return value if lang == "English" else SCHEME_TR.get(lang, {}).get(kind, {}).get(value, value)

        VOICE_WEATHER_TR = {
            "English": {},
            "Hindi": {"Clear sky": "साफ आकाश", "Mainly clear": "मुख्यतः साफ", "Partly cloudy": "आंशिक बादल", "Overcast": "बादल छाए", "Fog": "कोहरा", "Slight rain": "हल्की बारिश", "Moderate rain": "मध्यम बारिश", "Heavy rain": "तेज़ बारिश", "Rain showers": "बारिश की बौछारें", "Thunderstorm": "गरज के साथ बारिश", "Light drizzle": "हल्की बूंदाबांदी", "Moderate drizzle": "मध्यम बूंदाबांदी", "Variable conditions": "बदलता मौसम"},
            "Kannada": {"Clear sky": "ಸ್ವಚ್ಛ ಆಕಾಶ", "Mainly clear": "ಮುಖ್ಯವಾಗಿ ಸ್ವಚ್ಛ", "Partly cloudy": "ಭಾಗಶಃ ಮೋಡ", "Overcast": "ಮೋಡ ಕವಿದ", "Fog": "ಮಂಜು", "Slight rain": "ಸಣ್ಣ ಮಳೆ", "Moderate rain": "ಮಧ್ಯಮ ಮಳೆ", "Heavy rain": "ಭಾರಿ ಮಳೆ", "Rain showers": "ಮಳೆಯ ತುಂತುರು", "Thunderstorm": "ಗುಡುಗು ಸಹಿತ ಮಳೆ", "Light drizzle": "ಸಣ್ಣ ತುಂತುರು", "Moderate drizzle": "ಮಧ್ಯಮ ತುಂತುರು", "Variable conditions": "ಬದಲಾಗುವ ಹವಾಮಾನ"},
        }
        VOICE_UNIT_TR = {
            "English": {"kg": "kg", "piece": "piece"},
            "Hindi": {"kg": "किलो", "piece": "नग"},
            "Kannada": {"kg": "ಕೆ.ಜಿ", "piece": "ಒಂದಕ್ಕೆ"},
        }

        # Spoken-form aliases so the assistant recognises common ways
        # people actually say a crop name in English/Hindi/Kannada.
        VOICE_CROP_ALIASES = {
            "Tomato": ["tamatar", "tomoto", "tamota", "ಟೊಮೇಟೊ", "ಟೊಮ್ಯಾಟೊ", "टमाटर"],
            "Onion": ["pyaz", "pyaaz", "eerulli", "erulli", "ಈರುಳ್ಳಿ", "प्याज"],
            "Potato": ["aloo", "alu", "aalu", "alugadde", "ಆಲೂಗಡ್ಡೆ"],
            "Carrot": ["gajar", "ಗಜ್ಜರಿ"],
            "Beans": ["bean", "hurali", "ಬೀನ್ಸ್"],
            "Brinjal": ["baingan", "badanekai", "eggplant", "ಬದನೆ"],
            "Cabbage": ["patta gobhi", "elekosu", "ಎಲೆಕೋಸು"],
            "Cauliflower": ["phool gobhi", "hookosu", "ಹೂಕೋಸು"],
            "Green Chilli": ["hari mirch", "hasi menasu", "ಹಸಿ ಮೆಣಸು"],
            "Chilli": ["mirchi", "mirch", "menasinakai", "byadgi", "ಮೆಣಸು"],
            "Lady Finger": ["bhindi", "okra", "bendekai", "ಬೆಂಡೆ"],
            "Maize": ["makka", "corn", "mekkejola", "ಜೋಳ ಮೆಕ್ಕೆ"],
            "Wheat": ["gehu", "godhi", "ಗೋಧಿ"],
            "Rice": ["chawal", "paddy", "akki", "batta", "ಅಕ್ಕಿ"],
            "Ragi": ["finger millet", "raagi", "ರಾಗಿ"],
            "Jowar": ["sorghum", "jola", "ಜೋಳ"],
            "Bajra": ["pearl millet", "sajje", "ಸಜ್ಜೆ"],
            "Groundnut": ["peanut", "moongphali", "mungfali", "kadalekai", "ಕಡಲೆಕಾಯಿ"],
            "Sunflower": ["surajmukhi", "suryakanti", "ಸೂರ್ಯಕಾಂತಿ"],
            "Soybean": ["soya", "ಸೋಯಾ"],
            "Tur": ["toor", "arhar", "tur dal", "togari", "ತೊಗರಿ"],
            "Green Gram": ["moong", "mung", "hesaru", "ಹೆಸರು"],
            "Black Gram": ["urad", "uddu", "ಉದ್ದು"],
            "Bengal Gram": ["chana", "kadale", "ಕಡಲೆ"],
            "Cotton": ["kapas", "hatti", "ಹತ್ತಿ"],
            "Sugarcane": ["ganna", "kabbu", "ಕಬ್ಬು"],
            "Turmeric": ["haldi", "arishina", "ಅರಿಶಿನ"],
            "Ginger": ["adrak", "shunti", "ಶುಂಠಿ"],
            "Garlic": ["lahsun", "bellulli", "ಬೆಳ್ಳುಳ್ಳಿ"],
            "Coconut": ["nariyal", "tenginakai", "ತೆಂಗಿನಕಾಯಿ"],
            "Banana": ["kela", "balehannu", "ಬಾಳೆ"],
            "Mango": ["aam", "mavu", "ಮಾವಿನ"],
            "Papaya": ["papita", "pappaya", "ಪಪ್ಪಾಯಿ"],
            "Guava": ["amrud", "seebekai", "ಸೀಬೆ"],
            "Spinach": ["palak", "ಪಾಲಕ್"],
            "Coriander": ["dhaniya", "kottambari", "ಕೊತ್ತಂಬರಿ"],
            "Peas": ["matar", "batani", "ಬಟಾಣಿ"],
            "Capsicum": ["shimla mirch", "bell pepper", "donne menasu"],
            "Cucumber": ["kheera", "southekai", "ಸೌತೆ"],
            "Drumstick": ["sahjan", "nuggekai", "ನುಗ್ಗೆ"],
            "Beetroot": ["chukandar"],
            "Radish": ["mooli", "mulangi", "ಮೂಲಂಗಿ"],
            "Pumpkin": ["kaddu", "kumbalakai"],
            "Bottle Gourd": ["lauki", "sorekai"],
            "Bitter Gourd": ["karela", "hagalakai"],
            "Fenugreek Leaves": ["methi", "menthya"],
        }

        VOICE_SCHEME_ALIASES = {
            "PMEGP – Prime Minister's Employment Generation Programme": ["pmegp", "employment generation", "पीएमईजीपी"],
            "Pradhan Mantri MUDRA Yojana (PMMY)": ["mudra", "pmmy", "मुद्रा", "ಮುದ್ರಾ", "shishu", "kishor", "tarun"],
            "PM SVANidhi": ["svanidhi", "swanidhi", "street vendor", "स्वनिधि", "ಬೀದಿ ವ್ಯಾಪಾರಿ"],
            "PMFME – Pradhan Mantri Formalisation of Micro Food Processing Enterprises": ["pmfme", "food processing", "खाद्य प्रसंस्करण", "ಆಹಾರ ಸಂಸ್ಕರಣ"],
            "Kisan Credit Card (KCC)": ["kisan credit", "kcc", "किसान क्रेडिट", "ಕಿಸಾನ್ ಕ್ರೆಡಿಟ್"],
            "Agriculture Infrastructure Fund (AIF)": ["infrastructure fund", "aif", "इंफ्रास्ट्रक्चर"],
            "Agri-Clinics and Agri-Business Centres (ACABC)": ["agri clinic", "acabc", "agri business centre"],
            "DAY-NRLM – Deendayal Antyodaya Yojana": ["nrlm", "deendayal", "self help group", "shg", "स्वयं सहायता", "ಸ್ವಸಹಾಯ"],
            "PM Vishwakarma": ["vishwakarma", "artisan", "विश्वकर्मा", "ವಿಶ್ವಕರ್ಮ"],
            "PM-KUSUM": ["kusum", "solar", "सोलर", "ಸೌರ"],
        }

        VOICE_ANIMAL_ALIASES = {
            "Dairy / Milk-Based Business": ["dairy", "cow", "milk", "buffalo", "डेयरी", "गाय", "दूध", "भैंस", "ಹಸು", "ಹಾಲು", "ಡೈರಿ", "ಎಮ್ಮೆ"],
            "Goat / Sheep Rearing": ["goat", "sheep", "बकरी", "भेड़", "ಮೇಕೆ", "ಕುರಿ"],
            "Poultry Farming": ["poultry", "hen", "chicken", "egg", "मुर्गी", "अंडा", "ಕೋಳಿ", "ಮೊಟ್ಟೆ"],
        }

        # ---- build the knowledge base that the browser engine answers from ----
        voice_season = current_season()

        voice_locations = {}
        for loc_key in LOCATION_COORDS.keys():
            loc_names = {lg: (loc_key if lg == "English" else v_ui(loc_key, "location_name", lg)) for lg in VOICE_LANGS}
            voice_locations[loc_key] = {
                "names": loc_names,
                "aliases": sorted({loc_key.lower()} | {n.lower() for n in loc_names.values()}),
                "factor": LOCATION_FACTOR.get(loc_key, 1.0),
                "local": LOCAL_CROPS.get(loc_key, []),
                "water_key": location_water(loc_key),
                "water": {lg: v_ui(location_water(loc_key), "water", lg) for lg in VOICE_LANGS},
                "score": opportunity_score(loc_key)[0],
            }

        voice_crops = []
        for crop_key, crop_info in CROP_DATA.items():
            crop_names = {lg: v_data(crop_key, lg) for lg in VOICE_LANGS}
            alias_set = {crop_key.lower()} | {n.lower() for n in crop_names.values()}
            alias_set |= {a.lower() for a in VOICE_CROP_ALIASES.get(crop_key, [])}
            entry = {
                "key": crop_key,
                "names": crop_names,
                "aliases": sorted(alias_set, key=len, reverse=True),
                "base": crop_info["price"],
                "unit": {lg: VOICE_UNIT_TR[lg][crop_info["unit"]] for lg in VOICE_LANGS},
                "trend": {lg: v_data(crop_info["trend"], lg) for lg in VOICE_LANGS},
                "category": {lg: v_data(crop_info["category"], lg) for lg in VOICE_LANGS},
            }
            advisory = CROP_ADVISORY.get(crop_key)
            if advisory:
                entry["advisory"] = {
                    "seasons": advisory["seasons"],
                    "locations": advisory["locations"],
                    "success": advisory["success"],
                    "harvest": advisory["harvest"],
                    "risk": {lg: v_crop_text(advisory["risk"], lg) for lg in VOICE_LANGS},
                }
            voice_crops.append(entry)

        def v_trim(text):
            """Drop the trailing full stop so templates can add their own."""
            return text.rstrip().rstrip(".।|")

        voice_schemes = []
        for scheme in SCHEMES:
            voice_schemes.append({
                "names": {lg: v_scheme_name(scheme["name"], lg) for lg in VOICE_LANGS},
                "best": {lg: v_trim(v_scheme_text("best", scheme["best_for"], lg)) for lg in VOICE_LANGS},
                "key": {lg: v_trim(v_scheme_extra("key", scheme["key"], lg)) for lg in VOICE_LANGS},
                "aliases": sorted({a.lower() for a in VOICE_SCHEME_ALIASES.get(scheme["name"], [])} | {scheme["name"].lower()}, key=len, reverse=True),
            })

        voice_animals = []
        for animal_name, alias_list in VOICE_ANIMAL_ALIASES.items():
            herd_n, setup_c, monthly_c, income_c = livestock_defaults(animal_name)
            voice_animals.append({
                "names": {lg: v_business(animal_name, lg) for lg in VOICE_LANGS},
                "aliases": sorted({a.lower() for a in alias_list}, key=len, reverse=True),
                "n": herd_n, "setup": setup_c, "monthly": monthly_c, "income": income_c,
                "margin": (income_c - monthly_c) * herd_n,
            })

        voice_weather = None
        vw = fetch_weather(location)
        if vw["ok"]:
            vw_cur = vw["data"]["current"]
            vw_daily = vw["data"]["daily"]
            vw_code_text = weather_code_text(vw_cur.get("weather_code", 0))
            voice_weather = {
                "temp": round(float(vw_cur.get("temperature_2m", 0))),
                "feels": round(float(vw_cur.get("apparent_temperature", 0))),
                "humidity": round(float(vw_cur.get("relative_humidity_2m", 0))),
                "wind": round(float(vw_cur.get("wind_speed_10m", 0))),
                "rain": vw_daily["precipitation_probability_max"][0],
                "rain_tomorrow": vw_daily["precipitation_probability_max"][1] if len(vw_daily["precipitation_probability_max"]) > 1 else None,
                "tmin": round(float(vw_daily["temperature_2m_min"][0])),
                "tmax": round(float(vw_daily["temperature_2m_max"][0])),
                "cond": {lg: (vw_code_text if lg == "English" else VOICE_WEATHER_TR[lg].get(vw_code_text, vw_code_text)) for lg in VOICE_LANGS},
            }

        voice_kb = {
            "selected": location,
            "season": {lg: v_ui(voice_season, "season", lg) for lg in VOICE_LANGS},
            "locations": voice_locations,
            "crops": voice_crops,
            "schemes": voice_schemes,
            "animals": voice_animals,
            "weather": voice_weather,
            "langCodes": VOICE_LANG_CODES,
        }

        # ---- spoken answer templates ----
        VOICE_SAY = {
            "English": {
                "price": "In {loc}, {crop} is about {price} rupees per {unit}. The price trend is {trend}.{localNote}",
                "local_note": " {crop} is one of the locally grown crops there.",
                "price_list": "Sample prices in {loc} right now: {list}.",
                "crop_unknown": "I could not find that crop. You can ask about {list}.",
                "weather": "In {loc} it is {temp} degrees with {cond}. Humidity {humidity} percent, wind {wind} kilometres per hour. Rain chance today is {rain} percent, and today's range is {tmin} to {tmax} degrees.",
                "weather_off": "Live weather is not available right now for {loc}. Please check the Weather tab again in a moment.",
                "weather_other": " I have live weather only for the selected location, {loc}.",
                "water": "Water availability in {loc} is {water}.",
                "best": "For {loc} in the {season} season, the most suitable crops are {list}.",
                "suit": "{crop} suits {loc} in the {season} season at about {score} out of 100. Harvest takes {harvest}. Main risk is {risk}.",
                "scheme": "{name}. Best for {best}. Key point: {key}.",
                "scheme_list": "Relevant schemes are {list}. Ask me about any one of them by name.",
                "animal": "{animal}: a starting plan of {n} animals or birds, setup {setup} rupees each, monthly cost {monthly} rupees each and monthly income {income} rupees each. That is an illustrative monthly margin of about {margin} rupees.",
                "opportunity": "The prototype opportunity index for {loc} is {score} out of 100, with {crops} local crop profiles and {water} water availability.",
                "greet": "Namaste. I am Gram Sahayak. Ask me a crop price, the weather, water, which crop to grow, a government scheme, or livestock economics.",
                "help": "Try asking: what is the price of tomato, what is the weather today, which crop should I grow, how is the water here, or tell me about the Mudra scheme.",
                "disclaimer": "Prices are Gram Sahayak sample data, not live mandi rates.",
                "heard": "I heard",
                "idle": "Tap the microphone and ask your question.",
                "listening": "Listening...",
                "not_supported": "Speech recognition is not supported by this browser. Type your question below instead.",
                "mic_error": "Microphone error",
                "type_placeholder": "Or type your question here...",
                "ask": "Ask",
                "stop_speaking": "Stop speaking",
                "repeat": "Repeat",
                "answer": "Answer",
                "reply_lang": "Answer language",
                "no_voice": "No speech voice is installed for this language on this device, so the answer is shown as text.",
                "examples": "Examples",
            },
            "Hindi": {
                "price": "{loc} में {crop} का भाव लगभग {price} रुपये प्रति {unit} है। कीमत का रुझान: {trend}।{localNote}",
                "local_note": " {crop} वहाँ की स्थानीय फसलों में से एक है।",
                "price_list": "{loc} में अभी के नमूना भाव: {list}।",
                "crop_unknown": "यह फसल मुझे नहीं मिली। आप इनके बारे में पूछ सकते हैं: {list}।",
                "weather": "{loc} में अभी {temp} डिग्री तापमान है और मौसम {cond} है। नमी {humidity} प्रतिशत, हवा {wind} किलोमीटर प्रति घंटा। आज बारिश की संभावना {rain} प्रतिशत है और तापमान {tmin} से {tmax} डिग्री रहेगा।",
                "weather_off": "{loc} के लिए अभी लाइव मौसम उपलब्ध नहीं है। थोड़ी देर बाद मौसम टैब देखें।",
                "weather_other": " लाइव मौसम केवल चयनित स्थान {loc} के लिए उपलब्ध है।",
                "water": "{loc} में पानी की उपलब्धता {water} है।",
                "best": "{loc} में {season} सीज़न के लिए सबसे उपयुक्त फसलें हैं: {list}।",
                "suit": "{season} सीज़न में {loc} के लिए {crop} की उपयुक्तता लगभग {score} में से 100 है। फसल तैयार होने में {harvest} लगते हैं। मुख्य जोखिम: {risk}।",
                "scheme": "{name}। किसके लिए: {best}। मुख्य बात: {key}।",
                "scheme_list": "प्रमुख योजनाएँ हैं: {list}। किसी भी योजना का नाम लेकर पूछें।",
                "animal": "{animal}: शुरुआती योजना {n} पशु या पक्षी, प्रति पशु सेटअप लागत {setup} रुपये, मासिक लागत {monthly} रुपये और मासिक आय {income} रुपये। अनुमानित मासिक मार्जिन लगभग {margin} रुपये।",
                "opportunity": "{loc} का प्रोटोटाइप अवसर सूचकांक {score} में से 100 है, {crops} स्थानीय फसल प्रोफाइल और {water} पानी उपलब्धता के साथ।",
                "greet": "नमस्ते। मैं ग्राम सहायक हूँ। मुझसे फसल का भाव, मौसम, पानी, कौन सी फसल लगाएँ, सरकारी योजना या पशुपालन के बारे में पूछें।",
                "help": "ऐसे पूछें: टमाटर का भाव क्या है, आज मौसम कैसा है, कौन सी फसल लगाऊँ, यहाँ पानी कैसा है, या मुद्रा योजना के बारे में बताओ।",
                "disclaimer": "भाव ग्राम सहायक का नमूना डेटा है, लाइव मंडी भाव नहीं।",
                "heard": "मैंने सुना",
                "idle": "माइक्रोफोन दबाकर अपना सवाल पूछें।",
                "listening": "सुन रहा हूँ...",
                "not_supported": "इस ब्राउज़र में स्पीच रिकग्निशन समर्थित नहीं है। नीचे टाइप करके पूछें।",
                "mic_error": "माइक्रोफोन त्रुटि",
                "type_placeholder": "या यहाँ अपना सवाल लिखें...",
                "ask": "पूछें",
                "stop_speaking": "बोलना रोकें",
                "repeat": "दोहराएँ",
                "answer": "उत्तर",
                "reply_lang": "उत्तर की भाषा",
                "no_voice": "इस डिवाइस पर इस भाषा की आवाज़ उपलब्ध नहीं है, इसलिए उत्तर केवल टेक्स्ट में दिखाया गया है।",
                "examples": "उदाहरण",
            },
            "Kannada": {
                "price": "{loc}ನಲ್ಲಿ {crop} ಬೆಲೆ ಪ್ರತಿ {unit} ಗೆ ಸುಮಾರು {price} ರೂಪಾಯಿ. ಬೆಲೆಯ ಪ್ರವೃತ್ತಿ {trend}.{localNote}",
                "local_note": " {crop} ಅಲ್ಲಿನ ಸ್ಥಳೀಯ ಬೆಳೆಗಳಲ್ಲಿ ಒಂದು.",
                "price_list": "{loc}ನಲ್ಲಿ ಈಗಿನ ಮಾದರಿ ಬೆಲೆಗಳು: {list}.",
                "crop_unknown": "ಆ ಬೆಳೆ ಸಿಗಲಿಲ್ಲ. ನೀವು ಇವುಗಳ ಬಗ್ಗೆ ಕೇಳಬಹುದು: {list}.",
                "weather": "{loc}ನಲ್ಲಿ ಈಗ {temp} ಡಿಗ್ರಿ ಇದೆ, ಹವಾಮಾನ {cond}. ಆರ್ದ್ರತೆ {humidity} ಶೇಕಡಾ, ಗಾಳಿ {wind} ಕಿಲೋಮೀಟರ್. ಇಂದು ಮಳೆಯ ಸಾಧ್ಯತೆ {rain} ಶೇಕಡಾ, ತಾಪಮಾನ {tmin} ರಿಂದ {tmax} ಡಿಗ್ರಿ.",
                "weather_off": "{loc}ಗೆ ಸದ್ಯ ಲೈವ್ ಹವಾಮಾನ ಲಭ್ಯವಿಲ್ಲ. ಸ್ವಲ್ಪ ಸಮಯದ ನಂತರ ಹವಾಮಾನ ಟ್ಯಾಬ್ ನೋಡಿ.",
                "weather_other": " ಲೈವ್ ಹವಾಮಾನ ಆಯ್ಕೆ ಮಾಡಿದ ಸ್ಥಳ {loc}ಗೆ ಮಾತ್ರ ಲಭ್ಯ.",
                "water": "{loc}ನಲ್ಲಿ ನೀರಿನ ಲಭ್ಯತೆ {water}.",
                "best": "{season} ಋತುವಿನಲ್ಲಿ {loc}ಗೆ ಸೂಕ್ತವಾದ ಬೆಳೆಗಳು: {list}.",
                "suit": "{season} ಋತುವಿನಲ್ಲಿ {loc}ಗೆ {crop} ಸೂಕ್ತತೆ ಸುಮಾರು 100 ಕ್ಕೆ {score}. ಕೊಯ್ಲಿಗೆ {harvest} ಬೇಕು. ಮುಖ್ಯ ಅಪಾಯ: {risk}.",
                "scheme": "{name}. ಯಾರಿಗೆ: {best}. ಮುಖ್ಯ ಅಂಶ: {key}.",
                "scheme_list": "ಮುಖ್ಯ ಯೋಜನೆಗಳು: {list}. ಯಾವುದೇ ಯೋಜನೆಯ ಹೆಸರು ಹೇಳಿ ಕೇಳಿ.",
                "animal": "{animal}: ಆರಂಭಿಕ ಯೋಜನೆ {n} ಪ್ರಾಣಿ ಅಥವಾ ಪಕ್ಷಿ, ಪ್ರತಿಯೊಂದಕ್ಕೆ ಆರಂಭಿಕ ವೆಚ್ಚ {setup} ರೂಪಾಯಿ, ಮಾಸಿಕ ವೆಚ್ಚ {monthly} ರೂಪಾಯಿ ಮತ್ತು ಮಾಸಿಕ ಆದಾಯ {income} ರೂಪಾಯಿ. ಅಂದಾಜು ಮಾಸಿಕ ಮಾರ್ಜಿನ್ ಸುಮಾರು {margin} ರೂಪಾಯಿ.",
                "opportunity": "{loc}ನ ಪ್ರೋಟೋಟೈಪ್ ಅವಕಾಶ ಸೂಚ್ಯಂಕ 100 ಕ್ಕೆ {score}, {crops} ಸ್ಥಳೀಯ ಬೆಳೆ ಪ್ರೊಫೈಲ್‌ಗಳು ಮತ್ತು {water} ನೀರಿನ ಲಭ್ಯತೆಯೊಂದಿಗೆ.",
                "greet": "ನಮಸ್ಕಾರ. ನಾನು ಗ್ರಾಮ ಸಹಾಯಕ. ಬೆಳೆ ಬೆಲೆ, ಹವಾಮಾನ, ನೀರು, ಯಾವ ಬೆಳೆ ಬೆಳೆಯಬೇಕು, ಸರ್ಕಾರಿ ಯೋಜನೆ ಅಥವಾ ಪಶುಸಂಗೋಪನೆ ಬಗ್ಗೆ ಕೇಳಿ.",
                "help": "ಹೀಗೆ ಕೇಳಿ: ಟೊಮ್ಯಾಟೊ ಬೆಲೆ ಎಷ್ಟು, ಇಂದಿನ ಹವಾಮಾನ ಹೇಗಿದೆ, ಯಾವ ಬೆಳೆ ಬೆಳೆಯಲಿ, ಇಲ್ಲಿ ನೀರು ಹೇಗಿದೆ, ಅಥವಾ ಮುದ್ರಾ ಯೋಜನೆ ಬಗ್ಗೆ ಹೇಳಿ.",
                "disclaimer": "ಬೆಲೆಗಳು ಗ್ರಾಮ ಸಹಾಯಕದ ಮಾದರಿ ಡೇಟಾ, ಲೈವ್ ಮಾರುಕಟ್ಟೆ ದರ ಅಲ್ಲ.",
                "heard": "ನಾನು ಕೇಳಿದ್ದು",
                "idle": "ಮೈಕ್ರೋಫೋನ್ ಒತ್ತಿ ನಿಮ್ಮ ಪ್ರಶ್ನೆ ಕೇಳಿ.",
                "listening": "ಕೇಳುತ್ತಿದೆ...",
                "not_supported": "ಈ ಬ್ರೌಸರ್‌ನಲ್ಲಿ ಸ್ಪೀಚ್ ರೆಕಗ್ನಿಷನ್ ಬೆಂಬಲಿತವಿಲ್ಲ. ಕೆಳಗೆ ಟೈಪ್ ಮಾಡಿ ಕೇಳಿ.",
                "mic_error": "ಮೈಕ್ರೋಫೋನ್ ದೋಷ",
                "type_placeholder": "ಅಥವಾ ಇಲ್ಲಿ ನಿಮ್ಮ ಪ್ರಶ್ನೆ ಬರೆಯಿರಿ...",
                "ask": "ಕೇಳಿ",
                "stop_speaking": "ಮಾತು ನಿಲ್ಲಿಸಿ",
                "repeat": "ಪುನಃ ಹೇಳಿ",
                "answer": "ಉತ್ತರ",
                "reply_lang": "ಉತ್ತರದ ಭಾಷೆ",
                "no_voice": "ಈ ಸಾಧನದಲ್ಲಿ ಈ ಭಾಷೆಯ ಧ್ವನಿ ಇಲ್ಲ, ಆದ್ದರಿಂದ ಉತ್ತರ ಪಠ್ಯವಾಗಿ ತೋರಿಸಲಾಗಿದೆ.",
                "examples": "ಉದಾಹರಣೆಗಳು",
            },
        }

        VOICE_INTENTS = {
            "price": ["price", "rate", "cost", "how much", "market", "selling", "sell", "bhav", "भाव", "कीमत", "दाम", "रेट", "बाजार", "बाज़ार", "कितना", "कितने", "ಬೆಲೆ", "ದರ", "ರೇಟ್", "ಎಷ್ಟು", "ಮಾರುಕಟ್ಟೆ"],
            "weather": ["weather", "rain", "temperature", "forecast", "hot", "climate", "मौसम", "बारिश", "तापमान", "गर्मी", "ಹವಾಮಾನ", "ಮಳೆ", "ತಾಪಮಾನ", "ಬಿಸಿಲು"],
            "water": ["water", "irrigation", "borewell", "groundwater", "पानी", "जल", "सिंचाई", "ನೀರು", "ನೀರಾವರಿ"],
            "grow": ["which crop", "what crop", "should i grow", "grow", "sow", "plant", "cultivate", "suitable", "best crop", "recommend", "कौन सी फसल", "बोऊँ", "बोना", "उगा", "लगाऊ", "लगाऊँ", "खेती", "उपयुक्त", "ಯಾವ ಬೆಳೆ", "ಬೆಳೆಯ", "ಬಿತ್ತ", "ಸೂಕ್ತ", "ಕೃಷಿ"],
            "scheme": ["scheme", "loan", "subsidy", "government", "bank", "credit", "yojana", "योजना", "ऋण", "कर्ज", "सब्सिडी", "सरकारी", "लोन", "ಯೋಜನೆ", "ಸಾಲ", "ಸಬ್ಸಿಡಿ", "ಸರ್ಕಾರಿ", "ಬ್ಯಾಂಕ್"],
            "animal": ["dairy", "cow", "buffalo", "goat", "sheep", "poultry", "hen", "chicken", "egg", "milk", "livestock", "डेयरी", "गाय", "भैंस", "बकरी", "भेड़", "मुर्गी", "अंडा", "दूध", "पशु", "ಹಸು", "ಎಮ್ಮೆ", "ಮೇಕೆ", "ಕುರಿ", "ಕೋಳಿ", "ಮೊಟ್ಟೆ", "ಹಾಲು", "ಡೈರಿ", "ಪಶು"],
            "opportunity": ["opportunity", "business", "start", "invest", "अवसर", "व्यवसाय", "व्यापार", "शुरू", "ಅವಕಾಶ", "ವ್ಯವಹಾರ", "ಪ್ರಾರಂಭ"],
            "greet": ["hello", "hi", "hey", "namaste", "namaskara", "नमस्ते", "हैलो", "ನಮಸ್ಕಾರ", "ಹಲೋ"],
            "help": ["help", "what can you do", "मदद", "क्या कर सकते", "ಸಹಾಯ", "ಏನು ಮಾಡಬಹುದು"],
        }

        VOICE_EXAMPLES = {
            "English": ["What is the price of tomato?", "What is the weather today?", "Which crop should I grow?", "Tell me about the Mudra scheme", "How is the water here?"],
            "Hindi": ["टमाटर का भाव क्या है?", "आज मौसम कैसा है?", "कौन सी फसल लगाऊँ?", "मुद्रा योजना के बारे में बताओ", "यहाँ पानी कैसा है?"],
            "Kannada": ["ಟೊಮ್ಯಾಟೊ ಬೆಲೆ ಎಷ್ಟು?", "ಇಂದಿನ ಹವಾಮಾನ ಹೇಗಿದೆ?", "ಯಾವ ಬೆಳೆ ಬೆಳೆಯಲಿ?", "ಮುದ್ರಾ ಯೋಜನೆ ಬಗ್ಗೆ ಹೇಳಿ", "ಇಲ್ಲಿ ನೀರು ಹೇಗಿದೆ?"],
        }

        VOICE_ENGINE_HTML = r'''
<div class="voice-card">
  <div class="voice-mic" id="micOrb">🎙️</div>
  <h3 style="text-align:center;margin-top:1rem">__TITLE__</h3>

  <div style="display:flex;gap:8px;justify-content:center;margin:.9rem 0 .2rem" id="langRow"></div>
  <div style="text-align:center;font-size:.8rem;color:#8a8fa3" id="langLabel"></div>

  <div style="display:flex;gap:10px;justify-content:center;flex-wrap:wrap;margin:1rem 0">
    <button id="start" class="vbtn">🎙️ <span id="startTxt"></span></button>
    <button id="stop" class="vbtn">⏹️ <span id="stopTxt"></span></button>
    <button id="repeat" class="vbtn">🔁 <span id="repeatTxt"></span></button>
    <button id="mute" class="vbtn">🔇 <span id="muteTxt"></span></button>
  </div>

  <div id="status" style="text-align:center;color:#667085;min-height:1.2rem"></div>

  <div style="display:flex;gap:8px;margin-top:1rem">
    <input id="typed" type="text" style="flex:1;padding:12px 14px;border-radius:12px;border:1px solid #e3e3ef;font-size:1rem" />
    <button id="ask" class="vbtn" style="background:#7c4dff;color:#fff;border-color:#7c4dff"></button>
  </div>

  <div id="heard" style="margin-top:1rem;padding:.9rem 1rem;background:#fff;border-radius:14px;border:1px solid #eee;display:none"></div>

  <div id="reply" style="margin-top:.8rem;padding:1rem;background:#fff;border-radius:14px;border:1px solid #eee">
    <b id="replyLabel"></b><br><span id="replyText">—</span>
    <div id="replyNote" style="margin-top:.6rem;font-size:.78rem;color:#8a8fa3"></div>
  </div>

  <div style="margin-top:.9rem">
    <div style="font-size:.8rem;color:#8a8fa3;margin-bottom:.4rem" id="exLabel"></div>
    <div id="chips" style="display:flex;flex-wrap:wrap;gap:6px"></div>
  </div>
</div>

<style>
  .vbtn{padding:11px 16px;border-radius:12px;border:1px solid #e3e3ef;background:#fff;cursor:pointer;font-size:.95rem}
  .vbtn:hover{border-color:#7c4dff}
  .langpill{padding:7px 14px;border-radius:999px;border:1px solid #e3e3ef;background:#fff;cursor:pointer;font-size:.9rem}
  .langpill.active{background:#7c4dff;color:#fff;border-color:#7c4dff}
  .chip{padding:6px 11px;border-radius:999px;border:1px solid #ece7f7;background:#fbf9ff;cursor:pointer;font-size:.82rem}
  .chip:hover{border-color:#7c4dff}
</style>

<script>
const KB = __KB__;
const SAY = __SAY__;
const INTENTS = __INTENTS__;
const EXAMPLES = __EXAMPLES__;
const LANG_LABELS = __LANG_LABELS__;
const LANGS = ["English","Hindi","Kannada"];

let replyLang = __DEFAULT_LANG__;
let lastAnswer = "";
let muted = false;
let rec = null;

const $ = function(id){ return document.getElementById(id); };
function t(k){ return SAY[replyLang][k]; }
function fill(tpl, vars){
  let out = tpl;
  for (const k in vars){ out = out.split("{" + k + "}").join(vars[k]); }
  return out;
}
function norm(s){
  return (" " + (s || "").toLowerCase() + " ")
    .replace(/[?.,!;:\u0964"'()]/g, " ")
    .replace(/\s+/g, " ");
}
function esc(s){ return s.replace(/[.*+?^${}()|[\]\\]/g, "\\$&"); }
/* Latin words are matched on word boundaries so "price" never matches "rice".
   Indic words are matched as substrings, because Hindi/Kannada attach
   case suffixes directly to the word (e.g. "ಟೊಮ್ಯಾಟೊದ", "टमाटर का"). */
function hit(q, w){
  if (!w) return false;
  if (/^[\x00-\x7F]+$/.test(w)){
    try { return new RegExp("(^|[^a-z0-9])" + esc(w) + "([^a-z0-9]|$)", "i").test(q); }
    catch(e){ return q.indexOf(w) !== -1; }
  }
  return q.indexOf(w) !== -1;
}
function hasAny(q, words){
  for (const w of words){ if (hit(q, w)) return true; }
  return false;
}
function money(n){
  const r = Math.round(n * 10) / 10;
  return (r % 1 === 0) ? String(Math.round(r)) : r.toFixed(1);
}

/* ---------- resolvers ---------- */
function findLocation(q){
  let best = null;
  for (const key in KB.locations){
    for (const a of KB.locations[key].aliases){
      if (a.length > 2 && hit(q, a)){
        if (!best || a.length > best.len) best = {key: key, len: a.length};
      }
    }
  }
  return best ? best.key : null;
}
function findCrop(q){
  let best = null;
  for (const c of KB.crops){
    for (const a of c.aliases){
      if (a.length > 2 && hit(q, a)){
        if (!best || a.length > best.len) best = {crop: c, len: a.length};
      }
    }
  }
  return best ? best.crop : null;
}
function findScheme(q){
  for (const s of KB.schemes){
    for (const a of s.aliases){
      if (a.length > 3 && hit(q, a)) return s;
    }
  }
  return null;
}
function findAnimal(q){
  for (const a of KB.animals){
    for (const al of a.aliases){
      if (al.length > 2 && hit(q, al)) return a;
    }
  }
  return null;
}
function priceOf(crop, locKey){
  const loc = KB.locations[locKey];
  const isLocal = loc.local.indexOf(crop.key) !== -1;
  return {value: crop.base * loc.factor * (isLocal ? 1.04 : 1.0), local: isLocal};
}
function suitabilityOf(crop, locKey){
  if (!crop.advisory) return null;
  const seasonEn = __SEASON_EN__;
  let score = crop.advisory.success;
  score += (crop.advisory.locations.indexOf(locKey) !== -1) ? 8 : -15;
  score += (crop.advisory.seasons.indexOf(seasonEn) !== -1) ? 7 : -18;
  return Math.max(0, Math.min(100, score));
}
function bestCrops(locKey, limit){
  const out = [];
  for (const c of KB.crops){
    const s = suitabilityOf(c, locKey);
    if (s !== null && s >= 60) out.push({crop: c, score: s});
  }
  out.sort(function(a, b){ return b.score - a.score; });
  return out.slice(0, limit || 3);
}
function localCropNames(locKey, limit){
  const keys = KB.locations[locKey].local.slice(0, limit || 5);
  const names = [];
  for (const k of keys){
    for (const c of KB.crops){ if (c.key === k) names.push(c.names[replyLang]); }
  }
  return names;
}

/* ---------- the answer engine ---------- */
function answer(question){
  const q = norm(question);
  if (!q.trim()) return t("help");

  const askedLoc = findLocation(q);
  const locKey = askedLoc || KB.selected;
  const locName = KB.locations[locKey].names[replyLang];
  const crop = findCrop(q);

  const wantsWeather = hasAny(q, INTENTS.weather);
  const wantsWater = hasAny(q, INTENTS.water);
  const wantsScheme = hasAny(q, INTENTS.scheme);
  const wantsAnimal = hasAny(q, INTENTS.animal);
  const wantsGrow = hasAny(q, INTENTS.grow);
  const wantsPrice = hasAny(q, INTENTS.price);

  /* weather */
  if (wantsWeather && !crop){
    if (!KB.weather) return fill(t("weather_off"), {loc: KB.locations[KB.selected].names[replyLang]});
    const w = KB.weather;
    let out = fill(t("weather"), {
      loc: KB.locations[KB.selected].names[replyLang],
      temp: w.temp, cond: w.cond[replyLang], humidity: w.humidity,
      wind: w.wind, rain: w.rain, tmin: w.tmin, tmax: w.tmax
    });
    if (askedLoc && askedLoc !== KB.selected){
      out += fill(t("weather_other"), {loc: KB.locations[KB.selected].names[replyLang]});
    }
    return out;
  }

  /* government schemes */
  if (wantsScheme){
    const s = findScheme(q);
    if (s) return fill(t("scheme"), {name: s.names[replyLang], best: s.best[replyLang], key: s.key[replyLang]});
    const names = KB.schemes.slice(0, 4).map(function(x){ return x.names[replyLang]; });
    return fill(t("scheme_list"), {list: names.join(", ")});
  }

  /* livestock */
  if (wantsAnimal){
    const a = findAnimal(q) || KB.animals[0];
    return fill(t("animal"), {
      animal: a.names[replyLang], n: a.n, setup: a.setup,
      monthly: a.monthly, income: a.income, margin: a.margin
    });
  }

  /* water */
  if (wantsWater && !crop){
    return fill(t("water"), {loc: locName, water: KB.locations[locKey].water[replyLang]});
  }

  /* crop suitability / what to grow */
  if (wantsGrow && !wantsPrice){
    if (crop && crop.advisory){
      const sc = suitabilityOf(crop, locKey);
      return fill(t("suit"), {
        crop: crop.names[replyLang], loc: locName, season: KB.season[replyLang],
        score: sc, harvest: crop.advisory.harvest, risk: crop.advisory.risk[replyLang]
      });
    }
    const top = bestCrops(locKey, 3);
    if (top.length){
      const list = top.map(function(x){ return x.crop.names[replyLang] + " (" + x.score + "%)"; }).join(", ");
      return fill(t("best"), {loc: locName, season: KB.season[replyLang], list: list});
    }
  }

  /* crop price — the main ask */
  if (crop){
    const p = priceOf(crop, locKey);
    const localNote = p.local ? fill(t("local_note"), {crop: crop.names[replyLang]}) : "";
    return fill(t("price"), {
      loc: locName, crop: crop.names[replyLang], price: money(p.value),
      unit: crop.unit[replyLang], trend: crop.trend[replyLang], localNote: localNote
    }) + " " + t("disclaimer");
  }

  if (wantsPrice){
    const keys = KB.locations[locKey].local.slice(0, 4);
    const parts = [];
    for (const k of keys){
      for (const c of KB.crops){
        if (c.key === k){
          const p = priceOf(c, locKey);
          parts.push(c.names[replyLang] + " ₹" + money(p.value) + "/" + c.unit[replyLang]);
        }
      }
    }
    if (parts.length) return fill(t("price_list"), {loc: locName, list: parts.join(", ")}) + " " + t("disclaimer");
    return fill(t("crop_unknown"), {list: localCropNames(locKey, 5).join(", ")});
  }

  if (hasAny(q, INTENTS.opportunity)){
    return fill(t("opportunity"), {
      loc: locName, score: KB.locations[locKey].score,
      crops: KB.locations[locKey].local.length, water: KB.locations[locKey].water[replyLang]
    });
  }
  if (hasAny(q, INTENTS.greet)) return t("greet");
  return t("help");
}

/* ---------- speech output ---------- */
function pickVoice(code){
  const vs = window.speechSynthesis ? window.speechSynthesis.getVoices() : [];
  const base = code.split("-")[0];
  let v = vs.filter(function(x){ return x.lang && x.lang.replace("_", "-") === code; })[0];
  if (!v) v = vs.filter(function(x){ return x.lang && x.lang.toLowerCase().indexOf(base) === 0; })[0];
  return v || null;
}
function speak(text){
  if (muted || !window.speechSynthesis) return;
  try{
    window.speechSynthesis.cancel();
    const code = KB.langCodes[replyLang];
    const u = new SpeechSynthesisUtterance(text);
    u.lang = code;
    const v = pickVoice(code);
    if (v) { u.voice = v; $("replyNote").innerText = ""; }
    else { $("replyNote").innerText = t("no_voice"); }
    u.rate = 0.95;
    window.speechSynthesis.speak(u);
  }catch(e){}
}

/* ---------- ui ---------- */
function respondTo(question){
  $("heard").style.display = "block";
  $("heard").innerHTML = "<b>" + t("heard") + ":</b> " + question;
  const a = answer(question);
  lastAnswer = a;
  $("replyText").innerText = a;
  speak(a);
}
function renderStatic(){
  $("startTxt").innerText = __START__;
  $("stopTxt").innerText = __STOP__;
  $("repeatTxt").innerText = t("repeat");
  $("muteTxt").innerText = t("stop_speaking");
  $("ask").innerText = t("ask");
  $("typed").placeholder = t("type_placeholder");
  $("replyLabel").innerText = t("answer");
  $("langLabel").innerText = t("reply_lang");
  $("exLabel").innerText = t("examples");
  $("status").innerText = t("idle");

  $("langRow").innerHTML = "";
  LANGS.forEach(function(lg){
    const b = document.createElement("button");
    b.className = "langpill" + (lg === replyLang ? " active" : "");
    b.innerText = LANG_LABELS[lg];
    b.onclick = function(){
      replyLang = lg;
      if (rec) rec.lang = KB.langCodes[lg];
      renderStatic();
      if (lastAnswer) { $("replyText").innerText = "—"; lastAnswer = ""; $("heard").style.display = "none"; }
    };
    $("langRow").appendChild(b);
  });

  $("chips").innerHTML = "";
  EXAMPLES[replyLang].forEach(function(ex){
    const c = document.createElement("button");
    c.className = "chip";
    c.innerText = ex;
    c.onclick = function(){ $("typed").value = ex; respondTo(ex); };
    $("chips").appendChild(c);
  });
}

const SR = window.SpeechRecognition || window.webkitSpeechRecognition;
if (SR){
  rec = new SR();
  rec.lang = KB.langCodes[replyLang];
  rec.continuous = false;
  rec.interimResults = false;
  rec.onstart = function(){ $("status").innerText = t("listening"); $("micOrb").style.background = "#f1e9ff"; };
  rec.onend = function(){ $("status").innerText = t("idle"); $("micOrb").style.background = "#ffffff"; };
  rec.onerror = function(e){ $("status").innerText = t("mic_error") + ": " + e.error; };
  rec.onresult = function(e){ respondTo(e.results[0][0].transcript); };
  $("start").onclick = function(){ try{ rec.lang = KB.langCodes[replyLang]; rec.start(); }catch(err){} };
  $("stop").onclick = function(){ try{ rec.stop(); }catch(err){} };
}else{
  $("start").disabled = true;
  $("stop").disabled = true;
}

$("ask").onclick = function(){ if ($("typed").value.trim()) respondTo($("typed").value.trim()); };
$("typed").addEventListener("keydown", function(e){ if (e.key === "Enter" && $("typed").value.trim()) respondTo($("typed").value.trim()); });
$("repeat").onclick = function(){ if (lastAnswer) speak(lastAnswer); };
$("mute").onclick = function(){
  muted = !muted;
  if (window.speechSynthesis) window.speechSynthesis.cancel();
  $("mute").style.background = muted ? "#f4f0ff" : "#fff";
};

renderStatic();
if (!SR) $("status").innerText = t("not_supported");
if (window.speechSynthesis) window.speechSynthesis.onvoiceschanged = function(){};
</script>
'''

        def js_json(obj):
            """JSON for safe embedding inside a <script> block."""
            return json.dumps(obj, ensure_ascii=False).replace("</", "<\\/")

        voice_html = (VOICE_ENGINE_HTML
                      .replace("__KB__", js_json(voice_kb))
                      .replace("__SAY__", js_json(VOICE_SAY))
                      .replace("__INTENTS__", js_json(VOICE_INTENTS))
                      .replace("__EXAMPLES__", js_json(VOICE_EXAMPLES))
                      .replace("__LANG_LABELS__", js_json(VOICE_LANG_LABELS))
                      .replace("__DEFAULT_LANG__", js_json(language))
                      .replace("__SEASON_EN__", js_json(voice_season))
                      .replace("__TITLE__", p2("voice_title"))
                      .replace("__START__", js_json(p2("voice_start")))
                      .replace("__STOP__", js_json(p2("voice_stop"))))

        components.html(voice_html, height=760, scrolling=True)
        st.caption(p2("browser_note"))

    # ---------------- LIVESTOCK ----------------
    with hub_tabs[3]:
        page_banner("🐄", p2("livestock"), p2("livestock_desc"))
        animal_businesses=[b for b in BUSINESSES if b["name"] in ["Dairy / Milk-Based Business","Goat / Sheep Rearing","Poultry Farming"]]
        animal_names=[b["name"] for b in animal_businesses]
        selected_animal=st.selectbox(p2("animal_business"),animal_names,format_func=p1_business_name,key="p2_animal_business")
        profile=get_animal_advisory(selected_animal,location)
        default_n,default_setup,default_monthly,default_income=livestock_defaults(selected_animal)
        c1,c2=st.columns(2)
        with c1:
            herd=st.number_input(p2("herd"),min_value=1,value=default_n,step=1,key="p2_herd")
            setup=st.number_input(p2("setup"),min_value=0.0,value=float(default_setup),step=500.0,key="p2_setup")
        with c2:
            monthly=st.number_input(p2("monthly"),min_value=0.0,value=float(default_monthly),step=100.0,key="p2_monthly")
            income=st.number_input(p2("income"),min_value=0.0,value=float(default_income),step=100.0,key="p2_income")
        months=st.number_input(p2("months"),min_value=1,max_value=60,value=12,step=1,key="p2_months")
        setup_total=herd*setup; monthly_total=herd*monthly; monthly_income=herd*income; margin=monthly_income-monthly_total
        st.markdown("### 📊 " + p2("economics"))
        a,b,c,d=st.columns(4)
        a.metric(p2("setup_total"),money(setup_total)); b.metric(p2("monthly_total"),money(monthly_total)); c.metric(p2("monthly_income"),money(monthly_income)); d.metric(p2("monthly_margin"),money(margin))
        if margin>0:
            payback=setup_total/margin
            st.success(f"⏱️ {p2('break_even')}: ~{payback:.1f} months based on this simple model.")
        else:
            st.warning("⚠️ " + p2("illustrative_warning"))
        if profile:
            st.markdown(f"### 🐾 {p2('breed')}")
            st.markdown(f'''<div class="feature-card"><div class="feature-icon">🐄</div><h4>{animal_text(profile['breed'])}</h4><p>{animal_text(profile['why'])}</p></div>''', unsafe_allow_html=True)
            st.markdown(f"### 🧾 {p2('animal_care')}")
            for care in profile["care"]: st.write("• "+animal_text(care))
        st.info(f"📍 {p2('market_link')}: {ui_data(location,'location_name')} • {p2('water')}: {ui_data(location_water(location),'water')}")
        st.caption(p2("planner_note"))



P2_HOME = {
    "English":{"layers":"One assistant, connected layers","flow":"How the system connects the dots","judge":"Demo flow for judges","market":"Market Intelligence","market_d":"Location-aware demonstration crop profiles and transparent sample pricing.","context":"Live Context","context_d":"Weather + season + water context for practical farming decisions.","finance":"Financial Planning","finance_d":"Profit, EMI and scenario simulation before spending money.","engine":"Action Engine","engine_d":"Recommendations, risk alerts, comparisons and scheme readiness.","opportunity":"Opportunity View","opportunity_d":"Visual Karnataka opportunity signals built from the app's prototype profiles.","voice":"Voice Access","voice_d":"Browser voice interaction designed for accessibility and local-language use.","s1":"Choose location","d1":"Karnataka location becomes the local context.","s2":"Read signals","d2":"Market, water, season and weather are combined.","s3":"Compare options","d3":"Crops, businesses and schemes can be compared.","s4":"Plan before acting","d4":"Financial and livestock simulations expose assumptions.","s5":"Take the next step","d5":"The Smart Action Plan turns information into practical actions.","judge_msg":"Select a Karnataka location → open Rural Intelligence Hub → show weather → show opportunity map → demonstrate voice → run Smart Action Plan → compare options → check scheme documents.","transparency":"Prototype transparency: sample market data, rule-based recommendation logic and illustrative financial/livestock assumptions are clearly labelled inside the app."},
    "Hindi":{"layers":"एक सहायक, जुड़े हुए स्तर","flow":"सिस्टम जानकारी को कैसे जोड़ता है","judge":"जजों के लिए डेमो फ्लो","market":"बाज़ार जानकारी","market_d":"स्थान-आधारित प्रदर्शन फसल प्रोफाइल और पारदर्शी नमूना कीमतें।","context":"लाइव संदर्भ","context_d":"व्यावहारिक खेती निर्णयों के लिए मौसम + ऋतु + पानी संदर्भ।","finance":"वित्तीय योजना","finance_d":"निवेश से पहले लाभ, EMI और परिदृश्य सिमुलेशन।","engine":"कार्य इंजन","engine_d":"सिफारिशें, जोखिम संकेत, तुलना और योजना दस्तावेज़ तैयारी।","opportunity":"अवसर दृश्य","opportunity_d":"प्रोटोटाइप प्रोफाइल से बने कर्नाटक अवसर संकेत।","voice":"वॉइस सुविधा","voice_d":"पहुंच और स्थानीय भाषा उपयोग के लिए ब्राउज़र वॉइस इंटरैक्शन।","s1":"स्थान चुनें","d1":"कर्नाटक का स्थान स्थानीय संदर्भ बनता है।","s2":"संकेत देखें","d2":"बाज़ार, पानी, ऋतु और मौसम को जोड़ा जाता है।","s3":"विकल्पों की तुलना करें","d3":"फसल, व्यवसाय और योजनाओं की तुलना की जा सकती है।","s4":"कार्रवाई से पहले योजना बनाएं","d4":"वित्तीय और पशुपालन सिमुलेशन मान्यताओं को स्पष्ट करते हैं।","s5":"अगला कदम लें","d5":"स्मार्ट कार्य योजना जानकारी को व्यावहारिक कदमों में बदलती है।","judge_msg":"कर्नाटक स्थान चुनें → ग्रामीण इंटेलिजेंस हब खोलें → मौसम दिखाएं → अवसर मानचित्र दिखाएं → वॉइस दिखाएं → स्मार्ट कार्य योजना चलाएं → विकल्पों की तुलना करें → योजना दस्तावेज़ देखें।","transparency":"प्रोटोटाइप पारदर्शिता: नमूना बाज़ार डेटा, नियम-आधारित सिफारिशें और उदाहरणात्मक वित्तीय/पशुपालन मान्यताएँ स्पष्ट रूप से बताई गई हैं।"},
    "Kannada":{"layers":"ಒಂದೇ ಸಹಾಯಕ, ಸಂಪರ್ಕಿತ ಪದರಗಳು","flow":"ಸಿಸ್ಟಮ್ ಮಾಹಿತಿಯನ್ನು ಹೇಗೆ ಸಂಪರ್ಕಿಸುತ್ತದೆ","judge":"ನಿರ್ಣಾಯಕರಿಗಾಗಿ ಡೆಮೊ ಹರಿವು","market":"ಮಾರುಕಟ್ಟೆ ಮಾಹಿತಿ","market_d":"ಸ್ಥಳ ಆಧಾರಿತ ಡೆಮೊ ಬೆಳೆ ಪ್ರೊಫೈಲ್‌ಗಳು ಮತ್ತು ಪಾರದರ್ಶಕ ಮಾದರಿ ಬೆಲೆಗಳು.","context":"ಲೈವ್ ಸಂದರ್ಭ","context_d":"ಪ್ರಾಯೋಗಿಕ ಕೃಷಿ ನಿರ್ಧಾರಗಳಿಗೆ ಹವಾಮಾನ + ಋತು + ನೀರಿನ ಸಂದರ್ಭ.","finance":"ಹಣಕಾಸು ಯೋಜನೆ","finance_d":"ಹೂಡಿಕೆಗೂ ಮೊದಲು ಲಾಭ, EMI ಮತ್ತು ಪರಿಸ್ಥಿತಿ ಸಿಮ್ಯುಲೇಶನ್.","engine":"ಕಾರ್ಯ ಎಂಜಿನ್","engine_d":"ಶಿಫಾರಸುಗಳು, ಅಪಾಯ ಸೂಚನೆಗಳು, ಹೋಲಿಕೆ ಮತ್ತು ಯೋಜನೆ ದಾಖಲೆ ಸಿದ್ಧತೆ.","opportunity":"ಅವಕಾಶ ದೃಶ್ಯ","opportunity_d":"ಪ್ರೋಟೋಟೈಪ್ ಪ್ರೊಫೈಲ್‌ಗಳಿಂದ ನಿರ್ಮಿಸಿದ ಕರ್ನಾಟಕ ಅವಕಾಶ ಸೂಚನೆಗಳು.","voice":"ಧ್ವನಿ ಪ್ರವೇಶ","voice_d":"ಪ್ರವೇಶ ಮತ್ತು ಸ್ಥಳೀಯ ಭಾಷೆಗಾಗಿ ಬ್ರೌಸರ್ ಧ್ವನಿ ಸಂವಹನ.","s1":"ಸ್ಥಳ ಆಯ್ಕೆಮಾಡಿ","d1":"ಕರ್ನಾಟಕದ ಸ್ಥಳವು ಸ್ಥಳೀಯ ಸಂದರ್ಭವಾಗುತ್ತದೆ.","s2":"ಸೂಚನೆಗಳನ್ನು ನೋಡಿ","d2":"ಮಾರುಕಟ್ಟೆ, ನೀರು, ಋತು ಮತ್ತು ಹವಾಮಾನವನ್ನು ಸೇರಿಸಲಾಗುತ್ತದೆ.","s3":"ಆಯ್ಕೆಗಳನ್ನು ಹೋಲಿಸಿ","d3":"ಬೆಳೆ, ವ್ಯವಹಾರ ಮತ್ತು ಯೋಜನೆಗಳನ್ನು ಹೋಲಿಸಬಹುದು.","s4":"ಕಾರ್ಯಕ್ಕೂ ಮೊದಲು ಯೋಜಿಸಿ","d4":"ಹಣಕಾಸು ಮತ್ತು ಪಶುಸಂಗೋಪನಾ ಸಿಮ್ಯುಲೇಶನ್‌ಗಳು ಅಂದಾಜುಗಳನ್ನು ತೋರಿಸುತ್ತವೆ.","s5":"ಮುಂದಿನ ಹೆಜ್ಜೆ ತೆಗೆದುಕೊಳ್ಳಿ","d5":"ಸ್ಮಾರ್ಟ್ ಕಾರ್ಯ ಯೋಜನೆ ಮಾಹಿತಿಯನ್ನು ಪ್ರಾಯೋಗಿಕ ಹೆಜ್ಜೆಗಳಾಗಿ ಪರಿವರ್ತಿಸುತ್ತದೆ.","judge_msg":"ಕರ್ನಾಟಕ ಸ್ಥಳ ಆಯ್ಕೆಮಾಡಿ → ಗ್ರಾಮೀಣ ಇಂಟೆಲಿಜೆನ್ಸ್ ಹಬ್ ತೆರೆಯಿರಿ → ಹವಾಮಾನ ತೋರಿಸಿ → ಅವಕಾಶ ನಕ್ಷೆ ತೋರಿಸಿ → ಧ್ವನಿ ಪ್ರದರ್ಶಿಸಿ → ಸ್ಮಾರ್ಟ್ ಕಾರ್ಯ ಯೋಜನೆ ನಡೆಸಿ → ಆಯ್ಕೆಗಳನ್ನು ಹೋಲಿಸಿ → ಯೋಜನೆ ದಾಖಲೆಗಳನ್ನು ಪರಿಶೀಲಿಸಿ.","transparency":"ಪ್ರೋಟೋಟೈಪ್ ಪಾರದರ್ಶಕತೆ: ಮಾದರಿ ಮಾರುಕಟ್ಟೆ ಡೇಟಾ, ನಿಯಮ ಆಧಾರಿತ ಶಿಫಾರಸುಗಳು ಮತ್ತು ಉದಾಹರಣಾತ್ಮಕ ಹಣಕಾಸು/ಪಶುಸಂಗೋಪನಾ ಅಂದಾಜುಗಳನ್ನು ಸ್ಪಷ್ಟವಾಗಿ ಗುರುತಿಸಲಾಗಿದೆ."}
}
def p2home(key):
    return P2_HOME.get(language, P2_HOME["English"]).get(key, key)

# ============================================================
# HOME
# ============================================================


if page == "Smart Action Plan":
    page_banner("🧠", p1("title"), p1("desc"))
    st.write(p1("desc"))
    st.info("💡 " + p1("disclaimer"))

    # ---------- USER PROFILE FOR DECISION ENGINE ----------
    st.markdown(f"## 🎯 {p1('profile')}")
    c1,c2,c3=st.columns(3)
    with c1:
        action_capital=st.number_input(p1("capital_fit") + " (₹)", min_value=0.0, value=100000.0, step=5000.0, key="p1_capital")
    with c2:
        action_interest_options=[b["name"] for b in BUSINESSES]
        action_interest=st.selectbox(p1("business_option"), action_interest_options, format_func=p1_business_name, key="p1_interest")
    with c3:
        action_resources=st.multiselect(p1("resource_fit"), sorted({r for b in BUSINESSES for r in b["resources"]}), default=["Land"] if "Land" in {r for b in BUSINESSES for r in b["resources"]} else [], format_func=p1_resource_text, key="p1_resources")

    current= current_season()
    local_water=location_water(location)
    best_business=next(b for b in BUSINESSES if b["name"]==action_interest)
    top_crops=best_crops_for_location(location,current,limit=3)

    # ---------- WHAT SHOULD I DO TODAY ----------
    st.markdown(f"## 🌾 {p1('today')}")
    st.caption(p1("today_desc"))
    st.markdown(f"### 📍 {p1('context')}")
    a,b,c=st.columns(3)
    a.metric(p1("location"), ui_data(location, "location_name"))
    b.metric(p1("season"), ui_data(current, "season"))
    c.metric(p1("water_context"), ui_data(local_water, "water"))

    left,right=st.columns(2)
    with left:
        st.markdown(f"#### 🌱 {p1('top_crops')}")
        if top_crops:
            for crop,score,info in top_crops:
                st.write(f"🌾 **{tr_data(crop)}** — {score}% {ui('compare_suitability').lower()}")
        else:
            st.write("—")
    with right:
        st.markdown(f"#### 💼 {p1('business_option')}")
        st.success(f"**{p1_business_name(best_business['name'])}**")
        st.write(p1("next_steps"))
        for step in [p1("step1"),p1("step2"),p1("step3"),p1("step4")]: st.write("• "+step)

    # ---------- WHY RECOMMENDATION ----------
    st.markdown("---")
    st.markdown(f"## 🔍 {p1('why_title')}")
    st.caption(p1("why_desc"))
    score, matched=p1_score_breakdown(best_business,action_capital,action_resources,best_business["interests"][0],local_water,"Some experience",location)
    total=sum(score.values())
    labels=[("capital",p1("capital_fit")),("resource",p1("resource_fit")),("interest",p1("interest_fit")),("water",p1("water_fit")),("experience",p1("experience_fit")),("location",p1("location_fit"))]
    cols=st.columns(3)
    for i,(key,label) in enumerate(labels): cols[i%3].metric(label,f"{score[key]}")
    st.metric(p1("total"),f"{total} {p1('out_of')}")
    if matched: st.success(p1("matched_resources")+": "+", ".join(p1_resource_text(x) for x in matched))
    elif action_resources: st.warning(p1("no_resources"))
    else: st.info(p1("no_resources"))

    # ---------- RISK ALERTS ----------
    st.markdown("---")
    st.markdown(f"## ⚠️ {p1('risk_title')}")
    st.caption(p1("risk_desc"))
    alerts=p1_risk_alerts(best_business,action_capital,location,top_crops[0][0] if top_crops else None,current)
    for level,msg in alerts:
        if level=="high": st.error("🔴 "+p1("high")+": "+msg)
        elif level=="medium": st.warning("🟠 "+p1("medium")+": "+msg)
        else: st.info("🟢 "+p1("low")+": "+msg)

    # ---------- COMPARE ----------
    st.markdown("---")
    st.markdown(f"## ⚖️ {p1('compare_title')}")
    st.caption(p1("compare_desc"))
    compare_kind=st.radio(p1("option_type"),["Businesses","Crops"],horizontal=True,format_func=lambda x:p1("businesses") if x=="Businesses" else p1("crops"),key="p1_compare_kind")
    if compare_kind=="Businesses":
        opts=[b["name"] for b in BUSINESSES]
    else:
        opts=list(CROP_ADVISORY.keys())
    ca,cb=st.columns(2)
    with ca: opt_a=st.selectbox(p1("option_a"),opts,index=0,key="p1_a",format_func=p1_business_name if compare_kind=="Businesses" else tr_data)
    with cb:
        default_b=1 if len(opts)>1 else 0
        opt_b=st.selectbox(p1("option_b"),opts,index=default_b,key="p1_b",format_func=p1_business_name if compare_kind=="Businesses" else tr_data)
    st.markdown(f"### {p1('comparison')}")
    rows=p1_compare_rows(compare_kind,opt_a,opt_b,location,current)
    for label,a_val,b_val in rows:
        x,y,z=st.columns([1.2,1,1])
        x.markdown(f"**{label}**"); y.write(a_val); z.write(b_val)
    st.caption(p1("compare_note"))

    # ---------- SCHEME DOCUMENT READINESS ----------
    st.markdown("---")
    st.markdown(f"## 📋 {p1('scheme_title')}")
    st.caption(p1("scheme_desc"))
    scheme_names=[s["name"] for s in SCHEMES]
    selected_scheme=st.selectbox(p1("scheme"),scheme_names,format_func=scheme_name,key="p1_scheme")
    details=get_scheme_details(selected_scheme)
    if details:
        docs=details["documents"]
        st.markdown(f"**{p1('documents_have')}:**")
        checks=[]
        for i,doc in enumerate(docs):
            checks.append(st.checkbox(scheme_document_text(doc),key=f"p1_doc_{i}"))
        pct=round(100*sum(checks)/len(checks)) if checks else 0
        st.progress(pct/100)
        st.metric(p1("readiness"),f"{pct}%")
        if pct==100: st.success(f"{p1('ready')}: 100%")
        else: st.info(f"{p1('missing')}: {len(checks)-sum(checks)}")
        st.caption(p1("eligibility_check"))

    # ---------- SIMULATOR ----------
    st.markdown("---")
    st.markdown(f"## 💰 {p1('sim_title')}")
    st.caption(p1("sim_desc"))
    simtab1,simtab2=st.tabs([p1("business_sim"),p1("farm_sim")])
    with simtab1:
        x1,x2,x3,x4=st.columns(4)
        with x1: units=st.number_input(p1("units"),min_value=1.0,value=100.0,step=10.0,key="p1_units")
        with x2: sale=st.number_input(p1("sale_price"),min_value=0.0,value=50.0,step=1.0,key="p1_sale")
        with x3: var=st.number_input(p1("variable_cost"),min_value=0.0,value=30.0,step=1.0,key="p1_var")
        with x4: fixed=st.number_input(p1("fixed_cost"),min_value=0.0,value=1000.0,step=100.0,key="p1_fixed")
        scen=st.selectbox(p1("scenario"),["Normal","Selling price -10%","Variable cost +15%","Price -10% and variable cost +15%"],format_func=lambda x:{"Normal":p1("normal"),"Selling price -10%":p1("price_down"),"Variable cost +15%":p1("cost_up"),"Price -10% and variable cost +15%":p1("both")}[x],key="p1_scenario")
        sale2=sale*(0.9 if "price" in scen.lower() else 1)
        var2=var*(1.15 if "cost" in scen.lower() else 1)
        revenue=units*sale2; cost=units*var2+fixed; profit=revenue-cost
        q1,q2,q3=st.columns(3); q1.metric(p1("revenue"),money(revenue)); q2.metric(p1("cost"),money(cost)); q3.metric(p1("profit"),money(profit))
        st.info(f"{p1('scenario_result')}: {p1('baseline')} → {p1('scenario')}")
    with simtab2:
        f1,f2,f3,f4=st.columns(4)
        with f1: area=st.number_input(p1("farm_area"),min_value=0.1,value=1.0,step=0.5,key="p1_area")
        with f2: yield_a=st.number_input(p1("yield_per_acre"),min_value=0.0,value=1000.0,step=50.0,key="p1_yield")
        with f3: farm_price=st.number_input(p1("farm_price"),min_value=0.0,value=25.0,step=1.0,key="p1_fprice")
        with f4: farm_cost=st.number_input(p1("farm_cost"),min_value=0.0,value=15000.0,step=500.0,key="p1_fcost")
        farm_revenue=area*yield_a*farm_price; farm_profit=farm_revenue-farm_cost
        q1,q2,q3=st.columns(3); q1.metric(p1("revenue"),money(farm_revenue)); q2.metric(p1("cost"),money(farm_cost)); q3.metric(p1("profit"),money(farm_profit))
        st.caption(p1("farm_note"))

if page == "Home":
    st.markdown(f'''<div class="animated-hero"><div class="hero-orb one"></div><div class="hero-orb two"></div><div class="hero-orb three"></div><h1>🌾 Gram Sahayak</h1><p>{tr("subtitle")}</p><span class="hero-badge">🇮🇳 Karnataka-first • 🌐 English / हिंदी / ಕನ್ನಡ • 🧠 Decision-support prototype</span></div>''', unsafe_allow_html=True)
    st.markdown(f"## {tr('welcome')}")
    st.write(tr("home_desc"))

    col1,col2,col3,col4=st.columns(4)
    for col,icon,label,value in [(col1,"🌱",tr("crops"),len(CROP_DATA)),(col2,"📍",tr("locations"),len(locations)),(col3,"🏛️",tr("schemes_count"),len(SCHEMES)),(col4,"💡",tr("business_models"),len(BUSINESSES))]:
        with col:
            st.markdown(f"<div class='metric-strip'><div style='font-size:1.45rem'>{icon}</div><div style='font-size:.85rem;color:#667085'>{label}</div><div style='font-size:1.65rem;font-weight:800'>{value}</div></div>",unsafe_allow_html=True)

    st.markdown(f"### 📍 {tr('selected_market')}")
    st.info(f"{tr('demo_market')}: **{ui_data(location,'location_name')}**. {tr('market_disclaimer')}")

    st.markdown("### ✨ " + p2home("layers"))
    cards=[("📈",p2home("market"),p2home("market_d")),("🌦️",p2home("context"),p2home("context_d")),("💰",p2home("finance"),p2home("finance_d")),("🧠",p2home("engine"),p2home("engine_d")),("🗺️",p2home("opportunity"),p2home("opportunity_d")),("🎙️",p2home("voice"),p2home("voice_d"))]
    for start_i in range(0,len(cards),3):
        cols=st.columns(3)
        for col,(icon,title,desc) in zip(cols,cards[start_i:start_i+3]):
            with col:
                st.markdown(f"<div class='feature-card'><div class='feature-icon'>{icon}</div><h4>{title}</h4><p>{desc}</p></div>",unsafe_allow_html=True)

    st.markdown("### 🔄 " + p2home("flow"))
    steps=[("01",p2home("s1"),p2home("d1")),("02",p2home("s2"),p2home("d2")),("03",p2home("s3"),p2home("d3")),("04",p2home("s4"),p2home("d4")),("05",p2home("s5"),p2home("d5"))]
    for no,title,desc in steps:
        st.markdown(f"<div class='timeline-step'><b>{no} • {title}</b><div class='small-note'>{desc}</div></div>",unsafe_allow_html=True)

    st.markdown("### 🚀 " + p2home("judge"))
    st.success(p2home("judge_msg"))
    st.caption(p2home("transparency"))

# ============================================================
# MARKET PRICES
# ============================================================

if page == "Market Prices":
    page_banner("📈", tr("market_title"), tr("market_desc", location=ui_data(location, "location_name")))
    st.write(
        f"Current mandi prices for **{ui_data(location, 'location_name')}** are taken from the official "
        "data.gov.in daily market-price dataset. The selected location is used only to filter the dataset."
    )

    # --------------------------------------------------------
    # DATASET-BASED MARKET PRICES
    # --------------------------------------------------------
    mandi_df, mandi_error = fetch_mandi_data(location)

    if mandi_df is None:
        st.warning(
            "Live mandi prices could not be loaded from the official data.gov.in dataset."
        )
        if mandi_error:
            st.caption(mandi_error)

        with st.expander("🔐 Configure data.gov.in API key", expanded=True):
            st.markdown(
                "To load the official mandi prices, add your data.gov.in API key to "
                "**Streamlit Secrets**. Do not paste the key directly into this Python file."
            )
            st.code('DATA_GOV_API_KEY = "YOUR_DATA_GOV_API_KEY"', language="toml")
            st.markdown(
                "In Streamlit Cloud: **Manage app → Settings → Secrets**, paste the line above, "
                "replace `YOUR_DATA_GOV_API_KEY` with your actual key, save it, and then restart/redeploy the app."
            )
            st.caption(
                "The code also accepts DATA_GOV_API_KEY as an environment variable when running outside Streamlit Cloud."
            )

        st.info(
            "No hard-coded/sample prices are shown here. Once the official dataset is available, "
            "the vegetables and crops below will come directly from its commodity and price fields."
        )
    elif mandi_df.empty:
        st.warning(
            f"The official mandi dataset returned no records for **{ui_data(location, 'location_name')}**."
        )
        st.info("Try another location or check the latest district names in the data.gov.in dataset.")
    else:
        # Clean commodity names and remove rows that have no usable price.
        mandi_df = mandi_df.copy()
        mandi_df["commodity"] = mandi_df["commodity"].astype(str).str.strip()
        mandi_df = mandi_df[mandi_df["commodity"].ne("")]
        mandi_df = mandi_df[mandi_df["modal_price"].notna()]

        st.success(
            f"Loaded **{len(mandi_df):,}** mandi records from the official dataset for "
            f"**{ui_data(location, 'location_name')}**."
        )

        # The commodity list comes from the dataset itself — not CROP_DATA or user-entered prices.
        commodities = sorted(mandi_df["commodity"].dropna().unique().tolist())

        st.markdown("### 🥕 Vegetables and crops from the dataset")
        st.caption(
            "The prices below are dataset values. No manual price input or location multiplier is applied."
        )

        selected_commodity = st.selectbox(
            "Select commodity",
            ["All commodities"] + commodities,
            key="mandi_commodity_select"
        )

        display_df = mandi_df.copy()
        if selected_commodity != "All commodities":
            display_df = display_df[display_df["commodity"] == selected_commodity]

        # Show the fields supplied by the government dataset.
        display_columns = [
            "commodity", "variety", "grade", "market", "arrival_date",
            "min_price", "max_price", "modal_price"
        ]
        display_columns = [c for c in display_columns if c in display_df.columns]
        display_df = display_df[display_columns].copy()

        rename_map = {
            "commodity": "Commodity",
            "variety": "Variety",
            "grade": "Grade",
            "market": "Market",
            "arrival_date": "Arrival Date",
            "min_price": "Min Price (₹/quintal)",
            "max_price": "Max Price (₹/quintal)",
            "modal_price": "Modal Price (₹/quintal)",
        }
        display_df = display_df.rename(columns=rename_map)

        st.dataframe(display_df, use_container_width=True, hide_index=True)

        # Summary uses the modal price directly from the dataset.
        if selected_commodity != "All commodities" and not display_df.empty:
            row = display_df.iloc[0]
            a, b, c = st.columns(3)
            a.metric("Commodity", str(row.get("Commodity", selected_commodity)))
            b.metric("Modal price", f"₹{float(row['Modal Price (₹/quintal)']):,.0f}/quintal")
            c.metric(
                "Price range",
                f"₹{float(row['Min Price (₹/quintal)']):,.0f} – ₹{float(row['Max Price (₹/quintal)']):,.0f}"
            )

        st.caption(
            "Source: Government of India Open Government Data (data.gov.in), Current Daily Price of "
            "Various Commodities from Various Markets (Mandi). Prices are wholesale mandi prices in ₹/quintal."
        )

    # --------------------------------------------------------
    # CROP RECOMMENDATION (kept inside Market Prices)
    # --------------------------------------------------------
    st.markdown("---")
    st.markdown("## 🌱 Crop Recommendation")
    st.caption(
        f"Get crop recommendations for **{ui_data(location, 'location_name')}** using your soil and climate inputs. "
        "The recommendation engine uses the public Kaggle Crop Recommendation Dataset."
    )

    st.info(
        "The crop recommendation inputs are used only for crop recommendation. "
        "They do NOT change the mandi prices shown above. Market prices come directly from the government dataset. "
        "FAO SoilFER is shown as the suitability framework reference; it is not silently treated as a "
        "Karnataka-specific SoilFER dataset."
    )

    df_crop, crop_error = load_kaggle_crop_dataset()
    if df_crop is None:
        st.error("Could not load the Kaggle dataset right now.")
        st.caption(crop_error or "Unknown download error.")
    else:
        st.success(f"Kaggle dataset loaded: {len(df_crop):,} records and {df_crop['label'].nunique()} crop labels.")

        r1, r2, r3 = st.columns(3)
        with r1:
            n_val = st.number_input("Nitrogen (N)", min_value=0.0, max_value=200.0, value=50.0, step=1.0, key="market_crop_n")
            p_val = st.number_input("Phosphorus (P)", min_value=0.0, max_value=200.0, value=50.0, step=1.0, key="market_crop_p")
            k_val = st.number_input("Potassium (K)", min_value=0.0, max_value=250.0, value=50.0, step=1.0, key="market_crop_k")
        with r2:
            temp_val = st.number_input("Temperature (°C)", min_value=-10.0, max_value=60.0, value=25.0, step=0.5, key="market_crop_temp")
            humidity_val = st.number_input("Humidity (%)", min_value=0.0, max_value=100.0, value=70.0, step=1.0, key="market_crop_humidity")
        with r3:
            ph_val = st.number_input("Soil pH", min_value=0.0, max_value=14.0, value=6.5, step=0.1, key="market_crop_ph")
            rain_val = st.number_input("Rainfall (mm)", min_value=0.0, max_value=5000.0, value=100.0, step=5.0, key="market_crop_rain")

        if st.button("🌾 Recommend Crops", type="primary", key="market_recommend_crops"):
            values = {
                "N": n_val, "P": p_val, "K": k_val,
                "temperature": temp_val, "humidity": humidity_val,
                "ph": ph_val, "rainfall": rain_val
            }
            results = crop_recommendations_from_kaggle(df_crop, values)

            st.subheader("Recommended crops from the Kaggle dataset")
            for rank, (crop_name, score) in enumerate(results, 1):
                col_a, col_b = st.columns([3, 1])
                with col_a:
                    st.markdown(f"**{rank}. {crop_name.title()}**")
                with col_b:
                    st.metric("Match score", f"{score:.1f}%")

            st.caption(
                "Match score is a relative nearest-neighbour score from this dataset; "
                "it is not a yield, profit or guaranteed suitability probability."
            )

    st.markdown("### 🌍 FAO SoilFER suitability reference")
    st.write(
        "FAO SoilFER crop-suitability assessment links crop requirements with soil constraints/opportunities, "
        "climate context and land-cover information. The app uses this as a methodological reference and "
        "does not claim that the Kaggle recommendations are FAO SoilFER suitability results."
    )
    st.link_button("Open FAO SoilFER Crop Suitability Assessment", FAO_SOILFER_URL)


# ============================================================
# GOVERNMENT SCHEMES
# ============================================================

if page == "Government Schemes":
    page_banner("🏛️", tr("scheme_title"), tr("scheme_desc"))
    st.write(tr("scheme_desc"))

    search = st.text_input("🔎 " + tr("search"), placeholder=tr("placeholder"))

    # Search remains based on the original official English content so it is stable.
    shown = []
    for scheme in SCHEMES:
        searchable = (scheme["name"] + " " + scheme["best_for"] + " " +
                      scheme["description"] + " " + scheme["why"]).lower()
        if not search or search.lower() in searchable:
            shown.append(scheme)

    for scheme in shown:
        with st.expander(scheme_name(scheme["name"])):
            st.markdown(f"**{tr('best_for')}:** {stext('best', scheme['best_for'])}")
            st.write(stext('desc', scheme["description"]))
            st.markdown(f"**{tr('key')}:** {scheme_extra('key', scheme['key'])}")
            st.markdown(f"**{tr('why')}:** {scheme_extra('why', scheme['why'])}")

            scheme_details = get_scheme_details(scheme["name"])
            if scheme_details:
                st.markdown(f"**{tr('eligibility')}:** {scheme_eligibility_text(scheme_details['eligibility'])}")
                st.markdown(f"**{tr('documents')}:**")
                for doc in scheme_details["documents"]:
                    st.write("• " + scheme_document_text(doc))

            st.caption(f"{tr('source')}: {scheme_extra('source', scheme['source'])}")

    st.warning(tr("scheme_warning"))

# ============================================================
# FINANCIAL ASSISTANT
# ============================================================

if page == "Financial Assistant":
    page_banner("💰", tr("finance_title"), "Estimate profit, EMI and cash-flow scenarios before investing.")
    tab1, tab2 = st.tabs([tr("profit_tab"), tr("emi_tab")])

    with tab1:
        st.subheader(tr("profit_est"))
        col1, col2 = st.columns(2)
        with col1:
            quantity = st.number_input(tr("quantity"), min_value=1.0, value=100.0)
            purchase_price = st.number_input(tr("purchase"), min_value=0.0, value=20.0)
        with col2:
            selling_price = st.number_input(tr("selling"), min_value=0.0, value=30.0)
            other_costs = st.number_input(tr("other"), min_value=0.0, value=0.0)

        total_cost = quantity * purchase_price + other_costs
        revenue = quantity * selling_price
        profit = revenue - total_cost

        a, b, c = st.columns(3)
        a.metric(tr("total_cost"), money(total_cost))
        b.metric(tr("revenue"), money(revenue))
        c.metric(tr("profit"), money(profit))

        if profit > 0:
            st.success(tr("positive"))
        elif profit == 0:
            st.info(tr("break_even"))
        else:
            st.error(tr("loss"))

    with tab2:
        st.subheader(tr("emi_tab").replace("🏦 ", ""))
        col1, col2, col3 = st.columns(3)
        with col1:
            # Loan amount increases in ₹1,000 steps.
            principal = st.number_input(
                tr("loan"), min_value=1000.0, value=100000.0, step=1000.0, key="emi_principal"
            )
        with col2:
            annual_rate = st.number_input(
                tr("rate"), min_value=0.0, value=10.0, step=0.5, key="emi_rate"
            )
        with col3:
            years = st.number_input(
                tr("period"), min_value=1, value=3, key="emi_years"
            )

        months = years * 12
        monthly_rate = annual_rate / 12 / 100
        if monthly_rate == 0:
            emi = principal / months
        else:
            emi = principal * monthly_rate * (1 + monthly_rate) ** months / ((1 + monthly_rate) ** months - 1)

        total_payment = emi * months
        total_interest = total_payment - principal

        a, b, c = st.columns(3)
        a.metric(tr("monthly"), money(emi))
        b.metric(tr("total_payment"), money(total_payment))
        c.metric(tr("interest"), money(total_interest))
        st.caption(tr("loan_note"))

        # Simple loan affordability section: principal amount is explicitly
        # entered by the user, without additional complex loan calculations.
        st.divider()
        st.subheader("💳 Loan Affordability")
        st.caption("Enter the principal amount and your monthly income to see a simple EMI affordability estimate.")

        aff_col1, aff_col2 = st.columns(2)
        with aff_col1:
            affordability_principal = st.number_input(
                "Principal Amount (₹)",
                min_value=1000.0,
                value=100000.0,
                step=1000.0,
                key="affordability_principal"
            )
        with aff_col2:
            monthly_income = st.number_input(
                "Monthly Income (₹)",
                min_value=0.0,
                value=30000.0,
                step=1000.0,
                key="affordability_income"
            )

        # Reuse the EMI assumptions above so affordability stays simple.
        if monthly_rate == 0:
            affordability_emi = affordability_principal / months
        else:
            affordability_emi = (
                affordability_principal * monthly_rate * (1 + monthly_rate) ** months
                / ((1 + monthly_rate) ** months - 1)
            )

        affordability_ratio = (affordability_emi / monthly_income * 100) if monthly_income > 0 else None
        a1, b1 = st.columns(2)
        a1.metric("Estimated EMI", money(affordability_emi))
        if affordability_ratio is not None:
            b1.metric("EMI / Monthly Income", f"{affordability_ratio:.1f}%")
            if affordability_ratio <= 40:
                st.success("The estimated EMI is within 40% of the entered monthly income.")
            else:
                st.warning("The estimated EMI is above 40% of the entered monthly income.")
        else:
            b1.metric("EMI / Monthly Income", "—")
            st.info("Enter a monthly income above ₹0 to check affordability.")
        st.caption("This is a simple estimate, not a loan approval or lender eligibility decision.")


# ============================================================
# BUSINESS RECOMMENDATION
# ============================================================

if page == "Business Recommendation":
    page_banner("💡", tr("business_title"), tr("business_desc"))
    st.write(tr("business_desc"))

    col1, col2 = st.columns(2)

    # Build the resource list from all business profiles so users can select
    # multiple resources and the recommendation engine can compare them.
    resource_values = sorted({
        resource
        for business in BUSINESSES
        for resource in business["resources"]
    })
    resource_values.append("Not sure / I have limited resources")
    interest_values = [
        "Farming", "Agriculture", "Vegetables", "Food", "Cooking", "Retail",
        "Livestock", "Poultry", "Dairy", "Transport", "Delivery", "Tailoring",
        "Handicrafts", "Repair", "Technology", "General business"
    ]

    RESOURCE_TR = {
        "Hindi": {
            "Land":"ज़मीन","Water":"पानी","Shop space":"दुकान की जगह","Kitchen/Workspace":"रसोई/कार्यस्थल",
            "Cattle":"पशु","Sewing machine":"सिलाई मशीन","Vehicle":"वाहन","Repair tools":"मरम्मत के औज़ार",
            "Craft skills":"कारीगरी कौशल","Agriculture knowledge":"कृषि ज्ञान","Fodder":"चारा","Shelter":"शेड/आश्रय",
            "Agricultural tools":"कृषि उपकरण","Food processing equipment":"खाद्य प्रसंस्करण उपकरण",
            "Raw materials":"कच्चा माल","Kitchen equipment":"रसोई उपकरण","Small stall/shop":"छोटा स्टॉल/दुकान",
            "Food preparation skills":"खाना बनाने का कौशल","Livestock care":"पशु देखभाल","Poultry equipment":"पोल्ट्री उपकरण",
            "Two-wheeler/vehicle":"दो-पहिया/वाहन","Mobile phone":"मोबाइल फोन","Driving skills":"ड्राइविंग कौशल",
            "Workspace":"कार्यस्थल","Tailoring skills":"सिलाई कौशल","Shop":"दुकान","Working capital":"कार्यशील पूंजी",
            "Supplier network":"आपूर्तिकर्ता नेटवर्क","Technical skill":"तकनीकी कौशल",
            "Not sure / I have limited resources":"पता नहीं / मेरे पास सीमित संसाधन हैं"
        },
        "Kannada": {
            "Land":"ಭೂಮಿ","Water":"ನೀರು","Shop space":"ಅಂಗಡಿ ಸ್ಥಳ","Kitchen/Workspace":"ಅಡುಗೆಮನೆ/ಕೆಲಸದ ಸ್ಥಳ",
            "Cattle":"ಜಾನುವಾರು","Sewing machine":"ಹೊಲಿಗೆ ಯಂತ್ರ","Vehicle":"ವಾಹನ","Repair tools":"ದುರಸ್ತಿ ಉಪಕರಣಗಳು",
            "Craft skills":"ಕರಕುಶಲ ಕೌಶಲ್ಯ","Agriculture knowledge":"ಕೃಷಿ ಜ್ಞಾನ","Fodder":"ಮೇವು","Shelter":"ಶೆಡ್/ಆಶ್ರಯ",
            "Agricultural tools":"ಕೃಷಿ ಉಪಕರಣಗಳು","Food processing equipment":"ಆಹಾರ ಸಂಸ್ಕರಣಾ ಉಪಕರಣಗಳು",
            "Raw materials":"ಕಚ್ಚಾ ವಸ್ತುಗಳು","Kitchen equipment":"ಅಡುಗೆ ಉಪಕರಣಗಳು","Small stall/shop":"ಸಣ್ಣ ಸ್ಟಾಲ್/ಅಂಗಡಿ",
            "Food preparation skills":"ಆಹಾರ ತಯಾರಿಕಾ ಕೌಶಲ್ಯ","Livestock care":"ಜಾನುವಾರು ಆರೈಕೆ","Poultry equipment":"ಕೋಳಿ ಸಾಕಣೆ ಉಪಕರಣಗಳು",
            "Two-wheeler/vehicle":"ಎರಡು ಚಕ್ರದ ವಾಹನ/ವಾಹನ","Mobile phone":"ಮೊಬೈಲ್ ಫೋನ್","Driving skills":"ಚಾಲನಾ ಕೌಶಲ್ಯ",
            "Workspace":"ಕೆಲಸದ ಸ್ಥಳ","Tailoring skills":"ಹೊಲಿಗೆ ಕೌಶಲ್ಯ","Shop":"ಅಂಗಡಿ","Working capital":"ಕಾರ್ಯನಿರ್ವಹಣಾ ಬಂಡವಾಳ",
            "Supplier network":"ಪೂರೈಕೆದಾರರ ಜಾಲ","Technical skill":"ತಾಂತ್ರಿಕ ಕೌಶಲ್ಯ",
            "Not sure / I have limited resources":"ಖಚಿತವಿಲ್ಲ / ನನ್ನ ಬಳಿ ಸೀಮಿತ ಸಂಪನ್ಮೂಲಗಳಿವೆ"
        }
    }
    INTEREST_TR = {
        "Hindi": {"Farming":"खेती","Agriculture":"कृषि","Vegetables":"सब्ज़ियाँ","Food":"भोजन","Cooking":"खाना बनाना","Retail":"खुदरा","Livestock":"पशुपालन","Poultry":"पोल्ट्री","Dairy":"डेयरी","Transport":"परिवहन","Delivery":"डिलीवरी","Tailoring":"सिलाई","Handicrafts":"हस्तशिल्प","Repair":"मरम्मत","Technology":"तकनीक","General business":"सामान्य व्यवसाय"},
        "Kannada": {"Farming":"ಕೃಷಿ","Agriculture":"ಕೃಷಿ","Vegetables":"ತರಕಾರಿಗಳು","Food":"ಆಹಾರ","Cooking":"ಅಡುಗೆ","Retail":"ಚಿಲ್ಲರೆ ವ್ಯಾಪಾರ","Livestock":"ಪಶುಸಂಗೋಪನೆ","Poultry":"ಕೋಳಿ ಸಾಕಣೆ","Dairy":"ಡೈರಿ","Transport":"ಸಾರಿಗೆ","Delivery":"ವಿತರಣೆ","Tailoring":"ಹೊಲಿಗೆ","Handicrafts":"ಕರಕುಶಲ","Repair":"ದುರಸ್ತಿ","Technology":"ತಂತ್ರಜ್ಞಾನ","General business":"ಸಾಮಾನ್ಯ ವ್ಯವಹಾರ"}
    }

    # ---------------------------------------------------------
    # USER INPUTS
    # IMPORTANT: these variables must be created BEFORE the
    # recommendation button uses calculate_match().
    # ---------------------------------------------------------
    with col1:
        capital = st.number_input(
            tr("capital"),
            min_value=0.0,
            value=100000.0,
            step=5000.0,
            format="%.0f"
        )

        resources = st.multiselect(
            tr("resource"),
            resource_values,
            default=["Land"] if "Land" in resource_values else [],
            format_func=lambda x: RESOURCE_TR.get(language, {}).get(x, x),
            help="Select all resources you already have. The recommendation score will increase when your selected resources match the business requirements."
        )

        interest = st.selectbox(
            tr("interest_input"),
            interest_values,
            format_func=lambda x: INTEREST_TR.get(language, {}).get(x, x)
        )

    with col2:
        local_water = location_water(location)
        water_labels = {
            "Good": "Good / अच्छी / ಉತ್ತಮ",
            "Medium": "Medium / मध्यम / ಮಧ್ಯಮ",
            "Limited": "Limited / सीमित / ಸೀಮಿತ"
        }
        st.info(f"💧 {ui('water_for', location=ui_data(location, 'location_name'))}: **{ui_data(local_water, 'water')}**")

        experience = st.selectbox(
            tr("experience"),
            ["Beginner", "Some experience", "Experienced"],
            format_func=lambda x: {
                "Beginner": tr("beginner"),
                "Some experience": tr("some"),
                "Experienced": tr("experienced")
            }[x]
        )

    if resources:
        selected_resource_labels = ", ".join(
            RESOURCE_TR.get(language, {}).get(r, r) for r in resources
        )
        st.success(f"🧰 {ui('selected_resources')}: **{selected_resource_labels}**")
    else:
        st.warning(ui("select_resource"))

    st.info(tr("location_note", location=ui_data(location, "location_name")))

    # ---------------------------------------------------------
    # COMPLETE BUSINESS CONTENT TRANSLATIONS
    # These dictionaries translate the content stored in BUSINESSES
    # while keeping the English values internally for scoring.
    # ---------------------------------------------------------
    BUSINESS_CONTENT_TR = {
        "Hindi": {
            "investment": {
                "₹25,000 – ₹2.5 lakh": "₹25,000 – ₹2.5 लाख",
                "₹75,000 – ₹10 lakh+": "₹75,000 – ₹10 लाख+",
                "₹1 lakh – ₹7 lakh": "₹1 लाख – ₹7 लाख",
                "₹30,000 – ₹3 lakh": "₹30,000 – ₹3 लाख",
                "₹1 lakh – ₹8 lakh": "₹1 लाख – ₹8 लाख",
                "₹60,000 – ₹5 lakh": "₹60,000 – ₹5 लाख",
                "₹80,000 – ₹6 lakh": "₹80,000 – ₹6 लाख",
                "₹75,000 – ₹6 lakh": "₹75,000 – ₹6 लाख",
                "₹30,000 – ₹2.5 lakh": "₹30,000 – ₹2.5 लाख",
                "₹25,000 – ₹3 lakh": "₹25,000 – ₹3 लाख",
                "₹1.5 lakh – ₹10 lakh+": "₹1.5 लाख – ₹10 लाख+",
                "₹40,000 – ₹3 lakh": "₹40,000 – ₹3 लाख"
            },
            "model": {
                "Grow vegetables → sell to local markets, retailers, hotels or direct customers.": "सब्ज़ियाँ उगाएँ → स्थानीय बाजारों, खुदरा विक्रेताओं, होटलों या सीधे ग्राहकों को बेचें।",
                "Convert local produce into higher-value products such as flour, snacks, pickles, spice mixes or packaged foods.": "स्थानीय उपज को आटा, स्नैक्स, अचार, मसाला मिश्रण या पैकेज्ड खाद्य जैसे अधिक मूल्य वाले उत्पादों में बदलें।",
                "Sell essential household products with repeat local demand.": "नियमित स्थानीय मांग वाले आवश्यक घरेलू उत्पाद बेचें।",
                "Sell affordable snacks or meals at a high-footfall local location.": "अधिक ग्राहक आने वाली स्थानीय जगह पर किफायती स्नैक्स या भोजन बेचें।",
                "Milk production with possible value addition such as curd, paneer or ghee.": "दूध का उत्पादन करें और दही, पनीर या घी जैसे मूल्यवर्धित उत्पाद बनाएं।",
                "Rear animals for meat, breeding or local livestock markets.": "मांस, प्रजनन या स्थानीय पशु बाजारों के लिए पशुओं का पालन करें।",
                "Egg or broiler production for nearby markets.": "नजदीकी बाजारों के लिए अंडे या ब्रॉयलर का उत्पादन करें।",
                "Deliver groceries, farm inputs, medicines or local goods within nearby villages/towns.": "नजदीकी गांवों/कस्बों में किराना, कृषि इनपुट, दवाइयाँ या स्थानीय सामान पहुँचाएँ।",
                "Alterations, stitching, school uniforms, traditional clothing and small-batch garments.": "कपड़ों की अल्टरशन, सिलाई, स्कूल यूनिफॉर्म, पारंपरिक कपड़े और छोटे बैच के परिधान तैयार करें।",
                "Make baskets, decor, traditional products or locally distinctive handmade goods.": "टोकरी, सजावटी सामान, पारंपरिक उत्पाद या स्थानीय विशेषता वाले हस्तनिर्मित सामान बनाएँ।",
                "Supply seeds, tools, irrigation accessories and farm-related services.": "बीज, उपकरण, सिंचाई सामग्री और कृषि संबंधी सेवाएँ उपलब्ध कराएँ।",
                "Repair phones, appliances, agricultural equipment or other locally needed items.": "मोबाइल, उपकरण, कृषि मशीनरी या स्थानीय रूप से आवश्यक अन्य वस्तुओं की मरम्मत करें।"
            },
            "risk": {
                "Weather, water availability and price fluctuations.": "मौसम, पानी की उपलब्धता और कीमतों में उतार-चढ़ाव।",
                "Food safety, packaging, shelf life and market access.": "खाद्य सुरक्षा, पैकेजिंग, शेल्फ लाइफ और बाजार तक पहुँच।",
                "Competition, inventory management and credit sales.": "प्रतिस्पर्धा, स्टॉक प्रबंधन और उधार बिक्री।",
                "Location dependency, hygiene and daily demand variation.": "स्थान पर निर्भरता, स्वच्छता और दैनिक मांग में बदलाव।",
                "Animal health, feed costs and milk-price changes.": "पशु स्वास्थ्य, चारे की लागत और दूध की कीमतों में बदलाव।",
                "Disease, feed costs and market-price fluctuations.": "बीमारी, चारे की लागत और बाजार कीमतों में उतार-चढ़ाव।",
                "Feed costs, disease and price volatility.": "चारे की लागत, बीमारी और कीमतों में अस्थिरता।",
                "Fuel costs, vehicle maintenance and route density.": "ईंधन की लागत, वाहन रखरखाव और मार्ग की मांग।",
                "Competition and seasonal demand.": "प्रतिस्पर्धा और मौसमी मांग।",
                "Demand discovery and inconsistent order volume.": "मांग का पता लगाना और ऑर्डर की मात्रा में अस्थिरता।",
                "Inventory, licensing requirements and seasonal demand.": "स्टॉक, लाइसेंस की आवश्यकताएँ और मौसमी मांग।",
                "Skill dependency and availability of spare parts.": "कौशल पर निर्भरता और स्पेयर पार्ट्स की उपलब्धता।"
            },
            "steps": {
                "Select crops based on local demand and water availability.": "स्थानीय मांग और पानी की उपलब्धता के आधार पर फसलें चुनें।",
                "Estimate seed, labour, irrigation and transport costs.": "बीज, श्रम, सिंचाई और परिवहन की लागत का अनुमान लगाएँ।",
                "Plan more than one sales channel instead of depending on a single buyer.": "एक ही खरीदार पर निर्भर रहने के बजाय एक से अधिक बिक्री चैनल रखें।",
                "Choose one product with a clear local customer segment.": "स्पष्ट स्थानीय ग्राहक वर्ग वाला एक उत्पाद चुनें।",
                "Calculate raw material, packaging, labour and selling costs.": "कच्चे माल, पैकेजिंग, श्रम और बिक्री लागत की गणना करें।",
                "Test a small batch before investing in larger equipment.": "बड़े उपकरणों में निवेश करने से पहले छोटे बैच का परीक्षण करें।",
                "Start with fast-moving essentials instead of excessive inventory.": "अधिक स्टॉक रखने के बजाय तेजी से बिकने वाली आवश्यक वस्तुओं से शुरुआत करें।",
                "Track daily sales and stock movement.": "दैनिक बिक्री और स्टॉक की आवाजाही का रिकॉर्ड रखें।",
                "Add high-demand local products after observing customer behaviour.": "ग्राहकों के व्यवहार को देखकर अधिक मांग वाले स्थानीय उत्पाद जोड़ें।",
                "Choose a small menu with good margins.": "अच्छे मार्जिन वाला छोटा मेन्यू चुनें।",
                "Test demand at different times of the day.": "दिन के अलग-अलग समय पर मांग का परीक्षण करें।",
                "Maintain hygiene, consistent quality and simple bookkeeping.": "स्वच्छता, समान गुणवत्ता और सरल लेखा-जोखा बनाए रखें।",
                "Estimate feed and veterinary costs before buying animals.": "पशु खरीदने से पहले चारे और पशु चिकित्सा की लागत का अनुमान लगाएँ।",
                "Identify a reliable local milk buyer.": "एक भरोसेमंद स्थानीय दूध खरीदार की पहचान करें।",
                "Maintain records of milk yield and animal health.": "दूध उत्पादन और पशु स्वास्थ्य का रिकॉर्ड रखें।",
                "Start with a manageable herd size.": "संभालने योग्य झुंड के आकार से शुरुआत करें।",
                "Plan vaccination and veterinary care.": "टीकाकरण और पशु चिकित्सा देखभाल की योजना बनाएँ।",
                "Build a buyer network before scaling.": "विस्तार करने से पहले खरीदारों का नेटवर्क बनाएँ।",
                "Choose egg or meat production based on local demand.": "स्थानीय मांग के आधार पर अंडा या मांस उत्पादन चुनें।",
                "Calculate feed cost per bird.": "प्रति पक्षी चारे की लागत की गणना करें।",
                "Maintain biosecurity and veterinary schedules.": "जैव-सुरक्षा और पशु चिकित्सा कार्यक्रम बनाए रखें।",
                "Map villages and shops that need regular delivery.": "नियमित डिलीवरी की जरूरत वाले गांवों और दुकानों की सूची बनाएँ।",
                "Start with a defined service radius.": "एक निश्चित सेवा क्षेत्र से शुरुआत करें।",
                "Use simple digital records for orders, fuel and collections.": "ऑर्डर, ईंधन और भुगतान संग्रह के लिए सरल डिजिटल रिकॉर्ड रखें।",
                "Start with alterations and high-demand local garments.": "अल्टरशन और अधिक मांग वाले स्थानीय परिधानों से शुरुआत करें।",
                "Build repeat customers through reliable delivery.": "विश्वसनीय सेवा देकर नियमित ग्राहकों का आधार बनाएँ।",
                "Add machines only when order volume justifies them.": "ऑर्डर की मात्रा पर्याप्त होने पर ही मशीनें बढ़ाएँ।",
                "Create a small catalogue and sample products.": "एक छोटा कैटलॉग और नमूना उत्पाद तैयार करें।",
                "Explore local fairs, retailers and digital selling channels.": "स्थानीय मेलों, खुदरा विक्रेताओं और डिजिटल बिक्री चैनलों का उपयोग करें।",
                "Identify the crops and farm needs of nearby villages.": "नजदीकी गांवों की फसलों और कृषि जरूरतों की पहचान करें।",
                "Stock fast-moving inputs first.": "पहले तेजी से बिकने वाले कृषि इनपुट रखें।",
                "Follow all applicable licences and quality requirements.": "सभी लागू लाइसेंस और गुणवत्ता आवश्यकताओं का पालन करें।",
                "Choose one repair category based on local demand.": "स्थानीय मांग के आधार पर एक मरम्मत श्रेणी चुनें।",
                "Keep commonly required spare parts.": "आमतौर पर आवश्यक स्पेयर पार्ट्स रखें।",
                "Build trust through transparent pricing and service records.": "पारदर्शी कीमत और सेवा रिकॉर्ड के माध्यम से भरोसा बनाएँ।"
            }
        },
        "Kannada": {
            "investment": {
                "₹25,000 – ₹2.5 lakh": "₹25,000 – ₹2.5 ಲಕ್ಷ",
                "₹75,000 – ₹10 lakh+": "₹75,000 – ₹10 ಲಕ್ಷ+",
                "₹1 lakh – ₹7 lakh": "₹1 ಲಕ್ಷ – ₹7 ಲಕ್ಷ",
                "₹30,000 – ₹3 lakh": "₹30,000 – ₹3 ಲಕ್ಷ",
                "₹1 lakh – ₹8 lakh": "₹1 ಲಕ್ಷ – ₹8 ಲಕ್ಷ",
                "₹60,000 – ₹5 lakh": "₹60,000 – ₹5 ಲಕ್ಷ",
                "₹80,000 – ₹6 lakh": "₹80,000 – ₹6 ಲಕ್ಷ",
                "₹75,000 – ₹6 lakh": "₹75,000 – ₹6 ಲಕ್ಷ",
                "₹30,000 – ₹2.5 lakh": "₹30,000 – ₹2.5 ಲಕ್ಷ",
                "₹25,000 – ₹3 lakh": "₹25,000 – ₹3 ಲಕ್ಷ",
                "₹1.5 lakh – ₹10 lakh+": "₹1.5 ಲಕ್ಷ – ₹10 ಲಕ್ಷ+",
                "₹40,000 – ₹3 lakh": "₹40,000 – ₹3 ಲಕ್ಷ"
            },
            "model": {
                "Grow vegetables → sell to local markets, retailers, hotels or direct customers.": "ತರಕಾರಿಗಳನ್ನು ಬೆಳೆಸಿ → ಸ್ಥಳೀಯ ಮಾರುಕಟ್ಟೆಗಳು, ಚಿಲ್ಲರೆ ವ್ಯಾಪಾರಿಗಳು, ಹೋಟೆಲ್‌ಗಳು ಅಥವಾ ನೇರ ಗ್ರಾಹಕರಿಗೆ ಮಾರಾಟ ಮಾಡಿ.",
                "Convert local produce into higher-value products such as flour, snacks, pickles, spice mixes or packaged foods.": "ಸ್ಥಳೀಯ ಉತ್ಪನ್ನಗಳನ್ನು ಹಿಟ್ಟು, ತಿಂಡಿಗಳು, ಉಪ್ಪಿನಕಾಯಿ, ಮಸಾಲೆ ಮಿಶ್ರಣಗಳು ಅಥವಾ ಪ್ಯಾಕೇಜ್ ಮಾಡಿದ ಆಹಾರದಂತಹ ಹೆಚ್ಚಿನ ಮೌಲ್ಯದ ಉತ್ಪನ್ನಗಳಾಗಿ ಪರಿವರ್ತಿಸಿ.",
                "Sell essential household products with repeat local demand.": "ನಿರಂತರ ಸ್ಥಳೀಯ ಬೇಡಿಕೆಯಿರುವ ಅಗತ್ಯ ಗೃಹೋಪಯೋಗಿ ಉತ್ಪನ್ನಗಳನ್ನು ಮಾರಾಟ ಮಾಡಿ.",
                "Sell affordable snacks or meals at a high-footfall local location.": "ಹೆಚ್ಚು ಜನ ಸಂಚಾರವಿರುವ ಸ್ಥಳದಲ್ಲಿ ಕೈಗೆಟುಕುವ ತಿಂಡಿಗಳು ಅಥವಾ ಊಟವನ್ನು ಮಾರಾಟ ಮಾಡಿ.",
                "Milk production with possible value addition such as curd, paneer or ghee.": "ಹಾಲು ಉತ್ಪಾದಿಸಿ ಮತ್ತು ಮೊಸರು, ಪನೀರ್ ಅಥವಾ ತುಪ್ಪದಂತಹ ಮೌಲ್ಯವರ್ಧಿತ ಉತ್ಪನ್ನಗಳನ್ನು ತಯಾರಿಸಿ.",
                "Rear animals for meat, breeding or local livestock markets.": "ಮಾಂಸ, ಸಂತಾನೋತ್ಪತ್ತಿ ಅಥವಾ ಸ್ಥಳೀಯ ಜಾನುವಾರು ಮಾರುಕಟ್ಟೆಗಳಿಗಾಗಿ ಪ್ರಾಣಿಗಳನ್ನು ಸಾಕಿ.",
                "Egg or broiler production for nearby markets.": "ಹತ್ತಿರದ ಮಾರುಕಟ್ಟೆಗಳಿಗಾಗಿ ಮೊಟ್ಟೆ ಅಥವಾ ಬ್ರಾಯ್ಲರ್ ಉತ್ಪಾದನೆ ಮಾಡಿ.",
                "Deliver groceries, farm inputs, medicines or local goods within nearby villages/towns.": "ಹತ್ತಿರದ ಗ್ರಾಮಗಳು/ಪಟ್ಟಣಗಳಲ್ಲಿ ದಿನಸಿ, ಕೃಷಿ ಇನ್‌ಪುಟ್‌ಗಳು, ಔಷಧಿಗಳು ಅಥವಾ ಸ್ಥಳೀಯ ಸರಕುಗಳನ್ನು ವಿತರಿಸಿ.",
                "Alterations, stitching, school uniforms, traditional clothing and small-batch garments.": "ಬಟ್ಟೆ ಬದಲಾವಣೆ, ಹೊಲಿಗೆ, ಶಾಲಾ ಸಮವಸ್ತ್ರ, ಸಾಂಪ್ರದಾಯಿಕ ಉಡುಪುಗಳು ಮತ್ತು ಸಣ್ಣ ಪ್ರಮಾಣದ ಉಡುಪುಗಳನ್ನು ತಯಾರಿಸಿ.",
                "Make baskets, decor, traditional products or locally distinctive handmade goods.": "ಬುಟ್ಟಿಗಳು, ಅಲಂಕಾರಿಕ ವಸ್ತುಗಳು, ಸಾಂಪ್ರದಾಯಿಕ ಉತ್ಪನ್ನಗಳು ಅಥವಾ ಸ್ಥಳೀಯ ವಿಶೇಷತೆಯ ಕೈತಯಾರಿಕಾ ವಸ್ತುಗಳನ್ನು ತಯಾರಿಸಿ.",
                "Supply seeds, tools, irrigation accessories and farm-related services.": "ಬೀಜಗಳು, ಉಪಕರಣಗಳು, ನೀರಾವರಿ ಸಾಮಗ್ರಿಗಳು ಮತ್ತು ಕೃಷಿ ಸಂಬಂಧಿತ ಸೇವೆಗಳನ್ನು ಒದಗಿಸಿ.",
                "Repair phones, appliances, agricultural equipment or other locally needed items.": "ಮೊಬೈಲ್‌ಗಳು, ಉಪಕರಣಗಳು, ಕೃಷಿ ಯಂತ್ರೋಪಕರಣಗಳು ಅಥವಾ ಸ್ಥಳೀಯವಾಗಿ ಅಗತ್ಯವಿರುವ ಇತರ ವಸ್ತುಗಳನ್ನು ದುರಸ್ತಿ ಮಾಡಿ."
            },
            "risk": {
                "Weather, water availability and price fluctuations.": "ಹವಾಮಾನ, ನೀರಿನ ಲಭ್ಯತೆ ಮತ್ತು ಬೆಲೆ ಏರಿಳಿತಗಳು.",
                "Food safety, packaging, shelf life and market access.": "ಆಹಾರ ಸುರಕ್ಷತೆ, ಪ್ಯಾಕೇಜಿಂಗ್, ಸಂಗ್ರಹ ಅವಧಿ ಮತ್ತು ಮಾರುಕಟ್ಟೆ ಪ್ರವೇಶ.",
                "Competition, inventory management and credit sales.": "ಸ್ಪರ್ಧೆ, ದಾಸ್ತಾನು ನಿರ್ವಹಣೆ ಮತ್ತು ಸಾಲದ ಮಾರಾಟ.",
                "Location dependency, hygiene and daily demand variation.": "ಸ್ಥಳದ ಅವಲಂಬನೆ, ಸ್ವಚ್ಛತೆ ಮತ್ತು ದೈನಂದಿನ ಬೇಡಿಕೆಯ ಬದಲಾವಣೆ.",
                "Animal health, feed costs and milk-price changes.": "ಜಾನುವಾರುಗಳ ಆರೋಗ್ಯ, ಮೇವು ವೆಚ್ಚ ಮತ್ತು ಹಾಲಿನ ಬೆಲೆ ಬದಲಾವಣೆಗಳು.",
                "Disease, feed costs and market-price fluctuations.": "ರೋಗ, ಮೇವು ವೆಚ್ಚ ಮತ್ತು ಮಾರುಕಟ್ಟೆ ಬೆಲೆ ಏರಿಳಿತಗಳು.",
                "Feed costs, disease and price volatility.": "ಮೇವು ವೆಚ್ಚ, ರೋಗ ಮತ್ತು ಬೆಲೆ ಅಸ್ಥಿರತೆ.",
                "Fuel costs, vehicle maintenance and route density.": "ಇಂಧನ ವೆಚ್ಚ, ವಾಹನ ನಿರ್ವಹಣೆ ಮತ್ತು ಮಾರ್ಗದ ಬೇಡಿಕೆ.",
                "Competition and seasonal demand.": "ಸ್ಪರ್ಧೆ ಮತ್ತು ಋತುಮಾನ ಬೇಡಿಕೆ.",
                "Demand discovery and inconsistent order volume.": "ಬೇಡಿಕೆಯನ್ನು ಗುರುತಿಸುವುದು ಮತ್ತು ಆರ್ಡರ್ ಪ್ರಮಾಣದ ಅಸ್ಥಿರತೆ.",
                "Inventory, licensing requirements and seasonal demand.": "ದಾಸ್ತಾನು, ಪರವಾನಗಿ ಅಗತ್ಯತೆಗಳು ಮತ್ತು ಋತುಮಾನ ಬೇಡಿಕೆ.",
                "Skill dependency and availability of spare parts.": "ಕೌಶಲ್ಯದ ಅವಲಂಬನೆ ಮತ್ತು ಸ್ಪೇರ್ ಪಾರ್ಟ್ಸ್ ಲಭ್ಯತೆ."
            },
            "steps": {
                "Select crops based on local demand and water availability.": "ಸ್ಥಳೀಯ ಬೇಡಿಕೆ ಮತ್ತು ನೀರಿನ ಲಭ್ಯತೆಯ ಆಧಾರದ ಮೇಲೆ ಬೆಳೆಗಳನ್ನು ಆಯ್ಕೆ ಮಾಡಿ.",
                "Estimate seed, labour, irrigation and transport costs.": "ಬೀಜ, ಕಾರ್ಮಿಕ, ನೀರಾವರಿ ಮತ್ತು ಸಾರಿಗೆ ವೆಚ್ಚಗಳನ್ನು ಅಂದಾಜಿಸಿ.",
                "Plan more than one sales channel instead of depending on a single buyer.": "ಒಬ್ಬ ಖರೀದಿದಾರನ ಮೇಲೆ ಅವಲಂಬಿಸದೆ ಒಂದಕ್ಕಿಂತ ಹೆಚ್ಚು ಮಾರಾಟ ಮಾರ್ಗಗಳನ್ನು ಯೋಜಿಸಿ.",
                "Choose one product with a clear local customer segment.": "ಸ್ಪಷ್ಟ ಸ್ಥಳೀಯ ಗ್ರಾಹಕ ವರ್ಗವಿರುವ ಒಂದು ಉತ್ಪನ್ನವನ್ನು ಆಯ್ಕೆ ಮಾಡಿ.",
                "Calculate raw material, packaging, labour and selling costs.": "ಕಚ್ಚಾ ವಸ್ತು, ಪ್ಯಾಕೇಜಿಂಗ್, ಕಾರ್ಮಿಕ ಮತ್ತು ಮಾರಾಟ ವೆಚ್ಚಗಳನ್ನು ಲೆಕ್ಕಿಸಿ.",
                "Test a small batch before investing in larger equipment.": "ದೊಡ್ಡ ಉಪಕರಣಗಳಲ್ಲಿ ಹೂಡಿಕೆ ಮಾಡುವ ಮೊದಲು ಸಣ್ಣ ಬ್ಯಾಚ್ ಪರೀಕ್ಷಿಸಿ.",
                "Start with fast-moving essentials instead of excessive inventory.": "ಹೆಚ್ಚು ದಾಸ್ತಾನು ಇಡುವ ಬದಲು ವೇಗವಾಗಿ ಮಾರಾಟವಾಗುವ ಅಗತ್ಯ ವಸ್ತುಗಳಿಂದ ಆರಂಭಿಸಿ.",
                "Track daily sales and stock movement.": "ದೈನಂದಿನ ಮಾರಾಟ ಮತ್ತು ದಾಸ್ತಾನು ಚಲನವಲನವನ್ನು ದಾಖಲಿಸಿ.",
                "Add high-demand local products after observing customer behaviour.": "ಗ್ರಾಹಕರ ವರ್ತನೆಯನ್ನು ಗಮನಿಸಿದ ನಂತರ ಹೆಚ್ಚು ಬೇಡಿಕೆಯ ಸ್ಥಳೀಯ ಉತ್ಪನ್ನಗಳನ್ನು ಸೇರಿಸಿ.",
                "Choose a small menu with good margins.": "ಉತ್ತಮ ಲಾಭಾಂಶವಿರುವ ಸಣ್ಣ ಮೆನು ಆಯ್ಕೆ ಮಾಡಿ.",
                "Test demand at different times of the day.": "ದಿನದ ವಿವಿಧ ಸಮಯಗಳಲ್ಲಿ ಬೇಡಿಕೆಯನ್ನು ಪರೀಕ್ಷಿಸಿ.",
                "Maintain hygiene, consistent quality and simple bookkeeping.": "ಸ್ವಚ್ಛತೆ, ಸ್ಥಿರ ಗುಣಮಟ್ಟ ಮತ್ತು ಸರಳ ಲೆಕ್ಕಪತ್ರವನ್ನು ಕಾಪಾಡಿ.",
                "Estimate feed and veterinary costs before buying animals.": "ಜಾನುವಾರುಗಳನ್ನು ಖರೀದಿಸುವ ಮೊದಲು ಮೇವು ಮತ್ತು ಪಶುವೈದ್ಯಕೀಯ ವೆಚ್ಚಗಳನ್ನು ಅಂದಾಜಿಸಿ.",
                "Identify a reliable local milk buyer.": "ವಿಶ್ವಾಸಾರ್ಹ ಸ್ಥಳೀಯ ಹಾಲು ಖರೀದಿದಾರರನ್ನು ಗುರುತಿಸಿ.",
                "Maintain records of milk yield and animal health.": "ಹಾಲಿನ ಉತ್ಪಾದನೆ ಮತ್ತು ಜಾನುವಾರುಗಳ ಆರೋಗ್ಯದ ದಾಖಲೆಗಳನ್ನು ಇಡಿ.",
                "Start with a manageable herd size.": "ನಿರ್ವಹಿಸಬಹುದಾದ ಹಿಂಡಿನ ಗಾತ್ರದಿಂದ ಆರಂಭಿಸಿ.",
                "Plan vaccination and veterinary care.": "ಲಸಿಕೆ ಮತ್ತು ಪಶುವೈದ್ಯಕೀಯ ಆರೈಕೆಯ ಯೋಜನೆ ಮಾಡಿ.",
                "Build a buyer network before scaling.": "ವಿಸ್ತರಿಸುವ ಮೊದಲು ಖರೀದಿದಾರರ ಜಾಲವನ್ನು ನಿರ್ಮಿಸಿ.",
                "Choose egg or meat production based on local demand.": "ಸ್ಥಳೀಯ ಬೇಡಿಕೆಯ ಆಧಾರದ ಮೇಲೆ ಮೊಟ್ಟೆ ಅಥವಾ ಮಾಂಸ ಉತ್ಪಾದನೆಯನ್ನು ಆಯ್ಕೆ ಮಾಡಿ.",
                "Calculate feed cost per bird.": "ಪ್ರತಿ ಪಕ್ಷಿಯ ಮೇವು ವೆಚ್ಚವನ್ನು ಲೆಕ್ಕಿಸಿ.",
                "Maintain biosecurity and veterinary schedules.": "ಜೈವಿಕ ಭದ್ರತೆ ಮತ್ತು ಪಶುವೈದ್ಯಕೀಯ ವೇಳಾಪಟ್ಟಿಯನ್ನು ಕಾಪಾಡಿ.",
                "Map villages and shops that need regular delivery.": "ನಿಯಮಿತ ವಿತರಣೆಯ ಅಗತ್ಯವಿರುವ ಗ್ರಾಮಗಳು ಮತ್ತು ಅಂಗಡಿಗಳನ್ನು ಗುರುತಿಸಿ.",
                "Start with a defined service radius.": "ನಿರ್ದಿಷ್ಟ ಸೇವಾ ವ್ಯಾಪ್ತಿಯಿಂದ ಆರಂಭಿಸಿ.",
                "Use simple digital records for orders, fuel and collections.": "ಆರ್ಡರ್‌ಗಳು, ಇಂಧನ ಮತ್ತು ಪಾವತಿ ಸಂಗ್ರಹಕ್ಕಾಗಿ ಸರಳ ಡಿಜಿಟಲ್ ದಾಖಲೆಗಳನ್ನು ಬಳಸಿ.",
                "Start with alterations and high-demand local garments.": "ಬಟ್ಟೆ ಬದಲಾವಣೆ ಮತ್ತು ಹೆಚ್ಚು ಬೇಡಿಕೆಯ ಸ್ಥಳೀಯ ಉಡುಪುಗಳಿಂದ ಆರಂಭಿಸಿ.",
                "Build repeat customers through reliable delivery.": "ವಿಶ್ವಾಸಾರ್ಹ ಸೇವೆಯ ಮೂಲಕ ಮರುಬರುವ ಗ್ರಾಹಕರನ್ನು ನಿರ್ಮಿಸಿ.",
                "Add machines only when order volume justifies them.": "ಆರ್ಡರ್ ಪ್ರಮಾಣವು ಸಮರ್ಥಿಸಿದಾಗ ಮಾತ್ರ ಯಂತ್ರಗಳನ್ನು ಹೆಚ್ಚಿಸಿ.",
                "Create a small catalogue and sample products.": "ಸಣ್ಣ ಕ್ಯಾಟಲಾಗ್ ಮತ್ತು ಮಾದರಿ ಉತ್ಪನ್ನಗಳನ್ನು ತಯಾರಿಸಿ.",
                "Explore local fairs, retailers and digital selling channels.": "ಸ್ಥಳೀಯ ಜಾತ್ರೆಗಳು, ಚಿಲ್ಲರೆ ವ್ಯಾಪಾರಿಗಳು ಮತ್ತು ಡಿಜಿಟಲ್ ಮಾರಾಟ ಮಾರ್ಗಗಳನ್ನು ಅನ್ವೇಷಿಸಿ.",
                "Identify the crops and farm needs of nearby villages.": "ಹತ್ತಿರದ ಗ್ರಾಮಗಳ ಬೆಳೆಗಳು ಮತ್ತು ಕೃಷಿ ಅಗತ್ಯಗಳನ್ನು ಗುರುತಿಸಿ.",
                "Stock fast-moving inputs first.": "ಮೊದಲು ವೇಗವಾಗಿ ಮಾರಾಟವಾಗುವ ಕೃಷಿ ಇನ್‌ಪುಟ್‌ಗಳನ್ನು ಸಂಗ್ರಹಿಸಿ.",
                "Follow all applicable licences and quality requirements.": "ಅನ್ವಯವಾಗುವ ಎಲ್ಲಾ ಪರವಾನಗಿ ಮತ್ತು ಗುಣಮಟ್ಟದ ಅವಶ್ಯಕತೆಗಳನ್ನು ಪಾಲಿಸಿ.",
                "Choose one repair category based on local demand.": "ಸ್ಥಳೀಯ ಬೇಡಿಕೆಯ ಆಧಾರದ ಮೇಲೆ ಒಂದು ದುರಸ್ತಿ ವಿಭಾಗವನ್ನು ಆಯ್ಕೆ ಮಾಡಿ.",
                "Keep commonly required spare parts.": "ಸಾಮಾನ್ಯವಾಗಿ ಅಗತ್ಯವಿರುವ ಸ್ಪೇರ್ ಪಾರ್ಟ್ಸ್‌ಗಳನ್ನು ಇಟ್ಟುಕೊಳ್ಳಿ.",
                "Build trust through transparent pricing and service records.": "ಪಾರದರ್ಶಕ ಬೆಲೆ ಮತ್ತು ಸೇವಾ ದಾಖಲೆಗಳ ಮೂಲಕ ವಿಶ್ವಾಸವನ್ನು ನಿರ್ಮಿಸಿ."
            }
        }
    }

    def business_content(kind, value):
        return BUSINESS_CONTENT_TR.get(language, {}).get(kind, {}).get(value, value)

    # Names shown in the recommendation cards.
    BUSINESS_NAME_TR = {
        "Hindi": {
            "Vegetable Cultivation":"सब्ज़ी की खेती",
            "Small Food Processing Unit":"छोटी खाद्य प्रसंस्करण इकाई",
            "Grocery & Daily-Needs Store":"किराना और दैनिक जरूरतों की दुकान",
            "Street Food / Snack Business":"स्ट्रीट फूड / स्नैक व्यवसाय",
            "Dairy / Milk-Based Business":"डेयरी / दूध आधारित व्यवसाय",
            "Goat / Sheep Rearing":"बकरी / भेड़ पालन",
            "Poultry Farming":"पोल्ट्री फार्मिंग",
            "Local Delivery & Transport Service":"स्थानीय डिलीवरी और परिवहन सेवा",
            "Tailoring & Garment Service":"सिलाई और परिधान सेवा",
            "Handicrafts & Local Products":"हस्तशिल्प और स्थानीय उत्पाद",
            "Farm Input & Agri Service Centre":"कृषि इनपुट और कृषि सेवा केंद्र",
            "Small Repair & Service Centre":"छोटा मरम्मत और सेवा केंद्र"
        },
        "Kannada": {
            "Vegetable Cultivation":"ತರಕಾರಿ ಕೃಷಿ",
            "Small Food Processing Unit":"ಸಣ್ಣ ಆಹಾರ ಸಂಸ್ಕರಣಾ ಘಟಕ",
            "Grocery & Daily-Needs Store":"ಕಿರಾಣಿ ಮತ್ತು ದೈನಂದಿನ ಅಗತ್ಯಗಳ ಅಂಗಡಿ",
            "Street Food / Snack Business":"ಸ್ಟ್ರೀಟ್ ಫುಡ್ / ತಿಂಡಿ ವ್ಯವಹಾರ",
            "Dairy / Milk-Based Business":"ಡೈರಿ / ಹಾಲು ಆಧಾರಿತ ವ್ಯವಹಾರ",
            "Goat / Sheep Rearing":"ಮೇಕೆ / ಕುರಿ ಸಾಕಣೆ",
            "Poultry Farming":"ಕೋಳಿ ಸಾಕಣೆ",
            "Local Delivery & Transport Service":"ಸ್ಥಳೀಯ ವಿತರಣೆ ಮತ್ತು ಸಾರಿಗೆ ಸೇವೆ",
            "Tailoring & Garment Service":"ಹೊಲಿಗೆ ಮತ್ತು ಉಡುಪು ಸೇವೆ",
            "Handicrafts & Local Products":"ಕರಕುಶಲ ಮತ್ತು ಸ್ಥಳೀಯ ಉತ್ಪನ್ನಗಳು",
            "Farm Input & Agri Service Centre":"ಕೃಷಿ ಇನ್‌ಪುಟ್ ಮತ್ತು ಕೃಷಿ ಸೇವಾ ಕೇಂದ್ರ",
            "Small Repair & Service Centre":"ಸಣ್ಣ ದುರಸ್ತಿ ಮತ್ತು ಸೇವಾ ಕೇಂದ್ರ"
        }
    }

    REASON_TR = {
        "Hindi": {
            "Your available capital comfortably covers the indicative investment range.":"आपकी उपलब्ध पूंजी अनुमानित निवेश सीमा को आराम से कवर करती है।",
            "Your capital fits the lower-to-middle part of the indicative investment range.":"आपकी पूंजी अनुमानित निवेश सीमा के शुरुआती से मध्य भाग में फिट होती है।",
            "Your capital is below the typical starting range, so a smaller pilot may be needed.":"आपकी पूंजी सामान्य शुरुआती सीमा से कम है, इसलिए छोटा पायलट बेहतर हो सकता है।",
            "Capital is currently limited for this model.":"इस मॉडल के लिए वर्तमान पूंजी सीमित है।",
            "Your available resources can support this type of business.":"आपके उपलब्ध संसाधन इस प्रकार के व्यवसाय में मदद कर सकते हैं।",
            "You may need to arrange some additional resources before starting.":"शुरू करने से पहले आपको कुछ अतिरिक्त संसाधनों की व्यवस्था करनी पड़ सकती है।",
            "The business matches your stated interest.":"यह व्यवसाय आपकी बताई गई रुचि से मेल खाता है।",
            "Good water availability improves feasibility.":"अच्छी पानी की उपलब्धता व्यवहार्यता बढ़ाती है।",
            "Limited water availability makes this business more sensitive to planning.":"सीमित पानी की उपलब्धता के कारण इस व्यवसाय में बेहतर योजना की जरूरत है।",
            "Your existing experience reduces the learning curve.":"आपका अनुभव सीखने की अवधि को कम करता है।",
            "Your experience is a strong fit for execution.":"आपका अनुभव इस व्यवसाय को चलाने के लिए उपयोगी है।",
            "A small pilot and basic training are recommended before scaling.":"बड़ा निवेश करने से पहले छोटा पायलट और बुनियादी प्रशिक्षण उपयोगी रहेगा।"
        },
        "Kannada": {
            "Your available capital comfortably covers the indicative investment range.":"ನಿಮ್ಮ ಲಭ್ಯವಿರುವ ಬಂಡವಾಳವು ಅಂದಾಜು ಹೂಡಿಕೆ ವ್ಯಾಪ್ತಿಯನ್ನು ಸುಲಭವಾಗಿ ಪೂರೈಸುತ್ತದೆ.",
            "Your capital fits the lower-to-middle part of the indicative investment range.":"ನಿಮ್ಮ ಬಂಡವಾಳವು ಅಂದಾಜು ಹೂಡಿಕೆ ವ್ಯಾಪ್ತಿಯ ಆರಂಭಿಕದಿಂದ ಮಧ್ಯಮ ಭಾಗಕ್ಕೆ ಹೊಂದಿಕೊಳ್ಳುತ್ತದೆ.",
            "Your capital is below the typical starting range, so a smaller pilot may be needed.":"ನಿಮ್ಮ ಬಂಡವಾಳವು ಸಾಮಾನ್ಯ ಆರಂಭಿಕ ವ್ಯಾಪ್ತಿಗಿಂತ ಕಡಿಮೆಯಿದೆ; ಆದ್ದರಿಂದ ಸಣ್ಣ ಪೈಲಟ್ ಸೂಕ್ತವಾಗಬಹುದು.",
            "Capital is currently limited for this model.":"ಈ ಮಾದರಿಗೆ ಪ್ರಸ್ತುತ ಬಂಡವಾಳ ಸೀಮಿತವಾಗಿದೆ.",
            "Your available resources can support this type of business.":"ನಿಮ್ಮ ಲಭ್ಯವಿರುವ ಸಂಪನ್ಮೂಲಗಳು ಈ ರೀತಿಯ ವ್ಯವಹಾರಕ್ಕೆ ಸಹಾಯ ಮಾಡಬಹುದು.",
            "You may need to arrange some additional resources before starting.":"ಆರಂಭಿಸುವ ಮೊದಲು ಕೆಲವು ಹೆಚ್ಚುವರಿ ಸಂಪನ್ಮೂಲಗಳನ್ನು ವ್ಯವಸ್ಥೆ ಮಾಡಬೇಕಾಗಬಹುದು.",
            "The business matches your stated interest.":"ಈ ವ್ಯವಹಾರವು ನಿಮ್ಮ ಆಸಕ್ತಿಗೆ ಹೊಂದಿಕೊಳ್ಳುತ್ತದೆ.",
            "Good water availability improves feasibility.":"ಉತ್ತಮ ನೀರಿನ ಲಭ್ಯತೆ ವ್ಯವಹಾರದ ಸಾಧ್ಯತೆಯನ್ನು ಹೆಚ್ಚಿಸುತ್ತದೆ.",
            "Limited water availability makes this business more sensitive to planning.":"ಸೀಮಿತ ನೀರಿನ ಲಭ್ಯತೆಯಿಂದ ಉತ್ತಮ ಯೋಜನೆ ಅಗತ್ಯವಾಗುತ್ತದೆ.",
            "Your existing experience reduces the learning curve.":"ನಿಮ್ಮ ಅನುಭವ ಕಲಿಕೆಯ ಅವಧಿಯನ್ನು ಕಡಿಮೆ ಮಾಡುತ್ತದೆ.",
            "Your experience is a strong fit for execution.":"ನಿಮ್ಮ ಅನುಭವ ವ್ಯವಹಾರ ನಡೆಸಲು ಉತ್ತಮವಾಗಿ ಹೊಂದಿಕೊಳ್ಳುತ್ತದೆ.",
            "A small pilot and basic training are recommended before scaling.":"ವಿಸ್ತರಿಸುವ ಮೊದಲು ಸಣ್ಣ ಪೈಲಟ್ ಮತ್ತು ಮೂಲಭೂತ ತರಬೇತಿ ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ."
        }
    }

    def business_name(value):
        return BUSINESS_NAME_TR.get(language, {}).get(value, value)

    def reason_text(value):
        return REASON_TR.get(language, {}).get(value, value)

    BUSINESS_SCHEME_NAME_TR = {
        "Hindi": {
            "Kisan Credit Card": "किसान क्रेडिट कार्ड",
            "PMEGP": "PMEGP – प्रधानमंत्री रोजगार सृजन कार्यक्रम",
            "MUDRA": "प्रधानमंत्री मुद्रा योजना (MUDRA)",
            "PM SVANidhi": "PM SVANidhi – प्रधानमंत्री स्ट्रीट वेंडर्स आत्मनिर्भर निधि",
            "PMFME": "PMFME – प्रधानमंत्री सूक्ष्म खाद्य प्रसंस्करण उद्यम योजना",
            "Agriculture Infrastructure Fund": "कृषि अवसंरचना कोष",
            "ACABC": "एग्री-क्लिनिक और एग्री-बिजनेस सेंटर (ACABC)",
            "PM Vishwakarma": "PM विश्वकर्मा"
        },
        "Kannada": {
            "Kisan Credit Card": "ಕಿಸಾನ್ ಕ್ರೆಡಿಟ್ ಕಾರ್ಡ್",
            "PMEGP": "PMEGP – ಪ್ರಧಾನ ಮಂತ್ರಿ ಉದ್ಯೋಗ ಸೃಜನ ಕಾರ್ಯಕ್ರಮ",
            "MUDRA": "ಪ್ರಧಾನ ಮಂತ್ರಿ ಮುದ್ರಾ ಯೋಜನೆ (MUDRA)",
            "PM SVANidhi": "PM SVANidhi – ಪ್ರಧಾನ ಮಂತ್ರಿ ಬೀದಿ ವ್ಯಾಪಾರಿಗಳ ಆತ್ಮನಿರ್ಭರ ನಿಧಿ",
            "PMFME": "PMFME – ಪ್ರಧಾನ ಮಂತ್ರಿ ಸೂಕ್ಷ್ಮ ಆಹಾರ ಸಂಸ್ಕರಣಾ ಉದ್ಯಮ ಯೋಜನೆ",
            "Agriculture Infrastructure Fund": "ಕೃಷಿ ಮೂಲಸೌಕರ್ಯ ನಿಧಿ",
            "ACABC": "ಅಗ್ರಿ-ಕ್ಲಿನಿಕ್ ಮತ್ತು ಅಗ್ರಿ-ಬಿಸಿನೆಸ್ ಕೇಂದ್ರಗಳು (ACABC)",
            "PM Vishwakarma": "PM ವಿಶ್ವಕರ್ಮ"
        }
    }

    def business_scheme_name(value):
        return BUSINESS_SCHEME_NAME_TR.get(language, {}).get(value, value)

    if st.button(tr("generate"), type="primary", use_container_width=True):
        scored = []

        # All five user inputs are now guaranteed to exist.
        for business in BUSINESSES:
            score, reasons = calculate_match(
                business=business,
                capital=capital,
                resources=resources,
                interest=interest,
                water=local_water,
                experience=experience,
                location=location
            )
            scored.append({
                "business": business,
                "score": score,
                "reasons": reasons
            })

        scored.sort(key=lambda x: x["score"], reverse=True)
        top = scored[:3]

        st.success(tr("three"))

        for rank, item in enumerate(top, start=1):
            business = item["business"]
            score = item["score"]
            display_name = business_name(business["name"])

            st.markdown(
                f"""
                <div class="recommendation">
                    <h2>#{rank} {display_name}</h2>
                    <div class="score">{score}% {tr("match")}</div>
                    <p><strong>{tr("investment")}:</strong> {business_content("investment", business["investment"])}</p>
                    <p><strong>{tr("model")}:</strong> {business_content("model", business["model"])}</p>
                </div>
                """,
                unsafe_allow_html=True
            )

            left, right = st.columns(2)
            with left:
                animal_advice = get_animal_advisory(business["name"], location)
                if animal_advice:
                    st.markdown("#### 🐄 " + ui("animal_advisory"))
                    st.info(f"**{ui('animal')}:** {animal_text(animal_advice['animal'])}\n\n**{ui('breed')}:** {animal_text(animal_advice['breed'])}\n\n**{ui('why_suggestion')}:** {animal_text(animal_advice['why'])}")
                    st.markdown("**" + ui("care") + ":**")
                    for care_item in animal_advice["care"]:
                        st.write("• " + animal_text(care_item))
                    st.caption(ui("animal_note"))

                st.markdown("#### " + tr("why_match"))
                for reason in item["reasons"][:5]:
                    st.write("✅ " + reason_text(reason))
                st.markdown("#### " + tr("risk"))
                st.write("⚠️ " + business_content("risk", business["risk"]))

            with right:
                st.markdown("#### " + tr("steps"))
                for step in business["steps"]:
                    st.write("• " + business_content("steps", step))
                st.markdown("#### " + tr("relevant"))
                for scheme in business["schemes"]:
                    st.write("🏛️ " + business_scheme_name(scheme))
                    # Show business-specific scheme information instead of only a name.
                    scheme_obj = next((s for s in SCHEMES if s["name"].startswith(scheme) or scheme in s["name"]), None)
                    if scheme_obj:
                        st.caption(f"**{tr('why')}:** {stext('why', scheme_obj['why'])}")
                        st.caption(f"**{tr('key')}:** {scheme_extra('key', scheme_obj['key'])}")

                    scheme_details = get_scheme_details(scheme)
                    if scheme_details:
                        with st.expander(f"📋 {tr('eligibility')} & {tr('documents')}"):
                            st.markdown(f"**{tr('eligibility')}:** {scheme_eligibility_text(scheme_details['eligibility'])}")
                            st.markdown(f"**{tr('documents')}:**")
                            for doc in scheme_details["documents"]:
                                st.write("• " + scheme_document_text(doc))

            st.divider()

        st.markdown(f"### {tr('next_action')}")
        best = top[0]["business"]
        if capital < best["capital"][0]:
            st.warning(tr("below", business=business_name(best["name"])))
        else:
            st.success(tr("next", business=business_name(best["name"])))

        # ---------------------------------------------------------
        # BUSINESS SUCCESS / RISK OUTLOOK
        # ---------------------------------------------------------
        outlook = BUSINESS_OUTLOOK.get(best["name"], {
            "success_period": "3–6 months",
            "stable_period": "6–12 months",
            "risk_period": "first 3–6 months",
            "base_success": 65
        })
        # Convert the recommendation score into a prototype planning range.
        best_score = top[0]["score"]
        lower = max(40, min(90, outlook["base_success"] + int(best_score * 0.08) - 6))
        upper = min(95, lower + 10)

        st.markdown("### 📊 " + ui("business_risk_outlook"))
        st.caption(ui("planning_est"))
        o1, o2, o3 = st.columns(3)
        o1.metric(ui("success_potential"), f"{lower}–{upper}%")
        o2.metric(ui("first_results"), period_text(outlook["success_period"]))
        o3.metric(ui("higher_risk"), period_text(outlook["risk_period"]))
        st.info(f"📈 **{ui('stabilisation')}:** {period_text(outlook['stable_period'])}. {ui('success_context')}")

        st.caption(tr("limit"))

# ============================================================
# SEASONAL + LOCATION FARMING ADVISOR
# ============================================================

if page == "Business Recommendation":
    st.markdown("---")
    st.title("🌱 " + ui("farming_title"))
    st.write(ui("farming_desc"))

    season_options = ["Kharif", "Rabi", "Summer"]
    selected_season = st.selectbox(
        "🌦️ " + ui("farming_season"),
        season_options,
        index=season_options.index(current_season()),
        format_func=lambda x: ui_data(x, "season")
    )
    local_water = location_water(location)

    st.info(
        f"📍 {ui('farming_location')}: **{ui_data(location, 'location_name')}**  |  "
        f"🌦️ {ui('farming_season')}: **{ui_data(selected_season, 'season')}**  |  "
        f"💧 {ui('water_need')}: **{ui_data(local_water, 'water')}**"
    )

    recommendations = best_crops_for_location(location, selected_season, limit=5)

    if recommendations:
        st.subheader("🌾 " + ui("farming_recommend"))
        st.caption(ui("farming_note"))

        for rank, (crop, base_score, info) in enumerate(recommendations, start=1):
            suitability = crop_suitability(crop, location, selected_season)
            st.markdown(f"### #{rank} {tr_data(crop)} — {suitability}% {ui('compare_suitability').lower()}")
            c1, c2, c3, c4 = st.columns(4)
            c1.metric(ui("season"), ", ".join(ui_data(x, "season") for x in info["seasons"]))
            c2.metric(ui("water_need"), ui_data(info["water"], "water"))
            c3.metric(ui("harvest"), info["harvest"])
            c4.metric(ui("base_potential"), f"{info['success']}%")
            st.write(f"**{ui('why_here')}:** {ui('included')} — {ui_data(location, 'location_name')}")
            st.write(f"**{ui('main_risk')}:** {crop_text(info['risk'])}")
            st.divider()
    else:
        st.warning(ui("no_crop"))

    st.info("💡 " + ui("farming_example"))

# -----------------------------
# FOOTER
# -----------------------------
st.markdown(
    f"""
    <div class="footer">
        {tr("footer")}<br>
        <span class="small-note">{tr("footer_note")}</span>
    </div>
    """,
    unsafe_allow_html=True
)
