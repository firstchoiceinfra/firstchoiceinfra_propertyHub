import streamlit as st

# ============================================================
# PAGE 21 — PROPERTY LOAN, EMI & HOME FINANCE CENTRE
# FIRSTCHOICE INFRA PROPERTY HUB
# ============================================================

st.set_page_config(
    page_title="Property Loan & EMI | FirstChoice Property Hub",
    page_icon="🏦",
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
    font-size: 48px;
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
    font-size: 48px;
    font-weight: 900;
}

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

.bank-card {
    padding: 28px;
    border-radius: 26px;

    background: white;

    border: 1px solid #E5E7EB;

    box-shadow:
    0 12px 35px
    rgba(0,0,0,0.07);

    min-height: 170px;
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
🏦 Property Loan & Home Finance Centre
</h1>

<p>
Plan your property purchase with an easy-to-understand
home loan and EMI calculation dashboard.
</p>

<p>
🏠 Property Price • 💰 Down Payment • 🏦 Loan Amount • 📊 EMI • 📈 Interest • 📅 Tenure
</p>

</div>
""", unsafe_allow_html=True)


# ============================================================
# INTRO
# ============================================================

st.markdown("""
<div class="ai-card">

<h2>
🤖 Smart Home Finance Planner
</h2>

<p>
Calculate your estimated monthly EMI, total interest,
total repayment and loan-to-property ratio.
</p>

<p>
Use this tool for preliminary planning before discussing
your financing options with a bank or financial institution.
</p>

</div>
""", unsafe_allow_html=True)


# ============================================================
# PROPERTY DETAILS
# ============================================================

st.markdown("""
<div class="section">

<h2>
🏡 Property & Purchase Details
</h2>

<p>
Enter your property purchase information.
</p>

</div>
""", unsafe_allow_html=True)


c1, c2 = st.columns(2)


with c1:

    property_price = st.number_input(
        "🏠 Property Price (₹)",
        min_value=100000,
        value=5000000,
        step=100000
    )


with c2:

    down_payment = st.number_input(
        "💰 Down Payment (₹)",
        min_value=0,
        value=1500000,
        step=50000
    )


# ============================================================
# LOAN DETAILS
# ============================================================

st.markdown("""
<div class="section">

<h2>
🏦 Loan Details
</h2>

</div>
""", unsafe_allow_html=True)


l1, l2, l3 = st.columns(3)


with l1:

    interest_rate = st.number_input(
        "📈 Annual Interest Rate (%)",
        min_value=0.0,
        max_value=30.0,
        value=8.5,
        step=0.1
    )


with l2:

    tenure_years = st.slider(
        "📅 Loan Tenure (Years)",
        min_value=1,
        max_value=30,
        value=20
    )


with l3:

    processing_fee_percent = st.number_input(
        "📋 Processing Fee (%)",
        min_value=0.0,
        max_value=10.0,
        value=0.5,
        step=0.1
    )


# ============================================================
# LOAN CALCULATION
# ============================================================

loan_amount = max(
    property_price - down_payment,
    0
)


monthly_rate = (
    interest_rate
    /
    12
    /
    100
)


total_months = (
    tenure_years
    *
    12
)


if loan_amount > 0 and monthly_rate > 0:

    emi = (

        loan_amount
        *
        monthly_rate
        *
        (
            1
            +
            monthly_rate
        )
        **
        total_months

    ) / (

        (
            1
            +
            monthly_rate
        )
        **
        total_months
        -
        1

    )

elif loan_amount > 0:

    emi = (
        loan_amount
        /
        total_months
    )

else:

    emi = 0


total_payment = (

    emi
    *
    total_months

)


total_interest = (

    total_payment
    -
    loan_amount

)


processing_fee = (

    loan_amount
    *
    processing_fee_percent
    /
    100

)


total_initial_cash = (

    down_payment
    +
    processing_fee

)


loan_to_value = (

    loan_amount
    /
    property_price
    *
    100

    if property_price > 0

    else 0

)


# ============================================================
# CALCULATE BUTTON
# ============================================================

if st.button(
    "🚀 CALCULATE HOME LOAN & EMI",
    use_container_width=True
):

    st.session_state.loan_calculated = True


# ============================================================
# RESULTS
# ============================================================

if st.session_state.get(
    "loan_calculated",
    False
):

    st.markdown("""
    <div class="section">

    <h2>
    📊 Your Home Loan Summary
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
        Loan Amount: ₹{loan_amount:,.0f}
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )


    st.write("")


    r1, r2, r3, r4 = st.columns(4)


    with r1:

        st.markdown(
            f"""
            <div class="value-card">

            <h3>
            🏦 Loan Amount
            </h3>

            <h2>
            ₹{loan_amount:,.0f}
            </h2>

            </div>
            """,
            unsafe_allow_html=True
        )


    with r2:

        st.markdown(
            f"""
            <div class="value-card">

            <h3>
            📈 Total Interest
            </h3>

            <h2>
            ₹{total_interest:,.0f}
            </h2>

            </div>
            """,
            unsafe_allow_html=True
        )


    with r3:

        st.markdown(
            f"""
            <div class="value-card">

            <h3>
            💳 Total Repayment
            </h3>

            <h2>
            ₹{total_payment:,.0f}
            </h2>

            </div>
            """,
            unsafe_allow_html=True
        )


    with r4:

        st.markdown(
            f"""
            <div class="value-card">

            <h3>
            📊 Loan-to-Value
            </h3>

            <h2>
            {loan_to_value:.1f}%
            </h2>

            </div>
            """,
            unsafe_allow_html=True
        )


