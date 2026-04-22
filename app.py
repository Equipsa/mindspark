import streamlit as st
import random
from datetime import datetime

# ============================================================
# MindSpark — Collection de citations inspirantes
# ============================================================

st.set_page_config(
    page_title="MindSpark",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ============================================================
# STYLE CSS PERSONNALISÉ
# ============================================================
st.markdown("""
<style>
    /* Fond principal */
    .stApp {
        background: linear-gradient(135deg, #0F172A 0%, #1E293B 100%);
    }

    /* Titre principal */
    .main-title {
        font-size: 3.5rem;
        font-weight: 800;
        background: linear-gradient(90deg, #F59E0B 0%, #EF4444 50%, #8B5CF6 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        text-align: center;
        margin-bottom: 0.2rem;
        letter-spacing: -1px;
    }

    .subtitle {
        text-align: center;
        color: #94A3B8;
        font-size: 1.1rem;
        margin-bottom: 2rem;
        font-style: italic;
    }

    /* Cartes citations */
    .quote-card {
        background: rgba(30, 41, 59, 0.6);
        backdrop-filter: blur(10px);
        border-left: 4px solid #F59E0B;
        padding: 1.5rem 1.8rem;
        margin: 0.8rem 0;
        border-radius: 12px;
        transition: all 0.3s ease;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
    }

    .quote-card:hover {
        transform: translateX(4px);
        border-left-color: #EF4444;
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.5);
    }

    .quote-text {
        color: #F1F5F9;
        font-size: 1.15rem;
        line-height: 1.6;
        font-weight: 400;
    }

    .quote-number {
        color: #F59E0B;
        font-weight: 700;
        font-size: 1rem;
        margin-right: 0.5rem;
    }

    /* Featured quote */
    .featured-quote {
        background: linear-gradient(135deg, rgba(245, 158, 11, 0.15), rgba(139, 92, 246, 0.15));
        border: 2px solid rgba(245, 158, 11, 0.4);
        padding: 2.5rem;
        border-radius: 16px;
        text-align: center;
        margin: 1.5rem 0;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.4);
    }

    .featured-quote-text {
        color: #FEF3C7;
        font-size: 1.6rem;
        font-style: italic;
        font-weight: 500;
        line-height: 1.5;
    }

    .featured-label {
        color: #F59E0B;
        font-size: 0.85rem;
        font-weight: 700;
        letter-spacing: 3px;
        margin-bottom: 1rem;
    }

    /* Sections */
    .section-title {
        color: #F1F5F9;
        font-size: 1.4rem;
        font-weight: 700;
        margin: 1.5rem 0 1rem 0;
        padding-bottom: 0.5rem;
        border-bottom: 2px solid rgba(245, 158, 11, 0.3);
    }

    /* Stats */
    .stat-card {
        background: rgba(30, 41, 59, 0.5);
        padding: 1.2rem;
        border-radius: 10px;
        text-align: center;
        border: 1px solid rgba(148, 163, 184, 0.2);
    }

    .stat-number {
        font-size: 2rem;
        font-weight: 800;
        color: #F59E0B;
    }

    .stat-label {
        color: #94A3B8;
        font-size: 0.85rem;
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    /* Inputs */
    .stTextInput > div > div > input {
        background-color: rgba(30, 41, 59, 0.8);
        color: #F1F5F9;
        border: 1px solid rgba(148, 163, 184, 0.3);
        border-radius: 8px;
        padding: 0.6rem 1rem;
    }

    .stTextInput > div > div > input:focus {
        border-color: #F59E0B;
        box-shadow: 0 0 0 2px rgba(245, 158, 11, 0.2);
    }

    /* Buttons */
    .stButton > button {
        background: linear-gradient(135deg, #F59E0B, #EF4444);
        color: white;
        border: none;
        padding: 0.6rem 1.5rem;
        border-radius: 8px;
        font-weight: 600;
        transition: all 0.2s;
    }

    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 15px rgba(245, 158, 11, 0.4);
    }

    /* Empty state */
    .empty-state {
        text-align: center;
        padding: 3rem 1rem;
        color: #94A3B8;
    }

    /* Footer */
    .footer {
        text-align: center;
        color: #64748B;
        font-size: 0.85rem;
        margin-top: 3rem;
        padding-top: 1.5rem;
        border-top: 1px solid rgba(148, 163, 184, 0.1);
    }

    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)


# ============================================================
# DONNÉES INITIALES
# ============================================================
DEFAULT_QUOTES = [
    "Le succès appartient à ceux qui persévèrent malgré les obstacles.",
    "Chaque jour est une nouvelle chance de devenir meilleur.",
    "Ne jamais abandonner, même quand le chemin semble difficile.",
    "La discipline est le pont entre les objectifs et les accomplissements.",
    "Le plus grand risque est de ne prendre aucun risque.",
    "Le succès n'est pas la clé du bonheur. Le bonheur est la clé du succès.",
    "Votre avenir est créé par ce que vous faites aujourd'hui, pas demain.",
]


# ============================================================
# ÉTAT DE SESSION
# ============================================================
if "quotes" not in st.session_state:
    st.session_state.quotes = DEFAULT_QUOTES.copy()

if "featured" not in st.session_state:
    st.session_state.featured = random.choice(DEFAULT_QUOTES)


# ============================================================
# FONCTIONS
# ============================================================
def get_random_quote():
    if st.session_state.quotes:
        return random.choice(st.session_state.quotes)
    return "Ajoutez votre première citation pour commencer."


# ============================================================
# HEADER
# ============================================================
st.markdown('<h1 class="main-title">✨ MindSpark</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Votre collection personnelle de citations inspirantes</p>', unsafe_allow_html=True)


# ============================================================
# CITATION À L'HONNEUR
# ============================================================
st.markdown(f"""
<div class="featured-quote">
    <div class="featured-label">✦ CITATION À L'HONNEUR ✦</div>
    <div class="featured-quote-text">« {st.session_state.featured} »</div>
</div>
""", unsafe_allow_html=True)

col_refresh1, col_refresh2, col_refresh3 = st.columns([1, 1, 1])
with col_refresh2:
    if st.button("🎲  Nouvelle citation à l'honneur", use_container_width=True):
        st.session_state.featured = get_random_quote()
        st.rerun()


# ============================================================
# STATISTIQUES
# ============================================================
st.markdown('<div class="section-title">📊 Aperçu</div>', unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)
with c1:
    st.markdown(f"""
    <div class="stat-card">
        <div class="stat-number">{len(st.session_state.quotes)}</div>
        <div class="stat-label">Citations</div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    avg_length = sum(len(q) for q in st.session_state.quotes) // max(len(st.session_state.quotes), 1)
    st.markdown(f"""
    <div class="stat-card">
        <div class="stat-number">{avg_length}</div>
        <div class="stat-label">Car. en moyenne</div>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown(f"""
    <div class="stat-card">
        <div class="stat-number">{datetime.now().strftime("%H:%M")}</div>
        <div class="stat-label">Heure actuelle</div>
    </div>
    """, unsafe_allow_html=True)


# ============================================================
# AJOUTER UNE CITATION
# ============================================================
st.markdown('<div class="section-title">➕ Ajouter une citation</div>', unsafe_allow_html=True)

col_add1, col_add2 = st.columns([4, 1])
with col_add1:
    new_quote = st.text_input(
        "Nouvelle citation",
        placeholder="Écrivez une citation qui vous inspire...",
        label_visibility="collapsed",
    )
with col_add2:
    add_clicked = st.button("Ajouter", use_container_width=True)

if add_clicked:
    if new_quote.strip():
        st.session_state.quotes.append(new_quote.strip())
        st.success("✓ Citation ajoutée à votre collection !")
        st.rerun()
    else:
        st.warning("Veuillez écrire une citation avant d'ajouter.")


# ============================================================
# RECHERCHE
# ============================================================
st.markdown('<div class="section-title">🔍 Explorer votre collection</div>', unsafe_allow_html=True)

search = st.text_input(
    "Rechercher",
    placeholder="Rechercher par mot-clé...",
    label_visibility="collapsed",
)

filtered_quotes = [
    q for q in st.session_state.quotes
    if search.lower() in q.lower()
]


# ============================================================
# LISTE DES CITATIONS
# ============================================================
if filtered_quotes:
    for i, quote in enumerate(filtered_quotes, start=1):
        col_q, col_del = st.columns([10, 1])
        with col_q:
            st.markdown(f"""
            <div class="quote-card">
                <span class="quote-number">#{i:02d}</span>
                <span class="quote-text">{quote}</span>
            </div>
            """, unsafe_allow_html=True)
        with col_del:
            st.write("")
            if st.button("🗑️", key=f"delete_{i}_{quote[:20]}", help="Supprimer cette citation"):
                st.session_state.quotes.remove(quote)
                if quote == st.session_state.featured and st.session_state.quotes:
                    st.session_state.featured = random.choice(st.session_state.quotes)
                st.rerun()
else:
    if search:
        st.markdown("""
        <div class="empty-state">
            <div style="font-size: 3rem; margin-bottom: 0.5rem;">🔎</div>
            <div>Aucune citation ne correspond à votre recherche.</div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class="empty-state">
            <div style="font-size: 3rem; margin-bottom: 0.5rem;">📭</div>
            <div>Votre collection est vide. Ajoutez votre première citation !</div>
        </div>
        """, unsafe_allow_html=True)


# ============================================================
# ACTIONS GLOBALES
# ============================================================
st.markdown('<div class="section-title">⚙️ Actions</div>', unsafe_allow_html=True)

col_act1, col_act2, col_act3 = st.columns(3)
with col_act1:
    if st.button("🔄 Réinitialiser la collection", use_container_width=True):
        st.session_state.quotes = DEFAULT_QUOTES.copy()
        st.session_state.featured = random.choice(DEFAULT_QUOTES)
        st.success("Collection réinitialisée.")
        st.rerun()

with col_act2:
    if st.button("🎯 Citation aléatoire", use_container_width=True):
        st.info(f"💡 « {get_random_quote()} »")

with col_act3:
    if st.button("🗑️ Tout supprimer", use_container_width=True):
        st.session_state.quotes = []
        st.warning("Collection vidée.")
        st.rerun()


# ============================================================
# FOOTER
# ============================================================
st.markdown("""
<div class="footer">
    <strong>MindSpark</strong> — Votre étincelle d'inspiration quotidienne ✨
</div>
""", unsafe_allow_html=True)
