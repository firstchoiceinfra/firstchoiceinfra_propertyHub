import streamlit as st
from datetime import datetime

# ============================================================
# PAGE 23 — PROPERTY DEAL ROOM & SMART NEGOTIATION CENTRE
# FIRSTCHOICE INFRA PROPERTY HUB
# ============================================================

st.set_page_config(
    page_title="Property Deal Room | FirstChoice Property Hub",
    page_icon="🤝",
    layout="wide"
)

# ============================================================
# PREMIUM MULTICOLOUR UI
# ============================================================

st.markdown("""
<style>

.stApp {
    background:
    linear-gradient(
        135deg,
        #F5F7FF 0%,
        #FFF7ED 35%,
        #FDF4FF 70%,
        #ECFEFF 100%
    );
}

header {
    visibility: hidden;
}

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

.hero {
    padding: 52px;
    border-radius: 36px;
    color: white;

    background:
    linear-gradient(
        135deg,
        #020617,
        #1D4ED8,
        #7C3AED,
        #DB2777
    );

    box-shadow:
    0 24px 75px
    rgba(37,99,235,0.32);

    margin-bottom: 32px;
}

.hero h1 {
    font-size: 46px;
    font-weight: 900;
}

.hero p {
    font-size: 19px;
    line-height: 1.8;
}

.section {
    margin-top: 32px;
    margin-bottom: 22px;

    padding: 30px 34px;

    border-radius: 28px;

    color: white;

    background:
    linear-gradient(
        135deg,
        #1E3A8A,
        #4F46E5,
        #9333EA,
        #EC4899
    );

    box-shadow:
    0 14px 40px
    rgba(79,70,229,0.22);
}

.section h2 {
    margin: 0;
    font-size: 30px;
    font-weight: 900;
}

.card {
    padding: 28px;
    border-radius: 26px;

    background:
    linear-gradient(
        135deg,
        #FFFFFF,
        #F5F3FF,
        #EFF6FF
    );

    border: 1px solid #E0E7FF;

    box-shadow:
    0 12px 35px
    rgba(0,0,0,0.07);

    min-height: 170px;
}

.ai-card {
    padding: 32px;
    border-radius: 30px;

    color: white;

    background:
    linear-gradient(
        135deg,
        #4C1D95,
        #7C3AED,
        #C026D3
    );

    box-shadow:
    0 18px 55px
    rgba(124,58,237,0.25);
}

.offer-card {
    padding: 35px;
    border-radius: 30px;

    color: white;
    text-align: center;

    background:
    linear-gradient(
        135deg,
        #047857,
        #059669,
        #10B981
    );

    box-shadow:
    0 20px 60px
    rgba(5,150,105,0.25);
}

.counter-card {
    padding: 30px;
    border-radius: 28px;

    color: white;

    background:
    linear-gradient(
        135deg,
        #B45309,
        #F59E0B,
        #F97316
    );

    box-shadow:
    0 18px 50px
    rgba(245,158,11,0.22);
}

.success-card {
    padding: 30px;
    border-radius: 28px;

    color: white;

    background:
    linear-gradient(
        135deg,
        #065F46,
        #059669,
        #10B981
    );
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# HERO
# ============================================================

st.markdown("""
<div class="hero">

<h1>
🤝 Property Deal Room
</h1>

<p>
A smart digital negotiation space where buyers,
sellers, builders and agents can manage property offers
and deal discussions in one place.
</p>

<p>
💰 Offer • 🔄 Counter Offer • 💬 Negotiation • 📊 Deal Tracking • 🤝 Closing
</p>

</div>
""", unsafe_allow_html=True)


# ============================================================
# AI INTRO
# ============================================================

st.markdown("""
<div class="ai-card">

<h2>
🤖 Smart Property Negotiation Centre
</h2>

<p>
Instead of handling property negotiations across multiple
calls and messages, use one structured digital Deal Room.
</p>

<p>
Track the original asking price, buyer offer, seller counter-offer,
negotiation rounds and final agreed price.
</p>

</div>
""", unsafe_allow_html=True)


# ============================================================
# DEAL PARTICIPANTS
# ============================================================

st.markdown("""
<div class="section">

<h2>
👥 Deal Participants
</h2>

</div>
""", unsafe_allow_html=True)


c1, c2 = st.columns(2)


with c1:

    buyer_name = st.text_input(
        "👤 Buyer Name"
    )


with c2:

    seller_name = st.text_input(
        "🏢 Seller / Builder Name"
    )


c3, c4 = st.columns(2)


with c3:

    agent_name = st.text_input(
        "🤝 Agent / Executive Name"
    )


with c4:

    property_name = st.text_input(
        "🏡 Property Name"
    )


# ============================================================
# PROPERTY PRICE
# ============================================================

st.markdown("""
<div class="section">

<h2>
💰 Property Deal Pricing
</h2>

</div>
""", unsafe_allow_html=True)


p1, p2 = st.columns(2)


with p1:

    asking_price = st.number_input(
        "🏷️ Seller Asking Price (₹)",
        min_value=0,
        value=5000000,
        step=100000
    )


with p2:

    buyer_offer = st.number_input(
        "💰 Buyer Initial Offer (₹)",
        min_value=0,
        value=4500000,
        step=100000
    )


# ============================================================
# OFFER DIFFERENCE
# ============================================================

price_difference = (

    asking_price
    -
    buyer_offer

)


if asking_price > 0:

    discount_percentage = (

        price_difference
        /
        asking_price
        *
        100

    )

else:

    discount_percentage = 0


st.markdown(
    f"""
    <div class="offer-card">

    <p>
    Buyer Offer
    </p>

    <h1>
    ₹{buyer_offer:,.0f}
    </h1>

    <p>
    Difference from Asking Price:
    ₹{price_difference:,.0f}
    ({discount_percentage:.2f}%)
    </p>

    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# COUNTER OFFER
# ============================================================

st.markdown("""
<div class="section">

<h2>
🔄 Seller Counter-Offer
</h2>

</div>
""", unsafe_allow_html=True)


counter_offer = st.number_input(
    "💰 Seller Counter-Offer (₹)",
    min_value=0,
    value=4800000,
    step=100000
)


counter_difference = (

    counter_offer
    -
    buyer_offer

)


st.markdown(
    f"""
    <div class="counter-card">

    <h2>
    🔄 Counter Offer: ₹{counter_offer:,.0f}
    </h2>

    <p>
    Difference from Buyer's Initial Offer:
    ₹{counter_difference:,.0f}
    </p>

    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# NEGOTIATION STATUS
# ============================================================

st.markdown("""
<div class="section">

<h2>
📊 Deal Status
</h2>

</div>
""", unsafe_allow_html=True)


deal_status = st.selectbox(
    "Select Current Deal Status",
    [
        "New Offer",
        "Under Negotiation",
        "Counter Offer Received",
        "Price Agreed",
        "Token Pending",
        "Booking Pending",
        "Deal Closed",
        "Deal Cancelled"
    ]
)


# ============================================================
# PAYMENT TERMS
# ============================================================

st.markdown("""
<div class="section">

<h2>
💳 Payment & Deal Terms
</h2>

</div>
""", unsafe_allow_html=True)


t1, t2, t3 = st.columns(3)


with t1:

    token_amount = st.number_input(
        "💵 Token / Booking Amount (₹)",
        min_value=0,
        value=100000,
        step=10000
    )


with t2:

    payment_mode = st.selectbox(
        "💳 Preferred Payment Mode",
        [
            "Bank Transfer",
            "UPI",
            "Cheque",
            "Loan",
            "Mixed Payment"
        ]
    )


with t3:

    expected_closing_days = st.number_input(
        "📅 Expected Closing Days",
        min_value=1,
        max_value=365,
        value=30
    )


# ============================================================
# NEGOTIATION NOTES
# ============================================================

st.markdown("""
<div class="section">

<h2>
💬 Negotiation Notes
</h2>

</div>
""", unsafe_allow_html=True)


negotiation_notes = st.text_area(
    "📝 Add Negotiation Notes",
    placeholder=
    "Example: Buyer requested discount due to corner location..."
)


# ============================================================
# NEGOTIATION HISTORY
# ============================================================

st.markdown("""
<div class="section">

<h2>
🕒 Negotiation History
</h2>

</div>
""", unsafe_allow_html=True)


if "deal_history" not in st.session_state:

    st.session_state.deal_history = []


h1, h2 = st.columns(2)


with h1:

    history_role = st.selectbox(
        "👤 Action By",
        [
            "Buyer",
            "Seller / Builder",
            "Agent / Executive"
        ]
    )


with h2:

    history_amount = st.number_input(
        "💰 Offer Amount (₹)",
        min_value=0,
        value=buyer_offer,
        step=100000
    )


history_message = st.text_input(
    "💬 Message / Action"
)


if st.button(
    "➕ ADD NEGOTIATION ROUND",
    use_container_width=True
):

    st.session_state.deal_history.append({

        "Time":
        datetime.now().strftime(
            "%d-%m-%Y %I:%M %p"
        ),

        "Role":
        history_role,

        "Offer":
        f"₹{history_amount:,.0f}",

        "Message":
        history_message

    })


if st.session_state.deal_history:

    st.dataframe(
        st.session_state.deal_history,
        use_container_width=True,
        hide_index=True
    )

else:

    st.info(
        "No negotiation rounds added yet."
    )


# ============================================================
# DEAL CALCULATOR
# ============================================================

st.markdown("""
<div class="section">

<h2>
🧮 Deal Financial Summary
</h2>

</div>
""", unsafe_allow_html=True)


final_price = (

    counter_offer

    if counter_offer > 0

    else buyer_offer

)


remaining_amount = (

    final_price
    -
    token_amount

)


d1, d2, d3 = st.columns(3)


with d1:

    st.markdown(
        f"""
        <div class="card">

        <h3>
        🤝 Proposed Final Price
        </h3>

        <h2>
        ₹{final_price:,.0f}
        </h2>

        </div>
        """,
        unsafe_allow_html=True
    )


with d2:

    st.markdown(
        f"""
        <div class="card">

        <h3>
        💵 Token Amount
        </h3>

        <h2>
        ₹{token_amount:,.0f}
        </h2>

        </div>
        """,
        unsafe_allow_html=True
    )


with d3:

    st.markdown(
        f"""
        <div class="card">

        <h3>
        💰 Remaining Amount
        </h3>

        <h2>
        ₹{remaining_amount:,.0f}
        </h2>

        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# SAVE DEAL
# ============================================================

if st.button(
    "💾 SAVE PROPERTY DEAL ROOM",
    use_container_width=True
):

    st.session_state.deal_saved = True

    st.success(
        "✅ Deal Room saved successfully."
    )


# ============================================================
# DEAL CLOSING
# ============================================================

if deal_status == "Deal Closed":

    st.markdown("""
    <div class="success-card">

    <h2>
    🎉 Deal Successfully Marked as Closed
    </h2>

    <p>
    The negotiation process has reached a successful conclusion.
    </p>

    </div>
    """, unsafe_allow_html=True)


# ============================================================
# FUTURE SMART NEGOTIATION AI
# ============================================================

st.markdown("""
<div class="ai-card">

<h2>
🚀 Future AI Negotiation Engine
</h2>

<p>
The future version can analyse market pricing and help
participants understand negotiation scenarios.
</p>

<p>
🤖 AI Offer Suggestions
&nbsp; • &nbsp;
📊 Market Price Comparison
&nbsp; • &nbsp;
💡 Negotiation Insights
&nbsp; • &nbsp;
🔄 Automatic Counter Offers
&nbsp; • &nbsp;
📈 Deal Probability
</p>

<p>
The system could suggest an estimated negotiation range
based on property data, market trends and comparable listings.
</p>

</div>
""", unsafe_allow_html=True)


# ============================================================
# DISCLAIMER
# ============================================================

st.markdown("""
<div class="warning-card">

<h2>
⚠️ Important Notice
</h2>

<p>
This Deal Room is a negotiation and record-management tool.
An offer or counter-offer does not automatically create a
legally binding agreement.
</p>

<p>
Final transactions should be completed through appropriate
legal agreements and verified documentation.
</p>

</div>
""", unsafe_allow_html=True)
