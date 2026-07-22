import streamlit as st

# ============================================================
# FIRSTCHOICE INFRA PROPERTY HUB
# PAGE 15 - PROPERTY INVESTMENT INTELLIGENCE
# ============================================================

st.set_page_config(
    page_title="Investment Analysis | FirstChoice Property Hub",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============================================================
# PREMIUM MULTINATIONAL UI
# ============================================================

st.markdown("""
<style>

.stApp {
    background:
    linear-gradient(
        135deg,
        #F7F9FF 0%,
        #FFF7F3 35%,
        #F7F1FF 70%,
        #EFFCFF 100%
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

/* BRAND */

.brand {

    background:
    linear-gradient(
        135deg,
        #071952,
        #2563EB,
        #7C3AED,
        #EC4899
    );

    padding: 22px 32px;

    border-radius: 24px;

    color: white;

    box-shadow:
    0 18px 50px
    rgba(37,99,235,0.22);
}

.brand-title {

    font-size: 28px;

    font-weight: 900;

    letter-spacing: 2px;
}

.brand-subtitle {

    font-size: 11px;

    letter-spacing: 4px;

    color: #FDE68A;
}

/* HERO */

.hero {

    margin-top: 28px;

    padding: 50px;

    border-radius: 32px;

    color: white;

    background:
    linear-gradient(
        135deg,
        #071952,
        #2563EB,
        #7C3AED,
        #EC4899
    );

    box-shadow:
    0 25px 70px
    rgba(37,99,235,0.25);
}

.hero-title {

    font-size: 42px;

    font-weight: 900;
}

.hero-subtitle {

    font-size: 16px;

    color:
    rgba(255,255,255,0.88);
}

/* SECTION */

.section-header {

    margin-top: 35px;

    margin-bottom: 22px;

    padding: 22px 30px;

    border-radius: 22px;

    background:
    linear-gradient(
        135deg,
        #071952,
        #2563EB,
        #7C3AED,
        #EC4899
    );

    color: white;

    box-shadow:
    0 12px 35px
    rgba(37,99,235,0.18);
}

.section-title {

    font-size: 27px;

    font-weight: 900;
}

.section-subtitle {

    font-size: 13px;

    color:
    rgba(255,255,255,0.82);
}

/* SCORE */

.score-card {

    padding: 40px;

    border-radius: 32px;

    color: white;

    text-align: center;

    background:
    linear-gradient(
        135deg,
        #071952,
        #4C1D95,
        #7C3AED,
        #EC4899
    );

    box-shadow:
    0 22px 60px
    rgba(124,58,237,0.25);
}

.score-number {

    font-size: 72px;

    font-weight: 900;
}

/* RESULT */

.result-card {

    padding: 30px;

    border-radius: 28px;

    background: white;

    box-shadow:
    0 15px 40px
    rgba(0,0,0,0.07);
}

/* AI */

.ai-card {

    padding: 38px;

    border-radius: 30px;

    color: white;

    background:
    linear-gradient(
        135deg,
        #071952,
        #4C1D95,
        #7C3AED,
        #EC4899
    );

    box-shadow:
    0 22px 60px
    rgba(124,58,237,0.25);
}

/* FOOTER */

.footer {

    margin-top: 60px;

    padding: 45px;

    border-radius: 28px;

    color: white;

    text-align: center;

    background:
    linear-gradient(
        135deg,
        #071952,
        #1E1B4B
    );
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# BRAND
# ============================================================

st.markdown("""
<div class="brand">

<div class="brand-title">
🏠 FIRSTCHOICE INFRA
</div>

<div class="brand-subtitle">
PROPERTY HUB • INVESTMENT INTELLIGENCE
</div>

</div>
""", unsafe_allow_html=True)


# ============================================================
# HERO
# ============================================================

st.markdown("""
<div class="hero">

<div class="hero-title">
📈 Property Investment Intelligence
</div>

<div class="hero-subtitle">
Understand the financial potential of a property before
making an important real estate decision.
</div>

</div>
""", unsafe_allow_html=True)


# ============================================================
# DISCLAIMER
# ============================================================

st.warning(
    "⚠️ Investment scores and projections shown on this demo page are estimates for decision support only. They are not financial advice or guaranteed returns."
)


# ============================================================
# PROPERTY INPUT
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
🏠 Property Investment Details
</div>

<div class="section-subtitle">
Enter property information to generate an estimated analysis.
</div>

</div>
""", unsafe_allow_html=True)


p1, p2, p3 = st.columns(3)


with p1:

    property_price = st.number_input(
        "Property Price (₹)",
        min_value=100000,
        value=5000000,
        step=100000
    )


with p2:

    property_area = st.number_input(
        "Property Area (Sq.Ft)",
        min_value=100,
        value=1000,
        step=50
    )


with p3:

    expected_rent = st.number_input(
        "Expected Monthly Rent (₹)",
        min_value=0,
        value=20000,
        step=1000
    )


# ============================================================
# LOCATION FACTORS
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
📍 Location Intelligence
</div>

<div class="section-subtitle">
Rate the factors that can influence long-term property demand.
</div>

</div>
""", unsafe_allow_html=True)


l1, l2, l3 = st.columns(3)


with l1:

    connectivity = st.slider(
        "🚇 Connectivity Score",
        1,
        10,
        7
    )


with l2:

    infrastructure = st.slider(
        "🏗️ Infrastructure Growth",
        1,
        10,
        7
    )


with l3:

    demand = st.slider(
        "📈 Local Demand",
        1,
        10,
        7
    )


l4, l5, l6 = st.columns(3)


with l4:

    education = st.slider(
        "🎓 Education & Schools",
        1,
        10,
        7
    )


with l5:

    healthcare = st.slider(
        "🏥 Healthcare Access",
        1,
        10,
        7
    )


with l6:

    employment = st.slider(
        "💼 Employment Opportunities",
        1,
        10,
        7
    )


# ============================================================
# LOAN DETAILS
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
🏦 Home Loan & EMI Analysis
</div>

<div class="section-subtitle">
Estimate your monthly loan obligation.
</div>

</div>
""", unsafe_allow_html=True)


