import streamlit as st
import math
import datetime
import html
from pathlib import Path

try:
    import requests
except ImportError:
    requests = None

try:
    import pandas as pd
except ImportError:
    pd = None
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
:root {
  --gs-green:#2E7D32;
  --gs-green-dark:#1B5E20;
  --gs-mint:#E8F5E9;
  --gs-slate:#374151;
  --gs-muted:#6B7280;
  --gs-border:rgba(46,125,50,.18);
  --gs-card:#FFFFFF;
  --gs-bg:#F6FAF7;
}
.stApp{background:linear-gradient(180deg,#F8FBF8 0%,#F4F8F5 100%);color:var(--gs-slate);}
[data-theme="dark"] .stApp{background:#0e1510;color:#E5E7EB;}
.block-container{padding-top:1.5rem;padding-bottom:3rem;max-width:1480px;}
.hero{padding:1.7rem 1.9rem;border-radius:18px;background:linear-gradient(135deg,var(--gs-mint),#FFFFFF);border:1px solid var(--gs-border);margin-bottom:1.3rem;box-shadow:0 8px 24px rgba(27,94,32,.08);}
.hero h1{font-size:2.55rem;margin-bottom:.25rem;color:var(--gs-green-dark);}
.hero p{font-size:1.05rem;color:var(--gs-muted);line-height:1.6;}
.gs-card,.gs-metric,.gs-phase,.gs-scheme,.gs-table-wrap{border-radius:12px;border:1px solid var(--gs-border);box-shadow:0 4px 6px -1px rgba(0,0,0,.10),0 8px 18px rgba(27,94,32,.045);}
.gs-card{background:var(--gs-card);padding:20px;margin:.55rem 0 1rem;}
.gs-table-wrap{background:var(--gs-card);padding:12px 14px;margin:.6rem 0 1rem;overflow-x:auto;}
[data-theme="dark"] .gs-card,[data-theme="dark"] .gs-metric,[data-theme="dark"] .gs-phase,[data-theme="dark"] .gs-scheme,[data-theme="dark"] .gs-table-wrap{background:#141c16;border-color:rgba(144,202,149,.20);}
.gs-section-title{color:var(--gs-green-dark);font-weight:800;font-size:1.10rem;margin:.1rem 0 .4rem;}
.gs-microcopy{color:var(--gs-muted);font-size:.84rem;line-height:1.45;margin-bottom:.6rem;}
.gs-stepper{display:flex;gap:8px;flex-wrap:wrap;margin:.3rem 0 1.1rem;}
.gs-step{padding:7px 12px;border-radius:999px;border:1px solid var(--gs-border);background:#fff;font-size:.84rem;font-weight:700;color:#49604d;}
.gs-step.active{background:var(--gs-green);color:#fff;border-color:var(--gs-green);}
.gs-metric{background:linear-gradient(135deg,#F4FBF5,#FFFFFF);padding:16px 17px;min-height:106px;}
.gs-metric .label{font-size:.75rem;color:var(--gs-muted);text-transform:uppercase;letter-spacing:.05em;font-weight:750;}
.gs-metric .value{font-size:1.55rem;font-weight:850;color:var(--gs-green-dark);margin-top:4px;}
.gs-metric .hint{font-size:.78rem;color:var(--gs-muted);margin-top:5px;}
.gs-phase{padding:17px 18px;background:linear-gradient(135deg,rgba(232,245,233,.82),#fff);height:100%;}
.gs-phase .phase-no{display:inline-block;background:var(--gs-green);color:#fff;padding:4px 9px;border-radius:999px;font-size:.74rem;font-weight:800;margin-bottom:8px;}
.gs-risk-high{border-left:5px solid #C62828!important}.gs-risk-medium{border-left:5px solid #EF8B00!important}.gs-risk-low{border-left:5px solid #2E7D32!important}
.gs-scheme{padding:15px;background:linear-gradient(135deg,#F1F8F2,#FFFFFF);margin-bottom:12px;}
.gs-table{width:100%;border-collapse:collapse;font-size:.92rem;}
.gs-table th{background:var(--gs-green);color:#fff;text-align:left;padding:10px 11px;white-space:nowrap;}
.gs-table td{padding:9px 11px;border-bottom:1px solid rgba(107,114,128,.16);vertical-align:top;line-height:1.45;}
.gs-table tr:nth-child(even) td{background:rgba(232,245,233,.34);}
[data-theme="dark"] .gs-table tr:nth-child(even) td{background:rgba(46,125,50,.09);}
[data-theme="dark"] .gs-table td{border-bottom-color:rgba(229,231,235,.12);}
.gs-insight{padding:.85rem 1rem;border-radius:10px;background:var(--gs-mint);border-left:4px solid var(--gs-green);margin:.6rem 0;}
.gs-alert-note{font-size:.82rem;color:var(--gs-muted);}
.stExpander{border:1px solid var(--gs-border)!important;border-radius:12px!important;background:rgba(255,255,255,.72)!important;box-shadow:0 4px 6px -1px rgba(0,0,0,.06)!important;}
[data-theme="dark"] .stExpander{background:#121a15!important;}
div[data-baseweb="select"]>div,div[data-baseweb="input"]>div,textarea{border-radius:10px!important;}
input,textarea{line-height:1.4!important;}
button[kind="primary"]{background:var(--gs-green)!important;border-color:var(--gs-green)!important;}
button[kind="primary"]:hover{background:var(--gs-green-dark)!important;border-color:var(--gs-green-dark)!important;}
.footer{text-align:center;color:var(--gs-muted);padding:2rem 0 .5rem;}
.small-note{color:var(--gs-muted);font-size:.86rem;}

.gs-roadmap-wrap{position:relative}.gs-roadmap-card{background:#fff;border:1px solid var(--gs-border);border-left:5px solid var(--gs-green);border-radius:16px;padding:18px 20px;margin:6px 0;box-shadow:0 6px 18px rgba(46,125,50,.08)}.gs-roadmap-top{display:flex;align-items:center;gap:14px}.gs-roadmap-number{width:42px;height:42px;border-radius:12px;display:flex;align-items:center;justify-content:center;font-size:16px;font-weight:800;flex:0 0 42px}.gs-roadmap-heading{flex:1;min-width:0}.gs-roadmap-tag{font-size:11px;font-weight:800;letter-spacing:.08em}.gs-roadmap-title{font-size:21px;font-weight:800;color:var(--gs-slate);line-height:1.2;margin-top:2px}.gs-roadmap-duration{background:#f6f8f6;border:1px solid #e4ebe5;padding:8px 11px;border-radius:999px;font-size:12px;font-weight:700;color:#52605a;white-space:nowrap}.gs-roadmap-goal{margin:15px 0 12px;color:#46524b;line-height:1.55}.gs-roadmap-checks{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:10px}.gs-roadmap-check{display:flex;gap:8px;padding:11px 12px;background:#f9fbf9;border:1px solid #e9efea;border-radius:10px;color:#46524b;font-size:13px;line-height:1.45}.gs-roadmap-check span:first-child{width:22px;height:22px;border-radius:50%;background:#E8F5E9;color:#2E7D32;font-weight:900;display:flex;align-items:center;justify-content:center;flex:0 0 22px}.gs-roadmap-gate{margin-top:13px;padding:10px 12px;border-radius:9px;background:#F1F8E9;color:#33691E;font-size:12px;font-weight:700}.gs-roadmap-connector{width:2px;height:18px;background:#c7d8ca;margin-left:21px}.gs-roadmap-final{display:flex;align-items:flex-start;gap:12px;margin-top:18px}.gs-roadmap-final-icon{width:34px;height:34px;border-radius:10px;background:#E8F5E9;color:#2E7D32;display:flex;align-items:center;justify-content:center;font-weight:900;flex:0 0 34px}@media(max-width:900px){.gs-roadmap-checks{grid-template-columns:1fr}.gs-roadmap-duration{display:none}}

.gs-scheme-hero{display:flex;gap:16px;align-items:center;padding:20px 24px;border-radius:20px;background:linear-gradient(135deg,#E8F5E9 0%,#FFFFFF 72%);border:1px solid var(--gs-border);box-shadow:0 10px 28px rgba(27,94,32,.08);margin-bottom:18px}
.gs-scheme-hero-icon{width:58px;height:58px;border-radius:16px;display:flex;align-items:center;justify-content:center;background:#fff;border:1px solid var(--gs-border);font-size:29px;flex:0 0 58px}.gs-eyebrow{font-size:.72rem;letter-spacing:.12em;font-weight:850;color:var(--gs-green);margin-bottom:3px}.gs-scheme-hero h1{margin:0!important;font-size:2rem!important;color:var(--gs-green-dark)!important}.gs-scheme-hero p{margin:.25rem 0 0!important;color:var(--gs-muted);line-height:1.45}.gs-filter-spacer{height:26px}.gs-scheme-stat{border:1px solid var(--gs-border);border-radius:14px;background:#fff;padding:12px 14px;min-height:88px;display:flex;flex-direction:column;justify-content:center}.gs-scheme-stat span{font-size:17px}.gs-scheme-stat strong{font-size:1.35rem;color:var(--gs-green-dark);line-height:1.1}.gs-scheme-stat small{color:var(--gs-muted);font-size:.75rem;margin-top:4px}.gs-match-note{font-size:.82rem;color:var(--gs-muted);padding:9px 12px;border-radius:10px;background:rgba(232,245,233,.55);margin:6px 0 14px}.gs-scheme-card{border:1px solid var(--gs-border);border-radius:16px;padding:17px 18px;background:#fff;box-shadow:0 6px 20px rgba(27,94,32,.055);margin:8px 0 0}.gs-match-high{border-left:5px solid #2E7D32}.gs-match-mid{border-left:5px solid #EF8B00}.gs-match-low{border-left:5px solid #9E9E9E}.gs-scheme-card-top{display:flex;align-items:center;gap:13px}.gs-scheme-index{width:38px;height:38px;border-radius:11px;background:#F1F8E9;color:#33691E;font-size:.78rem;font-weight:850;display:flex;align-items:center;justify-content:center;flex:0 0 38px}.gs-scheme-card-title{min-width:0;flex:1}.gs-scheme-name{font-size:1.08rem;font-weight:850;color:var(--gs-green-dark);line-height:1.25}.gs-chip-row{display:flex;gap:5px;flex-wrap:wrap;margin-top:6px}.gs-chip{font-size:.68rem;padding:3px 8px;border-radius:999px;background:#F5F7F5;border:1px solid #E3E9E4;color:#5A665E}.gs-match-badge{padding:7px 10px;border-radius:999px;background:#EAF6EC;color:#25612A;font-size:.76rem;font-weight:850;white-space:nowrap}.gs-benefit-strip{display:flex;gap:10px;margin-top:13px;padding:11px 12px;border-radius:11px;background:#F6FBF6;color:#45534A;font-size:.86rem;line-height:1.45}.gs-benefit-strip span{font-size:18px}.gs-detail-panel{border:1px solid #E1E9E2;border-radius:13px;background:#F8FBF8;padding:14px}.gs-detail-label{font-size:.73rem;text-transform:uppercase;letter-spacing:.05em;color:var(--gs-muted);font-weight:800;margin-top:7px}.gs-detail-label:first-child{margin-top:0}.gs-detail-value{font-size:1.08rem;font-weight:850;color:var(--gs-green-dark);margin:4px 0 12px}.gs-progress{height:8px;border-radius:999px;background:#E5EAE6;overflow:hidden;margin-top:6px}.gs-progress div{height:100%;background:#2E7D32;border-radius:999px}.gs-detail-small{font-size:.72rem;color:var(--gs-muted);margin-top:5px}.gs-reason-box{padding:11px 13px;border-radius:11px;background:#F4FAF5;border-left:4px solid #2E7D32;margin:12px 0}.gs-reason-box ul{margin:.35rem 0 0 1.1rem;padding:0}.gs-reason-box li{margin:3px 0;color:#4A554E;font-size:.83rem}
[data-theme="dark"] .gs-scheme-hero,[data-theme="dark"] .gs-scheme-stat,[data-theme="dark"] .gs-scheme-card{background:#141c16}.gs-scheme-hero h1,[data-theme="dark"] .gs-scheme-name{color:#A5D6A7!important}.gs-detail-panel,[data-theme="dark"] .gs-detail-panel{background:#182219;border-color:rgba(144,202,149,.2)}
@media(max-width:800px){.gs-scheme-card-top{align-items:flex-start}.gs-match-badge{font-size:.68rem;padding:6px 8px}.gs-scheme-hero{padding:16px}.gs-scheme-hero-icon{display:none}}
</style>
""", unsafe_allow_html=True)


# -----------------------------
# TRANSLATIONS
# -----------------------------
TEXT = {
    "English": {
        "language": "Language", "location": "Market Location", "navigate": "Navigate",
        "home": "Home", "market": "Market Prices", "schemes": "Government Schemes",
        "finance": "Financial Assistant", "business": "Business Recommendation",
        "welcome": "Welcome to Gram Sahayak",
        "subtitle": "Business & Financial Guidance for Rural Micro-Entrepreneurs",
        "home_desc": "A simple digital assistant designed to help rural micro-entrepreneurs explore local business opportunities, understand sample market conditions, estimate finances and discover relevant government schemes.",
        "crops": "Crops Covered", "locations": "Locations", "schemes_count": "Schemes",
        "business_models": "Business Models", "selected_market": "Selected Market",
        "demo_market": "Current demonstration market", "market_disclaimer": "Market prices shown in this prototype are static sample data for demonstration only.",
        "what_can": "What you can do", "explore": "Explore Markets", "explore_desc": "Compare sample prices across a wider set of crops and locations.",
        "plan": "Plan Finances", "plan_desc": "Estimate profit, revenue, costs and loan EMI before making a decision.",
        "find": "Find a Business", "find_desc": "Get a structured business shortlist based on capital, resources, interests and location.",
        "how": "How Gram Sahayak Works", "how_desc": "Your inputs → local context → rule-based business matching → financial planning → relevant scheme suggestions → practical next steps.",
        "market_title": "Market Prices", "market_desc": "Sample market information for **{location}**. Use it for demonstration and planning only; verify current local mandi prices before making financial decisions.",
        "filter": "Filter by crop category", "all": "All", "board": "Crop Market Board", "showing": "Showing {count} crops for the selected demonstration market: {location}",
        "selected_crop": "Selected Crop", "choose_crop": "Choose a crop", "crop": "Crop", "sample_price": "Sample Price", "trend": "Trend",
        "increasing": "Increasing", "stable": "Stable", "decreasing": "Decreasing",
        "market_note": "Important: location factors and prices are controlled demonstration data for this prototype.",
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
        "business_title": "Business Recommendation", "business_desc": "Tell Gram Sahayak about your situation. The prototype will score business models using capital, resources, interest, water availability, experience and location.",
        "capital": "💰 Available capital (₹)", "resource": "🧰 Main available resource", "interest_input": "❤️ Main business interest",
        "water": "💧 Water availability", "experience": "🎯 Your experience", "good": "Good", "limited": "Limited",
        "not_applicable": "Not applicable", "not_sure": "Not sure", "beginner": "Beginner", "some": "Some experience", "experienced": "Experienced",
        "location_note": "📍 Recommendation will be adjusted for the selected market: **{location}**",
        "generate": "🔍 Generate Business Recommendations", "three": "Here are the three strongest prototype matches for your inputs.",
        "match": "Match", "investment": "Indicative investment", "model": "Business model", "why_match": "Why this matches",
        "risk": "Key risk", "steps": "Suggested first steps", "relevant": "Potentially relevant schemes",
        "next_action": "📌 Suggested next action", "below": "Your current capital is below the typical starting range for **{business}**. Consider a smaller pilot, savings, eligible financing or a lower-capital business model.",
        "next": "A practical next step is to prepare a simple cost sheet for **{business}** and compare it with expected local demand before investing.",
        "limit": "Prototype limitation: this is a rule-based recommendation engine using demonstration business profiles. It is a rule-based prototype and does not guarantee profitability.",
        "footer": "🌾 Gram Sahayak • Prototype for rural micro-entrepreneur business guidance",
        "footer_note": "Demo market data • Rule-based recommendations • Verify official scheme information before decisions",
    },
    "Hindi": {
        "language": "भाषा", "location": "बाज़ार स्थान", "navigate": "नेविगेट करें",
        "home": "होम", "market": "बाज़ार भाव", "schemes": "सरकारी योजनाएँ", "finance": "वित्तीय सहायक", "business": "व्यवसाय सुझाव",
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
        "increasing": "बढ़ रहा है", "stable": "स्थिर", "decreasing": "घट रहा है", "market_note": "महत्वपूर्ण: स्थान कारक और भाव नियंत्रित प्रदर्शन डेटा हैं, लाइव बाज़ार डेटा नहीं।",
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
        "capital": "💰 उपलब्ध पूंजी (₹)", "resource": "🧰 मुख्य उपलब्ध संसाधन", "interest_input": "❤️ मुख्य व्यवसाय रुचि", "water": "💧 पानी की उपलब्धता",
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
        "home": "ಮುಖಪುಟ", "market": "ಮಾರುಕಟ್ಟೆ ಬೆಲೆಗಳು", "schemes": "ಸರ್ಕಾರಿ ಯೋಜನೆಗಳು", "finance": "ಹಣಕಾಸು ಸಹಾಯಕ", "business": "ವ್ಯವಹಾರ ಶಿಫಾರಸು",
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
        "increasing": "ಏರಿಕೆ", "stable": "ಸ್ಥಿರ", "decreasing": "ಇಳಿಕೆ", "market_note": "ಮುಖ್ಯ: ಸ್ಥಳದ ಅಂಶಗಳು ಮತ್ತು ಬೆಲೆಗಳು ನಿಯಂತ್ರಿತ ಪ್ರದರ್ಶನ ಡೇಟಾ; ಲೈವ್ ಮಾರುಕಟ್ಟೆ ಫೀಡ್ ಅಲ್ಲ.",
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
        "capital": "💰 ಲಭ್ಯವಿರುವ ಬಂಡವಾಳ (₹)", "resource": "🧰 ಮುಖ್ಯ ಲಭ್ಯವಿರುವ ಸಂಪನ್ಮೂಲ", "interest_input": "❤️ ಮುಖ್ಯ ವ್ಯವಹಾರ ಆಸಕ್ತಿ", "water": "💧 ನೀರಿನ ಲಭ್ಯತೆ",
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

# -----------------------------
# EXTRA TRANSLATIONS (new features)
# Merged into TEXT so tr() keeps working the same way everywhere.
# Anything not translated for Hindi/Kannada gracefully falls back to English
# via the existing tr() lookup — same pattern already used across this file.
# -----------------------------
EXTRA_TEXT = {
    "English": {
        "crop_location_filter": "🌍 Show only crops suited to this location",
        "crop_location_note": "Suitability is based on this prototype's demonstration agro-climatic profile for each location.",
        "no_crops_for_location": "No demonstration crops are marked suitable for this location yet — showing all crops instead.",
        "resource_section_title": "🧾 Detailed resource availability (add one or more)",
        "resource_section_desc": "Add each land/resource you have access to, with its specifications. This improves the accuracy of the match, timeline and risk analysis.",
        "add_resource": "➕ Add another resource",
        "remove_resource": "🗑️ Remove this resource",
        "resource_n": "Resource",
        "resource_type_label": "Resource type",
        "land_area_label": "Area of land (acres)",
        "water_qty_label": "Amount of water available",
        "climate_label": "Climate in this land",
        "labor_label": "Labour available (people)",
        "market_access_label": "Market access",
        "water_none": "None / rain-fed only",
        "water_low": "Low (borewell/limited)",
        "water_medium": "Medium (seasonal canal/tank)",
        "water_high": "High (canal/river/reliable borewell)",
        "climate_dry": "Dry / semi-arid",
        "climate_moderate": "Moderate",
        "climate_humid": "Humid / high rainfall",
        "climate_hilly": "Hilly / cooler",
        "market_poor": "Poor (far from mandi/town)",
        "market_moderate": "Moderate (nearby town)",
        "market_good": "Good (close to mandi/city, transport available)",
        "no_resources_added": "No detailed resources added yet. You can still generate recommendations using the basic inputs above.",
        "success_rate_label": "📊 Estimated feasibility indicator",
        "timeline_label": "⏱️ Typical timeline to profitability",
        "return_label": "📈 Indicative annual return on investment",
        "months": "months",
        "view_details_btn": "🔍 View in-depth analysis",
        "back_to_results": "← Back to all recommendations",
        "deep_dive_title": "In-depth analysis",
        "deep_dive_crops_title": "🌱 Crops that can be grown at this location",
        "deep_dive_crops_none": "This business is not primarily crop-based, so no crop list is shown here.",
        "deep_dive_scheme_title": "🏛️ How each suggested scheme can help",
        "deep_dive_risk_title": "⚠️ Detailed risk analysis",
        "risk_category": "Category", "risk_likelihood": "Likelihood", "risk_impact": "Impact", "risk_mitigation": "Suggested mitigation",
        "deep_dive_invest_title": "💰 Investment vs. expected benefit calculator",
        "min_investment": "Minimum recommended investment for this business",
        "your_investment_input": "Enter an investment amount to check",
        "estimated_annual_benefit": "Indicative estimated annual benefit",
        "estimated_timeline_result": "Indicative timeline before this becomes visible",
        "investment_below_min_warning": "This amount is below the minimum indicative range for this business. Returns and timelines become less predictable below this level.",
        "investment_disclaimer": "These are prototype estimates based on demonstration success-rate and return assumptions for similar rural micro-enterprises. They are not a guarantee of profit and do not replace a proper business plan.",
        "compare_table_title": "Benefit at a few investment levels",
        "invest_level": "Investment", "invest_benefit": "Indicative annual benefit range",
    },
    "Hindi": {
        "crop_location_filter": "🌍 केवल इस स्थान के लिए उपयुक्त फसलें दिखाएँ",
        "crop_location_note": "उपयुक्तता इस प्रोटोटाइप के प्रत्येक स्थान के प्रदर्शन कृषि-जलवायु प्रोफाइल पर आधारित है।",
        "no_crops_for_location": "इस स्थान के लिए अभी कोई नमूना फसल चिह्नित नहीं है — इसलिए सभी फसलें दिखाई जा रही हैं।",
        "resource_section_title": "🧾 विस्तृत संसाधन उपलब्धता (एक या अधिक जोड़ें)",
        "resource_section_desc": "आपके पास मौजूद प्रत्येक भूमि/संसाधन को उसकी विशेषताओं के साथ जोड़ें। इससे मिलान, समयसीमा और जोखिम विश्लेषण अधिक सटीक होगा।",
        "add_resource": "➕ एक और संसाधन जोड़ें",
        "remove_resource": "🗑️ यह संसाधन हटाएँ",
        "resource_n": "संसाधन",
        "resource_type_label": "संसाधन प्रकार",
        "land_area_label": "भूमि का क्षेत्रफल (एकड़)",
        "water_qty_label": "उपलब्ध पानी की मात्रा",
        "climate_label": "इस भूमि की जलवायु",
        "labor_label": "उपलब्ध श्रमिक (संख्या)",
        "market_access_label": "बाज़ार तक पहुँच",
        "water_none": "नहीं / केवल वर्षा आधारित",
        "water_low": "कम (बोरवेल/सीमित)",
        "water_medium": "मध्यम (मौसमी नहर/तालाब)",
        "water_high": "अधिक (नहर/नदी/भरोसेमंद बोरवेल)",
        "climate_dry": "शुष्क / अर्ध-शुष्क",
        "climate_moderate": "सामान्य",
        "climate_humid": "आर्द्र / अधिक वर्षा",
        "climate_hilly": "पहाड़ी / ठंडा",
        "market_poor": "कमज़ोर (मंडी/शहर से दूर)",
        "market_moderate": "मध्यम (नजदीकी कस्बा)",
        "market_good": "अच्छा (मंडी/शहर के पास, परिवहन उपलब्ध)",
        "no_resources_added": "अभी तक कोई विस्तृत संसाधन नहीं जोड़ा गया। आप ऊपर दी गई बुनियादी जानकारी से भी सुझाव प्राप्त कर सकते हैं।",
        "success_rate_label": "📊 अनुमानित सफलता दर",
        "timeline_label": "⏱️ लाभदायक होने की सामान्य समयसीमा",
        "return_label": "📈 अनुमानित वार्षिक निवेश प्रतिफल",
        "months": "महीने",
        "view_details_btn": "🔍 विस्तृत विश्लेषण देखें",
        "back_to_results": "← सभी सुझावों पर वापस जाएँ",
        "deep_dive_title": "विस्तृत विश्लेषण",
        "deep_dive_crops_title": "🌱 इस स्थान पर उगाई जा सकने वाली फसलें",
        "deep_dive_crops_none": "यह व्यवसाय मुख्यतः फसल-आधारित नहीं है, इसलिए यहाँ फसल सूची नहीं दिखाई गई है।",
        "deep_dive_scheme_title": "🏛️ हर सुझाई गई योजना कैसे मदद कर सकती है",
        "deep_dive_risk_title": "⚠️ विस्तृत जोखिम विश्लेषण",
        "risk_category": "श्रेणी", "risk_likelihood": "संभावना", "risk_impact": "प्रभाव", "risk_mitigation": "सुझाया गया समाधान",
        "deep_dive_invest_title": "💰 निवेश बनाम अनुमानित लाभ कैलकुलेटर",
        "min_investment": "इस व्यवसाय के लिए न्यूनतम अनुशंसित निवेश",
        "your_investment_input": "जाँचने के लिए निवेश राशि दर्ज करें",
        "estimated_annual_benefit": "अनुमानित वार्षिक लाभ",
        "estimated_timeline_result": "यह प्रभाव दिखने की अनुमानित समयसीमा",
        "investment_below_min_warning": "यह राशि इस व्यवसाय की न्यूनतम अनुशंसित सीमा से कम है। इस स्तर से नीचे प्रतिफल और समयसीमा कम अनुमानित होती है।",
        "investment_disclaimer": "ये अनुमान समान ग्रामीण सूक्ष्म उद्यमों के लिए प्रदर्शन सफलता-दर और प्रतिफल मान्यताओं पर आधारित प्रोटोटाइप अनुमान हैं। यह लाभ की गारंटी नहीं है और उचित व्यवसाय योजना का विकल्प नहीं है।",
        "compare_table_title": "कुछ निवेश स्तरों पर लाभ",
        "invest_level": "निवेश", "invest_benefit": "अनुमानित वार्षिक लाभ सीमा",
    },
    "Kannada": {
        "crop_location_filter": "🌍 ಈ ಸ್ಥಳಕ್ಕೆ ಸೂಕ್ತವಾದ ಬೆಳೆಗಳನ್ನು ಮಾತ್ರ ತೋರಿಸಿ",
        "crop_location_note": "ಸೂಕ್ತತೆಯು ಈ ಪ್ರೋಟೋಟೈಪ್‌ನ ಪ್ರತಿ ಸ್ಥಳದ ಪ್ರದರ್ಶನ ಕೃಷಿ-ಹವಾಮಾನ ಪ್ರೊಫೈಲ್ ಆಧಾರಿತವಾಗಿದೆ.",
        "no_crops_for_location": "ಈ ಸ್ಥಳಕ್ಕೆ ಇನ್ನೂ ಯಾವುದೇ ಮಾದರಿ ಬೆಳೆ ಗುರುತಿಸಲಾಗಿಲ್ಲ — ಬದಲಿಗೆ ಎಲ್ಲಾ ಬೆಳೆಗಳನ್ನು ತೋರಿಸಲಾಗುತ್ತಿದೆ.",
        "resource_section_title": "🧾 ವಿವರವಾದ ಸಂಪನ್ಮೂಲ ಲಭ್ಯತೆ (ಒಂದು ಅಥವಾ ಹೆಚ್ಚು ಸೇರಿಸಿ)",
        "resource_section_desc": "ನಿಮ್ಮ ಬಳಿ ಇರುವ ಪ್ರತಿ ಭೂಮಿ/ಸಂಪನ್ಮೂಲವನ್ನು ಅದರ ವಿವರಗಳೊಂದಿಗೆ ಸೇರಿಸಿ. ಇದು ಹೊಂದಾಣಿಕೆ, ಸಮಯಪಟ್ಟಿ ಮತ್ತು ಅಪಾಯ ವಿಶ್ಲೇಷಣೆಯ ನಿಖರತೆಯನ್ನು ಸುಧಾರಿಸುತ್ತದೆ.",
        "add_resource": "➕ ಇನ್ನೊಂದು ಸಂಪನ್ಮೂಲ ಸೇರಿಸಿ",
        "remove_resource": "🗑️ ಈ ಸಂಪನ್ಮೂಲ ತೆಗೆದುಹಾಕಿ",
        "resource_n": "ಸಂಪನ್ಮೂಲ",
        "resource_type_label": "ಸಂಪನ್ಮೂಲ ಪ್ರಕಾರ",
        "land_area_label": "ಭೂಮಿಯ ವಿಸ್ತೀರ್ಣ (ಎಕರೆ)",
        "water_qty_label": "ಲಭ್ಯವಿರುವ ನೀರಿನ ಪ್ರಮಾಣ",
        "climate_label": "ಈ ಭೂಮಿಯ ಹವಾಮಾನ",
        "labor_label": "ಲಭ್ಯವಿರುವ ಕಾರ್ಮಿಕರು (ಸಂಖ್ಯೆ)",
        "market_access_label": "ಮಾರುಕಟ್ಟೆ ಪ್ರವೇಶ",
        "water_none": "ಇಲ್ಲ / ಕೇವಲ ಮಳೆ ಆಧಾರಿತ",
        "water_low": "ಕಡಿಮೆ (ಬೋರ್‌ವೆಲ್/ಸೀಮಿತ)",
        "water_medium": "ಮಧ್ಯಮ (ಋತುಮಾನ ಕಾಲುವೆ/ಕೆರೆ)",
        "water_high": "ಹೆಚ್ಚು (ಕಾಲುವೆ/ನದಿ/ವಿಶ್ವಾಸಾರ್ಹ ಬೋರ್‌ವೆಲ್)",
        "climate_dry": "ಒಣ / ಅರೆ-ಶುಷ್ಕ",
        "climate_moderate": "ಸಾಧಾರಣ",
        "climate_humid": "ಆರ್ದ್ರ / ಹೆಚ್ಚು ಮಳೆ",
        "climate_hilly": "ಗುಡ್ಡಗಾಡು / ತಂಪಾದ",
        "market_poor": "ಕಡಿಮೆ (ಮಂಡಿ/ಪಟ್ಟಣದಿಂದ ದೂರ)",
        "market_moderate": "ಮಧ್ಯಮ (ಹತ್ತಿರದ ಪಟ್ಟಣ)",
        "market_good": "ಉತ್ತಮ (ಮಂಡಿ/ನಗರದ ಹತ್ತಿರ, ಸಾರಿಗೆ ಲಭ್ಯ)",
        "no_resources_added": "ಇನ್ನೂ ಯಾವುದೇ ವಿವರವಾದ ಸಂಪನ್ಮೂಲ ಸೇರಿಸಿಲ್ಲ. ಮೇಲಿನ ಮೂಲ ಮಾಹಿತಿಯಿಂದಲೂ ನೀವು ಶಿಫಾರಸುಗಳನ್ನು ಪಡೆಯಬಹುದು.",
        "success_rate_label": "📊 ಅಂದಾಜು ಯಶಸ್ಸಿನ ದರ",
        "timeline_label": "⏱️ ಲಾಭದಾಯಕವಾಗಲು ಸಾಮಾನ್ಯ ಸಮಯಪಟ್ಟಿ",
        "return_label": "📈 ಅಂದಾಜು ವಾರ್ಷಿಕ ಹೂಡಿಕೆ ಪ್ರತಿಫಲ",
        "months": "ತಿಂಗಳುಗಳು",
        "view_details_btn": "🔍 ವಿವರವಾದ ವಿಶ್ಲೇಷಣೆ ನೋಡಿ",
        "back_to_results": "← ಎಲ್ಲಾ ಶಿಫಾರಸುಗಳಿಗೆ ಹಿಂತಿರುಗಿ",
        "deep_dive_title": "ವಿವರವಾದ ವಿಶ್ಲೇಷಣೆ",
        "deep_dive_crops_title": "🌱 ಈ ಸ್ಥಳದಲ್ಲಿ ಬೆಳೆಯಬಹುದಾದ ಬೆಳೆಗಳು",
        "deep_dive_crops_none": "ಈ ವ್ಯವಹಾರವು ಮುಖ್ಯವಾಗಿ ಬೆಳೆ-ಆಧಾರಿತವಲ್ಲ, ಆದ್ದರಿಂದ ಇಲ್ಲಿ ಬೆಳೆ ಪಟ್ಟಿ ತೋರಿಸಲಾಗಿಲ್ಲ.",
        "deep_dive_scheme_title": "🏛️ ಪ್ರತಿ ಶಿಫಾರಸು ಮಾಡಿದ ಯೋಜನೆ ಹೇಗೆ ಸಹಾಯ ಮಾಡಬಹುದು",
        "deep_dive_risk_title": "⚠️ ವಿವರವಾದ ಅಪಾಯ ವಿಶ್ಲೇಷಣೆ",
        "risk_category": "ವರ್ಗ", "risk_likelihood": "ಸಾಧ್ಯತೆ", "risk_impact": "ಪರಿಣಾಮ", "risk_mitigation": "ಸೂಚಿಸಿದ ಪರಿಹಾರ",
        "deep_dive_invest_title": "💰 ಹೂಡಿಕೆ ಮತ್ತು ಅಂದಾಜು ಲಾಭ ಕ್ಯಾಲ್ಕುಲೇಟರ್",
        "min_investment": "ಈ ವ್ಯವಹಾರಕ್ಕೆ ಕನಿಷ್ಠ ಶಿಫಾರಸು ಮಾಡಿದ ಹೂಡಿಕೆ",
        "your_investment_input": "ಪರಿಶೀಲಿಸಲು ಹೂಡಿಕೆ ಮೊತ್ತ ನಮೂದಿಸಿ",
        "estimated_annual_benefit": "ಅಂದಾಜು ವಾರ್ಷಿಕ ಲಾಭ",
        "estimated_timeline_result": "ಇದು ಗೋಚರಿಸುವ ಅಂದಾಜು ಸಮಯಪಟ್ಟಿ",
        "investment_below_min_warning": "ಈ ಮೊತ್ತವು ಈ ವ್ಯವಹಾರದ ಕನಿಷ್ಠ ಶಿಫಾರಸು ವ್ಯಾಪ್ತಿಗಿಂತ ಕಡಿಮೆಯಿದೆ. ಈ ಮಟ್ಟಕ್ಕಿಂತ ಕಡಿಮೆ ಪ್ರತಿಫಲ ಮತ್ತು ಸಮಯಪಟ್ಟಿ ಕಡಿಮೆ ಊಹಿಸಬಹುದಾಗಿರುತ್ತದೆ.",
        "investment_disclaimer": "ಇವು ಇದೇ ರೀತಿಯ ಗ್ರಾಮೀಣ ಸಣ್ಣ ಉದ್ಯಮಗಳಿಗೆ ಪ್ರದರ್ಶನ ಯಶಸ್ಸಿನ-ದರ ಮತ್ತು ಪ್ರತಿಫಲ ಊಹೆಗಳ ಆಧಾರದ ಮೇಲೆ ಪ್ರೋಟೋಟೈಪ್ ಅಂದಾಜುಗಳಾಗಿವೆ. ಇದು ಲಾಭದ ಖಾತರಿಯಲ್ಲ ಮತ್ತು ಸೂಕ್ತ ವ್ಯವಹಾರ ಯೋಜನೆಗೆ ಪರ್ಯಾಯವಲ್ಲ.",
        "compare_table_title": "ಕೆಲವು ಹೂಡಿಕೆ ಮಟ್ಟಗಳಲ್ಲಿ ಲಾಭ",
        "invest_level": "ಹೂಡಿಕೆ", "invest_benefit": "ಅಂದಾಜು ವಾರ್ಷಿಕ ಲಾಭ ವ್ಯಾಪ್ತಿ",
    },
}
for _lang in TEXT:
    TEXT[_lang].update(EXTRA_TEXT.get(_lang, {}))

# ------------------------------------------------------------
# Complete UI translation layer for dynamic/business screens
# ------------------------------------------------------------
UI_TR = {
    "Hindi": {
        "market_desc":"**{location}** के लिए प्रदर्शन बाज़ार जानकारी। सभी भाव स्थिर नमूना डेटा हैं।",
        "local_suitability":"स्थानीय फसल उपयुक्तता", "no_suitability":"इस स्थान के लिए अभी कोई मेल खाती नमूना फसल उपलब्ध नहीं है।",
        "market_board":"फसल बाज़ार बोर्ड",
        "Business Domain":"व्यवसाय क्षेत्र", "Specific Business":"विशिष्ट व्यवसाय", "Current Location":"वर्तमान स्थान", "Selected in the sidebar":"साइडबार में चुना गया",
        "Select Business":"व्यवसाय चुनें", "Enter Inputs":"जानकारी दर्ज करें", "Strategic Output":"रणनीतिक परिणाम",
        "Step 1 • Select Business":"चरण 1 • व्यवसाय चुनें", "Step 2 • Enter Inputs":"चरण 2 • जानकारी दर्ज करें", "Step 3 • Strategic Output":"चरण 3 • रणनीतिक परिणाम",
        "Step 1 • Business ✓":"चरण 1 • व्यवसाय ✓", "Step 2 • Inputs ✓":"चरण 2 • जानकारी ✓", "Step 3 • Strategic Output":"चरण 3 • रणनीतिक परिणाम",
        "Location & Climate Parameters":"स्थान और जलवायु पैरामीटर", "Soil & Water Profile":"मिट्टी और पानी प्रोफ़ाइल", "Capital & Financial Goals":"पूंजी और वित्तीय लक्ष्य",
        "Use realistic conditions for the specific site and production period. Defaults are regional planning values and should be replaced with measured/current values where available.":"विशिष्ट स्थान और उत्पादन अवधि के लिए वास्तविक परिस्थितियाँ दर्ज करें। डिफ़ॉल्ट क्षेत्रीय योजना मान हैं; जहाँ संभव हो उन्हें वर्तमान माप से बदलें।",
        "Use the latest soil/water information available. Tooltips explain what each field is used for.":"उपलब्ध नवीनतम मिट्टी/पानी की जानकारी दर्ज करें। टूलटिप हर फ़ील्ड का उपयोग समझाता है।",
        "Enter deployable capital, operating capacity and commercial constraints. Unknown or missing fields are excluded from adaptive scoring.":"उपयोग योग्य पूंजी, संचालन क्षमता और व्यावसायिक सीमाएँ दर्ज करें। अज्ञात या खाली फ़ील्ड स्कोर में शामिल नहीं किए जाते।",
        "This activity does not require additional location/climate inputs beyond the selected location.":"इस गतिविधि के लिए चुने गए स्थान के अलावा अतिरिक्त स्थान/जलवायु जानकारी आवश्यक नहीं है।",
        "No separate soil/water profile is required for this activity.":"इस गतिविधि के लिए अलग मिट्टी/पानी प्रोफ़ाइल आवश्यक नहीं है।",
        "No additional financial/setup inputs are required for this activity.":"इस गतिविधि के लिए अतिरिक्त वित्तीय/सेटअप जानकारी आवश्यक नहीं है।",
        "Tip: use the latest available measurements and realistic capacity. The recommendation engine adapts to partial information.":"सुझाव: नवीनतम माप और वास्तविक क्षमता का उपयोग करें। सिफारिश इंजन उपलब्ध जानकारी के अनुसार अपना आकलन बदलता है।",
        "Generate Recommendation":"सिफारिश बनाएं", "Business Recommendation":"व्यवसाय सिफारिश",
        "Select one business activity and enter only the inputs relevant to that activity. The form adapts automatically and missing values are not treated as zero.":"एक व्यवसाय गतिविधि चुनें और केवल उससे संबंधित जानकारी दर्ज करें। फ़ॉर्म अपने आप अनुकूलित होता है और खाली मानों को शून्य नहीं माना जाता।",
        "Choose the broad business domain first.":"पहले व्यापक व्यवसाय क्षेत्र चुनें।", "Choose the exact activity you want to evaluate.":"जिस गतिविधि का आकलन करना है उसे चुनें।",
        "Rule-based feasibility assessment":"नियम-आधारित व्यवहार्यता आकलन", "Financial figures are planning estimates, not guarantees. Validate local supplier quotes, buyer prices and current scheme rules before committing capital.":"वित्तीय आंकड़े केवल योजना अनुमान हैं, गारंटी नहीं। पूंजी लगाने से पहले स्थानीय आपूर्तिकर्ता दर, खरीदार मूल्य और वर्तमान योजना नियम सत्यापित करें।",
        "Species / Variety / Product Selection":"प्रजाति / किस्म / उत्पाद चयन", "Execution Roadmap":"कार्यान्वयन रोडमैप",
        "Prepare → pilot → validate → scale. Each phase has a clear translate_output_recursive(outcome) and a go/no-go translate_output_recursive(gate).":"तैयारी → पायलट → सत्यापन → विस्तार। हर चरण का स्पष्ट परिणाम और आगे बढ़ने का मानदंड है।",
        "Scale rule":"विस्तार नियम", "Practical Decision Check":"व्यावहारिक निर्णय जाँच", "Financial & Success Benchmarks":"वित्तीय और सफलता मानदंड",
        "Applicable scheme information is shown for the selected business mapping. Eligibility and support depend on current official guidelines.":"चयनित व्यवसाय मैपिंग के लिए संबंधित योजना जानकारी दिखाई गई है। पात्रता और सहायता वर्तमान आधिकारिक दिशानिर्देशों पर निर्भर करती है।",
        "No scheme is currently mapped to this business in the prototype. Use Government Schemes for broader discovery.":"इस प्रोटोटाइप में इस व्यवसाय के लिए कोई योजना मैप नहीं है। अधिक विकल्पों के लिए सरकारी योजनाएँ देखें।",
        "Generate Business Recommendations":"व्यवसाय सिफारिशें बनाएं",
    },
    "Kannada": {
        "market_desc":"**{location}** ಗಾಗಿ ಪ್ರದರ್ಶನ ಮಾರುಕಟ್ಟೆ ಮಾಹಿತಿ. ಎಲ್ಲಾ ಬೆಲೆಗಳು ಸ್ಥಿರ ಮಾದರಿ ಡೇಟಾ.",
        "local_suitability":"ಸ್ಥಳೀಯ ಬೆಳೆ ಸೂಕ್ತತೆ", "no_suitability":"ಈ ಸ್ಥಳಕ್ಕೆ ಹೊಂದುವ ಮಾದರಿ ಬೆಳೆ ಇನ್ನೂ ಲಭ್ಯವಿಲ್ಲ.", "market_board":"ಬೆಳೆ ಮಾರುಕಟ್ಟೆ ಫಲಕ",
        "Business Domain":"ವ್ಯವಹಾರ ಕ್ಷೇತ್ರ", "Specific Business":"ನಿರ್ದಿಷ್ಟ ವ್ಯವಹಾರ", "Current Location":"ಪ್ರಸ್ತುತ ಸ್ಥಳ", "Selected in the sidebar":"ಸೈಡ್‌ಬಾರ್‌ನಲ್ಲಿ ಆಯ್ಕೆ ಮಾಡಲಾಗಿದೆ",
        "Select Business":"ವ್ಯವಹಾರ ಆಯ್ಕೆ", "Enter Inputs":"ಮಾಹಿತಿ ನಮೂದಿಸಿ", "Strategic Output":"ತಂತ್ರಾತ್ಮಕ ಫಲಿತಾಂಶ",
        "Step 1 • Select Business":"ಹಂತ 1 • ವ್ಯವಹಾರ ಆಯ್ಕೆ", "Step 2 • Enter Inputs":"ಹಂತ 2 • ಮಾಹಿತಿ ನಮೂದಿಸಿ", "Step 3 • Strategic Output":"ಹಂತ 3 • ತಂತ್ರಾತ್ಮಕ ಫಲಿತಾಂಶ",
        "Step 1 • Business ✓":"ಹಂತ 1 • ವ್ಯವಹಾರ ✓", "Step 2 • Inputs ✓":"ಹಂತ 2 • ಮಾಹಿತಿ ✓",
        "Location & Climate Parameters":"ಸ್ಥಳ ಮತ್ತು ಹವಾಮಾನ ನಿಯತಾಂಕಗಳು", "Soil & Water Profile":"ಮಣ್ಣು ಮತ್ತು ನೀರಿನ ಪ್ರೊಫೈಲ್", "Capital & Financial Goals":"ಬಂಡವಾಳ ಮತ್ತು ಹಣಕಾಸು ಗುರಿಗಳು",
        "Use realistic conditions for the specific site and production period. Defaults are regional planning values and should be replaced with measured/current values where available.":"ನಿರ್ದಿಷ್ಟ ಸ್ಥಳ ಮತ್ತು ಉತ್ಪಾದನಾ ಅವಧಿಗೆ ನೈಜ ಪರಿಸ್ಥಿತಿಗಳನ್ನು ನಮೂದಿಸಿ. ಡೀಫಾಲ್ಟ್‌ಗಳು ಪ್ರಾದೇಶಿಕ ಯೋಜನಾ ಮೌಲ್ಯಗಳಾಗಿವೆ; ಸಾಧ್ಯವಾದಲ್ಲಿ ಪ್ರಸ್ತುತ ಮಾಪನಗಳಿಂದ ಬದಲಾಯಿಸಿ.",
        "Use the latest soil/water information available. Tooltips explain what each field is used for.":"ಲಭ್ಯವಿರುವ ಇತ್ತೀಚಿನ ಮಣ್ಣು/ನೀರಿನ ಮಾಹಿತಿಯನ್ನು ಬಳಸಿ. ಟೂಲ್‌ಟಿಪ್‌ಗಳು ಪ್ರತಿಯೊಂದು ಕ್ಷೇತ್ರದ ಬಳಕೆಯನ್ನು ವಿವರಿಸುತ್ತವೆ.",
        "Enter deployable capital, operating capacity and commercial constraints. Unknown or missing fields are excluded from adaptive scoring.":"ಬಳಸಬಹುದಾದ ಬಂಡವಾಳ, ಕಾರ್ಯಾಚರಣಾ ಸಾಮರ್ಥ್ಯ ಮತ್ತು ವ್ಯವಹಾರ ಮಿತಿಗಳನ್ನು ನಮೂದಿಸಿ. ತಿಳಿಯದ ಅಥವಾ ಖಾಲಿ ಕ್ಷೇತ್ರಗಳನ್ನು ಅಂಕದಲ್ಲಿ ಸೇರಿಸಲಾಗುವುದಿಲ್ಲ.",
        "This activity does not require additional location/climate inputs beyond the selected location.":"ಈ ಚಟುವಟಿಕೆಗೆ ಆಯ್ಕೆ ಮಾಡಿದ ಸ್ಥಳದ ಹೊರತಾಗಿ ಹೆಚ್ಚುವರಿ ಸ್ಥಳ/ಹವಾಮಾನ ಮಾಹಿತಿ ಅಗತ್ಯವಿಲ್ಲ.",
        "No separate soil/water profile is required for this activity.":"ಈ ಚಟುವಟಿಕೆಗೆ ಪ್ರತ್ಯೇಕ ಮಣ್ಣು/ನೀರಿನ ಪ್ರೊಫೈಲ್ ಅಗತ್ಯವಿಲ್ಲ.",
        "No additional financial/setup inputs are required for this activity.":"ಈ ಚಟುವಟಿಕೆಗೆ ಹೆಚ್ಚುವರಿ ಹಣಕಾಸು/ಸೆಟಪ್ ಮಾಹಿತಿ ಅಗತ್ಯವಿಲ್ಲ.",
        "Tip: use the latest available measurements and realistic capacity. The recommendation engine adapts to partial information.":"ಸಲಹೆ: ಲಭ್ಯವಿರುವ ಇತ್ತೀಚಿನ ಮಾಪನಗಳು ಮತ್ತು ನೈಜ ಸಾಮರ್ಥ್ಯವನ್ನು ಬಳಸಿ. ಶಿಫಾರಸು ಎಂಜಿನ್ ಲಭ್ಯವಿರುವ ಮಾಹಿತಿಗೆ ಹೊಂದಿಕೊಳ್ಳುತ್ತದೆ.",
        "Generate Recommendation":"ಶಿಫಾರಸು ರಚಿಸಿ", "Business Recommendation":"ವ್ಯವಹಾರ ಶಿಫಾರಸು",
        "Select one business activity and enter only the inputs relevant to that activity. The form adapts automatically and missing values are not treated as zero.":"ಒಂದು ವ್ಯವಹಾರ ಚಟುವಟಿಕೆಯನ್ನು ಆಯ್ಕೆ ಮಾಡಿ ಮತ್ತು ಅದಕ್ಕೆ ಸಂಬಂಧಿಸಿದ ಮಾಹಿತಿಯನ್ನು ಮಾತ್ರ ನಮೂದಿಸಿ. ಫಾರ್ಮ್ ಸ್ವಯಂಚಾಲಿತವಾಗಿ ಹೊಂದಿಕೊಳ್ಳುತ್ತದೆ ಮತ್ತು ಖಾಲಿ ಮೌಲ್ಯಗಳನ್ನು ಶೂನ್ಯವೆಂದು ಪರಿಗಣಿಸಲಾಗುವುದಿಲ್ಲ.",
        "Choose the broad business domain first.":"ಮೊದಲು ವ್ಯಾಪಕ ವ್ಯವಹಾರ ಕ್ಷೇತ್ರವನ್ನು ಆಯ್ಕೆ ಮಾಡಿ.", "Choose the exact activity you want to evaluate.":"ನೀವು ಮೌಲ್ಯಮಾಪನ ಮಾಡಲು ಬಯಸುವ ನಿಖರ ಚಟುವಟಿಕೆಯನ್ನು ಆಯ್ಕೆ ಮಾಡಿ.",
        "Rule-based feasibility assessment":"ನಿಯಮಾಧಾರಿತ ಕಾರ್ಯಸಾಧ್ಯತಾ ಮೌಲ್ಯಮಾಪನ", "Financial figures are planning estimates, not guarantees. Validate local supplier quotes, buyer prices and current scheme rules before committing capital.":"ಹಣಕಾಸು ಅಂಕಿಅಂಶಗಳು ಯೋಜನಾ ಅಂದಾಜುಗಳು ಮಾತ್ರ, ಖಾತರಿಗಳಲ್ಲ. ಬಂಡವಾಳ ಹೂಡಿಕೆಗೂ ಮೊದಲು ಸ್ಥಳೀಯ ಪೂರೈಕೆದಾರರ ದರ, ಖರೀದಿದಾರರ ಬೆಲೆ ಮತ್ತು ಪ್ರಸ್ತುತ ಯೋಜನಾ ನಿಯಮಗಳನ್ನು ಪರಿಶೀಲಿಸಿ.",
        "Species / Variety / Product Selection":"ಜಾತಿ / ತಳಿ / ಉತ್ಪನ್ನ ಆಯ್ಕೆ", "Execution Roadmap":"ಕಾರ್ಯಗತಗೊಳಿಸುವಿಕೆ ಮಾರ್ಗಸೂಚಿ",
        "Prepare → pilot → validate → scale. Each phase has a clear translate_output_recursive(outcome) and a go/no-go translate_output_recursive(gate).":"ತಯಾರಿ → ಪೈಲಟ್ → ಪರಿಶೀಲನೆ → ವಿಸ್ತರಣೆ. ಪ್ರತಿ ಹಂತಕ್ಕೂ ಸ್ಪಷ್ಟ ಫಲಿತಾಂಶ ಮತ್ತು ಮುಂದುವರಿಯುವ ಮಾನದಂಡವಿದೆ.",
        "Scale rule":"ವಿಸ್ತರಣೆ ನಿಯಮ", "Practical Decision Check":"ಪ್ರಾಯೋಗಿಕ ನಿರ್ಧಾರ ಪರಿಶೀಲನೆ", "Financial & Success Benchmarks":"ಹಣಕಾಸು ಮತ್ತು ಯಶಸ್ಸಿನ ಮಾನದಂಡಗಳು",
        "Applicable scheme information is shown for the selected business mapping. Eligibility and support depend on current official guidelines.":"ಆಯ್ಕೆ ಮಾಡಿದ ವ್ಯವಹಾರ ಮ್ಯಾಪಿಂಗ್‌ಗೆ ಸಂಬಂಧಿಸಿದ ಯೋಜನಾ ಮಾಹಿತಿಯನ್ನು ತೋರಿಸಲಾಗಿದೆ. ಅರ್ಹತೆ ಮತ್ತು ನೆರವು ಪ್ರಸ್ತುತ ಅಧಿಕೃತ ಮಾರ್ಗಸೂಚಿಗಳ ಮೇಲೆ ಅವಲಂಬಿತವಾಗಿದೆ.",
        "No scheme is currently mapped to this business in the prototype. Use Government Schemes for broader discovery.":"ಈ ಪ್ರೋಟೋಟೈಪ್‌ನಲ್ಲಿ ಈ ವ್ಯವಹಾರಕ್ಕೆ ಯಾವುದೇ ಯೋಜನೆ ಮ್ಯಾಪ್ ಮಾಡಲಾಗಿಲ್ಲ. ಹೆಚ್ಚಿನ ಆಯ್ಕೆಗಳಿಗಾಗಿ ಸರ್ಕಾರಿ ಯೋಜನೆಗಳನ್ನು ನೋಡಿ.",
        "Generate Business Recommendations":"ವ್ಯವಹಾರ ಶಿಫಾರಸುಗಳನ್ನು ರಚಿಸಿ",
    }
}

for _lang in TEXT:
    TEXT[_lang].update(UI_TR.get(_lang, {}))

# ------------------------------------------------------------
# COMPLETE UI FALLBACK TRANSLATOR
# ------------------------------------------------------------
# Some business profiles contain labels/options/descriptions directly in
# the configuration.  The dictionaries above cover the main UI, but this
# fallback also translates those dynamic strings so changing the language
# affects the whole application, not only the navigation.
UI_WORD_TR = {
    "Hindi": {
        "Business Domain":"व्यवसाय क्षेत्र","Specific Business":"विशिष्ट व्यवसाय",
        "Current Location":"वर्तमान स्थान","Selected in the sidebar":"साइडबार में चुना गया",
        "Location & Climate Parameters":"स्थान और जलवायु पैरामीटर","Soil & Water Profile":"मिट्टी और पानी प्रोफ़ाइल",
        "Capital & Financial Goals":"पूंजी और वित्तीय लक्ष्य","Generate Recommendation":"सुझाव तैयार करें",
        "Business Recommendation":"व्यवसाय सुझाव","Select one business activity and enter only the inputs relevant to that activity. The form adapts automatically and missing values are not treated as zero.":"एक व्यवसाय गतिविधि चुनें और केवल उससे संबंधित जानकारी दर्ज करें। फॉर्म अपने आप अनुकूलित होता है और खाली मानों को शून्य नहीं माना जाता।",
        "Step 1 • Select Business":"चरण 1 • व्यवसाय चुनें","Step 2 • Enter Inputs":"चरण 2 • जानकारी दर्ज करें","Step 3 • Strategic Output":"चरण 3 • रणनीतिक परिणाम",
        "Step 1 • Business ✓":"चरण 1 • व्यवसाय ✓","Step 2 • Inputs ✓":"चरण 2 • जानकारी ✓",
        "Choose the broad business domain first.":"पहले व्यापक व्यवसाय क्षेत्र चुनें।","Choose the exact activity you want to evaluate.":"वह सटीक गतिविधि चुनें जिसका आकलन करना है।",
        "Use realistic conditions for the specific site and production period. Defaults are regional planning values and should be replaced with measured/current values where available.":"विशिष्ट स्थान और उत्पादन अवधि के लिए वास्तविक परिस्थितियाँ दर्ज करें। डिफ़ॉल्ट क्षेत्रीय योजना मान हैं; जहाँ उपलब्ध हों वहाँ मापे गए या वर्तमान मानों से बदलें।",
        "Use the latest soil/water information available. Tooltips explain what each field is used for.":"उपलब्ध नवीनतम मिट्टी/पानी की जानकारी का उपयोग करें। टूलटिप में बताया गया है कि प्रत्येक फ़ील्ड का उपयोग किसलिए है।",
        "Enter deployable capital, operating capacity and commercial constraints. Unknown or missing fields are excluded from adaptive scoring.":"उपलब्ध पूंजी, संचालन क्षमता और व्यावसायिक सीमाएँ दर्ज करें। अज्ञात या खाली फ़ील्ड अनुकूलित स्कोर में शामिल नहीं किए जाते।",
        "This activity does not require additional location/climate inputs beyond the selected location.":"इस गतिविधि के लिए चुने गए स्थान के अलावा अतिरिक्त स्थान/जलवायु जानकारी आवश्यक नहीं है।",
        "No separate soil/water profile is required for this activity.":"इस गतिविधि के लिए अलग मिट्टी/पानी प्रोफ़ाइल आवश्यक नहीं है।",
        "No additional financial/setup inputs are required for this activity.":"इस गतिविधि के लिए अतिरिक्त वित्तीय/सेटअप जानकारी आवश्यक नहीं है।",
        "Tip: use the latest available measurements and realistic capacity. The recommendation engine adapts to partial information.":"सुझाव: उपलब्ध नवीनतम माप और वास्तविक क्षमता का उपयोग करें। सुझाव इंजन अधूरी जानकारी के अनुसार अनुकूलित होता है।",
        "CAPEX Required":"आवश्यक CAPEX","Break-Even Timeline":"ब्रेक-ईवन समयसीमा","Feasibility Score":"व्यवहार्यता स्कोर","Monthly Operating Cost":"मासिक संचालन लागत",
        "Current input / configured estimate":"वर्तमान जानकारी / कॉन्फ़िगर किया गया अनुमान","Indicative model estimate":"संकेतात्मक मॉडल अनुमान","Adaptive score from available inputs":"उपलब्ध जानकारी से अनुकूलित स्कोर","Indicative, scale-dependent":"संकेतात्मक, पैमाने पर निर्भर",
        "Market & Advisory":"बाज़ार और मार्गदर्शन","Risk Control":"जोखिम नियंत्रण","Financial Benchmarks":"वित्तीय मानदंड",
        "Species / Variety / Product Selection":"प्रजाति / किस्म / उत्पाद चयन","Execution Roadmap":"कार्यान्वयन रोडमैप",
        "Financial figures are planning estimates, not guarantees. Validate local supplier quotes, buyer prices and current scheme rules before committing capital.":"वित्तीय आंकड़े केवल योजना अनुमान हैं, गारंटी नहीं। पूंजी लगाने से पहले स्थानीय आपूर्तिकर्ता दर, खरीदार कीमत और वर्तमान योजना नियमों की पुष्टि करें।",
        "Priority gaps":"प्राथमिकता अंतराल","Practical Decision Check":"व्यावहारिक निर्णय जाँच",
        "No scheme is currently mapped to this business in the prototype. Use Government Schemes for broader discovery.":"इस प्रोटोटाइप में इस व्यवसाय से कोई योजना मैप नहीं की गई है। अधिक योजनाओं के लिए सरकारी योजनाएँ देखें।",
        "Do not move straight from setup to full investment. Validate the pilot first.":"सेटअप से सीधे पूर्ण निवेश पर न जाएँ। पहले पायलट को सत्यापित करें।",
        "Selection":"चयन","Schemes":"योजनाएँ","Market":"बाज़ार","Advisory":"मार्गदर्शन",
        "Input":"इनपुट","Output":"परिणाम","Score":"स्कोर","Reason":"कारण","Action":"कार्रवाई",
        "No":"नहीं","Yes":"हाँ","Some":"कुछ","Intermediate":"मध्यम","Unknown":"अज्ञात",
        "Cows":"गाय","Buffaloes":"भैंस","Mixed":"मिश्रित","Existing pond":"मौजूदा तालाब","New pond":"नया तालाब","Lined pond":"लाइनिंग वाला तालाब",
        "Canal":"नहर","Borewell":"बोरवेल","Tank/Pond":"टैंक/तालाब","River":"नदी","Seasonal":"मौसमी","Perennial":"सालभर उपलब्ध",
        "Cereals":"अनाज","Pulses":"दलहन","Oilseeds":"तिलहन","Commercial Crops":"व्यावसायिक फसलें","Allied Activities":"संबंधित गतिविधियाँ",
        "Land":"भूमि","Water":"पानी","Soil":"मिट्टी","Market":"बाज़ार","Equipment":"उपकरण","Packaging":"पैकेजिंग",
        "Processing":"प्रसंस्करण","Storage":"भंडारण","Transport":"परिवहन","Workspace":"कार्यस्थल","Workshop":"कार्यशाला",
        "Demand":"मांग","Experience":"अनुभव","Labour":"श्रमिक","Capital":"पूंजी","Investment":"निवेश","Electricity":"बिजली",
        "Feed":"चारा","Fuel":"ईंधन","Vehicle":"वाहन","Operator":"ऑपरेटर","Driver":"चालक","Skill":"कौशल",
        "Temperature":"तापमान","Humidity":"आर्द्रता","Rainfall":"वर्षा","Irrigation":"सिंचाई","Season":"मौसम",
        "Poor":"कमज़ोर","Moderate":"मध्यम","Good":"अच्छा","Low":"कम","Medium":"मध्यम","High":"अधिक","Limited":"सीमित","Partial":"आंशिक","Available":"उपलब्ध","Reliable":"विश्वसनीय","Shared":"साझा",
        "Beginner":"शुरुआती","Some experience":"कुछ अनुभव","Experienced":"अनुभवी",
        "Within 3 months":"3 महीने के भीतर","3–6 months":"3–6 महीने","6–12 months":"6–12 महीने","12+ months":"12+ महीने",
        "Rain-fed":"वर्षा आधारित","None":"नहीं","Other":"अन्य","Two-wheeler":"दो पहिया वाहन","Auto/three-wheeler":"ऑटो/तीन पहिया वाहन","Pickup":"पिकअप","Mini truck":"मिनी ट्रक","Leased":"लीज़ पर",
        "Agriculture":"कृषि","Livestock":"पशुपालन","Aquaculture":"मत्स्य पालन","Food Processing":"खाद्य प्रसंस्करण","Services":"सेवाएँ","Retail":"खुदरा",
        "Crop Cultivation":"फसल खेती","Vegetable Cultivation":"सब्ज़ी खेती","Fruit Cultivation":"फल खेती","Spice Cultivation":"मसाला खेती","Floriculture":"फूलों की खेती",
        "Poultry Farming":"पोल्ट्री फार्मिंग","Dairy Farming":"डेयरी फार्मिंग","Goat Farming":"बकरी पालन","Sheep Farming":"भेड़ पालन","Fish Farming":"मछली पालन",
    },
    "Kannada": {
        "Business Domain":"ವ್ಯವಹಾರ ಕ್ಷೇತ್ರ","Specific Business":"ನಿರ್ದಿಷ್ಟ ವ್ಯವಹಾರ","Current Location":"ಪ್ರಸ್ತುತ ಸ್ಥಳ","Selected in the sidebar":"ಸೈಡ್‌ಬಾರ್‌ನಲ್ಲಿ ಆಯ್ಕೆ ಮಾಡಲಾಗಿದೆ",
        "Location & Climate Parameters":"ಸ್ಥಳ ಮತ್ತು ಹವಾಮಾನ ನಿಯತಾಂಕಗಳು","Soil & Water Profile":"ಮಣ್ಣು ಮತ್ತು ನೀರಿನ ಪ್ರೊಫೈಲ್","Capital & Financial Goals":"ಬಂಡವಾಳ ಮತ್ತು ಹಣಕಾಸಿನ ಗುರಿಗಳು","Generate Recommendation":"ಶಿಫಾರಸು ರಚಿಸಿ",
        "Business Recommendation":"ವ್ಯವಹಾರ ಶಿಫಾರಸು","Step 1 • Select Business":"ಹಂತ 1 • ವ್ಯವಹಾರ ಆಯ್ಕೆ","Step 2 • Enter Inputs":"ಹಂತ 2 • ಮಾಹಿತಿ ನಮೂದಿಸಿ","Step 3 • Strategic Output":"ಹಂತ 3 • ತಂತ್ರಾತ್ಮಕ ಫಲಿತಾಂಶ",
        "Step 1 • Business ✓":"ಹಂತ 1 • ವ್ಯವಹಾರ ✓","Step 2 • Inputs ✓":"ಹಂತ 2 • ಮಾಹಿತಿ ✓",
        "Choose the broad business domain first.":"ಮೊದಲು ವ್ಯಾಪಕ ವ್ಯವಹಾರ ಕ್ಷೇತ್ರವನ್ನು ಆಯ್ಕೆಮಾಡಿ.","Choose the exact activity you want to evaluate.":"ಮೌಲ್ಯಮಾಪನ ಮಾಡಲು ಬಯಸುವ ನಿಖರ ಚಟುವಟಿಕೆಯನ್ನು ಆಯ್ಕೆಮಾಡಿ.",
        "Use realistic conditions for the specific site and production period. Defaults are regional planning values and should be replaced with measured/current values where available.":"ನಿರ್ದಿಷ್ಟ ಸ್ಥಳ ಮತ್ತು ಉತ್ಪಾದನಾ ಅವಧಿಗೆ ವಾಸ್ತವಿಕ ಪರಿಸ್ಥಿತಿಗಳನ್ನು ನಮೂದಿಸಿ. ಡೀಫಾಲ್ಟ್‌ಗಳು ಪ್ರಾದೇಶಿಕ ಯೋಜನಾ ಮೌಲ್ಯಗಳಾಗಿವೆ; ಲಭ್ಯವಿದ್ದಲ್ಲಿ ಪ್ರಸ್ತುತ/ಅಳತೆ ಮಾಡಿದ ಮೌಲ್ಯಗಳಿಂದ ಬದಲಿಸಿ.",
        "Use the latest soil/water information available. Tooltips explain what each field is used for.":"ಲಭ್ಯವಿರುವ ಇತ್ತೀಚಿನ ಮಣ್ಣು/ನೀರಿನ ಮಾಹಿತಿಯನ್ನು ಬಳಸಿ. ಪ್ರತಿಯೊಂದು ಕ್ಷೇತ್ರದ ಬಳಕೆಯನ್ನು ಟೂಲ್‌ಟಿಪ್ ವಿವರಿಸುತ್ತದೆ.",
        "Enter deployable capital, operating capacity and commercial constraints. Unknown or missing fields are excluded from adaptive scoring.":"ಬಳಸಬಹುದಾದ ಬಂಡವಾಳ, ಕಾರ್ಯಾಚರಣಾ ಸಾಮರ್ಥ್ಯ ಮತ್ತು ವಾಣಿಜ್ಯ ಮಿತಿಗಳನ್ನು ನಮೂದಿಸಿ. ತಿಳಿಯದ ಅಥವಾ ಖಾಲಿ ಕ್ಷೇತ್ರಗಳನ್ನು ಹೊಂದಿಕೊಳ್ಳುವ ಅಂಕದಲ್ಲಿ ಸೇರಿಸಲಾಗುವುದಿಲ್ಲ.",
        "This activity does not require additional location/climate inputs beyond the selected location.":"ಆಯ್ಕೆ ಮಾಡಿದ ಸ್ಥಳದ ಹೊರತಾಗಿ ಈ ಚಟುವಟಿಕೆಗೆ ಹೆಚ್ಚುವರಿ ಸ್ಥಳ/ಹವಾಮಾನ ಮಾಹಿತಿ ಅಗತ್ಯವಿಲ್ಲ.",
        "No separate soil/water profile is required for this activity.":"ಈ ಚಟುವಟಿಕೆಗೆ ಪ್ರತ್ಯೇಕ ಮಣ್ಣು/ನೀರಿನ ಪ್ರೊಫೈಲ್ ಅಗತ್ಯವಿಲ್ಲ.",
        "No additional financial/setup inputs are required for this activity.":"ಈ ಚಟುವಟಿಕೆಗೆ ಹೆಚ್ಚುವರಿ ಹಣಕಾಸು/ಸೆಟಪ್ ಮಾಹಿತಿ ಅಗತ್ಯವಿಲ್ಲ.",
        "Tip: use the latest available measurements and realistic capacity. The recommendation engine adapts to partial information.":"ಸಲಹೆ: ಲಭ್ಯವಿರುವ ಇತ್ತೀಚಿನ ಅಳತೆಗಳು ಮತ್ತು ವಾಸ್ತವಿಕ ಸಾಮರ್ಥ್ಯವನ್ನು ಬಳಸಿ. ಶಿಫಾರಸು ಎಂಜಿನ್ ಅಪೂರ್ಣ ಮಾಹಿತಿಗೆ ಹೊಂದಿಕೊಳ್ಳುತ್ತದೆ.",
        "CAPEX Required":"ಅಗತ್ಯ CAPEX","Break-Even Timeline":"ಬ್ರೇಕ್-ಈವನ್ ಸಮಯಪಟ್ಟಿ","Feasibility Score":"ಕಾರ್ಯಸಾಧ್ಯತಾ ಅಂಕ","Monthly Operating Cost":"ಮಾಸಿಕ ಕಾರ್ಯಾಚರಣಾ ವೆಚ್ಚ",
        "Current input / configured estimate":"ಪ್ರಸ್ತುತ ಮಾಹಿತಿ / ಕಾನ್ಫಿಗರ್ ಮಾಡಿದ ಅಂದಾಜು","Indicative model estimate":"ಸೂಚಕ ಮಾದರಿ ಅಂದಾಜು","Adaptive score from available inputs":"ಲಭ್ಯ ಮಾಹಿತಿಯಿಂದ ಹೊಂದಿಕೊಳ್ಳುವ ಅಂಕ","Indicative, scale-dependent":"ಸೂಚಕ, ಪ್ರಮಾಣದ ಮೇಲೆ ಅವಲಂಬಿತ",
        "Market & Advisory":"ಮಾರುಕಟ್ಟೆ ಮತ್ತು ಮಾರ್ಗದರ್ಶನ","Risk Control":"ಅಪಾಯ ನಿಯಂತ್ರಣ","Financial Benchmarks":"ಹಣಕಾಸು ಮಾನದಂಡಗಳು",
        "Species / Variety / Product Selection":"ಜಾತಿ / ತಳಿ / ಉತ್ಪನ್ನ ಆಯ್ಕೆ","Execution Roadmap":"ಕಾರ್ಯಗತಗೊಳಿಸುವಿಕೆ ಮಾರ್ಗಸೂಚಿ",
        "Selection":"ಆಯ್ಕೆ","Schemes":"ಯೋಜನೆಗಳು","Market":"ಮಾರುಕಟ್ಟೆ","Advisory":"ಮಾರ್ಗದರ್ಶನ","Input":"ಇನ್‌ಪುಟ್","Output":"ಫಲಿತಾಂಶ","Score":"ಅಂಕ","Reason":"ಕಾರಣ","Action":"ಕ್ರಮ",
        "No":"ಇಲ್ಲ","Yes":"ಹೌದು","Some":"ಕೆಲವು","Intermediate":"ಮಧ್ಯಮ","Unknown":"ತಿಳಿದಿಲ್ಲ",
        "Cows":"ಹಸುಗಳು","Buffaloes":"ಎಮ್ಮೆಗಳು","Mixed":"ಮಿಶ್ರ","Existing pond":"ಅಸ್ತಿತ್ವದಲ್ಲಿರುವ ಕೆರೆ","New pond":"ಹೊಸ ಕೆರೆ","Lined pond":"ಲೈನಿಂಗ್ ಮಾಡಿದ ಕೆರೆ",
        "Canal":"ಕಾಲುವೆ","Borewell":"ಬೋರ್‌ವೆಲ್","Tank/Pond":"ಟ್ಯಾಂಕ್/ಕೆರೆ","River":"ನದಿ","Seasonal":"ಋತುಮಾನ","Perennial":"ವರ್ಷಪೂರ್ತಿ",
        "Cereals":"ಧಾನ್ಯಗಳು","Pulses":"ಬೇಳೆಕಾಳುಗಳು","Oilseeds":"ಎಣ್ಣೆಬೀಜಗಳು","Commercial Crops":"ವಾಣಿಜ್ಯ ಬೆಳೆಗಳು","Allied Activities":"ಸಂಬಂಧಿತ ಚಟುವಟಿಕೆಗಳು",
        "Land":"ಭೂಮಿ","Water":"ನೀರು","Soil":"ಮಣ್ಣು","Equipment":"ಉಪಕರಣ","Packaging":"ಪ್ಯಾಕೇಜಿಂಗ್","Processing":"ಸಂಸ್ಕರಣೆ","Storage":"ಸಂಗ್ರಹಣೆ","Transport":"ಸಾರಿಗೆ","Workspace":"ಕಾರ್ಯಸ್ಥಳ","Workshop":"ಕಾರ್ಯಾಗಾರ",
        "Demand":"ಬೇಡಿಕೆ","Experience":"ಅನುಭವ","Labour":"ಕಾರ್ಮಿಕರು","Capital":"ಬಂಡವಾಳ","Investment":"ಹೂಡಿಕೆ","Electricity":"ವಿದ್ಯುತ್","Feed":"ಮೇವು","Fuel":"ಇಂಧನ","Vehicle":"ವಾಹನ","Operator":"ಆಪರೇಟರ್","Driver":"ಚಾಲಕ","Skill":"ಕೌಶಲ್ಯ",
        "Temperature":"ತಾಪಮಾನ","Humidity":"ಆರ್ದ್ರತೆ","Rainfall":"ಮಳೆ","Irrigation":"ನೀರಾವರಿ","Season":"ಋತು",
        "Poor":"ಕಡಿಮೆ","Moderate":"ಮಧ್ಯಮ","Good":"ಉತ್ತಮ","Low":"ಕಡಿಮೆ","Medium":"ಮಧ್ಯಮ","High":"ಹೆಚ್ಚು","Limited":"ಸೀಮಿತ","Partial":"ಭಾಗಶಃ","Available":"ಲಭ್ಯ","Reliable":"ವಿಶ್ವಾಸಾರ್ಹ","Shared":"ಹಂಚಿಕೆ",
        "Beginner":"ಆರಂಭಿಕ","Some experience":"ಸ್ವಲ್ಪ ಅನುಭವ","Experienced":"ಅನುಭವ ಹೊಂದಿರುವವರು",
        "Within 3 months":"3 ತಿಂಗಳೊಳಗೆ","3–6 months":"3–6 ತಿಂಗಳು","6–12 months":"6–12 ತಿಂಗಳು","12+ months":"12+ ತಿಂಗಳು",
        "Rain-fed":"ಮಳೆ ಆಧಾರಿತ","None":"ಇಲ್ಲ","Other":"ಇತರೆ","Two-wheeler":"ದ್ವಿಚಕ್ರ ವಾಹನ","Auto/three-wheeler":"ಆಟೋ/ಮೂರು ಚಕ್ರ ವಾಹನ","Pickup":"ಪಿಕಪ್","Mini truck":"ಮಿನಿ ಟ್ರಕ್","Leased":"ಲೀಸ್‌ಗೆ",
        "Agriculture":"ಕೃಷಿ","Livestock":"ಪಶುಸಂಗೋಪನೆ","Aquaculture":"ಮೀನುಗಾರಿಕೆ","Food Processing":"ಆಹಾರ ಸಂಸ್ಕರಣೆ","Services":"ಸೇವೆಗಳು","Retail":"ಚಿಲ್ಲರೆ",
        "Crop Cultivation":"ಬೆಳೆ ಕೃಷಿ","Vegetable Cultivation":"ತರಕಾರಿ ಕೃಷಿ","Fruit Cultivation":"ಹಣ್ಣು ಕೃಷಿ","Spice Cultivation":"ಮಸಾಲೆ ಕೃಷಿ","Floriculture":"ಹೂ ಬೆಳೆ",
        "Poultry Farming":"ಕೋಳಿ ಸಾಕಣೆ","Dairy Farming":"ಹೈನುಗಾರಿಕೆ","Goat Farming":"ಮೇಕೆ ಸಾಕಣೆ","Sheep Farming":"ಕುರಿ ಸಾಕಣೆ","Fish Farming":"ಮೀನು ಸಾಕಣೆ",
    }
}


# Agriculture/environment field translations (including NPK inputs and helper text).
ENV_UI_TR = {
    "Hindi": {
        "Nitrogen (N)":"नाइट्रोजन (N)", "Phosphorus (P)":"फॉस्फोरस (P)", "Potassium (K)":"पोटैशियम (K)",
        "Temperature (°C)":"तापमान (°C)", "Humidity (%)":"आर्द्रता (%)", "Soil pH":"मिट्टी का pH", "Rainfall (mm)":"वर्षा (मिमी)",
        "Nitrogen":"नाइट्रोजन", "Phosphorus":"फॉस्फोरस", "Potassium":"पोटैशियम",
        "Soil pH":"मिट्टी का pH", "Water availability":"पानी की उपलब्धता", "Market access":"बाज़ार तक पहुँच",
        "Feed availability":"चारे की उपलब्धता", "Fodder availability":"पशु चारे की उपलब्धता", "Veterinary access":"पशु चिकित्सा सुविधा",
        "Housing/shed":"आवास/शेड", "Grazing/feed availability":"चराई/चारे की उपलब्धता", "Electricity":"बिजली",
        "Use the latest soil-test N value; this helps compare crop requirements.":"मिट्टी की नवीनतम जाँच में दिया गया N मान दर्ज करें; इससे फसल की आवश्यकता की तुलना करने में मदद मिलती है।",
        "Use the latest soil-test P value.":"मिट्टी की नवीनतम जाँच में दिया गया P मान दर्ज करें।",
        "Use the latest soil-test K value.":"मिट्टी की नवीनतम जाँच में दिया गया K मान दर्ज करें।",
        "Use the latest soil-test pH; most crops have a preferred pH band.":"मिट्टी की नवीनतम जाँच का pH मान दर्ज करें; अधिकांश फसलों के लिए एक उपयुक्त pH सीमा होती है।",
        "Enter the expected temperature during the production period.":"उत्पादन अवधि के दौरान अपेक्षित तापमान दर्ज करें।",
        "Enter typical relative humidity for the production area.":"उत्पादन क्षेत्र की सामान्य सापेक्ष आर्द्रता दर्ज करें।",
        "Enter expected seasonal rainfall or the relevant production-period value.":"अपेक्षित मौसमी वर्षा या उत्पादन अवधि का संबंधित मान दर्ज करें।",
        "Enter a practical value":"व्यावहारिक मान दर्ज करें",
    },
    "Kannada": {
        "Nitrogen (N)":"ನೈಟ್ರೋಜನ್ (N)", "Phosphorus (P)":"ಫಾಸ್ಫರಸ್ (P)", "Potassium (K)":"ಪೊಟ್ಯಾಸಿಯಮ್ (K)",
        "Temperature (°C)":"ತಾಪಮಾನ (°C)", "Humidity (%)":"ಆರ್ದ್ರತೆ (%)", "Soil pH":"ಮಣ್ಣಿನ pH", "Rainfall (mm)":"ಮಳೆ (ಮಿಮೀ)",
        "Nitrogen":"ನೈಟ್ರೋಜನ್", "Phosphorus":"ಫಾಸ್ಫರಸ್", "Potassium":"ಪೊಟ್ಯಾಸಿಯಮ್",
        "Water availability":"ನೀರಿನ ಲಭ್ಯತೆ", "Market access":"ಮಾರುಕಟ್ಟೆ ಪ್ರವೇಶ", "Feed availability":"ಮೇವು ಲಭ್ಯತೆ",
        "Fodder availability":"ಪಶು ಮೇವು ಲಭ್ಯತೆ", "Veterinary access":"ಪಶುವೈದ್ಯಕೀಯ ಸೌಲಭ್ಯ", "Housing/shed":"ವಸತಿ/ಶೆಡ್",
        "Grazing/feed availability":"ಮೇಯಿಸುವಿಕೆ/ಮೇವು ಲಭ್ಯತೆ", "Electricity":"ವಿದ್ಯುತ್",
        "Use the latest soil-test N value; this helps compare crop requirements.":"ಇತ್ತೀಚಿನ ಮಣ್ಣಿನ ಪರೀಕ್ಷೆಯ N ಮೌಲ್ಯವನ್ನು ನಮೂದಿಸಿ; ಇದು ಬೆಳೆ ಅಗತ್ಯಗಳನ್ನು ಹೋಲಿಸಲು ಸಹಾಯ ಮಾಡುತ್ತದೆ.",
        "Use the latest soil-test P value.":"ಇತ್ತೀಚಿನ ಮಣ್ಣಿನ ಪರೀಕ್ಷೆಯ P ಮೌಲ್ಯವನ್ನು ನಮೂದಿಸಿ.",
        "Use the latest soil-test K value.":"ಇತ್ತೀಚಿನ ಮಣ್ಣಿನ ಪರೀಕ್ಷೆಯ K ಮೌಲ್ಯವನ್ನು ನಮೂದಿಸಿ.",
        "Use the latest soil-test pH; most crops have a preferred pH band.":"ಇತ್ತೀಚಿನ ಮಣ್ಣಿನ ಪರೀಕ್ಷೆಯ pH ಮೌಲ್ಯವನ್ನು ನಮೂದಿಸಿ; ಹೆಚ್ಚಿನ ಬೆಳೆಗಳಿಗೆ ಸೂಕ್ತ pH ಮಿತಿ ಇರುತ್ತದೆ.",
        "Enter the expected temperature during the production period.":"ಉತ್ಪಾದನಾ ಅವಧಿಯಲ್ಲಿ ನಿರೀಕ್ಷಿತ ತಾಪಮಾನವನ್ನು ನಮೂದಿಸಿ.",
        "Enter typical relative humidity for the production area.":"ಉತ್ಪಾದನಾ ಪ್ರದೇಶದ ಸಾಮಾನ್ಯ ಸಾಪೇಕ್ಷ ಆರ್ದ್ರತೆಯನ್ನು ನಮೂದಿಸಿ.",
        "Enter expected seasonal rainfall or the relevant production-period value.":"ನಿರೀಕ್ಷಿತ ಋತುಮಾನದ ಮಳೆ ಅಥವಾ ಉತ್ಪಾದನಾ ಅವಧಿಯ ಸಂಬಂಧಿತ ಮೌಲ್ಯವನ್ನು ನಮೂದಿಸಿ.",
        "Enter a practical value":"ಪ್ರಾಯೋಗಿಕ ಮೌಲ್ಯವನ್ನು ನಮೂದಿಸಿ",
    }
}


OUTPUT_TR = {'Hindi': {'Rule-based feasibility assessment': 'नियम-आधारित व्यवहार्यता मूल्यांकन', 'High Risk': 'उच्च जोखिम', 'Medium Risk': 'मध्यम जोखिम', 'Low Risk': 'कम जोखिम', 'Risk': 'जोखिम', 'Level': 'स्तर', 'Impact': 'प्रभाव', 'Control / mitigation': 'नियंत्रण / जोखिम कम करने का उपाय', 'Category': 'श्रेणी', 'Option': 'विकल्प', 'Cycle': 'चक्र', 'Soil / space': 'मिट्टी / स्थान', 'Water': 'पानी', 'Indicative production': 'अनुमानित उत्पादन', 'Specific option': 'विशिष्ट विकल्प', 'Production cycle': 'उत्पादन चक्र', 'Space requirement': 'स्थान की आवश्यकता', 'Climate compatibility': 'जलवायु अनुकूलता', 'Target market': 'लक्षित बाज़ार', 'Execution Roadmap': 'कार्यान्वयन रोडमैप', 'Foundation & Setup': 'आधार और स्थापना', 'READY THE BUSINESS': 'व्यवसाय को तैयार करें', 'Procure & Pilot': 'खरीद और पायलट', 'TEST BEFORE SCALE': 'विस्तार से पहले परीक्षण करें', 'Production, Market & Scale': 'उत्पादन, बाज़ार और विस्तार', 'TURN THE PILOT INTO A BUSINESS': 'पायलट को व्यवसाय में बदलें', 'Outcome:': 'परिणाम:', 'Scale rule': 'विस्तार नियम', 'Route': 'मार्ग', 'Practical use': 'व्यावहारिक उपयोग', 'Pricing focus': 'मूल्य निर्धारण पर ध्यान', 'Differentiation': 'विशेषता', 'Priority gaps': 'प्राथमिक कमियाँ', 'Gap': 'कमी', 'Action': 'कार्रवाई', 'Financial Benchmarks': 'वित्तीय मानदंड', 'Benchmark': 'मानदंड', 'Indicative value': 'अनुमानित मूल्य', 'Interpretation': 'व्याख्या', 'Minimum configured investment': 'न्यूनतम निर्धारित निवेश', 'Planned investment': 'नियोजित निवेश', 'Monthly operating cost': 'मासिक संचालन लागत', 'Annual benefit': 'वार्षिक लाभ', 'Break-even': 'ब्रेक-ईवन', 'Feasibility indicator': 'व्यवहार्यता संकेतक', 'Value': 'मूल्य', 'Note': 'टिप्पणी', 'Scheme': 'योजना', 'What it supports': 'यह किसका समर्थन करती है', 'Financial assistance': 'वित्तीय सहायता', 'Eligibility': 'पात्रता', 'Key documents / conditions': 'मुख्य दस्तावेज़ / शर्तें', 'Practical Decision Check': 'व्यावहारिक निर्णय जाँच', 'Not estimated': 'अनुमान उपलब्ध नहीं', 'Not provided': 'प्रदान नहीं किया गया', 'Not available': 'उपलब्ध नहीं', 'Indicative; verify locally': 'अनुमानित; स्थानीय रूप से सत्यापित करें', 'Current input / configured estimate': 'वर्तमान इनपुट / निर्धारित अनुमान', 'Indicative model estimate': 'अनुमानित मॉडल मूल्य', 'Adaptive score from available inputs': 'उपलब्ध इनपुट से अनुकूलित स्कोर', 'Indicative, scale-dependent': 'अनुमानित, पैमाने पर निर्भर', 'identified': 'पहचाना गया', 'item(s)': 'आइटम', 'Selection': 'चयन', 'Market & Advisory': 'बाज़ार और सलाह', 'Risk Control': 'जोखिम नियंत्रण', 'Schemes': 'योजनाएँ'}, 'Kannada': {'Rule-based feasibility assessment': 'ನಿಯಮ-ಆಧಾರಿತ ಕಾರ್ಯಸಾಧ್ಯತೆ ಮೌಲ್ಯಮಾಪನ', 'High Risk': 'ಹೆಚ್ಚಿನ ಅಪಾಯ', 'Medium Risk': 'ಮಧ್ಯಮ ಅಪಾಯ', 'Low Risk': 'ಕಡಿಮೆ ಅಪಾಯ', 'Risk': 'ಅಪಾಯ', 'Level': 'ಮಟ್ಟ', 'Impact': 'ಪರಿಣಾಮ', 'Control / mitigation': 'ನಿಯಂತ್ರಣ / ಅಪಾಯ ಕಡಿತ ಕ್ರಮ', 'Category': 'ವರ್ಗ', 'Option': 'ಆಯ್ಕೆ', 'Cycle': 'ಚಕ್ರ', 'Soil / space': 'ಮಣ್ಣು / ಸ್ಥಳ', 'Water': 'ನೀರು', 'Indicative production': 'ಅಂದಾಜು ಉತ್ಪಾದನೆ', 'Specific option': 'ನಿರ್ದಿಷ್ಟ ಆಯ್ಕೆ', 'Production cycle': 'ಉತ್ಪಾದನಾ ಚಕ್ರ', 'Space requirement': 'ಸ್ಥಳದ ಅವಶ್ಯಕತೆ', 'Climate compatibility': 'ಹವಾಮಾನ ಹೊಂದಾಣಿಕೆ', 'Target market': 'ಗುರಿ ಮಾರುಕಟ್ಟೆ', 'Execution Roadmap': 'ಕಾರ್ಯಗತಗೊಳಿಸುವ ಮಾರ್ಗಸೂಚಿ', 'Foundation & Setup': 'ಅಡಿಪಾಯ ಮತ್ತು ಸ್ಥಾಪನೆ', 'READY THE BUSINESS': 'ವ್ಯವಹಾರವನ್ನು ಸಿದ್ಧಪಡಿಸಿ', 'Procure & Pilot': 'ಖರೀದಿ ಮತ್ತು ಪೈಲಟ್', 'TEST BEFORE SCALE': 'ವಿಸ್ತರಿಸುವ ಮೊದಲು ಪರೀಕ್ಷಿಸಿ', 'Production, Market & Scale': 'ಉತ್ಪಾದನೆ, ಮಾರುಕಟ್ಟೆ ಮತ್ತು ವಿಸ್ತರಣೆ', 'TURN THE PILOT INTO A BUSINESS': 'ಪೈಲಟ್ ಅನ್ನು ವ್ಯವಹಾರವಾಗಿ ರೂಪಿಸಿ', 'Outcome:': 'ಫಲಿತಾಂಶ:', 'Scale rule': 'ವಿಸ್ತರಣೆ ನಿಯಮ', 'Route': 'ಮಾರ್ಗ', 'Practical use': 'ಪ್ರಾಯೋಗಿಕ ಬಳಕೆ', 'Pricing focus': 'ಬೆಲೆ ನಿಗದಿ ಗಮನ', 'Differentiation': 'ವಿಶಿಷ್ಟತೆ', 'Priority gaps': 'ಪ್ರಮುಖ ಕೊರತೆಗಳು', 'Gap': 'ಕೊರತೆ', 'Action': 'ಕ್ರಮ', 'Financial Benchmarks': 'ಹಣಕಾಸು ಮಾನದಂಡಗಳು', 'Benchmark': 'ಮಾನದಂಡ', 'Indicative value': 'ಅಂದಾಜು ಮೌಲ್ಯ', 'Interpretation': 'ವಿವರಣೆ', 'Minimum configured investment': 'ಕನಿಷ್ಠ ನಿಗದಿತ ಹೂಡಿಕೆ', 'Planned investment': 'ಯೋಜಿತ ಹೂಡಿಕೆ', 'Monthly operating cost': 'ಮಾಸಿಕ ಕಾರ್ಯಾಚರಣಾ ವೆಚ್ಚ', 'Annual benefit': 'ವಾರ್ಷಿಕ ಲಾಭ', 'Break-even': 'ಬ್ರೇಕ್-ಈವನ್', 'Feasibility indicator': 'ಕಾರ್ಯಸಾಧ್ಯತೆ ಸೂಚಕ', 'Value': 'ಮೌಲ್ಯ', 'Note': 'ಟಿಪ್ಪಣಿ', 'Scheme': 'ಯೋಜನೆ', 'What it supports': 'ಇದು ಯಾವುದಕ್ಕೆ ಬೆಂಬಲ ನೀಡುತ್ತದೆ', 'Financial assistance': 'ಹಣಕಾಸು ಸಹಾಯ', 'Eligibility': 'ಅರ್ಹತೆ', 'Key documents / conditions': 'ಮುಖ್ಯ ದಾಖಲೆಗಳು / ಷರತ್ತುಗಳು', 'Practical Decision Check': 'ಪ್ರಾಯೋಗಿಕ ನಿರ್ಧಾರ ಪರಿಶೀಲನೆ', 'Not estimated': 'ಅಂದಾಜು ಲಭ್ಯವಿಲ್ಲ', 'Not provided': 'ನೀಡಲಾಗಿಲ್ಲ', 'Not available': 'ಲಭ್ಯವಿಲ್ಲ', 'Indicative; verify locally': 'ಅಂದಾಜು; ಸ್ಥಳೀಯವಾಗಿ ಪರಿಶೀಲಿಸಿ', 'Current input / configured estimate': 'ಪ್ರಸ್ತುತ ಇನ್\u200cಪುಟ್ / ನಿಗದಿತ ಅಂದಾಜು', 'Indicative model estimate': 'ಅಂದಾಜು ಮಾದರಿ ಮೌಲ್ಯ', 'Adaptive score from available inputs': 'ಲಭ್ಯವಿರುವ ಇನ್\u200cಪುಟ್\u200cಗಳಿಂದ ಹೊಂದಿಕೊಳ್ಳುವ ಸ್ಕೋರ್', 'Indicative, scale-dependent': 'ಅಂದಾಜು, ಪ್ರಮಾಣದ ಮೇಲೆ ಅವಲಂಬಿತ', 'identified': 'ಗುರುತಿಸಲಾಗಿದೆ', 'item(s)': 'ಅಂಶ', 'Selection': 'ಆಯ್ಕೆ', 'Market & Advisory': 'ಮಾರುಕಟ್ಟೆ ಮತ್ತು ಸಲಹೆ', 'Risk Control': 'ಅಪಾಯ ನಿಯಂತ್ರಣ', 'Schemes': 'ಯೋಜನೆಗಳು'}}


# Complete Business Recommendation roadmap translations.
OUTPUT_TR.setdefault("Hindi", {}).update({
    "Make the site, resources, budget and compliance setup ready.": "स्थान, संसाधन, बजट और अनुपालन की तैयारी पूरी करें।",
    "Confirm land / workspace, water and access conditions.": "भूमि / कार्यस्थल, पानी और पहुंच की स्थिति की पुष्टि करें।",
    "Prepare a minimum investment plan and cash buffer.": "न्यूनतम निवेश योजना और नकद रिज़र्व तैयार करें।",
    "Complete required permits, registrations, testing or local checks.": "आवश्यक परमिट, पंजीकरण, परीक्षण या स्थानीय जांच पूरी करें।",
    "Site + resources + budget confirmed": "स्थान + संसाधन + बजट की पुष्टि",
    "Run a controlled pilot using the selected option and record real costs.": "चयनित विकल्प का नियंत्रित पायलट चलाएं और वास्तविक लागत दर्ज करें।",
    "Procure quality inputs / stock / equipment from traceable suppliers.": "विश्वसनीय और सत्यापित आपूर्तिकर्ताओं से गुणवत्तापूर्ण इनपुट / स्टॉक / उपकरण खरीदें।",
    "Start with a manageable pilot size and track labour, water and input use.": "प्रबंधनीय पायलट आकार से शुरुआत करें और श्रम, पानी तथा इनपुट के उपयोग को दर्ज करें।",
    "Record production, quality, demand and actual spending.": "उत्पादन, गुणवत्ता, मांग और वास्तविक खर्च दर्ज करें।",
    "Pilot data meets the planned operating thresholds": "पायलट डेटा नियोजित संचालन सीमाओं को पूरा करता है",
    "Move into repeat production, secure buyers and scale only where unit economics work.": "दोहराए जाने वाले उत्पादन में जाएं, खरीदार सुनिश्चित करें और केवल वहां विस्तार करें जहां प्रति-इकाई अर्थशास्त्र व्यवहार्य हो।",
    "Lock B2B + D2C sales channels and define pricing / pack strategy.": "B2B + D2C बिक्री चैनल तय करें और मूल्य निर्धारण / पैक रणनीति निर्धारित करें।",
    "Schedule production, grading, storage and transport.": "उत्पादन, ग्रेडिंग, भंडारण और परिवहन का समय निर्धारित करें।",
    "Review monthly cash flow and expand capacity in controlled steps.": "मासिक नकदी प्रवाह की समीक्षा करें और नियंत्रित चरणों में क्षमता बढ़ाएं।",
    "Repeat demand + workable unit economics + operational control": "दोहराई जाने वाली मांग + व्यवहार्य प्रति-इकाई अर्थशास्त्र + संचालन नियंत्रण",
    "Do not move straight from setup to full investment. Validate the pilot, actual operating cost and buyer response first.": "स्थापना से सीधे पूर्ण निवेश पर न जाएं। पहले पायलट, वास्तविक संचालन लागत और खरीदारों की प्रतिक्रिया को सत्यापित करें।",
    "Weeks 1–2": "सप्ताह 1–2",
    "Weeks 3–8": "सप्ताह 3–8",
    "After pilot validation": "पायलट सत्यापन के बाद",
    "Foundation & Setup": "अडिपाय और स्थापना",
    "Procure & Pilot": "खरीद और पायलट",
    "Production, Market & Scale": "उत्पादन, बाजार और विस्तार",
    "READY THE BUSINESS": "व्यवसाय को तैयार करें",
    "TEST BEFORE SCALE": "विस्तार से पहले परीक्षण करें",
    "TURN THE PILOT INTO A BUSINESS": "पायलट को व्यवसाय में बदलें",
})
OUTPUT_TR.setdefault("Kannada", {}).update({
    "Make the site, resources, budget and compliance setup ready.": "ಸ್ಥಳ, ಸಂಪನ್ಮೂಲಗಳು, ಬಜೆಟ್ ಮತ್ತು ಅನುಸರಣೆ ಸಿದ್ಧತೆಯನ್ನು ಪೂರ್ಣಗೊಳಿಸಿ.",
    "Confirm land / workspace, water and access conditions.": "ಭೂಮಿ / ಕೆಲಸದ ಸ್ಥಳ, ನೀರು ಮತ್ತು ಪ್ರವೇಶದ ಪರಿಸ್ಥಿತಿಗಳನ್ನು ಖಚಿತಪಡಿಸಿ.",
    "Prepare a minimum investment plan and cash buffer.": "ಕನಿಷ್ಠ ಹೂಡಿಕೆ ಯೋಜನೆ ಮತ್ತು ನಗದು ಮೀಸಲು ಸಿದ್ಧಪಡಿಸಿ.",
    "Complete required permits, registrations, testing or local checks.": "ಅಗತ್ಯ ಪರವಾನಗಿಗಳು, ನೋಂದಣಿಗಳು, ಪರೀಕ್ಷೆಗಳು ಅಥವಾ ಸ್ಥಳೀಯ ಪರಿಶೀಲನೆಗಳನ್ನು ಪೂರ್ಣಗೊಳಿಸಿ.",
    "Site + resources + budget confirmed": "ಸ್ಥಳ + ಸಂಪನ್ಮೂಲಗಳು + ಬಜೆಟ್ ದೃಢೀಕರಿಸಲಾಗಿದೆ",
    "Run a controlled pilot using the selected option and record real costs.": "ಆಯ್ಕೆ ಮಾಡಿದ ಆಯ್ಕೆಯನ್ನು ಬಳಸಿ ನಿಯಂತ್ರಿತ ಪೈಲಟ್ ನಡೆಸಿ ಮತ್ತು ನಿಜವಾದ ವೆಚ್ಚಗಳನ್ನು ದಾಖಲಿಸಿ.",
    "Procure quality inputs / stock / equipment from traceable suppliers.": "ವಿಶ್ವಾಸಾರ್ಹ ಮತ್ತು ಪರಿಶೀಲಿಸಬಹುದಾದ ಪೂರೈಕೆದಾರರಿಂದ ಗುಣಮಟ್ಟದ ಇನ್‌ಪುಟ್ / ಸ್ಟಾಕ್ / ಉಪಕರಣಗಳನ್ನು ಖರೀದಿಸಿ.",
    "Start with a manageable pilot size and track labour, water and input use.": "ನಿರ್ವಹಿಸಬಹುದಾದ ಪೈಲಟ್ ಗಾತ್ರದಿಂದ ಆರಂಭಿಸಿ ಮತ್ತು ಕಾರ್ಮಿಕ, ನೀರು ಹಾಗೂ ಇನ್‌ಪುಟ್ ಬಳಕೆಯನ್ನು ದಾಖಲಿಸಿ.",
    "Record production, quality, demand and actual spending.": "ಉತ್ಪಾದನೆ, ಗುಣಮಟ್ಟ, ಬೇಡಿಕೆ ಮತ್ತು ನಿಜವಾದ ಖರ್ಚನ್ನು ದಾಖಲಿಸಿ.",
    "Pilot data meets the planned operating thresholds": "ಪೈಲಟ್ ಡೇಟಾ ಯೋಜಿತ ಕಾರ್ಯಾಚರಣಾ ಮಿತಿಗಳನ್ನು ಪೂರೈಸುತ್ತದೆ",
    "Move into repeat production, secure buyers and scale only where unit economics work.": "ಪುನರಾವರ್ತಿತ ಉತ್ಪಾದನೆಗೆ ತೆರಳಿ, ಖರೀದಿದಾರರನ್ನು ಖಚಿತಪಡಿಸಿ ಮತ್ತು ಪ್ರತಿ ಘಟಕದ ಆರ್ಥಿಕತೆ ಕಾರ್ಯಸಾಧ್ಯವಾಗಿರುವಲ್ಲಿ ಮಾತ್ರ ವಿಸ್ತರಿಸಿ.",
    "Lock B2B + D2C sales channels and define pricing / pack strategy.": "B2B + D2C ಮಾರಾಟ ಚಾನೆಲ್‌ಗಳನ್ನು ನಿಗದಿಪಡಿಸಿ ಮತ್ತು ಬೆಲೆ / ಪ್ಯಾಕ್ ತಂತ್ರವನ್ನು ರೂಪಿಸಿ.",
    "Schedule production, grading, storage and transport.": "ಉತ್ಪಾದನೆ, ಗ್ರೇಡಿಂಗ್, ಸಂಗ್ರಹಣೆ ಮತ್ತು ಸಾರಿಗೆಯ ವೇಳಾಪಟ್ಟಿ ರೂಪಿಸಿ.",
    "Review monthly cash flow and expand capacity in controlled steps.": "ಮಾಸಿಕ ನಗದು ಹರಿವನ್ನು ಪರಿಶೀಲಿಸಿ ಮತ್ತು ನಿಯಂತ್ರಿತ ಹಂತಗಳಲ್ಲಿ ಸಾಮರ್ಥ್ಯವನ್ನು ಹೆಚ್ಚಿಸಿ.",
    "Repeat demand + workable unit economics + operational control": "ಪುನರಾವರ್ತಿತ ಬೇಡಿಕೆ + ಕಾರ್ಯಸಾಧ್ಯ ಪ್ರತಿ ಘಟಕದ ಆರ್ಥಿಕತೆ + ಕಾರ್ಯಾಚರಣಾ ನಿಯಂತ್ರಣ",
    "Do not move straight from setup to full investment. Validate the pilot, actual operating cost and buyer response first.": "ಸ್ಥಾಪನೆಯಿಂದ ನೇರವಾಗಿ ಪೂರ್ಣ ಹೂಡಿಕೆಗೆ ಹೋಗಬೇಡಿ. ಮೊದಲು ಪೈಲಟ್, ನಿಜವಾದ ಕಾರ್ಯಾಚರಣಾ ವೆಚ್ಚ ಮತ್ತು ಖರೀದಿದಾರರ ಪ್ರತಿಕ್ರಿಯೆಯನ್ನು ಪರಿಶೀಲಿಸಿ.",
    "Weeks 1–2": "ವಾರಗಳು 1–2",
    "Weeks 3–8": "ವಾರಗಳು 3–8",
    "After pilot validation": "ಪೈಲಟ್ ಪರಿಶೀಲನೆಯ ನಂತರ",
    "Foundation & Setup": "ಅಡಿಪಾಯ ಮತ್ತು ಸ್ಥಾಪನೆ",
    "Procure & Pilot": "ಖರೀದಿ ಮತ್ತು ಪೈಲಟ್",
    "Production, Market & Scale": "ಉತ್ಪಾದನೆ, ಮಾರುಕಟ್ಟೆ ಮತ್ತು ವಿಸ್ತರಣೆ",
    "READY THE BUSINESS": "ವ್ಯವಹಾರವನ್ನು ಸಿದ್ಧಪಡಿಸಿ",
    "TEST BEFORE SCALE": "ವಿಸ್ತರಿಸುವ ಮೊದಲು ಪರೀಕ್ಷಿಸಿ",
    "TURN THE PILOT INTO A BUSINESS": "ಪೈಲಟ್ ಅನ್ನು ವ್ಯವಹಾರವಾಗಿ ರೂಪಿಸಿ",
})


# Complete Business Recommendation output translations supplied for the
# Route, Risk Control, Financial Benchmarks, success criterion and Schemes.
OUTPUT_TR.setdefault("Hindi", {}).update({
    "Route": "मार्ग",
    "Practical use": "व्यावहारिक उपयोग",
    "Pricing focus": "मूल्य निर्धारण पर ध्यान",
    "B2B": "B2B",
    "D2C": "D2C",
    "Local institutional, wholesale or business buyers.": "स्थानीय संस्थागत, थोक या व्यावसायिक खरीदार।",
    "Compare net realized price after transport, handling and buyer deductions.": "परिवहन, हैंडलिंग और खरीदार की कटौतियों के बाद प्राप्त शुद्ध मूल्य की तुलना करें।",
    "Direct local households or end users where practical.": "जहां व्यावहारिक हो, स्थानीय परिवारों या अंतिम उपयोगकर्ताओं को सीधे बेचें।",
    "Test pack size, convenience, quality and repeat-purchase potential.": "पैक आकार, सुविधा, गुणवत्ता और दोबारा खरीद की संभावना का परीक्षण करें।",
    "Differentiation": "अलग पहचान",
    "Quality, grading, reliability, packaging or verified production practices where relevant.": "जहां प्रासंगिक हो, गुणवत्ता, ग्रेडिंग, विश्वसनीयता, पैकेजिंग या सत्यापित उत्पादन प्रक्रियाओं के आधार पर अलग पहचान बनाएं।",
    "Measure realized premium rather than assuming a premium.": "प्रीमियम मान लेने के बजाय वास्तविक रूप से प्राप्त प्रीमियम को मापें।",
    "Verify the main technical requirement and market channel before committing the full investment.": "पूर्ण निवेश करने से पहले मुख्य तकनीकी आवश्यकता और बाजार चैनल की पुष्टि करें।",
    "Use current local quotations for the startup and working-capital plan.": "स्टार्टअप और कार्यशील पूंजी योजना के लिए वर्तमान स्थानीय कोटेशन का उपयोग करें।",
    "Start with a manageable pilot and scale only after recording actual operating results.": "प्रबंधनीय पायलट से शुरुआत करें और वास्तविक संचालन परिणाम दर्ज करने के बाद ही विस्तार करें।",
    "Risk level": "अपरिपक्वता स्तर",
    "Impact": "प्रभाव",
    "Control / mitigation": "नियंत्रण / समाधान",
    "Market access risk": "बाजार पहुंच जोखिम",
    "Water availability risk": "पानी की उपलब्धता का जोखिम",
    "Biological crop risk": "जैविक फसल जोखिम",
    "Climate risk": "जलवायु जोखिम",
    "Crop price variation": "फसल मूल्य में बदलाव",
    "Input price variation": "इनपुट मूल्य में बदलाव",
    "Water availability": "पानी की उपलब्धता",
    "High": "उच्च",
    "Medium": "मध्यम",
    "Low": "कम",
    "High potential impact": "उच्च संभावित प्रभाव",
    "Identify at least two buyers before scaling, compare local prices weekly, and avoid expanding production until a selling channel is confirmed.": "विस्तार से पहले कम से कम दो खरीदारों की पहचान करें, स्थानीय कीमतों की साप्ताहिक तुलना करें और बिक्री चैनल की पुष्टि होने तक उत्पादन न बढ़ाएं।",
    "Secure a reliable source before scaling and maintain a contingency arrangement appropriate to the activity.": "विस्तार से पहले विश्वसनीय जल स्रोत सुनिश्चित करें और गतिविधि के अनुरूप वैकल्पिक व्यवस्था रखें।",
    "Use regular field scouting and preventive integrated management.": "नियमित खेत निरीक्षण और निवारक एकीकृत प्रबंधन अपनाएं।",
    "Use season-appropriate planning and a contingency response for extreme weather.": "मौसम के अनुसार योजना बनाएं और चरम मौसम के लिए वैकल्पिक प्रतिक्रिया तैयार रखें।",
    "Monitor this risk regularly and define a preventive response before scaling.": "इस जोखिम की नियमित निगरानी करें और विस्तार से पहले निवारक प्रतिक्रिया निर्धारित करें।",
    "Benchmark": "मानक",
    "Value": "मान",
    "Note": "टिप्पणी",
    "CAPEX": "पूंजीगत व्यय",
    "Validate with quotations.": "कोटेशन से सत्यापित करें।",
    "Feasibility": "व्यवहार्यता",
    "Adaptive rule-based score.": "अनुकूली नियम-आधारित स्कोर।",
    "Break-even": "ब्रेक-ईवन",
    "Not estimated": "अनुमानित नहीं",
    "Needs a configured financial model for this activity.": "इस गतिविधि के लिए कॉन्फ़िगर किया गया वित्तीय मॉडल आवश्यक है।",
    "Success criterion: Complete a pilot that records unit cost, production/service volume, actual selling price, loss/mortality where applicable, and customer acquisition cost before scaling.": "सफलता मानदंड: विस्तार से पहले इकाई लागत, उत्पादन/सेवा मात्रा, वास्तविक बिक्री मूल्य, जहां लागू हो वहां नुकसान/मृत्यु दर और ग्राहक प्राप्ति लागत दर्ज करने वाला पायलट पूरा करें।",
    "Success criterion": "सफलता मानदंड",
    "What it supports": "यह किसे सहायता करता है",
    "Financial assistance": "वित्तीय सहायता",
    "Eligibility": "पात्रता",
    "Key documents / conditions": "मुख्य दस्तावेज / शर्तें",
    "Kisan Credit Card (KCC)": "किसान क्रेडिट कार्ड (KCC)",
    "A formal agricultural credit mechanism for eligible crop and allied working-capital requirements.": "पात्र फसल और संबद्ध कार्यशील पूंजी आवश्यकताओं के लिए औपचारिक कृषि ऋण व्यवस्था।",
    "Provides access to institutional credit for eligible agricultural/allied needs, subject to lender and eligibility conditions.": "ऋणदाता और पात्रता शर्तों के अधीन, पात्र कृषि/संबद्ध आवश्यकताओं के लिए संस्थागत ऋण तक पहुंच प्रदान करता है।",
    "Farmer/borrower eligibility and sanctioned limits depend on the participating financial institution and applicable KCC rules.": "किसान/उधारकर्ता की पात्रता और स्वीकृत सीमा संबंधित वित्तीय संस्था तथा लागू KCC नियमों पर निर्भर करती है।",
    "KCC is credit, not a direct capital subsidy; repayment and lending conditions apply.": "KCC ऋण सुविधा है, प्रत्यक्ष पूंजी सब्सिडी नहीं; पुनर्भुगतान और ऋण शर्तें लागू होती हैं।",
    "Agriculture Infrastructure Fund (AIF)": "कृषि अवसंरचना निधि (AIF)",
    "A financing facility for eligible post-harvest management and agricultural infrastructure projects.": "पात्र फसल-कटाई के बाद प्रबंधन और कृषि अवसंरचना परियोजनाओं के लिए वित्तपोषण सुविधा।",
    "Official scheme material provides eligible borrowers with interest-support and credit-facilitation benefits subject to scheme conditions.": "आधिकारिक योजना सामग्री के अनुसार, योजना की शर्तों के अधीन पात्र उधारकर्ताओं को ब्याज सहायता और ऋण सुविधा लाभ मिलते हैं।",
    "Eligibility depends on the borrower category and the infrastructure asset/project being financed.": "पात्रता उधारकर्ता की श्रेणी और वित्तपोषित की जा रही अवसंरचना संपत्ति/परियोजना पर निर्भर करती है।",
    "The recommended project must fit an eligible infrastructure category and the current lending guidelines.": "अनुशंसित परियोजना को पात्र अवसंरचना श्रेणी और वर्तमान ऋण दिशानिर्देशों के अनुरूप होना चाहिए।",
})

OUTPUT_TR.setdefault("Kannada", {}).update({
    "Route": "ಮಾರ್ಗ",
    "Practical use": "ಪ್ರಾಯೋಗಿಕ ಬಳಕೆ",
    "Pricing focus": "ಬೆಲೆ ನಿಗದಿ ಗಮನ",
    "B2B": "B2B",
    "D2C": "D2C",
    "Local institutional, wholesale or business buyers.": "ಸ್ಥಳೀಯ ಸಂಸ್ಥೆಗಳು, ಸಗಟು ಖರೀದಿದಾರರು ಅಥವಾ ವ್ಯವಹಾರಿಕ ಖರೀದಿದಾರರು.",
    "Compare net realized price after transport, handling and buyer deductions.": "ಸಾರಿಗೆ, ನಿರ್ವಹಣೆ ಮತ್ತು ಖರೀದಿದಾರರ ಕಡಿತಗಳ ನಂತರ ದೊರೆಯುವ ನಿವ್ವಳ ಬೆಲೆಯನ್ನು ಹೋಲಿಸಿ.",
    "Direct local households or end users where practical.": "ಪ್ರಾಯೋಗಿಕವಾಗಿರುವಲ್ಲಿ ಸ್ಥಳೀಯ ಕುಟುಂಬಗಳು ಅಥವಾ ಅಂತಿಮ ಬಳಕೆದಾರರಿಗೆ ನೇರವಾಗಿ ಮಾರಾಟ ಮಾಡಿ.",
    "Test pack size, convenience, quality and repeat-purchase potential.": "ಪ್ಯಾಕ್ ಗಾತ್ರ, ಅನುಕೂಲತೆ, ಗುಣಮಟ್ಟ ಮತ್ತು ಮರುಖರೀದಿ ಸಾಧ್ಯತೆಯನ್ನು ಪರೀಕ್ಷಿಸಿ.",
    "Differentiation": "ವೈಶಿಷ್ಟ್ಯತೆ",
    "Quality, grading, reliability, packaging or verified production practices where relevant.": "ಅಗತ್ಯವಿರುವಲ್ಲಿ ಗುಣಮಟ್ಟ, ಗ್ರೇಡಿಂಗ್, ವಿಶ್ವಾಸಾರ್ಹತೆ, ಪ್ಯಾಕೇಜಿಂಗ್ ಅಥವಾ ಪರಿಶೀಲಿತ ಉತ್ಪಾದನಾ ವಿಧಾನಗಳ ಮೂಲಕ ವೈಶಿಷ್ಟ್ಯತೆ ರೂಪಿಸಿ.",
    "Measure realized premium rather than assuming a premium.": "ಪ್ರೀಮಿಯಂ ಇದೆ ಎಂದು ಊಹಿಸುವ ಬದಲು ನಿಜವಾಗಿ ದೊರೆತ ಪ್ರೀಮಿಯಂ ಅನ್ನು ಅಳೆಯಿರಿ.",
    "Verify the main technical requirement and market channel before committing the full investment.": "ಪೂರ್ಣ ಹೂಡಿಕೆಗೆ ಬದ್ಧರಾಗುವ ಮೊದಲು ಮುಖ್ಯ ತಾಂತ್ರಿಕ ಅವಶ್ಯಕತೆ ಮತ್ತು ಮಾರುಕಟ್ಟೆ ಚಾನೆಲ್ ಅನ್ನು ಪರಿಶೀಲಿಸಿ.",
    "Use current local quotations for the startup and working-capital plan.": "ಸ್ಟಾರ್ಟ್‌ಅಪ್ ಮತ್ತು ಕಾರ್ಯನಿರ್ವಹಣಾ ಬಂಡವಾಳ ಯೋಜನೆಗಾಗಿ ಪ್ರಸ್ತುತ ಸ್ಥಳೀಯ ಕೋಟೇಶನ್‌ಗಳನ್ನು ಬಳಸಿ.",
    "Start with a manageable pilot and scale only after recording actual operating results.": "ನಿರ್ವಹಿಸಬಹುದಾದ ಪೈಲಟ್‌ನಿಂದ ಆರಂಭಿಸಿ ಮತ್ತು ನಿಜವಾದ ಕಾರ್ಯಾಚರಣಾ ಫಲಿತಾಂಶಗಳನ್ನು ದಾಖಲಿಸಿದ ನಂತರ ಮಾತ್ರ ವಿಸ್ತರಿಸಿ.",
    "Risk level": "ಅಪಾಯ ಮಟ್ಟ",
    "Impact": "ಪರಿಣಾಮ",
    "Control / mitigation": "ನಿಯಂತ್ರಣ / ಪರಿಹಾರ",
    "Market access risk": "ಮಾರುಕಟ್ಟೆ ಪ್ರವೇಶ ಅಪಾಯ",
    "Water availability risk": "ನೀರಿನ ಲಭ್ಯತೆ ಅಪಾಯ",
    "Biological crop risk": "ಜೈವಿಕ ಬೆಳೆ ಅಪಾಯ",
    "Climate risk": "ಹವಾಮಾನ ಅಪಾಯ",
    "Crop price variation": "ಬೆಳೆ ಬೆಲೆ ಬದಲಾವಣೆ",
    "Input price variation": "ಇನ್‌ಪುಟ್ ಬೆಲೆ ಬದಲಾವಣೆ",
    "Water availability": "ನೀರಿನ ಲಭ್ಯತೆ",
    "High": "ಹೆಚ್ಚು",
    "Medium": "ಮಧ್ಯಮ",
    "Low": "ಕಡಿಮೆ",
    "High potential impact": "ಹೆಚ್ಚಿನ ಸಾಧ್ಯ ಪರಿಣಾಮ",
    "Identify at least two buyers before scaling, compare local prices weekly, and avoid expanding production until a selling channel is confirmed.": "ವಿಸ್ತರಿಸುವ ಮೊದಲು ಕನಿಷ್ಠ ಇಬ್ಬರು ಖರೀದಿದಾರರನ್ನು ಗುರುತಿಸಿ, ಸ್ಥಳೀಯ ಬೆಲೆಗಳನ್ನು ವಾರಕ್ಕೊಮ್ಮೆ ಹೋಲಿಸಿ ಮತ್ತು ಮಾರಾಟ ಚಾನೆಲ್ ದೃಢವಾಗುವವರೆಗೆ ಉತ್ಪಾದನೆಯನ್ನು ಹೆಚ್ಚಿಸಬೇಡಿ.",
    "Secure a reliable source before scaling and maintain a contingency arrangement appropriate to the activity.": "ವಿಸ್ತರಿಸುವ ಮೊದಲು ವಿಶ್ವಾಸಾರ್ಹ ನೀರಿನ ಮೂಲವನ್ನು ಖಚಿತಪಡಿಸಿ ಮತ್ತು ಚಟುವಟಿಕೆಗೆ ಸೂಕ್ತವಾದ ಪರ್ಯಾಯ ವ್ಯವಸ್ಥೆಯನ್ನು ಇಟ್ಟುಕೊಳ್ಳಿ.",
    "Use regular field scouting and preventive integrated management.": "ನಿಯಮಿತ ಹೊಲ ಪರಿಶೀಲನೆ ಮತ್ತು ತಡೆಗಟ್ಟುವ ಸಮಗ್ರ ನಿರ್ವಹಣೆಯನ್ನು ಬಳಸಿ.",
    "Use season-appropriate planning and a contingency response for extreme weather.": "ಋತುವಿಗೆ ಸೂಕ್ತವಾದ ಯೋಜನೆ ಮತ್ತು ತೀವ್ರ ಹವಾಮಾನಕ್ಕೆ ಪರ್ಯಾಯ ಪ್ರತಿಕ್ರಿಯೆಯನ್ನು ಬಳಸಿ.",
    "Monitor this risk regularly and define a preventive response before scaling.": "ಈ ಅಪಾಯವನ್ನು ನಿಯಮಿತವಾಗಿ ಮೇಲ್ವಿಚಾರಣೆ ಮಾಡಿ ಮತ್ತು ವಿಸ್ತರಿಸುವ ಮೊದಲು ತಡೆಗಟ್ಟುವ ಪ್ರತಿಕ್ರಿಯೆಯನ್ನು ನಿರ್ಧರಿಸಿ.",
    "Benchmark": "ಮಾನದಂಡ",
    "Value": "ಮೌಲ್ಯ",
    "Note": "ಟಿಪ್ಪಣಿ",
    "CAPEX": "ಬಂಡವಾಳ ವೆಚ್ಚ",
    "Validate with quotations.": "ಕೋಟೇಶನ್‌ಗಳಿಂದ ಪರಿಶೀಲಿಸಿ.",
    "Feasibility": "ಕಾರ್ಯಸಾಧ್ಯತೆ",
    "Adaptive rule-based score.": "ಹೊಂದಿಕೊಳ್ಳುವ ನಿಯಮ-ಆಧಾರಿತ ಸ್ಕೋರ್.",
    "Break-even": "ಬ್ರೇಕ್-ಈವನ್",
    "Not estimated": "ಅಂದಾಜಿಸಲಾಗಿಲ್ಲ",
    "Needs a configured financial model for this activity.": "ಈ ಚಟುವಟಿಕೆಗೆ ಕಾನ್ಫಿಗರ್ ಮಾಡಲಾದ ಹಣಕಾಸು ಮಾದರಿ ಅಗತ್ಯವಿದೆ.",
    "Success criterion: Complete a pilot that records unit cost, production/service volume, actual selling price, loss/mortality where applicable, and customer acquisition cost before scaling.": "ಯಶಸ್ಸಿನ ಮಾನದಂಡ: ವಿಸ್ತರಿಸುವ ಮೊದಲು ಘಟಕ ವೆಚ್ಚ, ಉತ್ಪಾದನೆ/ಸೇವಾ ಪ್ರಮಾಣ, ನಿಜವಾದ ಮಾರಾಟ ಬೆಲೆ, ಅನ್ವಯಿಸಿದಲ್ಲಿ ನಷ್ಟ/ಸಾವು ಪ್ರಮಾಣ ಮತ್ತು ಗ್ರಾಹಕ ಗಳಿಕೆ ವೆಚ್ಚವನ್ನು ದಾಖಲಿಸುವ ಪೈಲಟ್ ಪೂರ್ಣಗೊಳಿಸಿ.",
    "Success criterion": "ಯಶಸ್ಸಿನ ಮಾನದಂಡ",
    "What it supports": "ಇದು ಯಾವುದಕ್ಕೆ ಸಹಾಯ ಮಾಡುತ್ತದೆ",
    "Financial assistance": "ಹಣಕಾಸಿನ ನೆರವು",
    "Eligibility": "ಅರ್ಹತೆ",
    "Key documents / conditions": "ಮುಖ್ಯ ದಾಖಲೆಗಳು / ಷರತ್ತುಗಳು",
    "Kisan Credit Card (KCC)": "ಕಿಸಾನ್ ಕ್ರೆಡಿಟ್ ಕಾರ್ಡ್ (KCC)",
    "A formal agricultural credit mechanism for eligible crop and allied working-capital requirements.": "ಅರ್ಹ ಬೆಳೆ ಮತ್ತು ಸಂಬಂಧಿತ ಕಾರ್ಯನಿರ್ವಹಣಾ ಬಂಡವಾಳ ಅಗತ್ಯಗಳಿಗಾಗಿ ಅಧಿಕೃತ ಕೃಷಿ ಸಾಲ ವ್ಯವಸ್ಥೆ.",
    "Provides access to institutional credit for eligible agricultural/allied needs, subject to lender and eligibility conditions.": "ಸಾಲದಾತ ಮತ್ತು ಅರ್ಹತಾ ಷರತ್ತುಗಳಿಗೆ ಒಳಪಟ್ಟು, ಅರ್ಹ ಕೃಷಿ/ಸಂಬಂಧಿತ ಅಗತ್ಯಗಳಿಗೆ ಸಂಸ್ಥೆಯ ಸಾಲ ಸೌಲಭ್ಯವನ್ನು ಒದಗಿಸುತ್ತದೆ.",
    "Farmer/borrower eligibility and sanctioned limits depend on the participating financial institution and applicable KCC rules.": "ರೈತ/ಸಾಲಗಾರರ ಅರ್ಹತೆ ಮತ್ತು ಮಂಜೂರಾದ ಮಿತಿಗಳು ಭಾಗವಹಿಸುವ ಹಣಕಾಸು ಸಂಸ್ಥೆ ಹಾಗೂ ಅನ್ವಯಿಸುವ KCC ನಿಯಮಗಳ ಮೇಲೆ ಅವಲಂಬಿತವಾಗಿವೆ.",
    "KCC is credit, not a direct capital subsidy; repayment and lending conditions apply.": "KCC ಸಾಲ ಸೌಲಭ್ಯವಾಗಿದ್ದು, ನೇರ ಬಂಡವಾಳ ಸಬ್ಸಿಡಿ ಅಲ್ಲ; ಮರುಪಾವತಿ ಮತ್ತು ಸಾಲದ ಷರತ್ತುಗಳು ಅನ್ವಯಿಸುತ್ತವೆ.",
    "Agriculture Infrastructure Fund (AIF)": "ಕೃಷಿ ಮೂಲಸೌಕರ್ಯ ನಿಧಿ (AIF)",
    "A financing facility for eligible post-harvest management and agricultural infrastructure projects.": "ಅರ್ಹ ಕೊಯ್ಲಿನ ನಂತರದ ನಿರ್ವಹಣೆ ಮತ್ತು ಕೃಷಿ ಮೂಲಸೌಕರ್ಯ ಯೋಜನೆಗಳಿಗೆ ಹಣಕಾಸು ಸೌಲಭ್ಯ.",
    "Official scheme material provides eligible borrowers with interest-support and credit-facilitation benefits subject to scheme conditions.": "ಯೋಜನೆಯ ಷರತ್ತುಗಳಿಗೆ ಒಳಪಟ್ಟು ಅರ್ಹ ಸಾಲಗಾರರಿಗೆ ಬಡ್ಡಿ ನೆರವು ಮತ್ತು ಸಾಲ ಸೌಲಭ್ಯ ಪ್ರಯೋಜನಗಳನ್ನು ಅಧಿಕೃತ ಯೋಜನಾ ಮಾಹಿತಿಯು ಒದಗಿಸುತ್ತದೆ.",
    "Eligibility depends on the borrower category and the infrastructure asset/project being financed.": "ಅರ್ಹತೆಯು ಸಾಲಗಾರರ ವರ್ಗ ಮತ್ತು ಹಣಕಾಸು ಒದಗಿಸಲಾಗುತ್ತಿರುವ ಮೂಲಸೌಕರ್ಯ ಆಸ್ತಿ/ಯೋಜನೆಯ ಮೇಲೆ ಅವಲಂಬಿತವಾಗಿದೆ.",
    "The recommended project must fit an eligible infrastructure category and the current lending guidelines.": "ಶಿಫಾರಸು ಮಾಡಲಾದ ಯೋಜನೆಯು ಅರ್ಹ ಮೂಲಸೌಕರ್ಯ ವರ್ಗ ಮತ್ತು ಪ್ರಸ್ತುತ ಸಾಲ ಮಾರ್ಗಸೂಚಿಗಳಿಗೆ ಹೊಂದಿಕೆಯಾಗಿರಬೇಕು.",
})


# Kannada translations for the complete Business Recommendation content.
# These are exact UI/output strings, so the English version remains unchanged
# when English is selected.
PASTED_KANNADA_OUTPUT = {
    "Route": "ಮಾರ್ಗ",
    "Practical use": "ಪ್ರಾಯೋಗಿಕ ಬಳಕೆ",
    "Pricing focus": "ಬೆಲೆ ನಿಗದಿ ಗಮನ",
    "Local institutional, wholesale or business buyers.": "ಸ್ಥಳೀಯ ಸಂಸ್ಥೆಗಳು, ಸಗಟು ಅಥವಾ ವ್ಯವಹಾರಿಕ ಖರೀದಿದಾರರು.",
    "Compare net realized price after transport, handling and buyer deductions.": "ಸಾರಿಗೆ, ನಿರ್ವಹಣೆ ಮತ್ತು ಖರೀದಿದಾರರ ಕಡಿತಗಳ ನಂತರ ದೊರೆಯುವ ನಿವ್ವಳ ಬೆಲೆಯನ್ನು ಹೋಲಿಸಿ.",
    "Direct local households or end users where practical.": "ಪ್ರಾಯೋಗಿಕವಾಗಿರುವಲ್ಲಿ ಸ್ಥಳೀಯ ಕುಟುಂಬಗಳು ಅಥವಾ ಅಂತಿಮ ಬಳಕೆದಾರರಿಗೆ ನೇರವಾಗಿ ಮಾರಾಟ ಮಾಡಿ.",
    "Test pack size, convenience, quality and repeat-purchase potential.": "ಪ್ಯಾಕ್ ಗಾತ್ರ, ಅನುಕೂಲತೆ, ಗುಣಮಟ್ಟ ಮತ್ತು ಮರುಖರೀದಿ ಸಾಧ್ಯತೆಯನ್ನು ಪರೀಕ್ಷಿಸಿ.",
    "Quality, grading, reliability, packaging or verified production practices where relevant.": "ಅಗತ್ಯವಿರುವಲ್ಲಿ ಗುಣಮಟ್ಟ, ಗ್ರೇಡಿಂಗ್, ವಿಶ್ವಾಸಾರ್ಹತೆ, ಪ್ಯಾಕೇಜಿಂಗ್ ಅಥವಾ ಪರಿಶೀಲಿತ ಉತ್ಪಾದನಾ ವಿಧಾನಗಳ ಮೂಲಕ ವೈಶಿಷ್ಟ್ಯತೆ ರೂಪಿಸಿ.",
    "Measure realized premium rather than assuming a premium.": "ಪ್ರೀಮಿಯಂ ಇದೆ ಎಂದು ಊಹಿಸುವ ಬದಲು ನಿಜವಾಗಿ ದೊರೆತ ಪ್ರೀಮಿಯಂ ಅನ್ನು ಅಳೆಯಿರಿ.",
    "Verify the main technical requirement and market channel before committing the full investment.": "ಪೂರ್ಣ ಹೂಡಿಕೆಗೆ ಬದ್ಧರಾಗುವ ಮೊದಲು ಮುಖ್ಯ ತಾಂತ್ರಿಕ ಅವಶ್ಯಕತೆ ಮತ್ತು ಮಾರುಕಟ್ಟೆ ಚಾನೆಲ್ ಅನ್ನು ಪರಿಶೀಲಿಸಿ.",
    "Use current local quotations for the startup and working-capital plan.": "ಸ್ಟಾರ್ಟ್‌ಅಪ್ ಮತ್ತು ಕಾರ್ಯನಿರ್ವಹಣಾ ಬಂಡವಾಳ ಯೋಜನೆಗಾಗಿ ಪ್ರಸ್ತುತ ಸ್ಥಳೀಯ ಕೋಟೇಶನ್‌ಗಳನ್ನು ಬಳಸಿ.",
    "Start with a manageable pilot and scale only after recording actual operating results.": "ನಿರ್ವಹಿಸಬಹುದಾದ ಪೈಲಟ್‌ನಿಂದ ಆರಂಭಿಸಿ ಮತ್ತು ನಿಜವಾದ ಕಾರ್ಯಾಚರಣಾ ಫಲಿತಾಂಶಗಳನ್ನು ದಾಖಲಿಸಿದ ನಂತರ ಮಾತ್ರ ವಿಸ್ತರಿಸಿ.",

    "Risk level": "ಅಪಾಯ ಮಟ್ಟ",
    "Impact": "ಪರಿಣಾಮ",
    "Control / mitigation": "ನಿಯಂತ್ರಣ / ಪರಿಹಾರ",
    "Market access risk": "ಮಾರುಕಟ್ಟೆ ಪ್ರವೇಶ ಅಪಾಯ",
    "Water availability risk": "ನೀರಿನ ಲಭ್ಯತೆ ಅಪಾಯ",
    "Biological crop risk": "ಜೈವಿಕ ಬೆಳೆ ಅಪಾಯ",
    "Climate risk": "ಹವಾಮಾನ ಅಪಾಯ",
    "Crop price variation": "ಬೆಳೆ ಬೆಲೆ ಬದಲಾವಣೆ",
    "Input price variation": "ಇನ್‌ಪುಟ್ ಬೆಲೆ ಬದಲಾವಣೆ",
    "Water availability": "ನೀರಿನ ಲಭ್ಯತೆ",
    "High": "ಹೆಚ್ಚು",
    "Medium": "ಮಧ್ಯಮ",
    "Low": "ಕಡಿಮೆ",
    "High potential impact": "ಹೆಚ್ಚಿನ ಸಾಧ್ಯ ಪರಿಣಾಮ",
    "—": "—",
    "Identify at least two buyers before scaling, compare local prices weekly, and avoid expanding production until a selling channel is confirmed.": "ವಿಸ್ತರಿಸುವ ಮೊದಲು ಕನಿಷ್ಠ ಇಬ್ಬರು ಖರೀದಿದಾರರನ್ನು ಗುರುತಿಸಿ, ಸ್ಥಳೀಯ ಬೆಲೆಗಳನ್ನು ವಾರಕ್ಕೊಮ್ಮೆ ಹೋಲಿಸಿ ಮತ್ತು ಮಾರಾಟ ಚಾನೆಲ್ ದೃಢವಾಗುವವರೆಗೆ ಉತ್ಪಾದನೆಯನ್ನು ಹೆಚ್ಚಿಸಬೇಡಿ.",
    "Secure a reliable source before scaling and maintain a contingency arrangement appropriate to the activity.": "ವಿಸ್ತರಿಸುವ ಮೊದಲು ವಿಶ್ವಾಸಾರ್ಹ ನೀರಿನ ಮೂಲವನ್ನು ಖಚಿತಪಡಿಸಿ ಮತ್ತು ಚಟುವಟಿಕೆಗೆ ಸೂಕ್ತವಾದ ಪರ್ಯಾಯ ವ್ಯವಸ್ಥೆಯನ್ನು ಇಟ್ಟುಕೊಳ್ಳಿ.",
    "Use regular field scouting and preventive integrated management.": "ನಿಯಮಿತ ಹೊಲ ಪರಿಶೀಲನೆ ಮತ್ತು ತಡೆಗಟ್ಟುವ ಸಮಗ್ರ ನಿರ್ವಹಣೆಯನ್ನು ಬಳಸಿ.",
    "Use season-appropriate planning and a contingency response for extreme weather.": "ಋತುವಿಗೆ ಸೂಕ್ತವಾದ ಯೋಜನೆ ಮತ್ತು ತೀವ್ರ ಹವಾಮಾನಕ್ಕೆ ಪರ್ಯಾಯ ಪ್ರತಿಕ್ರಿಯೆಯನ್ನು ಬಳಸಿ.",
    "Monitor this risk regularly and define a preventive response before scaling.": "ಈ ಅಪಾಯವನ್ನು ನಿಯಮಿತವಾಗಿ ಮೇಲ್ವಿಚಾರಣೆ ಮಾಡಿ ಮತ್ತು ವಿಸ್ತರಿಸುವ ಮೊದಲು ತಡೆಗಟ್ಟುವ ಪ್ರತಿಕ್ರಿಯೆಯನ್ನು ನಿರ್ಧರಿಸಿ.",

    "Benchmark": "ಮಾನದಂಡ",
    "Value": "ಮೌಲ್ಯ",
    "Note": "ಟಿಪ್ಪಣಿ",
    "CAPEX": "ಬಂಡವಾಳ ವೆಚ್ಚ",
    "Validate with quotations.": "ಕೋಟೇಶನ್‌ಗಳಿಂದ ಪರಿಶೀಲಿಸಿ.",
    "Feasibility": "ಕಾರ್ಯಸಾಧ್ಯತೆ",
    "Adaptive rule-based score.": "ಹೊಂದಿಕೊಳ್ಳುವ ನಿಯಮ-ಆಧಾರಿತ ಸ್ಕೋರ್.",
    "Break-even": "ಬ್ರೇಕ್-ಈವನ್",
    "Not estimated": "ಅಂದಾಜಿಸಲಾಗಿಲ್ಲ",
    "Needs a configured financial model for this activity.": "ಈ ಚಟುವಟಿಕೆಗೆ ಕಾನ್ಫಿಗರ್ ಮಾಡಲಾದ ಹಣಕಾಸು ಮಾದರಿ ಅಗತ್ಯವಿದೆ.",

    "Success criterion": "ಯಶಸ್ಸಿನ ಮಾನದಂಡ",
    "Success criterion: Complete a pilot that records unit cost, production/service volume, actual selling price, loss/mortality where applicable, and customer acquisition cost before scaling.": "ಯಶಸ್ಸಿನ ಮಾನದಂಡ: ವಿಸ್ತರಿಸುವ ಮೊದಲು ಘಟಕ ವೆಚ್ಚ, ಉತ್ಪಾದನೆ/ಸೇವಾ ಪ್ರಮಾಣ, ನಿಜವಾದ ಮಾರಾಟ ಬೆಲೆ, ಅನ್ವಯಿಸಿದಲ್ಲಿ ನಷ್ಟ/ಸಾವು ಪ್ರಮಾಣ ಮತ್ತು ಗ್ರಾಹಕ ಗಳಿಕೆ ವೆಚ್ಚವನ್ನು ದಾಖಲಿಸುವ ಪೈಲಟ್ ಪೂರ್ಣಗೊಳಿಸಿ.",

    "Scheme": "ಯೋಜನೆ",
    "What it supports": "ಇದು ಯಾವುದಕ್ಕೆ ಸಹಾಯ ಮಾಡುತ್ತದೆ",
    "Financial assistance": "ಹಣಕಾಸಿನ ನೆರವು",
    "Eligibility": "ಅರ್ಹತೆ",
    "Key documents / conditions": "ಮುಖ್ಯ ದಾಖಲೆಗಳು / ಷರತ್ತುಗಳು",
    "Kisan Credit Card (KCC)": "ಕಿಸಾನ್ ಕ್ರೆಡಿಟ್ ಕಾರ್ಡ್ (KCC)",
    "A formal agricultural credit mechanism for eligible crop and allied working-capital requirements.": "ಅರ್ಹ ಬೆಳೆ ಮತ್ತು ಸಂಬಂಧಿತ ಕಾರ್ಯನಿರ್ವಹಣಾ ಬಂಡವಾಳ ಅಗತ್ಯಗಳಿಗಾಗಿ ಅಧಿಕೃತ ಕೃಷಿ ಸಾಲ ವ್ಯವಸ್ಥೆ.",
    "Provides access to institutional credit for eligible agricultural/allied needs, subject to lender and eligibility conditions.": "ಸಾಲದಾತ ಮತ್ತು ಅರ್ಹತಾ ಷರತ್ತುಗಳಿಗೆ ಒಳಪಟ್ಟು, ಅರ್ಹ ಕೃಷಿ/ಸಂಬಂಧಿತ ಅಗತ್ಯಗಳಿಗೆ ಸಂಸ್ಥೆಯ ಸಾಲ ಸೌಲಭ್ಯವನ್ನು ಒದಗಿಸುತ್ತದೆ.",
    "Farmer/borrower eligibility and sanctioned limits depend on the participating financial institution and applicable KCC rules.": "ರೈತ/ಸಾಲಗಾರರ ಅರ್ಹತೆ ಮತ್ತು ಮಂಜೂರಾದ ಮಿತಿಗಳು ಭಾಗವಹಿಸುವ ಹಣಕಾಸು ಸಂಸ್ಥೆ ಹಾಗೂ ಅನ್ವಯಿಸುವ KCC ನಿಯಮಗಳ ಮೇಲೆ ಅವಲಂಬಿತವಾಗಿವೆ.",
    "KCC is credit, not a direct capital subsidy; repayment and lending conditions apply.": "KCC ಸಾಲ ಸೌಲಭ್ಯವಾಗಿದ್ದು, ನೇರ ಬಂಡವಾಳ ಸಬ್ಸಿಡಿ ಅಲ್ಲ; ಮರುಪಾವತಿ ಮತ್ತು ಸಾಲದ ಷರತ್ತುಗಳು ಅನ್ವಯಿಸುತ್ತವೆ.",
    "Agriculture Infrastructure Fund (AIF)": "ಕೃಷಿ ಮೂಲಸೌಕರ್ಯ ನಿಧಿ (AIF)",
    "A financing facility for eligible post-harvest management and agricultural infrastructure projects.": "ಅರ್ಹ ಕೊಯ್ಲಿನ ನಂತರದ ನಿರ್ವಹಣೆ ಮತ್ತು ಕೃಷಿ ಮೂಲಸೌಕರ್ಯ ಯೋಜನೆಗಳಿಗೆ ಹಣಕಾಸು ಸೌಲಭ್ಯ.",
    "Official scheme material provides eligible borrowers with interest-support and credit-facilitation benefits subject to scheme conditions.": "ಯೋಜನೆಯ ಷರತ್ತುಗಳಿಗೆ ಒಳಪಟ್ಟು ಅರ್ಹ ಸಾಲಗಾರರಿಗೆ ಬಡ್ಡಿ ನೆರವು ಮತ್ತು ಸಾಲ ಸೌಲಭ್ಯ ಪ್ರಯೋಜನಗಳನ್ನು ಅಧಿಕೃತ ಯೋಜನಾ ಮಾಹಿತಿಯು ಒದಗಿಸುತ್ತದೆ.",
    "Eligibility depends on the borrower category and the infrastructure asset/project being financed.": "ಅರ್ಹತೆಯು ಸಾಲಗಾರರ ವರ್ಗ ಮತ್ತು ಹಣಕಾಸು ಒದಗಿಸಲಾಗುತ್ತಿರುವ ಮೂಲಸೌಕರ್ಯ ಆಸ್ತಿ/ಯೋಜನೆಯ ಮೇಲೆ ಅವಲಂಬಿತವಾಗಿದೆ.",
    "The recommended project must fit an eligible infrastructure category and the current lending guidelines.": "ಶಿಫಾರಸು ಮಾಡಲಾದ ಯೋಜನೆಯು ಅರ್ಹ ಮೂಲಸೌಕರ್ಯ ವರ್ಗ ಮತ್ತು ಪ್ರಸ್ತುತ ಸಾಲ ಮಾರ್ಗಸೂಚಿಗಳಿಗೆ ಹೊಂದಿಕೆಯಾಗಿರಬೇಕು.",

    # Roadmap
    "Make the site, resources, budget and compliance setup ready.": "ಸ್ಥಳ, ಸಂಪನ್ಮೂಲಗಳು, ಬಜೆಟ್ ಮತ್ತು ಅನುಸರಣೆ ಸಿದ್ಧತೆಯನ್ನು ಪೂರ್ಣಗೊಳಿಸಿ.",
    "Confirm land / workspace, water and access conditions.": "ಭೂಮಿ / ಕೆಲಸದ ಸ್ಥಳ, ನೀರು ಮತ್ತು ಪ್ರವೇಶದ ಪರಿಸ್ಥಿತಿಗಳನ್ನು ಖಚಿತಪಡಿಸಿ.",
    "Prepare a minimum investment plan and cash buffer.": "ಕನಿಷ್ಠ ಹೂಡಿಕೆ ಯೋಜನೆ ಮತ್ತು ನಗದು ಮೀಸಲು ಸಿದ್ಧಪಡಿಸಿ.",
    "Complete required permits, registrations, testing or local checks.": "ಅಗತ್ಯ ಪರವಾನಗಿಗಳು, ನೋಂದಣಿಗಳು, ಪರೀಕ್ಷೆಗಳು ಅಥವಾ ಸ್ಥಳೀಯ ಪರಿಶೀಲನೆಗಳನ್ನು ಪೂರ್ಣಗೊಳಿಸಿ.",
    "Site + resources + budget confirmed": "ಸ್ಥಳ + ಸಂಪನ್ಮೂಲಗಳು + ಬಜೆಟ್ ದೃಢೀಕರಿಸಲಾಗಿದೆ",
    "Run a controlled pilot using the selected option and record real costs.": "ಆಯ್ಕೆ ಮಾಡಿದ ಆಯ್ಕೆಯನ್ನು ಬಳಸಿ ನಿಯಂತ್ರಿತ ಪೈಲಟ್ ನಡೆಸಿ ಮತ್ತು ನಿಜವಾದ ವೆಚ್ಚಗಳನ್ನು ದಾಖಲಿಸಿ.",
    "Procure quality inputs / stock / equipment from traceable suppliers.": "ವಿಶ್ವಾಸಾರ್ಹ ಮತ್ತು ಪರಿಶೀಲಿಸಬಹುದಾದ ಪೂರೈಕೆದಾರರಿಂದ ಗುಣಮಟ್ಟದ ಇನ್‌ಪುಟ್ / ಸ್ಟಾಕ್ / ಉಪಕರಣಗಳನ್ನು ಖರೀದಿಸಿ.",
    "Start with a manageable pilot size and track labour, water and input use.": "ನಿರ್ವಹಿಸಬಹುದಾದ ಪೈಲಟ್ ಗಾತ್ರದಿಂದ ಆರಂಭಿಸಿ ಮತ್ತು ಕಾರ್ಮಿಕ, ನೀರು ಹಾಗೂ ಇನ್‌ಪುಟ್ ಬಳಕೆಯನ್ನು ದಾಖಲಿಸಿ.",
    "Record production, quality, demand and actual spending.": "ಉತ್ಪಾದನೆ, ಗುಣಮಟ್ಟ, ಬೇಡಿಕೆ ಮತ್ತು ನಿಜವಾದ ಖರ್ಚನ್ನು ದಾಖಲಿಸಿ.",
    "Pilot data meets the planned operating thresholds": "ಪೈಲಟ್ ಡೇಟಾ ಯೋಜಿತ ಕಾರ್ಯಾಚರಣಾ ಮಿತಿಗಳನ್ನು ಪೂರೈಸುತ್ತದೆ",
    "Move into repeat production, secure buyers and scale only where unit economics work.": "ಪುನರಾವರ್ತಿತ ಉತ್ಪಾದನೆಗೆ ತೆರಳಿ, ಖರೀದಿದಾರರನ್ನು ಖಚಿತಪಡಿಸಿ ಮತ್ತು ಪ್ರತಿ ಘಟಕದ ಆರ್ಥಿಕತೆ ಕಾರ್ಯಸಾಧ್ಯವಾಗಿರುವಲ್ಲಿ ಮಾತ್ರ ವಿಸ್ತರಿಸಿ.",
    "Lock B2B + D2C sales channels and define pricing / pack strategy.": "B2B + D2C ಮಾರಾಟ ಚಾನೆಲ್‌ಗಳನ್ನು ನಿಗದಿಪಡಿಸಿ ಮತ್ತು ಬೆಲೆ / ಪ್ಯಾಕ್ ತಂತ್ರವನ್ನು ರೂಪಿಸಿ.",
    "Schedule production, grading, storage and transport.": "ಉತ್ಪಾದನೆ, ಗ್ರೇಡಿಂಗ್, ಸಂಗ್ರಹಣೆ ಮತ್ತು ಸಾರಿಗೆಯ ವೇಳಾಪಟ್ಟಿ ರೂಪಿಸಿ.",
    "Review monthly cash flow and expand capacity in controlled steps.": "ಮಾಸಿಕ ನಗದು ಹರಿವನ್ನು ಪರಿಶೀಲಿಸಿ ಮತ್ತು ನಿಯಂತ್ರಿತ ಹಂತಗಳಲ್ಲಿ ಸಾಮರ್ಥ್ಯವನ್ನು ಹೆಚ್ಚಿಸಿ.",
    "Repeat demand + workable unit economics + operational control": "ಪುನರಾವರ್ತಿತ ಬೇಡಿಕೆ + ಕಾರ್ಯಸಾಧ್ಯ ಪ್ರತಿ ಘಟಕದ ಆರ್ಥಿಕತೆ + ಕಾರ್ಯಾಚರಣಾ ನಿಯಂತ್ರಣ",
    "Do not move straight from setup to full investment. Validate the pilot, actual operating cost and buyer response first.": "ಸ್ಥಾಪನೆಯಿಂದ ನೇರವಾಗಿ ಪೂರ್ಣ ಹೂಡಿಕೆಗೆ ಹೋಗಬೇಡಿ. ಮೊದಲು ಪೈಲಟ್, ನಿಜವಾದ ಕಾರ್ಯಾಚರಣಾ ವೆಚ್ಚ ಮತ್ತು ಖರೀದಿದಾರರ ಪ್ರತಿಕ್ರಿಯೆಯನ್ನು ಪರಿಶೀಲಿಸಿ.",
    "Weeks 1–2": "ವಾರಗಳು 1–2",
    "Weeks 3–8": "ವಾರಗಳು 3–8",
    "After pilot validation": "ಪೈಲಟ್ ಪರಿಶೀಲನೆಯ ನಂತರ",
}

def safe_float(value, default=0.0):
    """Safely convert user/config values to float."""
    try:
        if value is None or value == "":
            return default
        return float(value)
    except (TypeError, ValueError):
        return default


def translate_output_recursive(value):
    """Translate Business Recommendation output values recursively."""
    if isinstance(value, dict):
        return {k: translate_output_recursive(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        translated = [translate_output_recursive(v) for v in value]
        return type(value)(translated) if isinstance(value, tuple) else translated
    if isinstance(value, str):
        return tr_any(value)
    return value

def tr_any(value, **kwargs):
    text = str(value)
    # 1. Exact translation from all existing dictionaries.
    translated = TEXT.get(language, {}).get(text, None)
    if translated is None:
        translated = UI_WORD_TR.get(language, {}).get(text, None)
    if translated is None:
        translated = ENV_UI_TR.get(language, {}).get(text, None)
    if translated is None:
        translated = OUTPUT_TR.get(language, {}).get(text, None)
    if translated is None:
        # 2. Crop/category/trend values.
        translated = DATA_TR.get(language, {}).get(text, None)
    if translated is None:
        translated = text
    return translated.format(**kwargs) if kwargs else translated

# Display translations for the crop/category/trend content.

# Display names for business domains, activities, common input values and risk/output terms.
BUSINESS_DISPLAY_TR = {
    "Hindi": {
        "Agriculture":"कृषि", "Livestock":"पशुपालन", "Aquaculture":"मत्स्य पालन", "Food Processing":"खाद्य प्रसंस्करण", "Services":"सेवाएँ", "Retail":"खुदरा",
        "Crop Cultivation":"फसल खेती", "Vegetable Cultivation":"सब्ज़ी खेती", "Fruit Cultivation":"फल खेती", "Spice Cultivation":"मसाला खेती", "Floriculture":"फूलों की खेती",
        "Poultry Farming":"पोल्ट्री फार्मिंग", "Dairy Farming":"डेयरी फार्मिंग", "Goat Farming":"बकरी पालन", "Sheep Farming":"भेड़ पालन", "Fish Farming":"मछली पालन",
        "Kharif":"खरीफ", "Rabi":"रबी", "Summer":"ग्रीष्म", "None":"नहीं", "Low":"कम", "Medium":"मध्यम", "High":"अधिक", "Poor":"कमज़ोर", "Moderate":"मध्यम", "Good":"अच्छा", "No":"नहीं", "Partial":"आंशिक", "Yes":"हाँ", "Shared":"साझा", "Available":"उपलब्ध", "Reliable":"विश्वसनीय", "Rain-fed":"वर्षा आधारित", "Limited":"सीमित", "Beginner":"शुरुआती", "Some experience":"कुछ अनुभव", "Experienced":"अनुभवी", "Within 3 months":"3 महीने के भीतर", "3–6 months":"3–6 महीने", "6–12 months":"6–12 महीने", "12+ months":"12+ महीने",
        "Weather variability":"मौसम में बदलाव", "Water availability":"पानी की उपलब्धता", "Input-price changes":"इनपुट कीमतों में बदलाव", "Crop-price changes":"फसल कीमतों में बदलाव", "Pest/disease pressure":"कीट/रोग का दबाव", "Price fluctuations":"कीमत में उतार-चढ़ाव", "Water stress":"पानी का तनाव", "Market-price changes":"बाज़ार कीमतों में बदलाव", "Market-price variation":"बाज़ार कीमतों में बदलाव", "Post-harvest loss":"कटाई के बाद नुकसान",
    },
    "Kannada": {
        "Agriculture":"ಕೃಷಿ", "Livestock":"ಪಶುಸಂಗೋಪನೆ", "Aquaculture":"ಮೀನುಗಾರಿಕೆ", "Food Processing":"ಆಹಾರ ಸಂಸ್ಕರಣೆ", "Services":"ಸೇವೆಗಳು", "Retail":"ಚಿಲ್ಲರೆ",
        "Crop Cultivation":"ಬೆಳೆ ಕೃಷಿ", "Vegetable Cultivation":"ತರಕಾರಿ ಕೃಷಿ", "Fruit Cultivation":"ಹಣ್ಣು ಕೃಷಿ", "Spice Cultivation":"ಮಸಾಲೆ ಕೃಷಿ", "Floriculture":"ಹೂ ಬೆಳೆ",
        "Poultry Farming":"ಕೋಳಿ ಸಾಕಣೆ", "Dairy Farming":"ಹೈನುಗಾರಿಕೆ", "Goat Farming":"ಮೇಕೆ ಸಾಕಣೆ", "Sheep Farming":"ಕುರಿ ಸಾಕಣೆ", "Fish Farming":"ಮೀನು ಸಾಕಣೆ",
        "Kharif":"ಖರೀಫ್", "Rabi":"ರಬಿ", "Summer":"ಬೇಸಿಗೆ", "None":"ಇಲ್ಲ", "Low":"ಕಡಿಮೆ", "Medium":"ಮಧ್ಯಮ", "High":"ಹೆಚ್ಚು", "Poor":"ಕಡಿಮೆ", "Moderate":"ಮಧ್ಯಮ", "Good":"ಉತ್ತಮ", "No":"ಇಲ್ಲ", "Partial":"ಭಾಗಶಃ", "Yes":"ಹೌದು", "Shared":"ಹಂಚಿಕೆ", "Available":"ಲಭ್ಯ", "Reliable":"ವಿಶ್ವಾಸಾರ್ಹ", "Rain-fed":"ಮಳೆ ಆಧಾರಿತ", "Limited":"ಸೀಮಿತ", "Beginner":"ಆರಂಭಿಕ", "Some experience":"ಸ್ವಲ್ಪ ಅನುಭವ", "Experienced":"ಅನುಭವ ಹೊಂದಿರುವವರು", "Within 3 months":"3 ತಿಂಗಳೊಳಗೆ", "3–6 months":"3–6 ತಿಂಗಳು", "6–12 months":"6–12 ತಿಂಗಳು", "12+ months":"12+ ತಿಂಗಳು",
        "Weather variability":"ಹವಾಮಾನ ಬದಲಾವಣೆ", "Water availability":"ನೀರಿನ ಲಭ್ಯತೆ", "Input-price changes":"ಇನ್‌ಪುಟ್ ಬೆಲೆ ಬದಲಾವಣೆ", "Crop-price changes":"ಬೆಳೆ ಬೆಲೆ ಬದಲಾವಣೆ", "Pest/disease pressure":"ಕೀಟ/ರೋಗದ ಒತ್ತಡ", "Price fluctuations":"ಬೆಲೆ ಏರಿಳಿತ", "Water stress":"ನೀರಿನ ಒತ್ತಡ", "Market-price changes":"ಮಾರುಕಟ್ಟೆ ಬೆಲೆ ಬದಲಾವಣೆ", "Market-price variation":"ಮಾರುಕಟ್ಟೆ ಬೆಲೆ ವ್ಯತ್ಯಾಸ", "Post-harvest loss":"ಕೊಯ್ಲಿನ ನಂತರದ ನಷ್ಟ",
    }
}
for _lang,_map in BUSINESS_DISPLAY_TR.items():
    TEXT[_lang].update(_map)


# Additional dynamic-screen translations.
DYNAMIC_TR = {
 "Hindi": {
  "High Risk":"उच्च जोखिम","Medium Risk":"मध्यम जोखिम","Low Risk":"कम जोखिम","item(s)":"आइटम", "identified":"पहचाने गए",
  "Risk distribution is recalculated from the selected business and the current inputs.":"जोखिम वितरण चुने गए व्यवसाय और वर्तमान जानकारी के आधार पर फिर से गणना किया जाता है।",
  "HIGH RISK":"उच्च जोखिम","MEDIUM RISK":"मध्यम जोखिम","LOW RISK":"कम जोखिम", "Risk":"जोखिम","Level":"स्तर","Impact":"प्रभाव","Control / mitigation":"नियंत्रण / समाधान","Priority gaps":"प्राथमिकता अंतराल","Gap":"अंतराल","Action":"कार्रवाई",
  "No risk rules were triggered for the current business profile. Continue routine monitoring before scaling.":"वर्तमान व्यवसाय प्रोफ़ाइल के लिए कोई जोखिम नियम सक्रिय नहीं हुआ। विस्तार से पहले नियमित निगरानी जारी रखें।",
  "No configured risk items were returned for this activity.":"इस गतिविधि के लिए कोई कॉन्फ़िगर किया गया जोखिम नहीं मिला।",
  "Biological, climatic and operational risks should be actively managed before scaling.":"विस्तार से पहले जैविक, जलवायु और संचालन संबंधी जोखिमों का सक्रिय प्रबंधन करें।",
  "Species / Variety / Product Selection":"प्रजाति / किस्म / उत्पाद चयन","Execution Roadmap":"कार्यान्वयन रोडमैप","Market & Advisory":"बाज़ार और मार्गदर्शन","Risk Control":"जोखिम नियंत्रण","Financial Benchmarks":"वित्तीय मानदंड","Schemes":"योजनाएँ",
  "CAPEX Required":"आवश्यक CAPEX","Break-Even Timeline":"ब्रेक-ईवन समयसीमा","Feasibility Score":"व्यवहार्यता स्कोर","Monthly Operating Cost":"मासिक संचालन लागत",
  "Current input / configured estimate":"वर्तमान जानकारी / कॉन्फ़िगर किया गया अनुमान","Indicative model estimate":"संकेतात्मक मॉडल अनुमान","Adaptive score from available inputs":"उपलब्ध जानकारी से अनुकूलित स्कोर","Indicative, scale-dependent":"संकेतात्मक, पैमाने पर निर्भर",
  "Selection":"चयन","Market & Advisory":"बाज़ार और मार्गदर्शन","Risk Control":"जोखिम नियंत्रण","Financial Benchmarks":"वित्तीय मानदंड",
  "Strategic fit: combine at least one B2B route with a direct or diversified selling channel where the business model allows it.":"रणनीतिक मेल: जहाँ व्यवसाय मॉडल अनुमति देता है, वहाँ कम से कम एक B2B मार्ग को प्रत्यक्ष या विविध बिक्री चैनल के साथ जोड़ें।",
  "Biological, climatic and operational risks should be actively managed before scaling.":"विस्तार से पहले जैविक, जलवायु और संचालन संबंधी जोखिमों का सक्रिय प्रबंधन करें।",
  "Success benchmark: complete a pilot with recorded unit cost, output/service volume, realized selling price, wastage/mortality where relevant, and customer acquisition cost before expanding.":"सफलता मानदंड: विस्तार से पहले दर्ज इकाई लागत, उत्पादन/सेवा मात्रा, वास्तविक बिक्री मूल्य, जहाँ लागू हो वहाँ बर्बादी/मृत्यु दर और ग्राहक प्राप्ति लागत के साथ पायलट पूरा करें।",
  "Practical Decision Check":"व्यावहारिक निर्णय जाँच","Several currently entered conditions support feasibility. Validate supplier quotes, operating costs and buyer demand before scaling.":"वर्तमान में दर्ज कई स्थितियाँ व्यवहार्यता का समर्थन करती हैं। विस्तार से पहले आपूर्तिकर्ता दर, संचालन लागत और खरीदार मांग सत्यापित करें।",
  "The current assessment is mixed. Close the highest-impact gaps and test a smaller pilot before committing the full investment.":"वर्तमान आकलन मिश्रित है। सबसे अधिक प्रभाव वाले अंतराल बंद करें और पूरी पूंजी लगाने से पहले छोटा पायलट करें।",
  "Several configured conditions are weak. Address the highest-impact gaps first and reassess before committing the full investment.":"कई कॉन्फ़िगर की गई स्थितियाँ कमजोर हैं। पहले सबसे अधिक प्रभाव वाले अंतराल सुधारें और पूरी पूंजी लगाने से पहले पुनः आकलन करें।",
  "High potential impact":"उच्च संभावित प्रभाव","Moderate potential impact":"मध्यम संभावित प्रभाव","Lower potential impact":"कम संभावित प्रभाव","Potential impact":"संभावित प्रभाव",
 },
 "Kannada": {
  "High Risk":"ಹೆಚ್ಚಿನ ಅಪಾಯ","Medium Risk":"ಮಧ್ಯಮ ಅಪಾಯ","Low Risk":"ಕಡಿಮೆ ಅಪಾಯ","item(s)":"ಅಂಶಗಳು","identified":"ಗುರುತಿಸಲಾಗಿದೆ",
  "Risk distribution is recalculated from the selected business and the current inputs.":"ಅಪಾಯ ವಿತರಣೆ ಆಯ್ಕೆ ಮಾಡಿದ ವ್ಯವಹಾರ ಮತ್ತು ಪ್ರಸ್ತುತ ಮಾಹಿತಿಯ ಆಧಾರದ ಮೇಲೆ ಮರುಗಣಿಸಲಾಗುತ್ತದೆ.",
  "HIGH RISK":"ಹೆಚ್ಚಿನ ಅಪಾಯ","MEDIUM RISK":"ಮಧ್ಯಮ ಅಪಾಯ","LOW RISK":"ಕಡಿಮೆ ಅಪಾಯ","Risk":"ಅಪಾಯ","Level":"ಮಟ್ಟ","Impact":"ಪರಿಣಾಮ","Control / mitigation":"ನಿಯಂತ್ರಣ / ಪರಿಹಾರ","Priority gaps":"ಆದ್ಯತಾ ಅಂತರಗಳು","Gap":"ಅಂತರ","Action":"ಕ್ರಮ",
  "No risk rules were triggered for the current business profile. Continue routine monitoring before scaling.":"ಪ್ರಸ್ತುತ ವ್ಯವಹಾರ ಪ್ರೊಫೈಲ್‌ಗೆ ಯಾವುದೇ ಅಪಾಯ ನಿಯಮಗಳು ಸಕ್ರಿಯವಾಗಿಲ್ಲ. ವಿಸ್ತರಣೆಗೆ ಮೊದಲು ನಿಯಮಿತ ಮೇಲ್ವಿಚಾರಣೆ ಮುಂದುವರಿಸಿ.",
  "No configured risk items were returned for this activity.":"ಈ ಚಟುವಟಿಕೆಗೆ ಯಾವುದೇ ಕಾನ್ಫಿಗರ್ ಮಾಡಿದ ಅಪಾಯ ಅಂಶಗಳು ದೊರೆಯಲಿಲ್ಲ.",
  "Biological, climatic and operational risks should be actively managed before scaling.":"ವಿಸ್ತರಣೆಗೆ ಮೊದಲು ಜೈವಿಕ, ಹವಾಮಾನ ಮತ್ತು ಕಾರ್ಯಾಚರಣಾ ಅಪಾಯಗಳನ್ನು ಸಕ್ರಿಯವಾಗಿ ನಿರ್ವಹಿಸಬೇಕು.",
  "Species / Variety / Product Selection":"ಜಾತಿ / ತಳಿ / ಉತ್ಪನ್ನ ಆಯ್ಕೆ","Execution Roadmap":"ಕಾರ್ಯಗತಗೊಳಿಸುವಿಕೆ ಮಾರ್ಗಸೂಚಿ","Market & Advisory":"ಮಾರುಕಟ್ಟೆ ಮತ್ತು ಮಾರ್ಗದರ್ಶನ","Risk Control":"ಅಪಾಯ ನಿಯಂತ್ರಣ","Financial Benchmarks":"ಹಣಕಾಸು ಮಾನದಂಡಗಳು","Schemes":"ಯೋಜನೆಗಳು",
  "CAPEX Required":"ಅಗತ್ಯ CAPEX","Break-Even Timeline":"ಬ್ರೇಕ್-ಈವನ್ ಸಮಯಪಟ್ಟಿ","Feasibility Score":"ಕಾರ್ಯಸಾಧ್ಯತಾ ಅಂಕ","Monthly Operating Cost":"ಮಾಸಿಕ ಕಾರ್ಯಾಚರಣಾ ವೆಚ್ಚ",
  "Current input / configured estimate":"ಪ್ರಸ್ತುತ ಮಾಹಿತಿ / ಕಾನ್ಫಿಗರ್ ಮಾಡಿದ ಅಂದಾಜು","Indicative model estimate":"ಸೂಚಕ ಮಾದರಿ ಅಂದಾಜು","Adaptive score from available inputs":"ಲಭ್ಯ ಮಾಹಿತಿಯಿಂದ ಹೊಂದಿಕೊಳ್ಳುವ ಅಂಕ","Indicative, scale-dependent":"ಸೂಚಕ, ಪ್ರಮಾಣದ ಮೇಲೆ ಅವಲಂಬಿತ",
  "Selection":"ಆಯ್ಕೆ","Market & Advisory":"ಮಾರುಕಟ್ಟೆ ಮತ್ತು ಮಾರ್ಗದರ್ಶನ","Risk Control":"ಅಪಾಯ ನಿಯಂತ್ರಣ","Financial Benchmarks":"ಹಣಕಾಸು ಮಾನದಂಡಗಳು",
  "Strategic fit: combine at least one B2B route with a direct or diversified selling channel where the business model allows it.":"ತಂತ್ರಾತ್ಮಕ ಹೊಂದಾಣಿಕೆ: ವ್ಯವಹಾರ ಮಾದರಿ ಅನುಮತಿಸಿದಲ್ಲಿ ಕನಿಷ್ಠ ಒಂದು B2B ಮಾರ್ಗವನ್ನು ನೇರ ಅಥವಾ ವೈವಿಧ್ಯಮಯ ಮಾರಾಟ ಚಾನಲ್‌ನೊಂದಿಗೆ ಸಂಯೋಜಿಸಿ.",
  "Biological, climatic and operational risks should be actively managed before scaling.":"ವಿಸ್ತರಣೆಗೆ ಮೊದಲು ಜೈವಿಕ, ಹವಾಮಾನ ಮತ್ತು ಕಾರ್ಯಾಚರಣಾ ಅಪಾಯಗಳನ್ನು ಸಕ್ರಿಯವಾಗಿ ನಿರ್ವಹಿಸಬೇಕು.",
  "Success benchmark: complete a pilot with recorded unit cost, output/service volume, realized selling price, wastage/mortality where relevant, and customer acquisition cost before expanding.":"ಯಶಸ್ಸಿನ ಮಾನದಂಡ: ವಿಸ್ತರಿಸುವ ಮೊದಲು ಘಟಕ ವೆಚ್ಚ, ಉತ್ಪಾದನೆ/ಸೇವಾ ಪ್ರಮಾಣ, ನಿಜವಾದ ಮಾರಾಟ ಬೆಲೆ, ಅನ್ವಯಿಸಿದಲ್ಲಿ ನಷ್ಟ/ಸಾವು ಪ್ರಮಾಣ ಮತ್ತು ಗ್ರಾಹಕ ಗಳಿಕೆ ವೆಚ್ಚವನ್ನು ದಾಖಲಿಸಿದ ಪೈಲಟ್ ಪೂರ್ಣಗೊಳಿಸಿ.",
  "Practical Decision Check":"ಪ್ರಾಯೋಗಿಕ ನಿರ್ಧಾರ ಪರಿಶೀಲನೆ","Several currently entered conditions support feasibility. Validate supplier quotes, operating costs and buyer demand before scaling.":"ಪ್ರಸ್ತುತ ನಮೂದಿಸಿದ ಹಲವು ಪರಿಸ್ಥಿತಿಗಳು ಕಾರ್ಯಸಾಧ್ಯತೆಯನ್ನು ಬೆಂಬಲಿಸುತ್ತವೆ. ವಿಸ್ತರಣೆಗೆ ಮೊದಲು ಪೂರೈಕೆದಾರರ ದರ, ಕಾರ್ಯಾಚರಣಾ ವೆಚ್ಚ ಮತ್ತು ಖರೀದಿದಾರರ ಬೇಡಿಕೆಯನ್ನು ಪರಿಶೀಲಿಸಿ.",
  "The current assessment is mixed. Close the highest-impact gaps and test a smaller pilot before committing the full investment.":"ಪ್ರಸ್ತುತ ಮೌಲ್ಯಮಾಪನ ಮಿಶ್ರವಾಗಿದೆ. ಹೆಚ್ಚಿನ ಪರಿಣಾಮದ ಅಂತರಗಳನ್ನು ಮುಚ್ಚಿ, ಸಂಪೂರ್ಣ ಹೂಡಿಕೆಗೆ ಮೊದಲು ಸಣ್ಣ ಪೈಲಟ್ ಪರೀಕ್ಷಿಸಿ.",
  "Several configured conditions are weak. Address the highest-impact gaps first and reassess before committing the full investment.":"ಹಲವು ಕಾನ್ಫಿಗರ್ ಮಾಡಿದ ಪರಿಸ್ಥಿತಿಗಳು ದುರ್ಬಲವಾಗಿವೆ. ಹೆಚ್ಚಿನ ಪರಿಣಾಮದ ಅಂತರಗಳನ್ನು ಮೊದಲು ಸರಿಪಡಿಸಿ ಮತ್ತು ಸಂಪೂರ್ಣ ಹೂಡಿಕೆಗೆ ಮೊದಲು ಮರುಮೌಲ್ಯಮಾಪನ ಮಾಡಿ.",
  "High potential impact":"ಹೆಚ್ಚಿನ ಸಾಧ್ಯ ಪರಿಣಾಮ","Moderate potential impact":"ಮಧ್ಯಮ ಸಾಧ್ಯ ಪರಿಣಾಮ","Lower potential impact":"ಕಡಿಮೆ ಸಾಧ್ಯ ಪರಿಣಾಮ","Potential impact":"ಸಂಭಾವ್ಯ ಪರಿಣಾಮ",
 }
}
for _lang,_map in DYNAMIC_TR.items():
    TEXT[_lang].update(_map)

FIELD_UI_TR = {
 "Hindi": {
  "Water availability":"पानी की उपलब्धता","Labour":"श्रमिक","Investment":"निवेश","Market access":"बाज़ार तक पहुँच","Experience":"अनुभव","Electricity":"बिजली","Housing/shed":"आवास/शेड","Feed availability":"चारे की उपलब्धता","Veterinary access":"पशु चिकित्सा सहायता","Fodder availability":"चारा उपलब्धता","Grazing/feed availability":"चराई/चारा उपलब्धता",
  "Land area (acres)":"भूमि क्षेत्रफल (एकड़)","Land/covered area (acres)":"भूमि/कवर क्षेत्रफल (एकड़)","Season":"मौसम","Irrigation":"सिंचाई","Soil test available":"मिट्टी परीक्षण उपलब्ध","Available labour (people)":"उपलब्ध श्रमिक (संख्या)","Available investment (₹)":"उपलब्ध निवेश (₹)","Target time to income":"आय प्राप्ति का लक्ष्य समय","Risk preference":"जोखिम प्राथमिकता","Transport available":"परिवहन उपलब्ध","Storage available":"भंडारण उपलब्ध","Can wait for longer establishment period":"लंबी स्थापना अवधि की प्रतीक्षा कर सकते हैं",
  "Number of birds planned":"नियोजित पक्षियों की संख्या","Suitable shed available":"उपयुक्त शेड उपलब्ध","Available shed area (sq ft)":"उपलब्ध शेड क्षेत्र (वर्ग फुट)","Experience":"अनुभव","Veterinary support access":"पशु चिकित्सा सहायता तक पहुँच","Number of animals planned":"नियोजित पशुओं की संख्या","Animal type":"पशु प्रकार","Milking/chilling equipment":"दूध निकालने/ठंडा करने के उपकरण","Milk market access":"दूध बाज़ार तक पहुँच","Number of goats planned":"नियोजित बकरियों की संख्या","Goat shed available":"बकरी शेड उपलब्ध","Grazing/feed availability":"चराई/चारा उपलब्धता","Number of sheep planned":"नियोजित भेड़ों की संख्या","Sheep shed available":"भेड़ शेड उपलब्ध",
 },
 "Kannada": {
  "Water availability":"ನೀರಿನ ಲಭ್ಯತೆ","Labour":"ಕಾರ್ಮಿಕರು","Investment":"ಹೂಡಿಕೆ","Market access":"ಮಾರುಕಟ್ಟೆ ಪ್ರವೇಶ","Experience":"ಅನುಭವ","Electricity":"ವಿದ್ಯುತ್","Housing/shed":"ವಸತಿ/ಶೆಡ್","Feed availability":"ಆಹಾರ ಲಭ್ಯತೆ","Veterinary access":"ಪಶುವೈದ್ಯಕೀಯ ಪ್ರವೇಶ","Fodder availability":"ಮೇವು ಲಭ್ಯತೆ","Grazing/feed availability":"ಮೇಯಿಸುವಿಕೆ/ಮೇವು ಲಭ್ಯತೆ",
  "Land area (acres)":"ಭೂಮಿ ವಿಸ್ತೀರ್ಣ (ಎಕರೆ)","Land/covered area (acres)":"ಭೂಮಿ/ಆವರಿತ ವಿಸ್ತೀರ್ಣ (ಎಕರೆ)","Season":"ಋತು","Irrigation":"ನೀರಾವರಿ","Soil test available":"ಮಣ್ಣು ಪರೀಕ್ಷೆ ಲಭ್ಯ","Available labour (people)":"ಲಭ್ಯವಿರುವ ಕಾರ್ಮಿಕರು (ಸಂಖ್ಯೆ)","Available investment (₹)":"ಲಭ್ಯವಿರುವ ಹೂಡಿಕೆ (₹)","Target time to income":"ಆದಾಯದ ಗುರಿ ಸಮಯ","Risk preference":"ಅಪಾಯ ಆದ್ಯತೆ","Transport available":"ಸಾರಿಗೆ ಲಭ್ಯ","Storage available":"ಸಂಗ್ರಹಣೆ ಲಭ್ಯ","Can wait for longer establishment period":"ದೀರ್ಘ ಸ್ಥಾಪನಾ ಅವಧಿಗಾಗಿ ಕಾಯಬಹುದು",
  "Number of birds planned":"ಯೋಜಿತ ಪಕ್ಷಿಗಳ ಸಂಖ್ಯೆ","Suitable shed available":"ಸೂಕ್ತ ಶೆಡ್ ಲಭ್ಯ","Available shed area (sq ft)":"ಲಭ್ಯವಿರುವ ಶೆಡ್ ವಿಸ್ತೀರ್ಣ (ಚದರ ಅಡಿ)","Veterinary support access":"ಪಶುವೈದ್ಯಕೀಯ ನೆರವು ಪ್ರವೇಶ","Number of animals planned":"ಯೋಜಿತ ಪ್ರಾಣಿಗಳ ಸಂಖ್ಯೆ","Animal type":"ಪ್ರಾಣಿ ಪ್ರಕಾರ","Milking/chilling equipment":"ಹಾಲು ಹೀರುವ/ತಂಪುಗೊಳಿಸುವ ಉಪಕರಣ", "Milk market access":"ಹಾಲು ಮಾರುಕಟ್ಟೆ ಪ್ರವೇಶ","Number of goats planned":"ಯೋಜಿತ ಮೇಕೆಗಳ ಸಂಖ್ಯೆ","Goat shed available":"ಮೇಕೆ ಶೆಡ್ ಲಭ್ಯ","Number of sheep planned":"ಯೋಜಿತ ಕುರಿಗಳ ಸಂಖ್ಯೆ","Sheep shed available":"ಕುರಿ ಶೆಡ್ ಲಭ್ಯ",
 }
}
for _lang,_map in FIELD_UI_TR.items():
    TEXT[_lang].update(_map)


RISK_UI_TR = {
 "Hindi": {
  "Market-access risk":"बाज़ार पहुँच जोखिम","Capital risk":"पूंजी जोखिम","Execution-capital risk":"कार्यान्वयन-पूंजी जोखिम","Experience / execution risk":"अनुभव / कार्यान्वयन जोखिम","Labour-availability risk":"श्रमिक उपलब्धता जोखिम","Water-availability risk":"पानी उपलब्धता जोखिम","Irrigation reliability risk":"सिंचाई विश्वसनीयता जोखिम","Housing risk":"आवास जोखिम","Animal-health risk":"पशु स्वास्थ्य जोखिम","Feed / fodder cost risk":"चारा लागत जोखिम","Disease / mortality risk":"रोग / मृत्यु जोखिम","Post-harvest / transport risk":"कटाई के बाद / परिवहन जोखिम","Storage risk":"भंडारण जोखिम","Soil-information risk":"मिट्टी जानकारी जोखिम","Time-to-income mismatch":"आय-समय असंगति जोखिम","Biological health risk":"जैविक स्वास्थ्य जोखिम","Input-cost risk":"इनपुट लागत जोखिम","Price risk":"कीमत जोखिम","Biological crop risk":"जैविक फसल जोखिम","Climate risk":"जलवायु जोखिम","Water-quality risk":"पानी गुणवत्ता जोखिम","Perishability risk":"शीघ्र खराब होने का जोखिम","Equipment downtime risk":"उपकरण बंद रहने का जोखिम"
 },
 "Kannada": {
  "Market-access risk":"ಮಾರುಕಟ್ಟೆ ಪ್ರವೇಶ ಅಪಾಯ","Capital risk":"ಬಂಡವಾಳ ಅಪಾಯ","Execution-capital risk":"ಕಾರ್ಯಗತಗೊಳಿಸುವಿಕೆ-ಬಂಡವಾಳ ಅಪಾಯ","Experience / execution risk":"ಅನುಭವ / ಕಾರ್ಯಗತಗೊಳಿಸುವಿಕೆ ಅಪಾಯ","Labour-availability risk":"ಕಾರ್ಮಿಕ ಲಭ್ಯತೆ ಅಪಾಯ","Water-availability risk":"ನೀರಿನ ಲಭ್ಯತೆ ಅಪಾಯ","Irrigation reliability risk":"ನೀರಾವರಿ ವಿಶ್ವಾಸಾರ್ಹತೆ ಅಪಾಯ","Housing risk":"ವಸತಿ ಅಪಾಯ","Animal-health risk":"ಪ್ರಾಣಿ ಆರೋಗ್ಯ ಅಪಾಯ","Feed / fodder cost risk":"ಆಹಾರ / ಮೇವು ವೆಚ್ಚದ ಅಪಾಯ","Disease / mortality risk":"ರೋಗ / ಸಾವು ಅಪಾಯ","Post-harvest / transport risk":"ಕೊಯ್ಲಿನ ನಂತರ / ಸಾರಿಗೆ ಅಪಾಯ","Storage risk":"ಸಂಗ್ರಹಣೆ ಅಪಾಯ","Soil-information risk":"ಮಣ್ಣಿನ ಮಾಹಿತಿ ಅಪಾಯ","Time-to-income mismatch":"ಆದಾಯ-ಸಮಯ ಅಸಂಗತತೆ ಅಪಾಯ","Biological health risk":"ಜೈವಿಕ ಆರೋಗ್ಯ ಅಪಾಯ","Input-cost risk":"ಇನ್‌ಪುಟ್ ವೆಚ್ಚದ ಅಪಾಯ","Price risk":"ಬೆಲೆ ಅಪಾಯ","Biological crop risk":"ಜೈವಿಕ ಬೆಳೆ ಅಪಾಯ","Climate risk":"ಹವಾಮಾನ ಅಪಾಯ","Water-quality risk":"ನೀರಿನ ಗುಣಮಟ್ಟದ ಅಪಾಯ","Perishability risk":"ಶೀಘ್ರ ಹಾಳಾಗುವ ಅಪಾಯ","Equipment downtime risk":"ಉಪಕರಣ ಸ್ಥಗಿತ ಅಪಾಯ"
 }
}
for _lang,_map in RISK_UI_TR.items():
    TEXT[_lang].update(_map)

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

AGRI_LOCATION_CROPS = {
    "Bagalkot": ["Jowar", "Cotton", "Sugarcane", "Sunflower", "Grapes"],
    "Ballari": ["Paddy", "Cotton", "Sunflower", "Maize", "Jowar"],
    "Belagavi": ["Sugarcane", "Jowar", "Maize", "Tobacco", "Groundnut"],
    "Bengaluru Rural": ["Ragi", "Vegetables", "Mulberry", "Mango"],
    "Bengaluru Urban": ["Vegetables", "Ragi", "Flowers", "Mulberry"],
    "Bidar": ["Tur", "Soybean", "Sugarcane", "Jowar"],
    "Chamarajanagar": ["Ragi", "Turmeric", "Cotton", "Sugarcane", "Maize"],
    "Chikballapur": ["Ragi", "Groundnut", "Grapes", "Mulberry", "Vegetables"],
    "Chikkamagaluru": ["Coffee", "Pepper", "Cardamom", "Areca nut", "Paddy"],
    "Chitradurga": ["Groundnut", "Maize", "Onion", "Cotton", "Jowar"],
    "Dakshina Kannada": ["Areca nut", "Coconut", "Paddy", "Cashew", "Rubber"],
    "Davanagere": ["Maize", "Cotton", "Areca nut", "Paddy", "Groundnut"],
    "Dharwad": ["Cotton", "Jowar", "Groundnut", "Maize", "Wheat"],
    "Gadag": ["Cotton", "Groundnut", "Jowar", "Chilli", "Sunflower"],
    "Hassan": ["Paddy", "Ragi", "Coffee", "Potato", "Areca nut"],
    "Haveri": ["Cotton", "Maize", "Chilli", "Jowar", "Groundnut"],
    "Kalaburagi": ["Tur", "Jowar", "Cotton", "Sunflower", "Bajra"],
    "Kodagu": ["Coffee", "Pepper", "Cardamom", "Paddy", "Orange"],
    "Kolar": ["Ragi", "Tomato", "Mango", "Groundnut", "Grapes"],
    "Koppal": ["Paddy", "Cotton", "Maize", "Sunflower", "Jowar"],
    "Mandya": ["Sugarcane", "Paddy", "Ragi", "Coconut", "Jowar"],
    "Mysuru": ["Paddy", "Sugarcane", "Ragi", "Tobacco", "Cotton"],
    "Raichur": ["Paddy", "Cotton", "Jowar", "Sunflower", "Groundnut"],
    "Ramanagara": ["Ragi", "Mulberry", "Vegetables", "Maize"],
    "Shivamogga": ["Paddy", "Areca nut", "Sugarcane", "Coconut", "Cotton"],
    "Tumakuru": ["Ragi", "Groundnut", "Coconut", "Areca nut", "Maize"],
    "Udupi": ["Paddy", "Areca nut", "Coconut", "Cashew", "Rubber"],
    "Uttara Kannada": ["Paddy", "Areca nut", "Coconut", "Cashew", "Spices"],
    "Vijayapura": ["Grapes", "Sunflower", "Jowar", "Cotton", "Pomegranate"],
    "Vijayanagara": ["Paddy", "Cotton", "Sunflower", "Maize", "Jowar"],
    "Yadgir": ["Tur", "Cotton", "Paddy", "Jowar", "Sunflower"],
    "Jamkhandi": ["Sugarcane", "Jowar", "Cotton", "Grapes"],
    "Badami": ["Jowar", "Cotton", "Sunflower", "Onion"],
    "Hosapete": ["Paddy", "Banana", "Sugarcane", "Cotton"],
    "Sandur": ["Jowar", "Maize", "Groundnut"],
    "Gokak": ["Sugarcane", "Cotton", "Maize"],
    "Chikkodi": ["Sugarcane", "Tobacco", "Maize"],
    "Athani": ["Sugarcane", "Cotton", "Jowar", "Grapes"],
    "Nelamangala": ["Ragi", "Vegetables", "Coconut"],
    "Devanahalli": ["Grapes", "Mango", "Vegetables"],
    "Doddaballapura": ["Mulberry", "Ragi", "Vegetables"],
    "Anekal": ["Vegetables", "Ragi", "Flowers"],
    "Humnabad": ["Tur", "Sugarcane", "Soybean"],
    "Basavakalyan": ["Jowar", "Tur", "Sugarcane"],
    "Kollegal": ["Cotton", "Turmeric", "Ragi"],
    "Gundlupet": ["Cotton", "Sunflower", "Maize"],
    "Chikballapur Town": ["Grapes", "Mulberry", "Ragi"],
    "Sringeri": ["Coffee", "Areca nut", "Pepper"],
    "Mudigere": ["Coffee", "Cardamom", "Pepper"],
    "Kadur": ["Maize", "Areca nut", "Ragi"],
    "Hiriyur": ["Groundnut", "Onion", "Maize"],
    "Challakere": ["Groundnut", "Jowar", "Onion"],
    "Mangaluru": ["Areca nut", "Coconut", "Cashew", "Paddy"],
    "Puttur": ["Areca nut", "Rubber", "Coconut"],
    "Bantwal": ["Areca nut", "Paddy", "Coconut"],
    "Harihar": ["Areca nut", "Maize", "Cotton"],
    "Channagiri": ["Areca nut", "Maize", "Coconut"],
    "Hubballi": ["Cotton", "Jowar", "Maize"],
    "Kalghatgi": ["Cotton", "Groundnut", "Chilli"],
    "Ron": ["Cotton", "Chilli", "Groundnut"],
    "Sakleshpur": ["Coffee", "Areca nut", "Cardamom", "Paddy"],
    "Arsikere": ["Ragi", "Groundnut", "Potato"],
    "Ranebennur": ["Cotton", "Maize", "Chilli"],
    "Shahapur": ["Tur", "Cotton", "Paddy"],
    "Madikeri": ["Coffee", "Pepper", "Cardamom", "Orange"],
    "Virajpet": ["Coffee", "Pepper", "Paddy"],
    "Malur": ["Ragi", "Tomato", "Mango"],
    "Srinivaspur": ["Mango", "Groundnut", "Ragi"],
    "Gangavati": ["Paddy", "Cotton", "Maize"],
    "Kunigal": ["Ragi", "Coconut", "Groundnut"],
    "Pandavapura": ["Sugarcane", "Paddy", "Coconut"],
    "Srirangapatna": ["Sugarcane", "Paddy", "Ragi"],
    "Hunsur": ["Tobacco", "Paddy", "Cotton"],
    "Nanjangud": ["Paddy", "Sugarcane", "Turmeric"],
    "Manvi": ["Paddy", "Cotton", "Jowar"],
    "Sindhanur": ["Paddy", "Cotton", "Sunflower"],
    "Channapatna": ["Ragi", "Mulberry", "Coconut"],
    "Magadi": ["Ragi", "Groundnut", "Mulberry"],
    "Sagara": ["Areca nut", "Paddy", "Coconut"],
    "Bhadravathi": ["Sugarcane", "Paddy", "Areca nut"],
    "Tiptur": ["Coconut", "Areca nut", "Ragi"],
    "Kundapura": ["Paddy", "Areca nut", "Coconut"],
    "Karkala": ["Areca nut", "Paddy", "Coconut"],
    "Sirsi": ["Areca nut", "Spices", "Paddy"],
    "Karwar": ["Coconut", "Cashew", "Paddy"],
    "Sindagi": ["Jowar", "Grapes", "Sunflower"],
    "Indi": ["Sugarcane", "Grapes", "Jowar"],
}

# -----------------------------
# TOP NAVIGATION (SIDEBAR REMOVED)
# -----------------------------
st.markdown("""
<style>
[data-testid="stSidebar"], [data-testid="collapsedControl"] {
    display:none !important;
}
.block-container, [data-testid="stMainBlockContainer"] {
    max-width:1800px !important;
    width:100% !important;
    padding-left:2rem !important;
    padding-right:2rem !important;
}
div[data-testid="stHorizontalBlock"]:has([data-testid="stRadio"]) {
    position:sticky; top:0; z-index:1000;
    display:flex; align-items:center; gap:18px;
    padding:10px 16px; margin:0 0 22px;
    border-radius:18px;
    background:rgba(255,255,255,.94);
    border:1px solid rgba(46,125,50,.14);
    box-shadow:0 8px 28px rgba(27,94,32,.10);
    backdrop-filter:blur(14px);
}
.gs-global-brand {
    font-size:19px; font-weight:900; color:#2E7D32;
    white-space:nowrap; min-width:175px;
}
div[data-testid="stHorizontalBlock"]:has([data-testid="stRadio"]) .stRadio { margin:0 !important; flex:1; }
div[data-testid="stHorizontalBlock"]:has([data-testid="stRadio"]) .stRadio > label { display:none !important; }
div[data-testid="stHorizontalBlock"]:has([data-testid="stRadio"]) div[role="radiogroup"] {
    display:flex; justify-content:center; gap:4px; flex-wrap:wrap;
}
div[data-testid="stHorizontalBlock"]:has([data-testid="stRadio"]) div[role="radiogroup"] label {
    border-radius:999px !important; padding:7px 11px !important;
    transition:all .2s ease;
}
div[data-testid="stHorizontalBlock"]:has([data-testid="stRadio"]) div[role="radiogroup"] label:hover {
    background:#E8F5E9; transform:translateY(-1px);
}
div[data-testid="stHorizontalBlock"]:has([data-testid="stRadio"]) .stSelectbox { margin:0 !important; min-width:118px; }
div[data-testid="stHorizontalBlock"]:has([data-testid="stRadio"]) .stSelectbox > label { display:none !important; }
@media(max-width:1000px){
    div[data-testid="stHorizontalBlock"]:has([data-testid="stRadio"]){flex-wrap:wrap;}
    .gs-global-brand{min-width:auto;}
    div[data-testid="stHorizontalBlock"]:has([data-testid="stRadio"]) .stRadio{width:100%;order:3;}
}
@media(max-width:650px){
    .block-container, [data-testid="stMainBlockContainer"] {
        padding-left:.7rem !important; padding-right:.7rem !important;
    }
    div[data-testid="stHorizontalBlock"]:has([data-testid="stRadio"]){position:relative;padding:12px;margin-bottom:14px;}
    div[data-testid="stHorizontalBlock"]:has([data-testid="stRadio"]) div[role="radiogroup"]{justify-content:flex-start;overflow-x:auto;flex-wrap:nowrap;padding-bottom:3px;}
}
</style>
""", unsafe_allow_html=True)

LANGUAGE_NAMES = {
    "English": "English",
    "Hindi": "हिंदी",
    "Kannada": "ಕನ್ನಡ"
}

# ------------------------------------------------------------
# LOCATION (TALUKA) -> MANDI DISTRICT
# ------------------------------------------------------------
# The district and taluka chosen in the top navigation bar are used by every
# page. The government mandi dataset is published district-wise, so each
# taluka/town is mapped to the district under which its records are reported.
LOCATION_DISTRICT = {
    "Bagalkot": "Bagalkot", "Jamkhandi": "Bagalkot", "Badami": "Bagalkot",
    "Ballari": "Ballari", "Sandur": "Ballari",
    "Vijayanagara": "Ballari", "Hosapete": "Ballari",
    "Belagavi": "Belagavi", "Gokak": "Belagavi", "Chikkodi": "Belagavi", "Athani": "Belagavi",
    "Bengaluru Rural": "Bengaluru Rural", "Nelamangala": "Bengaluru Rural",
    "Devanahalli": "Bengaluru Rural", "Doddaballapura": "Bengaluru Rural",
    "Bengaluru Urban": "Bengaluru Urban", "Anekal": "Bengaluru Urban", "Bengaluru": "Bengaluru Urban",
    "Bidar": "Bidar", "Humnabad": "Bidar", "Basavakalyan": "Bidar",
    "Chamarajanagar": "Chamarajanagar", "Kollegal": "Chamarajanagar", "Gundlupet": "Chamarajanagar",
    "Chikballapur": "Chikkaballapur", "Chikballapur Town": "Chikkaballapur",
    "Chikkamagaluru": "Chikkamagaluru", "Sringeri": "Chikkamagaluru",
    "Mudigere": "Chikkamagaluru", "Kadur": "Chikkamagaluru",
    "Chitradurga": "Chitradurga", "Hiriyur": "Chitradurga", "Challakere": "Chitradurga",
    "Dakshina Kannada": "Dakshina Kannada", "Mangaluru": "Dakshina Kannada",
    "Puttur": "Dakshina Kannada", "Bantwal": "Dakshina Kannada",
    "Davanagere": "Davanagere", "Harihar": "Davanagere", "Channagiri": "Davanagere",
    "Dharwad": "Dharwad", "Hubballi": "Dharwad", "Kalghatgi": "Dharwad",
    "Gadag": "Gadag", "Ron": "Gadag",
    "Hassan": "Hassan", "Sakleshpur": "Hassan", "Arsikere": "Hassan",
    "Haveri": "Haveri", "Ranebennur": "Haveri",
    "Kalaburagi": "Kalaburagi",
    "Kodagu": "Kodagu", "Madikeri": "Kodagu", "Virajpet": "Kodagu",
    "Kolar": "Kolar", "Malur": "Kolar", "Srinivaspur": "Kolar",
    "Koppal": "Koppal", "Gangavati": "Koppal",
    "Mandya": "Mandya", "Pandavapura": "Mandya", "Srirangapatna": "Mandya",
    "Mysuru": "Mysuru", "Hunsur": "Mysuru", "Nanjangud": "Mysuru",
    "Raichur": "Raichur", "Manvi": "Raichur", "Sindhanur": "Raichur",
    "Ramanagara": "Ramanagara", "Channapatna": "Ramanagara", "Magadi": "Ramanagara",
    "Shivamogga": "Shivamogga", "Sagara": "Shivamogga", "Bhadravathi": "Shivamogga",
    "Tumakuru": "Tumakuru", "Kunigal": "Tumakuru", "Tiptur": "Tumakuru",
    "Udupi": "Udupi", "Kundapura": "Udupi", "Karkala": "Udupi",
    "Uttara Kannada": "Uttara Kannada", "Sirsi": "Uttara Kannada", "Karwar": "Uttara Kannada",
    "Vijayapura": "Vijayapura", "Sindagi": "Vijayapura", "Indi": "Vijayapura",
    "Yadgir": "Yadgir", "Shahapur": "Yadgir",
}

# Older/alternate district spellings still used inside the government dataset.
DISTRICT_ALIASES = {
    "Bengaluru Urban": ["Bengaluru Urban", "Bangalore Urban", "Bangalore"],
    "Bengaluru Rural": ["Bengaluru Rural", "Bangalore Rural"],
    "Belagavi": ["Belagavi", "Belgaum"],
    "Shivamogga": ["Shivamogga", "Shimoga"],
    "Vijayapura": ["Vijayapura", "Bijapur"],
    "Kalaburagi": ["Kalaburagi", "Gulbarga"],
    "Mysuru": ["Mysuru", "Mysore"],
    "Chikkamagaluru": ["Chikkamagaluru", "Chikmagalur"],
    "Chikkaballapur": ["Chikkaballapur", "Chikkaballapura", "Chikballapur"],
    "Dakshina Kannada": ["Dakshina Kannada", "Dakshin Kannada", "Mangalore"],
    "Tumakuru": ["Tumakuru", "Tumkur"],
    "Ballari": ["Ballari", "Bellary", "Vijayanagara"],
    "Chamarajanagar": ["Chamarajanagar", "Chamarajanagara"],
    "Uttara Kannada": ["Uttara Kannada", "Uttar Kannada", "Karwar"],
    "Bagalkot": ["Bagalkot", "Bagalkote"],
    "Davanagere": ["Davanagere", "Davangere"],
}

locations = sorted(AGRI_LOCATION_CROPS.keys())

page_values = ["Home", "Market Prices", "Government Schemes", "Financial Assistant", "Business Recommendation"]
page_labels = {
    "Home": "\U0001F3E0 Home",
    "Market Prices": "\U0001F4C8 Market Prices",
    "Government Schemes": "\U0001F3DB\uFE0F Schemes",
    "Financial Assistant": "\U0001F4B0 Finance",
    "Business Recommendation": "\U0001F4A1 Business"
}

if "language" not in st.session_state:
    st.session_state.language = "English"
if "location" not in st.session_state:
    st.session_state.location = locations[0] if locations else ""
if "page" not in st.session_state:
    st.session_state.page = "Home"

nav_brand, nav_pages, nav_lang, nav_location = st.columns(
    [1.25, 4.8, .85, 1.25], vertical_alignment="center"
)
with nav_brand:
    st.markdown('<div class="gs-global-brand">\U0001F33E Gram Sahayak</div>', unsafe_allow_html=True)
with nav_pages:
    page = st.radio(
        "Navigate",
        page_values,
        index=page_values.index(st.session_state.page),
        format_func=lambda x: page_labels[x],
        horizontal=True,
        key="gs_top_page"
    )
with nav_lang:
    language = st.selectbox(
        "Language",
        ["English", "Hindi", "Kannada"],
        index=["English", "Hindi", "Kannada"].index(st.session_state.language),
        format_func=lambda x: LANGUAGE_NAMES[x],
        label_visibility="collapsed",
        key="gs_top_language"
    )
with nav_location:
    location = st.selectbox(
        "Location",
        locations,
        index=locations.index(st.session_state.location) if st.session_state.location in locations else 0,
        label_visibility="collapsed",
        key="gs_top_location"
    )

# "location" is the single shared value used by every page in the app.
st.session_state.page = page
st.session_state.language = language
st.session_state.location = location

T = TEXT[language]
# ============================================================
# MARKET DATA
# ============================================================

# Demo/sample prices used only for demonstration.
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

# ============================================================
# LOCATION → SUITABLE CROPS
# ============================================================
CROP_LOCATION_SUITABILITY = AGRI_LOCATION_CROPS

def suitable_crops_for_location(loc):
    names = CROP_LOCATION_SUITABILITY.get(loc, [])
    valid = [c for c in names if c in CROP_DATA]
    return valid if valid else list(CROP_DATA.keys())

CROP_CATEGORY_FALLBACK = {"Paddy":"Cereal","Vegetables":"Vegetable","Flowers":"Floriculture","Mulberry":"Commercial","Grapes":"Fruit","Mango":"Fruit","Pomegranate":"Fruit","Orange":"Fruit","Coffee":"Commercial","Pepper":"Spice","Cardamom":"Spice","Areca nut":"Horticulture","Coconut":"Horticulture","Cashew":"Horticulture","Rubber":"Commercial","Tobacco":"Commercial","Spices":"Spice","Potato":"Vegetable"}

def crop_category(crop):
    return CROP_DATA.get(crop, {}).get("category", CROP_CATEGORY_FALLBACK.get(crop, "Other"))

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
        "schemes": ["Kisan Credit Card", "PMEGP", "Agriculture Infrastructure Fund"],
        "success_rate": 65,
        "timeline_months": (4, 8),
        "expected_return_pct": (20, 45),
        "is_crop_based": True,
        "risks": [
            {"category": "Climate", "description": "Erratic rainfall, heat stress or unseasonal rain can damage standing crops.",
             "likelihood": "Medium", "impact": "High",
             "mitigation": "Choose crops matched to local rainfall/water access; consider drip irrigation or mulching where feasible."},
            {"category": "Market", "description": "Vegetable prices can swing sharply within a single season due to oversupply.",
             "likelihood": "High", "impact": "Medium",
             "mitigation": "Sell across more than one channel (mandi, retailers, direct) and avoid growing only one crop."},
            {"category": "Financial", "description": "Input costs (seed, fertiliser, labour) can rise before the harvest is sold.",
             "likelihood": "Medium", "impact": "Medium",
             "mitigation": "Keep a simple cost sheet and a small buffer fund before the first harvest."},
        ],
        "scheme_benefits": {
            "Kisan Credit Card": "Gives access to working-capital credit for seed, fertiliser and irrigation costs each season.",
            "PMEGP": "Can support setup costs if this is structured as a new eligible micro-enterprise.",
            "Agriculture Infrastructure Fund": "Can help finance post-harvest storage or grading facilities to reduce distress selling.",
        },
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
        "schemes": ["PMFME", "MUDRA", "PMEGP"],
        "success_rate": 60,
        "timeline_months": (6, 12),
        "expected_return_pct": (18, 40),
        "is_crop_based": False,
        "risks": [
            {"category": "Operational", "description": "Food safety, hygiene and shelf-life issues can spoil batches or cause customer loss.",
             "likelihood": "Medium", "impact": "High",
             "mitigation": "Follow basic FSSAI hygiene practices and test shelf life before scaling production."},
            {"category": "Market", "description": "Building a reliable customer base for a new packaged product takes time.",
             "likelihood": "High", "impact": "Medium",
             "mitigation": "Start with local haats, retailers and word-of-mouth before wider distribution."},
            {"category": "Financial", "description": "Packaging and raw-material costs can erode thin margins if not tracked closely.",
             "likelihood": "Medium", "impact": "Medium",
             "mitigation": "Cost every batch precisely before setting a selling price."},
        ],
        "scheme_benefits": {
            "PMFME": "Directly targeted at micro food-processing units; may offer credit-linked capital subsidy for eligible individual units.",
            "MUDRA": "Collateral-free credit for equipment, raw material and working capital.",
            "PMEGP": "Useful for setting up a new eligible processing unit with structured project finance.",
        },
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
        "schemes": ["MUDRA", "PMEGP"],
        "success_rate": 70,
        "timeline_months": (3, 6),
        "expected_return_pct": (12, 25),
        "is_crop_based": False,
        "risks": [
            {"category": "Market", "description": "Larger stores or online delivery can undercut prices on fast-moving items.",
             "likelihood": "Medium", "impact": "Medium",
             "mitigation": "Compete on convenience, credit for regulars and personal relationships rather than price alone."},
            {"category": "Operational", "description": "Overstocking slow-moving items ties up working capital.",
             "likelihood": "Medium", "impact": "Medium",
             "mitigation": "Track sales weekly and reorder only fast-moving stock."},
            {"category": "Financial", "description": "Informal credit sales to regular customers can strain cash flow.",
             "likelihood": "Medium", "impact": "Medium",
             "mitigation": "Set a clear credit limit per customer and record it consistently."},
        ],
        "scheme_benefits": {
            "MUDRA": "Working-capital loan to stock inventory and manage day-to-day cash flow.",
            "PMEGP": "Can support initial shop setup if structured as a new eligible enterprise.",
        },
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
        "schemes": ["PM SVANidhi", "MUDRA", "PMEGP"],
        "success_rate": 62,
        "timeline_months": (2, 5),
        "expected_return_pct": (20, 50),
        "is_crop_based": False,
        "risks": [
            {"category": "Operational", "description": "Location and footfall drive most of the demand; a poor spot can sink an otherwise good menu.",
             "likelihood": "High", "impact": "High",
             "mitigation": "Test 2–3 candidate locations at different times before committing to one."},
            {"category": "Market", "description": "Daily demand can vary a lot with weather, local events and competition.",
             "likelihood": "High", "impact": "Medium",
             "mitigation": "Keep the menu flexible and prepare quantities based on recent daily sales, not guesses."},
            {"category": "Financial", "description": "Perishable ingredients can lead to daily wastage if overordered.",
             "likelihood": "Medium", "impact": "Medium",
             "mitigation": "Buy small quantities frequently rather than bulk, especially when starting out."},
        ],
        "scheme_benefits": {
            "PM SVANidhi": "Designed specifically for street vendors; provides progressive working-capital loan tranches.",
            "MUDRA": "Can fund a cart, cooking equipment or initial stock.",
            "PMEGP": "An option if this is scaled into a larger structured food outlet.",
        },
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
        "schemes": ["MUDRA", "Kisan Credit Card", "PMEGP"],
        "success_rate": 68,
        "timeline_months": (6, 10),
        "expected_return_pct": (15, 30),
        "is_crop_based": False,
        "risks": [
            {"category": "Climate", "description": "Heat stress and fodder shortage in dry spells can reduce milk yield.",
             "likelihood": "Medium", "impact": "Medium",
             "mitigation": "Plan a fodder reserve or fodder-crop backup before peak summer."},
            {"category": "Operational", "description": "Animal illness can sharply cut yield or require costly treatment.",
             "likelihood": "Medium", "impact": "High",
             "mitigation": "Keep a vaccination schedule and access to a local veterinarian."},
            {"category": "Market", "description": "Milk procurement prices can change with season and buyer negotiation power.",
             "likelihood": "Medium", "impact": "Medium",
             "mitigation": "Explore a cooperative or multiple buyers instead of one, and consider value-added products like curd or ghee."},
        ],
        "scheme_benefits": {
            "MUDRA": "Can finance cattle purchase, shelter or equipment.",
            "Kisan Credit Card": "Working-capital support for fodder and allied dairy costs.",
            "PMEGP": "An option for a larger structured dairy micro-enterprise.",
        },
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
        "schemes": ["MUDRA", "Kisan Credit Card", "PMEGP"],
        "success_rate": 64,
        "timeline_months": (8, 14),
        "expected_return_pct": (20, 40),
        "is_crop_based": False,
        "risks": [
            {"category": "Operational", "description": "Disease can spread quickly through a herd if not monitored.",
             "likelihood": "Medium", "impact": "High",
             "mitigation": "Regular vaccination and isolating new/sick animals before mixing with the herd."},
            {"category": "Climate", "description": "Fodder and water shortage in dry seasons raises feeding costs.",
             "likelihood": "Medium", "impact": "Medium",
             "mitigation": "Plan fodder storage ahead of the dry season."},
            {"category": "Market", "description": "Livestock prices fluctuate with festival demand and local supply.",
             "likelihood": "Medium", "impact": "Medium",
             "mitigation": "Time sales around known demand peaks (festivals) where possible."},
        ],
        "scheme_benefits": {
            "MUDRA": "Can finance purchase of animals and shelter construction.",
            "Kisan Credit Card": "Supports allied agricultural working-capital needs including feed costs.",
            "PMEGP": "An option for a larger structured livestock enterprise.",
        },
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
        "schemes": ["MUDRA", "Kisan Credit Card", "PMEGP"],
        "success_rate": 60,
        "timeline_months": (4, 8),
        "expected_return_pct": (15, 35),
        "is_crop_based": False,
        "risks": [
            {"category": "Operational", "description": "Disease outbreaks (e.g. avian illnesses) can wipe out a flock quickly.",
             "likelihood": "Medium", "impact": "High",
             "mitigation": "Follow biosecurity basics: limit outside visitors, disinfect equipment, isolate sick birds fast."},
            {"category": "Financial", "description": "Feed costs are usually the largest ongoing expense and can rise unexpectedly.",
             "likelihood": "High", "impact": "Medium",
             "mitigation": "Track feed-cost-per-bird and consider bulk-buying feed with neighbouring farmers."},
            {"category": "Market", "description": "Egg/broiler prices can be volatile around festivals and oversupply periods.",
             "likelihood": "Medium", "impact": "Medium",
             "mitigation": "Build relationships with more than one buyer to avoid price dependence on one channel."},
        ],
        "scheme_benefits": {
            "MUDRA": "Can finance shelter, equipment and initial birds/feed.",
            "Kisan Credit Card": "Supports allied agricultural working-capital needs.",
            "PMEGP": "An option for a larger structured poultry enterprise.",
        },
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
        "schemes": ["MUDRA", "PMEGP"],
        "success_rate": 66,
        "timeline_months": (2, 4),
        "expected_return_pct": (15, 30),
        "is_crop_based": False,
        "risks": [
            {"category": "Financial", "description": "Fuel price rises directly cut into thin per-delivery margins.",
             "likelihood": "High", "impact": "Medium",
             "mitigation": "Price deliveries to account for fuel, and bundle multiple orders per trip."},
            {"category": "Operational", "description": "Vehicle breakdown halts income until repaired.",
             "likelihood": "Medium", "impact": "Medium",
             "mitigation": "Keep a basic maintenance schedule and a small repair-fund buffer."},
            {"category": "Market", "description": "Low route density in sparsely populated areas can mean too few orders per trip.",
             "likelihood": "Medium", "impact": "Medium",
             "mitigation": "Map demand carefully before committing to a service radius."},
        ],
        "scheme_benefits": {
            "MUDRA": "Can finance a two-wheeler/vehicle or working capital for fuel and upkeep.",
            "PMEGP": "An option if scaled into a larger structured logistics micro-enterprise.",
        },
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
        "schemes": ["PM Vishwakarma", "MUDRA", "PMEGP"],
        "success_rate": 72,
        "timeline_months": (3, 6),
        "expected_return_pct": (15, 30),
        "is_crop_based": False,
        "risks": [
            {"category": "Market", "description": "Competition from ready-made garments can reduce demand for custom stitching.",
             "likelihood": "Medium", "impact": "Medium",
             "mitigation": "Focus on alterations, school uniforms and traditional wear where custom work still wins."},
            {"category": "Operational", "description": "Seasonal demand spikes (festivals, school years) can overload capacity.",
             "likelihood": "Medium", "impact": "Low",
             "mitigation": "Take advance bookings and set realistic delivery timelines during peak seasons."},
            {"category": "Financial", "description": "Machine repair or upgrade costs can be an unplanned expense.",
             "likelihood": "Low", "impact": "Medium",
             "mitigation": "Set aside a small maintenance fund from monthly earnings."},
        ],
        "scheme_benefits": {
            "PM Vishwakarma": "Aimed at traditional artisans/craftspeople; may offer toolkit support and skill development.",
            "MUDRA": "Can finance a sewing machine or workspace setup.",
            "PMEGP": "An option for a larger structured tailoring unit.",
        },
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
        "schemes": ["PM Vishwakarma", "PMEGP", "MUDRA"],
        "success_rate": 55,
        "timeline_months": (6, 12),
        "expected_return_pct": (10, 30),
        "is_crop_based": False,
        "risks": [
            {"category": "Market", "description": "Discovering steady buyers for handmade products can take longer than expected.",
             "likelihood": "High", "impact": "Medium",
             "mitigation": "Test small batches at local fairs and online marketplaces before scaling production."},
            {"category": "Operational", "description": "Order volumes are often inconsistent month to month.",
             "likelihood": "High", "impact": "Medium",
             "mitigation": "Keep costs low and flexible until a repeatable sales channel is found."},
            {"category": "Financial", "description": "Raw material costs can vary, affecting margins on fixed-price products.",
             "likelihood": "Low", "impact": "Low",
             "mitigation": "Review pricing periodically against current material costs."},
        ],
        "scheme_benefits": {
            "PM Vishwakarma": "Directly aimed at traditional artisans; may offer recognition, training and toolkit support.",
            "PMEGP": "Can support setup costs for a new eligible craft micro-enterprise.",
            "MUDRA": "Working-capital credit for raw materials and small-scale production.",
        },
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
        "schemes": ["ACABC", "MUDRA", "PMEGP"],
        "success_rate": 63,
        "timeline_months": (6, 12),
        "expected_return_pct": (12, 25),
        "is_crop_based": False,
        "risks": [
            {"category": "Market", "description": "Demand is closely tied to the local farming season and crop choices.",
             "likelihood": "Medium", "impact": "Medium",
             "mitigation": "Stock a mix of inputs matched to what nearby farmers actually grow."},
            {"category": "Financial", "description": "Carrying too much inventory ties up capital in a seasonal business.",
             "likelihood": "Medium", "impact": "Medium",
             "mitigation": "Stock fast-moving inputs first and reorder based on observed demand."},
            {"category": "Operational", "description": "Licensing and quality-compliance requirements can be a barrier to entry.",
             "likelihood": "Low", "impact": "Medium",
             "mitigation": "Confirm all applicable licences before stocking regulated inputs."},
        ],
        "scheme_benefits": {
            "ACABC": "Specifically supports agri-advisory and agri-business centres with training-linked assistance.",
            "MUDRA": "Working-capital credit for stock and shop setup.",
            "PMEGP": "An option for a larger structured agri-service centre.",
        },
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
        "schemes": ["MUDRA", "PMEGP"],
        "success_rate": 68,
        "timeline_months": (3, 6),
        "expected_return_pct": (15, 30),
        "is_crop_based": False,
        "risks": [
            {"category": "Operational", "description": "Skill gaps for newer device types can limit the jobs you can take on.",
             "likelihood": "Medium", "impact": "Medium",
             "mitigation": "Start with one repair category you know well and expand skills gradually."},
            {"category": "Financial", "description": "Spare-part availability and cost can delay jobs and squeeze margins.",
             "likelihood": "Medium", "impact": "Medium",
             "mitigation": "Keep commonly needed parts in stock and build a reliable supplier relationship."},
            {"category": "Market", "description": "Trust takes time to build in a new repair business.",
             "likelihood": "Medium", "impact": "Low",
             "mitigation": "Transparent pricing and honest turnaround estimates build repeat customers."},
        ],
        "scheme_benefits": {
            "MUDRA": "Can finance tools, spare parts inventory and workspace setup.",
            "PMEGP": "An option for a larger structured repair/service centre.",
        },
    },
]

# ============================================================
# GOVERNMENT SCHEMES
# ============================================================


# User-provided government scheme dataset. These records are normalized into the
# existing SCHEMES structure below so the current Government Schemes UI can use
# the richer target/benefit/conditions/documents/source/category metadata.
GOVT_SCHEMES_DATA = [
    {
        "name": "PM-KISAN (Pradhan Mantri Kisan Samman Nidhi)",
        "target": "Small and marginal farmer families possessing cultivable land.",
        "benefit": "Direct income support of ₹6,000 per year in three equal instalments of ₹2,000.",
        "key_conditions": "Subject to exclusion criteria such as high-income status, institutional landholders, and taxpayers.",
        "documents": "Aadhaar, Bank account details, Land record documents.",
        "source_url": "https://pmkisan.gov.in/",
        "categories": ["Agriculture", "Farmers"],
        "beneficiary_types": ["Individual Farmer", "Small/Marginal Farmer"],
        "business_stages": ["Existing Business", "New Business"],
        "funding_min": 0,
        "funding_max": 10000,
        "keywords": ["farmer", "income", "direct benefit", "agriculture", "land"]
    },
    {
        "name": "Kisan Credit Card (KCC)",
        "target": "Farmers, individual/joint borrowers, tenant farmers, SHGs, and JLGs.",
        "benefit": "Concessional short-term crop loans and working capital for agriculture, dairy, and fisheries.",
        "key_conditions": "Interest subvention available for prompt repayment as per RBI/NABARD guidelines.",
        "documents": "Identity proof, Address proof, Land documents, Crop details.",
        "source_url": "https://www.myscheme.gov.in/schemes/kcc",
        "categories": ["Agriculture", "Allied Activity", "Livestock", "Dairy"],
        "beneficiary_types": ["Individual Farmer", "SHG/Group", "Tenant Farmer"],
        "business_stages": ["Existing Business", "New Business"],
        "funding_min": 10000,
        "funding_max": 300000,
        "keywords": ["loan", "credit", "crop loan", "working capital", "dairy", "kcc"]
    },
    {
        "name": "PM MUDRA Yojana (PMMY)",
        "target": "Non-corporate, non-farm small/micro enterprises in retail, manufacturing, services, and allied agriculture.",
        "benefit": "Collateral-free loans up to ₹10 lakh under Shishu, Kishore, and Tarun categories.",
        "key_conditions": "Loans offered by commercial banks, RRBs, MFIs, and NBFCs based on business viability.",
        "documents": "Business plan, ID proof, Address proof, Bank statements, Equipment quotations.",
        "source_url": "https://www.mudra.org.in/",
        "categories": ["Business Activity", "Retail", "Services", "Food Processing", "Allied Activity"],
        "beneficiary_types": ["Individual Entrepreneur", "Micro-enterprise", "SHG/Group"],
        "business_stages": ["New Business", "Existing Business"],
        "funding_min": 10000,
        "funding_max": 1000000,
        "keywords": ["loan", "mudra", "business", "retail", "shop", "micro enterprise", "credit"]
    },
    {
        "name": "PMEGP (Prime Minister's Employment Generation Programme)",
        "target": "Individuals above 18 years, SHGs, Institutions, and Cooperatives establishing new micro-enterprises.",
        "benefit": "Margin money subsidy ranging from 15% to 35% on eligible project costs.",
        "key_conditions": "Applicable for setting up new micro-enterprises only. Beneficiary contribution is required.",
        "documents": "Project report, ID proof, Caste/Category certificate if applicable, Educational qualification certificate.",
        "source_url": "https://www.kviconline.gov.in/pmegpeportal/",
        "categories": ["Business Activity", "Manufacturing", "Services", "Artisan"],
        "beneficiary_types": ["Individual Entrepreneur", "SHG/Group", "Cooperative"],
        "business_stages": ["New Business"],
        "funding_min": 100000,
        "funding_max": 5000000,
        "keywords": ["subsidy", "pmegp", "new unit", "manufacturing", "service", "kvic", "setup"]
    },
    {
        "name": "PMFME (PM Formalisation of Micro Food Processing Enterprises)",
        "target": "Individual micro food processors, FPOs, SHGs, and Producer Cooperatives.",
        "benefit": "Credit-linked capital subsidy at 35% of eligible project cost up to ₹10 lakh per unit.",
        "key_conditions": "Focuses on food processing, ODOP approach, quality standards, and formalisation.",
        "documents": "ID proof, Business registration/license, FSSAI registration or application, Project report.",
        "source_url": "https://pmfme.mofpi.gov.in/",
        "categories": ["Food Processing", "Business Activity", "Agriculture"],
        "beneficiary_types": ["Individual Entrepreneur", "SHG/Group", "FPO", "Cooperative"],
        "business_stages": ["Existing Business", "New Business"],
        "funding_min": 50000,
        "funding_max": 1000000,
        "keywords": ["food processing", "odop", "pickle", "flour", "snack", "subsidy", "fssai"]
    },
    {
        "name": "PM Vishwakarma Scheme",
        "target": "Artisans and craftspeople working with hands and tools in traditional trades.",
        "benefit": "Skill training, toolkit incentive up to ₹15,000, and collateral-free loan support.",
        "key_conditions": "Applicant must be engaged in an eligible traditional craft trade.",
        "documents": "Aadhaar, Mobile number, Bank details, Ration card / Skill certificate.",
        "source_url": "https://pmvishwakarma.gov.in/",
        "categories": ["Artisan", "Handicrafts", "Services"],
        "beneficiary_types": ["Individual Artisan", "Individual Entrepreneur"],
        "business_stages": ["Existing Business", "New Business"],
        "funding_min": 15000,
        "funding_max": 300000,
        "keywords": ["artisan", "handicraft", "craft", "tailor", "carpenter", "blacksmith", "tools"]
    },
    {
        "name": "Agriculture Infrastructure Fund (AIF)",
        "target": "FPOs, Agriculture Entrepreneurs, Cooperatives, PACS and eligible infrastructure projects.",
        "benefit": "Interest subvention and credit guarantee support for eligible agricultural infrastructure projects.",
        "key_conditions": "For creation of post-harvest management infrastructure and community farming assets.",
        "documents": "DPR, Land details, KYC, Bank application.",
        "source_url": "https://agriinfra.dac.gov.in/",
        "categories": ["Agriculture", "Allied Activity", "Infrastructure"],
        "beneficiary_types": ["FPO", "SHG/Group", "Individual Entrepreneur", "Cooperative"],
        "business_stages": ["New Business", "Existing Business"],
        "funding_min": 200000,
        "funding_max": 20000000,
        "keywords": ["warehouse", "storage", "cold storage", "infrastructure", "fpo", "aif", "agri"]
    }
]


# Additional related government programmes / portals verified against official Government
# sources. These use the same schema so they automatically appear in the filters/table.
GOVT_SCHEMES_DATA.extend([
    {
        "name": "Pradhan Mantri Fasal Bima Yojana (PMFBY)",
        "target": "Farmers seeking crop insurance coverage for notified crops and areas.",
        "benefit": "Crop insurance protection against specified crop losses under the notified scheme terms.",
        "key_conditions": "Coverage, crops, areas, premium and claim conditions depend on the applicable season and state notification.",
        "documents": "Aadhaar/ID, bank details, land or cultivation details, crop details and applicable insurance documents.",
        "source_url": "https://pmfby.gov.in/",
        "categories": ["Agriculture", "Crop Insurance", "Farmers"],
        "beneficiary_types": ["Individual Farmer", "Small/Marginal Farmer", "Tenant Farmer"],
        "business_stages": ["Existing Business", "New Business"],
        "funding_min": 0,
        "funding_max": 1000000,
        "keywords": ["crop insurance", "insurance", "pmfby", "crop loss", "farmer"]
    },
    {
        "name": "PMKSY – Per Drop More Crop (Micro Irrigation)",
        "target": "Farmers and eligible agricultural beneficiaries adopting micro-irrigation such as drip and sprinkler systems.",
        "benefit": "Supports adoption of micro-irrigation to improve water-use efficiency and crop productivity, subject to applicable assistance rules.",
        "key_conditions": "Assistance and implementation are subject to applicable state/district plans, guidelines and beneficiary conditions.",
        "documents": "Identity proof, land/cultivation details, bank details and documents required by the implementing authority.",
        "source_url": "https://pmksy.gov.in/",
        "categories": ["Agriculture", "Irrigation", "Water Management"],
        "beneficiary_types": ["Individual Farmer", "Small/Marginal Farmer", "FPO", "Cooperative"],
        "business_stages": ["Existing Business", "New Business"],
        "funding_min": 10000,
        "funding_max": 1000000,
        "keywords": ["drip", "sprinkler", "irrigation", "water", "micro irrigation", "pmksy"]
    },
    {
        "name": "Soil Health Card / Soil Health & Fertility",
        "target": "Farmers who need soil nutrient assessment and fertilizer/soil-amendment recommendations.",
        "benefit": "Provides soil nutrient status and recommendations for appropriate fertilizer and soil amendments.",
        "key_conditions": "Implementation is through government/state agriculture systems and soil testing facilities.",
        "documents": "Farm/plot details, location, crop information and sample-related details as required by the soil testing system.",
        "source_url": "https://soilhealth.dac.gov.in/",
        "categories": ["Agriculture", "Soil Health", "Farm Advisory"],
        "beneficiary_types": ["Individual Farmer", "Small/Marginal Farmer", "FPO", "Cooperative"],
        "business_stages": ["Existing Business", "New Business"],
        "funding_min": 0,
        "funding_max": 100000,
        "keywords": ["soil", "soil health", "soil test", "fertilizer", "nutrients", "ph", "npk"]
    },
    {
        "name": "e-NAM (National Agriculture Market)",
        "target": "Farmers, traders, FPOs and other eligible participants using integrated agricultural markets.",
        "benefit": "Electronic trading platform connecting APMC markets and supporting transparent price discovery and online agricultural trade.",
        "key_conditions": "Registration, market participation and trading are subject to applicable e-NAM/APMC and state requirements.",
        "documents": "Registration and market-specific documents as required by the relevant e-NAM/APMC process.",
        "source_url": "https://enam.gov.in/",
        "categories": ["Agriculture", "Market Access", "Trading", "FPO"],
        "beneficiary_types": ["Individual Farmer", "FPO", "Individual Entrepreneur", "Cooperative"],
        "business_stages": ["Existing Business", "New Business"],
        "funding_min": 0,
        "funding_max": 0,
        "keywords": ["enam", "e-nam", "mandi", "market", "trading", "price discovery", "fpo"]
    },
])


GOVT_SCHEMES_DATA.extend([
    {
        "name": "National Livestock Mission (NLM)",
        "target": "Eligible entrepreneurs, farmers, FPOs, SHGs and other eligible entities in poultry, sheep, goat, piggery, and feed/fodder activities.",
        "benefit": "Supports entrepreneurship and breed-development activities in rural poultry, sheep, goat and piggery, along with feed and fodder activities, subject to applicable guidelines.",
        "key_conditions": "Activity, beneficiary type, project structure and assistance are governed by the current NLM guidelines and implementing process.",
        "documents": "Identity/KYC documents, land or project details, bank details, project proposal/DPR and other documents required by the implementing authority.",
        "source_url": "https://dahd.gov.in/schemes/programmes/national_livestock_mission",
        "categories": ["Poultry", "Livestock", "Goat", "Sheep", "Piggery", "Feed & Fodder"],
        "beneficiary_types": ["Individual Farmer", "Individual Entrepreneur", "FPO", "SHG/Group"],
        "business_stages": ["New Business", "Existing Business"],
        "funding_min": 50000,
        "funding_max": 10000000,
        "keywords": ["poultry", "chicken", "goat", "sheep", "pig", "piggery", "livestock", "fodder", "feed", "nlm"]
    },
    {
        "name": "Animal Husbandry Infrastructure Development Fund (AHIDF)",
        "target": "Eligible entrepreneurs, MSMEs, FPOs, private companies, Section 8 companies and dairy cooperatives working on animal-husbandry infrastructure.",
        "benefit": "Supports eligible investments in dairy/meat processing, animal feed, breed improvement, veterinary facilities and animal-waste-to-wealth infrastructure under applicable guidelines.",
        "key_conditions": "Eligibility, project categories, financing and current availability must be verified against the latest AHIDF guidelines and implementing authority.",
        "documents": "DPR/project proposal, KYC, business/entity documents, land/project details, bank documents and other lender/department requirements.",
        "source_url": "https://www.dahd.gov.in/schemes/programmes/ahidf",
        "categories": ["Dairy", "Livestock", "Poultry", "Meat Processing", "Animal Feed", "Infrastructure"],
        "beneficiary_types": ["Individual Entrepreneur", "Micro-enterprise", "FPO", "Cooperative"],
        "business_stages": ["New Business", "Existing Business"],
        "funding_min": 500000,
        "funding_max": 100000000,
        "keywords": ["ahidf", "dairy processing", "milk", "meat processing", "animal feed", "poultry feed", "veterinary", "waste to wealth"]
    },
    {
        "name": "Credit Guarantee Scheme through CGTMSE", 
        "target": "Eligible micro and small enterprises seeking institutional credit where credit guarantee support is applicable.",
        "benefit": "Credit guarantee support to eligible lending institutions for qualifying MSE credit facilities, helping improve access to institutional finance.",
        "key_conditions": "Guarantee coverage, eligible borrower, lender, credit facility and applicable limits depend on the current CGTMSE scheme and lender process.",
        "documents": "Udyam/business documents, KYC, project/business details, financial information and documents required by the lending institution.",
        "source_url": "https://www.cgtmse.in/",
        "categories": ["MSME", "Business Finance", "Manufacturing", "Services", "Retail"],
        "beneficiary_types": ["Individual Entrepreneur", "Micro-enterprise", "Small Enterprise"],
        "business_stages": ["New Business", "Existing Business"],
        "funding_min": 0,
        "funding_max": 0,
        "keywords": ["cgtmse", "credit guarantee", "collateral", "loan", "msme", "micro enterprise", "small enterprise"]
    },
    {
        "name": "SFURTI – Scheme of Fund for Regeneration of Traditional Industries",
        "target": "Traditional artisans, rural industries, clusters and implementing agencies working with traditional industry activities.",
        "benefit": "Cluster-based support for regeneration, competitiveness, common facilities, skills, design, technology and market support for traditional industries.",
        "key_conditions": "Typically implemented through approved cluster/project structures rather than as a simple individual cash benefit; current portal and guidelines apply.",
        "documents": "Cluster/project proposal, artisan/enterprise details, implementing-agency documents and documents required under current SFURTI guidelines.",
        "source_url": "https://sfurti.msme.gov.in/",
        "categories": ["Artisan", "Handicrafts", "Rural Industry", "Traditional Industry", "Cluster"],
        "beneficiary_types": ["Individual Artisan", "SHG/Group", "Cooperative", "Cluster"],
        "business_stages": ["New Business", "Existing Business"],
        "funding_min": 0,
        "funding_max": 50000000,
        "keywords": ["sfurti", "artisan", "handicraft", "khadi", "traditional industry", "cluster", "rural industry"]
    },
    {
        "name": "ASPIRE – Innovation, Rural Industry & Entrepreneurship",
        "target": "Eligible institutions and entrepreneurship/incubation initiatives supporting rural innovation and enterprise development.",
        "benefit": "Supports rural entrepreneurship, incubation and innovation ecosystems intended to create employment and enterprise opportunities.",
        "key_conditions": "Support is generally routed through eligible institutions/incubation mechanisms; current programme guidelines determine eligibility.",
        "documents": "Institution/project proposal, registration documents, project plan and documents required by the implementing agency.",
        "source_url": "https://dashboard.msme.gov.in/aspire.aspx",
        "categories": ["Rural Industry", "Entrepreneurship", "Innovation", "Incubation"],
        "beneficiary_types": ["Individual Entrepreneur", "Institution", "SHG/Group", "Cooperative"],
        "business_stages": ["New Business", "Existing Business"],
        "funding_min": 0,
        "funding_max": 0,
        "keywords": ["aspire", "rural industry", "innovation", "incubation", "entrepreneurship", "msme"]
    },
    {
        "name": "MSME TEAM Initiative",
        "target": "Micro and small enterprises seeking digital market access, visibility, e-commerce and marketing support.",
        "benefit": "Supports MSME market access through digital enablement, visibility, training and related market-linkage activities under the RAMP programme.",
        "key_conditions": "Eligibility and available support depend on current TEAM programme guidelines and participating ecosystem partners.",
        "documents": "Udyam/business details, KYC and digital/business information required by the programme or participating platform.",
        "source_url": "https://ramp.msme.gov.in/ramp/",
        "categories": ["MSME", "Digital Business", "Market Access", "E-commerce", "Marketing"],
        "beneficiary_types": ["Individual Entrepreneur", "Micro-enterprise", "Small Enterprise"],
        "business_stages": ["New Business", "Existing Business"],
        "funding_min": 0,
        "funding_max": 1000000,
        "keywords": ["team", "msme team", "digital marketing", "ecommerce", "market access", "online sales", "marketing"]
    },
    {
        "name": "Pradhan Mantri Matsya Sampada Yojana (PMMSY)",
        "target": "Fish farmers, fishers, aquaculture entrepreneurs and eligible fisheries-sector beneficiaries and groups.",
        "benefit": "Supports fisheries production, aquaculture, post-harvest infrastructure, value chains, technology and eligible fisheries activities under the scheme components.",
        "key_conditions": "Eligible activities, assistance pattern and beneficiary contribution depend on the applicable PMMSY component and state/implementing guidelines.",
        "documents": "KYC, fisheries/aquaculture activity details, land/water/project documents, bank details and component-specific documents.",
        "source_url": "https://pmmsy.dof.gov.in/",
        "categories": ["Fisheries", "Aquaculture", "Fish Processing", "Cold Storage", "Fish Retail"],
        "beneficiary_types": ["Individual Entrepreneur", "Individual Farmer", "FPO", "SHG/Group", "Cooperative"],
        "business_stages": ["New Business", "Existing Business"],
        "funding_min": 0,
        "funding_max": 0,
        "keywords": ["pmmsy", "fish", "fisheries", "aquaculture", "biofloc", "hatchery", "fish processing", "cold storage"]
    },
])

BASE_SCHEMES = [
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

# ============================================================
# HELPER FUNCTIONS
# ============================================================

def money(value):
    return f"₹{value:,.0f}"

def calculate_match(business, capital, resource, interest, water, experience, location, resources_list=None):
    score = 0
    reasons = []
    resources_list = resources_list or []

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

    # Resource fit
    resource_lower = resource.lower()
    resource_matches = [r.lower() for r in business["resources"]]
    if any(r in resource_lower for r in resource_matches) or resource == "Not sure / I have limited resources":
        score += 20
        reasons.append("Your available resources can support this type of business.")
    else:
        score += 7
        reasons.append("You may need to arrange some additional resources before starting.")

    # Interest fit
    interest_lower = interest.lower()
    if any(x.lower() in interest_lower for x in business["interests"]):
        score += 20
        reasons.append("The business matches your stated interest.")
    else:
        score += 7

    # Water fit
    if "Water" in business["resources"] or "water" in business["name"].lower():
        if water == "Good":
            score += 10
            reasons.append("Good water availability improves feasibility.")
        elif water == "Limited":
            score += 4
            reasons.append("Limited water availability makes this business more sensitive to planning.")
        else:
            score += 1
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

    # Detailed resource specifications (Feature 4): land area, water, labour
    # and market access from the user's added resource entries give a small
    # additional adjustment on top of the basic inputs above.
    if resources_list:
        total_land = sum(float(r.get("land_area") or 0) for r in resources_list)
        total_labor = sum(float(r.get("labor") or 0) for r in resources_list)
        best_market = "Poor"
        market_rank = {"Poor": 0, "Moderate": 1, "Good": 2}
        for r in resources_list:
            m = r.get("market_access", "Poor")
            if market_rank.get(m, 0) > market_rank.get(best_market, 0):
                best_market = m

        needs_land = "Land" in business["resources"]
        if needs_land:
            if total_land >= 1:
                score += 6
                reasons.append("Your recorded land area supports this business.")
            elif total_land > 0:
                score += 3
            # else: no bonus, no penalty (kept neutral for non-land businesses too)

        if total_labor >= 2:
            score += 4
        elif total_labor >= 1:
            score += 2

        if best_market == "Good":
            score += 5
            reasons.append("Good recorded market access improves feasibility.")
        elif best_market == "Moderate":
            score += 2

    return min(score, 100), reasons


def compute_investment_estimate(business, investment):
    """Feature 7: given a planned investment amount, return an indicative
    annual benefit range and the typical timeline, using this prototype's
    demonstration success-rate/return assumptions for the business."""
    low_ret, high_ret = business["expected_return_pct"]
    benefit_low = investment * (low_ret / 100)
    benefit_high = investment * (high_ret / 100)
    t_low, t_high = business["timeline_months"]
    return benefit_low, benefit_high, t_low, t_high


def scheme_for_business(business):
    return business["schemes"]




# ============================================================
# ENHANCED HYPER-LOCAL ADVISORY DATA + FINANCIAL ENGINE
# ============================================================
# These are structured prototype assumptions. Where official
# information is unavailable, the UI explicitly labels estimates/fallbacks.
LOCATION_CONTEXT = {
    "Hubballi": {"state":"Karnataka","district":"Dharwad","climate":"Semi-arid","temperature_c":26,"rainfall_mm":700,"soil":"Red/black mixed","water":"Medium","market_access":"Good"},
    "Dharwad": {"state":"Karnataka","district":"Dharwad","climate":"Semi-arid","temperature_c":25,"rainfall_mm":750,"soil":"Black/red mixed","water":"Medium","market_access":"Good"},
    "Belagavi": {"state":"Karnataka","district":"Belagavi","climate":"Moderate","temperature_c":24,"rainfall_mm":900,"soil":"Red/black","water":"Medium","market_access":"Good"},
    "Bengaluru": {"state":"Karnataka","district":"Bengaluru Urban","climate":"Moderate","temperature_c":23,"rainfall_mm":900,"soil":"Red loam","water":"Medium","market_access":"Good"},
    "Mysuru": {"state":"Karnataka","district":"Mysuru","climate":"Moderate","temperature_c":24,"rainfall_mm":800,"soil":"Red loam","water":"Medium","market_access":"Good"},
    "Shivamogga": {"state":"Karnataka","district":"Shivamogga","climate":"Humid","temperature_c":24,"rainfall_mm":1800,"soil":"Red loam","water":"High","market_access":"Good"},
    "Davanagere": {"state":"Karnataka","district":"Davanagere","climate":"Semi-arid","temperature_c":26,"rainfall_mm":650,"soil":"Black soil","water":"Medium","market_access":"Good"},
    "Gadag": {"state":"Karnataka","district":"Gadag","climate":"Semi-arid","temperature_c":27,"rainfall_mm":600,"soil":"Black soil","water":"Limited","market_access":"Moderate"},
    "Haveri": {"state":"Karnataka","district":"Haveri","climate":"Moderate","temperature_c":25,"rainfall_mm":750,"soil":"Black/red","water":"Medium","market_access":"Good"},
    "Vijayapura": {"state":"Karnataka","district":"Vijayapura","climate":"Dry","temperature_c":27,"rainfall_mm":550,"soil":"Black soil","water":"Limited","market_access":"Moderate"},
    "Kalaburagi": {"state":"Karnataka","district":"Kalaburagi","climate":"Dry","temperature_c":28,"rainfall_mm":650,"soil":"Deep black soil","water":"Limited","market_access":"Moderate"},
    "Raichur": {"state":"Karnataka","district":"Raichur","climate":"Dry","temperature_c":28,"rainfall_mm":650,"soil":"Black/alluvial","water":"Medium","market_access":"Good"},
    "Tumakuru": {"state":"Karnataka","district":"Tumakuru","climate":"Semi-arid","temperature_c":25,"rainfall_mm":700,"soil":"Red loam","water":"Limited","market_access":"Good"},
    "Chitradurga": {"state":"Karnataka","district":"Chitradurga","climate":"Dry","temperature_c":26,"rainfall_mm":600,"soil":"Red/black","water":"Limited","market_access":"Moderate"},
}

# Indicative crop profiles. Existing CROP_DATA remains the source for
# displayed demo prices; these fields are planning assumptions, not official
# agronomic guarantees.
CROP_PROFILES = {
    "Maize":{"water":"Medium","duration":"90–120 days","yield":"2.5–4.5 t/ha","soil":"Well-drained loam/black soil"},
    "Groundnut":{"water":"Low–Medium","duration":"100–120 days","yield":"1.2–2.0 t/ha","soil":"Sandy/red/loam"},
    "Cotton":{"water":"Medium","duration":"150–180 days","yield":"1.5–2.5 t/ha","soil":"Black soil"},
    "Tur":{"water":"Low–Medium","duration":"150–180 days","yield":"0.8–1.5 t/ha","soil":"Well-drained black/red soil"},
    "Bengal Gram":{"water":"Low","duration":"100–120 days","yield":"0.8–1.5 t/ha","soil":"Black/loam"},
    "Jowar":{"water":"Low","duration":"100–120 days","yield":"1.5–2.5 t/ha","soil":"Black/red soil"},
    "Bajra":{"water":"Low","duration":"75–100 days","yield":"1.5–2.5 t/ha","soil":"Light, well-drained soil"},
    "Sunflower":{"water":"Low–Medium","duration":"90–110 days","yield":"0.7–1.2 t/ha","soil":"Well-drained soil"},
    "Soybean":{"water":"Medium","duration":"90–120 days","yield":"1.5–2.5 t/ha","soil":"Well-drained loam/black soil"},
    "Rice":{"water":"High","duration":"110–150 days","yield":"3–5 t/ha","soil":"Clay/loam with water retention"},
    "Ragi":{"water":"Low–Medium","duration":"100–120 days","yield":"1.5–2.5 t/ha","soil":"Red loam"},
    "Sugarcane":{"water":"High","duration":"10–14 months","yield":"70–100 t/ha","soil":"Deep fertile soil"},
    "Tomato":{"water":"Medium–High","duration":"90–140 days","yield":"25–50 t/ha","soil":"Well-drained loam"},
    "Onion":{"water":"Medium","duration":"100–150 days","yield":"20–35 t/ha","soil":"Well-drained loam"},
    "Chilli":{"water":"Medium","duration":"120–180 days","yield":"1.5–3.0 t/ha dry","soil":"Well-drained loam"},
    "Turmeric":{"water":"Medium–High","duration":"7–9 months","yield":"20–30 t/ha fresh","soil":"Loam"},
    "Beans":{"water":"Medium","duration":"60–90 days","yield":"8–15 t/ha","soil":"Well-drained loam"},
    "Cabbage":{"water":"Medium","duration":"80–120 days","yield":"25–45 t/ha","soil":"Fertile loam"},
    "Potato":{"water":"Medium","duration":"80–120 days","yield":"20–35 t/ha","soil":"Sandy loam"},
    "Coconut":{"water":"Medium–High","duration":"Perennial","yield":"Indicative: 60–100 nuts/tree/year","soil":"Well-drained loam"},
    "Banana":{"water":"High","duration":"10–14 months","yield":"30–50 t/ha","soil":"Deep fertile loam"},
    "Ginger":{"water":"Medium–High","duration":"7–9 months","yield":"12–20 t/ha","soil":"Loose loam"},
    "Pumpkin":{"water":"Medium","duration":"90–120 days","yield":"15–30 t/ha","soil":"Loam"},
    "Bottle Gourd":{"water":"Medium","duration":"90–120 days","yield":"15–25 t/ha","soil":"Loam"},
    "Cucumber":{"water":"Medium","duration":"60–90 days","yield":"10–20 t/ha","soil":"Sandy loam"},
    "Coriander":{"water":"Low–Medium","duration":"40–90 days","yield":"Indicative; depends on leaf/seed production","soil":"Well-drained loam"},
    "Spinach":{"water":"Medium","duration":"30–60 days","yield":"Indicative; repeated harvest possible","soil":"Fertile loam"},
    "Carrot":{"water":"Medium","duration":"70–100 days","yield":"20–35 t/ha","soil":"Loose sandy loam"},
    "Cauliflower":{"water":"Medium","duration":"90–150 days","yield":"20–35 t/ha","soil":"Fertile loam"},
    "Capsicum":{"water":"Medium","duration":"120–180 days","yield":"15–30 t/ha","soil":"Well-drained loam"},
    "Beetroot":{"water":"Medium","duration":"60–90 days","yield":"15–25 t/ha","soil":"Sandy loam"},
    "Radish":{"water":"Medium","duration":"35–60 days","yield":"15–25 t/ha","soil":"Loose sandy loam"},
    "Papaya":{"water":"Medium–High","duration":"9–12 months to first harvest","yield":"Indicative; varies widely","soil":"Well-drained fertile soil"},
    "Guava":{"water":"Medium","duration":"2–3 years to meaningful harvest","yield":"Indicative; varies by cultivar","soil":"Well-drained soil"},
    "Green Gram":{"water":"Low","duration":"60–75 days","yield":"0.6–1.0 t/ha","soil":"Well-drained loam"},
    "Black Gram":{"water":"Low","duration":"70–90 days","yield":"0.6–1.0 t/ha","soil":"Well-drained loam"},
    "Fenugreek Leaves":{"water":"Low–Medium","duration":"30–50 days","yield":"Indicative; repeated harvest possible","soil":"Loam"},
    "Lady Finger":{"water":"Medium","duration":"50–80 days","yield":"8–15 t/ha","soil":"Loam"},
    "Pomegranate":{"water":"Medium","duration":"18–24 months to commercial harvest","yield":"Indicative; varies widely","soil":"Well-drained soil"},
}

def _secret(name, default=""):
    try:
        return st.secrets.get(name, default)
    except Exception:
        return default

def resource_totals(resources):
    totals = {"land":0.0,"water":"None","labor":0,"market":"Poor","shop":0,"vehicle":0,"storage":0,"electricity":0,"internet":0}
    water_rank = {"None":0,"Low":1,"Medium":2,"High":3}
    market_rank = {"Poor":0,"Moderate":1,"Good":2}
    for r in resources or []:
        typ = str(r.get("type",""))
        if typ == "Land":
            totals["land"] += float(r.get("land_area",0) or 0)
        if typ == "Labour":
            totals["labor"] += int(r.get("labor",0) or 0)
        if typ == "Shop space":
            totals["shop"] += 1
        if typ == "Vehicle":
            totals["vehicle"] += 1
        if typ == "Storage":
            totals["storage"] += 1
        if typ == "Electricity":
            totals["electricity"] += 1
        if typ == "Internet":
            totals["internet"] += 1
        w = str(r.get("water","None"))
        if water_rank.get(w,0) > water_rank.get(totals["water"],0):
            totals["water"] = w
        m = str(r.get("market_access","Poor"))
        if market_rank.get(m,0) > market_rank.get(totals["market"],0):
            totals["market"] = m
    return totals

def business_financial_model(business):
    """Build a transparent small-scale model from existing business ranges.
    All outputs are labelled estimates and use ranges, not guarantees."""
    low, high = business["capital"]
    recommended = int((low + high) / 2)
    maximum = high
    # Conservative assumptions vary by business type.
    low_ret, high_ret = business.get("expected_return_pct",(10,25))
    monthly_revenue_low = low * (1 + low_ret/100) / 12
    monthly_revenue_high = recommended * (1 + high_ret/100) / 8
    # Cost is kept separate from revenue; benefit is revenue minus operating cost.
    cost_ratio_low, cost_ratio_high = 0.55, 0.75
    monthly_cost_low = monthly_revenue_low * cost_ratio_low
    monthly_cost_high = monthly_revenue_high * cost_ratio_high
    return {
        "minimum_investment": low,
        "recommended_investment": recommended,
        "maximum_investment": maximum,
        "monthly_revenue": (monthly_revenue_low, monthly_revenue_high),
        "monthly_cost": (monthly_cost_low, monthly_cost_high),
        "monthly_benefit": (max(0, monthly_revenue_low-monthly_cost_high), max(0, monthly_revenue_high-monthly_cost_low)),
        "roi": (max(0, low_ret*0.5), max(0, high_ret)),
    }

def financial_projection(business, investment):
    fm = business_financial_model(business)
    min_i = fm["minimum_investment"]
    low_ret, high_ret = business.get("expected_return_pct",(10,25))
    scale = max(0.35, min(1.75, investment / max(min_i,1)))
    rev_low, rev_high = fm["monthly_revenue"]
    cost_low, cost_high = fm["monthly_cost"]
    rev_low *= scale; rev_high *= scale
    cost_low *= scale; cost_high *= scale
    benefit_low = max(0, rev_low-cost_high)
    benefit_high = max(0, rev_high-cost_low)
    annual_low, annual_high = benefit_low*12, benefit_high*12
    roi_low = (annual_low / investment * 100) if investment else 0
    roi_high = (annual_high / investment * 100) if investment else 0
    break_low = investment/benefit_high if benefit_high else float("inf")
    break_high = investment/benefit_low if benefit_low else float("inf")
    return {
        "revenue":(rev_low,rev_high),"cost":(cost_low,cost_high),
        "benefit":(benefit_low,benefit_high),
        "annual_benefit":(annual_low,annual_high),
        "roi":(roi_low,roi_high),
        "break_even":(break_low,break_high)
    }

def calculate_enhanced_match(business, capital, resource, interest, water, experience, location, resources):
    base_score, reasons = calculate_match(business, capital, resource, interest, water, experience, location, resources)
    totals = resource_totals(resources)
    ctx = LOCATION_CONTEXT.get(location, {"state":"Karnataka","district":"Locality profile pending","climate":"Use supplied climate input","temperature_c":"Not available","rainfall_mm":"Not available","soil":"Use supplied soil input","water":"Use supplied water input","market_access":"Use supplied market access input"})
    score = float(base_score)
    required = " ".join(business.get("resources",[])).lower()
    # Resource-specific scoring
    if "land" in required:
        score += 6 if totals["land"] >= 1 else (-4 if resources else 0)
    if "vehicle" in required:
        score += 6 if totals["vehicle"] else -3
    if "shop" in required or "workspace" in required:
        score += 5 if totals["shop"] or any("workspace" in str(r.get("type","")).lower() for r in resources) else 0
    if totals["labor"]:
        score += min(5, totals["labor"])
    # Water + local climate + market access
    if ("water" in required or business.get("is_crop_based")):
        wr = {"None":0,"Low":1,"Medium":2,"High":3}.get(totals["water"],0)
        if water == "Good": wr += 1
        elif water == "Limited": wr -= 0.5
        score += max(-5,min(5,wr))
    if location not in business.get("locations",[]):
        score -= 8
        reasons.append(f"{location} is not in this business profile's preferred location list.")
    if ctx.get("market_access") == "Good":
        score += 3
    # Crop suitability: crop-based businesses must have local crops.
    if business.get("is_crop_based") and not suitable_crops_for_location(location):
        score -= 10
    return max(0,min(100,round(score))), reasons, totals

def dynamic_success_rate(business, match_score, capital, resources, location):
    totals = resource_totals(resources)
    fm = business_financial_model(business)
    risk_penalty = 0
    if business.get("risks"):
        high_risks = sum(1 for r in business["risks"] if str(r.get("likelihood","")).lower()=="high")
        risk_penalty += min(12, high_risks*4)
    capital_factor = 1 if capital >= fm["minimum_investment"] else 0.75
    resource_factor = 1 if resources else 0.9
    rate = match_score*0.55 + business.get("success_rate",60)*0.25 + 20*capital_factor*resource_factor - risk_penalty
    return int(max(20,min(95,round(rate))))

def crop_analysis_rows(location):
    rows=[]
    for crop in suitable_crops_for_location(location):
        profile=CROP_PROFILES.get(crop,{})
        market = CROP_DATA.get(crop, {})
        rows.append({
            "crop":crop,"why":f"Listed as suitable for {location} in the prototype location profile.",
            "climate":LOCATION_CONTEXT.get(location,{"climate":"Use supplied climate input"}).get("climate","Use supplied climate input"),
            "water":profile.get("water","Not available"),
            "duration":profile.get("duration","Not available"),
            "yield":profile.get("yield","Not available"),
            "soil":profile.get("soil","Not available"),
            "price":market.get("price",0),
            "unit":market.get("unit","as reported"),
        })
    return rows

def ensure_business_fields():
    for b in BUSINESSES:
        fm=business_financial_model(b)
        b.setdefault("minimum_investment",fm["minimum_investment"])
        b.setdefault("recommended_investment",fm["recommended_investment"])
        b.setdefault("maximum_investment",fm["maximum_investment"])
        b.setdefault("financial_model",fm)
        b.setdefault("required_resources",b.get("resources",[]))
        b.setdefault("location_suitability",b.get("locations",[]))
        b.setdefault("climate_requirements","Depends on the specific activity; compare with local profile.")
        b.setdefault("water_requirements","Depends on the activity and scale.")
        b.setdefault("labour_requirements","Depends on the operating scale.")
        b.setdefault("market_requirements","Local demand and access to a selling channel are required.")
ensure_business_fields()

# ============================================================
# HOME
# ============================================================

if page == "Home":

    st.markdown("""
    <style>
    /* ==================== HOME ONLY ==================== */
    [data-testid="stMainBlockContainer"]{
        max-width:1800px!important;
        padding-left:2.5rem!important;
        padding-right:2.5rem!important;
        padding-top:1.2rem!important;
    }
    .gs-home{animation:gsFade .7s ease both;width:100%}

    /* TOP NAVIGATION */
    .gs-topnav{
        position:sticky;top:0;z-index:999;
        display:flex;align-items:center;justify-content:space-between;
        gap:22px;padding:13px 20px;margin:0 0 20px;
        border-radius:18px;background:rgba(255,255,255,.90);
        border:1px solid rgba(55,105,50,.12);
        box-shadow:0 10px 30px rgba(35,75,35,.10);
        backdrop-filter:blur(14px);
    }
    .gs-brand{display:flex;align-items:center;gap:9px;white-space:nowrap;font-size:18px;font-weight:900;color:#315b2c}
    .gs-navlinks{display:flex;align-items:center;justify-content:flex-end;gap:6px;flex-wrap:wrap}
    .gs-navlinks a{
        text-decoration:none!important;color:#40543c!important;font-size:13px;font-weight:750;
        padding:9px 13px;border-radius:999px;transition:all .25s ease;
    }
    .gs-navlinks a:hover{background:#eaf4e6;transform:translateY(-2px);color:#2f6429!important}

    /* HERO */
    .gs-hero{
        position:relative;min-height:620px;overflow:hidden;border-radius:34px;margin-bottom:18px;
        background:#edf6e9;border:1px solid rgba(54,105,52,.12);
        box-shadow:0 24px 65px rgba(35,75,35,.16)
    }
    .gs-hero-copy{position:relative;z-index:5;width:53%;padding:78px 46px 70px 68px;animation:gsSlide .8s ease both}
    .gs-kicker{display:inline-block;padding:9px 16px;border-radius:999px;background:rgba(255,255,255,.78);border:1px solid rgba(55,105,50,.12);font-size:12px;font-weight:800;letter-spacing:1.1px;text-transform:uppercase}
    .gs-hero-title{font-size:68px;line-height:1.0;margin:23px 0 15px;font-weight:900;letter-spacing:-2.8px}
    .gs-hero-subtitle{font-size:31px;line-height:1.22;font-weight:780;margin-bottom:15px;max-width:700px}
    .gs-hero-text{font-size:17px;line-height:1.75;max-width:650px;opacity:.72}
    .gs-hero-stage{margin-top:23px;font-size:13px;font-weight:750;opacity:.62}
    .gs-hero-visual{position:absolute;right:0;top:0;width:57%;height:100%;overflow:hidden}
    .gs-photo{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;animation:gsZoom 7s ease-in-out infinite alternate;filter:saturate(.95)}
    .gs-photo-overlay{position:absolute;inset:0;background:linear-gradient(90deg,#edf6e9 0%,rgba(237,246,233,.91) 10%,rgba(237,246,233,.30) 50%,rgba(237,246,233,0) 100%)}
    .gs-floating-leaf{position:absolute;z-index:4;font-size:34px;animation:gsFloat 4s ease-in-out infinite}
    .gs-leaf1{right:42%;top:15%}.gs-leaf2{right:10%;bottom:18%;animation-delay:1.3s}.gs-leaf3{right:28%;bottom:8%;font-size:24px;animation-delay:.6s}

    .gs-explore-row{text-align:center;margin:0 0 55px}
    .gs-explore-row .stButton>button{
        border-radius:999px!important;padding:13px 31px!important;font-size:15px!important;
        font-weight:850!important;background:#3f7338!important;color:white!important;border:0!important;
        box-shadow:0 12px 27px rgba(48,100,43,.24)!important;transition:all .25s ease!important
    }
    .gs-explore-row .stButton>button:hover{transform:translateY(-4px) scale(1.025)!important;box-shadow:0 17px 34px rgba(48,100,43,.30)!important}
    .gs-progress{height:5px;max-width:360px;margin:13px auto 0;background:rgba(60,110,55,.12);border-radius:20px;overflow:hidden}
    .gs-progress span{display:block;height:100%;background:#4f813f;border-radius:20px;transition:width .5s ease}

    /* SECTIONS */
    .gs-section{scroll-margin-top:95px}
    .gs-heading{text-align:center;font-size:34px;font-weight:850;margin:0}
    .gs-note{text-align:center;opacity:.62;margin:9px 0 28px;font-size:15px}
    .gs-feature-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:20px;margin-bottom:58px}
    .gs-card{min-height:190px;padding:28px 23px;border-radius:23px;background:rgba(255,255,255,.92);border:1px solid rgba(65,105,55,.12);box-shadow:0 11px 30px rgba(40,70,35,.09);transition:transform .3s ease,box-shadow .3s ease;animation:gsCard .65s ease both}
    .gs-card:hover{transform:translateY(-10px) rotate(.25deg);box-shadow:0 20px 40px rgba(40,70,35,.17)}
    .gs-icon{font-size:39px;margin-bottom:13px;animation:gsIcon 2.8s ease-in-out infinite}
    .gs-card-title{font-size:19px;font-weight:800;margin-bottom:8px}.gs-card-text{font-size:14px;line-height:1.65;opacity:.65}

    .gs-glance{padding:40px 32px;border-radius:29px;background:linear-gradient(135deg,#eef7e9,#faf4e0);border:1px solid rgba(65,105,55,.1);margin-bottom:58px;scroll-margin-top:95px}
    .gs-glance-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:17px;margin-top:28px}
    .gs-glance-item{padding:25px 17px;border-radius:19px;background:rgba(255,255,255,.86);text-align:center;border:1px solid rgba(65,105,55,.09);transition:all .25s ease}
    .gs-glance-item:hover{transform:translateY(-6px);box-shadow:0 12px 25px rgba(40,70,35,.09)}
    .gs-glance-icon{font-size:31px}.gs-glance-label{font-size:12px;opacity:.58;margin-top:9px}.gs-glance-value{font-size:16px;font-weight:760;margin-top:6px}

    .gs-how{margin-bottom:58px;scroll-margin-top:95px}.gs-process{display:flex;align-items:center;justify-content:center;gap:12px;margin-top:30px}
    .gs-step{flex:1;max-width:255px;padding:25px 15px;text-align:center;border-radius:21px;background:rgba(255,255,255,.86);border:1px solid rgba(65,105,55,.11);box-shadow:0 8px 24px rgba(40,70,35,.07);animation:gsCard .7s ease both}
    .gs-number{width:47px;height:47px;border-radius:50%;margin:0 auto 12px;display:flex;align-items:center;justify-content:center;background:#477a3c;color:white;font-weight:850;animation:gsPulse 2s infinite}
    .gs-step-title{font-size:15px;font-weight:780}.gs-step-text{font-size:12px;line-height:1.5;opacity:.62;margin-top:6px}.gs-arrow{font-size:29px;opacity:.4;animation:gsArrow 1.4s ease-in-out infinite}

    .gs-motion{display:grid;grid-template-columns:1.05fr 1fr;gap:30px;align-items:center;padding:28px;border-radius:29px;background:#f4f7ef;border:1px solid rgba(65,105,55,.1);margin-bottom:58px}
    .gs-gif{height:320px;border-radius:23px;overflow:hidden;background:#dfe9d8;box-shadow:0 14px 35px rgba(40,70,35,.13)}.gs-gif img{width:100%;height:100%;object-fit:cover}
    .gs-motion h2{font-size:31px;margin:0 0 13px}.gs-motion p{line-height:1.75;opacity:.68}.gs-badges{display:flex;flex-wrap:wrap;gap:9px;margin-top:18px}.gs-badge{padding:8px 13px;border-radius:999px;background:white;border:1px solid rgba(65,105,55,.1);font-size:12px;font-weight:700}

    .gs-built{display:grid;grid-template-columns:1fr 1fr;gap:34px;align-items:center;padding:30px;border-radius:29px;background:rgba(246,248,241,.86);border:1px solid rgba(65,105,55,.1);margin-bottom:58px;scroll-margin-top:95px}
    .gs-built-img{height:390px;border-radius:23px;overflow:hidden}.gs-built-img img{width:100%;height:100%;object-fit:cover;transition:transform .7s ease}.gs-built-img:hover img{transform:scale(1.07)}
    .gs-built h2{font-size:34px;margin:0 0 14px}.gs-built p{line-height:1.75;opacity:.68}.gs-checks{list-style:none;padding:0}.gs-checks li{margin:12px 0;font-weight:650;animation:gsSlide .5s ease both}

    .gs-cta{text-align:center;padding:54px 28px;border-radius:30px;background:linear-gradient(135deg,#edf6e9,#f8f2dd);border:1px solid rgba(65,105,55,.1);margin-bottom:25px;box-shadow:0 14px 38px rgba(40,70,35,.09)}
    .gs-cta h2{font-size:34px;margin:0 0 10px}.gs-cta p{opacity:.65;margin-bottom:21px}

    @keyframes gsFade{from{opacity:0}to{opacity:1}}
    @keyframes gsSlide{from{opacity:0;transform:translateX(-25px)}to{opacity:1;transform:translateX(0)}}
    @keyframes gsCard{from{opacity:0;transform:translateY(20px)}to{opacity:1;transform:translateY(0)}}
    @keyframes gsZoom{from{transform:scale(1)}to{transform:scale(1.08)}}
    @keyframes gsFloat{0%,100%{transform:translateY(0) rotate(-5deg)}50%{transform:translateY(-16px) rotate(8deg)}}
    @keyframes gsIcon{0%,100%{transform:translateY(0)}50%{transform:translateY(-5px)}}
    @keyframes gsArrow{0%,100%{transform:translateX(0)}50%{transform:translateX(8px)}}
    @keyframes gsPulse{0%,100%{box-shadow:0 0 0 0 rgba(71,122,60,.25)}50%{box-shadow:0 0 0 8px rgba(71,122,60,0)}}

    @media(max-width:1100px){
        [data-testid="stMainBlockContainer"]{padding-left:1.5rem!important;padding-right:1.5rem!important}
        .gs-feature-grid,.gs-glance-grid{grid-template-columns:repeat(2,1fr)}
        .gs-hero-copy{width:62%;padding-left:48px}.gs-hero-visual{width:51%}.gs-hero-title{font-size:56px}
        .gs-navlinks a{padding:8px 9px;font-size:12px}
    }
    @media(max-width:760px){
        [data-testid="stMainBlockContainer"]{padding-left:.7rem!important;padding-right:.7rem!important}
        .gs-topnav{position:relative;display:block;padding:14px;margin-bottom:14px}.gs-brand{justify-content:center;margin-bottom:10px}.gs-navlinks{justify-content:center}
        .gs-hero{min-height:720px}.gs-hero-copy{width:100%;padding:38px 24px}.gs-hero-title{font-size:45px}.gs-hero-subtitle{font-size:23px}.gs-hero-text{font-size:15px}
        .gs-hero-visual{width:100%;height:43%;top:auto;bottom:0}.gs-photo-overlay{background:linear-gradient(180deg,#edf6e9 0%,rgba(237,246,233,.30) 35%,rgba(237,246,233,0) 100%)}
        .gs-feature-grid,.gs-glance-grid,.gs-motion,.gs-built{grid-template-columns:1fr}.gs-process{flex-direction:column}.gs-step{width:100%;max-width:440px}.gs-arrow{transform:rotate(90deg)}
        .gs-gif{height:250px}.gs-built-img{height:290px}.gs-heading{font-size:28px}.gs-built h2,.gs-motion h2,.gs-cta h2{font-size:28px}
    }
    </style>
    """, unsafe_allow_html=True)

    if "gs_scene" not in st.session_state:
        st.session_state.gs_scene = 0

    scenes = [
        {
            "image": "https://images.unsplash.com/photo-1500382017468-9049fed747ef?auto=format&fit=crop&w=1500&q=88",
            "title": "Your Digital Companion for Smarter Farming",
            "text": "Get useful information about crops, market prices, government schemes and financial guidance — all in one place.",
            "stage": "01 / 03"
        },
        {
            "image": "https://images.unsplash.com/photo-1464226184884-fa280b87c399?auto=format&fit=crop&w=1500&q=88",
            "title": "Discover Better Farming Information",
            "text": "Explore crop information and practical agricultural guidance through a simple farmer-friendly interface.",
            "stage": "02 / 03"
        },
        {
            "image": "https://images.unsplash.com/photo-1488459716781-31db52582fe9?auto=format&fit=crop&w=1500&q=88",
            "title": "Make Informed Decisions",
            "text": "Check available mandi prices, explore schemes and use financial guidance to support your next step.",
            "stage": "03 / 03"
        }
    ]
    scene = scenes[st.session_state.gs_scene]

    st.markdown(f"""
    <div class="gs-home">
      <div class="gs-hero">
        <div class="gs-hero-copy">
          <div class="gs-kicker">🌱 Agriculture • Information • Guidance</div>
          <h1 class="gs-hero-title">🌾 Gram Sahayak</h1>
          <div class="gs-hero-subtitle">{scene['title']}</div>
          <p class="gs-hero-text">{scene['text']}</p>
        </div>
        <div class="gs-hero-visual">
          <img class="gs-photo" src="{scene['image']}" alt="Agriculture and farming">
          <div class="gs-photo-overlay"></div>
          <div class="gs-floating-leaf gs-leaf1">🌿</div>
          <div class="gs-floating-leaf gs-leaf2">🍃</div>
          <div class="gs-floating-leaf gs-leaf3">🌱</div>
        </div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div id="gs-features" class="gs-section">
      <h2 class="gs-heading">✨ Explore Gram Sahayak</h2>
      <p class="gs-note">Useful tools gathered in one simple farmer-friendly interface.</p>
      <div class="gs-feature-grid">
        <div class="gs-card"><div class="gs-icon">🌾</div><div class="gs-card-title">Crop Information</div><div class="gs-card-text">Learn about crops and farming practices.</div></div>
        <div class="gs-card"><div class="gs-icon">💰</div><div class="gs-card-title">Market Prices</div><div class="gs-card-text">Check the latest available mandi prices.</div></div>
        <div class="gs-card"><div class="gs-icon">🏛️</div><div class="gs-card-title">Government Schemes</div><div class="gs-card-text">Explore useful government agricultural schemes.</div></div>
        <div class="gs-card"><div class="gs-icon">🤖</div><div class="gs-card-title">Financial Assistant</div><div class="gs-card-text">Get simple financial guidance for farming.</div></div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div id="gs-glance" class="gs-glance gs-section">
      <h2 class="gs-heading">🌱 Farming at a Glance</h2>
      <p class="gs-note">A quick overview using information already available in the app.</p>
      <div class="gs-glance-grid">
        <div class="gs-glance-item"><div class="gs-glance-icon">📍</div><div class="gs-glance-label">Location</div><div class="gs-glance-value">{str(location)}</div></div>
        <div class="gs-glance-item"><div class="gs-glance-icon">🌾</div><div class="gs-glance-label">Crop</div><div class="gs-glance-value">Select in Crop Information</div></div>
        <div class="gs-glance-item"><div class="gs-glance-icon">💰</div><div class="gs-glance-label">Market Price</div><div class="gs-glance-value">Latest available in Market Prices</div></div>
        <div class="gs-glance-item"><div class="gs-glance-icon">🏛️</div><div class="gs-glance-label">Government Schemes</div><div class="gs-glance-value">Available in the Government Schemes page</div></div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div id="gs-how" class="gs-how gs-section">
      <h2 class="gs-heading">⚙️ How Gram Sahayak Works</h2>
      <p class="gs-note">A simple flow from selection to useful information.</p>
      <div class="gs-process">
        <div class="gs-step"><div class="gs-number">1</div><div class="gs-step-title">📍 Select Location</div><div class="gs-step-text">Choose your location from the app.</div></div>
        <div class="gs-arrow">→</div>
        <div class="gs-step"><div class="gs-number">2</div><div class="gs-step-title">🌾 Select Crop</div><div class="gs-step-text">Choose the crop or information you need.</div></div>
        <div class="gs-arrow">→</div>
        <div class="gs-step"><div class="gs-number">3</div><div class="gs-step-title">🔎 Find Information</div><div class="gs-step-text">Gram Sahayak finds the relevant information.</div></div>
        <div class="gs-arrow">→</div>
        <div class="gs-step"><div class="gs-number">4</div><div class="gs-step-title">📊 View Results</div><div class="gs-step-text">See useful results in the app.</div></div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="gs-motion" id="gs-smart-farming">
      <div class="gs-gif"><img src="https://media.giphy.com/media/mDBBU8K7Np2UQs9Dqy/giphy.gif" alt="Seedlings growing animation"></div>
      <div>
        <div class="gs-kicker">🌱 From Seed to Harvest</div>
        <h2>Grow Smarter with Gram Sahayak</h2>
        <p>Get crop information, market updates, scheme details and financial guidance to support better farming decisions.</p>
        <div class="gs-badges"><span class="gs-badge">🌱 Crop Information</span><span class="gs-badge">📈 Market Updates</span><span class="gs-badge">🏛️ Schemes</span><span class="gs-badge">💰 Financial Guidance</span></div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div id="gs-built" class="gs-built gs-section">
      <div class="gs-built-img"><img src="https://images.unsplash.com/photo-1464226184884-fa280b87c399?auto=format&fit=crop&w=1200&q=88" alt="Farmer and agricultural produce"></div>
      <div>
        <h2>👨‍🌾 Built for Farmers</h2>
        <p>Gram Sahayak brings important agricultural information together in a simple and accessible interface.</p>
        <ul class="gs-checks"><li>✓ Simple to use</li><li>✓ Agricultural information</li><li>✓ Latest available mandi prices</li><li>✓ Government scheme information</li><li>✓ Financial guidance</li></ul>
      </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="gs-cta">
      <h2>🌱 Everything you need, in one place.</h2>
      <p>Explore Gram Sahayak and discover useful tools for smarter farming.</p>
    </div>
    """, unsafe_allow_html=True)



# ============================================================
# LIVE MANDI / AGMARKNET CONNECTION — ADDITION ONLY
# ============================================================
# The complete original Market Prices implementation below is preserved.
# This new interface is rendered first and stops before the legacy block.
MANDI_RESOURCE_ID = "9ef84268-d588-465a-a308-a864a43d0070"
MANDI_API_URL = f"https://api.data.gov.in/resource/{MANDI_RESOURCE_ID}"
MANDI_STATE = "Karnataka"

# ------------------------------------------------------------
# data.gov.in API KEY
# ------------------------------------------------------------
# The key is entered by the user on the Market Prices page (as before).
# A default can optionally be pre-filled from .streamlit/secrets.toml.
DEFAULT_MANDI_API_KEY = ""
try:
    DEFAULT_MANDI_API_KEY = st.secrets.get("MANDI_API_KEY", "") or ""
except Exception:
    DEFAULT_MANDI_API_KEY = ""


def _mandi_norm(value):
    return " ".join(str(value or "").strip().lower().split())


def _mandi_num(value):
    try:
        return float(str(value).replace(",", "").strip())
    except Exception:
        return None


# ------------------------------------------------------------
# LOCATION -> MANDI DISTRICT
# ------------------------------------------------------------
# The location chosen in the top navigation bar is used everywhere in the
# app. Many of those locations are taluks/towns, while the government mandi
# dataset is published district-wise, so each location is mapped to the
# district under which its mandi records are reported.
# Crop name (app) -> commodity names used in the government mandi dataset.
MANDI_COMMODITY_ALIASES = {
    "Green Chilli": ["Green Chilli", "Green Chilli (Fresh)", "Chilli Green", "Chilli", "Green Chilli Fresh"],
    "Chilli": ["Chilli", "Green Chilli", "Chillies", "Red Chilli", "Dry Chillies", "Chilly Capsicum"],
    "Lady Finger": ["Lady Finger", "Bhindi", "Okra", "Bhindi(Ladies Finger)"],
    "Brinjal": ["Brinjal", "Eggplant", "Brinjal (Purple)"],
    "Coriander": ["Coriander", "Coriander Seed", "Dhaniya", "Coriander(Leaves)"],
    "Groundnut": ["Groundnut", "Ground Nut", "Peanut", "Groundnut (Split)", "Groundnut Seed"],
    "Areca nut": ["Arecanut", "Areca nut", "Areca Nut", "Supari", "Arecanut(Betelnut/Supari)"],
    "Bengal Gram": ["Bengal Gram", "Bengal Gram(Gram)(Whole)", "Gram", "Chana", "Kabuli Chana"],
    "Black Gram": ["Black Gram", "Black Gram (Urd Beans)(Whole)", "Black Gram Dal", "Urad", "Urad Dal"],
    "Green Gram": ["Green Gram", "Green Gram (Moong)(Whole)", "Green Gram Dal", "Moong", "Moong Dal"],
    "Tur": ["Tur", "Arhar", "Arhar (Tur/Red Gram)(Whole)", "Arhar Dal", "Red Gram", "Tur Dal"],
    "Jowar": ["Jowar", "Jowar(Sorghum)", "Sorghum"],
    "Bajra": ["Bajra", "Bajra(Pearl Millet/Cumbu)", "Pearl Millet"],
    "Maize": ["Maize", "Corn"],
    "Paddy": ["Paddy", "Paddy(Dhan)(Common)", "Paddy(Dhan)(Basmati)", "Rice"],
    "Cotton": ["Cotton", "Cotton (Unginned)", "Kapas"],
    "Sugarcane": ["Sugarcane"],
    "Sunflower": ["Sunflower", "Sunflower Seed"],
    "Soybean": ["Soyabean", "Soybean", "Soyabean Yellow"],
    "Tomato": ["Tomato"],
    "Onion": ["Onion", "Onions"],
    "Potato": ["Potato"],
    "Mango": ["Mango", "Mango (Raw-Ripe)"],
    "Grapes": ["Grapes"],
    "Pomegranate": ["Pomegranate", "Pomegranate (Anar)"],
    "Turmeric": ["Turmeric", "Turmeric Raw", "Turmeric (raw)"],
    "Coffee": ["Coffee", "Coffee Beans"],
    "Pepper": ["Black Pepper", "Pepper", "Pepper ungarbled", "Pepper garbled"],
    "Cardamom": ["Cardamom", "Cardamoms"],
    "Coconut": ["Coconut", "Coconut Seed", "Coconut Oil", "Tender Coconut"],
    "Cashew": ["Cashew", "Cashewnuts", "Cashew Nut", "Cashewnut"],
    "Banana": ["Banana", "Banana - Green"],
    "Orange": ["Orange", "Orange (Nagpur)"],
    "Ragi": ["Ragi", "Ragi (Finger Millet)", "Finger Millet"],
    "Wheat": ["Wheat"],
    "Tobacco": ["Tobacco"],
    "Rubber": ["Rubber"],
    "Mulberry": ["Mulberry", "Mulberry Leaf", "Cocoon", "Mulberry Cocoon"],
    "Flowers": ["Rose(Loose)", "Marigold(Calcutta)", "Jasmine", "Chrysanthemum(Loose)", "Marigold(Loose)"],
    "Vegetables": ["Tomato", "Onion", "Potato", "Brinjal", "Cabbage", "Cauliflower", "Beans"],
    "Spices": ["Pepper", "Cardamom", "Turmeric", "Chilli", "Coriander"],
}

# Some AGRI_LOCATION_CROPS entries list a broad category rather than a single
# crop. This map expands each category into the individual crops that should
# get their own price card, styled the same way as every other crop.
CATEGORY_EXPANSION = {
    "Vegetables": ["Tomato", "Onion", "Potato", "Brinjal", "Cabbage", "Cauliflower", "Beans"],
    "Spices": ["Pepper", "Cardamom", "Turmeric", "Coriander"],
}

# Reverse map: normalised commodity text -> app crop name.
_MANDI_COMMODITY_LOOKUP = {}
for _crop, _names in MANDI_COMMODITY_ALIASES.items():
    for _name in _names:
        _MANDI_COMMODITY_LOOKUP.setdefault(_mandi_norm(_name), []).append(_crop)


def _mandi_date_key(row):
    raw = str(row.get("arrival_date", "")).strip()
    for fmt in ("%d/%m/%Y", "%Y-%m-%d", "%d-%m-%Y"):
        try:
            return datetime.datetime.strptime(raw, fmt)
        except Exception:
            pass
    return datetime.datetime.min


def _mandi_request(params):
    """Single request with one retry on timeout/connection problems."""
    last_error = None
    for attempt in range(2):
        try:
            response = requests.get(
                MANDI_API_URL,
                params=params,
                timeout=(8, 20),
                headers={"User-Agent": "Gram-Sahayak/1.0"},
            )
            response.raise_for_status()
            payload = response.json()
            records = payload.get("records", []) if isinstance(payload, dict) else []
            return records, None
        except (requests.exceptions.Timeout, requests.exceptions.ConnectionError) as exc:
            last_error = "The government mandi server took too long to respond. Please try again in a moment."
            if attempt == 0:
                import time
                time.sleep(1.0)
        except Exception as exc:
            message = str(exc)
            # Never show the API key back to the user in an error message.
            message = message.split("?")[0]
            if "401" in message or "403" in message:
                message = ("The data.gov.in service rejected this API key. "
                           "Please check the key entered above, or generate a free "
                           "key at data.gov.in.")
            return [], message
    return [], last_error


@st.cache_data(ttl=900, show_spinner=False)
def _fetch_karnataka_records(district, api_key):
    """
    Fetch Karnataka mandi records once for the whole page.

    One call is made for the selected district (and its alternate spellings)
    and one state-wide call is kept as a fallback, so every crop box can be
    filled from a small number of requests instead of one request per crop.
    """
    if not api_key:
        return [], [], "Enter your data.gov.in API key above to load live mandi prices."
    if requests is None:
        return [], [], "The requests package is not installed. Run: pip install requests"

    district_records, state_records, error = [], [], None

    for district_name in DISTRICT_ALIASES.get(district, [district]):
        got, err = _mandi_request({
            "api-key": api_key,
            "format": "json",
            "limit": 1000,
            "offset": 0,
            "filters[state]": MANDI_STATE,
            "filters[district]": district_name,
        })
        district_records.extend(got)
        if err and not error:
            error = err

    got, err = _mandi_request({
        "api-key": api_key,
        "format": "json",
        "limit": 2000,
        "offset": 0,
        "filters[state]": MANDI_STATE,
    })
    state_records.extend(got)
    if err and not error:
        error = err

    return district_records, state_records, error


def _best_record(records, crop, taluka=None):
    """
    Latest usable price record for one crop from a list of mandi records.

    When a taluka is given, only mandis whose market name matches that taluka
    are considered, so the cards can show the taluka's own mandi first.
    """
    wanted = {_mandi_norm(n) for n in MANDI_COMMODITY_ALIASES.get(crop, [crop])}
    taluka_key = _mandi_norm(taluka) if taluka else None
    matches = []
    for row in records:
        commodity = _mandi_norm(row.get("commodity"))
        if not commodity:
            continue
        if taluka_key:
            market = _mandi_norm(row.get("market"))
            if taluka_key not in market and market not in taluka_key:
                continue
        if commodity in wanted or any(w and (w in commodity or commodity in w) for w in wanted):
            matches.append(row)
    if not matches:
        return None

    matches.sort(key=_mandi_date_key, reverse=True)
    for row in matches:
        mn = _mandi_num(row.get("min_price"))
        md = _mandi_num(row.get("modal_price"))
        mx = _mandi_num(row.get("max_price"))
        if mn is None and md is None and mx is None:
            continue
        values = [v for v in (mn, md, mx) if v is not None]
        return {
            "commodity": row.get("commodity", crop),
            "market": row.get("market", "Not reported"),
            "district": row.get("district", "Not reported"),
            "date": row.get("arrival_date", "Not reported"),
            "min": mn if mn is not None else min(values),
            "modal": md if md is not None else max(values),
            "max": mx if mx is not None else max(values),
            "variety": row.get("variety", ""),
        }
    return None


# Master crop list: every crop that appears anywhere in AGRI_LOCATION_CROPS,
# with the broad "Vegetables"/"Spices" categories expanded into their
# individual crops. This is the same list of price cards shown for every
# location, so no location shows a shorter list than another.
_ALL_LOCATION_CROPS = set()
for _crop_list in AGRI_LOCATION_CROPS.values():
    _ALL_LOCATION_CROPS.update(_crop_list)

ALL_MARKET_CROPS = []
_seen_market_crops = set()
for _crop in sorted(_ALL_LOCATION_CROPS):
    for _expanded in CATEGORY_EXPANSION.get(_crop, [_crop]):
        if _expanded not in _seen_market_crops:
            _seen_market_crops.add(_expanded)
            ALL_MARKET_CROPS.append(_expanded)
ALL_MARKET_CROPS.sort()


def get_mandi_prices(district, taluka, api_key):
    """
    Latest mandi price for every crop in ALL_MARKET_CROPS, for the selected
    location.

    Preference order for each crop:
      1. a mandi inside the selected location (taluka/town),
      2. any mandi inside the selected location's district,
      3. the nearest available mandi elsewhere in Karnataka.
    """
    crops = ALL_MARKET_CROPS
    district_records, state_records, error = _fetch_karnataka_records(district, api_key)

    results = []
    for crop in crops:
        record, scope = _best_record(district_records, crop, taluka=taluka), "taluka"
        if not record:
            record, scope = _best_record(district_records, crop), "district"
        if not record:
            record, scope = _best_record(state_records, crop), "state"
        if record:
            record["scope"] = scope
        results.append((crop, record))
    return results, error


# ============================================================
# MARKET PRICES — LIVE KARNATAKA MANDI PRICES
# ============================================================
if page == "Market Prices":
    st.markdown("""
    <style>
    .gs-price-grid-note{color:#6B7280;font-size:13.5px;margin:.2rem 0 1rem;}
    .gs-price-card{
        background:#FFFFFF;border:1px solid rgba(46,125,50,.18);border-radius:14px;
        padding:16px 18px;margin-bottom:14px;min-height:172px;
        box-shadow:0 4px 6px -1px rgba(0,0,0,.08),0 10px 20px rgba(27,94,32,.05);
    }
    .gs-price-card.empty{background:#FAFAFA;border-style:dashed;}
    .gs-price-crop{font-size:17px;font-weight:800;color:#1B5E20;margin-bottom:6px;}
    .gs-price-modal{font-size:28px;font-weight:900;color:#2E7D32;line-height:1.15;}
    .gs-price-modal span{font-size:13px;font-weight:600;color:#6B7280;margin-left:4px;}
    .gs-price-range{font-size:13.5px;color:#374151;margin:6px 0 8px;}
    .gs-price-meta{font-size:12.5px;color:#6B7280;line-height:1.5;}
    .gs-price-tag{
        display:inline-block;margin-top:9px;padding:3px 10px;border-radius:999px;
        font-size:11.5px;font-weight:700;background:#E8F5E9;color:#1B5E20;
    }
    .gs-price-tag.state{background:#FFF4E5;color:#8A5300;}
    .gs-price-empty-text{font-size:13.5px;color:#6B7280;margin-top:10px;}
    </style>
    """, unsafe_allow_html=True)

    st.title("📈 " + tr("market_title"))

    # "location" comes from the top navigation bar and is shared by every
    # page in the app. The government mandi dataset is published
    # district-wise, so the location is mapped to its district internally.
    district = LOCATION_DISTRICT.get(location, location)
    st.write(
        f"Live **Karnataka** mandi prices for **{location}** "
        f"({district} district) from the Government of India "
        f"Open Government Data platform, data.gov.in."
    )

    key_col, refresh_col = st.columns([4, 1], vertical_alignment="bottom")
    with key_col:
        market_api_key = st.text_input(
            "🔑 data.gov.in API key",
            value=DEFAULT_MANDI_API_KEY,
            type="password",
            key="market_ui_api_key",
            help="Enter your free data.gov.in API key to load live mandi prices.",
        )
    with refresh_col:
        if st.button("🔄 Refresh", use_container_width=True, key="market_refresh_btn"):
            _fetch_karnataka_records.clear()
            st.rerun()

    if not market_api_key.strip():
        st.info(
            "Enter your data.gov.in API key above to load live Karnataka mandi prices "
            f"for {location} ({district} district). No sample or simulated prices are shown on this page."
        )
    else:
        with st.spinner(f"Loading Karnataka mandi prices for {location}, {district}..."):
            results, error = get_mandi_prices(district, location, market_api_key.strip())

        available = [(c, r) for c, r in results if r]
        missing = [c for c, r in results if not r]

        st.markdown(
            f"<div class='gs-price-grid-note'>Showing {len(available)} of {len(results)} "
            f"crops, every vegetable priced individually, for <b>{html.escape(str(location))}</b>, "
            f"{html.escape(str(district))} district • Karnataka • "
            f"prices in ₹ per quintal (100 kg)</div>",
            unsafe_allow_html=True
        )

        if error and not available:
            st.warning(error)

        if available:
            per_row = 3
            for start in range(0, len(available), per_row):
                chunk = available[start:start + per_row]
                cols = st.columns(per_row)
                for col, (crop, rec) in zip(cols, chunk):
                    scope = rec.get("scope")
                    if scope == "taluka":
                        tag_class = "gs-price-tag"
                        tag_text = f"{html.escape(str(location))} mandi"
                    elif scope == "district":
                        tag_class = "gs-price-tag"
                        tag_text = f"{html.escape(str(district))} district mandi"
                    else:
                        tag_class = "gs-price-tag state"
                        tag_text = "Nearest Karnataka mandi"
                    variety = str(rec.get("variety") or "").strip()
                    variety_line = (
                        f"<div class='gs-price-meta'>Variety: {html.escape(variety)}</div>"
                        if variety and variety.lower() not in ("other", "not reported")
                        else ""
                    )
                    with col:
                        st.markdown(
                            f"""<div class="gs-price-card">
  <div class="gs-price-crop">🌾 {html.escape(str(tr_data(crop)))}</div>
  <div class="gs-price-modal">₹{rec['modal']:,.0f}<span>/quintal</span></div>
  <div class="gs-price-range">Min ₹{rec['min']:,.0f} &nbsp;•&nbsp; Max ₹{rec['max']:,.0f}</div>
  <div class="gs-price-meta">Mandi: {html.escape(str(rec['market']))}</div>
  {variety_line}
  <div class="gs-price-meta">Arrival date: {html.escape(str(rec['date']))}</div>
  <div class="{tag_class}">{tag_text}</div>
</div>""",
                            unsafe_allow_html=True
                        )

        if missing:
            st.markdown("#### 🕒 No price reported today")
            per_row = 3
            for start in range(0, len(missing), per_row):
                chunk = missing[start:start + per_row]
                cols = st.columns(per_row)
                for col, crop in zip(cols, chunk):
                    with col:
                        st.markdown(
                            f"""<div class="gs-price-card empty">
  <div class="gs-price-crop">🌾 {html.escape(str(tr_data(crop)))}</div>
  <div class="gs-price-empty-text">No Karnataka mandi price has been published for this
  crop in the latest available government update. Please check again later.</div>
</div>""",
                            unsafe_allow_html=True
                        )

        st.caption(
            "Source: Government of India • data.gov.in • Agmarknet daily mandi prices (Karnataka). "
            "Prices are the latest published records and may lag by a day or two. "
            "Verify at your local mandi before taking a financial decision."
        )

    st.markdown("<div style='height:22px'></div>", unsafe_allow_html=True)
    st.divider()
    st.markdown("<div style='text-align:center; color:#5f6b78; font-size:14px;'>🌾 Gram Sahayak • Prototype for rural micro-entrepreneur business guidance</div>", unsafe_allow_html=True)
    st.markdown("<div style='text-align:center; color:#667085; font-size:13px; margin-top:12px;'>Live Karnataka mandi prices • Rule-based recommendations • Verify official scheme information before decisions</div>", unsafe_allow_html=True)
    st.stop()

# Merge the user-provided records into the existing Government Schemes dataset.
# Existing entries from the same scheme family are removed first to avoid duplicate
# cards for KCC/PMEGP/PMMY/PMFME/AIF.
_SCHEME_FAMILY_KEYS = {
    "pm-kisan": "PM-KISAN",
    "kcc": "Kisan Credit Card",
    "mudra": "MUDRA",
    "pmegp": "PMEGP",
    "pmfme": "PMFME",
    "vishwakarma": "Vishwakarma",
    "aif": "Agriculture Infrastructure Fund",
}

def _scheme_family(name):
    n = name.lower()
    for key, family in _SCHEME_FAMILY_KEYS.items():
        if key in n:
            return family
    return name

_new_families = {_scheme_family(x["name"]) for x in GOVT_SCHEMES_DATA}
SCHEMES = [x for x in BASE_SCHEMES if _scheme_family(x["name"]) not in _new_families]
for _g in GOVT_SCHEMES_DATA:
    SCHEMES.append({
        "name": _g["name"],
        "best_for": _g["target"],
        "description": _g["benefit"],
        "key": _g["key_conditions"],
        "why": "Relevant when the applicant/business matches the scheme's stated beneficiary type, stage and activity conditions.",
        "source": _g["source_url"],
        "source_url": _g["source_url"],
        "documents": _g["documents"],
        "categories": _g["categories"],
        "beneficiary_types": _g["beneficiary_types"],
        "business_stages": _g["business_stages"],
        "funding_min": _g["funding_min"],
        "funding_max": _g["funding_max"],
        "keywords": _g["keywords"],
    })


# ------------------------------------------------------------
# GOVERNMENT SCHEME DISPLAY HELPERS
# ------------------------------------------------------------
# These helpers keep the Government Schemes renderer compatible
# with the translation system. They safely fall back to the
# original English text when a translation is not available.
def scheme_name(value):
    return tr_any(value)

def stext(kind, value):
    return tr_any(value)

def scheme_extra(kind, value):
    return tr_any(value)


if page == "Government Schemes":
    st.markdown(
        f"""<div class="gs-scheme-hero">
            <div class="gs-scheme-hero-icon">🏛️</div>
            <div>
                <div class="gs-eyebrow">GRAM SAHAYAK • SCHEME DISCOVERY</div>
                <h1>{html.escape(tr("scheme_title"))}</h1>
                <p>{html.escape(tr("scheme_desc"))}</p>
            </div>
        </div>""", unsafe_allow_html=True
    )

    all_beneficiaries = sorted({b for x in SCHEMES for b in x.get("beneficiary_types", [])})
    all_stages = sorted({b for x in SCHEMES for b in x.get("business_stages", [])})
    all_categories = sorted({b for x in SCHEMES for b in x.get("categories", [])})

    f1, f2, f3 = st.columns([1.05, 1.05, 1.05])
    with f1:
        beneficiary = st.selectbox("👤 " + tr_any("User / Beneficiary Type"), ["All"] + all_beneficiaries, key="scheme_beneficiary")
    with f2:
        stage = st.selectbox("🧭 " + tr_any("Business Stage"), ["All"] + all_stages, key="scheme_stage")
    with f3:
        category = st.selectbox("🌱 " + tr_any("Activity Category"), ["All"] + all_categories, key="scheme_category")

    f4, f5, f6 = st.columns([1.25, 1.0, 1.0])
    with f4:
        search = st.text_input("🔎 " + tr("search"), placeholder=tr("placeholder"), key="scheme_search")
    with f5:
        funding = st.number_input(
            "💰 " + tr_any("Approximate Funding Requirement (₹)"),
            min_value=0, max_value=20000000, value=100000, step=10000,
            key="scheme_funding"
        )
    with f6:
        st.markdown('<div class="gs-filter-spacer"></div>', unsafe_allow_html=True)
        matches_only = st.checkbox(tr_any("Show matches only (>30% profile match)"), value=False, key="scheme_matches")

    def scheme_profile_match(scheme):
        score = 0
        reasons = []
        max_score = 4
        if beneficiary == "All" or beneficiary in scheme.get("beneficiary_types", []):
            score += 1
            if beneficiary != "All":
                reasons.append("Beneficiary type aligns with the scheme profile.")
        if stage == "All" or stage in scheme.get("business_stages", []):
            score += 1
            if stage != "All":
                reasons.append("Business stage is covered by the scheme profile.")
        if category == "All" or category in scheme.get("categories", []):
            score += 1
            if category != "All":
                reasons.append("Activity category is covered by the scheme profile.")
        lo, hi = scheme.get("funding_min", 0), scheme.get("funding_max", 10**12)
        if lo == 0 and hi == 0:
            reasons.append("Funding amount is determined by the applicable scheme component, lender or current guidelines.")
        elif lo <= funding <= hi:
            score += 1
            reasons.append(f"Funding requirement (₹{funding:,.0f}) falls within the scheme range.")
        elif funding > 0:
            reasons.append(f"Funding requirement is outside the indicative range (₹{lo:,.0f} – ₹{hi:,.0f}).")
        return round(score / max_score * 100), reasons

    shown = []
    for scheme in SCHEMES:
        haystack = " ".join([
            scheme.get("name", ""), scheme.get("best_for", ""), scheme.get("description", ""),
            scheme.get("key", ""), scheme.get("why", ""),
            " ".join(scheme.get("keywords", [])), " ".join(scheme.get("categories", []))
        ]).lower()
        if search and search.lower().strip() not in haystack:
            continue
        match, reasons = scheme_profile_match(scheme)
        if matches_only and match <= 30:
            continue
        shown.append((scheme, match, reasons))

    shown.sort(key=lambda x: (-x[1], x[0].get("name", "")))
    total = len(SCHEMES)
    matched = sum(1 for _, m, _ in shown if m > 30)
    exact_range = sum(1 for x in SCHEMES if x.get("funding_min", 0) != 0 or x.get("funding_max", 0) != 0 if x.get("funding_min", 0) <= funding <= x.get("funding_max", 10**12))

    m1, m2, m3, m4 = st.columns(4)
    m1.markdown(f'<div class="gs-scheme-stat"><span>📋</span><strong>{len(shown)}</strong><small>{html.escape(tr_any("Schemes shown"))}</small></div>', unsafe_allow_html=True)
    m2.markdown(f'<div class="gs-scheme-stat"><span>🎯</span><strong>{matched}</strong><small>{html.escape(tr_any("Profile matches"))}</small></div>', unsafe_allow_html=True)
    m3.markdown(f'<div class="gs-scheme-stat"><span>💰</span><strong>{exact_range}</strong><small>{html.escape(tr_any("Funding range fit"))}</small></div>', unsafe_allow_html=True)
    m4.markdown(f'<div class="gs-scheme-stat"><span>🏛️</span><strong>{total}</strong><small>{html.escape(tr_any("Total schemes"))}</small></div>', unsafe_allow_html=True)

    st.markdown(
        f'<div class="gs-match-note">ℹ️ {html.escape(tr_any("Matches are calculated programmatically for profile alignment. This is NOT an official eligibility confirmation."))}</div>',
        unsafe_allow_html=True
    )

    if not shown:
        st.info(tr_any("No schemes match the selected filters. Try changing the beneficiary, stage, category or funding requirement."))
    else:
        for idx, (scheme, match, reasons) in enumerate(shown, start=1):
            name = scheme_name(scheme.get("name", ""))
            benefit = stext("desc", scheme.get("description", ""))
            target = stext("best", scheme.get("best_for", ""))
            key_info = scheme_extra("key", scheme.get("key", ""))
            why = scheme_extra("why", scheme.get("why", ""))
            source_label = scheme_extra("source", scheme.get("source", ""))
            lo, hi = scheme.get("funding_min", 0), scheme.get("funding_max", 10**12)
            categories = scheme.get("categories", [])
            docs = scheme.get("documents", "")
            source_url = scheme.get("source_url") or scheme.get("source")
            match_class = "high" if match >= 75 else ("mid" if match > 30 else "low")
            badge_text = f"{match}% {tr_any('Profile Match')}"
            chips = "".join(f'<span class="gs-chip">{html.escape(str(c))}</span>' for c in categories[:4])
            reasons_html = "".join(f"<li>{html.escape(r)}</li>" for r in reasons)

            st.markdown(
                f"""<div class="gs-scheme-card gs-match-{match_class}">
                    <div class="gs-scheme-card-top">
                        <div class="gs-scheme-index">{idx:02d}</div>
                        <div class="gs-scheme-card-title">
                            <div class="gs-scheme-name">{html.escape(name)}</div>
                            <div class="gs-chip-row">{chips}</div>
                        </div>
                        <div class="gs-match-badge">🎯 {html.escape(badge_text)}</div>
                    </div>
                    <div class="gs-benefit-strip"><span>💡</span><div><b>{html.escape(tr_any('Key Benefit'))}</b><br>{html.escape(benefit)}</div></div>
                </div>""", unsafe_allow_html=True
            )

            if isinstance(source_url, str) and source_url.startswith("http"):
                official_html = f'<a href="{html.escape(source_url, quote=True)}" target="_blank" rel="noopener noreferrer">Visit Official Website ↗</a>'
            else:
                official_html = html.escape(str(source_label or "Not available"))

            funding_text = (
                f"Indicative range: ₹{lo:,.0f} – ₹{hi:,.0f}"
                if hi > 0 else
                "No direct funding amount specified; this is a market/trading portal."
            )
            table_rows = [
                ("🎯", "Purpose & Description", benefit),
                ("👥", "Target Beneficiaries", target),
                ("📋", "Major Eligibility Conditions", key_info),
                ("💰", "Financial Support / Range", funding_text),
                ("📄", "Important Documents Required", docs or "Check the official portal for current document requirements."),
                ("🔗", "Official Source / Portal", official_html),
            ]
            table_html = "".join(
                f'<tr><td class="gs-table-label"><span>{icon}</span><b>{html.escape(label)}</b></td><td>{value}</td></tr>'
                for icon, label, value in table_rows
            )
            st.markdown(
                f'<div class="gs-info-table-wrap"><table class="gs-info-table"><tbody>{table_html}</tbody></table></div>',
                unsafe_allow_html=True
            )

            if reasons:
                st.markdown(
                    f'<div class="gs-reason-box"><b>{html.escape(tr_any("Why this matches"))}</b><ul>{reasons_html}</ul></div>',
                    unsafe_allow_html=True
                )
            with st.expander(f"{tr_any('View scheme details')} · {name}"):
                st.markdown(f"**{tr_any('Why this scheme may be relevant')}:** {why}")
                st.markdown(f"**{tr_any('Profile alignment')}:** {match}%")
                if isinstance(source_url, str) and source_url.startswith("http"):
                    st.link_button("🔗 " + tr_any("Open Official Portal"), source_url)

    st.warning(tr("scheme_warning"))

# ============================================================
# FINANCIAL ASSISTANT
# ============================================================

# ============================================================
# PAGE 4: FINANCIAL ASSISTANT
# ============================================================
if page == "Financial Assistant":
    st.markdown(f"## 💰 {tr('finance_title')}")
    st.markdown(
        "Use these beginner-friendly calculators to plan business sales, "
        "evaluate loan EMIs, estimate affordability, and forecast monthly cash flows."
    )

    fin_tab1, fin_tab2, fin_tab3, fin_tab4 = st.tabs([
        tr("profit_tab"),
        tr("emi_tab"),
        "📊 Loan Affordability",
        "💵 Monthly Cash Flow Planner"
    ])

    # ========================================================
    # TAB 1: PROFIT CALCULATOR
    # ========================================================
    with fin_tab1:
        st.markdown(f"### {tr('profit_est')}")

        pc1, pc2 = st.columns(2)

        with pc1:
            fin_qty = st.number_input(
                tr("quantity"),
                min_value=1,
                value=100,
                step=10,
                key="fa_profit_qty"
            )

            fin_buy = st.number_input(
                tr("purchase"),
                min_value=0.0,
                value=20.0,
                step=1.0,
                key="fa_profit_buy"
            )

            fin_sell = st.number_input(
                tr("selling"),
                min_value=0.0,
                value=30.0,
                step=1.0,
                key="fa_profit_sell"
            )

        with pc2:
            fin_other = st.number_input(
                tr("other"),
                min_value=0.0,
                value=200.0,
                step=50.0,
                key="fa_profit_other"
            )

        # Calculations
        fin_total_purchase = fin_qty * fin_buy
        fin_total_cost = fin_total_purchase + fin_other
        fin_revenue = fin_qty * fin_sell
        fin_profit = fin_revenue - fin_total_cost

        # Profit margin
        fin_margin = (
            fin_profit / fin_revenue * 100
            if fin_revenue > 0
            else 0.0
        )

        # Break-even analysis
        unit_margin = fin_sell - fin_buy

        if unit_margin > 0:
            be_qty = math.ceil(fin_other / unit_margin)
            be_sales = be_qty * fin_sell
        else:
            be_qty = None
            be_sales = None

        st.divider()

        m1, m2, m3, m4 = st.columns(4)

        with m1:
            st.metric(
                tr("total_cost"),
                f"₹{fin_total_cost:,.2f}"
            )

        with m2:
            st.metric(
                tr("revenue"),
                f"₹{fin_revenue:,.2f}"
            )

        with m3:
            st.metric(
                tr("profit"),
                f"₹{fin_profit:,.2f}"
            )

        with m4:
            st.metric(
                "Profit Margin",
                f"{fin_margin:.1f}%"
            )

        if fin_profit > 0:
            st.success(f"✅ {tr('positive')}")

        elif abs(fin_profit) < 1e-5:
            st.info(f"⚖️ {tr('break_even')}")

        else:
            st.error(f"⚠️ {tr('loss')}")

        st.markdown("#### Break-Even Analysis")

        if unit_margin <= 0:
            st.warning(
                "Selling price per unit is less than or equal to "
                "purchase cost per unit. You cannot recover fixed/other "
                "costs at this price."
            )
        else:
            st.info(
                f"To cover your fixed/other costs of "
                f"**₹{fin_other:,.2f}**, you must sell at least "
                f"**{be_qty:,} units** "
                f"(total sales revenue of **₹{be_sales:,.2f}**)."
            )

    # ========================================================
    # TAB 2: LOAN EMI CALCULATOR
    # ========================================================
    with fin_tab2:
        st.markdown(f"### 🏦 {tr('loan')}")

        lc1, lc2 = st.columns(2)

        with lc1:
            fin_loan_amt = st.number_input(
                tr("loan"),
                min_value=1000,
                value=50000,
                step=5000,
                key="fa_emi_amt"
            )

            fin_rate = st.number_input(
                tr("rate"),
                min_value=0.0,
                max_value=30.0,
                value=9.0,
                step=0.5,
                key="fa_emi_rate"
            )

        with lc2:
            fin_years = st.number_input(
                tr("period"),
                min_value=1,
                max_value=20,
                value=3,
                step=1,
                key="fa_emi_years"
            )

        fin_n = fin_years * 12

        if fin_rate > 0:
            fin_r = (fin_rate / 100) / 12

            fin_emi = (
                fin_loan_amt
                * fin_r
                * ((1 + fin_r) ** fin_n)
            ) / (
                ((1 + fin_r) ** fin_n) - 1
            )

        else:
            fin_r = 0
            fin_emi = fin_loan_amt / fin_n

        fin_total_pay = fin_emi * fin_n
        fin_interest = fin_total_pay - fin_loan_amt

        st.divider()

        em1, em2, em3 = st.columns(3)

        with em1:
            st.metric(
                tr("monthly"),
                f"₹{fin_emi:,.2f}"
            )

        with em2:
            st.metric(
                tr("total_payment"),
                f"₹{fin_total_pay:,.2f}"
            )

        with em3:
            st.metric(
                tr("interest"),
                f"₹{fin_interest:,.2f}"
            )

        st.caption(f"💡 {tr('loan_note')}")

    # ========================================================
    # TAB 3: LOAN AFFORDABILITY CALCULATOR
    # ========================================================
    with fin_tab3:
        st.markdown("### 📊 Loan Affordability Calculator")

        st.markdown(
            "Estimate how much loan EMI your monthly income can handle "
            "based on your existing expenses."
        )

        ac1, ac2 = st.columns(2)

        with ac1:
            aff_income = st.number_input(
                "Monthly Income (₹)",
                min_value=0.0,
                value=30000.0,
                step=1000.0,
                key="fa_aff_income"
            )

            aff_living_exp = st.number_input(
                "Existing Monthly Living Expenses (₹)",
                min_value=0.0,
                value=15000.0,
                step=1000.0,
                key="fa_aff_living"
            )

            aff_existing_emi = st.number_input(
                "Existing Monthly Loan EMIs (₹)",
                min_value=0.0,
                value=2000.0,
                step=500.0,
                key="fa_aff_emi"
            )

        with ac2:
            aff_interest_rate = st.number_input(
                "Proposed Loan Interest Rate (% p.a.)",
                min_value=0.0,
                max_value=30.0,
                value=10.0,
                step=0.5,
                key="fa_aff_rate"
            )

            aff_period_years = st.number_input(
                "Proposed Loan Period (Years)",
                min_value=1,
                max_value=20,
                value=3,
                step=1,
                key="fa_aff_years"
            )

        # Disposable income
        aff_net_surplus = (
            aff_income
            - aff_living_exp
            - aff_existing_emi
        )

        # Estimated EMI capacity
        aff_max_safe_emi = max(
            0.0,
            aff_net_surplus * 0.50
        )

        # Loan capacity calculation
        aff_n = aff_period_years * 12

        if aff_interest_rate > 0:

            aff_r = (
                aff_interest_rate / 100
            ) / 12

            aff_estimated_loan_amt = (
                aff_max_safe_emi
                * (
                    ((1 + aff_r) ** aff_n - 1)
                    /
                    (aff_r * ((1 + aff_r) ** aff_n))
                )
            )

        else:
            aff_estimated_loan_amt = (
                aff_max_safe_emi * aff_n
            )

        st.divider()

        am1, am2, am3 = st.columns(3)

        with am1:
            st.metric(
                "Net Monthly Disposable Income",
                f"₹{aff_net_surplus:,.2f}"
            )

        with am2:
            st.metric(
                "Estimated Max Monthly EMI",
                f"₹{aff_max_safe_emi:,.2f}"
            )

        with am3:
            st.metric(
                "Estimated Loan Capacity",
                f"₹{aff_estimated_loan_amt:,.2f}"
            )

        if aff_net_surplus <= 0:
            st.error(
                "⚠️ Your existing expenses and EMIs meet or exceed "
                "your monthly income. An additional loan may not fit "
                "within the entered cash flow."
            )

        else:
            st.success(
                f"Based on allocating 50% of your monthly surplus "
                f"towards a new EMI, the estimated EMI capacity is "
                f"**₹{aff_max_safe_emi:,.2f}**, corresponding to an "
                f"estimated loan amount of approximately "
                f"**₹{aff_estimated_loan_amt:,.2f}** over "
                f"{aff_period_years} years."
            )

        st.info(
            "ℹ️ **Disclaimer:** This is an estimate for financial "
            "planning only. Actual loan eligibility, interest rates, "
            "fees and repayment terms depend on the lender."
        )

    # ========================================================
    # TAB 4: MONTHLY CASH FLOW PLANNER
    # ========================================================
    with fin_tab4:
        st.markdown("### 💵 Monthly Cash Flow Planner")

        st.markdown(
            "Plan your expected monthly income and expenses to "
            "estimate your remaining cash flow."
        )

        cf1, cf2 = st.columns(2)

        with cf1:
            cf_income = st.number_input(
                "Expected Monthly Business/Family Income (₹)",
                min_value=0.0,
                value=35000.0,
                step=1000.0,
                key="fa_cf_income"
            )

            cf_operating = st.number_input(
                "Monthly Operating / Business Expenses (₹)",
                min_value=0.0,
                value=12000.0,
                step=1000.0,
                key="fa_cf_operating"
            )

        with cf2:
            cf_household = st.number_input(
                "Monthly Household / Personal Expenses (₹)",
                min_value=0.0,
                value=14000.0,
                step=1000.0,
                key="fa_cf_household"
            )

            cf_emis = st.number_input(
                "Total Monthly Debt / EMI Payments (₹)",
                min_value=0.0,
                value=3000.0,
                step=500.0,
                key="fa_cf_emis"
            )

        # Cash flow calculation
        cf_total_expenses = (
            cf_operating
            + cf_household
            + cf_emis
        )

        cf_net_cash_flow = (
            cf_income
            - cf_total_expenses
        )

        st.divider()

        cfm1, cfm2, cfm3 = st.columns(3)

        with cfm1:
            st.metric(
                "Total Monthly Income",
                f"₹{cf_income:,.2f}"
            )

        with cfm2:
            st.metric(
                "Total Monthly Expenses",
                f"₹{cf_total_expenses:,.2f}"
            )

        with cfm3:
            st.metric(
                "Remaining Cash Flow",
                f"₹{cf_net_cash_flow:,.2f}"
            )

        if cf_net_cash_flow > 0:

            st.success(
                f"✅ **Positive Cash Flow:** "
                f"₹{cf_net_cash_flow:,.2f} remains after "
                f"the entered monthly expenses and EMIs."
            )

        elif abs(cf_net_cash_flow) < 1e-5:

            st.info(
                "⚖️ **Zero Cash Flow:** Your entered monthly "
                "income exactly covers your expenses and EMIs."
            )

        else:

            st.error(
                f"⚠️ **Negative Cash Flow:** Your monthly deficit "
                f"is **₹{abs(cf_net_cash_flow):,.2f}** based on "
                f"the entered values."
            )

    st.markdown("<br>", unsafe_allow_html=True)

    st.warning(
        "⚠️ **Financial Safety Note:** All calculations provided "
        "in this section are estimates for guidance and educational "
        "planning. Actual bank interest rates, repayment schedules, "
        "and loan eligibility decisions depend on official lender policies."
    )

# DOMAIN-BASED BUSINESS RECOMMENDATION CONFIGURATION
# ============================================================
# Each business has its own inputs, requirement checks, weights and risks.
# Numeric financial fields are only shown when supported by the existing
# business profile; otherwise the app explicitly marks them as unavailable.

BUSINESS_DOMAIN_CONFIG = {
    "Agriculture": {
        "icon": "🌾",
        "businesses": {
            "Crop Cultivation": {
                "inputs": [
                    ("land_acres", "Land area (acres)", "number", {"min_value": 0.5, "value": 1.0, "step": 0.5}),
                    ("season", "Season", "select", {"options": ["Kharif", "Rabi", "Summer"]}),
                    ("water", "Water availability", "select", {"options": ["None", "Low", "Medium", "High"]}),
                    ("irrigation", "Irrigation", "select", {"options": ["Rain-fed", "Limited", "Available", "Reliable"]}),
                    ("soil_test", "Soil test available", "select", {"options": ["Yes", "No"]}),
                    ("labour", "Available labour (people)", "number", {"min_value": 0, "value": 1, "step": 1}),
                    ("investment", "Available investment (₹)", "number", {"min_value": 0, "value": 100000, "step": 5000}),
                    ("market_access", "Market access", "select", {"options": ["Poor", "Moderate", "Good"]}),
                    ("income_time", "Target time to income", "select", {"options": ["Within 3 months", "3–6 months", "6–12 months", "12+ months"]}),
                    ("risk", "Risk preference", "select", {"options": ["Low", "Medium", "High"]}),
                ],
                "requirements": {"Water": "Water suitable for the chosen crop/season", "Land": "Sufficient cultivable land", "Market": "A practical selling channel", "Soil": "Soil information is strongly recommended"},
                "weights": {"land_acres": 15, "season": 10, "water": 12, "irrigation": 8, "soil_test": 8, "labour": 7, "investment": 15, "market_access": 12, "income_time": 6, "risk": 7},
                "risks": ["Weather variability", "Water availability", "Input-price changes", "Crop-price changes", "Pest/disease pressure"],
            },
            "Cereals": {
                "inputs": [],
                "requirements": {},
                "weights": {},
                "risks": ["Weather variability", "Water availability", "Input-price changes", "Market-price changes", "Pest/disease pressure"],
            },
            "Pulses": {
                "inputs": [],
                "requirements": {},
                "weights": {},
                "risks": ["Rainfall variability", "Pest/disease pressure", "Input-price changes", "Market-price changes"],
            },
            "Oilseeds": {
                "inputs": [],
                "requirements": {},
                "weights": {},
                "risks": ["Weather variability", "Water stress", "Pest/disease pressure", "Market-price changes"],
            },
            "Commercial Crops": {
                "inputs": [],
                "requirements": {},
                "weights": {},
                "risks": ["Longer production cycle", "Input-price changes", "Market-price changes", "Weather variability"],
            },
            "Vegetable Cultivation": {
                "inputs": [
                    ("land_acres", "Land area (acres)", "number", {"min_value": 0.5, "value": 1.0, "step": 0.5}),
                    ("season", "Season", "select", {"options": ["Kharif", "Rabi", "Summer"]}),
                    ("water", "Water availability", "select", {"options": ["None", "Low", "Medium", "High"]}),
                    ("irrigation", "Irrigation", "select", {"options": ["Rain-fed", "Limited", "Available", "Reliable"]}),
                    ("soil_test", "Soil test available", "select", {"options": ["Yes", "No"]}),
                    ("labour", "Available labour (people)", "number", {"min_value": 0, "value": 2, "step": 1}),
                    ("investment", "Available investment (₹)", "number", {"min_value": 0, "value": 100000, "step": 5000}),
                    ("market_access", "Market access", "select", {"options": ["Poor", "Moderate", "Good"]}),
                    ("transport", "Transport available", "select", {"options": ["No", "Shared", "Yes"]}),
                    ("income_time", "Target time to income", "select", {"options": ["Within 3 months", "3–6 months", "6–12 months"]}),
                ],
                "requirements": {"Water": "Reliable water is important for vegetable production", "Labour": "Regular crop-care labour", "Market": "Fast access to a selling channel", "Transport": "Useful for frequent harvest movement"},
                "weights": {"land_acres": 12, "water": 15, "irrigation": 10, "soil_test": 6, "labour": 10, "investment": 13, "market_access": 15, "transport": 8, "income_time": 6, "season": 5},
                "risks": ["Perishability", "Price fluctuations", "Pest/disease pressure", "Water stress"],
            },
            "Fruit Cultivation": {
                "inputs": [
                    ("land_acres", "Land area (acres)", "number", {"min_value": 0.5, "value": 1.0, "step": 0.5}),
                    ("water", "Water availability", "select", {"options": ["None", "Low", "Medium", "High"]}),
                    ("irrigation", "Irrigation", "select", {"options": ["Rain-fed", "Limited", "Available", "Reliable"]}),
                    ("soil_test", "Soil test available", "select", {"options": ["Yes", "No"]}),
                    ("labour", "Available labour (people)", "number", {"min_value": 0, "value": 2, "step": 1}),
                    ("investment", "Available investment (₹)", "number", {"min_value": 0, "value": 150000, "step": 5000}),
                    ("market_access", "Market access", "select", {"options": ["Poor", "Moderate", "Good"]}),
                    ("storage", "Storage available", "select", {"options": ["No", "Partial", "Yes"]}),
                    ("long_term", "Can wait for longer establishment period", "select", {"options": ["No", "Yes"]}),
                ],
                "requirements": {"Land": "Sufficient land for orchard layout", "Water": "Long-term water availability", "Capital": "Higher upfront establishment cost", "Time": "Ability to wait for orchard establishment"},
                "weights": {"land_acres": 15, "water": 15, "irrigation": 10, "soil_test": 7, "labour": 8, "investment": 18, "market_access": 10, "storage": 5, "long_term": 12},
                "risks": ["Long establishment period", "Weather extremes", "Pest/disease pressure", "Market-price variability"],
            },
            "Spice Cultivation": {
                "inputs": [
                    ("land_acres", "Land area (acres)", "number", {"min_value": 0.5, "value": 1.0, "step": 0.5}),
                    ("season", "Season", "select", {"options": ["Kharif", "Rabi", "Summer"]}),
                    ("water", "Water availability", "select", {"options": ["None", "Low", "Medium", "High"]}),
                    ("soil_test", "Soil test available", "select", {"options": ["Yes", "No"]}),
                    ("labour", "Available labour (people)", "number", {"min_value": 0, "value": 2, "step": 1}),
                    ("investment", "Available investment (₹)", "number", {"min_value": 0, "value": 100000, "step": 5000}),
                    ("market_access", "Market access", "select", {"options": ["Poor", "Moderate", "Good"]}),
                    ("drying", "Drying/processing space", "select", {"options": ["No", "Partial", "Yes"]}),
                    ("income_time", "Target time to income", "select", {"options": ["Within 3 months", "3–6 months", "6–12 months", "12+ months"]}),
                ],
                "requirements": {"Water": "Crop-specific water requirement", "Labour": "Regular crop management", "Processing": "Post-harvest drying/handling may be required", "Market": "Quality-sensitive buyers"},
                "weights": {"land_acres": 12, "season": 8, "water": 12, "soil_test": 8, "labour": 10, "investment": 13, "market_access": 15, "drying": 10, "income_time": 12},
                "risks": ["Quality variation", "Price volatility", "Pest/disease pressure", "Post-harvest loss"],
            },
            "Floriculture": {
                "inputs": [
                    ("land_acres", "Land/covered area (acres)", "number", {"min_value": 0.5, "value": 0.5, "step": 0.5}),
                    ("water", "Water availability", "select", {"options": ["None", "Low", "Medium", "High"]}),
                    ("irrigation", "Irrigation", "select", {"options": ["Rain-fed", "Limited", "Available", "Reliable"]}),
                    ("labour", "Available labour (people)", "number", {"min_value": 0, "value": 2, "step": 1}),
                    ("investment", "Available investment (₹)", "number", {"min_value": 0, "value": 100000, "step": 5000}),
                    ("market_access", "Market access", "select", {"options": ["Poor", "Moderate", "Good"]}),
                    ("transport", "Transport available", "select", {"options": ["No", "Shared", "Yes"]}),
                    ("protected", "Protected cultivation/structure available", "select", {"options": ["No", "Partial", "Yes"]}),
                ],
                "requirements": {"Water": "Reliable irrigation", "Labour": "Regular harvesting/handling", "Market": "Fast access to buyers", "Transport": "Important because flowers are perishable"},
                "weights": {"land_acres": 10, "water": 15, "irrigation": 10, "labour": 12, "investment": 16, "market_access": 15, "transport": 12, "protected": 10},
                "risks": ["High perishability", "Demand fluctuations", "Weather sensitivity", "Post-harvest handling"],
            },
        }
    },
    "Livestock": {
        "icon": "🐄",
        "businesses": {
            "Poultry Farming": {
                "inputs": [
                    ("birds", "Number of birds planned", "number", {"min_value": 1, "value": 500, "step": 50}),
                    ("shed", "Suitable shed available", "select", {"options": ["No", "Partial", "Yes"]}),
                    ("shed_area", "Available shed area (sq ft)", "number", {"min_value": 0, "value": 500, "step": 50}),
                    ("water", "Water availability", "select", {"options": ["None", "Low", "Medium", "High"]}),
                    ("feed", "Feed availability", "select", {"options": ["Poor", "Moderate", "Good"]}),
                    ("electricity", "Electricity", "select", {"options": ["No", "Limited", "Reliable"]}),
                    ("labour", "Available labour (people)", "number", {"min_value": 0, "value": 1, "step": 1}),
                    ("investment", "Available investment (₹)", "number", {"min_value": 0, "value": 150000, "step": 5000}),
                    ("veterinary", "Veterinary support access", "select", {"options": ["No", "Limited", "Good"]}),
                    ("market_access", "Market access", "select", {"options": ["Poor", "Moderate", "Good"]}),
                    ("experience", "Experience", "select", {"options": ["Beginner", "Some experience", "Experienced"]}),
                    ("income_time", "Target time to income", "select", {"options": ["Within 3 months", "3–6 months", "6–12 months"]}),
                ],
                "requirements": {"Housing": "Suitable, ventilated poultry housing", "Water": "Reliable clean water", "Feed": "Reliable feed supply", "Health": "Veterinary/vaccination arrangement", "Market": "Buyer/market access"},
                "weights": {"birds": 5, "shed": 10, "shed_area": 7, "water": 10, "feed": 10, "electricity": 5, "labour": 6, "investment": 15, "veterinary": 12, "market_access": 10, "experience": 5, "income_time": 5},
                "risks": ["Disease and mortality", "Feed-cost changes", "Market-price changes", "Heat/stress management", "Biosecurity failures"],
            },
            "Dairy Farming": {
                "inputs": [
                    ("animals", "Number of animals planned", "number", {"min_value": 1, "value": 2, "step": 1}),
                    ("animal_type", "Animal type", "select", {"options": ["Cows", "Buffaloes", "Mixed"]}),
                    ("shed", "Suitable shed available", "select", {"options": ["No", "Partial", "Yes"]}),
                    ("fodder", "Fodder availability", "select", {"options": ["Poor", "Moderate", "Good"]}),
                    ("water", "Water availability", "select", {"options": ["None", "Low", "Medium", "High"]}),
                    ("veterinary", "Veterinary support access", "select", {"options": ["No", "Limited", "Good"]}),
                    ("equipment", "Milking/chilling equipment", "select", {"options": ["No", "Partial", "Yes"]}),
                    ("labour", "Available labour (people)", "number", {"min_value": 0, "value": 1, "step": 1}),
                    ("investment", "Available investment (₹)", "number", {"min_value": 0, "value": 200000, "step": 5000}),
                    ("market_access", "Milk market access", "select", {"options": ["Poor", "Moderate", "Good"]}),
                    ("experience", "Experience", "select", {"options": ["Beginner", "Some experience", "Experienced"]}),
                ],
                "requirements": {"Housing": "Animal shed", "Feed": "Reliable fodder", "Water": "Adequate drinking/cleaning water", "Health": "Veterinary support", "Market": "Milk buyer/collection channel"},
                "weights": {"animals": 5, "animal_type": 4, "shed": 10, "fodder": 12, "water": 10, "veterinary": 10, "equipment": 5, "labour": 6, "investment": 15, "market_access": 12, "experience": 7, "income_time": 4},
                "risks": ["Animal disease", "Feed/fodder cost", "Milk-price variation", "Water shortage", "Animal productivity variation"],
            },
            "Goat Farming": {
                "inputs": [
                    ("animals", "Number of goats planned", "number", {"min_value": 1, "value": 10, "step": 1}),
                    ("shed", "Goat shed available", "select", {"options": ["No", "Partial", "Yes"]}),
                    ("grazing", "Grazing/feed availability", "select", {"options": ["Poor", "Moderate", "Good"]}),
                    ("water", "Water availability", "select", {"options": ["None", "Low", "Medium", "High"]}),
                    ("veterinary", "Veterinary support access", "select", {"options": ["No", "Limited", "Good"]}),
                    ("labour", "Available labour (people)", "number", {"min_value": 0, "value": 1, "step": 1}),
                    ("investment", "Available investment (₹)", "number", {"min_value": 0, "value": 150000, "step": 5000}),
                    ("market_access", "Market access", "select", {"options": ["Poor", "Moderate", "Good"]}),
                    ("experience", "Experience", "select", {"options": ["Beginner", "Some experience", "Experienced"]}),
                ],
                "requirements": {"Housing": "Dry, secure shelter", "Feed": "Grazing or feed supply", "Water": "Regular clean water", "Health": "Veterinary access", "Market": "Livestock buyer access"},
                "weights": {"animals": 7, "shed": 10, "grazing": 14, "water": 10, "veterinary": 10, "labour": 8, "investment": 15, "market_access": 12, "experience": 8, "season": 6},
                "risks": ["Disease", "Feed availability", "Market-price variation", "Mortality", "Predation/security"],
            },
            "Sheep Farming": {
                "inputs": [
                    ("animals", "Number of sheep planned", "number", {"min_value": 1, "value": 10, "step": 1}),
                    ("shed", "Sheep shed available", "select", {"options": ["No", "Partial", "Yes"]}),
                    ("grazing", "Grazing/feed availability", "select", {"options": ["Poor", "Moderate", "Good"]}),
                    ("water", "Water availability", "select", {"options": ["None", "Low", "Medium", "High"]}),
                    ("veterinary", "Veterinary support access", "select", {"options": ["No", "Limited", "Good"]}),
                    ("labour", "Available labour (people)", "number", {"min_value": 0, "value": 1, "step": 1}),
                    ("investment", "Available investment (₹)", "number", {"min_value": 0, "value": 150000, "step": 5000}),
                    ("market_access", "Market access", "select", {"options": ["Poor", "Moderate", "Good"]}),
                    ("experience", "Experience", "select", {"options": ["Beginner", "Some experience", "Experienced"]}),
                ],
                "requirements": {"Housing": "Dry secure shelter", "Feed": "Grazing/feed supply", "Water": "Regular clean water", "Health": "Veterinary access", "Market": "Buyer access"},
                "weights": {"animals": 7, "shed": 10, "grazing": 14, "water": 10, "veterinary": 10, "labour": 8, "investment": 15, "market_access": 12, "experience": 8, "season": 6},
                "risks": ["Disease", "Feed shortage", "Market-price variation", "Mortality", "Predation/security"],
            },
        }
    },
    "Aquaculture": {
        "icon": "🐟",
        "businesses": {
            "Fish Farming": {
                "inputs": [
                    ("pond_area", "Pond area (acres)", "number", {"min_value": 0.05, "value": 0.5}),
                    ("pond_type", "Pond type", "select", {"options": ["Existing pond", "New pond", "Lined pond", "Other"]}),
                    ("water_source", "Water source", "select", {"options": ["Rain-fed", "Canal", "Borewell", "Tank/Pond", "River", "Other"]}),
                    ("water_quality", "Water quality assessment", "select", {"options": ["Unknown", "Poor", "Moderate", "Good"]}),
                    ("water_availability", "Water availability", "select", {"options": ["Seasonal", "Perennial"]}),
                    ("species", "Fish species selected", "text", {}),
                    ("feed", "Feed availability", "select", {"options": ["Poor", "Moderate", "Good"]}),
                    ("electricity", "Electricity", "select", {"options": ["No", "Limited", "Reliable"]}),
                    ("labour", "Available labour (people)", "number", {"min_value": 0, "value": 1, "step": 1}),
                    ("investment", "Available investment (₹)", "number", {"min_value": 0, "value": 200000, "step": 5000}),
                    ("market_access", "Market access", "select", {"options": ["Poor", "Moderate", "Good"]}),
                    ("experience", "Experience", "select", {"options": ["Beginner", "Some experience", "Experienced"]}),
                ],
                "requirements": {"Pond": "Adequate pond area and suitable infrastructure", "Water quality": "Suitable water quality", "Water": "Stable water availability", "Feed": "Reliable feed supply", "Market": "Buyer/market channel"},
                "weights": {"pond_area": 15, "pond_type": 6, "water_source": 8, "water_quality": 15, "water_availability": 10, "species": 3, "feed": 10, "electricity": 5, "labour": 6, "investment": 12, "market_access": 7, "experience": 3},
                "risks": ["Water-quality failure", "Disease", "Feed costs", "Fish mortality", "Market-price changes"],
            },
        }
    },
    "Horticulture & Nursery": {
        "icon": "🌱",
        "businesses": {
            "Plant Nursery": {
                "inputs": [("space", "Nursery space (sq ft)", "number", {"min_value": 10, "value": 1000, "step": 50}), ("water", "Water availability", "select", {"options": ["None", "Low", "Medium", "High"]}), ("irrigation", "Irrigation", "select", {"options": ["None", "Limited", "Available", "Reliable"]}), ("shade", "Shade/protected area", "select", {"options": ["No", "Partial", "Yes"]}), ("plant_material", "Planting material source", "select", {"options": ["Poor", "Moderate", "Reliable"]}), ("labour", "Available labour (people)", "number", {"min_value": 0, "value": 1, "step": 1}), ("investment", "Available investment (₹)", "number", {"min_value": 0, "value": 100000, "step": 5000}), ("market_access", "Market access", "select", {"options": ["Poor", "Moderate", "Good"]}), ("transport", "Transport available", "select", {"options": ["No", "Shared", "Yes"]})],
                "requirements": {"Space": "Nursery area", "Water": "Reliable watering", "Plant material": "Consistent source", "Market": "Local buyer demand"},
                "weights": {"space": 12, "water": 14, "irrigation": 10, "shade": 10, "plant_material": 12, "labour": 8, "investment": 14, "market_access": 12, "transport": 8},
                "risks": ["Plant mortality", "Seasonal demand", "Water stress", "Disease/pest pressure"],
            },
            "Fruit Nursery": {
                "inputs": [("space", "Nursery space (sq ft)", "number", {"min_value": 10, "value": 1500, "step": 50}), ("water", "Water availability", "select", {"options": ["None", "Low", "Medium", "High"]}), ("shade", "Shade/protected area", "select", {"options": ["No", "Partial", "Yes"]}), ("plant_material", "Certified/quality planting material access", "select", {"options": ["Poor", "Moderate", "Reliable"]}), ("labour", "Available labour (people)", "number", {"min_value": 0, "value": 1, "step": 1}), ("investment", "Available investment (₹)", "number", {"min_value": 0, "value": 150000, "step": 5000}), ("market_access", "Market access", "select", {"options": ["Poor", "Moderate", "Good"]}), ("transport", "Transport available", "select", {"options": ["No", "Shared", "Yes"]})],
                "requirements": {"Space": "Nursery space", "Water": "Regular watering", "Plant material": "Quality planting material", "Market": "Demand from growers"},
                "weights": {"space": 13, "water": 14, "shade": 10, "plant_material": 16, "labour": 8, "investment": 15, "market_access": 14, "transport": 10},
                "risks": ["Plant-quality issues", "Demand variability", "Water stress", "Disease"],
            },
            "Flower Nursery": {
                "inputs": [("space", "Nursery space (sq ft)", "number", {"min_value": 10, "value": 1000, "step": 50}), ("water", "Water availability", "select", {"options": ["None", "Low", "Medium", "High"]}), ("shade", "Shade/protected area", "select", {"options": ["No", "Partial", "Yes"]}), ("labour", "Available labour (people)", "number", {"min_value": 0, "value": 2, "step": 1}), ("investment", "Available investment (₹)", "number", {"min_value": 0, "value": 100000, "step": 5000}), ("market_access", "Market access", "select", {"options": ["Poor", "Moderate", "Good"]}), ("transport", "Transport available", "select", {"options": ["No", "Shared", "Yes"]})],
                "requirements": {"Space": "Nursery/production space", "Water": "Regular watering", "Market": "Local demand and transport"},
                "weights": {"space": 13, "water": 15, "shade": 12, "labour": 10, "investment": 15, "market_access": 18, "transport": 17},
                "risks": ["Perishability", "Seasonal demand", "Disease", "Transport damage"],
            },
        }
    },
    "Allied Activities": {
        "icon": "🐝",
        "businesses": {
            "Beekeeping": {
                "inputs": [("boxes", "Bee boxes planned", "number", {"min_value": 1, "value": 10, "step": 1}), ("forage", "Flowering/forage availability", "select", {"options": ["Poor", "Moderate", "Good"]}), ("water", "Water availability", "select", {"options": ["None", "Low", "Medium", "High"]}), ("equipment", "Beekeeping equipment", "select", {"options": ["No", "Partial", "Yes"]}), ("labour", "Available labour (people)", "number", {"min_value": 0, "value": 1, "step": 1}), ("investment", "Available investment (₹)", "number", {"min_value": 0, "value": 100000, "step": 5000}), ("market_access", "Market access", "select", {"options": ["Poor", "Moderate", "Good"]}), ("experience", "Experience", "select", {"options": ["Beginner", "Some experience", "Experienced"]})],
                "requirements": {"Forage": "Adequate flowering/forage source", "Equipment": "Bee boxes and handling equipment", "Market": "Honey/wax selling channel"},
                "weights": {"boxes": 10, "forage": 20, "water": 6, "equipment": 15, "labour": 8, "investment": 15, "market_access": 16, "experience": 10},
                "risks": ["Colony loss", "Weather", "Pests/disease", "Market-price variation"],
            },
            "Mushroom Cultivation": {
                "inputs": [("room_area", "Growing room area (sq ft)", "number", {"min_value": 10, "value": 500, "step": 25}), ("temperature_control", "Temperature control", "select", {"options": ["No", "Partial", "Yes"]}), ("humidity_control", "Humidity control", "select", {"options": ["No", "Partial", "Yes"]}), ("water", "Water availability", "select", {"options": ["None", "Low", "Medium", "High"]}), ("substrate", "Substrate/raw material availability", "select", {"options": ["Poor", "Moderate", "Good"]}), ("electricity", "Electricity", "select", {"options": ["No", "Limited", "Reliable"]}), ("labour", "Available labour (people)", "number", {"min_value": 0, "value": 1, "step": 1}), ("investment", "Available investment (₹)", "number", {"min_value": 0, "value": 100000, "step": 5000}), ("market_access", "Market access", "select", {"options": ["Poor", "Moderate", "Good"]})],
                "requirements": {"Growing space": "Suitable clean growing space", "Environment": "Temperature/humidity management", "Water": "Reliable water", "Market": "Fast selling channel"},
                "weights": {"room_area": 12, "temperature_control": 14, "humidity_control": 14, "water": 10, "substrate": 12, "electricity": 8, "labour": 7, "investment": 11, "market_access": 12},
                "risks": ["Contamination", "Temperature/humidity fluctuations", "Short shelf life", "Market demand"],
            },
            "Sericulture": {
                "inputs": [("mulberry_land", "Mulberry area (acres)", "number", {"min_value": 0.1, "value": 1.0}), ("water", "Water availability", "select", {"options": ["None", "Low", "Medium", "High"]}), ("rearing_space", "Rearing space", "select", {"options": ["No", "Partial", "Yes"]}), ("labour", "Available labour (people)", "number", {"min_value": 0, "value": 2, "step": 1}), ("investment", "Available investment (₹)", "number", {"min_value": 0, "value": 150000, "step": 5000}), ("market_access", "Market access", "select", {"options": ["Poor", "Moderate", "Good"]}), ("experience", "Experience", "select", {"options": ["Beginner", "Some experience", "Experienced"]})],
                "requirements": {"Mulberry": "Mulberry cultivation/source", "Water": "Regular water", "Rearing": "Suitable rearing space", "Market": "Cocoon/market channel"},
                "weights": {"mulberry_land": 16, "water": 15, "rearing_space": 14, "labour": 12, "investment": 16, "market_access": 17, "experience": 10},
                "risks": ["Disease", "Weather", "Leaf availability", "Market-price variation"],
            },
        }
    },
    "Agri/Food Processing": {
        "icon": "🏭",
        "businesses": {
            "Grain Milling": {
                "inputs": [("workspace", "Workspace available", "select", {"options": ["No", "Partial", "Yes"]}), ("raw_material", "Raw-material availability", "select", {"options": ["Poor", "Moderate", "Good"]}), ("machine", "Milling machine available", "select", {"options": ["No", "Partial", "Yes"]}), ("electricity", "Electricity", "select", {"options": ["No", "Limited", "Reliable"]}), ("labour", "Available labour (people)", "number", {"min_value": 0, "value": 2, "step": 1}), ("investment", "Available investment (₹)", "number", {"min_value": 0, "value": 300000, "step": 10000}), ("storage", "Storage available", "select", {"options": ["No", "Partial", "Yes"]}), ("market_access", "Market access", "select", {"options": ["Poor", "Moderate", "Good"]})],
                "requirements": {"Workspace": "Food-grade workspace", "Raw material": "Reliable grain supply", "Machine": "Suitable milling equipment", "Electricity": "Reliable power", "Market": "Local selling channel"},
                "weights": {"workspace": 10, "raw_material": 17, "machine": 16, "electricity": 10, "labour": 8, "investment": 15, "storage": 10, "market_access": 14},
                "risks": ["Raw-material price", "Machine downtime", "Electricity interruptions", "Competition"],
            },
            "Spice Processing": {
                "inputs": [("workspace", "Workspace available", "select", {"options": ["No", "Partial", "Yes"]}), ("raw_material", "Raw-material availability", "select", {"options": ["Poor", "Moderate", "Good"]}), ("grinder", "Grinding/processing equipment", "select", {"options": ["No", "Partial", "Yes"]}), ("electricity", "Electricity", "select", {"options": ["No", "Limited", "Reliable"]}), ("labour", "Available labour (people)", "number", {"min_value": 0, "value": 2, "step": 1}), ("investment", "Available investment (₹)", "number", {"min_value": 0, "value": 250000, "step": 10000}), ("packaging", "Packaging availability", "select", {"options": ["Poor", "Moderate", "Good"]}), ("market_access", "Market access", "select", {"options": ["Poor", "Moderate", "Good"]})],
                "requirements": {"Workspace": "Clean processing area", "Raw material": "Reliable spice supply", "Equipment": "Grinding/packing equipment", "Packaging": "Suitable packaging", "Market": "Retail/wholesale buyers"},
                "weights": {"workspace": 10, "raw_material": 18, "grinder": 15, "electricity": 8, "labour": 8, "investment": 15, "packaging": 12, "market_access": 14},
                "risks": ["Raw-material quality", "Food safety requirements", "Packaging cost", "Competition"],
            },
            "Oil Extraction": {
                "inputs": [("workspace", "Workspace available", "select", {"options": ["No", "Partial", "Yes"]}), ("oilseed_supply", "Oilseed availability", "select", {"options": ["Poor", "Moderate", "Good"]}), ("machine", "Oil extraction machine", "select", {"options": ["No", "Partial", "Yes"]}), ("electricity", "Electricity", "select", {"options": ["No", "Limited", "Reliable"]}), ("labour", "Available labour (people)", "number", {"min_value": 0, "value": 2, "step": 1}), ("investment", "Available investment (₹)", "number", {"min_value": 0, "value": 400000, "step": 10000}), ("storage", "Storage available", "select", {"options": ["No", "Partial", "Yes"]}), ("market_access", "Market access", "select", {"options": ["Poor", "Moderate", "Good"]})],
                "requirements": {"Raw material": "Steady oilseed supply", "Machine": "Suitable extraction unit", "Electricity": "Reliable power", "Storage": "Safe storage", "Market": "Retail/wholesale market"},
                "weights": {"workspace": 8, "oilseed_supply": 18, "machine": 18, "electricity": 10, "labour": 7, "investment": 16, "storage": 8, "market_access": 15},
                "risks": ["Oilseed price", "Equipment downtime", "Quality compliance", "Competition"],
            },
            "Pickle / Jam / Food Processing": {
                "inputs": [("workspace", "Food-processing workspace", "select", {"options": ["No", "Partial", "Yes"]}), ("raw_material", "Raw-material availability", "select", {"options": ["Poor", "Moderate", "Good"]}), ("equipment", "Processing equipment", "select", {"options": ["No", "Partial", "Yes"]}), ("electricity", "Electricity", "select", {"options": ["No", "Limited", "Reliable"]}), ("labour", "Available labour (people)", "number", {"min_value": 0, "value": 2, "step": 1}), ("investment", "Available investment (₹)", "number", {"min_value": 0, "value": 150000, "step": 5000}), ("packaging", "Packaging availability", "select", {"options": ["Poor", "Moderate", "Good"]}), ("market_access", "Market access", "select", {"options": ["Poor", "Moderate", "Good"]}), ("storage", "Storage available", "select", {"options": ["No", "Partial", "Yes"]})],
                "requirements": {"Workspace": "Clean food-processing space", "Raw material": "Seasonal/local raw material", "Packaging": "Food-grade packaging", "Market": "Local retail or direct customers"},
                "weights": {"workspace": 12, "raw_material": 16, "equipment": 12, "electricity": 8, "labour": 8, "investment": 15, "packaging": 12, "market_access": 12, "storage": 5},
                "risks": ["Food spoilage", "Raw-material seasonality", "Food safety requirements", "Demand variability"],
            },
            "Milk Processing": {
                "inputs": [("milk_supply", "Milk supply availability", "select", {"options": ["Poor", "Moderate", "Good"]}), ("workspace", "Processing workspace", "select", {"options": ["No", "Partial", "Yes"]}), ("equipment", "Processing equipment", "select", {"options": ["No", "Partial", "Yes"]}), ("electricity", "Electricity", "select", {"options": ["No", "Limited", "Reliable"]}), ("cold_storage", "Cold storage/refrigeration", "select", {"options": ["No", "Partial", "Yes"]}), ("labour", "Available labour (people)", "number", {"min_value": 0, "value": 2, "step": 1}), ("investment", "Available investment (₹)", "number", {"min_value": 0, "value": 250000, "step": 10000}), ("market_access", "Market access", "select", {"options": ["Poor", "Moderate", "Good"]})],
                "requirements": {"Milk": "Reliable milk supply", "Workspace": "Clean processing area", "Cold chain": "Adequate chilling/storage", "Market": "Buyer network"},
                "weights": {"milk_supply": 20, "workspace": 10, "equipment": 15, "electricity": 10, "cold_storage": 15, "labour": 8, "investment": 10, "market_access": 12},
                "risks": ["Perishability", "Cold-chain failure", "Milk quality variation", "Food safety requirements"],
            },
        }
    },
    "Farm Services": {
        "icon": "🚜",
        "businesses": {
            "Farm Equipment Rental": {
                "inputs": [("equipment", "Equipment already available", "select", {"options": ["No", "Some", "Yes"]}), ("storage", "Equipment storage", "select", {"options": ["No", "Partial", "Yes"]}), ("capital", "Available investment (₹)", "number", {"min_value": 0, "value": 500000, "step": 10000}), ("operator", "Operator/technical labour", "number", {"min_value": 0, "value": 1, "step": 1}), ("fuel", "Fuel access", "select", {"options": ["Poor", "Moderate", "Good"]}), ("service_area", "Service area", "select", {"options": ["Village", "Multiple villages", "Taluk-wide"]}), ("farmer_demand", "Local farmer demand", "select", {"options": ["Low", "Medium", "High"]}), ("market_access", "Business/booking access", "select", {"options": ["Poor", "Moderate", "Good"]})],
                "requirements": {"Equipment": "Usable machinery/tools", "Storage": "Secure storage", "Operator": "Qualified operator where required", "Demand": "Sufficient local demand"},
                "weights": {"equipment": 20, "storage": 10, "capital": 15, "operator": 10, "fuel": 8, "service_area": 10, "farmer_demand": 17, "market_access": 10},
                "risks": ["Equipment downtime", "Fuel costs", "Low seasonal utilisation", "Maintenance costs"],
            },
            "Custom Farm Services": {
                "inputs": [("tools", "Tools/machinery available", "select", {"options": ["No", "Some", "Yes"]}), ("technical_skill", "Technical skill", "select", {"options": ["Beginner", "Intermediate", "Experienced"]}), ("operator", "Available operators", "number", {"min_value": 0, "value": 1, "step": 1}), ("fuel", "Fuel access", "select", {"options": ["Poor", "Moderate", "Good"]}), ("investment", "Available investment (₹)", "number", {"min_value": 0, "value": 300000, "step": 10000}), ("farmer_demand", "Local farmer demand", "select", {"options": ["Low", "Medium", "High"]}), ("service_area", "Service area", "select", {"options": ["Village", "Multiple villages", "Taluk-wide"]})],
                "requirements": {"Tools": "Relevant farm tools/equipment", "Skill": "Technical skill", "Demand": "Farmer demand", "Operations": "Operator availability"},
                "weights": {"tools": 18, "technical_skill": 16, "operator": 10, "fuel": 10, "investment": 14, "farmer_demand": 20, "service_area": 12},
                "risks": ["Seasonality", "Equipment breakdown", "Travel/fuel costs", "Demand uncertainty"],
            },
            "Agricultural Transport": {
                "inputs": [("vehicle", "Suitable vehicle available", "select", {"options": ["No", "Leased", "Yes"]}), ("vehicle_type", "Vehicle type", "select", {"options": ["Two-wheeler", "Auto/three-wheeler", "Pickup", "Mini truck", "Other"]}), ("storage", "Load/storage protection", "select", {"options": ["No", "Partial", "Yes"]}), ("driver", "Driver availability", "select", {"options": ["No", "Part-time", "Yes"]}), ("fuel", "Fuel access", "select", {"options": ["Poor", "Moderate", "Good"]}), ("investment", "Available investment (₹)", "number", {"min_value": 0, "value": 400000, "step": 10000}), ("farmer_demand", "Local demand", "select", {"options": ["Low", "Medium", "High"]}), ("service_area", "Service area", "select", {"options": ["Village", "Multiple villages", "Taluk-wide"]})],
                "requirements": {"Vehicle": "Suitable transport vehicle", "Driver": "Driver availability", "Demand": "Repeat local demand", "Fuel": "Fuel access"},
                "weights": {"vehicle": 20, "vehicle_type": 8, "storage": 8, "driver": 12, "fuel": 10, "investment": 15, "farmer_demand": 17, "service_area": 10},
                "risks": ["Fuel prices", "Vehicle maintenance", "Seasonal demand", "Road/transport delays"],
            },
            "Agricultural Equipment Repair": {
                "inputs": [("workshop", "Workshop space", "select", {"options": ["No", "Partial", "Yes"]}), ("tools", "Repair tools", "select", {"options": ["Poor", "Moderate", "Good"]}), ("skill", "Technical skill", "select", {"options": ["Beginner", "Intermediate", "Experienced"]}), ("spares", "Spare-parts access", "select", {"options": ["Poor", "Moderate", "Good"]}), ("electricity", "Electricity", "select", {"options": ["No", "Limited", "Reliable"]}), ("investment", "Available investment (₹)", "number", {"min_value": 0, "value": 150000, "step": 5000}), ("farmer_demand", "Local demand", "select", {"options": ["Low", "Medium", "High"]}), ("market_access", "Market access", "select", {"options": ["Poor", "Moderate", "Good"]})],
                "requirements": {"Workshop": "Repair workspace", "Tools": "Suitable repair tools", "Skill": "Technical repair skill", "Spare parts": "Reliable parts source", "Demand": "Local equipment demand"},
                "weights": {"workshop": 12, "tools": 18, "skill": 20, "spares": 13, "electricity": 8, "investment": 12, "farmer_demand": 12, "market_access": 5},
                "risks": ["Incorrect repairs", "Spare-parts delays", "Seasonality", "Equipment diversity"],
            },
        }
    },
}


# Add shared agricultural environment inputs to every agriculture activity.
# These appear only when the Agriculture domain is selected.
ENV_FACTOR_WEIGHTS = {
    "N": 9, "P": 9, "K": 9, "pH": 9,
    "Temperature": 9, "Humidity": 7, "Rainfall": 8
}

AGRICULTURE_ENV_INPUTS = [
    ("nitrogen", "Nitrogen (N)", "number", {"min_value": 0.0, "value": 70.0, "step": 1.0}),
    ("phosphorus", "Phosphorus (P)", "number", {"min_value": 0.0, "value": 40.0, "step": 1.0}),
    ("potassium", "Potassium (K)", "number", {"min_value": 0.0, "value": 40.0, "step": 1.0}),
    ("temperature", "Temperature (°C)", "number", {"min_value": -10.0, "max_value": 60.0, "value": 25.0, "step": 0.5}),
    ("humidity", "Humidity (%)", "number", {"min_value": 0.0, "max_value": 100.0, "value": 70.0, "step": 1.0}),
    ("soil_ph", "Soil pH", "number", {"min_value": 3.0, "max_value": 10.0, "value": 6.5, "step": 0.1, "format": "%.1f"}),
    ("rainfall", "Rainfall (mm)", "number", {"min_value": 0.0, "value": 700.0, "step": 25.0}),
]

for _ag_name, _ag_cfg in BUSINESS_DOMAIN_CONFIG.get("Agriculture", {}).get("businesses", {}).items():
    _existing = {x[0] for x in _ag_cfg["inputs"]}
    _extras = [x for x in AGRICULTURE_ENV_INPUTS if x[0] not in _existing]
    # Keep core environment factors together after season/land/water/irrigation.
    _ag_cfg["inputs"][0:0] = []
    insert_at = 0
    for i, item in enumerate(_ag_cfg["inputs"]):
        if item[0] in {"water", "irrigation"}:
            insert_at = i + 1
    _ag_cfg["inputs"][insert_at:insert_at] = _extras
    for _item in _extras:
        _ag_cfg["weights"].setdefault(_item[0], ENV_FACTOR_WEIGHTS.get({"nitrogen":"N","phosphorus":"P","potassium":"K","soil_ph":"pH","temperature":"Temperature","humidity":"Humidity","rainfall":"Rainfall"}.get(_item[0],""), 5))

# Category-level agriculture businesses reuse the core crop input model, while
# their candidate-crop set is filtered by category below.
_core_crop_cfg = BUSINESS_DOMAIN_CONFIG.get("Agriculture", {}).get("businesses", {}).get("Crop Cultivation", {})
for _cat_name in ("Cereals", "Pulses", "Oilseeds", "Commercial Crops"):
    if _cat_name in BUSINESS_DOMAIN_CONFIG.get("Agriculture", {}).get("businesses", {}):
        _cat_cfg = BUSINESS_DOMAIN_CONFIG["Agriculture"]["businesses"][_cat_name]
        _cat_cfg["inputs"] = list(_core_crop_cfg.get("inputs", []))
        _cat_cfg["requirements"] = dict(_core_crop_cfg.get("requirements", {}))
        _cat_cfg["weights"] = dict(_core_crop_cfg.get("weights", {}))

# Add a few direct aliases for the existing prototype business profiles.
BUSINESS_PROFILE_ALIAS = {
    "Dairy Farming": "Dairy / Milk-Based Business",
    "Goat Farming": "Goat / Sheep Rearing",
    "Sheep Farming": "Goat / Sheep Rearing",
    "Poultry Farming": "Poultry Farming",
    "Vegetable Cultivation": "Vegetable Cultivation",
    "Small Food Processing Unit": "Small Food Processing Unit",
}

FIELD_LABELS = {
    "water": "Water availability", "labour": "Labour", "investment": "Investment", "market_access": "Market access",
    "experience": "Experience", "electricity": "Electricity", "shed": "Housing/shed", "feed": "Feed availability",
    "veterinary": "Veterinary access", "fodder": "Fodder availability", "grazing": "Grazing/feed availability",
}


# ------------------------------------------------------------
# AGRICULTURE ENVIRONMENT ENGINE USED INSIDE BUSINESS RECOMMENDATION
# ------------------------------------------------------------
NPK_FILE_CANDIDATES = [
    "Crop_recommendation.csv", "crop_recommendation.csv", "Crop Recommendation.csv",
    "crop recommendation.csv", "NPK_crop_recommendation.csv"
]

@st.cache_data(show_spinner=False)
def load_npk_reference():
    """Load the uploaded NPK crop dataset when present in the app folder."""
    if pd is None:
        return None, "pandas is not installed"
    candidates = []
    for base in [Path.cwd(), Path(__file__).resolve().parent]:
        for name in NPK_FILE_CANDIDATES:
            f = base / name
            if f.exists():
                candidates.append(f)
    if not candidates:
        # Scan the app directory for compatible CSVs without requiring an exact filename.
        for f in Path.cwd().glob("*.csv"):
            try:
                cols = {str(c).strip().lower() for c in pd.read_csv(f, nrows=2).columns}
                if {"n", "p", "k", "temperature", "humidity", "ph", "rainfall", "label"}.issubset(cols):
                    candidates.append(f)
                    break
            except Exception:
                continue
    if not candidates:
        return None, "NPK reference CSV not found"
    try:
        df = pd.read_csv(candidates[0])
        rename = {c: str(c).strip().lower() for c in df.columns}
        df = df.rename(columns=rename)
        needed = ["n", "p", "k", "temperature", "humidity", "ph", "rainfall", "label"]
        if not set(needed).issubset(df.columns):
            return None, "NPK CSV does not contain the expected columns"
        for c in needed[:-1]:
            df[c] = pd.to_numeric(df[c], errors="coerce")
        df["label"] = df["label"].astype(str).str.strip()
        df = df.dropna(subset=needed[:-1] + ["label"])
        return df, str(candidates[0])
    except Exception as exc:
        return None, f"Could not load NPK reference: {type(exc).__name__}"

CROP_CANONICAL_ALIASES = {
    "rice": "rice", "paddy": "rice", "maize": "maize", "corn": "maize",
    "cotton": "cotton", "chickpea": "chickpea", "bengal gram": "chickpea",
    "bengalgram": "chickpea", "pigeonpeas": "pigeonpeas", "pigeon pea": "pigeonpeas",
    "tur": "pigeonpeas", "groundnut": "groundnut", "peanut": "groundnut",
    "mungbean": "mungbean", "green gram": "mungbean", "blackgram": "blackgram",
    "black gram": "blackgram", "lentil": "lentil", "sorghum": "sorghum", "jowar": "sorghum",
    "wheat": "wheat", "sugarcane": "sugarcane", "banana": "banana", "mango": "mango",
    "papaya": "papaya", "pomegranate": "pomegranate", "chilli": "chilli", "chili": "chilli",
    "onion": "onion", "potato": "potato", "tomato": "tomato", "cucumber": "cucumber",
}

def _canonical_crop(name):
    k = str(name).strip().lower()
    return CROP_CANONICAL_ALIASES.get(k, k)

def _factor_match_score(value, series, full_points, critical=True):
    """Rule/statistical score using p10-p90 as the strong-fit band and p05-p95 as validity band."""
    if series is None or len(series) < 5:
        return None, True, "Reference range unavailable"
    p05, p10, p90, p95 = [float(series.quantile(q)) for q in (0.05, 0.10, 0.90, 0.95)]
    x = float(value)
    if x < p05 or x > p95:
        return 0.0, (False if critical else True), f"Outside reference validity band ({p05:.1f}–{p95:.1f})"
    if p10 <= x <= p90:
        return float(full_points), True, f"Inside strong-fit band ({p10:.1f}–{p90:.1f})"
    if x < p10:
        frac = (x - p05) / max(p10 - p05, 1e-9)
    else:
        frac = (p95 - x) / max(p95 - p90, 1e-9)
    return round(full_points * (0.5 + 0.5 * max(0.0, min(1.0, frac))), 2), True, f"Near edge of reference band ({p05:.1f}–{p95:.1f})"

def agriculture_environment_analysis(location, business_name, values):
    """Score location candidate crops against user-provided environment values."""
    candidates = []
    for _, items in _agriculture_options_for_business(business_name, location):
        candidates.extend(items)
    candidates = [c for c in candidates if not str(c).startswith("No verified")]
    df, source = load_npk_reference()
    if not candidates:
        return [], source

    inputs = {
        "N": values.get("nitrogen"), "P": values.get("phosphorus"), "K": values.get("potassium"),
        "pH": values.get("soil_ph"), "Temperature": values.get("temperature"),
        "Humidity": values.get("humidity"), "Rainfall": values.get("rainfall")
    }
    results = []
    if df is None:
        for crop in candidates:
            results.append({"crop": crop, "valid": True, "score": None, "breakdown": {}, "reason": "Environmental reference dataset unavailable"})
        return results, source

    labels = df["label"].apply(_canonical_crop)
    for crop in candidates:
        canon = _canonical_crop(crop)
        sub = df[labels == canon]
        if sub.empty:
            results.append({"crop": crop, "valid": False, "score": None, "breakdown": {}, "reason": "No matching crop rows in the uploaded NPK dataset"})
            continue
        breakdown = {}
        total = 0.0
        valid = True
        reasons = []
        for factor, points in ENV_FACTOR_WEIGHTS.items():
            val = inputs.get(factor)
            if val is None:
                breakdown[factor] = "Not entered"
                continue
            col = factor.lower() if factor != "Temperature" else "temperature"
            if factor == "pH": col = "ph"
            if factor not in {"N", "P", "K", "Temperature", "Humidity", "Rainfall", "pH"}:
                continue
            series = sub[col]
            pts, ok, msg = _factor_match_score(val, series, points, critical=True)
            breakdown[factor] = {"score": pts, "max": points, "status": msg}
            if pts is not None:
                total += pts
            if not ok:
                valid = False
                reasons.append(f"{factor}: {msg}")
        results.append({"crop": crop, "valid": valid, "score": round(total, 1), "breakdown": breakdown,
                        "reason": "; ".join(reasons) if reasons else "Within the uploaded environmental reference bands"})
    results.sort(key=lambda r: (r["valid"], r["score"] if r["score"] is not None else -1), reverse=True)
    return results, source


def _profile_for_business(business_name):
    existing_name = BUSINESS_PROFILE_ALIAS.get(business_name)
    if not existing_name:
        return None
    return next((b for b in BUSINESSES if b.get("name") == existing_name), None)


def _scale_value(v, levels):
    return levels.get(v, 0.0)


def evaluate_business_config(business_name, values):
    """Adaptive 0-100 rule score. Missing/unknown inputs are excluded and the
    remaining configured weights are renormalized, so partial profiles still work."""
    _, cfg = business_config_for(business_name)
    if not cfg:
        return 0, [], ["Business configuration not found."]

    level = {
        "Poor": 0.10, "Very Low": 0.10, "Low": 0.20, "Limited": 0.40,
        "Moderate": 0.55, "Medium": 0.55, "Partial": 0.55, "Shared": 0.50,
        "Available": 0.75, "Good": 1.00, "High": 1.00, "Reliable": 1.00,
        "Yes": 1.00, "Experienced": 1.00, "Some experience": 0.65,
        "Intermediate": 0.65, "Beginner": 0.40, "No": 0.00, "None": 0.00,
        "Not sure": None, "Unknown": None, "Not provided": None, "": None
    }

    available_weight = 0.0
    earned = 0.0
    reasons = []
    gaps = []
    used_fields = 0
    missing_fields = []

    for key, weight in cfg.get("weights", {}).items():
        v = values.get(key)
        ratio = None

        if v is None or (isinstance(v, str) and v.strip() in {"", "Not sure", "Unknown", "Not provided"}):
            missing_fields.append(tr_any(FIELD_LABELS.get(key, key.replace("_", " ").title())))
            continue

        if isinstance(v, (int, float)) and not isinstance(v, bool):
            if key in {"investment", "capital"}:
                ratio = min(1.0, max(0.0, v / 100000.0))
            elif key in {"land_acres", "mulberry_land", "pond_area"}:
                ratio = min(1.0, max(0.0, v / 1.0))
            elif key in {"labour", "operator"}:
                ratio = min(1.0, max(0.0, v / 2.0))
            elif key in {"animals", "birds", "boxes", "workers"}:
                ratio = 1.0 if v > 0 else 0.0
            elif key in {"nitrogen", "phosphorus", "potassium", "soil_ph", "temperature", "humidity", "rainfall"}:
                # Environmental suitability is handled separately by the crop engine.
                # For the general business score, presence of a numeric reading earns credit.
                ratio = 1.0
            else:
                ratio = 1.0 if v > 0 else 0.0
        elif isinstance(v, str):
            ratio = level.get(v, 0.50)

        if ratio is None:
            missing_fields.append(tr_any(FIELD_LABELS.get(key, key.replace("_", " ").title())))
            continue

        ratio = max(0.0, min(1.0, float(ratio)))
        available_weight += weight
        earned += weight * ratio
        used_fields += 1

        label = tr_any(FIELD_LABELS.get(key, key.replace("_", " ").title()))
        if ratio >= 0.75:
            reasons.append(f"{label}: currently supports feasibility.")
        elif ratio < 0.45:
            gaps.append(f"{label}: needs attention before starting.")

    if available_weight <= 0:
        return 0, ["No usable business inputs were provided."], ["Provide at least the core inputs for the selected business."]

    score = round((earned / available_weight) * 100)
    if missing_fields:
        gaps.append("Missing or unknown inputs not used in the score: " + ", ".join(missing_fields[:6]) + ("..." if len(missing_fields) > 6 else ""))
    reasons.append(f"Adaptive scoring used {used_fields} available factor(s) and renormalized the configured weights.")
    return max(0, min(100, score)), reasons, gaps


def business_config_for(name):
    for domain_name, domain in BUSINESS_DOMAIN_CONFIG.items():
        if name in domain["businesses"]:
            return domain_name, domain["businesses"][name]
    return None, None


def render_business_input(key, label, kind, options, widget_key):
    """Render an input with consistent microcopy, tooltip, and practical defaults."""
    help_map = {
        "nitrogen": "Use the latest soil-test N value; this helps compare crop requirements.",
        "phosphorus": "Use the latest soil-test P value.",
        "potassium": "Use the latest soil-test K value.",
        "soil_ph": "Use the latest soil-test pH; most crops have a preferred pH band.",
        "temperature": "Enter the expected temperature during the production period.",
        "humidity": "Enter typical relative humidity for the production area.",
        "rainfall": "Enter expected seasonal rainfall or the relevant production-period value.",
        "investment": "Enter only capital you can actually deploy for this business.",
        "capital": "Enter the capital available for the service/business setup.",
        "land_acres": "Enter usable area, not total owned land if part is unavailable.",
        "pond_area": "Enter usable pond/culture area in acres.",
        "market_access": "Rate the practical access you have to buyers after transport and handling.",
        "water": "Select the dependable water availability for the planned scale.",
        "irrigation": "Select the irrigation reliability you can maintain during the production cycle.",
        "labour": "Enter people who can reliably work on the activity when needed.",
        "income_time": "Choose the time window in which you need the activity to start generating income.",
        "experience": "Choose the experience level you can rely on for this activity.",
        "farmer_demand": "Estimate current local demand from farmers or service buyers.",
        "electricity": "Consider the reliability of the electricity connection at the operating site.",
        "veterinary": "Select access to dependable animal-health support.",
        "water_quality": "Use a recent water-quality test where available.",
        "soil_type": "Choose the dominant soil type in the proposed production area.",
        "season": "Choose the intended production season.",
    }
    placeholder_map = {
        "text": "Enter a practical value",
    }
    help_text = help_map.get(key, f"Provide the most realistic current value for {label.lower()}.")
    if kind == "number":
        return st.number_input(tr_any(label), key=widget_key, help=tr_any(help_text), **options)
    if kind == "select":
        return st.selectbox(tr_any(label), options["options"], key=widget_key, help=tr_any(help_text), format_func=tr_any)
    if kind == "text":
        return st.text_input(tr_any(label), key=widget_key, help=tr_any(help_text), placeholder=tr_any(placeholder_map["text"]))
    return st.text_input(tr_any(label), key=widget_key, help=tr_any(help_text), placeholder=tr_any(placeholder_map["text"]))


def _input_group(key):
    """Map business-specific inputs into three progressive-disclosure cards."""
    climate = {"season","temperature","humidity","rainfall","climate","location","species","animal_type","breed","fish_species","plant","flower","product","service_type","equipment","vehicle_type","business_type"}
    soil_water = {"nitrogen","phosphorus","potassium","soil_ph","soil_type","soil_test","water","irrigation","water_quality","water_source","water_depth","pond_area","culture_area","land_acres","mulberry_land","growing_medium","feed","fodder","grazing","storage","cold_storage","drying","protected","shed","shed_area"}
    financial = {"investment","capital","working_capital","market_access","income_time","time_to_income","income_goal","risk_preference","experience","labour","workers","operator","driver","electricity","transport","farmer_demand","service_area","capacity","workspace","machinery","packaging"}
    if key in climate:
        return "location_climate"
    if key in soil_water:
        return "soil_water"
    if key in financial:
        return "capital_financial"
    return "capital_financial"


def _md_table(headers, rows):
    """Render a compact styled Markdown-like HTML table for comparison grids."""
    def esc(v):
        return str(v).replace("&","&amp;").replace("<","&lt;").replace(">","&gt;").replace("|","&#124;")
    html=['<div class="gs-table-wrap"><table class="gs-table"><thead><tr>']
    html += [f'<th>{esc(h)}</th>' for h in headers]
    html.append('</tr></thead><tbody>')
    for row in rows:
        html.append('<tr>' + ''.join(f'<td>{esc(cell)}</td>' for cell in row) + '</tr>')
    html.append('</tbody></table></div>')
    st.markdown(''.join(html), unsafe_allow_html=True)


def business_success_rate(score):
    """Backward-compatible helper; returns the feasibility score, not a probability."""
    return max(0, min(100, round(float(score))))



# ------------------------------------------------------------
# BUSINESS RECOMMENDATION OUTPUT
# ------------------------------------------------------------

BUSINESS_OPTION_LIBRARY = {
    "Vegetable Cultivation": [
        {"name": "Tomato", "space": "Open field / protected cultivation depending on scale", "climate": "Warm conditions; verify season and local suitability", "cycle": "Typically a few months; verify variety and season", "market": "Local mandi, retailers, hotels, direct consumers"},
        {"name": "Onion", "space": "Open field; requires suitable soil and drainage", "climate": "Cooler growth period with suitable moisture management", "cycle": "Season-dependent", "market": "Mandi, wholesalers, retailers, institutional buyers"},
        {"name": "Chilli", "space": "Open field; spacing depends on variety", "climate": "Warm climate with controlled moisture", "cycle": "Season- and variety-dependent", "market": "Mandi, traders, processors, retailers"},
    ],
    "Fruit Cultivation": [
        {"name": "Banana", "space": "Open field with reliable water and drainage", "climate": "Warm conditions; frost-free environment preferred", "cycle": "Typically around one year depending on cultivar", "market": "Wholesalers, retailers, institutional buyers"},
        {"name": "Papaya", "space": "Open field with drainage and irrigation", "climate": "Warm conditions", "cycle": "Generally faster than orchard crops; cultivar-dependent", "market": "Wholesalers, retailers, processors"},
        {"name": "Guava", "space": "Orchard space with irrigation", "climate": "Warm to subtropical conditions", "cycle": "Longer establishment period; perennial crop", "market": "Fruit traders, retailers, processors"},
    ],
    "Floriculture": [
        {"name": "Rose", "space": "Open field or protected structure depending on production model", "climate": "Variety- and production-system dependent", "cycle": "Repeated harvest after establishment", "market": "Flower markets, florists, decorators, events"},
        {"name": "Gerbera", "space": "Often grown under protected cultivation for commercial consistency", "climate": "Needs controlled growing conditions for commercial quality", "cycle": "Repeated flower harvest after establishment", "market": "Florists, decorators, events, wholesale flower markets"},
        {"name": "Marigold", "space": "Open field", "climate": "Warm conditions; season-dependent", "cycle": "Shorter seasonal cycle than perennial flowers", "market": "Temples, events, florists, wholesale markets"},
    ],
    "Poultry Farming": [
        {"name": "Broiler Poultry", "space": "Shed space sized to flock density and local standards", "climate": "Requires ventilation and temperature management", "cycle": "Short production cycle; verify target live weight and local system", "market": "Local traders, retailers, restaurants, institutional buyers"},
        {"name": "Layer Poultry", "space": "Layer housing with adequate feeding, water and ventilation", "climate": "Requires environmental control and biosecurity", "cycle": "Longer production cycle than broilers; egg production is recurring", "market": "Egg wholesalers, retailers, bakeries, institutions"},
        {"name": "Rural Poultry", "space": "Smaller housing/free-range space depending on system", "climate": "Adapted to local conditions; health management remains essential", "cycle": "Longer/variable cycle than commercial broilers", "market": "Local households, traders, premium/direct buyers"},
    ],
    "Dairy Farming": [
        {"name": "Dairy Cattle", "space": "Covered shed with clean resting, feeding and drainage area", "climate": "Needs heat-stress and water management", "cycle": "Recurring milk production after calving; herd replacement is long-term", "market": "Milk collection centres, local retailers, direct consumers"},
        {"name": "Dairy Buffalo", "space": "Shed plus adequate water/cooling arrangements", "climate": "Strong attention to heat and water management", "cycle": "Recurring milk production after calving", "market": "Milk collection, dairies, local consumers"},
    ],
    "Goat Farming": [
        {"name": "Meat Goat Unit", "space": "Dry, ventilated shelter with feeding and movement area", "climate": "Generally adaptable; disease and heat management matter", "cycle": "Multiple growth/reproduction cycles; scale determines sales timing", "market": "Livestock traders, local markets, direct buyers"},
        {"name": "Breeding Goat Unit", "space": "Shelter plus controlled breeding area", "climate": "Local adaptation and health management required", "cycle": "Longer breeding cycle than short-term fattening", "market": "Breeding-stock buyers and livestock markets"},
    ],
    "Sheep Farming": [
        {"name": "Sheep Meat Unit", "space": "Dry shelter plus grazing/feed area", "climate": "Breed and local conditions determine suitability", "cycle": "Growth and breeding cycle depends on flock system", "market": "Livestock traders, local markets, institutional buyers"},
        {"name": "Sheep Breeding Unit", "space": "Shelter and managed breeding area", "climate": "Local breed and weather compatibility should be verified", "cycle": "Breeding cycle is longer than simple fattening", "market": "Breeding-stock buyers, livestock markets"},
    ],
    "Fish Farming": [
        {"name": "Freshwater Fish Farming", "space": "Pond/tank area sized to stocking and water management capacity", "climate": "Species-specific; water temperature and quality must be monitored", "cycle": "Species and stocking model dependent", "market": "Local fish markets, wholesalers, restaurants, direct buyers"},
        {"name": "Composite Fish Culture", "space": "Pond with adequate water management", "climate": "Species combination must match local water conditions", "cycle": "Species and stocking schedule dependent", "market": "Local markets, wholesalers and institutional buyers"},
    ],
    "Plant Nursery": [
        {"name": "Fruit Sapling Nursery", "space": "Nursery beds/containers with irrigation and shade/protection", "climate": "Depends on species and nursery conditions", "cycle": "Saleable stage varies by plant species", "market": "Farmers, gardeners, landscapers, horticulture projects"},
        {"name": "Vegetable Seedling Nursery", "space": "Protected/managed nursery area", "climate": "Requires controlled moisture and nursery hygiene", "cycle": "Short-cycle seedling production", "market": "Vegetable farmers, local growers, FPOs"},
        {"name": "Ornamental Nursery", "space": "Nursery space with shade and irrigation", "climate": "Species-dependent", "cycle": "Varies by plant", "market": "Households, landscapers, institutions"},
    ],
    "Beekeeping": [
        {"name": "Honey Bee Apiary", "space": "Apiary location with safe hive placement and access to forage", "climate": "Depends on forage availability and seasonal conditions", "cycle": "Honey harvest is seasonal/management-dependent", "market": "Direct consumers, retailers, processors"},
        {"name": "Migratory Beekeeping", "space": "Apiary equipment plus transport/logistics capability", "climate": "Follows flowering seasons across locations", "cycle": "Multiple seasonal honey flows possible", "market": "Bulk buyers, processors, direct retail"},
    ],
    "Mushroom Cultivation": [
        {"name": "Oyster Mushroom", "space": "Clean growing room or controlled production area", "climate": "Needs variety-specific temperature and humidity control", "cycle": "Short production cycles under suitable conditions", "market": "Local retailers, restaurants, direct consumers"},
        {"name": "Button Mushroom", "space": "More controlled production environment", "climate": "Requires tighter environmental management", "cycle": "Short production cycles under controlled conditions", "market": "Retailers, restaurants, institutional buyers"},
    ],
    "Sericulture": [
        {"name": "Mulberry Sericulture", "space": "Mulberry acreage plus rearing house", "climate": "Requires suitable mulberry growth and silkworm rearing conditions", "cycle": "Crop and silkworm cycles are seasonal/management-dependent", "market": "Cocoon markets, reelers, silk value chain"},
    ],
}

BUSINESS_ADVICE = {
    "Poultry Farming": {
        "advice": [
            "Secure chicks, feed and veterinary support before stocking the first batch.",
            "Use a written feed, vaccination, mortality and cleaning schedule.",
            "Pre-arrange at least one reliable buyer and transport route before the sale window.",
        ],
        "steps": [
            "Complete shed preparation, ventilation, water, sanitation and biosecurity checks.",
            "Confirm chick supplier, feed supplier and health-support contact.",
            "Start the pilot batch at the selected scale and record daily feed use, mortality and growth.",
            "Lock the buyer/market route before the birds reach sale weight.",
            "Compare actual cycle cost and sales with the plan before expanding.",
        ],
    },
    "Dairy Farming": {
        "advice": [
            "Do not scale the herd beyond dependable fodder, water, shed and labour capacity.",
            "Track feed cost and milk yield animal-by-animal.",
            "Secure a milk collection or direct-selling channel before adding animals.",
        ],
        "steps": [
            "Prepare shed, drainage, water, fodder storage and cleaning arrangements.",
            "Finalize animal sourcing, veterinary support and feeding plan.",
            "Set up milk collection, chilling/transport or direct-sale arrangements.",
            "Start with the planned herd size and record yield, feed and health costs.",
            "Review the first production period before adding more animals.",
        ],
    },
    "Goat Farming": {
        "advice": [
            "Match herd size to year-round feed and water availability.",
            "Use dry housing, routine vaccination/deworming and quick disease response.",
            "Plan sales around local livestock-market demand rather than only herd growth.",
        ],
        "steps": [
            "Prepare secure shelter, fencing, feeding and water arrangements.",
            "Source healthy stock from a reliable supplier and arrange veterinary support.",
            "Set a feeding and health-monitoring schedule.",
            "Identify buyers and transport before the target sale period.",
            "Review mortality, feed cost and realized sale price before scaling.",
        ],
    },
    "Sheep Farming": {
        "advice": [
            "Plan flock size around grazing/feed availability and seasonal shortages.",
            "Maintain dry housing and preventive health management.",
            "Use market-linked sale planning instead of holding animals without a cost limit.",
        ],
        "steps": [
            "Prepare shelter, fencing, water and feed/grazing arrangements.",
            "Source healthy animals and arrange veterinary support.",
            "Set a vaccination, parasite-control and record-keeping routine.",
            "Confirm market and transport arrangements before sale.",
            "Review actual cost per animal and realized price before expansion.",
        ],
    },
    "Fish Farming": {
        "advice": [
            "Do not stock fish until pond condition and water quality are verified.",
            "Select species based on water conditions and the local selling channel.",
            "Monitor feed use, water quality, mortality and growth throughout the cycle.",
        ],
        "steps": [
            "Test and prepare the pond/water system before stocking.",
            "Confirm species, stocking plan and dependable seed/feed suppliers.",
            "Start the production cycle with a documented feeding and water-quality schedule.",
            "Secure buyers and harvesting/transport arrangements ahead of harvest.",
            "Review production cost, survival and realized sale price before increasing stocking density.",
        ],
    },
    "Plant Nursery": {
        "advice": [
            "Produce varieties with verified local demand instead of maximizing variety.",
            "Prioritize planting-material quality, irrigation and nursery hygiene.",
            "Track survival rate and sales by plant type before expanding.",
        ],
        "steps": [
            "Prepare nursery beds/containers, shade/protection and irrigation.",
            "Source reliable planting material and production inputs.",
            "Plan production batches around local planting seasons and customer demand.",
            "Build farmer, landscaper and retail buyer channels.",
            "Scale only after observing actual survival and sales data.",
        ],
    },
    "Beekeeping": {
        "advice": [
            "Verify forage/flower availability before placing colonies.",
            "Plan colony-health monitoring and pest management from day one.",
            "Use direct sales and quality packaging where local demand supports it.",
        ],
        "steps": [
            "Select a suitable apiary location and prepare hives/equipment.",
            "Source healthy colonies and establish forage/season management.",
            "Maintain routine inspection, pest and colony-health records.",
            "Prepare extraction, packaging and buyer arrangements.",
            "Review honey yield per colony and sales realization before adding colonies.",
        ],
    },
    "Mushroom Cultivation": {
        "advice": [
            "Treat contamination control and environmental stability as core production priorities.",
            "Secure reliable spawn and substrate before starting a batch.",
            "Pre-arrange fast local sales because fresh mushrooms are perishable.",
        ],
        "steps": [
            "Prepare a clean growing room and verify temperature/humidity control.",
            "Secure spawn, substrate and packaging supplies.",
            "Run a small pilot batch and record contamination and yield.",
            "Build retail, restaurant or direct-consumer sales before increasing batches.",
            "Scale only after the first batches show repeatable production and sales.",
        ],
    },
    "Sericulture": {
        "advice": [
            "Keep mulberry leaf availability ahead of planned silkworm capacity.",
            "Control rearing hygiene and monitor disease early.",
            "Align cocoon production with the local market/collection schedule.",
        ],
        "steps": [
            "Prepare mulberry area, irrigation and rearing space.",
            "Arrange healthy silkworm seed and technical support.",
            "Maintain feeding, hygiene and disease-monitoring schedules.",
            "Confirm cocoon collection/market arrangements.",
            "Review leaf use, labour, cocoon output and sale realization before scaling.",
        ],
    },
}

DEFAULT_ADVICE = [
    "Verify the main technical requirement and market channel before committing the full investment.",
    "Use current local quotations for the startup and working-capital plan.",
    "Start with a manageable pilot and scale only after recording actual operating results.",
]

DEFAULT_STEPS = [
    "Verify site/infrastructure and compliance requirements.",
    "Secure reliable input/resource suppliers.",
    "Run a small pilot and record actual operating performance.",
    "Secure a market channel before the sale/harvest/service window.",
    "Review actual costs, sales and operational problems before scaling.",
]

BUSINESS_SCHEME_MAP = {
    "Crop Cultivation": ["Kisan Credit Card (KCC)", "Agriculture Infrastructure Fund (AIF)"],
    "Vegetable Cultivation": ["Mission for Integrated Development of Horticulture (MIDH)", "National Horticulture Board (NHB) Schemes", "Kisan Credit Card (KCC)"],
    "Fruit Cultivation": ["Mission for Integrated Development of Horticulture (MIDH)", "National Horticulture Board (NHB) Schemes", "Kisan Credit Card (KCC)"],
    "Spice Cultivation": ["Mission for Integrated Development of Horticulture (MIDH)", "National Horticulture Board (NHB) Schemes", "Kisan Credit Card (KCC)"],
    "Floriculture": ["Mission for Integrated Development of Horticulture (MIDH)", "National Horticulture Board (NHB) Schemes", "Agriculture Infrastructure Fund (AIF)"],
    "Poultry Farming": ["National Livestock Mission (NLM-EDP)", "Kisan Credit Card (KCC)", "Pradhan Mantri MUDRA Yojana (PMMY)"],
    "Dairy Farming": ["Animal Husbandry Infrastructure Development Fund (AHIDF)", "Kisan Credit Card (KCC)", "Pradhan Mantri MUDRA Yojana (PMMY)"],
    "Goat Farming": ["National Livestock Mission (NLM-EDP)", "Kisan Credit Card (KCC)"],
    "Sheep Farming": ["National Livestock Mission (NLM-EDP)", "Kisan Credit Card (KCC)"],
    "Fish Farming": ["Fisheries and Aquaculture Infrastructure Development Fund (FIDF)", "Kisan Credit Card (KCC)", "Agriculture Infrastructure Fund (AIF)"],
    "Plant Nursery": ["Mission for Integrated Development of Horticulture (MIDH)", "National Horticulture Board (NHB) Schemes", "Agriculture Infrastructure Fund (AIF)"],
    "Vegetable Cultivation": ["Mission for Integrated Development of Horticulture (MIDH)", "National Horticulture Board (NHB) Schemes", "Kisan Credit Card (KCC)"],
    "Fruit Cultivation": ["Mission for Integrated Development of Horticulture (MIDH)", "National Horticulture Board (NHB) Schemes", "Kisan Credit Card (KCC)"],
    "Floriculture": ["Mission for Integrated Development of Horticulture (MIDH)", "National Horticulture Board (NHB) Schemes", "Agriculture Infrastructure Fund (AIF)"],
    "Beekeeping": ["National Livestock Mission (NLM)", "Kisan Credit Card (KCC)", "PMEGP – Prime Minister's Employment Generation Programme"],
    "Mushroom Cultivation": ["Mission for Integrated Development of Horticulture (MIDH)", "PMEGP – Prime Minister's Employment Generation Programme", "Kisan Credit Card (KCC)"],
    "Sericulture": ["Mission for Integrated Development of Horticulture (MIDH)", "Kisan Credit Card (KCC)", "PMEGP – Prime Minister's Employment Generation Programme"],
    "Grain Milling": ["PMFME – Pradhan Mantri Formalisation of Micro Food Processing Enterprises", "Agriculture Infrastructure Fund (AIF)", "Pradhan Mantri MUDRA Yojana (PMMY)"],
    "Spice Processing": ["PMFME – Pradhan Mantri Formalisation of Micro Food Processing Enterprises", "Agriculture Infrastructure Fund (AIF)", "Pradhan Mantri MUDRA Yojana (PMMY)"],
    "Oil Extraction": ["PMFME – Pradhan Mantri Formalisation of Micro Food Processing Enterprises", "Agriculture Infrastructure Fund (AIF)", "Pradhan Mantri MUDRA Yojana (PMMY)"],
    "Pickle / Jam / Food Processing": ["PMFME – Pradhan Mantri Formalisation of Micro Food Processing Enterprises", "Pradhan Mantri MUDRA Yojana (PMMY)", "PMEGP – Prime Minister's Employment Generation Programme"],
    "Milk Processing": ["PMFME – Pradhan Mantri Formalisation of Micro Food Processing Enterprises", "AHIDF", "Pradhan Mantri MUDRA Yojana (PMMY)"],
    "Farm Equipment Rental": ["Agriculture Infrastructure Fund (AIF)", "Pradhan Mantri MUDRA Yojana (PMMY)", "ACABC"],
    "Custom Farm Services": ["Agriculture Infrastructure Fund (AIF)", "Pradhan Mantri MUDRA Yojana (PMMY)", "ACABC"],
    "Agricultural Transport": ["Pradhan Mantri MUDRA Yojana (PMMY)", "PMEGP – Prime Minister's Employment Generation Programme"],
    "Agricultural Equipment Repair": ["Pradhan Mantri MUDRA Yojana (PMMY)", "PMEGP – Prime Minister's Employment Generation Programme"],
}

SCHEME_DETAILS = {
    "National Livestock Mission (NLM-EDP)": {
        "what_it_is": "Entrepreneurship support under the National Livestock Mission for specified rural poultry and small-ruminant activities, including entrepreneurship development in rural poultry and sheep/goat sectors.",
        "benefit": "Eligible projects can receive scheme-based capital subsidy/incentive support subject to the current component guidelines and approval process.",
        "eligibility": "Current guidelines specify eligible entities and project conditions; examples include individuals, SHGs, FPOs/FCOs, JLGs and Section 8 companies, with conditions such as trained entrepreneurship/expert support and land/loan or guarantee requirements for relevant components.",
        "use": "Relevant for eligible poultry or sheep/goat entrepreneurship, breed-development units and specified feed/fodder activities.",
        "note": "Eligibility, subsidy amount, project size and application route depend on the exact NLM component selected.",
        "source": "Department of Animal Husbandry & Dairying (DAHD) — National Livestock Mission / NLM-EDP"
    },
    "Animal Husbandry Infrastructure Development Fund (AHIDF)": {
        "what_it_is": "A financing support scheme for eligible animal-husbandry infrastructure and value-addition investments.",
        "benefit": "Current DAHD information covers dairy processing/value addition, meat processing, animal feed, breed improvement/multiplication, veterinary vaccine/drug manufacturing and animal-waste-to-wealth infrastructure; financing support is subject to scheme terms.",
        "eligibility": "Eligible individuals, private companies, MSMEs, FPOs, Section 8 companies and dairy cooperatives may qualify for specified activities under the current operational guidelines.",
        "use": "Most relevant when the business involves eligible dairy processing, feed, breeding, processing or other qualifying infrastructure rather than ordinary small livestock rearing alone.",
        "note": "Do not treat AHIDF as an automatic subsidy for every dairy or livestock unit; the exact infrastructure/activity must fall within the current eligible categories.",
        "source": "Department of Animal Husbandry & Dairying (DAHD) — AHIDF"
    },
    "Fisheries and Aquaculture Infrastructure Development Fund (FIDF)": {
        "what_it_is": "A concessional-finance framework for eligible fisheries and aquaculture infrastructure projects.",
        "benefit": "Financing support is available for eligible fisheries/aquaculture infrastructure through designated channels, subject to current scheme conditions.",
        "eligibility": "Eligibility depends on the beneficiary/project category and the infrastructure activity covered by the current FIDF guidelines.",
        "use": "Relevant for eligible aquaculture/fisheries infrastructure rather than treating it as a universal operating subsidy.",
        "note": "Check current FIDF validity, eligible activities and lending route before preparing a project.",
        "source": "Department of Fisheries, Government of India — FIDF"
    },
    "Mission for Integrated Development of Horticulture (MIDH)": {
        "what_it_is": "A horticulture development scheme supporting eligible horticulture activities through centrally supported/state implementation mechanisms.",
        "benefit": "Support varies by component and can cover specified horticulture development, planting material, protected cultivation, post-harvest or related infrastructure depending on the applicable component.",
        "eligibility": "Component-specific norms, cost ceilings, beneficiary conditions and implementation arrangements apply.",
        "use": "Relevant to eligible horticulture activities such as fruits, vegetables, flowers, nurseries and protected cultivation where the chosen component is covered.",
        "note": "Exact assistance must be checked against the current component and Karnataka/state implementation guidelines.",
        "source": "Mission for Integrated Development of Horticulture (MIDH) / horticulture implementation guidelines"
    },
    "National Horticulture Board (NHB) Schemes": {
        "what_it_is": "NHB schemes support eligible commercial horticulture and related infrastructure/projects under current operational guidelines.",
        "benefit": "Assistance depends on the specific NHB scheme/component, project type, cost norms and admissibility conditions.",
        "eligibility": "Project-specific technical, financial and implementation requirements apply.",
        "use": "Relevant for eligible commercial horticulture, protected cultivation and related infrastructure where an NHB component applies.",
        "note": "Do not show an NHB benefit as guaranteed; the project must satisfy the current NHB guidelines and approval process.",
        "source": "National Horticulture Board (NHB)"
    },
    "Agriculture Infrastructure Fund (AIF)": {
        "what_it_is": "A financing facility for eligible post-harvest management and agricultural infrastructure projects.",
        "benefit": "Official scheme material provides eligible borrowers with interest-support and credit-facilitation benefits subject to scheme conditions.",
        "eligibility": "Eligibility depends on the borrower category and the infrastructure asset/project being financed.",
        "use": "More relevant to storage, grading, aggregation, primary processing and other eligible agricultural infrastructure than routine cultivation expenses.",
        "note": "The recommended project must fit an eligible infrastructure category and the current lending guidelines.",
        "source": "Government of India — Agriculture Infrastructure Fund"
    },
    "Kisan Credit Card (KCC)": {
        "what_it_is": "A formal agricultural credit mechanism for eligible crop and allied working-capital requirements.",
        "benefit": "Provides access to institutional credit for eligible agricultural/allied needs, subject to lender and eligibility conditions.",
        "eligibility": "Farmer/borrower eligibility and sanctioned limits depend on the participating financial institution and applicable KCC rules.",
        "use": "Relevant for working-capital needs in eligible crop and allied agricultural activities.",
        "note": "KCC is credit, not a direct capital subsidy; repayment and lending conditions apply.",
        "source": "Government of India / participating financial institutions"
    },
    "Pradhan Mantri MUDRA Yojana (PMMY)": {
        "what_it_is": "Institutional micro-credit support for eligible micro-enterprises through participating lenders.",
        "benefit": "Can support eligible micro-business financing needs subject to lender assessment and current PMMY categories/conditions.",
        "eligibility": "Eligibility and sanctioned amount depend on the business, applicant and participating lender.",
        "use": "Potentially relevant to small non-farm and eligible service/trading/manufacturing micro-enterprises, including some rural businesses.",
        "note": "The scheme does not guarantee approval; the lender assesses the application.",
        "source": "Department of Financial Services / participating lenders"
    },
    "PMEGP – Prime Minister's Employment Generation Programme": {
        "what_it_is": "A credit-linked programme supporting eligible new micro-enterprises through bank finance and margin-money subsidy.",
        "benefit": "Eligible projects may receive margin-money subsidy subject to current PMEGP guidelines, category and project conditions.",
        "eligibility": "Applicant, activity, project-cost and other eligibility requirements under the current PMEGP guidelines apply.",
        "use": "Relevant for eligible new micro-enterprise activities, particularly non-farm manufacturing and service enterprises and other covered activities.",
        "note": "The selected business must be an eligible PMEGP activity; subsidy is not automatic.",
        "source": "KVIC / Ministry of MSME — PMEGP"
    },
    "Agri-Clinics and Agri-Business Centres (ACABC)": {
        "what_it_is": "Support framework for eligible trained agriculture professionals establishing agri-clinics and agri-business centres.",
        "benefit": "Provides eligible project support according to current ACABC training, finance and subsidy provisions.",
        "eligibility": "Training/qualification, project, financing and other current ACABC conditions apply.",
        "use": "Relevant to agriculture advisory, farm services, input/services and eligible agri-business models.",
        "note": "Not intended as a general subsidy for every farm business.",
        "source": "MANAGE / Ministry of Agriculture & Farmers Welfare — ACABC"
    },
    "National Beekeeping and Honey Mission (NBHM)": {
        "what_it_is": "A national support programme for scientific beekeeping, honey and related value-chain development under the applicable programme guidelines.",
        "benefit": "Support depends on the approved activity/component and implementing agency; assistance can be linked to beekeeping development, equipment, training or value-chain activities where permitted.",
        "eligibility": "Beneficiary and activity conditions vary by component and implementing agency.",
        "use": "Relevant to eligible beekeeping and honey-value-chain activities.",
        "note": "Check the current implementing-agency guidelines before treating a component as available to an individual applicant.",
        "source": "Government of India — National Beekeeping and Honey Mission"
    },
    "PMFME – Pradhan Mantri Formalisation of Micro Food Processing Enterprises": {
        "what_it_is": "A food-processing enterprise support scheme covering eligible micro food-processing units and group/common-infrastructure models.",
        "benefit": "For eligible individual micro food-processing units, the official PMFME portal states credit-linked capital subsidy of 35% of eligible project cost, up to ₹10 lakh per unit; group/common infrastructure has separate limits and conditions.",
        "eligibility": "Eligibility, beneficiary contribution, bank finance, ODOP alignment and other current PMFME conditions apply.",
        "use": "Directly relevant to eligible micro food-processing activities such as spice processing, milling, pickles and other value-added food products.",
        "note": "The subsidy is credit-linked and subject to the current PMFME guidelines and approval process.",
        "source": "Ministry of Food Processing Industries (MoFPI) — PMFME"
    },
}

SCHEME_ALIASES = {
    "AHIDF": "Animal Husbandry Infrastructure Development Fund (AHIDF)",
    "FIDF": "Fisheries and Aquaculture Infrastructure Development Fund (FIDF)",
}

def related_scheme_names(business_name, profile=None):
    names = BUSINESS_SCHEME_MAP.get(business_name, [])
    if not names and profile:
        names = profile.get("schemes", [])
    normalized = [SCHEME_ALIASES.get(n, n) for n in names]
    # Resolve common naming variants to the actual keys available in SCHEME_DETAILS.
    detail_keys = set(SCHEME_DETAILS.keys())
    aliases = {
        "National Livestock Mission (NLM-EDP)": "National Livestock Mission (NLM)",
        "Kisan Credit Card": "Kisan Credit Card (KCC)",
        "PM MUDRA Yojana (PMMY)": "Pradhan Mantri MUDRA Yojana (PMMY)",
    }
    normalized = [aliases.get(n, n) for n in normalized]
    return [n for n in dict.fromkeys(normalized) if n in detail_keys]

def _location_category_crops(location):
    """Return all crops configured for the selected location, grouped by category."""
    crops = suitable_crops_for_location(location)
    grouped = {}
    for crop in crops:
        category = crop_category(crop)
        grouped.setdefault(category, []).append(crop)
    order = ["Vegetable", "Leafy", "Fruit", "Horticulture", "Cereal", "Pulse", "Oilseed", "Spice", "Commercial", "Other"]
    return {k: grouped[k] for k in order if k in grouped}

def _agriculture_options_for_business(name, location):
    grouped = _location_category_crops(location)
    if name == "Vegetable Cultivation":
        return [("Vegetables", grouped.get("Vegetable", []) + grouped.get("Leafy", []))]
    if name == "Fruit Cultivation":
        return [("Fruits", grouped.get("Fruit", []) + grouped.get("Horticulture", []))]
    if name == "Cereals":
        return [("Cereals", grouped.get("Cereal", []))]
    if name == "Pulses":
        return [("Pulses", grouped.get("Pulse", []))]
    if name == "Oilseeds":
        return [("Oilseeds", grouped.get("Oilseed", []))]
    if name == "Spice Cultivation":
        return [("Spices", grouped.get("Spice", []))]
    if name == "Commercial Crops":
        return [("Commercial Crops", grouped.get("Commercial", []))]
    if name == "Floriculture":
        return [("Flowers", [])]
    if name in {"Crop Cultivation", "Plant Nursery"}:
        return [(k, v) for k, v in grouped.items()]
    return []

def _option_candidates(name, domain_name, location):
    if domain_name == "Agriculture":
        grouped = _agriculture_options_for_business(name, location)
        if any(items for _, items in grouped):
            return grouped
        if name == "Floriculture":
            return [("Flowers", ["No verified location-to-flower mapping is present in the current dataset."])]
    opts = BUSINESS_OPTION_LIBRARY.get(name, [])
    if opts:
        return [("Business options", opts[:3])]
    return []

def dynamic_risk_analysis(name, cfg, values, score, location):
    """Generate risks from the selected business AND the user's actual inputs.
    This is a rule-based decision-support layer, not a statistical probability model.
    """
    risks = []

    def add(title, level, trigger, mitigation):
        impact_map = {"High": "High potential impact", "Medium": "Moderate potential impact", "Low": "Lower potential impact"}
        risks.append({
            "title": title,
            "level": level,
            "trigger": trigger,
            "impact": impact_map.get(level, "Potential impact"),
            "mitigation": mitigation,
        })

    water = str(values.get("water", ""))
    irrigation = str(values.get("irrigation", ""))
    market = str(values.get("market_access", ""))
    vet = str(values.get("veterinary", ""))
    feed = str(values.get("feed", values.get("fodder", "")))
    electricity = str(values.get("electricity", ""))
    labour = safe_float(values.get("labour", 0))
    investment = safe_float(values.get("investment", 0))
    experience = str(values.get("experience", ""))
    transport = str(values.get("transport", ""))
    shed = str(values.get("shed", ""))
    storage = str(values.get("storage", ""))
    equipment = str(values.get("equipment", ""))
    soil_test = str(values.get("soil_test", ""))
    income_time = str(values.get("income_time", ""))

    # Universal commercial risks driven by actual conditions.
    if market == "Poor":
        add("Market-access risk", "High",
            "The selected market-access level is Poor.",
            "Identify at least two buyers before scaling, compare local prices weekly, and avoid expanding production until a selling channel is confirmed.")
    elif market == "Moderate":
        add("Market-access risk", "Medium",
            "The selected market-access level is Moderate.",
            "Maintain at least two buyer channels and compare prices before each sales cycle.")

    if investment <= 0:
        add("Capital risk", "High",
            "No available investment has been entered.",
            "Prepare a complete startup and working-capital budget before committing to the activity.")
    elif score < 60:
        add("Execution-capital risk", "High",
            f"Current feasibility score is {score}/100.",
            "Start with a smaller pilot, close the highest-impact resource gaps, and only then consider scaling.")

    if experience == "Beginner":
        add("Experience / execution risk", "Medium",
            "The selected experience level is Beginner.",
            "Use a small pilot, obtain practical training, and arrange mentoring or technical support before full-scale operation.")

    if labour == 0 and "labour" in cfg.get("weights", {}):
        add("Labour-availability risk", "High",
            "Available labour is zero while the business requires labour.",
            "Secure named workers or service support before launch and define peak-season labour requirements.")
    elif labour < 1 and "labour" in cfg.get("weights", {}):
        add("Labour-availability risk", "Medium",
            "Limited labour has been entered.",
            "Plan labour for the busiest operating period and arrange backup support.")

    if water in {"None", "Low"} and "water" in cfg.get("weights", {}):
        add("Water-availability risk", "High" if water == "None" else "Medium",
            f"Water availability is set to {water}.",
            "Secure a reliable source before scaling and maintain a contingency arrangement appropriate to the activity.")
    elif irrigation in {"Rain-fed", "Limited"} and "irrigation" in cfg.get("weights", {}):
        add("Irrigation reliability risk", "Medium",
            f"Irrigation is {irrigation}.",
            "Plan crop/activity cycles around available water and arrange backup irrigation where technically feasible.")

    # Livestock / animal-specific triggers.
    if any(x in name.lower() for x in ["poultry", "dairy", "goat", "sheep"]):
        if shed in {"No", "Partial"}:
            add("Housing risk", "High" if shed == "No" else "Medium",
                f"Housing availability is {shed}.",
                "Complete suitable housing, ventilation, drainage, sanitation and protection arrangements before increasing the animal population.")
        if vet in {"No", "Limited"}:
            add("Animal-health risk", "High" if vet == "No" else "Medium",
                f"Veterinary support access is {vet}.",
                "Arrange a reliable veterinary contact, vaccination/health schedule and a rapid-response plan before stocking animals.")
        if feed in {"Poor", "Moderate"}:
            add("Feed / fodder cost risk", "High" if feed == "Poor" else "Medium",
                f"Feed/fodder availability is {feed}.",
                "Lock in more than one supplier, track feed/fodder cost per animal or bird, and maintain a short contingency stock.")

    # Poultry-specific risk logic.
    if "poultry" in name.lower():
        birds = safe_float(values.get("birds", 0))
        if birds >= 1000 and vet != "Good":
            add("Scale-related biosecurity risk", "High",
                f"The planned bird count is {int(birds):,} while veterinary support is not Good.",
                "Use a written biosecurity protocol, controlled visitor access, routine sanitation and a documented vaccination/health plan before scaling.")
        if electricity in {"No", "Limited"}:
            add("Power / heat-stress risk", "Medium",
                f"Electricity reliability is {electricity}.",
                "Plan backup power and ventilation/temperature management suitable for the production system.")

    # Dairy-specific risk logic.
    if "dairy" in name.lower():
        if equipment in {"No", "Partial"}:
            add("Milk-handling risk", "Medium",
                f"Milking/chilling equipment availability is {equipment}.",
                "Define clean milking, cooling, storage and collection arrangements to protect milk quality.")

    # Aquaculture / fish-specific triggers.
    if "fish" in name.lower() or "aquaculture" in name.lower():
        water_quality = str(values.get("water_quality", ""))
        if water_quality in {"Poor", "Unknown", ""}:
            add("Water-quality risk", "High",
                "Water quality is missing, unknown or poor.",
                "Test the water before stocking and monitor the critical water parameters required for the selected species.")
        if feed in {"Poor", "Moderate"}:
            add("Feed and growth risk", "Medium",
                f"Feed availability is {feed}.",
                "Establish a dependable feed source and monitor feed conversion, mortality and growth before expanding.")

    # Processing / services / equipment risks.
    if "processing" in cfg.get("domain", "").lower() or any(k in name.lower() for k in ["milling", "processing", "repair", "equipment rental"]):
        if electricity in {"No", "Limited"}:
            add("Operational downtime risk", "Medium",
                f"Electricity availability is {electricity}.",
                "Plan backup power or an alternative operating arrangement and schedule preventive equipment maintenance.")
        if equipment in {"No", "Partial"}:
            add("Equipment-capacity risk", "Medium",
                f"Equipment availability is {equipment}.",
                "Confirm machine capacity, service support, spare parts and maintenance costs before purchasing or scaling.")

    # Post-harvest / perishability signals.
    if transport in {"No", "Shared"} and any(x in name.lower() for x in ["vegetable", "floriculture", "flower", "nursery", "milk", "food", "mushroom"]):
        add("Post-harvest / transport risk", "Medium",
            f"Transport availability is {transport} for a time-sensitive product.",
            "Pre-arrange transport and buyer collection windows so harvested/produced stock is not held longer than necessary.")

    if storage in {"No", "Partial"} and any(x in name.lower() for x in ["grain", "spice", "oil", "processing"]):
        add("Storage risk", "Medium",
            f"Storage availability is {storage}.",
            "Define safe storage capacity and quality-control procedures before purchasing large quantities of raw material.")

    if soil_test == "No" and any(x in name.lower() for x in ["crop", "vegetable", "fruit", "spice", "floriculture"]):
        add("Soil-information risk", "Medium",
            "A soil test is not available.",
            "Obtain a soil test before making crop-specific nutrient decisions and use results to refine the plan.")

    # Time-goal mismatch: don't call it a failure; flag it as a planning risk.
    if income_time == "Within 3 months" and any(x in name.lower() for x in ["fruit", "orchard", "sericulture"]):
        add("Time-to-income mismatch", "High",
            "The target is income within 3 months for an activity that may require a longer establishment cycle.",
            "Choose a suitable short-cycle component, revise the income timeline, or begin with an additional faster-cashflow activity where appropriate.")

    # Always include baseline business-specific risks that were not triggered, with lower prominence.
    configured = cfg.get("risks", [])
    triggered_titles = {r["title"] for r in risks}
    fallback_map = {
        "Disease and mortality": ("Biological health risk", "Monitor health indicators, hygiene and preventive health procedures."),
        "Feed-cost changes": ("Input-cost risk", "Track unit feed/fodder cost and maintain alternate suppliers."),
        "Market-price changes": ("Price risk", "Compare multiple buyers and avoid relying on a single sales channel."),
        "Pest/disease pressure": ("Biological crop risk", "Use regular field scouting and preventive integrated management."),
        "Weather variability": ("Climate risk", "Use season-appropriate planning and a contingency response for extreme weather."),
        "Water-quality failure": ("Water-quality risk", "Test and monitor water quality before and during production."),
        "Perishability": ("Perishability risk", "Coordinate production timing with confirmed buyers and transport."),
        "Equipment downtime": ("Equipment downtime risk", "Use preventive maintenance and maintain access to critical spare parts."),
    }
    for base_risk in configured:
        title, mitigation = fallback_map.get(base_risk, (base_risk, "Monitor this risk regularly and define a preventive response before scaling."))
        if title not in triggered_titles and len(risks) < 8:
            risks.append({"title": title, "level": "Low", "trigger": "Business-specific baseline risk.", "mitigation": mitigation})
            triggered_titles.add(title)

    priority = {"High": 0, "Medium": 1, "Low": 2}
    risks.sort(key=lambda r: (priority.get(r["level"], 9), r["title"]))
    return risks[:8]


def render_dynamic_risk_analysis(name, risks):
    """Show three risk levels and actionable controls without repeating trigger text."""
    if not risks:
        st.info(tr_any("No risk rules were triggered for the current business profile. Continue routine monitoring before scaling."))
        return
    counts={"High":0,"Medium":0,"Low":0}
    for r in risks:
        lvl=r.get("level","Low")
        counts[lvl if lvl in counts else "Low"] += 1
    total=sum(counts.values()) or 1
    high_pct=round(counts["High"]/total*100); med_pct=round(counts["Medium"]/total*100); low_pct=100-high_pct-med_pct
    st.caption(tr_any("Risk distribution is recalculated from the selected business and the current inputs."))
    c1,c2,c3=st.columns(3)
    c1.markdown(f'<div class="gs-metric"><div class="label">High Risk</div><div class="value">🔴 {high_pct}%</div><div>{counts["High"]} item(s)</div></div>',unsafe_allow_html=True)
    c2.markdown(f'<div class="gs-metric"><div class="label">Medium Risk</div><div class="value">🟠 {med_pct}%</div><div>{counts["Medium"]} item(s)</div></div>',unsafe_allow_html=True)
    c3.markdown(f'<div class="gs-metric"><div class="label">Low Risk</div><div class="value">🟢 {low_pct}%</div><div>{counts["Low"]} item(s)</div></div>',unsafe_allow_html=True)
    grouped={"High":[],"Medium":[],"Low":[]}
    for r in risks: grouped.get(r.get("level","Low"),grouped["Low"]).append(r)
    for level,title,cls in [("High","🔴 HIGH RISK","gs-risk-high"),("Medium","🟠 MEDIUM RISK","gs-risk-medium"),("Low","🟢 LOW RISK","gs-risk-low")]:
        if not grouped[level]: continue
        st.markdown(f"#### {tr_any(title)}")
        for r in grouped[level]:
            st.markdown(f'<div class="gs-card {cls}"><b>{tr_any(r["title"])}</b><br><span class="small-note">{tr_any(r.get("mitigation","Monitor and manage this risk before scaling."))}</span></div>',unsafe_allow_html=True)

def _irrigation_score(values):
    """Transparent irrigation/water feasibility score out of 10."""
    water = str(values.get("water", "None"))
    irrigation = str(values.get("irrigation", "Rain-fed"))
    water_pts = {"None": 0, "Low": 2, "Medium": 4, "High": 5}.get(water, 2)
    irr_pts = {"Rain-fed": 2, "Limited": 2.5, "Available": 4, "Reliable": 5}.get(irrigation, 2)
    # Keep total bounded at 10 and make the result explainable.
    return round(min(10.0, water_pts + irr_pts), 1)


def _agriculture_environment_summary(location, business_name, values):
    """Return environment + irrigation analysis for the agriculture branch."""
    env_results, env_source = agriculture_environment_analysis(location, business_name, values)
    irrigation = _irrigation_score(values)
    return env_results, env_source, irrigation


def business_specific_output(name, domain_name, cfg, values, score, reasons, gaps, location):
    """Render the strategic dashboard with a compact, production-style information hierarchy."""
    schemes = related_scheme_names(name, _profile_for_business(name))
    profile = _profile_for_business(name)
    options = _option_candidates(name, domain_name, location)
    advice = BUSINESS_ADVICE.get(name, {}).get("advice", DEFAULT_ADVICE)
    steps = BUSINESS_ADVICE.get(name, {}).get("steps", DEFAULT_STEPS)

    # Financial figures are explicitly labelled estimates.
    capex = values.get("investment") or values.get("capital")
    break_even = "Not estimated"
    monthly_cost = "Not estimated"
    if profile:
        fm = business_financial_model(profile)
        plan_investment = float(capex or fm["recommended_investment"])
        proj = financial_projection(profile, plan_investment)
        be_lo, be_hi = proj["break_even"]
        if math.isfinite(be_lo) and math.isfinite(be_hi):
            break_even = f"{be_lo:.1f}–{be_hi:.1f} months"
        monthly_cost = f"₹{proj['cost'][0]:,.0f}–₹{proj['cost'][1]:,.0f}"
    capex_label = f"₹{float(capex):,.0f}" if capex else "Not provided"

    st.markdown(f"## 🔎 {tr_any(name)}")
    st.caption(f"{tr_any(domain_name)}  •  {tr_any(location)}  •  {tr_any('Rule-based feasibility assessment')}")
    st.divider()

    # Executive KPI header.
    k1,k2,k3,k4 = st.columns(4)
    with k1:
        st.markdown(f'<div class="gs-metric"><div class="label">{tr_any("CAPEX Required")}</div><div class="value">{capex_label}</div><div class="hint">{tr_any("Current input / configured estimate")}</div></div>', unsafe_allow_html=True)
    with k2:
        st.markdown(f'<div class="gs-metric"><div class="label">{tr_any("Break-Even Timeline")}</div><div class="value">{break_even}</div><div class="hint">{tr_any("Indicative model estimate")}</div></div>', unsafe_allow_html=True)
    with k3:
        st.markdown(f'<div class="gs-metric"><div class="label">{tr_any("Feasibility Score")}</div><div class="value">{score}/100</div><div class="hint">{tr_any("Adaptive score from available inputs")}</div></div>', unsafe_allow_html=True)
    with k4:
        st.markdown(f'<div class="gs-metric"><div class="label">{tr_any("Monthly Operating Cost")}</div><div class="value">{monthly_cost}</div><div class="hint">{tr_any("Indicative, scale-dependent")}</div></div>', unsafe_allow_html=True)
    st.caption(tr_any("Financial figures are planning estimates, not guarantees. Validate local supplier quotes, buyer prices and current scheme rules before committing capital."))

    tabs = st.tabs(["🌱 " + tr_any("Selection"), "🪜 " + tr_any("Execution Roadmap"), "🛒 " + tr_any("Market & Advisory"), "⚠️ " + tr_any("Risk Control"), "📊 " + tr_any("Financial Benchmarks"), "🏛️ " + tr_any("Schemes")])

    with tabs[0]:
        st.markdown("### " + tr_any("Species / Variety / Product Selection"))
        if domain_name == "Agriculture":
            matrix=[]
            for category, crop_list in options:
                for crop in crop_list:
                    profile_crop=CROP_PROFILES.get(crop,{})
                    matrix.append([
                        category, crop,
                        profile_crop.get("duration","Not available"),
                        profile_crop.get("soil","Not available"),
                        profile_crop.get("water","Not available"),
                        profile_crop.get("yield","Indicative; verify locally"),
                    ])
            if matrix:
                _md_table(["Category","Option","Cycle","Soil / space","Water","Indicative production"], matrix[:18])
                if len(matrix)>18:
                    st.caption(f"Showing 18 of {len(matrix)} location-suitable options in this dashboard. The full location mapping remains the source list.")
            else:
                st.info(tr_any("No location-suitable options are configured for this activity yet."))
            st.info(f"Location filter: {location}. The candidate list comes from the prototype's location-to-crop mapping; feasibility is then assessed from the inputs you supplied.")
        else:
            matrix=[]
            for _, opt_items in options:
                for opt in opt_items:
                    if isinstance(opt, dict):
                        matrix.append([opt.get("name","—"),opt.get("cycle","—"),opt.get("space","—"),opt.get("climate","—"),opt.get("market","—")])
                    else:
                        matrix.append([str(opt),"—","—","—","—"])
            if matrix:
                _md_table(["Specific option","Production cycle","Space requirement","Climate compatibility","Target market"], matrix)
            else:
                st.info(tr_any("No business-specific selection library is configured for this activity yet."))

    with tabs[1]:
        st.markdown("### 🪜 " + tr_any("Execution Roadmap"))
        st.caption(tr_any("Prepare → pilot → validate → scale. Each phase has a clear outcome and a go/no-go gate."))
        roadmap = [
            ("01","Foundation & Setup","READY THE BUSINESS","Weeks 1–2","Make the site, resources, budget and compliance setup ready",["Confirm land / workspace, water and access conditions.","Prepare a minimum investment plan and cash buffer.","Complete required permits, registrations, testing or local checks."],"Gate 1 · Site + resources + budget confirmed","#2E7D32","#E8F5E9"),
            ("02","Procure & Pilot","TEST BEFORE SCALE","Weeks 3–8","Run a controlled pilot using the selected option and record real costs",["Procure quality inputs / stock / equipment from traceable suppliers.","Start with a manageable pilot size and track labour, water and input use.","Record production, quality, demand and actual spending."],"Gate 2 · Pilot data meets the planned operating thresholds","#558B2F","#F1F8E9"),
            ("03","Production, Market & Scale","TURN THE PILOT INTO A BUSINESS","After pilot validation","Move into repeat production, secure buyers and scale only where unit economics work",["Lock B2B + D2C sales channels and define pricing / pack strategy.","Schedule production, grading, storage and transport.","Review monthly cash flow and expand capacity in controlled steps."],"Gate 3 · Repeat demand + workable unit economics + operational control","#1B5E20","#E8F5E9"),
        ]
        for i,(no,title,tag,duration,goal,checks,gate,color,accent) in enumerate(roadmap):
            checks_html = "".join(["<div class='gs-roadmap-check'><span>✓</span><span>" + tr_any(c) + "</span></div>" for c in checks])
            connector = "<div class='gs-roadmap-connector'></div>" if i < 2 else ""
            html = "<div class='gs-roadmap-wrap'><div class='gs-roadmap-card' style='border-left-color:"+color+";'><div class='gs-roadmap-top'><div class='gs-roadmap-number' style='background:"+accent+";color:"+color+";'>"+no+"</div><div class='gs-roadmap-heading'><div class='gs-roadmap-tag' style='color:"+color+";'>"+tr_any(tag)+"</div><div class='gs-roadmap-title'>"+tr_any(title)+"</div></div><div class='gs-roadmap-duration'>⏱ "+tr_any(duration)+"</div></div><div class='gs-roadmap-goal'><b>"+tr_any("Outcome:")+"</b> "+tr_any(goal)+".</div><div class='gs-roadmap-checks'>"+checks_html+"</div><div class='gs-roadmap-gate'>"+tr_any(gate)+"</div></div>"+connector+"</div>"
            st.markdown(html, unsafe_allow_html=True)
        st.markdown(f"<div class='gs-insight gs-roadmap-final'><div class='gs-roadmap-final-icon'>↗</div><div><b>{tr_any("Scale rule")}</b><br><span>{tr_any("Do not move straight from setup to full investment. Validate the pilot, actual operating cost and buyer response first.")}</span></div></div>", unsafe_allow_html=True)

    with tabs[2]:
        st.info(tr_any("Strategic fit: combine at least one B2B route with a direct or diversified selling channel where the business model allows it."))
        market_channels={
            "Poultry Farming":"Local retailers, restaurants, meat shops, institutions and direct households.",
            "Dairy Farming":"Milk collection centres, dairies, sweet shops, cafes, retailers and direct subscriptions.",
            "Goat Farming":"Livestock buyers, traders, butchers and direct buyers.",
            "Sheep Farming":"Livestock buyers, traders, butchers and institutional buyers where available.",
            "Fish Farming":"Fish retailers, wholesalers, restaurants, hotels and direct consumers.",
            "Vegetable Cultivation":"Retailers, restaurants, hotels, FPOs, farmers' markets and direct subscriptions.",
            "Fruit Cultivation":"Fruit retailers, wholesalers, processors, hotels and direct consumers.",
            "Mushroom Cultivation":"Restaurants, retailers, hotels and direct consumers.",
            "Plant Nursery":"Farmers, landscapers, gardeners, institutions and horticulture projects.",
        }
        _md_table(["Route","Practical use","Pricing focus"],[
            ["B2B",market_channels.get(name,"Local institutional, wholesale or business buyers."),"Compare net realized price after transport, handling and buyer deductions."],
            ["D2C", "Direct local households or end users where practical.", "Test pack size, convenience, quality and repeat-purchase potential."],
            ["Differentiation", "Quality, grading, reliability, packaging or verified production practices where relevant.", "Measure realized premium rather than assuming a premium."],
        ])
        for item in advice[:4]:
            st.markdown(f"- {tr_any(item)}")

    with tabs[3]:
        st.warning(tr_any("Biological, climatic and operational risks should be actively managed before scaling."))
        risks=dynamic_risk_analysis(name,cfg,values,score,location)
        counts={"High":0,"Medium":0,"Low":0}
        for r in risks:
            lvl=r.get("level","Low")
            counts[lvl if lvl in counts else "Low"]+=1
        total=sum(counts.values()) or 1
        high_pct=round(counts["High"]/total*100); med_pct=round(counts["Medium"]/total*100); low_pct=100-high_pct-med_pct
        a,b,c=st.columns(3)
        a.metric("🔴 " + tr_any("High Risk"),f"{high_pct}%",f"{counts['High']} {tr_any('identified')}")
        b.metric("🟠 " + tr_any("Medium Risk"),f"{med_pct}%",f"{counts['Medium']} {tr_any('identified')}")
        c.metric("🟢 " + tr_any("Low Risk"),f"{low_pct}%",f"{counts['Low']} {tr_any('identified')}")
        risk_rows=[[r.get("title","Risk"),r.get("level","Low"),r.get("impact","—"),r.get("mitigation","Monitor and manage before scaling.")] for r in risks]
        if risk_rows:
            _md_table([tr_any("Risk"),tr_any("Level"),tr_any("Impact"),tr_any("Control / mitigation")],[[tr_any(a),tr_any(b),tr_any(c),tr_any(d)] for a,b,c,d in risk_rows])
        else:
            st.info(tr_any("No configured risk items were returned for this activity."))
        if gaps:
            st.markdown("### " + tr_any("Priority gaps"))
            _md_table([tr_any("Gap"),tr_any("Action")],[[tr_any(g),tr_any("Close this gap or test a smaller pilot before scaling.")] for g in gaps[:6]])

    with tabs[4]:
        st.markdown("### " + tr_any("Financial Benchmarks"))
        if profile:
            plan_investment=float(capex or business_financial_model(profile)["recommended_investment"])
            fm=business_financial_model(profile)
            proj=financial_projection(profile,plan_investment)
            _md_table(["Benchmark","Indicative value","Interpretation"],[
                ["Minimum configured investment",f"₹{fm['minimum_investment']:,.0f}","Prototype planning range; validate supplier/asset quotes."],
                ["Planned investment",f"₹{plan_investment:,.0f}","Based on the current input or configured recommendation."],
                ["Monthly operating cost",f"₹{proj['cost'][0]:,.0f}–₹{proj['cost'][1]:,.0f}","Scale-dependent estimate."],
                ["Annual benefit",f"₹{proj['annual_benefit'][0]:,.0f}–₹{proj['annual_benefit'][1]:,.0f}","Indicative model output, not guaranteed income."],
                ["Break-even",break_even,"Depends on realized contribution margin and sales/production volume."],
                ["Feasibility indicator",f"{score}/100","Rule-based fit score from currently available inputs."],
            ])
        else:
            _md_table(["Benchmark","Value","Note"],[["CAPEX",capex_label,"Validate with quotations."],["Feasibility",f"{score}/100","Adaptive rule-based score."],["Break-even","Not estimated","Needs a configured financial model for this activity."]])
        st.info(tr_any("Success benchmark: complete a pilot with recorded unit cost, output/service volume, realized selling price, wastage/mortality where relevant, and customer acquisition cost before expanding."))

    with tabs[5]:
        st.success(tr_any("Applicable scheme information is shown for the selected business mapping. Eligibility and support depend on current official guidelines."))
        if schemes:
            scheme_rows=[]
            for scheme in schemes:
                details=SCHEME_DETAILS.get(scheme,{})
                scheme_rows.append([
                    scheme,
                    details.get("what_it_is","Check the current official scheme guidelines."),
                    details.get("benefit","Check the current official scheme guidelines."),
                    details.get("eligibility","Eligibility depends on the current official guidelines."),
                    details.get("note","Prepare documents requested by the implementing authority or lender."),
                ])
            _md_table(["Scheme","What it supports","Financial assistance","Eligibility","Key documents / conditions"],scheme_rows)
            for scheme in schemes:
                src=SCHEME_DETAILS.get(scheme,{}).get("source")
                if src: st.caption(f"{scheme}: {src}")
        else:
            st.info(tr_any("No scheme is currently mapped to this business in the prototype. Use Government Schemes for broader discovery."))

    st.divider()
    st.markdown("### ✅ " + tr_any("Practical Decision Check"))
    if score>=75:
        st.success(tr_any("Several currently entered conditions support feasibility. Validate supplier quotes, operating costs and buyer demand before scaling."))
    elif score>=55:
        st.warning(tr_any("The current assessment is mixed. Close the highest-impact gaps and test a smaller pilot before committing the full investment."))
    else:
        st.warning(tr_any("Several configured conditions are weak. Address the highest-impact gaps first and reassess before committing the full investment."))


def rank_business_recommendations(domain_name, values, location, limit=3):
    """Return a rule-based shortlist using the existing business evaluator."""
    cfg = BUSINESS_DOMAIN_CONFIG.get(domain_name, {})
    businesses = cfg.get("businesses", {})
    ranked = []
    for business_name in businesses:
        try:
            local_values = dict(values)
            local_values["location"] = location
            score, reasons, gaps = evaluate_business_config(business_name, local_values)
            ranked.append({
                "business": business_name,
                "score": max(0, min(100, round(safe_float(score)))),
                "reasons": reasons,
                "gaps": gaps,
            })
        except Exception:
            continue
    ranked.sort(key=lambda x: x["score"], reverse=True)
    return ranked[:limit]


# ============================================================
# BUSINESS RECOMMENDATION
# ============================================================

if page == "Business Recommendation":
    st.markdown(f'<div class="hero"><h1>💡 {tr_any("Business Recommendation")}</h1><p>{tr_any("Select one business activity and enter only the inputs relevant to that activity. The form adapts automatically and missing values are not treated as zero.")}</p></div>', unsafe_allow_html=True)

    domain_names = list(BUSINESS_DOMAIN_CONFIG.keys())
    top1, top2, top3 = st.columns([1.2, 1.5, 1])
    with top1:
        domain_name = st.selectbox(
            "🏷️ " + tr_any("Business Domain"),
            domain_names,
            format_func=lambda x: f"{BUSINESS_DOMAIN_CONFIG[x]['icon']} {tr_any(x)}",
            help=tr_any("Choose the broad business domain first."),
            key="br_domain",
        )
    business_names = list(BUSINESS_DOMAIN_CONFIG[domain_name].get("businesses", {}).keys())
    with top2:
        business_name = st.selectbox(
            "💼 " + tr_any("Specific Business"),
            business_names,
            format_func=tr_any,
            help=tr_any("Choose the exact activity you want to evaluate."),
            key="br_business",
        )
    with top3:
        st.markdown(
            f'<div class="gs-metric"><div class="label">{tr_any("Current Location")}</div>'
            f'<div class="value" style="font-size:1.05rem">{html.escape(str(location))}</div>'
            f'<div class="hint">{tr_any("Selected in the sidebar")}</div></div>',
            unsafe_allow_html=True,
        )

    # Clear an old result whenever the user changes the evaluated business/location.
    selection_signature = (domain_name, business_name, location)
    if st.session_state.get("br_selection_signature") != selection_signature:
        st.session_state["br_selection_signature"] = selection_signature
        st.session_state.pop("business_recommendation_result", None)
        st.session_state.pop("br_top3", None)

    cfg = BUSINESS_DOMAIN_CONFIG[domain_name]["businesses"][business_name]
    values = {}
    input_items = list(cfg.get("inputs", []))

    groups = {"location_climate": [], "soil_water": [], "capital_financial": []}
    for item in input_items:
        if len(item) < 4:
            continue
        groups.setdefault(_input_group(item[0]), []).append(item)

    if domain_name == "Agriculture":
        existing = {x[0] for x in input_items if len(x) >= 1}
        for item in AGRICULTURE_ENV_INPUTS:
            if item[0] not in existing:
                groups[_input_group(item[0])].append(item)

    st.markdown(f'<div class="gs-stepper"><span class="gs-step active">{tr_any("Step 1 • Select Business")}</span><span class="gs-step active">{tr_any("Step 2 • Enter Inputs")}</span><span class="gs-step">{tr_any("Step 3 • Strategic Output")}</span></div>', unsafe_allow_html=True)
    st.divider()

    with st.expander("📍 " + tr_any("Location & Climate Parameters"), expanded=True):
        st.markdown(f'<div class="gs-microcopy">{tr_any("Use realistic conditions for the specific site and production period. Defaults are regional planning values and should be replaced with measured/current values where available.")}</div>', unsafe_allow_html=True)
        card_cols = st.columns(3)
        for idx, item in enumerate(groups["location_climate"]):
            key, label, kind, opts = item
            with card_cols[idx % 3]:
                values[key] = render_business_input(key, label, kind, opts, widget_key=f"biz_{domain_name}_{business_name}_{key}")
        if not groups["location_climate"]:
            st.caption(tr_any("This activity does not require additional location/climate inputs beyond the selected location."))

    with st.expander("🧪 " + tr_any("Soil & Water Profile"), expanded=True):
        st.markdown(f'<div class="gs-microcopy">{tr_any("Use the latest soil/water information available. Tooltips explain what each field is used for.")}</div>', unsafe_allow_html=True)
        card_cols = st.columns(3)
        for idx, item in enumerate(groups["soil_water"]):
            key, label, kind, opts = item
            with card_cols[idx % 3]:
                values[key] = render_business_input(key, label, kind, opts, widget_key=f"biz_{domain_name}_{business_name}_{key}")
        if not groups["soil_water"]:
            st.caption(tr_any("No separate soil/water profile is required for this activity."))

    with st.expander("💰 " + tr_any("Capital & Financial Goals"), expanded=True):
        st.markdown(f'<div class="gs-microcopy">{tr_any("Enter deployable capital, operating capacity and commercial constraints. Unknown or missing fields are excluded from adaptive scoring.")}</div>', unsafe_allow_html=True)
        card_cols = st.columns(3)
        for idx, item in enumerate(groups["capital_financial"]):
            key, label, kind, opts = item
            with card_cols[idx % 3]:
                values[key] = render_business_input(key, label, kind, opts, widget_key=f"biz_{domain_name}_{business_name}_{key}")
        if not groups["capital_financial"]:
            st.caption(tr_any("No additional financial/setup inputs are required for this activity."))

    values["location"] = location
    st.divider()
    action_col1, action_col2 = st.columns([3, 1])
    with action_col1:
        st.caption(tr_any("Tip: use the latest available measurements and realistic capacity. The recommendation engine adapts to partial information."))
    with action_col2:
        generate = st.button("🔍 " + tr_any("Generate Recommendation"), type="primary", use_container_width=True, key="br_generate")
    if generate:
        st.session_state["br_top3"] = rank_business_recommendations(domain_name, values, location, limit=3)

    top3 = st.session_state.get("br_top3", [])
    if top3:
        st.markdown("### 🏆 " + tr_any("Top Suitable Business Activities"))
        st.caption(tr_any("Rule-based feasibility indicators from the currently entered inputs. This is a planning aid, not a guarantee of business success."))
        for idx, item in enumerate(top3, 1):
            c1, c2, c3 = st.columns([0.5, 2.5, 1])
            with c1:
                st.markdown(f"**#{idx}**")
            with c2:
                st.markdown(f"**{tr_any(item['business'])}**")
            with c3:
                st.metric(tr_any("Feasibility"), f"{item['score']}/100")


    if generate:
        try:
            score, reasons, gaps = evaluate_business_config(business_name, values)
            st.session_state["business_recommendation_result"] = {
                "domain": domain_name, "business": business_name, "cfg": cfg,
                "values": values, "score": score, "reasons": reasons,
                "gaps": gaps, "location": location,
            }
        except Exception as exc:
            st.error(tr_any("The recommendation could not be generated from the current inputs."))
            st.exception(exc)

    result = st.session_state.get("business_recommendation_result")
    if result and result.get("business") == business_name and result.get("domain") == domain_name and result.get("location") == location:
        st.markdown(f'<div class="gs-stepper"><span class="gs-step">{tr_any("Step 1 • Business ✓")}</span><span class="gs-step">{tr_any("Step 2 • Inputs ✓")}</span><span class="gs-step active">{tr_any("Step 3 • Strategic Output")}</span></div>', unsafe_allow_html=True)
        try:
            business_specific_output(result["business"], result["domain"], result["cfg"], result["values"], result["score"], result["reasons"], result["gaps"], result["location"])
        except Exception as exc:
            st.error(tr_any("The recommendation was calculated, but the results dashboard encountered an error."))
            st.exception(exc)

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
