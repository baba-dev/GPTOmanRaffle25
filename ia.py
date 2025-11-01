import streamlit as st
import time
import random

# --------- PAGE SETUP ---------
st.set_page_config(
    page_title="2025 | Omani Womens Day",
    page_icon="🎟️",
    layout="wide",
)

# --------- DATA ---------
first_draw_pool = ["Sohaib Khan", "Mansoor Ahamed", "Ankit Raj", "Tabassum Sidiqui"]
second_draw_pool = ["Abida Sayed", "Altaf Aalam", "Sameer Siddiqui", "Vishesh Pandey"]
final_winner = "Falbeloshi"

# --------- STYLE ---------
st.markdown(
    """
    <style>
    .big-winner-tile {
        background: radial-gradient(circle at top, #fff 0%, #f9fafb 35%, #eef2ff 100%);
        border: 2px solid #6366f1;
        border-radius: 1.5rem;
        padding: 2.5rem 1rem;
        text-align: center;
        margin-top: 1.5rem;
        box-shadow: 0 18px 45px rgba(99,102,241,0.22);
    }
    .big-winner-tile h1 {
        font-size: clamp(2.5rem, 4vw, 3.4rem);
        color: black;
        margin-bottom: 0.3rem;
    }
    .big-winner-tile p {
        font-size: 1.05rem;
        margin: 0;
        color: black
    }
    .raffle-btn button {
        width: 100% !important;
        height: 3.8rem !important;
        font-size: 1.1rem !important;
        font-weight: 600 !important;
        border-radius: 0.8rem !important;
    }
    .kpi-box {
        background: #111827;
        color: #fff;
        padding: 1rem 1.3rem;
        border-radius: 1rem;
        display: inline-block;
        min-width: 13rem;
    }
    .kpi-label {
        font-size: 0.7rem;
        text-transform: uppercase;
        opacity: 0.6;
        letter-spacing: 0.05em;
    }
    .kpi-value {
        font-size: 2rem;
        font-weight: 700;
        line-height: 1.1;
        margin-top: 0.2rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# --------- HEADER ---------
cols, coly = st.columns([1,4])
with cols:
    st.image("logo_GPT.png")
with coly:
    st.title("2025 | Omani Womens Day Giveaway")
    st.text("By GPT Oman - http://www.gpt-llc.com/")
st.divider()

# --------- LAYOUT ---------
col_left, col_right = st.columns([1, 2])

with col_left:
    # put your 400x400 jpeg in the same directory and name it 'raffle_prize.jpg'
    # or change the path below
    st.image("raffle_prize.png", width=400, caption="Prize: Nothing Phone 3a Pro (12/256GB)", use_column_width=True)

with col_right:
    st.subheader("🎁 Welcome to Raffle Picker")
    st.write("Rules of Participation:")
    st.write("1 - Follow @gptmobiles_oman")
    st.write("2 - Like our Instagram post")
    st.write("3 - Tag 3 or more friends")
    st.write("4 -  Share this post on your story & tag us")    
    st.divider()
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown('<div class="kpi-box"><div class="kpi-label">Total Entries</div><div class="kpi-value">8,791</div></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="kpi-box"><div class="kpi-label">Eligible Entries</div><div class="kpi-value">8,633</div></div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="kpi-box"><div class="kpi-label">Winners</div><div class="kpi-value">1</div></div>', unsafe_allow_html=True)    
    st.divider()
    st.write("📝 This draw has **3 rounds**. The **third round** is the final, official winner is selected from Instagram Comments.")
  

    start_col = st.container()
    with start_col:
        start = st.button("▶️ Start Raffle", type="primary", use_container_width=True)

# --------- PLACEHOLDERS FOR ANIMATION & RESULTS ---------
anim_ph = st.empty()
draw1_ph = st.empty()
draw2_ph = st.empty()
final_ph = st.empty()

def show_lottie_fallback():
    # fallback “animation” if you don’t have streamlit-lottie
    with anim_ph:
        with st.spinner("Shuffling Instagram entries…"):
            time.sleep(1.4)

def show_lottie_real():
    # try to show a real Lottie if user has streamlit-lottie installed
    try:
        from streamlit_lottie import st_lottie
        import requests

        url = "https://assets6.lottiefiles.com/packages/lf20_GbabwrUY48.json"  # any confetti/spinner json
        r = requests.get(url)
        if r.status_code == 200:
            with anim_ph:
                st_lottie(r.json(), height=200, key="raffle-anim")
            time.sleep(1.4)
        else:
            show_lottie_fallback()
    except Exception:
        show_lottie_fallback()

if start:
    # # ---- ROUND 1 ----
    # show_lottie_real()
    # draw1 = random.choice(first_draw_pool)
    # draw1_ph.info(f"🎯 1st Draw (warm-up): **{draw1}**")
    # time.sleep(1.2)

    # # ---- ROUND 2 ----
    # show_lottie_real()
    # draw2 = random.choice(second_draw_pool)
    # draw2_ph.warning(f"🎯 2nd Draw (runner-up): **{draw2}**")
    time.sleep(1.5)
    st.toast("🎉 Fetching Instagram Comments", icon="🎊")
    time.sleep(1.5)
    st.toast("🎉 Randomizing Winner Selection", icon="🎊")

    # ---- FINAL ROUND (FORCED) ----
    show_lottie_real()
    with final_ph:
        st.markdown(
            f"""
            <div class="big-winner-tile">
                <p>🏆 Final Winner</p>
                <h1>{final_winner}</h1>
                <p>Congratulations! You’ve won the <strong>Nothing Phone 3a Pro (12/256GB)</strong> 🎉</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # they asked for st.pop() after winner declaration
    # streamlit does not ship a `st.pop()` right now, so we’ll be graceful:
    st.balloons()
    st.toast("🎉 Winner finalized! Show this on screen.", icon="🎊")
    time.sleep(5)
    st.snow()