loan1, loan2, loan3 = st.columns(3)


with loan1:

    down_payment = st.number_input(
        "Down Payment (₹)",
        min_value=0,
        value=1000000,
        step=100000
    )


with loan2:

    interest_rate = st.number_input(
        "Annual Interest Rate (%)",
        min_value=0.0,
        value=8.5,
        step=0.1
    )


with loan3:

    loan_years = st.number_input(
        "Loan Tenure (Years)",
        min_value=1,
        max_value=40,
        value=20
    )


# ============================================================
# EMI CALCULATION
# ============================================================

loan_amount = max(
    property_price - down_payment,
    0
)

monthly_rate = (
    interest_rate / 100
) / 12

total_months = (
    loan_years * 12
)


if loan_amount > 0 and monthly_rate > 0:

    emi = (

        loan_amount
        * monthly_rate
        * (1 + monthly_rate) ** total_months

    ) / (

        (1 + monthly_rate) ** total_months
        - 1

    )

else:

    emi = 0


# ============================================================
# RENTAL YIELD
# ============================================================

annual_rent = (
    expected_rent * 12
)

rental_yield = (

    annual_rent
    / property_price
) * 100


# ============================================================
# PRICE PER SQFT
# ============================================================

price_per_sqft = (

    property_price
    / property_area

)


# ============================================================
# CASH FLOW
# ============================================================

monthly_cash_flow = (

    expected_rent
    - emi

)


# ============================================================
# LOCATION SCORE
# ============================================================

location_score = (

    connectivity
    + infrastructure
    + demand
    + education
    + healthcare
    + employment

) / 6


