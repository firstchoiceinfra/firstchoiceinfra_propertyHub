import streamlit as st

# ============================================================
# PAGE 19 — VIRTUAL PROPERTY TOUR & 360° EXPERIENCE
# FIRSTCHOICE INFRA PROPERTY HUB
# ============================================================

st.set_page_config(
    page_title="Virtual Property Tour | FirstChoice Property Hub",
    page_icon="🥽",
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

/* TOUR CARD */

.tour-card {
    padding: 32px;
    border-radius: 30px;

    background:
    linear-gradient(
        135deg,
        #FFFFFF,
        #F5F3FF,
        #EFF6FF
    );

    border: 1px solid #E0E7FF;

    box-shadow:
    0 15px 45px
    rgba(0,0,0,0.08);

    margin-bottom: 25px;
}

/* VR CARD */

.vr-card {
    padding: 42px;
    border-radius: 34px;

    color: white;
    text-align: center;

    background:
    linear-gradient(
        135deg,
        #312E81,
        #7C3AED,
        #C026D3
    );

    box-shadow:
    0 22px 65px
    rgba(124,58,237,0.30);

    margin-bottom: 30px;
}

/* FEATURE */

.feature-card {
    padding: 28px;
    border-radius: 26px;

    background: white;

    border: 1px solid #E5E7EB;

    box-shadow:
    0 12px 35px
    rgba(0,0,0,0.07);

    min-height: 190px;
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
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# HERO
# ============================================================

st.markdown("""
<div class="hero">

<h1>
🥽 Virtual Property Tour
</h1>

<p>
Experience properties remotely with immersive photos,
videos, floor plans and future-ready 360° virtual tours.
</p>

<p>
🎥 Video Tour • 📸 Gallery • 🥽 360° View • 🗺️ Floor Plan • 📍 Location
</p>

</div>
""", unsafe_allow_html=True)


# ============================================================
# PROPERTY SELECTOR
# ============================================================

st.markdown("""
<div class="section">

<h2>
🏡 Select Your Property Experience
</h2>

<p>
Choose a property and explore its digital presentation.
</p>

</div>
""", unsafe_allow_html=True)


property_name = st.selectbox(
    "Select Property",
    [
        "Luxury 3 BHK Skyline Apartment",
        "Premium 4 BHK Garden Villa",
        "Modern 2 BHK Smart Home",
        "Mihan Investment Apartment",
        "Luxury Wardha Road Villa"
    ]
)


# ============================================================
# VIRTUAL EXPERIENCE
# ============================================================

st.markdown("""
<div class="vr-card">

<h1>
🥽 IMMERSIVE PROPERTY EXPERIENCE
</h1>

<p>
Walk through the property virtually from anywhere in the world.
</p>

<p>
This interface is ready for integration with
360° panoramas, Matterport-style tours and interactive
property walkthrough technology.
</p>

</div>
""", unsafe_allow_html=True)


# ============================================================
# MEDIA OPTIONS
# ============================================================

st.markdown("""
<div class="section">

<h2>
🎬 Explore Property Media
</h2>

</div>
""", unsafe_allow_html=True)


media_type = st.radio(
    "Choose Experience",
    [
        "🎥 Property Video",
        "📸 Photo Gallery",
        "🥽 360° Virtual Tour",
        "🗺️ Floor Plan",
        "📍 Location View"
    ],
    horizontal=True
)


# ============================================================
# VIDEO TOUR
# ============================================================

if media_type == "🎥 Property Video":

    st.markdown(
        """
        <div class="tour-card">

        <h2>
        🎬 Cinematic Property Video
        </h2>

        <p>
        Showcase the property with a professional cinematic
        walkthrough video.
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )

    video_url = st.text_input(
        "🎥 Paste Property Video URL",
        placeholder="Paste YouTube or supported video URL"
    )

    if video_url:

        st.video(
            video_url
        )

    else:

        st.info(
            "Add a property video URL to display the video tour."
        )


# ============================================================
# PHOTO GALLERY
# ============================================================

elif media_type == "📸 Photo Gallery":

    st.markdown(
        """
        <div class="tour-card">

        <h2>
        📸 Premium Property Gallery
        </h2>

        <p>
        Display high-quality images of interiors,
        exteriors, amenities and surroundings.
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )

    uploaded_images = st.file_uploader(
        "Upload Property Images",
        type=[
            "jpg",
            "jpeg",
            "png",
            "webp"
        ],
        accept_multiple_files=True
    )


    if uploaded_images:

        st.image(
            uploaded_images,
            caption=[
                f"{property_name} — View {i + 1}"
                for i in range(
                    len(uploaded_images)
                )
            ],
            use_container_width=True
        )

    else:

        st.info(
            "Upload property images to create the premium gallery."
        )


# ============================================================
# 360 TOUR
# ============================================================

elif media_type == "🥽 360° Virtual Tour":

    st.markdown(
        """
        <div class="vr-card">

        <h2>
        🥽 360° Virtual Property Experience
        </h2>

        <p>
        The future version of Property Hub can connect
        interactive 360° property tours.
        </p>

        <p>
        Users will be able to move through rooms,
        explore interiors and experience properties remotely.
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )


    tour_url = st.text_input(
        "🔗 360° Tour Embed / URL",
        placeholder="Paste your 360° tour URL"
    )


    if tour_url:

        st.components.v1.iframe(
            tour_url,
            height=600,
            scrolling=True
        )

    else:

        st.info(
            "Add a supported 360° tour URL to display the immersive experience."
        )


# ============================================================
# FLOOR PLAN
# ============================================================

elif media_type == "🗺️ Floor Plan":

    st.markdown(
        """
        <div class="tour-card">

        <h2>
        🗺️ Interactive Floor Plan
        </h2>

        <p>
        Help buyers understand room layouts,
        dimensions and property flow before visiting.
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )


    floor_plan = st.file_uploader(
        "Upload Floor Plan",
        type=[
            "jpg",
            "jpeg",
            "png",
            "pdf"
        ]
    )


    if floor_plan:

        if floor_plan.type != "application/pdf":

            st.image(
                floor_plan,
                use_container_width=True
            )

        else:

            st.success(
                "📄 Floor plan PDF uploaded successfully."
            )

    else:

        st.info(
            "Upload a property floor plan to display it here."
        )


# ============================================================
# LOCATION VIEW
# ============================================================

elif media_type == "📍 Location View":

    st.markdown(
        """
        <div class="tour-card">

        <h2>
        📍 Property Location Intelligence
        </h2>

        <p>
        Show buyers the surrounding neighbourhood,
        roads, transport, schools, hospitals and amenities.
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )


    location_url = st.text_input(
        "🗺️ Map URL",
        placeholder="Paste supported map embed URL"
    )


    if location_url:

        st.components.v1.iframe(
            location_url,
            height=500,
            scrolling=True
        )

    else:

        st.info(
            "Add a supported map URL to display the location."
        )


# ============================================================
# PROPERTY HIGHLIGHTS
# ============================================================

st.markdown("""
<div class="section">

<h2>
✨ Property Highlights
</h2>

</div>
""", unsafe_allow_html=True)


f1, f2, f3, f4 = st.columns(4)


with f1:

    st.markdown("""
    <div class="feature-card">

    <h2>🎥</h2>

    <h3>
    HD Video
    </h3>

    <p>
    Professional cinematic property walkthroughs.
    </p>

    </div>
    """, unsafe_allow_html=True)


with f2:

    st.markdown("""
    <div class="feature-card">

    <h2>🥽</h2>

    <h3>
    360° Tour
    </h3>

    <p>
    Immersive digital property exploration.
    </p>

    </div>
    """, unsafe_allow_html=True)


with f3:

    st.markdown("""
    <div class="feature-card">

    <h2>📸</h2>

    <h3>
    HD Gallery
    </h3>

    <p>
    High-quality property photography.
    </p>

    </div>
    """, unsafe_allow_html=True)


with f4:

    st.markdown("""
    <div class="feature-card">

    <h2>🗺️</h2>

    <h3>
    Floor Plan
    </h3>

    <p>
    Understand property layout before visiting.
    </p>

    </div>
    """, unsafe_allow_html=True)


# ============================================================
# REMOTE PROPERTY VISIT
# ============================================================

st.markdown("""
<div class="section">

<h2>
🌍 Remote Property Discovery
</h2>

<p>
Explore properties remotely before scheduling a physical visit.
</p>

</div>
""", unsafe_allow_html=True)


r1, r2, r3 = st.columns(3)


with r1:

    st.markdown("""
    <div class="feature-card">

    <h3>
    🌎 Anywhere Access
    </h3>

    <p>
    Explore properties from any location.
    </p>

    </div>
    """, unsafe_allow_html=True)


with r2:

    st.markdown("""
    <div class="feature-card">

    <h3>
    ⏱️ Save Time
    </h3>

    <p>
    Shortlist properties before travelling.
    </p>

    </div>
    """, unsafe_allow_html=True)


with r3:

    st.markdown("""
    <div class="feature-card">

    <h3>
    👨‍👩‍👧 Share With Family
    </h3>

    <p>
    Share the digital tour with family members.
    </p>

    </div>
    """, unsafe_allow_html=True)


# ============================================================
# CTA
# ============================================================

st.markdown("""
<div class="cta">

<h2>
📅 Ready For A Physical Visit?
</h2>

<p>
After exploring the property digitally,
schedule a site visit with our property team.
</p>

</div>
""", unsafe_allow_html=True)


if st.button(
    "📅 SCHEDULE PROPERTY VISIT",
    use_container_width=True
):

    st.success(
        f"Your site visit request for {property_name} has been initiated."
    )


# ============================================================
# FUTURE TECHNOLOGY
# ============================================================

st.markdown("""
<div class="ai-card">

<h2>
🚀 Future Immersive Property Technology
</h2>

<p>
Our long-term vision is to bring advanced digital property
experiences to FirstChoice Property Hub.
</p>

<p>
🥽 VR Property Tours
&nbsp; • &nbsp;
📱 AR Furniture Preview
&nbsp; • &nbsp;
🤖 AI Virtual Property Guide
&nbsp; • &nbsp;
🗺️ Interactive Maps
&nbsp; • &nbsp;
🎥 Live Video Walkthrough
</p>

<p>
Buyers will be able to experience properties digitally
before deciding to visit them physically.
</p>

</div>
""", unsafe_allow_html=True)


# ============================================================
# DISCLAIMER
# ============================================================

st.warning(
    "⚠️ Virtual tours, images and videos are for property discovery "
    "and presentation purposes. Users should physically inspect "
    "the property and independently verify all relevant information "
    "before making a transaction."
)
