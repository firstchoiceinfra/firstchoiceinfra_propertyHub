```python
import streamlit as st
import pandas as pd

# ============================================================
# PAGE 28 — SMART PROPERTY INVESTMENT, ROI & FINANCE CENTER
# FIRSTCHOICE INFRA PROPERTY HUB
#
# FEATURES:
# ✅ Property Investment Planner
# ✅ Purchase & Acquisition Cost
# ✅ Down Payment
# ✅ Loan Requirement
# ✅ Rental Income
# ✅ Vacancy
# ✅ Rent Growth
# ✅ Property Expenses
# ✅ Appreciation Forecast
# ✅ ROI Summary
# ✅ Gross Rental Yield
# ✅ Net Rental Yield
# ✅ Current Capital Gain
# ✅ Future Property Value
# ✅ Future Capital Gain
# ✅ Monthly Cash Flow
# ✅ Multiple Lender Comparison
# ✅ EMI Calculator
# ✅ Fixed / Floating Rate
# ✅ Processing Fee
# ✅ Other Charges
# ✅ Total Interest
# ✅ Total Loan Cost
# ✅ Best Loan Recommendation
# ✅ EMI Affordability
# ✅ Existing EMI
# ✅ Investment Intelligence
# ✅ Navigation / Next Actions
#
# 🔥 UPGRADE:
# Loan Tenure Maximum = 30 Years
# ============================================================


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Smart Property Investment & Finance Center | FirstChoice Property Hub",
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

    margin-bottom: 25px;
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

    margin-bottom: 25px;
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

    margin-bottom: 25px;
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

    margin-top: 30px;
}

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

    margin-bottom: 20px;
}

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

    margin-bottom: 25px;
}

.result-card h1 {
    font-size: 46px;
    font-weight: 900;
}

.stTabs [data-baseweb="tab-list"] {
    gap: 10px;
}

.stTabs [data-baseweb="tab"] {
    padding: 15px 25px;
    border-radius: 15px;
    font-weight: 800;
}

.stButton > button {
    border-radius: 14px;
    font-weight: 800;
    padding: 12px;
}

@media (max-width: 768px) {

    .hero {
        padding: 30px;
    }

    .hero h1 {
        font-size: 32px;
    }

    .section {
        padding: 22px;
    }

}

</style>
""", unsafe_allow_html=True)


# ============================================================
# HERO
# ============================================================

st.markdown("""
<div class="hero">

<h1>
📈 Smart Property Investment, ROI & Finance Center
</h1>

<p>
Analyze property investment potential, calculate ROI,
estimate rental income, forecast appreciation, analyze
cash flow and compare multiple property loan offers
from different lenders in one intelligent platform.
</p>

<p>
🏠 Property Investment
&nbsp; • &nbsp;
📊 ROI
&nbsp; • &nbsp;
🏡 Rental Yield
&nbsp; • &nbsp;
📈 Appreciation
&nbsp; • &nbsp;
💸 Cash Flow
&nbsp; • &nbsp;
🏦 Loan EMI
&nbsp; • &nbsp;
💳 Lender Comparison
</p>

</div>
""", unsafe_allow_html=True)


# ============================================================
# SMART INTRO
# ============================================================

st.markdown("""
<div class="ai-card">

<h2>
🤖 Smart Property Investment & Finance Intelligence
</h2>

<p>
This unified investment center combines property ROI analysis
and property finance planning into one complete financial
decision-making workspace.
</p>

<p>
Evaluate rental income, vacancy, expenses, appreciation,
capital gain, rental yield, ROI, financing cost, EMI
affordability and multiple loan offers before making
an investment decision.
</p>

</div>
""", unsafe_allow_html=True)


# ============================================================
# MAIN TABS
# ============================================================

tab1, tab2, tab3, tab4 = st.tabs([
    "🏡 Investment Planner",
    "📊 ROI & Rental Yield",
    "🏦 Loan & EMI Center",
    "🤖 Investment Intelligence"
])


# ################################################################
# TAB 1 — PROPERTY INVESTMENT PLANNER
# ################################################################

with tab1:

    st.markdown("""
    <div class="section">

    <h2>
    🏡 Property & Investment Details
    </h2>

    <p>
    Enter the basic property information and investment assumptions.
    </p>

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
            "📍 Location",
            placeholder="Example: Nagpur, Maharashtra"
        )


    with c3:

        purchase_price = st.number_input(
            "🏷️ Property Purchase Price (₹)",
            min_value=100000,
            value=5000000,
            step=100000
        )


    # ========================================================
    # CURRENT VALUE
    # ========================================================

    st.markdown("""
    <div class="section">

    <h2>
    🏷️ Current / Expected Property Value
    </h2>

    <p>
    Used to calculate present estimated capital gain.
    </p>

    </div>
    """, unsafe_allow_html=True)


    current_value = st.number_input(
        "🏷️ Current / Expected Property Value (₹)",
        min_value=100000,
        value=6000000,
        step=100000
    )


    # ========================================================
    # PURCHASE COST
    # ========================================================

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


    # ========================================================
    # RENTAL INCOME
    # ========================================================

    st.markdown("""
    <div class="section">

    <h2>
    🏠 Rental Income & Vacancy
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
            min_value=0,
            max_value=50,
            value=5
        )


    with r3:

        rent_growth = st.number_input(
            "📈 Annual Rent Growth (%)",
            min_value=0.0,
            max_value=30.0,
            value=5.0,
            step=0.5
        )


    # ========================================================
    # PROPERTY EXPENSES
    # ========================================================

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
            "🔧 Maintenance (₹ / Year)",
            min_value=0,
            value=30000,
            step=5000
        )


    with e2:

        property_tax = st.number_input(
            "🏛️ Property Tax (₹ / Year)",
            min_value=0,
            value=15000,
            step=5000
        )


    with e3:

        insurance = st.number_input(
            "🛡️ Insurance (₹ / Year)",
            min_value=0,
            value=10000,
            step=5000
        )


    # ========================================================
    # APPRECIATION
    # ========================================================

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
            "📅 Investment Holding Period (Years)",
            min_value=1,
            max_value=50,
            value=10
        )


    # ========================================================
    # CALCULATIONS
    # ========================================================

    total_acquisition_cost = (
        purchase_price
        +
        registration_cost
        +
        renovation_cost
    )


    required_loan = max(
        purchase_price - down_payment,
        0
    )


    annual_gross_rent = (
        monthly_rent * 12
    )


    effective_rent = (
        annual_gross_rent
        *
        (1 - vacancy_rate / 100)
    )


    total_expenses = (
        maintenance
        +
        property_tax
        +
        insurance
    )


    annual_net_rental_income = (
        effective_rent
        -
        total_expenses
    )


    gross_rental_yield = (

        annual_gross_rent
        /
        purchase_price
        *
        100

    ) if purchase_price > 0 else 0


    net_rental_yield = (

        annual_net_rental_income
        /
        purchase_price
        *
        100

    ) if purchase_price > 0 else 0


    current_capital_gain = (
        current_value
        -
        purchase_price
    )


    current_capital_gain_percentage = (

        current_capital_gain
        /
        purchase_price
        *
        100

    ) if purchase_price > 0 else 0


    future_property_value = (

        purchase_price
        *
        (
            1
            +
            appreciation_rate / 100
        )
        **
        investment_years

    )


    future_capital_gain = (

        future_property_value
        -
        purchase_price

    )


    # ========================================================
    # RENT GROWTH PROJECTION
    # ========================================================

    total_projected_rental_income = 0

    projected_annual_rent = effective_rent


    for year in range(
        1,
        int(investment_years) + 1
    ):

        total_projected_rental_income += (
            projected_annual_rent
        )

        projected_annual_rent *= (
            1
            +
            rent_growth / 100
        )


    estimated_total_return = (

        total_projected_rental_income
        +
        future_capital_gain

    )


    estimated_roi = (

        estimated_total_return
        /
        total_acquisition_cost
        *
        100

    ) if total_acquisition_cost > 0 else 0


    # ========================================================
    # INVESTMENT SUMMARY
    # ========================================================

    st.markdown("""
    <div class="section">

    <h2>
    📊 Investment Performance Summary
    </h2>

    </div>
    """, unsafe_allow_html=True)


    m1, m2, m3 = st.columns(3)


    with m1:

        st.metric(
            "💰 Total Acquisition Cost",
            f"₹{total_acquisition_cost:,.0f}"
        )


    with m2:

        st.metric(
            "🏦 Required Loan",
            f"₹{required_loan:,.0f}"
        )


    with m3:

        st.metric(
            "💵 Annual Net Rental Income",
            f"₹{annual_net_rental_income:,.0f}"
        )


    m4, m5, m6 = st.columns(3)


    with m4:

        st.metric(
            "📈 Current Capital Gain",
            f"₹{current_capital_gain:,.0f}"
        )


    with m5:

        st.metric(
            "🔮 Future Property Value",
            f"₹{future_property_value:,.0f}"
        )


    with m6:

        st.metric(
            "📊 Estimated ROI",
            f"{estimated_roi:.2f}%"
        )


    st.markdown(
        f"""
        <div class="result-card">

        <p>
        Estimated Total Investment ROI
        </p>

        <h1>
        {estimated_roi:.2f}%
        </h1>

        <p>
        Based on estimated rental income,
        rental growth and property appreciation
        over <b>{investment_years} years</b>.
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )


# ################################################################
# TAB 2 — ROI & RENTAL YIELD
# ################################################################

with tab2:

    st.markdown("""
    <div class="section">

    <h2>
    🏠 Rental Yield Analysis
    </h2>

    <p>
    Compare gross and net rental returns generated by the property.
    </p>

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

            <h1>
            {gross_rental_yield:.2f}%
            </h1>

            <p>
            Calculated using annual gross rent
            before vacancy and property expenses.
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

            <h1>
            {net_rental_yield:.2f}%
            </h1>

            <p>
            Calculated after vacancy adjustment
            and annual property expenses.
            </p>

            </div>
            """,
            unsafe_allow_html=True
        )


    st.markdown("""
    <div class="section">

    <h2>
    📈 Capital Appreciation Analysis
    </h2>

    </div>
    """, unsafe_allow_html=True)


    c1, c2, c3 = st.columns(3)


    with c1:

        st.metric(
            "🏷️ Purchase Price",
            f"₹{purchase_price:,.0f}"
        )


    with c2:

        st.metric(
            "📍 Current / Expected Value",
            f"₹{current_value:,.0f}"
        )


    with c3:

        st.metric(
            "📈 Current Capital Gain",
            f"₹{current_capital_gain:,.0f}"
        )


    st.progress(
        min(
            max(
                current_capital_gain_percentage / 100,
                0
            ),
            1
        )
    )


    st.caption(
        f"Current estimated capital appreciation: "
        f"{current_capital_gain_percentage:.2f}%"
    )


    st.markdown("""
    <div class="section">

    <h2>
    🔮 Future Property Value Projection
    </h2>

    </div>
    """, unsafe_allow_html=True)


    f1, f2 = st.columns(2)


    with f1:

        st.markdown(
            f"""
            <div class="info-card">

            <h3>
            🏡 Estimated Future Property Value
            </h3>

            <h2>
            ₹{future_property_value:,.0f}
            </h2>

            <p>
            After {investment_years} years at
            {appreciation_rate:.1f}% annual appreciation.
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
            📈 Future Capital Gain
            </h3>

            <h2>
            ₹{future_capital_gain:,.0f}
            </h2>

            <p>
            Estimated increase over the original
            property purchase price.
            </p>

            </div>
            """,
            unsafe_allow_html=True
        )


    if net_rental_yield >= 5:

        score = "Excellent"

        score_message = (
            "Strong rental income potential under the entered assumptions."
        )


    elif net_rental_yield >= 3:

        score = "Good"

        score_message = (
            "Reasonable rental income potential."
        )


    elif net_rental_yield >= 2:

        score = "Moderate"

        score_message = (
            "Moderate rental income potential."
        )


    else:

        score = "Low"

        score_message = (
            "Rental yield is relatively low; "
            "capital appreciation may be the main investment driver."
        )


    st.markdown("""
    <div class="section">

    <h2>
    🎯 Investment Rental Score
    </h2>

    </div>
    """, unsafe_allow_html=True)


    st.success(
        f"⭐ Investment Rental Score: {score}"
    )


    st.info(
        score_message
    )


    st.markdown("""
    <div class="section">

    <h2>
    🧮 ROI Component Breakdown
    </h2>

    </div>
    """, unsafe_allow_html=True)


    b1, b2, b3 = st.columns(3)


    with b1:

        st.metric(
            "🏠 Projected Rental Income",
            f"₹{total_projected_rental_income:,.0f}"
        )


    with b2:

        st.metric(
            "📈 Future Capital Gain",
            f"₹{future_capital_gain:,.0f}"
        )


    with b3:

        st.metric(
            "💰 Estimated Total Return",
            f"₹{estimated_total_return:,.0f}"
        )


    st.warning(
        "⚠️ The ROI calculation is an estimate based on "
        "user-entered assumptions. It does not include all "
        "possible taxes, transaction costs, financing costs, "
        "vacancy changes or market risks."
    )


# ################################################################
# TAB 3 — LOAN & EMI CENTER
# ################################################################

with tab3:

    st.markdown("""
    <div class="section">

    <h2>
    🏦 Smart Loan & EMI Comparison Center
    </h2>

    <p>
    Compare multiple lenders and calculate EMI for loan tenure
    up to 30 years.
    </p>

    </div>
    """, unsafe_allow_html=True)


    st.markdown("""
    <div class="ai-card">

    <h2>
    🤖 Compare Multiple Lenders
    </h2>

    <p>
    Compare monthly EMI, total interest, processing fees,
    other charges and estimated total financing cost.
    </p>

    <p>
    🔥 Loan tenure supported from 1 year up to 30 years.
    </p>

    </div>
    """, unsafe_allow_html=True)


    lender_count = st.selectbox(
        "🏦 How many loan offers do you want to compare?",
        [2, 3, 4, 5]
    )


    loans = []


    # ========================================================
    # LOAN CALCULATOR FUNCTION
    # ========================================================

    def calculate_loan(
        principal,
        annual_rate,
        years
    ):

        months = int(
            years * 12
        )


        if principal <= 0:

            return (
                0,
                0,
                0
            )


        monthly_rate = (

            annual_rate
            /
            12
            /
            100

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


    # ========================================================
    # LOAN INPUTS
    # ========================================================

    for i in range(
        lender_count
    ):

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
                key=f"page28_lender_{i}"
            )


        with c2:

            interest_rate = st.number_input(
                "📊 Interest Rate (%)",
                min_value=0.0,
                max_value=30.0,
                value=8.5,
                step=0.05,
                key=f"page28_interest_{i}"
            )


        with c3:

            # =================================================
            # 🔥 UPGRADED:
            # MAXIMUM TENURE NOW 30 YEARS
            # =================================================

            tenure = st.number_input(
                "📅 Loan Tenure (Years) — Max 30 Years",
                min_value=1,
                max_value=30,
                value=20,
                step=1,
                key=f"page28_tenure_{i}"
            )


        c4, c5, c6 = st.columns(3)


        with c4:

            processing_fee = st.number_input(
                "💳 Processing Fee (₹)",
                min_value=0,
                value=10000,
                step=1000,
                key=f"page28_processing_{i}"
            )


        with c5:

            other_charges = st.number_input(
                "📄 Other Charges (₹)",
                min_value=0,
                value=5000,
                step=1000,
                key=f"page28_other_{i}"
            )


        with c6:

            floating_rate = st.checkbox(
                "📈 Floating Interest Rate",
                value=True,
                key=f"page28_floating_{i}"
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


    # ========================================================
    # LOAN RESULTS
    # ========================================================

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

            "Rate Type":
            "Floating"
            if loan["floating"]
            else "Fixed",

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
            f"₹{total_cost:,.0f}"

        })


    st.markdown("""
    <div class="section">

    <h2>
    📊 Loan Offer Comparison
    </h2>

    </div>
    """, unsafe_allow_html=True)


    st.dataframe(
        pd.DataFrame(results),
        use_container_width=True,
        hide_index=True
    )


    # ========================================================
    # BEST LOAN
    # ========================================================

    best_index = min(

        range(
            len(loans)
        ),

        key=lambda i:

        (
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
        <b>
        {best_loan['interest']:.2f}%
        </b>
        </p>

        <p>
        📌 Rate Type:
        <b>
        {"Floating" if best_loan["floating"] else "Fixed"}
        </b>
        </p>

        <p>
        📅 Tenure:
        <b>
        {best_loan['tenure']} Years
        </b>
        </p>

        <p>
        💳 Monthly EMI:
        <b>
        ₹{best_emi:,.0f}
        </b>
        </p>

        <p>
        💸 Total Interest:
        <b>
        ₹{best_interest:,.0f}
        </b>
        </p>

        <p>
        💰 Estimated Total Loan Cost:
        <b>
        ₹{best_total_cost:,.0f}
        </b>
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )


    # ========================================================
    # EMI AFFORDABILITY
    # ========================================================

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
        step=5000,
        key="page28_monthly_income"
    )


    existing_emi = st.number_input(
        "🏦 Existing Monthly EMI Obligations (₹)",
        min_value=0,
        value=0,
        step=1000,
        key="page28_existing_emi"
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


    # ========================================================
    # MONTHLY CASH FLOW
    # ========================================================

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


    monthly_effective_rent = (

        effective_rent
        /
        12

    )


    monthly_cash_flow = (

        monthly_effective_rent
        -
        monthly_expenses
        -
        best_emi

    )


    if monthly_cash_flow >= 0:

        cash_message = (
            "🟢 Positive Estimated Monthly Cash Flow"
        )

    else:

        cash_message = (
            "🟠 Negative Estimated Monthly Cash Flow"
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

        <p>
        Based on effective monthly rent,
        property expenses and selected best loan EMI.
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )


# ################################################################
# TAB 4 — INVESTMENT INTELLIGENCE
# ################################################################

with tab4:

    if estimated_roi >= 100:

        insight = """
        The estimated long-term return appears strong under the
        assumptions entered. Validate appreciation, rental demand,
        financing costs, taxes and transaction costs before investing.
        """


    elif estimated_roi >= 50:

        insight = """
        The property shows a moderate estimated return.
        Compare it with alternative properties and investment
        opportunities before making a final decision.
        """


    else:

        insight = """
        The estimated return is relatively low under the current
        assumptions. Review the purchase price, rental potential,
        vacancy, expenses and expected appreciation.
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


    st.markdown("""
    <div class="section">

    <h2>
    🎯 Investment Decision Snapshot
    </h2>

    </div>
    """, unsafe_allow_html=True)


    s1, s2, s3, s4 = st.columns(4)


    with s1:

        st.metric(
            "📊 ROI",
            f"{estimated_roi:.2f}%"
        )


    with s2:

        st.metric(
            "🏠 Net Rental Yield",
            f"{net_rental_yield:.2f}%"
        )


    with s3:

        st.metric(
            "📈 Appreciation",
            f"{appreciation_rate:.1f}%"
        )


    with s4:

        st.metric(
            "💰 Future Value",
            f"₹{future_property_value:,.0f}"
        )


    st.markdown("""
    <div class="section">

    <h2>
    🎯 Continue Your Investment Journey
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

        ],

        key="page28_next_step"

    )


    if st.button(
        "🚀 CONTINUE INVESTMENT JOURNEY",
        use_container_width=True
    ):

        st.success(
            f"✅ Selected next step: {next_step}"
        )


    st.markdown("""
    <div class="ai-card">

    <h2>
    🚀 Smart Investment & Finance Features
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
    loan approval, interest rates, taxes, processing fees,
    vacancy, maintenance and repayment terms may differ.
    </p>

    <p>
    This tool is for informational and planning purposes only
    and does not constitute financial or investment advice.
    </p>

    </div>
    """, unsafe_allow_html=True)
```
