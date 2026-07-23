import streamlit as st

# ============================================================
# PAGE 27 — SMART PROPERTY COMPARISON & DECISION CENTER
# FIRSTCHOICE INFRA PROPERTY HUB
# ============================================================

st.set_page_config(
    page_title="Property Comparison Center | FirstChoice Property Hub",
    page_icon="⚖️",
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
⚖️ Smart Property Comparison Center
</h1>

<p>
Compare multiple properties side-by-side and make a
better property purchase or investment decision.
</p>

<p>
💰 Price • 📍 Location • 📐 Area • 🏠 Amenities • 📊 Investment • ⭐ Rating
</p>

</div>
""", unsafe_allow_html=True)


# ============================================================
# INTRO
# ============================================================

st.markdown("""
<div class="ai-card">

<h2>
🤖 Smart Property Decision Engine
</h2>

<p>
Instead of opening multiple property listings one by one,
compare your shortlisted properties on one screen.
</p>

<p>
The system can calculate a weighted score based on your
personal priorities and highlight the property that best
matches your requirements.
</p>

</div>
""", unsafe_allow_html=True)


# ============================================================
# NUMBER OF PROPERTIES
# ============================================================

st.markdown("""
<div class="section">

<h2>
🏡 Select Properties for Comparison
</h2>

</div>
""", unsafe_allow_html=True)


property_count = st.selectbox(
    "How many properties do you want to compare?",
    [2, 3, 4, 5]
)


# ============================================================
# PROPERTY INPUTS
# ============================================================

properties = []


for i in range(property_count):

    st.markdown(
        f"""
        <div class="section">

        <h2>
        🏠 Property {i + 1}
        </h2>

        </div>
        """,
        unsafe_allow_html=True
    )

    c1, c2, c3 = st.columns(3)

    with c1:

        name = st.text_input(
            f"Property {i + 1} Name",
            value=f"Property {i + 1}",
            key=f"name_{i}"
        )

    with c2:

        location = st.text_input(
            f"📍 Location",
            key=f"location_{i}"
        )

    with c3:

        price = st.number_input(
            f"💰 Price (₹)",
            min_value=0,
            value=5000000,
            step=100000,
            key=f"price_{i}"
        )

    c4, c5, c6 = st.columns(3)

    with c4:

        area = st.number_input(
            f"📐 Area (Sq.Ft.)",
            min_value=1,
            value=1000,
            key=f"area_{i}"
        )

    with c5:

        bedrooms = st.number_input(
            f"🛏️ Bedrooms",
            min_value=0,
            value=2,
            key=f"bedrooms_{i}"
        )

    with c6:

        bathrooms = st.number_input(
            f"🚿 Bathrooms",
            min_value=0,
            value=2,
            key=f"bathrooms_{i}"
        )

    c7, c8, c9 = st.columns(3)

    with c7:

        site_rating = st.slider(
            f"⭐ Site Visit Rating",
            1.0,
            5.0,
            3.0,
            key=f"site_{i}"
        )

    with c8:

        location_rating = st.slider(
            f"📍 Location Rating",
            1.0,
            5.0,
            3.0,
            key=f"loc_{i}"
        )

    with c9:

        investment_rating = st.slider(
            f"📈 Investment Potential",
            1.0,
            5.0,
            3.0,
            key=f"investment_{i}"
        )

    c10, c11 = st.columns(2)

    with c10:

        legal_status = st.selectbox(
            f"⚖️ Legal Status",
            [
                "Verified",
                "Under Verification",
                "Needs Review",
                "Not Verified"
            ],
            key=f"legal_{i}"
        )

    with c11:

        amenities = st.multiselect(
            f"✨ Amenities",
            [
                "Parking",
                "Lift",
                "Security",
                "Swimming Pool",
                "Gym",
                "Garden",
                "Club House",
                "Power Backup"
            ],
            key=f"amenities_{i}"
        )

    properties.append({

        "name": name,
        "location": location,
        "price": price,
        "area": area,
        "bedrooms": bedrooms,
        "bathrooms": bathrooms,
        "site_rating": site_rating,
        "location_rating": location_rating,
        "investment_rating": investment_rating,
        "legal_status": legal_status,
        "amenities": amenities

    })


# ============================================================
# BUYER PRIORITIES
# ============================================================

st.markdown("""
<div class="section">

<h2>
🎯 Your Property Buying Priorities
</h2>

<p>
Set how important each factor is to you.
</p>

</div>
""", unsafe_allow_html=True)


p1, p2, p3 = st.columns(3)


with p1:

    price_weight = st.slider(
        "💰 Price Importance",
        1,
        10,
        8
    )

with p2:

    location_weight = st.slider(
        "📍 Location Importance",
        1,
        10,
        8
    )

with p3:

    investment_weight = st.slider(
        "📈 Investment Importance",
        1,
        10,
        7
    )


p4, p5, p6 = st.columns(3)


with p4:

    site_weight = st.slider(
        "⭐ Site Visit Importance",
        1,
        10,
        7
    )

with p5:

    legal_weight = st.slider(
        "⚖️ Legal Safety Importance",
        1,
        10,
        10
    )

with p6:

    amenities_weight = st.slider(
        "✨ Amenities Importance",
        1,
        10,
        5
    )


# ============================================================
# CALCULATE SCORES
# ============================================================

max_price = max(
    [p["price"] for p in properties]
)


min_price = min(
    [p["price"] for p in properties]
)


def price_score(price):

    if max_price == min_price:

        return 100

    return (
        (max_price - price)
        /
        (max_price - min_price)
        *
        100
    )


def legal_score(status):

    if status == "Verified":

        return 100

    if status == "Under Verification":

        return 60

    if status == "Needs Review":

        return 35

    return 10


scores = []


for p in properties:

    p_score = price_score(
        p["price"]
    )

    loc_score = (
        p["location_rating"]
        /
        5
        *
        100
    )

    investment_score = (
        p["investment_rating"]
        /
        5
        *
        100
    )

    site_score = (
        p["site_rating"]
        /
        5
        *
        100
    )

    legal_score_value = legal_score(
        p["legal_status"]
    )

    amenities_score = min(
        len(p["amenities"])
        /
        8
        *
        100,
        100
    )

    total_weight = (

        price_weight
        +
        location_weight
        +
        investment_weight
        +
        site_weight
        +
        legal_weight
        +
        amenities_weight

    )

    final_score = (

        p_score * price_weight
        +
        loc_score * location_weight
        +
        investment_score * investment_weight
        +
        site_score * site_weight
        +
        legal_score_value * legal_weight
        +
        amenities_score * amenities_weight

    ) / total_weight

    scores.append({

        "Property":
        p["name"],

        "Price Score":
        round(p_score, 1),

        "Location Score":
        round(loc_score, 1),

        "Investment Score":
        round(investment_score, 1),

        "Site Visit Score":
        round(site_score, 1),

        "Legal Score":
        round(legal_score_value, 1),

        "Amenities Score":
        round(amenities_score, 1),

        "Final Score":
        round(final_score, 1)

    })


# ============================================================
# COMPARISON TABLE
# ============================================================

st.markdown("""
<div class="section">

<h2>
📊 Side-by-Side Property Comparison
</h2>

</div>
""", unsafe_allow_html=True)


comparison_data = []


for p in properties:

    comparison_data.append({

        "Property":
        p["name"],

        "Location":
        p["location"],

        "Price":
        f"₹{p['price']:,.0f}",

        "Area":
        f"{p['area']:,.0f} Sq.Ft.",

        "Bedrooms":
        p["bedrooms"],

        "Bathrooms":
        p["bathrooms"],

        "Site Rating":
        f"{p['site_rating']:.1f}/5",

        "Location Rating":
        f"{p['location_rating']:.1f}/5",

        "Investment":
        f"{p['investment_rating']:.1f}/5",

        "Legal":
        p["legal_status"],

        "Amenities":
        len(p["amenities"])

    })


st.dataframe(
    comparison_data,
    use_container_width=True,
    hide_index=True
)


# ============================================================
# SCORE TABLE
# ============================================================

st.markdown("""
<div class="section">

<h2>
🏆 Smart Decision Scores
</h2>

</div>
""", unsafe_allow_html=True)


st.dataframe(
    scores,
    use_container_width=True,
    hide_index=True
)


# ============================================================
# BEST PROPERTY
# ============================================================

best_index = max(
    range(len(scores)),
    key=lambda i:
    scores[i]["Final Score"]
)


best_property = properties[
    best_index
]


best_score = scores[
    best_index
]["Final Score"]


st.markdown(
    f"""
    <div class="best-card">

    <h2>
    🏆 Smart Recommendation
    </h2>

    <h1>
    {best_property['name']}
    </h1>

    <h2>
    Decision Score: {best_score}/100
    </h2>

    <p>
    📍 {best_property['location']}
    </p>

    <p>
    💰 ₹{best_property['price']:,.0f}
    </p>

    <p>
    📐 {best_property['area']:,.0f} Sq.Ft.
    </p>

    <p>
    ⚖️ Legal Status: {best_property['legal_status']}
    </p>

    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# AI DECISION INSIGHT
# ============================================================

if best_score >= 80:

    insight = """
    This property strongly matches the selected priorities.
    It may be considered the leading option for further
    legal, financial and physical verification.
    """

elif best_score >= 60:

    insight = """
    This property is a reasonably strong match.
    Compare the final deal price and complete all due diligence
    before making a final decision.
    """

else:

    insight = """
    None of the shortlisted properties strongly match the
    selected priorities. Consider adding more properties
    or changing your search criteria.
    """


st.markdown(
    f"""
    <div class="ai-card">

    <h2>
    🤖 AI Decision Insight
    </h2>

    <p>
    {insight}
    </p>

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
🚀 Recommended Next Action
</h2>

</div>
""", unsafe_allow_html=True)


next_action = st.selectbox(
    "Choose your next action",
    [
        "Schedule Site Visit",
        "Start Legal Verification",
        "Calculate Loan / EMI",
        "Open Property Deal Room",
        "Compare More Properties",
        "Save Property to Shortlist"
    ]
)


if st.button(
    "➡️ CONTINUE WITH SELECTED PROPERTY",
    use_container_width=True
):

    st.success(
        f"✅ Next action selected: {next_action}"
    )


# ============================================================
# FUTURE FEATURES
# ============================================================

st.markdown("""
<div class="ai-card">

<h2>
🚀 Future Smart Comparison Features
</h2>

<p>
The production version can integrate:
</p>

<p>
🗺️ Live Location Comparison
&nbsp; • &nbsp;
💰 Real Market Price Analysis
&nbsp; • &nbsp;
🏦 Automatic EMI Comparison
&nbsp; • &nbsp;
📈 Investment ROI Forecast
&nbsp; • &nbsp;
⚖️ Legal Risk Score
&nbsp; • &nbsp;
🌐 Nearby Amenities
&nbsp; • &nbsp;
🤖 AI Personalized Recommendation
</p>

<p>
The system can learn buyer preferences and automatically
rank properties based on budget, lifestyle and investment goals.
</p>

</div>
""", unsafe_allow_html=True)


# ============================================================
# NOTICE
# ============================================================

st.markdown("""
<div class="warning-card">

<h2>
⚠️ Important Notice
</h2>

<p>
The Smart Decision Score is an informational comparison
tool based on user-entered data. It is not financial,
legal or investment advice.
</p>

</div>
""", unsafe_allow_html=True)
