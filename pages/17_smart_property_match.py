import streamlit as st
import pandas as pd

# ============================================================
# PAGE 17 — AI SMART PROPERTY MATCH
# FIRSTCHOICE INFRA PROPERTY HUB
# ============================================================

st.set_page_config(
    page_title="AI Smart Property Match | FirstChoice Property Hub",
    page_icon="🤖",
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

/* PROPERTY CARD */

.property-card {
    padding: 28px;
    border-radius: 28px;

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

    margin-bottom: 22px;
}

/* MATCH CARD */

.match-card {
    padding: 30px;
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
    0 18px 55px
    rgba(5,150,105,0.25);

    margin-bottom: 25px;
}

/* AI CARD */

.ai-card {
    padding: 30px;
    border-radius: 28px;

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
🤖 AI Smart Property Match
</h1>

<p>
Tell us what you are looking for.
Our intelligent matching engine will analyse your preferences
and identify properties that best match your requirements.
</p>

<p>
💰 Budget • 📍 Location • 🏡 Property Type • 🛏️ Bedrooms • 🎯 Purpose
</p>

</div>
""", unsafe_allow_html=True)


# ============================================================
# AI INTRO
# ============================================================

st.markdown("""
<div class="ai-card">

<h2>
🧠 Your Personal Property Discovery Assistant
</h2>

<p>
Instead of searching through hundreds of listings manually,
define your requirements and get a personalised property match score.
</p>

<p>
The current version uses a smart rule-based matching engine.
It can later be connected to AI, live inventory and user behaviour data.
</p>

</div>
""", unsafe_allow_html=True)


# ============================================================
# DEMO PROPERTY DATABASE
# ============================================================

properties = pd.DataFrame({

    "Property": [
        "Luxury 3 BHK Skyline Apartment",
        "Premium 4 BHK Garden Villa",
        "Modern 2 BHK Smart Home",
        "Premium Residential Plot",
        "Mihan Investment Apartment",
        "Luxury Wardha Road Villa",
        "Affordable Family Apartment"
    ],

    "Location": [
        "Civil Lines",
        "Wardha Road",
        "Manish Nagar",
        "Besa",
        "Mihan",
        "Wardha Road",
        "Hingna"
    ],

    "Type": [
        "Apartment",
        "Villa",
        "Apartment",
        "Plot",
        "Apartment",
        "Villa",
        "Apartment"
    ],

    "Price": [
        6500000,
        12000000,
        4200000,
        3000000,
        5500000,
        9500000,
        3200000
    ],

    "Bedrooms": [
        3,
        4,
        2,
        0,
        2,
        4,
        2
    ],

    "Purpose": [
        "End Use",
        "End Use",
        "End Use",
        "Investment",
        "Investment",
        "End Use",
        "End Use"
    ],

    "Verified": [
        True,
        True,
        True,
        False,
        True,
        True,
        False
    ]

})


# ============================================================
# USER REQUIREMENTS
# ============================================================

st.markdown("""
<div class="section">

<h2>
🎯 Tell Us Your Property Requirements
</h2>

<p>
The more accurately you define your needs,
the better the matching result.
</p>

</div>
""", unsafe_allow_html=True)


c1, c2 = st.columns(2)


with c1:

    budget = st.number_input(
        "💰 Maximum Budget (₹)",
        min_value=500000,
        value=7000000,
        step=500000
    )


with c2:

    location = st.selectbox(
        "📍 Preferred Location",
        [
            "Any Location",
            "Civil Lines",
            "Wardha Road",
            "Manish Nagar",
            "Besa",
            "Mihan",
            "Hingna"
        ]
    )


c3, c4 = st.columns(2)


with c3:

    property_type = st.selectbox(
        "🏡 Property Type",
        [
            "Any Type",
            "Apartment",
            "Villa",
            "Plot"
        ]
    )


with c4:

    bedrooms = st.selectbox(
        "🛏️ Minimum Bedrooms",
        [
            0,
            1,
            2,
            3,
            4
        ]
    )


purpose = st.selectbox(
    "🎯 Property Purpose",
    [
        "Any Purpose",
        "End Use",
        "Investment"
    ]
)


verified_only = st.toggle(
    "🛡️ Show Only Verified Properties",
    value=True
)


# ============================================================
# MATCH ENGINE
# ============================================================

def calculate_match_score(row):

    score = 0

    # Budget
    if row["Price"] <= budget:

        score += 30

    elif row["Price"] <= budget * 1.10:

        score += 15


    # Location
    if (
        location == "Any Location"
        or row["Location"] == location
    ):

        score += 20


    # Type
    if (
        property_type == "Any Type"
        or row["Type"] == property_type
    ):

        score += 20


    # Bedrooms
    if row["Bedrooms"] >= bedrooms:

        score += 15


    # Purpose
    if (
        purpose == "Any Purpose"
        or row["Purpose"] == purpose
    ):

        score += 10


    # Verification
    if row["Verified"]:

        score += 5


    return score


# ============================================================
# FIND MATCHES
# ============================================================

if st.button(
    "🚀 FIND MY PERFECT PROPERTY",
    use_container_width=True
):

    results = properties.copy()


    if verified_only:

        results = results[
            results["Verified"] == True
        ]


    results[
        "Match Score"
    ] = results.apply(
        calculate_match_score,
        axis=1
    )


    results = results.sort_values(
        "Match Score",
        ascending=False
    )


    st.session_state.smart_matches = results


# ============================================================
# DISPLAY RESULTS
# ============================================================

if "smart_matches" in st.session_state:

    results = st.session_state.smart_matches


    st.markdown("""
    <div class="section">

    <h2>
    🏆 Your Smart Property Matches
    </h2>

    <p>
    Properties are ranked according to your selected preferences.
    </p>

    </div>
    """, unsafe_allow_html=True)


    if len(results) == 0:

        st.warning(
            "No matching properties found. Try changing your requirements."
        )


    else:

        top_score = results.iloc[0]["Match Score"]


        st.markdown(
            f"""
            <div class="match-card">

            <h2>
            🎯 Best Match Found
            </h2>

            <p>
            Our current smart matching engine found
            <b>{len(results)}</b>
            potential property matches.
            </p>

            <p>
            🏆 Highest Match Score:
            <b>{top_score}%</b>
            </p>

            </div>
            """,
            unsafe_allow_html=True
        )


        for index, row in results.iterrows():

            score = int(
                row["Match Score"]
            )


            if score >= 80:

                badge = "🔥 Excellent Match"

            elif score >= 60:

                badge = "⭐ Strong Match"

            else:

                badge = "👍 Potential Match"


            verification = (
                "🛡️ Verified"
                if row["Verified"]
                else "⚠️ Verification Pending"
            )


            st.markdown(
                f"""
                <div class="property-card">

                <h2>
                🏡 {row["Property"]}
                </h2>

                <p>
                📍 {row["Location"]}
                &nbsp; • &nbsp;
                🏠 {row["Type"]}
                &nbsp; • &nbsp;
                🛏️ {row["Bedrooms"]} Bedrooms
                </p>

                <h2>
                💰 ₹{row["Price"]:,.0f}
                </h2>

                <p>
                🎯 Purpose: {row["Purpose"]}
                </p>

                <p>
                {verification}
                </p>

                <h3>
                {badge}
                &nbsp; — &nbsp;
                {score}% Match
                </h3>

                </div>
                """,
                unsafe_allow_html=True
            )


            b1, b2, b3 = st.columns(3)


            with b1:

                if st.button(
                    "❤️ Save Property",
                    key=f"save_{index}",
                    use_container_width=True
                ):

                    st.success(
                        "Property saved to your favourites."
                    )


            with b2:

                if st.button(
                    "💬 Enquire Now",
                    key=f"enquire_{index}",
                    use_container_width=True
                ):

                    st.info(
                        "Your enquiry request has been initiated."
                    )


            with b3:

                if st.button(
                    "📅 Schedule Visit",
                    key=f"visit_{index}",
                    use_container_width=True
                ):

                    st.success(
                        "Site visit request initiated."
                    )


# ============================================================
# HOW MATCH SCORE WORKS
# ============================================================

st.markdown("""
<div class="section">

<h2>
🧠 How Our Smart Match Score Works
</h2>

</div>
""", unsafe_allow_html=True)


m1, m2, m3, m4, m5 = st.columns(5)


with m1:

    st.markdown("""
    <div class="property-card">

    <h3>
    💰 30%
    </h3>

    <p>
    Budget compatibility
    </p>

    </div>
    """, unsafe_allow_html=True)


with m2:

    st.markdown("""
    <div class="property-card">

    <h3>
    📍 20%
    </h3>

    <p>
    Location preference
    </p>

    </div>
    """, unsafe_allow_html=True)


with m3:

    st.markdown("""
    <div class="property-card">

    <h3>
    🏡 20%
    </h3>

    <p>
    Property type
    </p>

    </div>
    """, unsafe_allow_html=True)


with m4:

    st.markdown("""
    <div class="property-card">

    <h3>
    🛏️ 15%
    </h3>

    <p>
    Bedroom requirement
    </p>

    </div>
    """, unsafe_allow_html=True)


with m5:

    st.markdown("""
    <div class="property-card">

    <h3>
    🎯 10%
    </h3>

    <p>
    Purpose matching
    </p>

    </div>
    """, unsafe_allow_html=True)


# ============================================================
# FUTURE AI ENGINE
# ============================================================

st.markdown("""
<div class="ai-card">

<h2>
🚀 Future AI Property Recommendation Engine
</h2>

<p>
The future version can analyse:
</p>

<p>
📍 Search history
&nbsp; • &nbsp;
❤️ Saved properties
&nbsp; • &nbsp;
💰 Budget behaviour
&nbsp; • &nbsp;
🏡 Property preferences
&nbsp; • &nbsp;
📊 Market trends
&nbsp; • &nbsp;
🧠 User interactions
</p>

<p>
The system can continuously improve recommendations
and create a personalised property discovery experience.
</p>

</div>
""", unsafe_allow_html=True)


# ============================================================
# DISCLAIMER
# ============================================================

st.warning(
    "⚠️ The current matching engine is a demonstration based on "
    "sample property data and rule-based scoring. Match scores "
    "are not financial or investment recommendations. "
    "Future versions can connect this interface to the actual "
    "Property Hub inventory database and AI recommendation services."
)
