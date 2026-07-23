import streamlit as st

# ============================================================
# PAGE 28 — SMART PROPERTY INVESTMENT & ROI PLANNER
# FIRSTCHOICE INFRA PROPERTY HUB
# ============================================================

st.set_page_config(
    page_title="Property Investment ROI Planner | FirstChoice Property Hub",
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
    font-size: 18px;
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
    font-size: 29px;
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

    margin-bottom: 20px;
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

.profit-card {
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
    0 20px 60px
    rgba(5,150,105,0.25);
}

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
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# HERO
# ============================================================

st.markdown("""
<div class="hero">

<h1>
📈 Smart Property Investment & ROI Planner
</h1>

<p>
Understand the potential financial performance of a
property before making an investment decision.
</p>

<p>
💰 Purchase • 🏦 Loan • 🏠 Rent • 📈 Appreciation • 💸 Expenses • 📊 ROI
</p>

</div>
""", unsafe_allow_html=True)


# ============================================================
# INTRO
# ============================================================

st.markdown("""
<div class="ai-card">

<h2>
🤖 Property Investment Intelligence
</h2>

<p>
This tool helps users estimate potential rental income,
property appreciation, annual expenses and overall return
over a selected investment period.
</p>

<p>
The goal is to make property investment decisions more
data-driven instead of relying only on the purchase price.
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

</div>
""", unsafe_allow_html=True)


c1, c2 = st.columns(2)


with c1:

    property_name = st.text_input(
        "🏠 Property Name",
        value="Investment Property"
    )


with c2:

    location = st.text_input(
        "📍 Location"
    )


# ============================================================
# PURCHASE DETAILS
# ============================================================

st.markdown("""
<div class="section">

<h2>
💰 Purchase & Acquisition Cost
</h2>

</div>
""", unsafe_allow_html=True)


p1, p2, p3 = st.columns(3)


with p1:

    purchase_price = st.number_input(
        "🏷️ Purchase Price (₹)",
        min_value=0,
        value=5000000,
        step=100000
    )


with p2:

    registration_cost = st.number_input(
        "📄 Registration & Stamp Duty (₹)",
        min_value=0,
        value=300000,
        step=10000
    )


with p3:

    renovation_cost = st.number_input(
        "🔨 Renovation / Setup Cost (₹)",
        min_value=0,
        value=100000,
        step=10000
    )


total_initial_investment = (

    purchase_price
    +
    registration_cost
    +
    renovation_cost

)


# ============================================================
# LOAN DETAILS
# ============================================================

st.markdown("""
<div class="section">

<h2>
🏦 Financing Details
</h2>

</div>
""", unsafe_allow_html=True)


l1, l2, l3 = st.columns(3)


with l1:

    loan_amount = st.number_input(
        "🏦 Loan Amount (₹)",
        min_value=0,
        value=3000000,
        step=100000
    )


with l2:

    interest_rate = st.number_input(
        "📊 Annual Interest Rate (%)",
        min_value=0.0,
        max_value=30.0,
        value=8.5,
        step=0.1
    )


with l3:

    loan_years = st.number_input(
        "📅 Loan Tenure (Years)",
        min_value=1,
        max_value=40,
        value=20
    )


# ============================================================
# EMI CALCULATION
# ============================================================

monthly_rate = (
    interest_rate
    /
    12
    /
    100
)

number_of_payments = (
    loan_years
    *
    12
)


if loan_amount > 0 and monthly_rate > 0:

    monthly_emi = (

        loan_amount
        *
        monthly_rate
        *
        (
            (1 + monthly_rate)
            **
            number_of_payments
        )
        /
        (
            (
                1 + monthly_rate
            )
            **
            number_of_payments
            -
            1
        )

    )

elif loan_amount > 0:

    monthly_emi = (

        loan_amount
        /
        number_of_payments

    )

else:

    monthly_emi = 0


annual_emi = (
    monthly_emi
    *
    12
)


# ============================================================
# RENTAL INCOME
# ============================================================

st.markdown("""
<div class="section">

<h2>
🏠 Rental Income
</h2>

</div>
""", unsafe_allow_html=True)


r1, r2, r3 = st.columns(3)


with r1:

    monthly_rent = st.number_input(
        "💵 Expected Monthly Rent (₹)",
        min_value=0,
        value=25000,
        step=1000
    )


with r2:

    vacancy_rate = st.slider(
        "📅 Expected Vacancy (%)",
        0,
        50,
        5
    )


with r3:

    rent_growth = st.number_input(
        "📈 Annual Rent Growth (%)",
        min_value=0.0,
        max_value=30.0,
        value=5.0,
        step=0.5
    )


annual_gross_rent = (

    monthly_rent
    *
    12

)


effective_rent = (

    annual_gross_rent
    *
    (
        1
        -
        vacancy_rate
        /
        100
    )

)


# ============================================================
# EXPENSES
# ============================================================

st.markdown("""
<div class="section">

<h2>
💸 Annual Property Expenses
</h2>

</div>
""", unsafe_allow_html=True)


e1, e2, e3 = st.columns(3)


with e1:

    maintenance = st.number_input(
        "🔧 Maintenance (₹/Year)",
        min_value=0,
        value=30000,
        step=5000
    )


with e2:

    property_tax = st.number_input(
        "🏛️ Property Tax (₹/Year)",
        min_value=0,
        value=15000,
        step=5000
    )


with e3:

    insurance = st.number_input(
        "🛡️ Insurance (₹/Year)",
        min_value=0,
        value=10000,
        step=5000
    )


total_expenses = (

    maintenance
    +
    property_tax
    +
    insurance

)


# ============================================================
# APPRECIATION
# ============================================================

st.markdown("""
<div class="section">

<h2>
📈 Property Appreciation Forecast
</h2>

</div>
""", unsafe_allow_html=True)


a1, a2 = st.columns(2)


with a1:

    appreciation_rate = st.number_input(
        "📊 Expected Annual Appreciation (%)",
        min_value=-20.0,
        max_value=50.0,
        value=7.0,
        step=0.5
    )


with a2:

    investment_years = st.number_input(
        "📅 Investment Horizon (Years)",
        min_value=1,
        max_value=50,
        value=10
    )


future_property_value = (

    purchase_price
    *
    (
        1
        +
        appreciation_rate
        /
        100
    )
    **
    investment_years

)


capital_gain = (

    future_property_value
    -
    purchase_price

)


# ============================================================
# ROI CALCULATION
# ============================================================

annual_net_rental_income = (

    effective_rent
    -
    total_expenses

)


total_rental_income = (

    annual_net_rental_income
    *
    investment_years

)


total_capital_gain = capital_gain


estimated_total_return = (

    total_rental_income
    +
    total_capital_gain

)


simple_roi = (

    estimated_total_return
    /
    total_initial_investment
    *
    100

) if total_initial_investment > 0 else 0


# ============================================================
# RESULTS
# ============================================================

st.markdown("""
<div class="section">

<h2>
📊 Investment Performance Summary
</h2>

</div>
""", unsafe_allow_html=True)


m1, m2, m3 = st.columns(3)


with m1:

    st.markdown(
        f"""
        <div class="card">

        <h3>
        🏠 Total Initial Investment
        </h3>

        <h2>
        ₹{total_initial_investment:,.0f}
        </h2>

        </div>
        """,
        unsafe_allow_html=True
    )


with m2:

    st.markdown(
        f"""
        <div class="card">

        <h3>
        💵 Annual Net Rental Income
        </h3>

        <h2>
        ₹{annual_net_rental_income:,.0f}
        </h2>

        </div>
        """,
        unsafe_allow_html=True
    )


with m3:

    st.markdown(
        f"""
        <div class="card">

        <h3>
        📈 Future Property Value
        </h3>

        <h2>
        ₹{future_property_value:,.0f}
        </h2>

        </div>
        """,
        unsafe_allow_html=True
    )


m4, m5, m6 = st.columns(3)


with m4:

    st.markdown(
        f"""
        <div class="card">

        <h3>
        🏦 Monthly EMI
        </h3>

        <h2>
        ₹{monthly_emi:,.0f}
        </h2>

        </div>
        """,
        unsafe_allow_html=True
    )


with m5:

    st.markdown(
        f"""
        <div class="card">

        <h3>
        💰 Estimated Capital Gain
        </h3>

        <h2>
        ₹{capital_gain:,.0f}
        </h2>

        </div>
        """,
        unsafe_allow_html=True
    )


with m6:

    st.markdown(
        f"""
        <div class="profit-card">

        <h3>
        📊 Estimated Simple ROI
        </h3>

        <h1>
        {simple_roi:.2f}%
        </h1>

        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# CASH FLOW CHECK
# ============================================================

st.markdown("""
<div class="section">

<h2>
💸 Monthly Cash Flow Analysis
</h2>

</div>
""", unsafe_allow_html=True)


monthly_expenses = (

    total_expenses
    /
    12

)


monthly_net_rent = (

    effective_rent
    /
    12

)


monthly_cash_flow = (

    monthly_net_rent
    -
    monthly_emi
    -
    monthly_expenses

)


if monthly_cash_flow >= 0:

    cash_message = (
        "🟢 Positive estimated monthly cash flow"
    )

else:

    cash_message = (
        "🟠 Negative estimated monthly cash flow"
    )


st.markdown(
    f"""
    <div class="profit-card">

    <h2>
    {cash_message}
    </h2>

    <h1>
    ₹{monthly_cash_flow:,.0f} / Month
    </h1>

    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# INVESTMENT INSIGHT
# ============================================================

if simple_roi >= 100:

    insight = """
    The estimated long-term return appears strong under the
    assumptions entered. Consider validating appreciation,
    rental demand, financing costs and taxes before investing.
    """

elif simple_roi >= 50:

    insight = """
    The property shows a moderate estimated return.
    Compare it with alternative properties and investment options.
    """

else:

    insight = """
    The estimated return is relatively low under the current
    assumptions. Review the purchase price, rental potential
    and expected appreciation.
    """


st.markdown(
    f"""
    <div class="ai-card">

    <h2>
    🤖 Smart Investment Insight
    </h2>

    <p>
    {insight}
    </p>

    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# INVESTMENT DECISION
# ============================================================

st.markdown("""
<div class="section">

<h2>
🎯 Investment Decision
</h2>

</div>
""", unsafe_allow_html=True)


decision = st.radio(
    "What do you want to do next?",
    [
        "❤️ Add to Investment Watchlist",
        "🏦 Compare Loan Options",
        "📊 Compare With Another Property",
        "📍 Schedule Site Visit",
        "⚖️ Start Legal Verification",
        "🤝 Open Deal Room"
    ]
)


if st.button(
    "🚀 CONTINUE INVESTMENT JOURNEY",
    use_container_width=True
):

    st.success(
        f"✅ Selected next step: {decision}"
    )


# ============================================================
# FUTURE AI FEATURES
# ============================================================

st.markdown("""
<div class="ai-card">

<h2>
🚀 Future AI Investment Intelligence
</h2>

<p>
The production version can add:
</p>

<p>
📊 Market Price Prediction
&nbsp; • &nbsp;
🏠 Rental Demand Forecast
&nbsp; • &nbsp;
📈 AI Appreciation Forecast
&nbsp; • &nbsp;
💰 Tax Impact Calculator
&nbsp; • &nbsp;
🏦 Loan vs Cash Purchase Analysis
&nbsp; • &nbsp;
📉 Risk Score
&nbsp; • &nbsp;
📊 Multi-Property Portfolio ROI
</p>

<p>
Users could eventually build and monitor their complete
real-estate investment portfolio inside FirstChoice Property Hub.
</p>

</div>
""", unsafe_allow_html=True)


# ============================================================
# DISCLAIMER
# ============================================================

st.markdown("""
<div class="warning-card">

<h2>
⚠️ Important Financial Disclaimer
</h2>

<p>
All calculations on this page are estimates based on
user-entered assumptions. Actual property returns,
rental income, taxes, loan costs, market appreciation and
expenses may differ significantly.
</p>

<p>
This tool is for informational purposes only and is not
financial or investment advice.
</p>

</div>
""", unsafe_allow_html=True)