# ============================================================
# CASH REQUIREMENT
# ============================================================

if st.session_state.get(
    "loan_calculated",
    False
):

    st.markdown("""
    <div class="section">

    <h2>
    💰 Initial Purchase Funding
    </h2>

    </div>
    """, unsafe_allow_html=True)


    q1, q2, q3 = st.columns(3)


    with q1:

        st.markdown(
            f"""
            <div class="value-card">

            <h3>
            💵 Down Payment
            </h3>

            <h2>
            ₹{down_payment:,.0f}
            </h2>

            </div>
            """,
            unsafe_allow_html=True
        )


    with q2:

        st.markdown(
            f"""
            <div class="value-card">

            <h3>
            📋 Processing Fee
            </h3>

            <h2>
            ₹{processing_fee:,.0f}
            </h2>

            </div>
            """,
            unsafe_allow_html=True
        )


    with q3:

        st.markdown(
            f"""
            <div class="value-card">

            <h3>
            💰 Estimated Initial Cash
            </h3>

            <h2>
            ₹{total_initial_cash:,.0f}
            </h2>

            <p>
            Down payment + processing fee
            </p>

            </div>
            """,
            unsafe_allow_html=True
        )


# ============================================================
# LOAN BREAKDOWN
# ============================================================

if st.session_state.get(
    "loan_calculated",
    False
):

    st.markdown("""
    <div class="section">

    <h2>
    📊 Loan Cost Breakdown
    </h2>

    </div>
    """, unsafe_allow_html=True)


    chart_data = {

        "Amount": [
            loan_amount,
            total_interest
        ]

    }


    st.bar_chart(
        chart_data
    )


# ============================================================
# AFFORDABILITY ANALYSIS
# ============================================================

st.markdown("""
<div class="section">

<h2>
💼 EMI Affordability Planner
</h2>

<p>
Enter your approximate monthly household income to estimate
the EMI burden.
</p>

</div>
""", unsafe_allow_html=True)


monthly_income = st.number_input(
    "💼 Monthly Household Income (₹)",
    min_value=0,
    value=100000,
    step=5000
)


emi_income_ratio = (

    emi
    /
    monthly_income
    *
    100

    if monthly_income > 0

    else 0

)


