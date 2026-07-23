import streamlit as st

# ============================================================
# PAGE 28 — SMART PROPERTY INVESTMENT & FINANCE CENTER
# FIRSTCHOICE INFRA PROPERTY HUB
#
# MERGED:
# PAGE 28 — PROPERTY INVESTMENT & ROI PLANNER
# PAGE 29 — PROPERTY LOAN & EMI COMPARISON CENTER
# ============================================================

st.set_page_config(
    page_title="Property Investment & Finance Center | FirstChoice Property Hub",
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
    font-size: 46px;
    font-weight: 900;
}

.hero p {
    font-size: 18px;
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
    font-size: 29px;
    font-weight: 900;
}

/* CARD */

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

/* AI CARD */

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

/* PROFIT CARD */

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

/* BEST LOAN CARD */

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
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# HERO
# ============================================================

st.markdown("""
<div class="hero">

<h1>
📈 Smart Property Investment & Finance Center
</h1>

<p>
Analyze property investment potential, calculate ROI,
estimate rental income, forecast appreciation and compare
multiple property loan offers in one place.
</p>

<p>
🏠 Property Investment
&nbsp; • &nbsp;
📊 ROI
&nbsp; • &nbsp;
💰 Rental Income
&nbsp; • &nbsp;
📈 Appreciation
&nbsp; • &nbsp;
🏦 Loan EMI
&nbsp; • &nbsp;
💳 Lender Comparison
</p>

</div>
""", unsafe_allow_html=True)


# ============================================================
# CENTER INTRO
# ============================================================

st.markdown("""
<div class="ai-card">

<h2>
🤖 Smart Property Investment & Finance Intelligence
</h2>

<p>
This unified center helps users evaluate the potential
financial performance of a property and understand the
financing cost before making an investment decision.
</p>

<p>
Compare property returns, rental income, appreciation,
cash flow, EMI affordability and multiple loan offers
from different lenders.
</p>

</div>
""", unsafe_allow_html=True)


# ============================================================
# PROPERTY DETAILS
# ============================================================

st.markdown("""
<div class="section">
<h2>
🏡 Property & Investment Details
</h2>
</div>
""", unsafe_allow_html=True)


c1, c2, c3 = st.columns(3)

with c1:

    property_name = st.text_input(
        "🏠 Property Name",
        value="Investment Property"
    )

with c2:

    location = st.text_input(
        "📍 Location"
    )

with c3:

    property_price = st.number_input(
        "🏷️ Property Price (₹)",
        min_value=0,
        value=5000000,
        step=100000
    )


# ============================================================
# PURCHASE COST
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

    registration_cost = st.number_input(
        "📄 Registration & Stamp Duty (₹)",
        min_value=0,
        value=300000,
        step=10000
    )

with p2:

    renovation_cost = st.number_input(
        "🔨 Renovation / Setup Cost (₹)",
        min_value=0,
        value=100000,
        step=10000
    )

with p3:

    down_payment = st.number_input(
        "💰 Down Payment (₹)",
        min_value=0,
        value=1500000,
        step=100000
    )


# ============================================================
# INITIAL INVESTMENT
# ============================================================

total_initial_investment = (
    property_price
    +
    registration_cost
    +
    renovation_cost
)


required_loan = max(
    property_price - down_payment,
    0
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
    monthly_rent * 12
)


effective_rent = (
    annual_gross_rent
    *
    (
        1
        -
        vacancy_rate / 100
    )
)


# ============================================================
# PROPERTY EXPENSES
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
# PROPERTY APPRECIATION
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
    property_price
    *
    (
        1
        +
        appreciation_rate / 100
    )
    **
    investment_years
)


capital_gain = (
    future_property_value
    -
    property_price
)


# ============================================================
# NET RENTAL & ROI
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


estimated_total_return = (
    total_rental_income
    +
    capital_gain
)


simple_roi = (

    estimated_total_return
    /
    total_initial_investment
    *
    100

) if total_initial_investment > 0 else 0


# ============================================================
# ROI SUMMARY
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
        🏦 Required Loan
        </h3>

        <h2>
        ₹{required_loan:,.0f}
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
# LOAN SECTION
# ============================================================

st.markdown("""
<div class="section">
<h2>
🏦 Smart Loan & EMI Comparison Center
</h2>
</div>
""", unsafe_allow_html=True)


st.markdown("""
<div class="ai-card">

<h2>
🤖 Compare Multiple Lenders
</h2>

<p>
Enter loan offers from different lenders and compare
monthly EMI, total interest, processing fees and
estimated total financing cost.
</p>

</div>
""", unsafe_allow_html=True)


# ============================================================
# LOAN OFFER COUNT
# ============================================================

lender_count = st.selectbox(
    "🏦 How many loan offers do you want to compare?",
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
            "🏦 Lender / Bank Name",
            value=f"Lender {i + 1}",
            key=f"merged_lender_{i}"
        )


    with c2:

        interest_rate = st.number_input(
            "📊 Interest Rate (%)",
            min_value=0.0,
            max_value=30.0,
            value=8.5,
            step=0.05,
            key=f"merged_interest_{i}"
        )


    with c3:

        tenure = st.number_input(
            "📅 Loan Tenure (Years)",
            min_value=1,
            max_value=40,
            value=20,
            key=f"merged_tenure_{i}"
        )


    c4, c5, c6 = st.columns(3)


    with c4:

        processing_fee = st.number_input(
            "💳 Processing Fee (₹)",
            min_value=0,
            value=10000,
            step=1000,
            key=f"merged_processing_{i}"
        )


    with c5:

        other_charges = st.number_input(
            "📄 Other Charges (₹)",
            min_value=0,
            value=5000,
            step=1000,
            key=f"merged_other_{i}"
        )


    with c6:

        floating_rate = st.checkbox(
            "📈 Floating Interest Rate",
            value=True,
            key=f"merged_floating_{i}"
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
        years * 12
    )


    monthly_rate = (
        annual_rate
        /
        12
        /
        100
    )


    if principal <= 0:

        return (
            0,
            0,
            0
        )


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
            **
            months

            /

            (

                (
                    1
                    +
                    monthly_rate
                )
                **
                months

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
# CALCULATE LOAN COMPARISON
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
# BEST LOAN RECOMMENDATION
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
    <b>
    ₹{total_monthly_obligation:,.0f}
    </b>
    </p>

    <p>
    EMI-to-Income Ratio:
    <b>
    {emi_ratio:.1f}%
    </b>
    </p>

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
# MONTHLY CASH FLOW
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

    best_emi

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
# NEXT ACTION
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

        "❤️ Add to Investment Watchlist",

        "🏦 Start Loan Application",

        "📞 Request Loan Consultation",

        "📊 Compare With Another Property",

        "💰 Increase Down Payment",

        "📈 Recalculate With Different Tenure",

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
        f"✅ Selected next step: {next_step}"
    )


# ============================================================
# FUTURE SMART FEATURES
# ============================================================

st.markdown("""
<div class="ai-card">

<h2>
🚀 Future Smart Investment & Finance Features
</h2>

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

🤖 AI Eligibility Prediction
&nbsp; • &nbsp;

📊 Credit Score Integration
&nbsp; • &nbsp;

💳 Pre-Approval Tracking
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
All calculations shown on this page are estimates based on
user-entered assumptions.
</p>

<p>
Actual property returns, rental income, appreciation,
loan approval, interest rates, taxes, processing fees
and repayment terms may differ.
</p>

<p>
This tool is for informational purposes only and does not
constitute financial or investment advice.
</p>

</div>
""", unsafe_allow_html=True)
