import streamlit as st
import pandas as pd

# ============================================================
# PAGE 16 — PROPERTY PRICE INTELLIGENCE & MARKET INSIGHTS
# FIRSTCHOICE INFRA PROPERTY HUB
# ============================================================

st.set_page_config(
    page_title="Market Insights | FirstChoice Property Hub",
    page_icon="📊",
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
    padding: 48px;
    border-radius: 34px;
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
    rgba(37,99,235,0.28);

    margin-bottom: 30px;
}

.hero h1 {
    font-size: 44px;
    font-weight: 900;
}

.hero p {
    font-size: 18px;
    line-height: 1.7;
}

/* SECTION */

.section {
    margin-top: 30px;
    margin-bottom: 20px;

    padding: 28px 32px;

    border-radius: 26px;

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
    rgba(79,70,229,0.20);
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

/* INSIGHT */

.insight-card {
    padding: 28px;
    border-radius: 25px;

    background:
    linear-gradient(
        135deg,
        #FFFFFF,
        #F5F3FF,
        #EFF6FF
    );

    border: 1px solid #E0E7FF;

    box-shadow:
    0 10px 30px
    rgba(0,0,0,0.06);

    min-height: 190px;
}

/* SUCCESS */

.success-card {
    padding: 30px;
    border-radius: 28px;

    color: white;

    background:
    linear-gradient(
        135deg,
        #047857,
        #059669,
        #10B981
    );

    box-shadow:
    0 18px 50px
    rgba(5,150,105,0.25);
}

/* ALERT */

.alert-card {
    padding: 28px;
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
📊 Property Price Intelligence
</h1>

<p>
Understand property prices, compare locations and explore
real-estate market trends before making your next move.
</p>

<p>
📍 Location • 💰 Price • 📈 Trends • 🏡 Demand • 🧠 Intelligence
</p>

</div>
""", unsafe_allow_html=True)


# ============================================================
# MARKET OVERVIEW
# ============================================================

st.markdown("""
<div class="section">

<h2>
🌐 Real Estate Market Overview
</h2>

<p>
Explore an illustrative market dashboard. In the future,
this section can connect with verified live market datasets.
</p>

</div>
""", unsafe_allow_html=True)


# Demo data — later replace with database/API data

market_data = pd.DataFrame({

    "Location": [
        "Civil Lines",
        "Wardha Road",
        "Manish Nagar",
        "Besa",
        "Mihan",
        "Hingna"
    ],

    "Average Price": [
        7200,
        5600,
        6100,
        4800,
        5200,
        3900
    ],

    "Annual Growth": [
        7.8,
        9.2,
        6.5,
        10.4,
        11.2,
        5.8
    ],

    "Demand Score": [
        82,
        91,
        78,
        88,
        94,
        67
    ]

})


# ============================================================
# LOCATION SELECTOR
# ============================================================

location = st.selectbox(
    "📍 Select Location",
    market_data["Location"]
)


selected = market_data[
    market_data["Location"]
    ==
    location
].iloc[0]


price_per_sqft = selected[
    "Average Price"
]


growth = selected[
    "Annual Growth"
]


demand = selected[
    "Demand Score"
]


# ============================================================
# LOCATION INSIGHTS
# ============================================================

st.markdown("""
<div class="section">

<h2>
📍 Location Intelligence
</h2>

</div>
""", unsafe_allow_html=True)


i1, i2, i3 = st.columns(3)


with i1:

    st.markdown(
        f"""
        <div class="insight-card">

        <h3>
        💰 Average Price
        </h3>

        <h2>
        ₹{price_per_sqft:,}/sq.ft.
        </h2>

        <p>
        Illustrative average market price.
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )


with i2:

    st.markdown(
        f"""
        <div class="insight-card">

        <h3>
        📈 Annual Growth
        </h3>

        <h2>
        {growth:.1f}%
        </h2>

        <p>
        Illustrative estimated annual growth.
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )


with i3:

    st.markdown(
        f"""
        <div class="insight-card">

        <h3>
        🔥 Demand Score
        </h3>

        <h2>
        {demand}/100
        </h2>

        <p>
        Illustrative market demand indicator.
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# MARKET DEMAND
# ============================================================

st.markdown("""
<div class="section">

<h2>
🔥 Demand Intelligence
</h2>

</div>
""", unsafe_allow_html=True)


st.progress(
    min(
        demand / 100,
        1.0
    )
)


if demand >= 90:

    st.success(
        "🚀 Very High Demand Area — strong buyer interest."
    )

elif demand >= 80:

    st.info(
        "📈 High Demand Area — healthy market activity."
    )

elif demand >= 70:

    st.warning(
        "📊 Moderate Demand Area — evaluate property carefully."
    )

else:

    st.warning(
        "⚠️ Lower Demand Area — consider long-term factors."
    )


# ============================================================
# PRICE COMPARISON
# ============================================================

st.markdown("""
<div class="section">

<h2>
🏙️ Location Price Comparison
</h2>

<p>
Compare illustrative average prices across selected locations.
</p>

</div>
""", unsafe_allow_html=True)


st.bar_chart(
    market_data.set_index(
        "Location"
    )["Average Price"]
)


# ============================================================
# GROWTH COMPARISON
# ============================================================

st.markdown("""
<div class="section">

<h2>
📈 Market Growth Comparison
</h2>

</div>
""", unsafe_allow_html=True)


st.line_chart(
    market_data.set_index(
        "Location"
    )["Annual Growth"]
)


# ============================================================
# MARKET TABLE
# ============================================================

st.markdown("""
<div class="section">

<h2>
📋 Market Data Table
</h2>

</div>
""", unsafe_allow_html=True)


st.dataframe(
    market_data,
    use_container_width=True,
    hide_index=True
)


# ============================================================
# BUYER INSIGHT
# ============================================================

st.markdown("""
<div class="section">

<h2>
🧠 Smart Buyer Insight
</h2>

</div>
""", unsafe_allow_html=True)


budget = st.number_input(
    "💰 Enter Your Property Budget (₹)",
    min_value=100000,
    value=5000000,
    step=100000
)


expected_area = (
    budget
    /
    price_per_sqft
)


b1, b2 = st.columns(2)


with b1:

    st.markdown(
        f"""
        <div class="insight-card">

        <h3>
        🏡 Estimated Property Area
        </h3>

        <h2>
        {expected_area:,.0f} sq.ft.
        </h2>

        <p>
        Approximate area based on the selected
        illustrative average price.
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )


with b2:

    st.markdown(
        f"""
        <div class="insight-card">

        <h3>
        📍 Selected Market
        </h3>

        <h2>
        {location}
        </h2>

        <p>
        Current selection for your analysis.
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# INVESTOR INSIGHT
# ============================================================

st.markdown("""
<div class="section">

<h2>
💼 Investor Perspective
</h2>

</div>
""", unsafe_allow_html=True)


if growth >= 10 and demand >= 85:

    st.markdown("""
    <div class="success-card">

    <h2>
    🚀 High Growth Opportunity
    </h2>

    <p>
    This illustrative market profile shows both strong growth
    and strong demand. Investors may wish to investigate
    infrastructure, rental demand and future development.
    </p>

    </div>
    """, unsafe_allow_html=True)

elif growth >= 7:

    st.info(
        "📈 Balanced Growth Market — investigate rental yield "
        "and long-term infrastructure development."
    )

else:

    st.warning(
        "⚠️ Lower Growth Profile — compare with alternative "
        "locations before making an investment decision."
    )


# ============================================================
# FUTURE DATA INTELLIGENCE
# ============================================================

st.markdown("""
<div class="section">

<h2>
🤖 Future Property Intelligence Engine
</h2>

<p>
The long-term vision is to build a real-time property intelligence
platform using verified datasets and authorised data sources.
</p>

</div>
""", unsafe_allow_html=True)


f1, f2, f3 = st.columns(3)


with f1:

    st.markdown("""
    <div class="insight-card">

    <h3>
    🛰️ Live Market Data
    </h3>

    <p>
    Connect verified data sources to monitor
    real-time property market movements.
    </p>

    </div>
    """, unsafe_allow_html=True)


with f2:

    st.markdown("""
    <div class="insight-card">

    <h3>
    🗺️ Infrastructure Intelligence
    </h3>

    <p>
    Analyse roads, metro, airports, schools,
    hospitals and upcoming development.
    </p>

    </div>
    """, unsafe_allow_html=True)


with f3:

    st.markdown("""
    <div class="insight-card">

    <h3>
    🤖 AI Property Score
    </h3>

    <p>
    Future AI can combine price, demand,
    location and investment indicators.
    </p>

    </div>
    """, unsafe_allow_html=True)


# ============================================================
# DISCLAIMER
# ============================================================

st.markdown("""
<div class="alert-card">

<h2>
⚠️ Important Information
</h2>

<p>
The market numbers displayed on this page are illustrative
demo data for the current frontend version and should not be
treated as live market prices or investment advice.
</p>

<p>
Future versions should use verified, current and legally
permitted data sources before displaying real market intelligence.
</p>

</div>
""", unsafe_allow_html=True)


# ============================================================
# FOOTER
# ============================================================

st.markdown("""
<div class="success-card">

<h2>
🌐 FirstChoice Property Hub
</h2>

<p>
From property discovery to intelligent real-estate decisions.
</p>

</div>
""", unsafe_allow_html=True)
