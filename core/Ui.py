import streamlit as st


# ============================================================
# FIRSTCHOICE INFRA PROPERTY HUB
# CORE UI DESIGN SYSTEM
# ============================================================


def load_premium_ui():

    st.markdown(
        """
        <style>

        /* ==================================================
           GLOBAL APPLICATION
        ================================================== */

        .stApp {

            background:
            radial-gradient(
                circle at 10% 10%,
                rgba(99,102,241,0.10),
                transparent 30%
            ),

            radial-gradient(
                circle at 90% 20%,
                rgba(236,72,153,0.10),
                transparent 30%
            ),

            linear-gradient(
                135deg,
                #F8FAFC,
                #EEF2FF,
                #FAF5FF,
                #F0FDFA
            );

        }


        /* ==================================================
           HIDE STREAMLIT DEFAULT UI
        ================================================== */

        header {
            visibility: hidden;
        }

        #MainMenu {
            visibility: hidden;
        }

        footer {
            visibility: hidden;
        }


        /* ==================================================
           SIDEBAR
        ================================================== */

        [data-testid="stSidebar"] {

            background:
            linear-gradient(
                180deg,
                #020617,
                #0F172A,
                #1E1B4B,
                #312E81
            );

            border-right:
            1px solid
            rgba(255,255,255,0.10);

        }


        [data-testid="stSidebar"] * {

            color:
            #FFFFFF !important;

        }


        /* ==================================================
           MAIN HERO
        ================================================== */

        .fc-hero {

            position:
            relative;

            padding:
            55px;

            border-radius:
            38px;

            overflow:
            hidden;

            color:
            white;

            background:

            linear-gradient(
                135deg,
                #020617 0%,
                #172554 35%,
                #4C1D95 70%,
                #9D174D 100%
            );

            box-shadow:

            0 30px 80px
            rgba(30,41,59,0.30);

            margin-bottom:
            35px;

        }


        .fc-hero h1 {

            font-size:
            48px;

            font-weight:
            900;

            letter-spacing:
            -1px;

            margin-bottom:
            12px;

        }


        .fc-hero p {

            font-size:
            19px;

            line-height:
            1.7;

            color:
            rgba(255,255,255,0.88);

        }


        /* ==================================================
           SECTION HEADER
        ================================================== */

        .fc-section {

            padding:
            25px 30px;

            border-radius:
            28px;

            color:
            white;

            background:

            linear-gradient(
                135deg,
                #1E3A8A,
                #4338CA,
                #7E22CE,
                #BE185D
            );

            box-shadow:

            0 18px 45px
            rgba(79,70,229,0.22);

            margin:

            35px 0 25px 0;

        }


        .fc-section h2 {

            margin:
            0;

            font-size:
            30px;

            font-weight:
            900;

        }


        .fc-section p {

            margin-top:
            8px;

            font-size:
            16px;

            opacity:
            0.88;

        }


        /* ==================================================
           PREMIUM CARD
        ================================================== */

        .fc-card {

            padding:
            28px;

            border-radius:
            28px;

            background:

            rgba(
                255,
                255,
                255,
                0.88
            );

            border:
            1px solid
            rgba(148,163,184,0.20);

            box-shadow:

            0 18px 45px
            rgba(15,23,42,0.08);

            backdrop-filter:
            blur(15px);

            margin-bottom:
            20px;

        }


        .fc-card h3 {

            font-size:
            23px;

            font-weight:
            800;

            color:
            #0F172A;

        }


        .fc-card p {

            color:
            #475569;

            line-height:
            1.7;

        }


        /* ==================================================
           PROPERTY CARD
        ================================================== */

        .property-card {

            border-radius:
            30px;

            overflow:
            hidden;

            background:
            white;

            border:
            1px solid
            #E2E8F0;

            box-shadow:

            0 18px 45px
            rgba(15,23,42,0.10);

            transition:
            transform 0.25s ease,
            box-shadow 0.25s ease;

            margin-bottom:
            25px;

        }


        .property-card:hover {

            transform:
            translateY(-7px);

            box-shadow:

            0 28px 60px
            rgba(15,23,42,0.18);

        }


        .property-info {

            padding:
            24px;

        }


        .property-title {

            font-size:
            22px;

            font-weight:
            850;

            color:
            #0F172A;

        }


        .property-location {

            color:
            #64748B;

            margin-top:
            8px;

        }


        .property-price {

            color:
            #047857;

            font-size:
            24px;

            font-weight:
            900;

            margin-top:
            15px;

        }


        /* ==================================================
           STAT CARD
        ================================================== */

        .fc-stat {

            padding:
            25px;

            border-radius:
            25px;

            color:
            white;

            background:

            linear-gradient(
                135deg,
                #0F172A,
                #1E3A8A,
                #4338CA
            );

            box-shadow:

            0 15px 40px
            rgba(30,64,175,0.20);

        }


        .fc-stat-number {

            font-size:
            32px;

            font-weight:
            900;

        }


        .fc-stat-label {

            font-size:
            14px;

            opacity:
            0.80;

        }


        /* ==================================================
           SUCCESS CARD
        ================================================== */

        .fc-success {

            padding:
            28px;

            border-radius:
            28px;

            color:
            white;

            background:

            linear-gradient(
                135deg,
                #047857,
                #059669,
                #10B981
            );

            box-shadow:

            0 20px 50px
            rgba(5,150,105,0.20);

        }


        /* ==================================================
           WARNING CARD
        ================================================== */

        .fc-warning {

            padding:
            28px;

            border-radius:
            28px;

            color:
            white;

            background:

            linear-gradient(
                135deg,
                #B45309,
                #D97706,
                #F59E0B
            );

        }


        /* ==================================================
           DANGER CARD
        ================================================== */

        .fc-danger {

            padding:
            28px;

            border-radius:
            28px;

            color:
            white;

            background:

            linear-gradient(
                135deg,
                #991B1B,
                #DC2626,
                #EF4444
            );

        }


        /* ==================================================
           PREMIUM BUTTONS
        ================================================== */

        .stButton > button {

            border-radius:
            14px;

            border:
            none;

            padding:
            12px 20px;

            font-weight:
            750;

            transition:
            all 0.20s ease;

        }


        .stButton > button:hover {

            transform:
            translateY(-2px);

            box-shadow:

            0 10px 25px
            rgba(37,99,235,0.20);

        }


        /* ==================================================
           INPUT BOXES
        ================================================== */

        input,
        textarea {

            border-radius:
            12px !important;

        }


        /* ==================================================
           FOOTER
        ================================================== */

        .fc-footer {

            margin-top:
            60px;

            padding:
            40px;

            border-radius:
            32px;

            color:
            white;

            text-align:
            center;

            background:

            linear-gradient(
                135deg,
                #020617,
                #1E1B4B,
                #312E81
            );

        }

        </style>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# HERO COMPONENT
# ============================================================

def hero(title, subtitle=""):

    st.markdown(
        f"""
        <div class="fc-hero">

        <h1>
        {title}
        </h1>

        <p>
        {subtitle}
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# SECTION COMPONENT
# ============================================================

def section(title, subtitle=""):

    st.markdown(
        f"""
        <div class="fc-section">

        <h2>
        {title}
        </h2>

        <p>
        {subtitle}
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# CARD COMPONENT
# ============================================================

def card(title, description=""):

    st.markdown(
        f"""
        <div class="fc-card">

        <h3>
        {title}
        </h3>

        <p>
        {description}
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# FOOTER COMPONENT
# ============================================================

def footer():

    st.markdown(
        """
        <div class="fc-footer">

        <h2>
        🏠 FIRSTCHOICE INFRA PROPERTY HUB
        </h2>

        <p>
        Buy • Sell • Rent • Invest • Build • Discover
        </p>

        <p>
        India's Next-Generation Real Estate Ecosystem
        </p>

        <hr>

        <p>
        © FirstChoice Infra Property Hub
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )
