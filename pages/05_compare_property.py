import streamlit as st

# ============================================================
# PAGE 5 — COMPARE PROPERTY
# FIRSTCHOICE INFRA PROPERTY HUB
# ============================================================

st.set_page_config(
    page_title="Compare Properties | FirstChoice Property Hub",
    page_icon="⚖️",
    layout="wide"
)

# ============================================================
# PREMIUM MULTICOLOUR DESIGN
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
    padding: 45px;
    border-radius: 32px;
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
    rgba(37,99,235,0.25);

    margin-bottom: 30px;
}

.hero h1 {
    font-size: 44px;
    font-weight: 900;
}

.hero p {
    font-size: 18px;
}

/* SECTION */

.section {
    margin-top: 30px;
    margin-bottom: 20px;

    padding: 25px 30px;

    border-radius: 24px;

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
    rgba(79,70,229,0.18);
}

.section h2 {
    margin: 0;
    font-size: 28px;
    font-weight: 900;
}

/* CARD */

.card {
    padding: 28px;

    border-radius: 25px;

    background: white;

    box-shadow:
    0 15px 45px
    rgba(0,0,0,0.08);

    margin-bottom: 25px;
}

/* WINNER */

.winner {
    padding: 25px;

    border-radius: 25px;

    color: white;

    background:
    linear-gradient(
        135deg,
        #047857,
        #059669,
        #10B981
    );

    box-shadow:
    0 15px 45px
    rgba(5,150,105,0.20);
}

/* CTA */

