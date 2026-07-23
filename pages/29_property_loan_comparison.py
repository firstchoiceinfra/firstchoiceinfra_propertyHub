import streamlit as st

# ============================================================
# PAGE 29 — SMART PROPERTY LOAN & EMI COMPARISON CENTER
# FIRSTCHOICE INFRA PROPERTY HUB
# ============================================================

st.set_page_config(
    page_title="Property Loan Comparison | FirstChoice Property Hub",
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

.best-card {
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
🏦 Smart Property Loan & EMI Comparison Center
</h1>

<p>
Compare multiple home loan offers and understand the
true cost of financing your property purchase.
</p>

<p>
💰 Loan Amount • 📊 Interest • 📅 Tenure • 💳 EMI • 💸 Processing Fee
</p>

</div>
""", unsafe_allow_html=True)


# ============================================================
# INTRO
# ============================================================

st.markdown("""
<div class="ai-card">

<h2>
🤖 Smart Loan Decision Engine
</h2>

<p>
Enter loan offers from different lenders and compare
monthly EMI, total interest, processing fees and total
repayment cost.
</p>

<p>
This helps buyers understand which financing option may
be more suitable for their requirements.
</p>

</div>
""", unsafe_allow_html=True)


# ============================================================
# PROPERTY & LOAN REQUIREMENT
# ============================================================

st.markdown("""
<div class="section">

<h2>
🏡 Property Loan Requirement
</h2>

</div>
""", unsafe_allow_html=True)


c1, c2, c3 = st.columns(3)


with c1:

    property_price = st.number_input(
        "🏠 Property Price (₹)",
        min_value=0,
        value=5000000,
        step=100000
    )


with c2:

    down_payment = st.number_input(
        "💰 Down Payment (₹)",
        min_value=0,
        value=1500000,
        step=100000
    )


with c3:

    required_loan = max(
        property_price
        -
        down_payment,
        0
    )


    st.metric(
        "🏦 Required Loan",
        f"₹{required_loan:,.0f}"
    )


# ============================================================
# NUMBER OF LOAN OFFERS
# ============================================================

st.markdown("""
<div class="section">

<h2>
🏦 Compare Lenders
</h2>

</div>
""", unsafe_allow_html=True)


lender_count = st.selectbox(
    "How many loan offers do you want to compare?",
    [2, 3, 4, 5]
)


loans = []


# ============================================================
# LOAN INPUTS
# ============================================================

for i in range(lender_count):

    st.markdown(
        f"""
        <div class="section">

        <h2>
        🏦 Loan Offer {i + 1}
        </h2>

        </div>
        """,
        unsafe_allow_html=True
    )

    c1, c2, c3 = st.columns(3)


    with c1:

        lender_name = st.text_input(
            f"🏦 Lender / Bank Name",
            value=f"Lender {i + 1}",
            key=f"lender_{i}"
        )


    with c2:

        interest_rate = st.number_input(
            f"📊 Interest Rate (%)",
            min_value=0.0,
            max_value=30.0,
            value=8.5,
            step=0.05,
            key=f"interest_{i}"
        )


    with c3:

        tenure = st.number_input(
            f"📅 Loan Tenure (Years)",
            min_value=1,
            max_value=40,
            value=20,
            key=f"tenure_{i}"
        )


    c4, c5, c6 = st.columns(3)


    with c4:

        processing_fee = st.number_input(
            f"💳 Processing Fee (₹)",
            min_value=0,
            value=10000,
            step=1000,
            key=f"processing_{i}"
        )


    with c5:

        other_charges = st.number_input(
            f"📄 Other Charges (₹)",
            min_value=0,
            value=5000,
            step=1000,
            key=f"other_{i}"
        )


    with c6:

        floating_rate = st.checkbox(
            "📈 Floating Interest Rate",
            value=True,
            key=f"floating_{i}"
        )


    loans.append({

        "lender":
        lender_name,

        "interest":
        interest_rate,

        "tenure":
        tenure,

        "processing":
        processing_fee,

        "other":
        other_charges,

        "floating":
        floating_rate

    })


# ============================================================
# EMI CALCULATOR
# ============================================================

def calculate_loan(
    principal,
    annual_rate,
    years
):

    months = (
        years
        *
        12
    )

    monthly_rate = (

        annual_rate
        /
        12
        /
        100

    )


    if principal <= 0:

        return 0, 0, 0


    if monthly_rate == 0:

        emi = (
            principal
            /
            months
        )

    else:

        emi = (

            principal
            *
            monthly_rate
            *
            (
                1
                +
                monthly_rate
            )
            ** months

            /

            (
                (
                    1
                    +
                    monthly_rate
                )
                ** months
                -
                1
            )

        )


    total_payment = (

        emi
        *
        months

    )


    total_interest = (

        total_payment
        -
        principal

    )


    return (

        emi,
        total_payment,
        total_interest

    )


# ============================================================
# CALCULATE COMPARISON
# ============================================================

results = []


for loan in loans:

    emi, total_payment, total_interest = calculate_loan(

        required_loan,

        loan["interest"],

        loan["tenure"]

    )


    total_cost = (

        total_payment
        +
        loan["processing"]
        +
        loan["other"]

    )


    results.append({

        "Lender":
        loan["lender"],

        "Interest Rate":
        f"{loan['interest']:.2f}%",

        "Tenure":
        f"{loan['tenure']} Years",

        "Monthly EMI":
        f"₹{emi:,.0f}",

        "Total Interest":
        f"₹{total_interest:,.0f}",

        "Processing Fee":
        f"₹{loan['processing']:,.0f}",

        "Other Charges":
        f"₹{loan['other']:,.0f}",

        "Total Loan Cost":
        f"₹{total_cost:,.0f}",

        "Rate Type":
        "Floating"
        if loan["floating"]
        else "Fixed"

    })


# ============================================================
# COMPARISON TABLE
# ============================================================

st.markdown("""
<div class="section">

<h2>
📊 Loan Offer Comparison
</h2>

</div>
""", unsafe_allow_html=True)


st.dataframe(
    results,
    use_container_width=True,
    hide_index=True
)


# ============================================================
# BEST LOAN
# ============================================================

best_index = min(

    range(
        len(results)
    ),

    key=lambda i:
    calculate_loan(

        required_loan,

        loans[i]["interest"],

        loans[i]["tenure"]

    )[1]

    +
    loans[i]["processing"]

    +
    loans[i]["other"]

)


best_loan = loans[
    best_index
]


best_emi, best_payment, best_interest = calculate_loan(

    required_loan,

    best_loan["interest"],

    best_loan["tenure"]

)


best_total_cost = (

    best_payment
    +
    best_loan["processing"]
    +
    best_loan["other"]

)


# ============================================================
# RECOMMENDATION
# ============================================================

st.markdown(
    f"""
    <div class="best-card">

    <h2>
    🏆 Lowest Estimated Financing Cost
    </h2>

    <h1>
    {best_loan['lender']}
    </h1>

    <p>
    📊 Interest Rate:
    {best_loan['interest']:.2f}%
    </p>

    <p>
    💳 Monthly EMI:
    ₹{best_emi:,.0f}
    </p>

    <p>
    💸 Total Interest:
    ₹{best_interest:,.0f}
    </p>

    <p>
    💰 Estimated Total Loan Cost:
    ₹{best_total_cost:,.0f}
    </p>

    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# EMI AFFORDABILITY
# ============================================================

st.markdown("""
<div class="section">

<h2>
💰 EMI Affordability Check
</h2>

</div>
""", unsafe_allow_html=True)


monthly_income = st.number_input(
    "👤 Your Monthly Household Income (₹)",
    min_value=0,
    value=100000,
    step=5000
)


existing_emi = st.number_input(
    "🏦 Existing Monthly EMI Obligations (₹)",
    min_value=0,
    value=0,
    step=1000
)


total_monthly_obligation = (

    best_emi
    +
    existing_emi

)


emi_ratio = (

    total_monthly_obligation
    /
    monthly_income
    *
    100

) if monthly_income > 0 else 0


if emi_ratio <= 40:

    affordability_message = (
        "🟢 Estimated EMI burden is within a relatively comfortable range."
    )

elif emi_ratio <= 60:

    affordability_message = (
        "🟠 Estimated EMI burden is moderate. Review your monthly budget carefully."
    )

else:

    affordability_message = (
        "🔴 Estimated EMI burden is high. Consider a larger down payment or longer tenure."
    )


st.markdown(
    f"""
    <div class="card">

    <h2>
    {affordability_message}
    </h2>

    <p>
    Total Monthly EMI Obligations:
    <b>₹{total_monthly_obligation:,.0f}</b>
    </p>

    <p>
    EMI-to-Income Ratio:
    <b>{emi_ratio:.1f}%</b>
    </p>

    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# LOAN DECISION
# ============================================================

st.markdown("""
<div class="section">

<h2>
🎯 Next Step
</h2>

</div>
""", unsafe_allow_html=True)


next_step = st.selectbox(
    "Choose your next action",
    [
        "📄 Start Loan Application",
        "📞 Request Loan Consultation",
        "🏦 Compare More Lenders",
        "💰 Increase Down Payment",
        "📈 Recalculate With Different Tenure",
        "🏡 Return to Property Investment Planner"
    ]
)


if st.button(
    "🚀 CONTINUE",
    use_container_width=True
):

    st.success(
        f"✅ Selected action: {next_step}"
    )


# ============================================================
# FUTURE FEATURES
# ============================================================

st.markdown("""
<div class="ai-card">

<h2>
🚀 Future Smart Loan Features
</h2>

<p>
Production version में आगे ये features जोड़े जा सकते हैं:
</p>

<p>
🏦 Real-Time Lender Offers
&nbsp; • &nbsp;
📄 Digital Loan Application
&nbsp; • &nbsp;
🤖 AI Eligibility Prediction
&nbsp; • &nbsp;
📊 Credit Score Integration
&nbsp; • &nbsp;
💳 Pre-Approval Tracking
&nbsp; • &nbsp;
📱 Loan Document Upload
&nbsp; • &nbsp;
🔔 EMI Due Reminders
&nbsp; • &nbsp;
📈 Interest Rate Change Alerts
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
The calculations shown are estimates based on the information
entered by the user. Actual loan approval, interest rates,
processing fees, taxes and repayment terms depend on the
lender's policies and the applicant's eligibility.
</p>

<p>
This tool is for informational purposes only and does not
guarantee loan approval or represent financial advice.
</p>

</div>
""", unsafe_allow_html=True)
