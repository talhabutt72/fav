import streamlit as st
import random
import datetime
import pytz

# --- 1. CONFIGURATION ---
YOUR_NAME = "Talha Butt"
HER_NAME = "Rofiqah"
# The secret names she loves
FAV_NICKNAMES = ["guggu", "sayang"] 

# --- 2. PAGE SETUP ---
st.set_page_config(page_title=f"Eid Mubarak, {HER_NAME}!", page_icon="🌙", layout="centered")

# --- 3. THE FIXED CSS ---
st.markdown(f"""
    <style>
    .stApp {{
        background-color: #FFF5F7 !important;
    }}
    
    h1, h2, h3, p, span, label, .stMarkdown, .stSelectSlider p {{
        color: #4A0E0E !important;
        text-align: center !important;
    }}

    div[data-baseweb="slider"] {{
        background-color: #FFD1DC;
        border-radius: 10px;
        padding: 10px;
    }}

    .stButton>button {{
        width: 100%;
        border-radius: 25px;
        border: 2px solid #D33682;
        background-color: #D33682;
        color: white !important;
        font-weight: bold;
    }}
    
    .stButton>button:hover {{
        background-color: #A62A66;
        border: 2px solid #A62A66;
    }}

    .stImage {{
        display: flex;
        justify-content: center;
    }}

    .footer {{
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #FFF5F7;
        text-align: center;
        color: #4A0E0E;
        padding: 10px;
        font-size: 14px;
        border-top: 1px solid #FFD1DC;
    }}
    .recipe-box {{
        background-color: white;
        padding: 20px;
        border-radius: 15px;
        border: 2px dashed #D33682;
        text-align: left !important;
        color: #4A0E0E;
    }}
    </style>
    """, unsafe_allow_html=True)

# --- 4. THE AUTHENTICATION GATE ---
if 'authenticated' not in st.session_state:
    st.session_state['authenticated'] = False

if not st.session_state['authenticated']:
    st.markdown("<h1 style='margin-top: 50px;'>🔒 A Secret for You</h1>", unsafe_allow_html=True)
    st.markdown("<p>To enter, please tell me...</p>", unsafe_allow_html=True)
    
    nickname_input = st.text_input("What is that favorite name I love to call you?", type="default")
    
    if st.button("Unlock my Heart"):
        # BUG FIX: Check if input matches any name in the list
        if nickname_input.strip().lower() in FAV_NICKNAMES:
            st.session_state['authenticated'] = True
            st.rerun()
        else:
            st.error("That's not it! Try the name I always use when I'm being extra sweet.")
    st.stop()

# --- 5. THE MAIN CONTENT ---
st.balloons()
st.markdown(f"<h1>🌙 Eid Mubarak, {HER_NAME}!</h1>", unsafe_allow_html=True)
st.markdown("<p style='font-size: 22px; font-style: italic;'>Distance is just a test of how far love can travel.</p>", unsafe_allow_html=True)

st.divider()
st.markdown("### 🎁 Pick Your Eid Gift")
gift_col1, gift_col2, gift_col3 = st.columns(3)

with gift_col1:
    if st.button("A Virtual Rose 🌹"):
        st.success("Sent with all my love!")
with gift_col2:
    if st.button("A Digital Hug 🤗"):
        st.info("Can you feel it? I'm holding you tight.")
with gift_col3:
    if st.button("A Sweet Kiss 💋"):
        st.warning("Muah! Save this one for later.")

# --- SECTION: THE HEARTFELT LETTER ---
st.divider()
st.markdown("### 💌 To My Love,")
st.write("""
    I'm almost 23 years old, never got excited or happy on any eid... but this eid is really special for me. You make this special. You don't know how much I love you, maybe even I don't know.
    My feelings regarding you are pure, genuine. I'm feeling blessed to have you. In every prayer, I ask Allah to write you into my fate.
    You every time make me feel proud about having you, you are amazing.. even if you don't know it. 
    I remember how you take care of me like I'm your husbii, which hits me even harder. The way you treat me—I love that. When I'm getting angry or not feeling right, the way you handle me and my emotions is really amazing.
    I never imagine anyone else in my wife's place. You are perfect for me, the way you are.. I love that.
    I love you sooo much muchh❤️❤️. I don't remember all my favorite things, but I know which food you like, which flower...
""")

# --- NEW SECTION: THE CONNECTION STATUS ---
st.divider()
st.markdown("### 📡 Connection Status")
col_link1, col_link2, col_link3 = st.columns([2, 1, 2])

with col_link1:
    st.write("📍 **Sheikhupura**")
    st.caption("Waiting for you...")

with col_link2:
    st.markdown("<h2 style='text-align: center;'>✈️</h2>", unsafe_allow_html=True)

with col_link3:
    st.write(f"📍 **{HER_NAME}'s City (Tawau)**")
    st.caption("My favorite place.")