if st.session_state.get(
    "loan_calculated",
    False
):

    st.markdown(
        f"""
        <div class="value-card">

        <h2>
        📊 Estimated EMI-to-Income Ratio
        </h2>

        <h1>
        {emi_income_ratio:.1f}%
        </h1>

        <p>
        Monthly EMI: ₹{emi:,.0f}
        <br>
        Monthly Income: ₹{monthly_income:,.0f}
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )


    if emi_income_ratio <= 30:

        st.success(
            "✅ The estimated EMI is within a relatively comfortable range based on the income entered."
        )

    elif emi_income_ratio <= 45:

        st.info(
            "📊 The estimated EMI represents a moderate portion of the income entered."
        )

    else:

        st.warning(
            "⚠️ The estimated EMI represents a high portion of the income entered. Consider reviewing the loan amount or tenure."
        )


# ============================================================
# BANK FINANCE CENTRE
# ============================================================

st.markdown("""
<div class="section">

<h2>
🏦 Home Finance Discovery Centre
</h2>

<p>
Compare financing options with different lenders and
understand the factors that may affect your loan.
</p>

</div>
""", unsafe_allow_html=True)


b1, b2, b3 = st.columns(3)


with b1:

    st.markdown("""
    <div class="bank-card">

    <h2>
    🏦 Bank Loan
    </h2>

    <p>
    Explore home loan products from banks
    and compare eligibility requirements.
    </p>

    </div>
    """, unsafe_allow_html=True)


with b2:

    st.markdown("""
    <div class="bank-card">

    <h2>
    💳 Housing Finance
    </h2>

    <p>
    Explore housing finance companies
    and available financing options.
    </p>

    </div>
    """, unsafe_allow_html=True)


with b3:

    st.markdown("""
    <div class="bank-card">

    <h2>
    📄 Loan Documents
    </h2>

    <p>
    Understand common documents required
    during the home loan application process.
    </p>

    </div>
    """, unsafe_allow_html=True)


# ============================================================
# DOCUMENT CHECKLIST
# ============================================================

st.markdown("""
<div class="section">

<h2>
📋 Home Loan Document Checklist
</h2>

</div>
""", unsafe_allow_html=True)


documents = [

    "🪪 Identity Proof",

    "🏠 Address Proof",

    "💼 Income Proof",

    "🏦 Bank Statements",

    "📄 Property Documents",

    "📑 Sale Agreement",

    "💰 Down Payment Proof"

]


for document in documents:

    st.checkbox(
        document
    )


# ============================================================
# SMART FINANCE FEATURES
# ============================================================

st.markdown("""
<div class="section">

<h2>
🚀 Smart Finance Features
</h2>

</div>
""", unsafe_allow_html=True)


f1, f2, f3, f4 = st.columns(4)


with f1:

    st.markdown("""
    <div class="value-card">

    <h3>
    🧮 EMI Calculator
    </h3>

    <p>
    Estimate monthly loan repayment.
    </p>

    </div>
    """, unsafe_allow_html=True)


with f2:

    st.markdown("""
    <div class="value-card">

    <h3>
    📊 Loan Comparison
    </h3>

    <p>
    Compare different interest rates and tenures.
    </p>

    </div>
    """, unsafe_allow_html=True)


with f3:

    st.markdown("""
    <div class="value-card">

    <h3>
    💼 Affordability
    </h3>

    <p>
    Understand the estimated EMI burden.
    </p>

    </div>
    """, unsafe_allow_html=True)


with f4:

    st.markdown("""
    <div class="value-card">

    <h3>
    📄 Document Centre
    </h3>

    <p>
    Track your loan document checklist.
    </p>

    </div>
    """, unsafe_allow_html=True)


# ============================================================
# FUTURE AI FINANCE
# ============================================================

st.markdown("""
<div class="ai-card">

<h2>
🚀 Future AI Home Finance Engine
</h2>

<p>
The future version of Property Hub can connect users with
a complete digital property financing journey.
</p>

<p>
🤖 AI Loan Eligibility
&nbsp; • &nbsp;
🏦 Lender Matching
&nbsp; • &nbsp;
📊 Loan Comparison
&nbsp; • &nbsp;
📄 Digital Documents
&nbsp; • &nbsp;
🔐 Secure Application Tracking
</p>

<p>
Users can discover a property, calculate affordability,
explore financing options and track their home loan journey
from one integrated platform.
</p>

</div>
""", unsafe_allow_html=True)


# ============================================================
# DISCLAIMER
# ============================================================

st.markdown("""
<div class="warning-card">

<h2>
⚠️ Important Finance Disclaimer
</h2>

<p>
The EMI, interest and affordability calculations shown here
are illustrative estimates based on the information entered.
</p>

<p>
Actual loan approval, interest rate, eligibility, processing
fees and terms are determined by the respective lender.
</p>

</div>
""", unsafe_allow_html=True)
