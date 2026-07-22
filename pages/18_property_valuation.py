import streamlit as st

# ============================================================
# PAGE 18 — AI PROPERTY PRICE ESTIMATOR & VALUATION
# FIRSTCHOICE INFRA PROPERTY HUB
# ============================================================

st.set_page_config(
    page_title="Property Valuation | FirstChoice Property Hub",
    page_icon="💎",
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
    padding: 50px;
    border-radius: 35px;
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
    0 22px 70px
    rgba(37,99,235,0.30);

    margin-bottom: 30px;
}

.hero h1 {
    font-size: 46px;
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

    border-radius: 27px;

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

/* RESULT */

.result-card {
    padding: 40px;
    border-radius: 32px;

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
    rgba(5,150,105,0.28);

    text-align: center;
}

.result-card h1 {
    font-size: 48px;
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

/* AI CARD */

.ai-card {
    padding: 30px;
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

</style>
""", unsafe_allow_html=True)


# ============================================================
# HERO
# ============================================================

st.markdown("""
<div class="hero">

<h1>
💎 AI Property Price Estimator
</h1>

<p>
Discover an estimated property value using location,
property type, area, age, condition and market factors.
</p>

<p>
📍 Location • 📐 Area • 🏡 Property Type • 🏗️ Age • 📊 Market
</p>

</div>
""", unsafe_allow_html=True)


# ============================================================
# AI INTRO
# ============================================================

st.markdown("""
<div class="ai-card">

<h2>
🤖 Smart Property Valuation Engine
</h2>

<p>
Enter the basic details of your property and receive an
illustrative estimated market value range.
</p>

<p>
The current version uses a rule-based estimation model.
In the future, it can be connected to verified market data,
actual transactions and AI valuation models.
</p>

</div>
""", unsafe_allow_html=True)


# ============================================================
# PROPERTY DETAILS
# ============================================================

st.markdown("""
<div class="section">

<h2>
🏡 Property Details
</h2>

<p>
Enter accurate information for a better estimated valuation.
</p>

</div>
""", unsafe_allow_html=True)


c1, c2 = st.columns(2)


with c1:

    location = st.selectbox(
        "📍 Property Location",
        [
            "Civil Lines",
            "Wardha Road",
            "Manish Nagar",
            "Besa",
            "Mihan",
            "Hingna"
        ]
    )


with c2:

    property_type = st.selectbox(
        "🏡 Property Type",
        [
            "Apartment",
            "Villa",
            "Independent House",
            "Residential Plot",
            "Commercial Property"
        ]
    )


c3, c4 = st.columns(2)


with c3:

    area = st.number_input(
        "📐 Property Area (Sq.Ft.)",
        min_value=100,
        value=1000,
        step=50
    )


with c4:

    property_age = st.number_input(
        "🏗️ Property Age (Years)",
        min_value=0,
        max_value=100,
        value=5,
        step=1
    )


# ============================================================
# PROPERTY CONDITION
# ============================================================

condition = st.select_slider(
    "✨ Property Condition",
    options=[
        "Needs Renovation",
        "Average",
        "Good",
        "Premium",
        "Luxury"
    ],
    value="Good"
)


# ============================================================
# AMENITIES
# ============================================================

st.markdown("""
<div class="section">

<h2>
✨ Property Features & Amenities
</h2>

</div>
""", unsafe_allow_html=True)


a1, a2, a3 = st.columns(3)


with a1:

    parking = st.checkbox(
        "🚗 Parking"
    )

    lift = st.checkbox(
        "🛗 Lift"
    )


with a2:

    security = st.checkbox(
        "🛡️ Security"
    )

    garden = st.checkbox(
        "🌳 Garden"
    )


with a3:

    clubhouse = st.checkbox(
        "🏊 Clubhouse"
    )

    prime_location = st.checkbox(
        "📍 Prime Location"
    )


# ============================================================
# LOCATION BASE PRICES
# ============================================================

location_prices = {

    "Civil Lines": 7200,

    "Wardha Road": 5600,

    "Manish Nagar": 6100,

    "Besa": 4800,

    "Mihan": 5200,

    "Hingna": 3900

}


base_price = location_prices[
    location
]


# ============================================================
# PROPERTY TYPE MULTIPLIER
# ============================================================

type_multiplier = {

    "Apartment": 1.00,

    "Villa": 1.35,

    "Independent House": 1.20,

    "Residential Plot": 0.85,

    "Commercial Property": 1.50

}


base_price *= type_multiplier[
    property_type
]


# ============================================================
# CONDITION MULTIPLIER
# ============================================================

condition_multiplier = {

    "Needs Renovation": 0.80,

    "Average": 0.90,

    "Good": 1.00,

    "Premium": 1.15,

    "Luxury": 1.30

}


base_price *= condition_multiplier[
    condition
]


# ============================================================
# PROPERTY AGE ADJUSTMENT
# ============================================================

if property_age <= 5:

    age_factor = 1.00

elif property_age <= 10:

    age_factor = 0.95

elif property_age <= 20:

    age_factor = 0.88

else:

    age_factor = 0.78


base_price *= age_factor


# ============================================================
# AMENITY PREMIUM
# ============================================================

amenity_bonus = 0


if parking:

    amenity_bonus += 0.03


if lift:

    amenity_bonus += 0.02


if security:

    amenity_bonus += 0.02


if garden:

    amenity_bonus += 0.02


if clubhouse:

    amenity_bonus += 0.04


if prime_location:

    amenity_bonus += 0.06


base_price *= (
    1 + amenity_bonus
)


# ============================================================
# ESTIMATED VALUE
# ============================================================

estimated_value = (
    area
    *
    base_price
)


low_value = (
    estimated_value
    *
    0.90
)


high_value = (
    estimated_value
    *
    1.10
)


# ============================================================
# VALUATION RESULT
# ============================================================

if st.button(
    "🚀 ESTIMATE PROPERTY VALUE",
    use_container_width=True
):

    st.session_state.valuation_done = True


if st.session_state.get(
    "valuation_done",
    False
):

    st.markdown("""
    <div class="section">

    <h2>
    💎 Estimated Property Valuation
    </h2>

    </div>
    """, unsafe_allow_html=True)


    st.markdown(
        f"""
        <div class="result-card">

        <p>
        Estimated Market Value
        </p>

        <h1>
        ₹{estimated_value:,.0f}
        </h1>

        <p>
        Estimated Value Range
        </p>

        <h2>
        ₹{low_value:,.0f}
        — 
        ₹{high_value:,.0f}
        </h2>

        </div>
        """,
        unsafe_allow_html=True
    )


    st.write("")


    v1, v2, v3 = st.columns(3)


    with v1:

        st.markdown(
            f"""
            <div class="value-card">

            <h3>
            📐 Area
            </h3>

            <h2>
            {area:,.0f} Sq.Ft.
            </h2>

            </div>
            """,
            unsafe_allow_html=True
        )


    with v2:

        st.markdown(
            f"""
            <div class="value-card">

            <h3>
            💰 Estimated Rate
            </h3>

            <h2>
            ₹{base_price:,.0f}
            </h2>

            <p>
            Approximate rate per Sq.Ft.
            </p>

            </div>
            """,
            unsafe_allow_html=True
        )


    with v3:

        st.markdown(
            f"""
            <div class="value-card">

            <h3>
            📍 Location
            </h3>

            <h2>
            {location}
            </h2>

            </div>
            """,
            unsafe_allow_html=True
        )


# ============================================================
# VALUATION BREAKDOWN
# ============================================================

if st.session_state.get(
    "valuation_done",
    False
):

    st.markdown("""
    <div class="section">

    <h2>
    🔍 Valuation Factors
    </h2>

    </div>
    """, unsafe_allow_html=True)


    factors = {

        "📍 Location": 30,

        "📐 Property Area": 20,

        "🏡 Property Type": 15,

        "✨ Property Condition": 15,

        "🏗️ Property Age": 10,

        "🚗 Amenities": 10

    }


    for factor, percentage in factors.items():

        st.write(
            f"**{factor} — {percentage}% influence**"
        )

        st.progress(
            percentage / 100
        )


# ============================================================
# SELLER SECTION
# ============================================================

st.markdown("""
<div class="section">

<h2>
🏷️ Planning To Sell Your Property?
</h2>

<p>
Use the estimated valuation as a starting point and compare
your property with similar listings.
</p>

</div>
""", unsafe_allow_html=True)


s1, s2, s3 = st.columns(3)


with s1:

    st.markdown("""
    <div class="value-card">

    <h3>
    📊 Compare Market
    </h3>

    <p>
    Compare similar properties in your area.
    </p>

    </div>
    """, unsafe_allow_html=True)


with s2:

    st.markdown("""
    <div class="value-card">

    <h3>
    📸 List Property
    </h3>

    <p>
    Create a premium property listing
    with photos and videos.
    </p>

    </div>
    """, unsafe_allow_html=True)


with s3:

    st.markdown("""
    <div class="value-card">

    <h3>
    🤝 Find Buyers
    </h3>

    <p>
    Connect your property with interested
    buyers and investors.
    </p>

    </div>
    """, unsafe_allow_html=True)


# ============================================================
# FUTURE AI
# ============================================================

st.markdown("""
<div class="ai-card">

<h2>
🚀 Future AI Valuation Engine
</h2>

<p>
The next-generation version can analyse:
</p>

<p>
📍 Location Intelligence
&nbsp; • &nbsp;
🏗️ Construction Quality
&nbsp; • &nbsp;
📊 Recent Transactions
&nbsp; • &nbsp;
🏡 Comparable Properties
&nbsp; • &nbsp;
🚇 Infrastructure
&nbsp; • &nbsp;
📈 Market Trends
</p>

<p>
The system can generate an explainable valuation report
and help users understand why a property may be priced
above or below the surrounding market.
</p>

</div>
""", unsafe_allow_html=True)


# ============================================================
# DISCLAIMER
# ============================================================

st.warning(
    "⚠️ This valuation is an illustrative estimate based on "
    "user-provided information and sample pricing assumptions. "
    "It is not a certified property valuation, appraisal or "
    "investment recommendation. Actual market value may differ."
)