st.write("Current Love Signal Strength:")
st.progress(100)
st.success("✅ Signal Perfect. Heartbeat Synchronized.")

# --- SECTION: REASONS WHY RANDOMIZER ---
st.divider()
st.markdown("### ✨ A Little Reminder...")
reasons = [
    "I love the way you treat me.",
    "I love how you always know exactly what to say to make me smile.",
    "I love our late-night chats that never seem long enough.",
    "I love your kindness and the way you care about me.",
    "I love how you make me feel like I can achieve anything.",
    "I love the future we are building together, step by step."
]

if st.button("Click for a reason I love you"):
    st.snow()
    random_reason = random.choice(reasons)
    st.success(f"**{random_reason}**")

st.divider()
my_tz = pytz.timezone("Asia/Karachi")
# Rofiqah is 3 hours ahead of Pakistan (Asia/Singapore or Asia/Kuala_Lumpur)
her_tz = pytz.timezone("Asia/Singapore") 

# 2. Get the current time for those specific zones
my_time = datetime.datetime.now(my_tz)
her_time = datetime.datetime.now(her_tz)

col_time1, col_time2 = st.columns(2)

with col_time1:
    st.markdown("**My Time (PKT)**")
    # Using my_time instead of datetime.now()
    st.subheader(my_time.strftime("%I:%M %p"))
    st.caption("Thinking of you...")

with col_time2:
    st.markdown(f"**{HER_NAME}'s Time**")
    # Using her_time instead of datetime.now()
    st.subheader(her_time.strftime("%I:%M %p"))
    st.caption("My favorite person's world.")

# --- NEW SECTION: THE FINAL SURPRISE ---
st.divider()
if st.button("Open Your Eid Gift"):
    st.balloons()
    st.snow()
    st.markdown(f"""
    <div style="background-color: white; padding: 30px; border-radius: 10px; border: 3px solid #D33682;">
        <h2 style="color: #D33682;">You are my home.</h2>
        <p style="color: #4A0E0E; font-size: 18px;">
            I love you sooo much, you are my comfort zone. I am working every day 
            to make our 'Future Goal' a reality. <br><br>
            <b>Eid Mubarak, {HER_NAME}!</b>
        </p>
    </div>
    """, unsafe_allow_html=True)

with st.expander("✨ My Fav sweet dish."):
    st.markdown("""
    <div class="recipe-box">
    <h3 style='text-align: left !important; color: #D33682;'>🍚 Traditional Chawal ki Kheer</h3>
    <p>This is my favorite because it reminds me of home... and you.</p>
    <strong>Ingredients:</strong>
    <ul>
        <li>1 Liter Full-Cream Milk</li>
        <li>1/4 cup Basmati Rice (soaked and crushed)</li>
        <li>1/2 cup Sugar</li>
        <li>4-5 Green Cardamoms</li>
        <li>Chopped Almonds & Pistachios</li>
    </ul>
    <strong>How to make it:</strong><br>
    1. Boil milk with cardamoms.<br>
    2. Add crushed rice and slow-cook.<br>
    3. Stir until thickened and creamy.<br>
    4. Add sugar and nuts.<br><br>
    <em>Serve it chilled, just like I wish I could serve it to you tomorrow.</em>
    </div>
    """, unsafe_allow_html=True)

# --- SECTION: THE JOURNEY & FUTURE GOAL ---
st.divider()
st.markdown("### ⏳ Our Journey & Beyond")

journey_val = st.select_slider(
    'Slide through our story:',
    options=['The Start', 'The Missed Call','Much More','Today', 'Our Future Goal'])

if journey_val == 'The Start':
    st.markdown("#### 📍 The Beginning")
    st.write("Where it all started. 11/13/2025 (Best day of my life).")
elif journey_val == 'The Missed Call':
    st.markdown("#### 📞 The Missed Call")
    st.write("Just mistake, but it hit me hard dono why (12/1/2026 3:51 PM).")
elif journey_val == 'Much More':
    st.markdown("#### ❤️ There are much more memories")
elif journey_val == 'Today':
    st.markdown("#### 🌙 Eid 2026")
    st.write("Our 1st Eid.")
elif journey_val == 'Our Future Goal':
    st.markdown("#### 🏠 The Dream We're Building")
    st.write("When we build our own home, our family, together!")

# BUG FIX: Moved image out of the 'if' block so it shows correctly
try:
    st.image('future_goal.jpg', caption="Our 'Why'", use_container_width=True)
    st.markdown("<p style='font-style: italic;'>'This is my future plan regarding you.'</p>", unsafe_allow_html=True)
except FileNotFoundError:
    st.error("🖼️ Image Not Found: Please upload 'future_goal.jpg' to the folder.")

# --- FOOTER ---
st.markdown(f"<div class='footer'>Made with ❤️ by {YOUR_NAME} | Eid 2026</div>", unsafe_allow_html=True)
