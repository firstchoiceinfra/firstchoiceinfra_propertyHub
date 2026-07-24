import streamlit as st
import pandas as pd

from navigation import (
    render_sidebar,
    render_bottom_navigation
)


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(

    page_title=
    "Investment & Finance Center",

    page_icon="📈",

    layout="wide"

)


# ============================================================
# SIDEBAR
# ============================================================

render_sidebar()


# ============================================================
# CSS
# ============================================================

st.markdown(
"""
<style>

.stApp {

    background:
    linear-gradient(
        135deg,
        #F5F7FF,
        #FFF7ED,
        #FDF4FF,
        #ECFEFF
    );

}


.hero {

    padding:45px;

    border-radius:35px;

    color:white;

    background:
    linear-gradient(
        135deg,
        #020617,
        #1D4ED8,
        #7C3AED,
        #DB2777
    );

}


.section {

    margin-top:30px;

    padding:28px;

    border-radius:25px;

    color:white;

    background:
    linear-gradient(
        135deg,
        #1E3A8A,
        #4F46E5,
        #9333EA,
        #EC4899
    );

}


.card {

    padding:25px;

    border-radius:25px;

    background:white;

    box-shadow:
    0 10px 30px
    rgba(0,0,0,0.07);

}


.best {

    padding:30px;

    border-radius:30px;

    color:white;

    background:
    linear-gradient(
        135deg,
        #047857,
        #059669,
        #10B981
    );

}

</style>
""",
unsafe_allow_html=True
)


# ============================================================
# HERO
# ============================================================

st.markdown(
"""
<div class="hero">

<h1>
📈 Smart Property Investment,
ROI & Finance Center
</h1>

<p>
Analyze property ROI, rental yield,
capital appreciation, cash flow
and compare multiple lenders.
</p>

</div>
""",
unsafe_allow_html=True
)


# ============================================================
# TABS
# ============================================================

tab1, tab2, tab3, tab4 = st.tabs(

    [
        "🏡 Investment Planner",
        "📊 ROI & Rental Yield",
        "🏦 Loan & EMI Center",
        "🤖 Investment Intelligence"
    ]

)


# ============================================================
# TAB 1
# ============================================================

