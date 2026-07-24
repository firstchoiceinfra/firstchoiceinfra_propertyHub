import streamlit as st

from navigation import (
    render_sidebar,
    render_bottom_navigation
)


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(

    page_title="FirstChoice Property Hub",

    page_icon="🏠",

    layout="wide",

    initial_sidebar_state="expanded"

)


# ============================================================
# SIDEBAR
# ============================================================

render_sidebar()


# ============================================================
# PREMIUM UI
# ============================================================

st.markdown(
"""
<style>

.stApp {

    background:
    linear-gradient(
        135deg,
        #F7F9FF 0%,
        #FFF7F3 35%,
        #F7F1FF 70%,
        #EFFCFF 100%
    );

}


header {

    visibility:hidden;

}


#MainMenu {

    visibility:hidden;

}


footer {

    visibility:hidden;

}


.hero {

    padding:50px;

    border-radius:36px;

    color:white;

    background:
    linear-gradient(
        135deg,
        #071952,
        #2563EB,
        #7C3AED,
        #EC4899
    );

    box-shadow:
    0 25px 70px
    rgba(37,99,235,0.25);

}


.card {

    padding:30px;

    min-height:200px;

    border-radius:28px;

    background:white;

    box-shadow:
    0 15px 40px
    rgba(0,0,0,0.08);

}


.section {

    margin-top:30px;

    padding:28px;

    border-radius:26px;

    color:white;

    background:
    linear-gradient(
        135deg,
        #071952,
        #2563EB,
        #7C3AED,
        #EC4899
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
🏠 FirstChoice Property Hub
</h1>

<h3>
India's Next-Generation Real Estate Marketplace
</h3>

<p>
Buy • Sell • Rent • Invest • Compare • Discover
</p>

</div>
""",
unsafe_allow_html=True
)


# ============================================================
# SEARCH
# ============================================================

st.markdown(
"""
<div class="section">

<h2>
🔎 Find Your Perfect Property
</h2>

<p>
Search homes, plots, commercial spaces and investment opportunities.
</p>

</div>
""",
unsafe_allow_html=True
)


c1, c2, c3 = st.columns(3)


with c1:

    looking_for = st.selectbox(

        "What are you looking for?",

        [
            "🏠 Buy",
            "🔑 Rent",
            "🏢 Commercial",
            "🌳 Land & Plot",
            "📈 Investment"
        ]

    )


with c2:

    location = st.text_input(

        "📍 Location",

        placeholder=
        "City, Locality or PIN Code"

    )


with c3:

    property_type = st.selectbox(

        "🏡 Property Type",

        [
            "Any Property",
            "Apartment",
            "Flat",
            "Villa",
            "Independent House",
            "Plot",
            "Farm Land",
            "Office",
            "Shop",
            "Warehouse"
        ]

    )


if st.button(

    "🔎 SEARCH PROPERTY",

    use_container_width=True

):

    st.success(

        "Property search request submitted."

    )


# ============================================================
# FEATURES
# ============================================================

st.markdown(
"""
<div class="section">

<h2>
🚀 One Platform. Every Property Need.
</h2>

</div>
""",
unsafe_allow_html=True
)


f1, f2, f3, f4 = st.columns(4)


features = [

    (
        "🏠 Buy",
        "Discover apartments, villas, houses and plots."
    ),

    (
        "🔑 Rent",
        "Find homes and commercial properties for rent."
    ),

    (
        "📈 Invest",
        "Analyze ROI, rental yield and future value."
    ),

    (
        "🛡️ Trust",
        "Explore verified properties and trusted users."
    )

]


for column, feature in zip(

    [f1, f2, f3, f4],

    features

):

    with column:

        st.markdown(
            f"""
            <div class="card">

            <h2>
            {feature[0]}
            </h2>

            <p>
            {feature[1]}
            </p>

            </div>
            """,
            unsafe_allow_html=True
        )


# ============================================================
# QUICK ACCESS
# ============================================================

st.markdown(
"""
<div class="section">

<h2>
⚡ Quick Access
</h2>

</div>
""",
unsafe_allow_html=True
)


q1, q2, q3 = st.columns(3)


with q1:

    if st.button(
        "📈 Investment & Finance",
        use_container_width=True
    ):

        st.switch_page(
            "pages/28_Investment_Finance_Center.py"
        )


with q2:

    if st.button(
        "⚖️ Property Comparison",
        use_container_width=True
    ):

        st.switch_page(
            "pages/29_Property_Comparison.py"
        )


with q3:

    if st.button(
        "🏦 Loan & EMI Comparison",
        use_container_width=True
    ):

        st.switch_page(
            "pages/30_Loan_EMI_Comparison.py"
        )


# ============================================================
# BOTTOM NAVIGATION
# ============================================================

render_bottom_navigation(
    "🏠 Home"
)


# ============================================================
# FOOTER
# ============================================================

st.markdown(
"""
<div style="
    text-align:center;
    padding:35px;
">

<h2>
🏠 FIRSTCHOICE INFRA PROPERTY HUB
</h2>

<p>
Buy • Sell • Rent • Invest • Discover
</p>

</div>
""",
unsafe_allow_html=True
)