.cta {
    padding: 35px;

    border-radius: 30px;

    color: white;

    text-align: center;

    background:
    linear-gradient(
        135deg,
        #071952,
        #2563EB,
        #7C3AED,
        #EC4899
    );

    box-shadow:
    0 20px 60px
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
⚖️ Compare Properties
</h1>

<p>
Compare properties side-by-side and make a smarter
real estate decision.
</p>

<p>
💰 Price • 📐 Area • 📍 Location • 🏠 Features • 🛡️ Trust
</p>

</div>
""", unsafe_allow_html=True)


# ============================================================
# INTRO
# ============================================================

st.markdown("""
<div class="section">

<h2>
🏡 Smart Property Comparison
</h2>

<p>
Select up to three properties and compare the most important
factors before buying or investing.
</p>

</div>
""", unsafe_allow_html=True)


# ============================================================
# PROPERTY SELECTION
# ============================================================

st.markdown("""
<div class="card">

<h2>
🔎 Select Properties
</h2>

</div>
""", unsafe_allow_html=True)


property_options = [
    "Premium 3 BHK Luxury Apartment — Civil Lines",
    "Modern 4 BHK Premium Villa — Wardha Road",
    "Premium Residential Plot — Amravati Road",
    "Commercial Office Space — MIHAN",
    "Luxury Villa — Seminary Hills"
]


selected_properties = st.multiselect(
    "Choose properties to compare",
    property_options,
    default=[
        property_options[0],
        property_options[1],
        property_options[2]
    ],
    max_selections=3
)


# ============================================================
# COMPARISON DATA
# ============================================================

property_data = {

    "Premium 3 BHK Luxury Apartment — Civil Lines": {
        "image":
        "https://images.unsplash.com/photo-1600585154340-be6161a56a0c",
        "type": "Apartment",
        "configuration": "3 BHK",
        "area": "1,850 Sq.Ft.",
        "price": "₹1.25 Cr",
        "price_sqft": "₹6,756",
        "location": "Civil Lines, Nagpur",
        "age": "New Construction",
        "parking": "Yes",
        "pool": "Yes",
        "gym": "Yes",
        "security": "24x7",
        "verification": "Verified",
        "trust": 85
    },

    "Modern 4 BHK Premium Villa — Wardha Road": {
        "image":
        "https://images.unsplash.com/photo-1600607687920-4e2a09cf159d",
        "type": "Villa",
        "configuration": "4 BHK",
        "area": "2,800 Sq.Ft.",
        "price": "₹2.10 Cr",
        "price_sqft": "₹7,500",
        "location": "Wardha Road, Nagpur",
        "age": "New Construction",
        "parking": "Yes",
        "pool": "Yes",
        "gym": "Yes",
        "security": "24x7",
        "verification": "Identity Verified",
        "trust": 92
    },

    "Premium Residential Plot — Amravati Road": {
        "image":
        "https://images.unsplash.com/photo-1500382017468-9049fed747ef",
        "type": "Residential Plot",
        "configuration": "N/A",
        "area": "2,000 Sq.Ft.",
        "price": "₹65 Lakh",
        "price_sqft": "₹3,250",
        "location": "Amravati Road, Nagpur",
        "age": "New",
        "parking": "N/A",
        "pool": "N/A",
        "gym": "N/A",
        "security": "Area Security",
        "verification": "Documents Under Review",
        "trust": 72
    },

    "Commercial Office Space — MIHAN": {
        "image":
        "https://images.unsplash.com/photo-1497366754035-f200968a6e72",
        "type": "Commercial Office",
        "configuration": "Office",
        "area": "3,500 Sq.Ft.",
        "price": "₹1.80 Cr",
        "price_sqft": "₹5,143",
        "location": "MIHAN, Nagpur",
        "age": "New",
        "parking": "Yes",
        "pool": "No",
        "gym": "No",
        "security": "24x7",
        "verification": "Verified",
        "trust": 88
    },

    "Luxury Villa — Seminary Hills": {
        "image":
        "https://images.unsplash.com/photo-1613490493576-7fde63acd811",
        "type": "Luxury Villa",
        "configuration": "5 BHK",
        "area": "4,200 Sq.Ft.",
        "price": "₹3.50 Cr",
        "price_sqft": "₹8,333",
        "location": "Seminary Hills, Nagpur",
        "age": "2 Years",
        "parking": "Yes",
        "pool": "Yes",
        "gym": "Yes",
        "security": "24x7",
        "verification": "Verified",
        "trust": 95
    }
}


# ============================================================
# SHOW COMPARISON
# ============================================================

if len(selected_properties) >= 2:

    st.markdown("""
    <div class="section">

    <h2>
    📊 Property Comparison
    </h2>

    <p>
    Compare selected properties side-by-side.
    </p>

    </div>
    """, unsafe_allow_html=True)


    columns = st.columns(len(selected_properties))


    # --------------------------------------------------------
    # PROPERTY IMAGE + TITLE
    # --------------------------------------------------------

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

                <h2>
                {property_name}
                </h2>

                </div>
                """,
                unsafe_allow_html=True
            )


    # ========================================================
    # COMPARISON TABLE
    # ========================================================

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
        ("⭐ Trust Score", "trust")
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

                if key == "trust":

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


    trust_values = []

    for property_name in selected_properties:

        trust_values.append(
            (
                property_name,
                property_data[property_name]["trust"]
            )
        )


    trust_values.sort(
        key=lambda x: x[1],
        reverse=True
    )


    winner_name = trust_values[0][0]

    winner_score = trust_values[0][1]


    st.markdown(
        f"""
        <div class="winner">

        <h2>
        🏆 Highest Trust Score
        </h2>

        <h3>
        {winner_name}
        </h3>

        <p>
        ⭐ Trust Score: {winner_score}/100
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


else:

    st.warning(
        "Please select at least two properties to compare."
    )


# ============================================================
# FUTURE AI FEATURE
# ============================================================

st.markdown("""
<div class="cta">

<h2>
🤖 AI Property Decision Assistant
</h2>

<p>
In the future, FirstChoice Property Hub will analyze
price, location, amenities, verification and investment
potential to help users identify the best-fit property.
</p>

</div>
""", unsafe_allow_html=True)


if st.button(
    "🤖 GET SMART PROPERTY RECOMMENDATION",
    use_container_width=True
):

    st.info(
        "AI recommendation engine will be connected "
        "to the real property database in the next phase."
    )
