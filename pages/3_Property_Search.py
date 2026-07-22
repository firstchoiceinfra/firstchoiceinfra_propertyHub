import streamlit as st

# ============================================================
# FIRSTCHOICE INFRA PROPERTY HUB
# PAGE 3 - PROPERTY SEARCH & EXPLORE
# PREMIUM MULTICOLOR REAL ESTATE MARKETPLACE
# ============================================================

st.set_page_config(
    page_title="Explore Properties | FirstChoice Property Hub",
    page_icon="🏡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============================================================
# DEMO PROPERTY DATA
# Later this will come from database/API
# ============================================================

properties = [
    {
        "title": "Luxury 3 BHK Premium Residence",
        "city": "Nagpur",
        "locality": "Civil Lines",
        "price": "₹1.25 Cr",
        "area": "2,150 Sq.Ft.",
        "beds": "3 BHK",
        "type": "Apartment",
        "image": "https://images.unsplash.com/photo-1600607687939-ce8a6c25118c?auto=format&fit=crop&w=1200&q=85",
        "badge": "Premium",
        "verified": True
    },
    {
        "title": "Modern Villa with Private Garden",
        "city": "Pune",
        "locality": "Baner",
        "price": "₹2.80 Cr",
        "area": "3,800 Sq.Ft.",
        "beds": "4 BHK",
        "type": "Villa",
        "image": "https://images.unsplash.com/photo-1600585154340-be6161a56a0c?auto=format&fit=crop&w=1200&q=85",
        "badge": "Featured",
        "verified": True
    },
    {
        "title": "Prime Residential Plot",
        "city": "Nagpur",
        "locality": "Wardha Road",
        "price": "₹48 Lakh",
        "area": "1,500 Sq.Ft.",
        "beds": "Plot",
        "type": "Residential Plot",
        "image": "https://images.unsplash.com/photo-1500382017468-9049fed747ef?auto=format&fit=crop&w=1200&q=85",
        "badge": "Hot Deal",
        "verified": True
    },
    {
        "title": "Premium Commercial Office Space",
        "city": "Mumbai",
        "locality": "Andheri",
        "price": "₹3.50 Cr",
        "area": "2,800 Sq.Ft.",
        "beds": "Office",
        "type": "Commercial",
        "image": "https://images.unsplash.com/photo-1497366811353-6870744d04b2?auto=format&fit=crop&w=1200&q=85",
        "badge": "Business",
        "verified": True
    },
    {
        "title": "Luxury Penthouse with City View",
        "city": "Bengaluru",
        "locality": "Whitefield",
        "price": "₹4.25 Cr",
        "area": "4,500 Sq.Ft.",
        "beds": "4 BHK",
        "type": "Penthouse",
        "image": "https://images.unsplash.com/photo-1600607687920-4e2a09cf159d?auto=format&fit=crop&w=1200&q=85",
        "badge": "Luxury",
        "verified": True
    },
    {
        "title": "Green Farm Land Investment",
        "city": "Nashik",
        "locality": "Trimbak Road",
        "price": "₹75 Lakh",
        "area": "2 Acres",
        "beds": "Land",
        "type": "Agricultural",
        "image": "https://images.unsplash.com/photo-1500076656116-558758c991c1?auto=format&fit=crop&w=1200&q=85",
        "badge": "Investment",
        "verified": True
    }
]

# ============================================================
# PREMIUM CSS
# ============================================================

st.markdown("""
<style>

.stApp {
    background:
    linear-gradient(
        135deg,
        #f7f9ff 0%,
        #fff7f4 35%,
        #f7f1ff 70%,
        #effcff 100%
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

/* BRAND */

.brand {
    background:
    linear-gradient(
        135deg,
        #071952,
        #2563EB,
        #7C3AED,
        #EC4899
    );

    padding: 18px 28px;
    border-radius: 20px;

    color: white;

    box-shadow:
    0 15px 35px rgba(37,99,235,0.20);
}

.brand-title {
    font-size: 27px;
    font-weight: 900;
    letter-spacing: 2px;
}

.brand-subtitle {
    font-size: 11px;
    letter-spacing: 4px;
    color: #FDE68A;
}

/* HERO */

.hero {
    margin-top: 25px;

    min-height: 430px;

    border-radius: 32px;

    overflow: hidden;

    position: relative;

    background:
    linear-gradient(
        90deg,
        rgba(7,25,82,0.96),
        rgba(7,25,82,0.72),
        rgba(7,25,82,0.25)
    ),
    url("https://images.unsplash.com/photo-1600607687920-4e2a09cf159d?auto=format&fit=crop&w=1800&q=90");

    background-size: cover;

    background-position: center;

    padding: 65px 55px;

    color: white;

    box-shadow:
    0 25px 60px rgba(7,25,82,0.25);
}

.hero h1 {
    font-size: 48px;
    font-weight: 900;
    max-width: 700px;
}

.hero p {
    font-size: 18px;
    max-width: 650px;
    line-height: 1.7;
}

/* SEARCH */

.search-box {
    background:
    rgba(255,255,255,0.97);

    padding: 22px;

    border-radius: 22px;

    margin-top: 30px;

    box-shadow:
    0 15px 40px rgba(0,0,0,0.15);
}

/* SECTION */

.section-title {
    color: #071952;

    font-size: 30px;

    font-weight: 900;

    margin-top: 45px;
}

.section-subtitle {
    color: #667085;

    margin-bottom: 25px;
}

/* CATEGORY */

.category {
    padding: 25px;

    border-radius: 22px;

    color: white;

    text-align: center;

    min-height: 145px;

    box-shadow:
    0 12px 30px rgba(0,0,0,0.10);
}

.blue {
    background: linear-gradient(135deg,#2563EB,#06B6D4);
}

.purple {
    background: linear-gradient(135deg,#7C3AED,#EC4899);
}

.orange {
    background: linear-gradient(135deg,#F97316,#EF4444);
}

.green {
    background: linear-gradient(135deg,#059669,#22C55E);
}

.gold {
    background: linear-gradient(135deg,#B7791F,#F2C94C);
}

.sky {
    background: linear-gradient(135deg,#0284C7,#38BDF8);
}

.category-icon {
    font-size: 42px;
}

.category-name {
    font-size: 18px;
    font-weight: 900;
}

/* PROPERTY CARD */

.property-card {
    background: white;

    border-radius: 25px;

    overflow: hidden;

    box-shadow:
    0 12px 35px rgba(31,41,55,0.10);

    margin-bottom: 25px;
}

.property-image {
    height: 245px;

    width: 100%;

    object-fit: cover;
}

.property-content {
    padding: 22px;
}

.property-title {
    font-size: 20px;

    font-weight: 900;

    color: #071952;
}

.property-location {
    color: #667085;

    font-size: 14px;
}

.property-price {
    color: #7C3AED;

    font-size: 25px;

    font-weight: 900;
}

.badge {
    display: inline-block;

    padding: 6px 12px;

    border-radius: 20px;

    background:
    linear-gradient(
        135deg,
        #F97316,
        #EC4899
    );

    color: white;

    font-size: 11px;

    font-weight: 900;
}

.verified {
    color: #059669;

    font-weight: 800;

    font-size: 13px;
}

/* AI */

.ai-box {
    background:
    linear-gradient(
        135deg,
        #071952,
        #4C1D95,
        #7C3AED,
        #EC4899
    );

    color: white;

    padding: 45px;

    border-radius: 30px;

    box-shadow:
    0 25px 55px rgba(124,58,237,0.25);
}

/* STATS */

.stat {
    background: white;

    padding: 25px;

    border-radius: 20px;

    text-align: center;

    box-shadow:
    0 10px 30px rgba(0,0,0,0.06);
}

.stat-number {
    font-size: 30px;

    font-weight: 900;

    color: #7C3AED;
}

.stat-label {
    color: #667085;
}

/* FOOTER */

.footer {
    background:
    linear-gradient(
        135deg,
        #071952,
        #1E1B4B
    );

    color: white;

    text-align: center;

    padding: 45px;

    border-radius: 25px;

    margin-top: 60px;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# BRAND
# ============================================================

st.markdown("""
<div class="brand">

<div class="brand-title">
🏠 FIRSTCHOICE INFRA
</div>

<div class="brand-subtitle">
PROPERTY HUB • INDIA'S SMART REAL ESTATE MARKETPLACE
</div>

</div>
""", unsafe_allow_html=True)


# ============================================================
# HERO
# ============================================================

st.markdown("""
<div class="hero">

<h1>
Find a Place You'll Love to Call Home
</h1>

<p>
Explore verified homes, premium villas, commercial spaces,
plots and investment opportunities across India's growing cities.
</p>

</div>
""", unsafe_allow_html=True)


# ============================================================
# SEARCH PANEL
# ============================================================

st.markdown(
    '<div class="search-box">',
    unsafe_allow_html=True
)

s1, s2, s3, s4 = st.columns([1.1, 1.5, 1.5, 1])

with s1:

    purpose = st.selectbox(
        "I Want To",
        [
            "Buy",
            "Rent",
            "Invest"
        ]
    )

with s2:

    city = st.text_input(
        "📍 Location",
        placeholder="City or Locality"
    )

with s3:

    property_type = st.selectbox(
        "🏡 Property Type",
        [
            "All Properties",
            "Apartment",
            "Villa",
            "Plot",
            "Commercial",
            "Agricultural"
        ]
    )

with s4:

    budget = st.selectbox(
        "💰 Budget",
        [
            "Any Budget",
            "Under ₹25 Lakh",
            "₹25 Lakh - ₹50 Lakh",
            "₹50 Lakh - ₹1 Crore",
            "₹1 Crore - ₹5 Crore",
            "₹5 Crore+"
        ]
    )

st.markdown(
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# CATEGORIES
# ============================================================

st.markdown(
    '<div class="section-title">Explore Property Categories</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-subtitle">Discover spaces designed for every lifestyle and investment goal.</div>',
    unsafe_allow_html=True
)

c1,c2,c3,c4,c5,c6 = st.columns(6)

cats = [
    ("🏠","Homes","blue"),
    ("🏢","Commercial","purple"),
    ("🌳","Plots","orange"),
    ("🌾","Agriculture","green"),
    ("🏰","Luxury","gold"),
    ("🏗️","New Projects","sky")
]

for col, cat in zip(
    [c1,c2,c3,c4,c5,c6],
    cats
):

    with col:

        st.markdown(
            f"""
            <div class="category {cat[2]}">

            <div class="category-icon">
            {cat[0]}
            </div>

            <div class="category-name">
            {cat[1]}
            </div>

            </div>
            """,
            unsafe_allow_html=True
        )


# ============================================================
# FILTERS
# ============================================================

st.markdown(
    '<div class="section-title">🔎 Refine Your Search</div>',
    unsafe_allow_html=True
)

f1,f2,f3,f4 = st.columns(4)

with f1:

    verified_only = st.checkbox(
        "🛡️ Verified Properties"
    )

with f2:

    video_only = st.checkbox(
        "🎬 Video Available"
    )

with f3:

    featured_only = st.checkbox(
        "⭐ Featured Listings"
    )

with f4:

    sort_by = st.selectbox(
        "Sort By",
        [
            "Recommended",
            "Newest",
            "Price: Low to High",
            "Price: High to Low"
        ]
    )


# ============================================================
# PROPERTY LISTINGS
# ============================================================

st.markdown(
    '<div class="section-title">🔥 Featured Properties</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-subtitle">Handpicked opportunities from across India.</div>',
    unsafe_allow_html=True
)


# Simple demo filtering

filtered_properties = properties

if city:

    filtered_properties = [
        p for p in properties
        if city.lower() in p["city"].lower()
        or city.lower() in p["locality"].lower()
    ]

if property_type != "All Properties":

    filtered_properties = [
        p for p in filtered_properties
        if property_type.lower()
        in p["type"].lower()
    ]

if verified_only:

    filtered_properties = [
        p for p in filtered_properties
        if p["verified"]
    ]


# ============================================================
# PROPERTY CARDS
# ============================================================

for i in range(
    0,
    len(filtered_properties),
    3
):

    row = filtered_properties[i:i+3]

    cols = st.columns(3)

    for col, prop in zip(
        cols,
        row
    ):

        with col:

            st.markdown(
                f"""
                <div class="property-card">

                <img
                src="{prop['image']}"
                class="property-image"
                >

                <div class="property-content">

                <span class="badge">
                {prop['badge']}
                </span>

                <br><br>

                <div class="property-title">
                {prop['title']}
                </div>

                <div class="property-location">
                📍 {prop['locality']}, {prop['city']}
                </div>

                <br>

                <div class="property-price">
                {prop['price']}
                </div>

                <hr>

                <div>
                📐 {prop['area']}
                &nbsp;&nbsp; | &nbsp;&nbsp;
                🛏️ {prop['beds']}
                </div>

                <br>

                <div class="verified">
                🛡️ Verified Property
                </div>

                </div>

                </div>
                """,
                unsafe_allow_html=True
            )

            b1,b2 = st.columns(2)

            with b1:

                st.button(
                    "❤️ Save",
                    key=f"save_{i}_{prop['title']}",
                    use_container_width=True
                )

            with b2:

                st.button(
                    "👁 View",
                    key=f"view_{i}_{prop['title']}",
                    use_container_width=True
                )


if not filtered_properties:

    st.warning(
        "No properties found. Try another city or property type."
    )


# ============================================================
# AI RECOMMENDATION
# ============================================================

st.markdown("<br>", unsafe_allow_html=True)

st.markdown("""
<div class="ai-box">

<h1>
🤖 Smart Property Recommendations
</h1>

<p>
Tell us what you're looking for and FirstChoice Property Hub
will help you discover properties that match your lifestyle,
budget and investment goals.
</p>

</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

ai1,ai2,ai3 = st.columns(3)

with ai1:

    st.selectbox(
        "Your Preferred City",
        [
            "Nagpur",
            "Mumbai",
            "Pune",
            "Bengaluru",
            "Delhi NCR",
            "Hyderabad"
        ]
    )

with ai2:

    st.selectbox(
        "Your Goal",
        [
            "Dream Home",
            "Investment",
            "Rental Income",
            "Business",
            "Land Investment"
        ]
    )

with ai3:

    st.selectbox(
        "Your Budget",
        [
            "Under ₹25 Lakh",
            "₹25-50 Lakh",
            "₹50 Lakh-1 Crore",
            "₹1-5 Crore",
            "₹5 Crore+"
        ]
    )

if st.button(
    "✨ Find My Perfect Property",
    use_container_width=True
):

    st.success(
        "Your smart property recommendations are being prepared."
    )


# ============================================================
# PROPERTY VIDEO SECTION
# ============================================================

st.markdown(
    '<div class="section-title">🎬 Explore Properties Through Video</div>',
    unsafe_allow_html=True
)

v1,v2 = st.columns(2)

with v1:

    st.video(
        "https://www.youtube.com/watch?v=ScMzIvxBSi4"
    )

with v2:

    st.markdown("""
    <div style="
    background:
    linear-gradient(
        135deg,
        #FCE7F3,
        #E0E7FF,
        #DBEAFE
    );

    padding:45px;

    border-radius:25px;

    min-height:300px;
    ">

    <h2>
    🎥 See More. Feel More. Decide Better.
    </h2>

    <p>
    Property videos help buyers experience spaces
    before scheduling a physical visit.
    </p>

    <p>
    🏡 Virtual Tours
    </p>

    <p>
    🎬 Property Walkthroughs
    </p>

    <p>
    📍 Location Videos
    </p>

    </div>
    """, unsafe_allow_html=True)


# ============================================================
# MARKETPLACE STATS
# ============================================================

st.markdown(
    '<div class="section-title">🇮🇳 India's Growing Property Marketplace</div>',
    unsafe_allow_html=True
)

st1,st2,st3,st4 = st.columns(4)

stats = [
    ("10,000+","Properties"),
    ("100+","Cities"),
    ("5,000+","Verified Users"),
    ("24/7","Property Discovery")
]

for col, stat in zip(
    [st1,st2,st3,st4],
    stats
):

    with col:

        st.markdown(
            f"""
            <div class="stat">

            <div class="stat-number">
            {stat[0]}
            </div>

            <div class="stat-label">
            {stat[1]}
            </div>

            </div>
            """,
            unsafe_allow_html=True
        )


# ============================================================
# FOOTER
# ============================================================

st.markdown("""
<div class="footer">

<h2>
🏠 FIRSTCHOICE INFRA PROPERTY HUB
</h2>

<p>
India's Next-Generation Real Estate Marketplace
</p>

<p>
Buy • Sell • Rent • Invest • Discover
</p>

<hr>

<small>
© FirstChoice Infra Property Hub
</small>

</div>
""", unsafe_allow_html=True)
