import streamlit as st

# ============================================================
# PAGE 14 — PROPERTY INVESTMENT & ROI ANALYZER
# FIRSTCHOICE INFRA PROPERTY HUB
# ============================================================

st.set_page_config(
    page_title="Investment & ROI | FirstChoice Property Hub",
    page_icon="📈",
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

/* RESULT */

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
    font-size: 44px;
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
📈 Property Investment & ROI Analyzer
</h1>

<p>
Understand the potential financial performance of a property
before making an investment decision.
</p>

<p>
💰 Purchase • 🏠 Rental Income • 📈 Appreciation • 💸 Expenses • 📊 ROI
</p>

</div>
""", unsafe_allow_html=True)


# ============================================================
# INTRO
# ============================================================

st.markdown("""
<div class="section">

<h2>
🧮 Smart Investment Analysis
</h2>

<p>
Enter estimated property values and rental income to calculate
potential rental yield and investment returns.
</p>

</div>
""", unsafe_allow_html=True)


# ============================================================
# PROPERTY INVESTMENT INPUTS
# ============================================================

st.markdown("""
<div class="card">

<h2>
🏡 Property Investment Details
</h2>

</div>
""", unsafe_allow_html=True)


c1, c2 = st.columns(2)


with c1:

    purchase_price = st.number_input(
        "💰 Property Purchase Price (₹)",
        min_value=100000,
        value=5000000,
        step=100000
    )


with c2:

    current_value = st.number_input(
        "🏷️ Current / Expected Property Value (₹)",
        min_value=100000,
        value=6000000,
        step=100000
    )


c3, c4 = st.columns(2)


with c3:

    monthly_rent = st.number_input(
        "🏠 Expected Monthly Rent (₹)",
        min_value=0,
        value=25000,
        step=1000
    )


with c4:

    annual_expenses = st.number_input(
        "💸 Annual Property Expenses (₹)",
        min_value=0,
        value=50000,
        step=5000
    )


c5, c6 = st.columns(2)


with c5:

    holding_years = st.slider(
        "📅 Investment Holding Period (Years)",
        min_value=1,
        max_value=30,
        value=5
    )


with c6:

    future_appreciation = st.number_input(
        "📈 Expected Annual Appreciation (%)",
        min_value=0.0,
        max_value=50.0,
        value=8.0,
        step=0.5
    )


# ============================================================
# CALCULATIONS
# ============================================================

annual_rent = (
    monthly_rent * 12
)


net_annual_rental_income = max(
    annual_rent - annual_expenses,
    0
)


gross_rental_yield = (
    annual_rent
    /
    purchase_price
    *
    100
)


net_rental_yield = (
    net_annual_rental_income
    /
    purchase_price
    *
    100
)


capital_gain = max(
    current_value - purchase_price,
    0
)


capital_gain_percentage = (
    capital_gain
    /
    purchase_price
    *
    100
)


total_rental_income = (
    net_annual_rental_income
    *
    holding_years
)


total_estimated_return = (
    capital_gain
    +
    total_rental_income
)


estimated_roi = (
    total_estimated_return
    /
    purchase_price
    *
    100
)


# Future estimated value using annual appreciation

future_value = (
    purchase_price
    *
    (
        1
        +
        future_appreciation / 100
    )
    ** holding_years
)


future_capital_gain = max(
    future_value - purchase_price,
    0
)


# ============================================================
# MAIN ROI RESULT
# ============================================================

st.markdown("""
<div class="section">

<h2>
📊 Your Investment Analysis
</h2>

</div>
""", unsafe_allow_html=True)


st.markdown(
    f"""
    <div class="result-card">

    <p>
    Estimated Total ROI
    </p>

    <h1>
    {estimated_roi:.2f}%
    </h1>

    <p>
    Estimated Return Over
    <b>{holding_years} Years</b>
    </p>

    </div>
    """,
    unsafe_allow_html=True
)


st.write("")


r1, r2, r3, r4 = st.columns(4)


with r1:

    st.metric(
        "🏠 Annual Rent",
        f"₹{annual_rent:,.0f}"
    )


with r2:

    st.metric(
        "📊 Net Rental Yield",
        f"{net_rental_yield:.2f}%"
    )


with r3:

    st.metric(
        "📈 Capital Gain",
        f"₹{capital_gain:,.0f}"
    )


with r4:

    st.metric(
        "💰 Total Return",
        f"₹{total_estimated_return:,.0f}"
    )


# ============================================================
# RENTAL YIELD
# ============================================================

st.markdown("""
<div class="section">

<h2>
🏠 Rental Yield Analysis
</h2>

</div>
""", unsafe_allow_html=True)


y1, y2 = st.columns(2)


with y1:

    st.markdown(
        f"""
        <div class="info-card">

        <h3>
        💵 Gross Rental Yield
        </h3>

        <h2>
        {gross_rental_yield:.2f}%
        </h2>

        <p>
        Calculated before annual property expenses.
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )


with y2:

    st.markdown(
        f"""
        <div class="info-card">

        <h3>
        💰 Net Rental Yield
        </h3>

        <h2>
        {net_rental_yield:.2f}%
        </h2>

        <p>
        Calculated after estimated annual expenses.
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# CAPITAL APPRECIATION
# ============================================================

st.markdown("""
<div class="section">

<h2>
📈 Capital Appreciation Analysis
</h2>

</div>
""", unsafe_allow_html=True)


a1, a2, a3 = st.columns(3)


with a1:

    st.metric(
        "🏷️ Purchase Price",
        f"₹{purchase_price:,.0f}"
    )


with a2:

    st.metric(
        "📍 Current / Expected Value",
        f"₹{current_value:,.0f}"
    )


with a3:

    st.metric(
        "📈 Capital Gain",
        f"₹{capital_gain:,.0f}"
    )


st.progress(
    min(
        capital_gain_percentage / 100,
        1.0
    )
)


st.caption(
    f"Estimated capital appreciation: "
    f"{capital_gain_percentage:.2f}%"
)


# ============================================================
# FUTURE VALUE PROJECTION
# ============================================================

st.markdown("""
<div class="section">

<h2>
🔮 Future Property Value Projection
</h2>

<p>
Based on your expected annual appreciation rate.
</p>

</div>
""", unsafe_allow_html=True)


f1, f2 = st.columns(2)


with f1:

    st.markdown(
        f"""
        <div class="info-card">

        <h3>
        🏡 Estimated Future Value
        </h3>

        <h2>
        ₹{future_value:,.0f}
        </h2>

        <p>
        After {holding_years} years at
        {future_appreciation:.1f}% annual appreciation.
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )


with f2:

    st.markdown(
        f"""
        <div class="info-card">

        <h3>
        📈 Potential Capital Gain
        </h3>

        <h2>
        ₹{future_capital_gain:,.0f}
        </h2>

        <p>
        Estimated increase over original purchase price.
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# INVESTMENT SCORE
# ============================================================

if net_rental_yield >= 5:

    score = "Excellent"

    message = (
        "Strong rental income potential."
    )

elif net_rental_yield >= 3:

    score = "Good"

    message = (
        "Reasonable rental income potential."
    )

elif net_rental_yield >= 2:

    score = "Moderate"

    message = (
        "Moderate rental income potential."
    )

else:

    score = "Low"

    message = (
        "Rental yield is relatively low; "
        "capital appreciation may be the main investment driver."
    )


st.markdown("""
<div class="section">

<h2>
🎯 Investment Insight
</h2>

</div>
""", unsafe_allow_html=True)


st.success(
    f"⭐ Investment Rental Score: {score}"
)


st.info(
    message
)


# ============================================================
# FUTURE SMART FEATURES
# ============================================================

st.markdown("""
<div class="section">

<h2>
🚀 Future Investment Intelligence
</h2>

<p>
FirstChoice Property Hub can evolve this tool into a complete
real estate investment intelligence platform.
</p>

</div>
""", unsafe_allow_html=True)


i1, i2, i3 = st.columns(3)


with i1:

    st.markdown("""
    <div class="info-card">

    <h3>
    🤖 AI Investment Score
    </h3>

    <p>
    Analyse property location, price, rental yield,
    demand and appreciation potential.
    </p>

    </div>
    """, unsafe_allow_html=True)


with i2:

    st.markdown("""
    <div class="info-card">

    <h3>
    🗺️ Location Intelligence
    </h3>

    <p>
    Compare infrastructure, connectivity,
    development and future growth.
    </p>

    </div>
    """, unsafe_allow_html=True)


with i3:

    st.markdown("""
    <div class="info-card">

    <h3>
    📊 Property Investment Comparison
    </h3>

    <p>
    Compare multiple properties based on
    rental yield, ROI and expected appreciation.
    </p>

    </div>
    """, unsafe_allow_html=True)


# ============================================================
# DISCLAIMER
# ============================================================

st.warning(
    "⚠️ This tool provides estimated calculations for educational "
    "and planning purposes only. Actual property returns depend on "
    "market conditions, taxes, maintenance, vacancies, financing, "
    "transaction costs and other factors."
)
