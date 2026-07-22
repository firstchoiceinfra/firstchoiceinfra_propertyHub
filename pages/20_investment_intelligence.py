import streamlit as st

# ============================================================
# PAGE 20 — PROPERTY INVESTMENT & ROI INTELLIGENCE
# FIRSTCHOICE INFRA PROPERTY HUB
# ============================================================

st.set_page_config(
    page_title="Investment Intelligence | FirstChoice Property Hub",
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
    font-size: 48px;
    font-weight: 900;
}

.hero p {
    font-size: 19px;
    line-height: 1.8;
}

/* SECTION */

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

/* RESULT */

.result-card {
    padding: 40px;
    border-radius: 32px;

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
    rgba(5,150,105,0.28);
}

.result-card h1 {
    font-size: 50px;
    font-weight: 900;
}

/* VALUE CARD */

.value-card {
    padding: 28px;
    border-radius: 27px;

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

    min-height: 180px;
}

/* AI */

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

/* WARNING */

.warning-card {
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

</style>
""", unsafe_allow_html=True)


# ============================================================
# HERO
# ============================================================

st.markdown("""
<div class="hero">

<h1>
📈 Property Investment Intelligence
</h1>

<p>
Analyse the potential financial performance of a property
before making an investment decision.
</p>

<p>
💰 Rental Income • 📊 ROI • 📈 Appreciation • 🏡 Property Value • 🎯 Investment Score
</p>

</div>
""", unsafe_allow_html=True)


# ============================================================
# AI INTRO
# ============================================================

st.markdown("""
<div class="ai-card">

<h2>
🤖 Your Real Estate Investment Intelligence Centre
</h2>

<p>
Enter the property purchase price, rental income,
expected appreciation and expenses to generate an
illustrative investment analysis.
</p>

<p>
The current version uses a calculation model.
Future versions can connect this dashboard with
live property data, rental data and market intelligence.
</p>

</div>
""", unsafe_allow_html=True)


# ============================================================
# PROPERTY DETAILS
# ============================================================

st.markdown("""
<div class="section">

<h2>
🏡 Investment Property Details
</h2>

<p>
Enter the financial details of the property.
</p>

</div>
""", unsafe_allow_html=True)


c1, c2 = st.columns(2)


with c1:

    property_name = st.text_input(
        "🏷️ Property Name",
        value="Premium Investment Property"
    )


with c2:

    property_location = st.text_input(
        "📍 Location",
        value="Mihan"
    )


c3, c4 = st.columns(2)


with c3:

    purchase_price = st.number_input(
        "💰 Purchase Price (₹)",
        min_value=100000,
        value=5000000,
        step=100000
    )


with c4:

    down_payment = st.number_input(
        "💵 Down Payment (₹)",
        min_value=0,
        value=1500000,
        step=100000
    )


# ============================================================
# RENTAL DETAILS
# ============================================================

st.markdown("""
<div class="section">

<h2>
🏠 Rental Income Analysis
</h2>

</div>
""", unsafe_allow_html=True)


r1, r2 = st.columns(2)


with r1:

    monthly_rent = st.number_input(
        "🏠 Expected Monthly Rent (₹)",
        min_value=0,
        value=25000,
        step=1000
    )


with r2:

    occupancy = st.slider(
        "📅 Expected Occupancy",
        min_value=50,
        max_value=100,
        value=90,
        step=5
    )


# ============================================================
# EXPENSES
# ============================================================

st.markdown("""
<div class="section">

<h2>
💳 Annual Property Expenses
</h2>

</div>
""", unsafe_allow_html=True)


e1, e2, e3 = st.columns(3)


with e1:

    maintenance = st.number_input(
        "🔧 Maintenance / Year (₹)",
        min_value=0,
        value=30000,
        step=5000
    )


with e2:

    property_tax = st.number_input(
        "🏛️ Property Tax / Year (₹)",
        min_value=0,
        value=12000,
        step=1000
    )


with e3:

    other_expenses = st.number_input(
        "📋 Other Expenses / Year (₹)",
        min_value=0,
        value=10000,
        step=1000
    )


# ============================================================
# APPRECIATION
# ============================================================

st.markdown("""
<div class="section">

<h2>
📈 Future Property Appreciation
</h2>

</div>
""", unsafe_allow_html=True)


a1, a2 = st.columns(2)


with a1:

    expected_appreciation = st.slider(
        "📈 Expected Annual Appreciation (%)",
        min_value=0.0,
        max_value=20.0,
        value=8.0,
        step=0.5
    )


with a2:

    projection_years = st.slider(
        "📅 Investment Projection",
        min_value=1,
        max_value=20,
        value=5
    )


# ============================================================
# CALCULATIONS
# ============================================================

annual_gross_rent = (
    monthly_rent
    *
    12
    *
    occupancy
    /
    100
)


annual_expenses = (
    maintenance
    +
    property_tax
    +
    other_expenses
)


annual_net_rental_income = (
    annual_gross_rent
    -
    annual_expenses
)


rental_yield = (

    annual_net_rental_income
    /
    purchase_price
    *
    100

    if purchase_price > 0

    else 0
)


future_property_value = (

    purchase_price
    *
    (
        1
        +
        expected_appreciation
        /
        100
    )
    **
    projection_years

)


capital_appreciation = (

    future_property_value
    -
    purchase_price

)


total_rental_income = (

    annual_net_rental_income
    *
    projection_years

)


total_estimated_return = (

    capital_appreciation
    +
    total_rental_income

)


total_roi = (

    total_estimated_return
    /
    purchase_price
    *
    100

    if purchase_price > 0

    else 0

)


# ============================================================
# INVESTMENT SCORE
# ============================================================

score = 0


if rental_yield >= 5:

    score += 35

elif rental_yield >= 3:

    score += 25

elif rental_yield >= 2:

    score += 15


if expected_appreciation >= 10:

    score += 35

elif expected_appreciation >= 7:

    score += 25

elif expected_appreciation >= 5:

    score += 15


if occupancy >= 90:

    score += 20

elif occupancy >= 75:

    score += 15

else:

    score += 8


if down_payment >= purchase_price * 0.25:

    score += 10

elif down_payment >= purchase_price * 0.15:

    score += 7

else:

    score += 4


# ============================================================
# GENERATE ANALYSIS
# ============================================================

if st.button(
    "🚀 GENERATE INVESTMENT ANALYSIS",
    use_container_width=True
):

    st.session_state.investment_analysis = True


if st.session_state.get(
    "investment_analysis",
    False
):

    # ========================================================
    # MAIN RESULT
    # ========================================================

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
        Estimated Investment Score
        </p>

        <h1>
        {score}/100
        </h1>

        <p>
        Illustrative analysis based on the information provided.
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )


    # ========================================================
    # KEY METRICS
    # ========================================================

    st.write("")


    m1, m2, m3, m4 = st.columns(4)


    with m1:

        st.markdown(
            f"""
            <div class="value-card">

            <h3>
            🏠 Net Rental Income
            </h3>

            <h2>
            ₹{annual_net_rental_income:,.0f}
            </h2>

            <p>
            Per year
            </p>

            </div>
            """,
            unsafe_allow_html=True
        )


    with m2:

        st.markdown(
            f"""
            <div class="value-card">

            <h3>
            📈 Rental Yield
            </h3>

            <h2>
            {rental_yield:.2f}%
            </h2>

            <p>
            Estimated annual yield
            </p>

            </div>
            """,
            unsafe_allow_html=True
        )


    with m3:

        st.markdown(
            f"""
            <div class="value-card">

            <h3>
            💎 Future Value
            </h3>

            <h2>
            ₹{future_property_value:,.0f}
            </h2>

            <p>
            After {projection_years} years
            </p>

            </div>
            """,
            unsafe_allow_html=True
        )


    with m4:

        st.markdown(
            f"""
            <div class="value-card">

            <h3>
            🚀 Total ROI
            </h3>

            <h2>
            {total_roi:.2f}%
            </h2>

            <p>
            Rental + appreciation
            </p>

            </div>
            """,
            unsafe_allow_html=True
        )


    # ========================================================
    # FINANCIAL BREAKDOWN
    # ========================================================

    st.markdown("""
    <div class="section">

    <h2>
    💰 Investment Financial Breakdown
    </h2>

    </div>
    """, unsafe_allow_html=True)


    b1, b2 = st.columns(2)


    with b1:

        st.markdown(
            f"""
            <div class="value-card">

            <h3>
            📊 Total Rental Income
            </h3>

            <h2>
            ₹{total_rental_income:,.0f}
            </h2>

            <p>
            Estimated net rental income over
            {projection_years} years.
            </p>

            </div>
            """,
            unsafe_allow_html=True
        )


    with b2:

        st.markdown(
            f"""
            <div class="value-card">

            <h3>
            📈 Capital Appreciation
            </h3>

            <h2>
            ₹{capital_appreciation:,.0f}
            </h2>

            <p>
            Estimated property value appreciation.
            </p>

            </div>
            """,
            unsafe_allow_html=True
        )


# ============================================================
# INVESTMENT INSIGHT
# ============================================================

if st.session_state.get(
    "investment_analysis",
    False
):

    st.markdown("""
    <div class="section">

    <h2>
    🧠 Smart Investment Insight
    </h2>

    </div>
    """, unsafe_allow_html=True)


    if score >= 80:

        st.success(
            "🚀 Strong Illustrative Investment Profile — "
            "The property shows attractive rental and appreciation assumptions."
        )

    elif score >= 60:

        st.info(
            "📈 Moderate-to-Strong Investment Profile — "
            "Further research into location, financing and market conditions is recommended."
        )

    else:

        st.warning(
            "⚠️ Cautious Investment Profile — "
            "Consider comparing this property with other opportunities."
        )


# ============================================================
# FIVE YEAR / PROJECTION TABLE
# ============================================================

if st.session_state.get(
    "investment_analysis",
    False
):

    st.markdown("""
    <div class="section">

    <h2>
    📅 Property Value Projection
    </h2>

    </div>
    """, unsafe_allow_html=True)


    projection_data = []


    for year in range(
        1,
        projection_years + 1
    ):

        value = (

            purchase_price
            *
            (
                1
                +
                expected_appreciation
                /
                100
            )
            **
            year

        )


        rental = (

            annual_net_rental_income
            *
            year

        )


        total_return = (

            value
            -
            purchase_price
            +
            rental

        )


        projection_data.append({

            "Year": year,

            "Estimated Property Value":
            round(value),

            "Cumulative Net Rental":
            round(rental),

            "Total Estimated Return":
            round(total_return)

        })


    st.dataframe(
        projection_data,
        use_container_width=True,
        hide_index=True
    )


# ============================================================
# INVESTMENT STRATEGIES
# ============================================================

st.markdown("""
<div class="section">

<h2>
🎯 Choose Your Investment Strategy
</h2>

</div>
""", unsafe_allow_html=True)


s1, s2, s3 = st.columns(3)


with s1:

    st.markdown("""
    <div class="value-card">

    <h2>
    🏠 Rental Income
    </h2>

    <p>
    Focus on properties with strong rental demand
    and consistent occupancy potential.
    </p>

    </div>
    """, unsafe_allow_html=True)


with s2:

    st.markdown("""
    <div class="value-card">

    <h2>
    📈 Capital Growth
    </h2>

    <p>
    Focus on emerging locations with infrastructure
    and long-term appreciation potential.
    </p>

    </div>
    """, unsafe_allow_html=True)


with s3:

    st.markdown("""
    <div class="value-card">

    <h2>
    🔄 Hybrid Strategy
    </h2>

    <p>
    Combine rental income with long-term
    capital appreciation.
    </p>

    </div>
    """, unsafe_allow_html=True)


# ============================================================
# FUTURE AI
# ============================================================

st.markdown("""
<div class="ai-card">

<h2>
🚀 Future AI Investment Intelligence
</h2>

<p>
Future versions can analyse:
</p>

<p>
📍 Location Growth
&nbsp; • &nbsp;
🏗️ Infrastructure
&nbsp; • &nbsp;
🏠 Rental Demand
&nbsp; • &nbsp;
📊 Historical Prices
&nbsp; • &nbsp;
💰 Financing Cost
&nbsp; • &nbsp;
📈 Market Trends
</p>

<p>
The system can create a personalised investment report
and compare multiple properties side-by-side.
</p>

</div>
""", unsafe_allow_html=True)


# ============================================================
# DISCLAIMER
# ============================================================

st.markdown("""
<div class="warning-card">

<h2>
⚠️ Important Investment Disclaimer
</h2>

<p>
All calculations on this page are illustrative estimates
based on user-provided assumptions. They are not guaranteed
returns, financial advice or investment recommendations.
</p>

<p>
Actual property returns depend on market conditions,
vacancy, taxes, financing costs, maintenance, legal factors
and many other variables.
</p>

</div>
""", unsafe_allow_html=True)