with tab1:

    st.markdown(
        """
        <div class="section">

        <h2>
        🏡 Property & Investment Details
        </h2>

        </div>
        """,
        unsafe_allow_html=True
    )


    c1, c2, c3 = st.columns(3)


    with c1:

        property_name = st.text_input(

            "🏠 Property Name",

            "Investment Property"

        )


    with c2:

        location = st.text_input(

            "📍 Location",

            "Nagpur, Maharashtra"

        )


    with c3:

        purchase_price = st.number_input(

            "🏷️ Purchase Price (₹)",

            min_value=100000,

            value=5000000,

            step=100000

        )


    current_value = st.number_input(

        "🏷️ Current / Expected Value (₹)",

        min_value=100000,

        value=6000000,

        step=100000

    )


    p1, p2, p3 = st.columns(3)


    with p1:

        registration_cost = st.number_input(

            "📄 Registration & Stamp Duty",

            min_value=0,

            value=300000

        )


    with p2:

        renovation_cost = st.number_input(

            "🔨 Renovation Cost",

            min_value=0,

            value=100000

        )


    with p3:

        down_payment = st.number_input(

            "💰 Down Payment",

            min_value=0,

            value=1500000

        )


    r1, r2, r3 = st.columns(3)


    with r1:

        monthly_rent = st.number_input(

            "💵 Monthly Rent",

            min_value=0,

            value=25000

        )


    with r2:

        vacancy_rate = st.slider(

            "📅 Vacancy (%)",

            0,

            50,

            5

        )


    with r3:

        rent_growth = st.number_input(

            "📈 Annual Rent Growth (%)",

            0.0,

            30.0,

            5.0

        )


    e1, e2, e3 = st.columns(3)


    with e1:

        maintenance = st.number_input(

            "🔧 Maintenance / Year",

            0,

            1000000,

            30000

        )


    with e2:

        property_tax = st.number_input(

            "🏛️ Property Tax / Year",

            0,

            1000000,

            15000

        )


    with e3:

        insurance = st.number_input(

            "🛡️ Insurance / Year",

            0,

            1000000,

            10000

        )


    a1, a2 = st.columns(2)


    with a1:

        appreciation_rate = st.number_input(

            "📈 Annual Appreciation (%)",

            -20.0,

            50.0,

            7.0

        )


    with a2:

        investment_years = st.number_input(

            "📅 Holding Period",

            1,

            50,

            10

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

        purchase_price
        -
        down_payment,

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


    total_projected_rental_income = 0


    projected_rent = effective_rent


    for year in range(

        1,

        int(
            investment_years
        ) + 1

    ):

        total_projected_rental_income += (

            projected_rent

        )


        projected_rent *= (

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
    # SUMMARY
    # ========================================================

    st.markdown(
        """
        <div class="section">

        <h2>
        📊 Investment Summary
        </h2>

        </div>
        """,
        unsafe_allow_html=True
    )


    m1, m2, m3 = st.columns(3)


    m1.metric(

        "💰 Acquisition Cost",

        f"₹{total_acquisition_cost:,.0f}"

    )


    m2.metric(

        "🏦 Required Loan",

        f"₹{required_loan:,.0f}"

    )


    m3.metric(

        "💵 Net Rental Income",

        f"₹{annual_net_rental_income:,.0f}"

    )


    m4, m5, m6 = st.columns(3)


    m4.metric(

        "📈 Capital Gain",

        f"₹{current_capital_gain:,.0f}"

    )


    m5.metric(

        "🔮 Future Value",

        f"₹{future_property_value:,.0f}"

    )


    m6.metric(

        "📊 Estimated ROI",

        f"{estimated_roi:.2f}%"

    )


# ============================================================
# TAB 2
# ============================================================

with tab2:

    st.markdown(
        """
        <div class="section">

        <h2>
        📊 ROI & Rental Yield Analysis
        </h2>

        </div>
        """,
        unsafe_allow_html=True
    )


    c1, c2 = st.columns(2)


    with c1:

        st.metric(

            "💵 Gross Rental Yield",

            f"{gross_rental_yield:.2f}%"

        )


    with c2:

        st.metric(

            "💰 Net Rental Yield",

            f"{net_rental_yield:.2f}%"

        )


    st.metric(

        "📈 Current Capital Gain",

        f"₹{current_capital_gain:,.0f}"

    )


    st.metric(

        "🔮 Future Property Value",

        f"₹{future_property_value:,.0f}"

    )


    st.metric(

        "💰 Future Capital Gain",

        f"₹{future_capital_gain:,.0f}"

    )


    st.metric(

        "📊 Total Projected Rental Income",

        f"₹{total_projected_rental_income:,.0f}"

    )


# ============================================================
# TAB 3
# LOAN & EMI
# ============================================================

with tab3:

    st.markdown(
        """
        <div class="section">

        <h2>
        🏦 Multiple Lender Comparison
        </h2>

        <p>
        Compare EMI, interest, processing fee and
        total financing cost.
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )


    lender_count = st.selectbox(

        "🏦 Number of Lenders",

        [2, 3, 4, 5]

    )


    def calculate_loan(

        principal,

        annual_rate,

        years

    ):

        months = int(

            years * 12

        )


        if principal <= 0:

            return 0, 0, 0


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


    loans = []


    for i in range(

        lender_count

    ):

        st.markdown(
            f"""
            <div class="card">

            <h3>
            🏦 Loan Offer {i + 1}
            </h3>

            </div>
            """,
            unsafe_allow_html=True
        )


        c1, c2, c3 = st.columns(3)


        with c1:

            lender = st.text_input(

                "Lender / Bank",

                f"Lender {i + 1}",

                key=f"lender_{i}"

            )


        with c2:

            interest = st.number_input(

                "Interest Rate (%)",

                0.0,

                30.0,

                8.5,

                0.05,

                key=f"interest_{i}"

            )


        with c3:

            tenure = st.number_input(

                "Loan Tenure (Years)",

                1,

                30,

                20,

                key=f"tenure_{i}"

            )


        c4, c5, c6 = st.columns(3)


        with c4:

            processing = st.number_input(

                "Processing Fee (₹)",

                0,

                1000000,

                10000,

                key=f"processing_{i}"

            )


        with c5:

            other = st.number_input(

                "Other Charges (₹)",

                0,

                1000000,

                5000,

                key=f"other_{i}"

            )


        with c6:

            floating = st.checkbox(

                "📈 Floating Rate",

                True,

                key=f"floating_{i}"

            )


        loans.append({

            "lender":
            lender,

            "interest":
            interest,

            "tenure":
            tenure,

            "processing":
            processing,

            "other":
            other,

            "floating":
            floating

        })


    results = []


    for loan in loans:

        emi, payment, interest = calculate_loan(

            required_loan,

            loan["interest"],

            loan["tenure"]

        )


        total_cost = (

            payment
            +
            loan["processing"]
            +
            loan["other"]

        )


        results.append({

            "Lender":
            loan["lender"],

            "Rate":
            f"{loan['interest']:.2f}%",

            "Type":
            "Floating"
            if loan["floating"]
            else "Fixed",

            "Tenure":
            f"{loan['tenure']} Years",

            "Monthly EMI":
            f"₹{emi:,.0f}",

            "Total Interest":
            f"₹{interest:,.0f}",

            "Processing Fee":
            f"₹{loan['processing']:,.0f}",

            "Other Charges":
            f"₹{loan['other']:,.0f}",

            "Total Loan Cost":
            f"₹{total_cost:,.0f}"

        })


    st.dataframe(

        pd.DataFrame(

            results

        ),

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


    best = loans[

        best_index

    ]


    best_emi, best_payment, best_interest = calculate_loan(

        required_loan,

        best["interest"],

        best["tenure"]

    )


    best_cost = (

        best_payment
        +
        best["processing"]
        +
        best["other"]

    )


    st.markdown(
        f"""
        <div class="best">

        <h2>
        🏆 Best Estimated Loan
        </h2>

        <h1>
        {best['lender']}
        </h1>

        <p>
        Interest Rate:
        {best['interest']:.2f}%
        </p>

        <p>
        Tenure:
        {best['tenure']} Years
        </p>

        <p>
        Monthly EMI:
        ₹{best_emi:,.0f}
        </p>

        <p>
        Total Interest:
        ₹{best_interest:,.0f}
        </p>

        <p>
        Total Loan Cost:
        ₹{best_cost:,.0f}
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )


    # ========================================================
    # AFFORDABILITY
    # ========================================================

    st.markdown(
        """
        <div class="section">

        <h2>
        💰 EMI Affordability
        </h2>

        </div>
        """,
        unsafe_allow_html=True
    )


    income = st.number_input(

        "Monthly Household Income",

        0,

        10000000,

        100000

    )


    existing_emi = st.number_input(

        "Existing EMI",

        0,

        10000000,

        0

    )


    total_obligation = (

        best_emi
        +
        existing_emi

    )


    emi_ratio = (

        total_obligation
        /
        income
        *
        100

    ) if income > 0 else 0


    st.metric(

        "EMI-to-Income Ratio",

        f"{emi_ratio:.1f}%"

    )


    if emi_ratio <= 40:

        st.success(

            "🟢 EMI burden appears comfortable."

        )


    elif emi_ratio <= 60:

        st.warning(

            "🟠 EMI burden is moderate."

        )


    else:

        st.error(

            "🔴 EMI burden is high."

        )


# ============================================================
# TAB 4
# ============================================================

with tab4:

    if estimated_roi >= 100:

        insight = (

            "Strong estimated long-term return. "
            "Validate market assumptions before investing."

        )

    elif estimated_roi >= 50:

        insight = (

            "Moderate estimated return. "
            "Compare alternative investments."

        )

    else:

        insight = (

            "Estimated return is relatively low. "
            "Review purchase price and rental potential."

        )


    st.markdown(
        f"""
        <div class="card">

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


    c1, c2, c3, c4 = st.columns(4)


    c1.metric(

        "ROI",

        f"{estimated_roi:.2f}%"

    )


    c2.metric(

        "Net Rental Yield",

        f"{net_rental_yield:.2f}%"

    )


    c3.metric(

        "Appreciation",

        f"{appreciation_rate:.1f}%"

    )


    c4.metric(

        "Future Value",

        f"₹{future_property_value:,.0f}"

    )


# ============================================================
# BOTTOM NAVIGATION
# ============================================================

render_bottom_navigation(

    "📈 Investment & Finance"

)


st.warning(

    "⚠️ All calculations are estimates for planning purposes only. "
    "Actual loan terms, property returns, taxes and market conditions may vary."

)