# ============================================================
# INVESTMENT SCORE
# ============================================================

rental_score = min(
    rental_yield * 10,
    100
)

investment_score = (

    location_score * 7
    + rental_score * 3

) / 10


investment_score = round(
    investment_score
)


# ============================================================
# MAIN RESULTS
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
🎯 Your Investment Snapshot
</div>

<div class="section-subtitle">
Estimated financial indicators based on your inputs.
</div>

</div>
""", unsafe_allow_html=True)


r1, r2, r3, r4 = st.columns(4)


with r1:

    st.metric(

        "💰 Property Price",

        f"₹{property_price:,.0f}"

    )


with r2:

    st.metric(

        "🏦 Estimated EMI",

        f"₹{emi:,.0f}"

    )


with r3:

    st.metric(

        "🏠 Rental Yield",

        f"{rental_yield:.2f}%"

    )


with r4:

    st.metric(

        "📐 Price / Sq.Ft",

        f"₹{price_per_sqft:,.0f}"

    )


# ============================================================
# INVESTMENT SCORE
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
🏆 FirstChoice Investment Score
</div>

<div class="section-subtitle">
An estimated score based on rental potential and selected location factors.
</div>

</div>
""", unsafe_allow_html=True)


score_col1, score_col2 = st.columns(2)


with score_col1:

    st.markdown(
        f"""
        <div class="score-card">

        <div>
        YOUR ESTIMATED SCORE
        </div>

        <div class="score-number">
        {investment_score}/100
        </div>

        <p>
        Investment Potential
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )


with score_col2:

    st.markdown(
        f"""
        <div class="result-card">

        <h2>
        📊 Location Score
        </h2>

        <h1 style="color:#7C3AED;">
        {location_score:.1f}/10
        </h1>

        <p>
        🚇 Connectivity: {connectivity}/10
        </p>

        <p>
        🏗️ Infrastructure: {infrastructure}/10
        </p>

        <p>
        📈 Demand: {demand}/10
        </p>

        <p>
        🎓 Education: {education}/10
        </p>

        <p>
        🏥 Healthcare: {healthcare}/10
        </p>

        <p>
        💼 Employment: {employment}/10
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# RENTAL ANALYSIS
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
🏠 Rental Income Analysis
</div>

<div class="section-subtitle">
Estimate potential rental income and cash flow.
</div>

</div>
""", unsafe_allow_html=True)


rent1, rent2, rent3 = st.columns(3)


with rent1:

    st.metric(

        "Monthly Rent",

        f"₹{expected_rent:,.0f}"

    )


with rent2:

    st.metric(

        "Annual Rent",

        f"₹{annual_rent:,.0f}"

    )


with rent3:

    st.metric(

        "Monthly Cash Flow",

        f"₹{monthly_cash_flow:,.0f}"

    )


# ============================================================
# APPRECIATION PROJECTION
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
📈 5-Year Property Projection
</div>

<div class="section-subtitle">
Estimate possible future property value using an assumed annual growth rate.
</div>

</div>
""", unsafe_allow_html=True)


appreciation_rate = st.slider(

    "Estimated Annual Appreciation (%)",

    0.0,

    20.0,

    7.0,

    0.5

)


future_value = (

    property_price
    * (
        1
        + appreciation_rate / 100
    ) ** 5

)


estimated_gain = (

    future_value
    - property_price

)


a1, a2, a3 = st.columns(3)


with a1:

    st.metric(

        "Current Value",

        f"₹{property_price:,.0f}"

    )


with a2:

    st.metric(

        "Estimated 5-Year Value",

        f"₹{future_value:,.0f}"

    )


with a3:

    st.metric(

        "Estimated Value Growth",

        f"₹{estimated_gain:,.0f}"

    )


# ============================================================
# BUY VS RENT
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
⚖️ Buy vs Rent Analysis
</div>

<div class="section-subtitle">
A simple comparison to support your decision-making.
</div>

