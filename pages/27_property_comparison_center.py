import streamlit as st

# ============================================================
# PAGE — SMART PROPERTY COMPARISON & DECISION CENTER
# MERGED: PAGE 5 + PAGE 27
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

/* ============================================================
HERO
============================================================ */

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

/* ============================================================
SECTION
============================================================ */

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

/* ============================================================
CARD
============================================================ */

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

/* ============================================================
AI CARD
============================================================ */

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

/* ============================================================
BEST PROPERTY
============================================================ */

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

/* ============================================================
WARNING
============================================================ */

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

/* ============================================================
PROPERTY IMAGE
============================================================ */

.property-image {
    border-radius: 20px;
}

/* ============================================================
BADGES
============================================================ */

.badge {
    display: inline-block;
    padding: 7px 14px;
    border-radius: 30px;
    color: white;
    font-size: 12px;
    font-weight: 800;
    margin-right: 5px;
}

.verified {
    background: #059669;
}

.premium {
    background: #7C3AED;
}

.featured {
    background: #EF4444;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# HERO
# ============================================================

st.markdown("""
<div class="hero">

<h1>
⚖️ Smart Property Comparison & Decision Center
</h1>

<p>
Compare multiple properties side-by-side and make a smarter
property purchase or investment decision.
</p>

<p>
💰 Price • 📍 Location • 📐 Area • 🏠 Amenities •
⚖️ Legal • 📈 Investment • ⭐ Trust • 🤖 Smart Score
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
Select properties from your shortlist and compare important
property factors on one screen.
</p>

<p>
The system calculates a smart decision score based on your
personal priorities and highlights the property that best
matches your requirements.
</p>

</div>
""", unsafe_allow_html=True)


# ============================================================
# PROPERTY DATABASE
# PAGE 5 EXISTING PROPERTY DATA
# ============================================================

property_data = {

"Premium 3 BHK Luxury Apartment — Civil Lines": {

"image":
"https://images.unsplash.com/photo-1600585154340-be6161a56a0c",

"type":
"Apartment",

"configuration":
"3 BHK",

"area":
1850,

"price":
12500000,

"price_sqft":
6756,

"location":
"Civil Lines, Nagpur",

"age":
"New Construction",

"parking":
"Yes",

"pool":
"Yes",

"gym":
"Yes",

"security":
"24x7",

"verification":
"Verified",

"legal_status":
"Verified",

"trust":
85,

"site_rating":
4.5,

"location_rating":
4.5,

"investment_rating":
4.2,

"amenities":
[
"Parking",
"Lift",
"Security",
"Swimming Pool",
"Gym",
"Garden"
]

},

"Modern 4 BHK Premium Villa — Wardha Road": {

"image":
"https://images.unsplash.com/photo-1600607687920-4e2a09cf159d",

"type":
"Villa",

"configuration":
"4 BHK",

"area":
2800,

"price":
21000000,

"price_sqft":
7500,

"location":
"Wardha Road, Nagpur",

"age":
"New Construction",

"parking":
"Yes",

"pool":
"Yes",

"gym":
"Yes",

"security":
"24x7",

"verification":
"Identity Verified",

"legal_status":
"Verified",

"trust":
92,

"site_rating":
4.7,

"location_rating":
4.6,

"investment_rating":
4.5,

"amenities":
[
"Parking",
"Lift",
"Security",
"Swimming Pool",
"Gym",
"Garden",
"Club House"
]

},

"Premium Residential Plot — Amravati Road": {

"image":
"https://images.unsplash.com/photo-1500382017468-9049fed747ef",

"type":
"Residential Plot",

"configuration":
"N/A",

"area":
2000,

"price":
6500000,

"price_sqft":
3250,

"location":
"Amravati Road, Nagpur",

"age":
"New",

"parking":
"N/A",

"pool":
"N/A",

"gym":
"N/A",

"security":
"Area Security",

"verification":
"Documents Under Review",

"legal_status":
"Under Verification",

"trust":
72,

"site_rating":
3.8,

"location_rating":
4.0,

"investment_rating":
4.6,

"amenities":
[
"Security",
"Road Access"
]

},

"Commercial Office Space — MIHAN": {

"image":
"https://images.unsplash.com/photo-1497366754035-f200968a6e72",

"type":
"Commercial Office",

"configuration":
"Office",

"area":
3500,

"price":
18000000,

"price_sqft":
5143,

"location":
"MIHAN, Nagpur",

"age":
"New",

"parking":
"Yes",

"pool":
"No",

"gym":
"No",

"security":
"24x7",

"verification":
"Verified",

"legal_status":
"Verified",

"trust":
88,

"site_rating":
4.2,

"location_rating":
4.3,

"investment_rating":
4.7,

"amenities":
[
"Parking",
"Security",
"Lift",
"Power Backup"
]

},

"Luxury Villa — Seminary Hills": {

"image":
"https://images.unsplash.com/photo-1613490493576-7fde63acd811",

"type":
"Luxury Villa",

"configuration":
"5 BHK",

"area":
4200,

"price":
35000000,

"price_sqft":
8333,

"location":
"Seminary Hills, Nagpur",

"age":
"2 Years",

"parking":
"Yes",

"pool":
"Yes",

"gym":
"Yes",

"security":
"24x7",

"verification":
"Verified",

"legal_status":
"Verified",

"trust":
95,

"site_rating":
4.8,

"location_rating":
4.9,

"investment_rating":
4.6,

"amenities":
[
"Parking",
"Lift",
"Security",
"Swimming Pool",
"Gym",
"Garden",
"Club House",
"Power Backup"
]

}

}


# ============================================================
# SELECT PROPERTIES
# ============================================================

st.markdown("""
<div class="section">

<h2>
🏡 Select Properties for Comparison
</h2>

<p>
Choose 2 to 5 properties from your shortlist.
</p>

</div>
""", unsafe_allow_html=True)


selected_properties = st.multiselect(

"🔎 Choose properties to compare",

list(property_data.keys()),

default=[
"Premium 3 BHK Luxury Apartment — Civil Lines",
"Modern 4 BHK Premium Villa — Wardha Road",
"Premium Residential Plot — Amravati Road"
],

max_selections=5

)


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
# MAIN COMPARISON
# ============================================================

if len(selected_properties) >= 2:

    selected_data = [
        property_data[name]
        for name in selected_properties
    ]


    # ========================================================
    # PROPERTY CARDS
    # ========================================================

    st.markdown("""
    <div class="section">

    <h2>
    🏠 Selected Properties
    </h2>

    </div>
    """, unsafe_allow_html=True)


    columns = st.columns(
        len(selected_properties)
    )


    for index, property_name in enumerate(
        selected_properties
    ):

        data = property_data[property_name]

        with columns[index]:

            st.image(
                data["image"],
                use_container_width=True
            )

            st.markdown(
                f"""
                <div class="card">

                <span class="badge verified">
                🛡️ {data["verification"]}
                </span>

                <h3>
                {property_name}
                </h3>

                <p>
                📍 {data["location"]}
                </p>

                <h2>
                ₹{data["price"]:,.0f}
                </h2>

                <p>
                🏠 {data["type"]}
                </p>

                <p>
                📐 {data["area"]:,} Sq.Ft.
                </p>

                <p>
                ⭐ Trust Score:
                {data["trust"]}/100
                </p>

                </div>
                """,
                unsafe_allow_html=True
            )


    # ========================================================
    # SIDE BY SIDE COMPARISON
    # ========================================================

    st.markdown("""
    <div class="section">

    <h2>
    📊 Side-by-Side Property Comparison
    </h2>

    </div>
    """, unsafe_allow_html=True)


    comparison_rows = [

        ("🏠 Property Type", "type"),

        ("🛏️ Configuration", "configuration"),

        ("📐 Area", "area"),

        ("💰 Price", "price"),

        ("💵 Price / Sq.Ft.", "price_sqft"),

        ("📍 Location", "location"),

        ("🏗️ Property Age", "age"),

        ("🚗 Parking", "parking"),

        ("🏊 Swimming Pool", "pool"),

        ("🏋️ Gym", "gym"),

        ("🔒 Security", "security"),

        ("🛡️ Verification", "verification"),

        ("⚖️ Legal Status", "legal_status"),

        ("⭐ Trust Score", "trust"),

        ("📅 Site Visit Rating", "site_rating"),

        ("📍 Location Rating", "location_rating"),

        ("📈 Investment Rating", "investment_rating"),

        ("✨ Amenities Count", "amenities")

    ]


    for label, key in comparison_rows:

        row_columns = st.columns(
            len(selected_properties) + 1
        )

        with row_columns[0]:

            st.markdown(
                f"**{label}**"
            )

        for index, property_name in enumerate(
            selected_properties
        ):

            data = property_data[property_name]

            with row_columns[index + 1]:

                value = data[key]

                if key == "price":

                    st.write(
                        f"₹{value:,.0f}"
                    )

                elif key == "area":

                    st.write(
                        f"{value:,} Sq.Ft."
                    )

                elif key == "price_sqft":

                    st.write(
                        f"₹{value:,}"
                    )

                elif key == "amenities":

                    st.write(
                        f"{len(value)} Amenities"
                    )

                elif key in [
                    "site_rating",
                    "location_rating",
                    "investment_rating"
                ]:

                    st.write(
                        f"{value}/5"
                    )

                elif key == "trust":

                    st.progress(
                        value / 100
                    )

                    st.write(
                        f"{value}/100"
                    )

                else:

                    st.write(
                        value
                    )

        st.divider()


    # ========================================================
    # TRUST SCORE ANALYSIS
    # ========================================================

    st.markdown("""
    <div class="section">

    <h2>
    ⭐ Trust Score Analysis
    </h2>

    </div>
    """, unsafe_allow_html=True)


    trust_values = [

        (
            name,
            property_data[name]["trust"]
        )

        for name in selected_properties

    ]


    trust_values.sort(
        key=lambda x: x[1],
        reverse=True
    )


    trust_winner = trust_values[0]


    st.success(

        f"""
        🏆 Highest Trust Score:

        {trust_winner[0]}

        ⭐ Score: {trust_winner[1]}/100
        """

    )


    # ========================================================
    # SMART SCORE CALCULATION
    # ========================================================

    prices = [

        property_data[name]["price"]

        for name in selected_properties

    ]


    max_price = max(prices)

    min_price = min(prices)


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

        elif status == "Under Verification":

            return 60

        elif status == "Needs Review":

            return 35

        else:

            return 10


    scores = []


    for property_name in selected_properties:

        p = property_data[property_name]


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

            investment_score
            * investment_weight

            +

            site_score
            * site_weight

            +

            legal_score_value
            * legal_weight

            +

            amenities_score
            * amenities_weight

        ) / total_weight


        scores.append({

            "Property":
            property_name,

            "Price Score":
            round(
                p_score,
                1
            ),

            "Location Score":
            round(
                loc_score,
                1
            ),

            "Investment Score":
            round(
                investment_score,
                1
            ),

            "Site Visit Score":
            round(
                site_score,
                1
            ),

            "Legal Score":
            round(
                legal_score_value,
                1
            ),

            "Amenities Score":
            round(
                amenities_score,
                1
            ),

            "Final Score":
            round(
                final_score,
                1
            )

        })


    # ========================================================
    # SMART DECISION SCORE
    # ========================================================

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


    # ========================================================
    # BEST PROPERTY
    # ========================================================

    best_index = max(

        range(
            len(scores)
        ),

        key=lambda i:
        scores[i]["Final Score"]

    )


    best_property_name = (

        selected_properties[
            best_index
        ]

    )


    best_property = property_data[

        best_property_name

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
        {best_property_name}
        </h1>

        <h2>
        Decision Score:
        {best_score}/100
        </h2>

        <p>
        📍 {best_property["location"]}
        </p>

        <p>
        💰 ₹{best_property["price"]:,.0f}
        </p>

        <p>
        📐 {best_property["area"]:,} Sq.Ft.
        </p>

        <p>
        ⭐ Trust Score:
        {best_property["trust"]}/100
        </p>

        <p>
        ⚖️ Legal Status:
        {best_property["legal_status"]}
        </p>

        </div>
        """,

        unsafe_allow_html=True

    )


    # ========================================================
    # AI DECISION INSIGHT
    # ========================================================

    if best_score >= 80:

        insight = """

        This property strongly matches your selected priorities.
        It may be considered the leading option for further legal,
        financial and physical verification.

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


    # ========================================================
    # ACTIONS
    # ========================================================

    st.markdown("""
    <div class="section">

    <h2>
    🚀 What Would You Like To Do?
    </h2>

    </div>
    """, unsafe_allow_html=True)


    a1, a2, a3 = st.columns(3)


    with a1:

        if st.button(

            "❤️ Save Comparison",

            use_container_width=True

        ):

            st.success(

                "Comparison saved to your account."

            )


    with a2:

        if st.button(

            "📞 Contact Best Property",

            use_container_width=True

        ):

            st.success(

                "Contact request submitted."

            )


    with a3:

        if st.button(

            "📅 Schedule Site Visit",

            use_container_width=True

        ):

            st.success(

                "Site visit request initiated."

            )


    # ========================================================
    # NEXT ACTION
    # ========================================================

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

            f"✅ Next action selected: "
            f"{next_action}"

        )


else:

    st.warning(

        "Please select at least two properties "
        "to compare."

    )


# ============================================================
# FUTURE AI FEATURES
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
tool based on available property data and user priorities.
It is not financial, legal or investment advice.
</p>

</div>
""", unsafe_allow_html=True)
