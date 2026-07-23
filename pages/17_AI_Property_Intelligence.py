import streamlit as st
import pandas as pd

# ============================================================
# PAGE 17 + 18 MERGED
# AI PROPERTY INTELLIGENCE
# FIRSTCHOICE INFRA PROPERTY HUB
# ============================================================

st.set_page_config(
    page_title="AI Property Intelligence | FirstChoice Property Hub",
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
    font-size: 30px;
    font-weight: 900;
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

    margin-bottom: 30px;
}

/* PROPERTY CARD */

.property-card {
    padding: 30px;
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
    padding: 32px;
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

/* RESULT CARD */

.result-card {
    padding: 42px;
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

    margin-bottom: 30px;
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

    margin-bottom: 20px;
}

/* CTA */

.cta {
    padding: 36px;
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

    margin-top: 30px;
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

    box-shadow:
    0 18px 50px
    rgba(245,158,11,0.22);

    margin-top: 30px;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# SESSION STATE
# ============================================================

if "smart_matches" not in st.session_state:
    st.session_state.smart_matches = None

if "valuation_done" not in st.session_state:
    st.session_state.valuation_done = False

if "property_enquiries" not in st.session_state:
    st.session_state.property_enquiries = []

if "saved_properties" not in st.session_state:
    st.session_state.saved_properties = []

if "site_visit_requests" not in st.session_state:
    st.session_state.site_visit_requests = []


# ============================================================
# HERO
# ============================================================

st.markdown("""
<div class="hero">

<h1>
🤖 AI Property Intelligence
</h1>

<p>
Your intelligent real estate discovery and valuation centre.
Find properties that match your requirements and estimate
their potential market value using smart property intelligence.
</p>

<p>
🎯 Smart Match
&nbsp; • &nbsp;
💎 Property Valuation
&nbsp; • &nbsp;
📊 Market Intelligence
&nbsp; • &nbsp;
❤️ Saved Properties
&nbsp; • &nbsp;
💬 Property Enquiry
</p>

</div>
""", unsafe_allow_html=True)


# ============================================================
# AI INTRO
# ============================================================

st.markdown("""
<div class="ai-card">

<h2>
🧠 Your Personal Property Intelligence Assistant
</h2>

<p>
Use the Smart Match engine to discover properties according to
your budget, location, property type, bedroom requirements
and investment or end-use purpose.
</p>

<p>
You can also use the Property Valuation engine to generate an
illustrative estimated property value based on location,
area, property type, condition, age and amenities.
</p>

<p>
The current version uses rule-based intelligence.
Future versions can connect directly with live Property Hub
inventory, market data, transaction history and AI models.
</p>

</div>
""", unsafe_allow_html=True)


# ============================================================
# MAIN TABS
# ============================================================

tab1, tab2 = st.tabs([
    "🤖 AI Smart Property Match",
    "💎 AI Property Price Estimator"
])


# ################################################################
# TAB 1 — AI SMART PROPERTY MATCH
# ################################################################

with tab1:

    # ============================================================
    # DEMO PROPERTY DATABASE
    # ============================================================

    properties = pd.DataFrame({

        "Property ID": [
            "FC-PROP-1001",
            "FC-PROP-1002",
            "FC-PROP-1003",
            "FC-PROP-1004",
            "FC-PROP-1005",
            "FC-PROP-1006",
            "FC-PROP-1007"
        ],

        "Posted By User ID": [
            "USER-OWNER-001",
            "USER-BUILDER-002",
            "USER-OWNER-003",
            "USER-AGENT-004",
            "USER-BUILDER-005",
            "USER-OWNER-006",
            "USER-AGENT-007"
        ],

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
    # SECTION
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
            step=500000,
            key="match_budget"
        )


    with c2:

        match_location = st.selectbox(
            "📍 Preferred Location",
            [
                "Any Location",
                "Civil Lines",
                "Wardha Road",
                "Manish Nagar",
                "Besa",
                "Mihan",
                "Hingna"
            ],
            key="match_location"
        )


    c3, c4 = st.columns(2)


    with c3:

        match_property_type = st.selectbox(
            "🏡 Property Type",
            [
                "Any Type",
                "Apartment",
                "Villa",
                "Plot"
            ],
            key="match_type"
        )


    with c4:

        match_bedrooms = st.selectbox(
            "🛏️ Minimum Bedrooms",
            [
                0,
                1,
                2,
                3,
                4
            ],
            key="match_bedrooms"
        )


    purpose = st.selectbox(
        "🎯 Property Purpose",
        [
            "Any Purpose",
            "End Use",
            "Investment"
        ],
        key="match_purpose"
    )


    verified_only = st.toggle(
        "🛡️ Show Only Verified Properties",
        value=True,
        key="verified_only"
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
            match_location == "Any Location"
            or row["Location"] == match_location
        ):

            score += 20


        # Type
        if (
            match_property_type == "Any Type"
            or row["Type"] == match_property_type
        ):

            score += 20


        # Bedrooms
        if row["Bedrooms"] >= match_bedrooms:

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
        use_container_width=True,
        key="find_property"
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

    if st.session_state.smart_matches is not None:

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

            top_score = int(
                results.iloc[0]["Match Score"]
            )


            st.markdown(
                f"""
                <div class="match-card">

                <h2>
                🎯 Best Match Found
                </h2>

                <p>
                Our smart matching engine found
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

                    else

                    "⚠️ Verification Pending"

                )


                st.markdown(
                    f"""
                    <div class="property-card">

                    <h2>
                    🏡 {row["Property"]}
                    </h2>

                    <p>
                    🆔 Property ID:
                    <b>{row["Property ID"]}</b>
                    </p>

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


                # ====================================================
                # SAVE PROPERTY
                # ====================================================

                with b1:

                    if st.button(
                        "❤️ Save Property",
                        key=f"save_{row['Property ID']}",
                        use_container_width=True
                    ):

                        if row["Property ID"] not in [
                            x["Property ID"]
                            for x in st.session_state.saved_properties
                        ]:

                            st.session_state.saved_properties.append({

                                "Property ID":
                                row["Property ID"],

                                "Property":
                                row["Property"],

                                "Posted By User ID":
                                row["Posted By User ID"]

                            })


                        st.success(
                            "Property saved to your favourites."
                        )


                # ====================================================
                # ENQUIRY
                # IMPORTANT:
                # ENQUIRY GOES TO PROPERTY POSTER
                # ====================================================

                with b2:

                    if st.button(
                        "💬 Enquire Now",
                        key=f"enquire_{row['Property ID']}",
                        use_container_width=True
                    ):

                        enquiry_record = {

                            "Property ID":
                            row["Property ID"],

                            "Property":
                            row["Property"],

                            "Posted By User ID":
                            row["Posted By User ID"],

                            "Enquiry Status":
                            "New"

                        }


                        st.session_state.property_enquiries.append(
                            enquiry_record
                        )


                        st.success(
                            "Your enquiry has been sent to the person who posted this property."
                        )


                # ====================================================
                # SITE VISIT
                # ====================================================

                with b3:

                    if st.button(
                        "📅 Schedule Visit",
                        key=f"visit_{row['Property ID']}",
                        use_container_width=True
                    ):

                        visit_record = {

                            "Property ID":
                            row["Property ID"],

                            "Property":
                            row["Property"],

                            "Posted By User ID":
                            row["Posted By User ID"],

                            "Visit Status":
                            "Requested"

                        }


                        st.session_state.site_visit_requests.append(
                            visit_record
                        )


                        st.success(
                            "Site visit request sent to the property poster."
                        )


    # ============================================================
    # MATCH SCORE
    # ============================================================

    st.markdown("""
    <div class="section">

    <h2>
    🧠 How Our Smart Match Score Works
    </h2>

    </div>
    """, unsafe_allow_html=True)


    m1, m2, m3, m4, m5 = st.columns(5)


    match_factors = [

        ("💰", "30%", "Budget compatibility"),

        ("📍", "20%", "Location preference"),

        ("🏡", "20%", "Property type"),

        ("🛏️", "15%", "Bedroom requirement"),

        ("🎯", "10%", "Purpose matching")

    ]


    for col, data in zip(
        [m1, m2, m3, m4, m5],
        match_factors
    ):

        with col:

            st.markdown(
                f"""
                <div class="value-card">

                <h2>
                {data[0]} {data[1]}
                </h2>

                <p>
                {data[2]}
                </p>

                </div>
                """,
                unsafe_allow_html=True
            )


# ################################################################
# TAB 2 — AI PROPERTY PRICE ESTIMATOR
# ################################################################

with tab2:

    # ============================================================
    # VALUATION INTRO
    # ============================================================

    st.markdown("""
    <div class="ai-card">

    <h2>
    💎 Smart Property Valuation Engine
    </h2>

    <p>
    Enter the basic details of your property and receive an
    illustrative estimated market value range.
    </p>

    <p>
    The current version uses a rule-based estimation model.
    Future versions can connect to verified market data,
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

        valuation_location = st.selectbox(
            "📍 Property Location",
            [
                "Civil Lines",
                "Wardha Road",
                "Manish Nagar",
                "Besa",
                "Mihan",
                "Hingna"
            ],
            key="valuation_location"
        )


    with c2:

        valuation_property_type = st.selectbox(
            "🏡 Property Type",
            [
                "Apartment",
                "Villa",
                "Independent House",
                "Residential Plot",
                "Commercial Property"
            ],
            key="valuation_type"
        )


    c3, c4 = st.columns(2)


    with c3:

        area = st.number_input(
            "📐 Property Area (Sq.Ft.)",
            min_value=100,
            value=1000,
            step=50,
            key="valuation_area"
        )


    with c4:

        property_age = st.number_input(
            "🏗️ Property Age (Years)",
            min_value=0,
            max_value=100,
            value=5,
            step=1,
            key="valuation_age"
        )


    # ============================================================
    # CONDITION
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
        value="Good",
        key="valuation_condition"
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
            "🚗 Parking",
            key="parking"
        )

        lift = st.checkbox(
            "🛗 Lift",
            key="lift"
        )


    with a2:

        security = st.checkbox(
            "🛡️ Security",
            key="security"
        )

        garden = st.checkbox(
            "🌳 Garden",
            key="garden"
        )


    with a3:

        clubhouse = st.checkbox(
            "🏊 Clubhouse",
            key="clubhouse"
        )

        prime_location = st.checkbox(
            "📍 Prime Location",
            key="prime_location"
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
        valuation_location
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
        valuation_property_type
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
    # AGE
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
    # AMENITY BONUS
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
    # GENERATE VALUATION
    # ============================================================

    if st.button(
        "🚀 ESTIMATE PROPERTY VALUE",
        use_container_width=True,
        key="estimate_property"
    ):

        st.session_state.valuation_done = True


    # ============================================================
    # VALUATION RESULT
    # ============================================================

    if st.session_state.valuation_done:

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
                {valuation_location}
                </h2>

                </div>
                """,
                unsafe_allow_html=True
            )


        # ========================================================
        # VALUATION FACTORS
        # ========================================================

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
# PROPERTY ENQUIRY ROUTING
# ============================================================

st.markdown("""
<div class="section">

<h2>
📨 Property Enquiry Routing
</h2>

<p>
Every enquiry is connected to the Property ID and the User ID
of the person who posted that property.
</p>

<p>
This ensures that a buyer's interest goes to the correct
property owner, agent or builder.
</p>

</div>
""", unsafe_allow_html=True)


if len(st.session_state.property_enquiries) > 0:

    st.subheader(
        "💬 Enquiry Records"
    )

    enquiry_df = pd.DataFrame(
        st.session_state.property_enquiries
    )

    st.dataframe(
        enquiry_df,
        use_container_width=True,
        hide_index=True
    )

else:

    st.info(
        "No property enquiries generated in this session."
    )


# ============================================================
# SAVED PROPERTIES
# ============================================================

if len(st.session_state.saved_properties) > 0:

    st.markdown("""
    <div class="section">

    <h2>
    ❤️ Saved Properties
    </h2>

    </div>
    """, unsafe_allow_html=True)


    saved_df = pd.DataFrame(
        st.session_state.saved_properties
    )


    st.dataframe(
        saved_df,
        use_container_width=True,
        hide_index=True
    )


# ============================================================
# FUTURE AI ENGINE
# ============================================================

st.markdown("""
<div class="ai-card">

<h2>
🚀 Future AI Property Intelligence Engine
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
&nbsp; • &nbsp;
❤️ User Behaviour
&nbsp; • &nbsp;
🔎 Search History
</p>

<p>
The system can continuously improve property recommendations,
generate explainable valuation reports and connect buyers with
the exact person who posted each property.
</p>

</div>
""", unsafe_allow_html=True)


# ============================================================
# DISCLAIMER
# ============================================================

st.markdown("""
<div class="warning-card">

<h2>
⚠️ Important Disclaimer
</h2>

<p>
AI Smart Match scores are based on the current rule-based
demonstration model and should not be considered financial
or investment recommendations.
</p>

<p>
Property valuation results are illustrative estimates based
on sample pricing assumptions. They are not certified
property valuations or appraisals.
</p>

<p>
Users should independently verify property ownership,
documents, legal status, market value and other relevant
information before making any transaction.
</p>

</div>
""", unsafe_allow_html=True)