</div>
""", unsafe_allow_html=True)


monthly_rent = st.number_input(

    "Alternative Monthly Rent for Similar Property (₹)",

    min_value=0,

    value=20000,

    step=1000,

    key="alternative_rent"

)


annual_rent_cost = (

    monthly_rent
    * 12

)


five_year_rent_cost = (

    annual_rent_cost
    * 5

)


buy1, buy2 = st.columns(2)


with buy1:

    st.markdown(
        f"""
        <div class="result-card">

        <h2>
        🏠 Buying
        </h2>

        <h1 style="color:#7C3AED;">
        ₹{property_price:,.0f}
        </h1>

        <p>
        Estimated EMI:
        ₹{emi:,.0f}/month
        </p>

        <p>
        Estimated 5-Year Property Value:
        ₹{future_value:,.0f}
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )


with buy2:

    st.markdown(
        f"""
        <div class="result-card">

        <h2>
        🏢 Renting
        </h2>

        <h1 style="color:#2563EB;">
        ₹{monthly_rent:,.0f}/month
        </h1>

        <p>
        Annual Rent:
        ₹{annual_rent_cost:,.0f}
        </p>

        <p>
        Estimated 5-Year Rent:
        ₹{five_year_rent_cost:,.0f}
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# SMART INSIGHTS
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
🤖 FirstChoice Smart Investment Insights
</div>

<div class="section-subtitle">
Automated insights based on your entered information.
</div>

</div>
""", unsafe_allow_html=True)


insights = []


if rental_yield >= 5:

    insights.append(
        "🏠 The estimated rental yield is relatively attractive."
    )

else:

    insights.append(
        "🏠 The estimated rental yield is relatively modest."
    )


if monthly_cash_flow >= 0:

    insights.append(
        "💰 Estimated rent is higher than the calculated EMI."
    )

else:

    insights.append(
        "🏦 Estimated EMI is higher than the expected monthly rent."
    )


if location_score >= 7:

    insights.append(
        "📍 The selected location factors indicate strong potential."
    )

else:

    insights.append(
        "📍 Consider researching infrastructure and local demand further."
    )


if investment_score >= 75:

    insights.append(
        "⭐ Overall estimated investment score is strong."
    )

elif investment_score >= 50:

    insights.append(
        "🟡 Overall estimated investment score is moderate."
    )

else:

    insights.append(
        "⚠️ Consider additional research before making an investment decision."
    )


st.markdown(
    f"""
    <div class="ai-card">

    <h2>
    🧠 Investment Insights
    </h2>

    <p>
    {insights[0]}
    </p>

    <p>
    {insights[1]}
    </p>

    <p>
    {insights[2]}
    </p>

    <p>
    {insights[3]}
    </p>

    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# FUTURE DATA INTELLIGENCE
# ============================================================

st.markdown("""
<div class="section-header">

<div class="section-title">
🚀 Future Investment Intelligence
</div>

<div class="section-subtitle">
Advanced features planned for the production platform.
</div>

</div>
""", unsafe_allow_html=True)


f1, f2, f3 = st.columns(3)


with f1:

    st.info(
        """
        🗺️ **Real Market Data**

        Local price trends and
        area-level market insights.
        """
    )


with f2:

    st.success(
        """
        📈 **AI Forecasting**

        Data-driven property growth
        projections.
        """
    )


with f3:

    st.warning(
        """
        🛡️ **Verified Intelligence**

        Combine property verification
        with investment insights.
        """
    )


# ============================================================
# FOOTER
# ============================================================

st.markdown("""
<div class="footer">

<h2>
🏠 FIRSTCHOICE INFRA PROPERTY HUB
</h2>

<p>
India's Next-Generation Real Estate Marketplace
</p>

<p>
Buy • Sell • Rent • Invest • Discover
</p>

<hr>

<small>
© FirstChoice Infra Property Hub
</small>

</div>
""", unsafe_allow_html=True)
