import streamlit as st

# ============================================================
# PAGE 13 — PROPERTY FINANCE & EMI CALCULATOR
# FIRSTCHOICE INFRA PROPERTY HUB
# ============================================================

st.set_page_config(
    page_title="Property Finance | FirstChoice Property Hub",
    page_icon="💰",
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

/* HERO */

.hero {
    padding: 45px;
    border-radius: 32px;
    color: white;

    background:
    linear-gradient(
        135deg,
        #071952,
        #2563EB,
        #7C3AED,
        #DB2777
    );

    box-shadow:
    0 20px 65px
    rgba(37,99,235,0.25);

    margin-bottom: 30px;
}

.hero h1 {
    font-size: 44px;
    font-weight: 900;
}

.hero p {
    font-size: 18px;
}

/* SECTION */

.section {
    margin-top: 30px;
    margin-bottom: 20px;

    padding: 25px 30px;

    border-radius: 24px;

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
    0 12px 35px
    rgba(79,70,229,0.18);
}

.section h2 {
    margin: 0;
    font-size: 28px;
    font-weight: 900;
}

/* CARD */

.card {
    padding: 30px;
    border-radius: 28px;

    background: white;

    box-shadow:
    0 15px 45px
    rgba(0,0,0,0.08);

    margin-bottom: 25px;
}

/* EMI RESULT */

.result-card {
    padding: 35px;
    border-radius: 30px;

    color: white;

    background:
    linear-gradient(
        135deg,
        #047857,
        #059669,
        #10B981
    );

    box-shadow:
    0 20px 55px
    rgba(5,150,105,0.25);

    text-align: center;
}

.result-card h1 {
    font-size: 42px;
    font-weight: 900;
}

/* INFO */

.info-card {
    padding: 25px;
    border-radius: 25px;

    background:
    linear-gradient(
        135deg,
        #EFF6FF,
        #F5F3FF,
        #FDF2F8
    );

    border: 1px solid #E0E7FF;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# HERO
# ============================================================

st.markdown("""
<div class="hero">

<h1>
💰 Property Finance & EMI Planner
</h1>

<p>
Plan your property purchase with a smarter understanding
of your budget, loan requirement and estimated monthly EMI.
</p>

<p>
🏡 Property Price • 💳 Down Payment • 🏦 Loan • 📊 EMI • 📈 Interest
</p>

</div>
""", unsafe_allow_html=True)


# ============================================================
# INTRO
# ============================================================

st.markdown("""
<div class="section">

<h2>
🧮 Smart Home Loan Calculator
</h2>

<p>
Adjust the values below to estimate your monthly property loan EMI.
</p>

</div>
""", unsafe_allow_html=True)


# ============================================================
# INPUT CARD
# ============================================================

st.markdown(
    '<div class="card">',
    unsafe_allow_html=True
)


c1, c2 = st.columns(2)


with c1:

    property_price = st.number_input(
        "🏡 Property Price (₹)",
        min_value=100000,
        value=5000000,
        step=100000
    )


with c2:

    down_payment = st.number_input(
        "💰 Down Payment (₹)",
        min_value=0,
        value=1000000,
        step=100000
    )


loan_amount = max(
    property_price - down_payment,
    0
)


c3, c4 = st.columns(2)


with c3:

    interest_rate = st.number_input(
        "📈 Annual Interest Rate (%)",
        min_value=0.0,
        max_value=30.0,
        value=8.5,
        step=0.1
    )


with c4:

    loan_years = st.slider(
        "📅 Loan Tenure (Years)",
        min_value=1,
        max_value=30,
        value=20
    )


st.markdown(
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# EMI CALCULATION
# ============================================================

months = loan_years * 12

monthly_rate = (
    interest_rate / 12 / 100
)


if loan_amount <= 0:

    emi = 0

    total_payment = 0

    total_interest = 0

elif monthly_rate == 0:

    emi = loan_amount / months

    total_payment = loan_amount

    total_interest = 0

else:

    emi = (
        loan_amount
        * monthly_rate
        * (1 + monthly_rate) ** months
        /
        (
            (1 + monthly_rate) ** months
            - 1
        )
    )

    total_payment = (
        emi * months
    )

    total_interest = (
        total_payment
        - loan_amount
    )


# ============================================================
# RESULT
# ============================================================

st.markdown("""
<div class="section">

<h2>
📊 Your Estimated Loan Plan
</h2>

</div>
""", unsafe_allow_html=True)


st.markdown(
    f"""
    <div class="result-card">

    <p>
    Estimated Monthly EMI
    </p>

    <h1>
    ₹{emi:,.0f}
    </h1>

    <p>
    Estimated Loan Amount:
    <b>₹{loan_amount:,.0f}</b>
    </p>

    </div>
    """,
    unsafe_allow_html=True
)


st.write("")


r1, r2, r3 = st.columns(3)


with r1:

    st.metric(
        "🏦 Loan Amount",
        f"₹{loan_amount:,.0f}"
    )


with r2:

    st.metric(
        "💸 Total Interest",
        f"₹{total_interest:,.0f}"
    )


with r3:

    st.metric(
        "💰 Total Payment",
        f"₹{total_payment:,.0f}"
    )


# ============================================================
# LOAN SUMMARY
# ============================================================

st.markdown("""
<div class="section">

<h2>
📋 Purchase Summary
</h2>

</div>
""", unsafe_allow_html=True)


summary1, summary2 = st.columns(2)


with summary1:

    st.markdown(
        f"""
        <div class="info-card">

        <h3>
        🏡 Property Value
        </h3>

        <h2>
        ₹{property_price:,.0f}
        </h2>

        <p>
        Your selected property price.
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )


with summary2:

    st.markdown(
        f"""
        <div class="info-card">

        <h3>
        💰 Down Payment
        </h3>

        <h2>
        ₹{down_payment:,.0f}
        </h2>

        <p>
        Amount paid upfront.
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# AFFORDABILITY INDICATOR
# ============================================================

st.markdown("""
<div class="section">

<h2>
🎯 Loan Planning Insight
</h2>

</div>
""", unsafe_allow_html=True)


if property_price > 0:

    down_payment_percentage = (
        down_payment
        /
        property_price
        *
        100
    )


    if down_payment_percentage >= 30:

        st.success(
            f"🟢 Strong down payment position: "
            f"{down_payment_percentage:.1f}% of property value."
        )

    elif down_payment_percentage >= 20:

        st.info(
            f"🔵 Moderate down payment: "
            f"{down_payment_percentage:.1f}% of property value."
        )

    else:

        st.warning(
            f"🟠 Lower down payment: "
            f"{down_payment_percentage:.1f}% of property value. "
            f"Actual loan eligibility depends on lender policies."
        )


# ============================================================
# FUTURE FINANCE FEATURES
# ============================================================

st.markdown("""
<div class="section">

<h2>
🚀 Future Property Finance Tools
</h2>

<p>
FirstChoice Property Hub can expand this module into a complete
property financial planning ecosystem.
</p>

</div>
""", unsafe_allow_html=True)


f1, f2, f3 = st.columns(3)


with f1:

    st.markdown("""
    <div class="info-card">

    <h3>
    🏦 Loan Comparison
    </h3>

    <p>
    Compare home loan offers, interest rates
    and estimated EMI from multiple lenders.
    </p>

    </div>
    """, unsafe_allow_html=True)


with f2:

    st.markdown("""
    <div class="info-card">

    <h3>
    📊 Investment Calculator
    </h3>

    <p>
    Estimate rental yield, appreciation
    and long-term investment potential.
    </p>

    </div>
    """, unsafe_allow_html=True)


with f3:

    st.markdown("""
    <div class="info-card">

    <h3>
    🤖 AI Finance Assistant
    </h3>

    <p>
    Future AI tools can help users understand
    affordability and property investment scenarios.
    </p>

    </div>
    """, unsafe_allow_html=True)


# ============================================================
# DISCLAIMER
# ============================================================

st.warning(
    "⚠️ This calculator provides an estimate for planning purposes only. "
    "Actual EMI, interest rate, loan eligibility, taxes and charges "
    "depend on the lender and applicable regulations."
)
