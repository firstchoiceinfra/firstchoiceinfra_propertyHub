import streamlit as st
from datetime import datetime


# ============================================================
# PAGE 25 — PROPERTY COLLABORATION & ENQUIRY HUB
# FIRSTCHOICE INFRA PROPERTY HUB
#
# CONNECTED WITH PAGE 2 — POST PROPERTY
#
# FLOW:
# PAGE 2 — POST PROPERTY
#       ↓
# UNIQUE PROPERTY ID
#       ↓
# ORIGINAL POSTER ID
#       ↓
# PAGE 25 PROPERTY SELECTION
#       ↓
# ORIGINAL POSTER AUTO CONNECTED
#       ↓
# BUYER LIKE / SAVE / INTEREST
#       ↓
# ENQUIRY → ORIGINAL PROPERTY POSTER
#       ↓
# MESSAGE / FOLLOW-UP / SITE VISIT / TASK
# ============================================================


st.set_page_config(
    page_title="Property Collaboration & Enquiry Hub | FirstChoice Property Hub",
    page_icon="💬",
    layout="wide"
)


# ============================================================
# SESSION STATE
# ============================================================

if "property_messages" not in st.session_state:
    st.session_state.property_messages = []


if "property_tasks" not in st.session_state:
    st.session_state.property_tasks = []


if "property_enquiries" not in st.session_state:
    st.session_state.property_enquiries = []


if "property_followups" not in st.session_state:
    st.session_state.property_followups = []


if "property_likes" not in st.session_state:
    st.session_state.property_likes = []


if "property_saved" not in st.session_state:
    st.session_state.property_saved = []


if "property_interests" not in st.session_state:
    st.session_state.property_interests = []


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


.success-card {
    padding: 32px;
    border-radius: 28px;

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
}


.info-card {
    padding: 30px;
    border-radius: 28px;

    color: white;

    background:
    linear-gradient(
        135deg,
        #0369A1,
        #0284C7,
        #06B6D4
    );

    box-shadow:
    0 18px 55px
    rgba(3,105,161,0.22);
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


.enquiry-card {
    padding: 28px;
    border-radius: 26px;

    background:
    linear-gradient(
        135deg,
        #FFFFFF,
        #EFF6FF,
        #F5F3FF
    );

    border-left:
    6px solid #7C3AED;

    box-shadow:
    0 12px 35px
    rgba(0,0,0,0.08);

    margin-bottom: 18px;
}


.poster-card {
    padding: 30px;
    border-radius: 28px;

    color: white;

    background:
    linear-gradient(
        135deg,
        #0F172A,
        #1E40AF,
        #7C3AED
    );

    box-shadow:
    0 18px 55px
    rgba(30,64,175,0.25);
}


.property-card {
    padding: 30px;
    border-radius: 30px;

    color: white;

    background:
    linear-gradient(
        135deg,
        #1E3A8A,
        #2563EB,
        #7C3AED
    );

    box-shadow:
    0 18px 55px
    rgba(37,99,235,0.25);

    margin-bottom: 25px;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# HERO
# ============================================================

st.markdown("""
<div class="hero">

<h1>
💬 Property Collaboration & Enquiry Hub
</h1>

<p>
Every property enquiry stays connected to the original
property poster.
</p>

<p>
❤️ Like • ⭐ Save • 👋 Interest • 📞 Enquiry •
📅 Site Visit • 💬 Chat • ✅ Follow-up • 🤝 Collaboration
</p>

</div>
""", unsafe_allow_html=True)


# ============================================================
# SMART INTRO
# ============================================================

st.markdown("""
<div class="ai-card">

<h2>
🤖 Smart Property Communication Centre
</h2>

<p>
This page is connected with Page 2 — Post Property.
Select a property created in Page 2 and its original
property poster will be automatically connected.
</p>

<p>
The buyer or interested user's interaction will remain
linked with the same Property ID.
</p>

<p>
<strong>
Page 2 Property Post → Unique Property ID →
Original Poster → Buyer Interest → Enquiry →
Communication → Follow-up → Site Visit → Deal
</strong>
</p>

</div>
""", unsafe_allow_html=True)


# ============================================================
# CHECK PAGE 2 PROPERTY DATA
# ============================================================

if "properties" not in st.session_state:

    st.session_state.properties = []


if not st.session_state.properties:

    st.warning(
        "⚠️ अभी Page 2 से कोई property available नहीं है. "
        "पहले Page 2 — Post Property से property publish करें."
    )

    st.stop()


# ============================================================
# PROPERTY SELECTION
# CONNECTED WITH PAGE 2
# ============================================================

st.markdown("""
<div class="section">

<h2>
🏡 Select Property
</h2>

<p>
Page 2 — Post Property से property automatically load होगी.
Property select करते ही Original Property Poster की details
automatically connect हो जाएंगी.
</p>

</div>
""", unsafe_allow_html=True)


property_options = []


for item in st.session_state.properties:

    property_options.append(
        f"{item.get('property_title', 'Untitled Property')} "
        f"| {item.get('property_id', 'No ID')} "
        f"| {item.get('city', '')}, {item.get('locality', '')}"
    )


selected_property_label = st.selectbox(
    "🏠 Select Property",
    property_options
)


selected_index = property_options.index(
    selected_property_label
)


selected_property = st.session_state.properties[
    selected_index
]


# ============================================================
# AUTOMATIC PROPERTY DATA
# ============================================================

property_id = selected_property.get(
    "property_id",
    ""
)


property_name = selected_property.get(
    "property_title",
    "Untitled Property"
)


poster_id = selected_property.get(
    "poster_id",
    ""
)


poster_name = selected_property.get(
    "poster_name",
    ""
)


poster_mobile = selected_property.get(
    "poster_mobile",
    ""
)


poster_role = selected_property.get(
    "poster_role",
    ""
)


# ============================================================
# PROPERTY INFORMATION CARD
# ============================================================

st.markdown(
    f"""
    <div class="property-card">

    <h2>
    🏠 {property_name}
    </h2>

    <p>
    🆔 <strong>Property ID:</strong>
    {property_id}
    </p>

    <p>
    📍 <strong>Location:</strong>
    {selected_property.get("city", "")},
    {selected_property.get("locality", "")},
    {selected_property.get("state", "")}
    </p>

    <p>
    🏘️ <strong>Property Type:</strong>
    {selected_property.get("property_type", "")}
    </p>

    <p>
    🎯 <strong>Purpose:</strong>
    {selected_property.get("purpose", "")}
    </p>

    <p>
    📐 <strong>Area:</strong>
    {selected_property.get("area", 0):,.0f} Sq.Ft.
    </p>

    <p>
    💰 <strong>Expected Price:</strong>
    ₹{selected_property.get("price", 0):,.0f}
    </p>

    <p>
    📊 <strong>Listing Status:</strong>
    {selected_property.get("listing_status", "")}
    </p>

    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# ORIGINAL PROPERTY POSTER
# AUTOMATICALLY CONNECTED FROM PAGE 2
# ============================================================

st.markdown("""
<div class="section">

<h2>
👤 Original Property Poster
</h2>

<p>
This information is automatically loaded from Page 2.
It should not be manually changed here.
</p>

</div>
""", unsafe_allow_html=True)


st.markdown(
    f"""
    <div class="poster-card">

    <h2>
    🔗 Original Poster Automatically Connected
    </h2>

    <p>
    <strong>Property:</strong>
    {property_name}
    </p>

    <p>
    <strong>Property ID:</strong>
    {property_id}
    </p>

    <p>
    <strong>Original Poster ID:</strong>
    {poster_id}
    </p>

    <p>
    <strong>Original Poster:</strong>
    {poster_name if poster_name else "Not Available"}
    </p>

    <p>
    <strong>Poster Role:</strong>
    {poster_role}
    </p>

    <p>
    <strong>Poster Mobile:</strong>
    {poster_mobile if poster_mobile else "Not Available"}
    </p>

    <p>
    📩 All enquiries for this property will remain
    connected to this original property poster.
    </p>

    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# PROPERTY INTERACTION
# ============================================================

st.markdown("""
<div class="section">

<h2>
❤️ Property Interest & Enquiry
</h2>

<p>
Buyer or interested user can interact with the selected property.
All interactions are linked with the Property ID.
</p>

</div>
""", unsafe_allow_html=True)


b1, b2, b3 = st.columns(3)


with b1:

    interested_user = st.text_input(
        "👤 Interested User Name"
    )


with b2:

    interested_mobile = st.text_input(
        "📱 Interested User Mobile",
        max_chars=10
    )


with b3:

    interested_email = st.text_input(
        "✉️ Email"
    )


i1, i2, i3 = st.columns(3)


with i1:

    like_property = st.button(
        "❤️ LIKE PROPERTY",
        use_container_width=True
    )


with i2:

    save_property = st.button(
        "⭐ SAVE PROPERTY",
        use_container_width=True
    )


with i3:

    show_interest = st.button(
        "👋 I'M INTERESTED",
        use_container_width=True
    )


# ============================================================
# LIKE PROPERTY
# ============================================================

if like_property:

    st.session_state.property_likes.append({

        "Property ID":
        property_id,

        "Property":
        property_name,

        "Original Poster ID":
        poster_id,

        "Original Poster":
        poster_name,

        "Interested User":
        interested_user,

        "Mobile":
        interested_mobile,

        "Time":
        datetime.now().strftime(
            "%d-%m-%Y %I:%M %p"
        )

    })

    st.success(
        "❤️ Property liked successfully."
    )


# ============================================================
# SAVE PROPERTY
# ============================================================

if save_property:

    st.session_state.property_saved.append({

        "Property ID":
        property_id,

        "Property":
        property_name,

        "Original Poster ID":
        poster_id,

        "Original Poster":
        poster_name,

        "Saved By":
        interested_user,

        "Mobile":
        interested_mobile,

        "Time":
        datetime.now().strftime(
            "%d-%m-%Y %I:%M %p"
        )

    })

    st.success(
        "⭐ Property saved successfully."
    )


# ============================================================
# SHOW INTEREST
# ============================================================

if show_interest:

    if not interested_user:

        st.warning(
            "⚠️ Please enter Interested User Name."
        )

    elif not interested_mobile:

        st.warning(
            "⚠️ Please enter Interested User Mobile."
        )

    else:

        st.session_state.property_interests.append({

            "Property ID":
            property_id,

            "Property":
            property_name,

            "Original Poster ID":
            poster_id,

            "Original Poster":
            poster_name,

            "Interested User":
            interested_user,

            "Mobile":
            interested_mobile,

            "Email":
            interested_email,

            "Status":
            "New",

            "Created":
            datetime.now().strftime(
                "%d-%m-%Y %I:%M %p"
            )

        })

        st.success(
            "👋 Interest registered successfully."
        )


# ============================================================
# CREATE ENQUIRY
# ============================================================

st.markdown("""
<div class="section">

<h2>
📨 Send Enquiry to Original Property Poster
</h2>

</div>
""", unsafe_allow_html=True)


enquiry_type = st.selectbox(
    "📌 Enquiry Type",
    [
        "General Property Enquiry",
        "Price Enquiry",
        "Request Property Details",
        "Request Call Back",
        "Request WhatsApp Contact",
        "Request Site Visit",
        "Booking Enquiry",
        "Investment Enquiry",
        "Loan / Finance Enquiry"
    ]
)


enquiry_message = st.text_area(
    "💬 Enquiry Message",
    placeholder=
    "Write your enquiry about this property..."
)


if st.button(
    "📨 SEND ENQUIRY TO ORIGINAL PROPERTY POSTER",
    use_container_width=True
):

    if not interested_user:

        st.warning(
            "⚠️ Please enter interested user's name."
        )

    elif not interested_mobile:

        st.warning(
            "⚠️ Please enter interested user's mobile number."
        )

    else:

        new_enquiry = {

            "Property ID":
            property_id,

            "Property":
            property_name,

            "Original Poster ID":
            poster_id,

            "Poster Name":
            poster_name,

            "Poster Role":
            poster_role,

            "Poster Mobile":
            poster_mobile,

            "Interested User":
            interested_user,

            "Interested Mobile":
            interested_mobile,

            "Interested Email":
            interested_email,

            "Enquiry Type":
            enquiry_type,

            "Message":
            enquiry_message,

            "Status":
            "New",

            "Created":
            datetime.now().strftime(
                "%d-%m-%Y %I:%M %p"
            )

        }

        st.session_state.property_enquiries.append(
            new_enquiry
        )

        st.success(
            f"✅ Enquiry successfully connected to "
            f"the original property poster: {poster_name}"
        )

        if poster_mobile:

            st.info(
                f"📱 Enquiry destination: {poster_mobile}"
            )


# ============================================================
# POSTER ENQUIRY DASHBOARD
# ============================================================

st.markdown("""
<div class="section">

<h2>
📥 Property Poster Enquiry Dashboard
</h2>

<p>
Enquiries are filtered by both Property ID and Original Poster ID.
</p>

</div>
""", unsafe_allow_html=True)


poster_enquiries = [

    enquiry

    for enquiry
    in st.session_state.property_enquiries

    if enquiry.get("Property ID")
    == property_id

    and enquiry.get("Original Poster ID")
    == poster_id

]


if poster_enquiries:

    for index, enquiry in enumerate(
        poster_enquiries
    ):

        st.markdown(
            f"""
            <div class="enquiry-card">

            <h3>
            📨 {enquiry["Enquiry Type"]}
            </h3>

            <p>
            <strong>Property:</strong>
            {enquiry["Property"]}
            </p>

            <p>
            <strong>Property ID:</strong>
            {enquiry["Property ID"]}
            </p>

            <p>
            <strong>Original Poster:</strong>
            {enquiry["Poster Name"]}
            </p>

            <p>
            <strong>Interested User:</strong>
            {enquiry["Interested User"]}
            </p>

            <p>
            <strong>Mobile:</strong>
            {enquiry["Interested Mobile"]}
            </p>

            <p>
            <strong>Email:</strong>
            {enquiry["Interested Email"]}
            </p>

            <p>
            <strong>Message:</strong>
            {enquiry["Message"]}
            </p>

            <p>
            <strong>Received:</strong>
            {enquiry["Created"]}
            </p>

            <p>
            <strong>Status:</strong>
            {enquiry["Status"]}
            </p>

            </div>
            """,
            unsafe_allow_html=True
        )


        new_status = st.selectbox(

            "Update Enquiry Status",

            [
                "New",
                "Contacted",
                "Follow-up",
                "Site Visit Scheduled",
                "Negotiation",
                "Booking in Progress",
                "Closed",
                "Not Interested"
            ],

            key=f"enquiry_status_{index}"

        )


        if st.button(
            "🔄 UPDATE ENQUIRY STATUS",
            key=f"update_enquiry_{index}",
            use_container_width=True
        ):

            target_created = enquiry["Created"]

            for item in st.session_state.property_enquiries:

                if (
                    item.get("Property ID")
                    == property_id

                    and item.get("Original Poster ID")
                    == poster_id

                    and item.get("Created")
                    == target_created
                ):

                    item["Status"] = new_status


            st.success(
                "✅ Enquiry status updated."
            )

else:

    st.info(
        "📭 No enquiries received for this property yet."
    )


# ============================================================
# MESSAGE CENTRE
# ============================================================

st.markdown("""
<div class="section">

<h2>
💬 Property Message Centre
</h2>

</div>
""", unsafe_allow_html=True)


message_type = st.selectbox(
    "📌 Message Type",
    [
        "General Enquiry",
        "Property Information",
        "Site Visit",
        "Price Discussion",
        "Document Request",
        "Loan Discussion",
        "Legal Query",
        "Booking Query"
    ]
)


message_text = st.text_area(
    "💬 Write Message",
    placeholder=
    "Type your property-related message..."
)


current_user = st.text_input(
    "👤 Your Name",
    value=interested_user
)


user_role = st.selectbox(
    "👥 Your Role",
    [
        "Buyer",
        "Seller",
        "Builder",
        "Agent",
        "Executive",
        "Legal Consultant",
        "Loan Consultant"
    ]
)


if st.button(
    "📨 SEND PROPERTY MESSAGE",
    use_container_width=True
):

    if not message_text:

        st.warning(
            "⚠️ Please enter a message."
        )

    else:

        st.session_state.property_messages.append({

            "Property ID":
            property_id,

            "Property":
            property_name,

            "Original Poster ID":
            poster_id,

            "Original Poster":
            poster_name,

            "Time":
            datetime.now().strftime(
                "%d-%m-%Y %I:%M %p"
            ),

            "From":
            current_user,

            "Role":
            user_role,

            "Message Type":
            message_type,

            "Message":
            message_text

        })

        st.success(
            "✅ Message added to Property Communication Centre."
        )


# ============================================================
# MESSAGE HISTORY
# ============================================================

property_messages = [

    message

    for message
    in st.session_state.property_messages

    if message.get("Property ID")
    == property_id

]


if property_messages:

    st.markdown("""
    <div class="section">

    <h2>
    🕒 Property Communication History
    </h2>

    </div>
    """, unsafe_allow_html=True)


    st.dataframe(
        property_messages,
        use_container_width=True,
        hide_index=True
    )

else:

    st.info(
        "💬 No property communication history yet."
    )


# ============================================================
# TASK MANAGEMENT
# ============================================================

st.markdown("""
<div class="section">

<h2>
✅ Property Transaction Task Board
</h2>

<p>
Create and track important tasks related to this property.
</p>

</div>
""", unsafe_allow_html=True)


t1, t2 = st.columns(2)


with t1:

    task_title = st.text_input(
        "📌 Task Name",
        placeholder=
        "Example: Collect Sale Agreement"
    )


with t2:

    task_owner = st.text_input(
        "👤 Assigned To"
    )


t3, t4 = st.columns(2)


with t3:

    task_priority = st.selectbox(
        "🚦 Priority",
        [
            "Low",
            "Medium",
            "High",
            "Urgent"
        ]
    )


with t4:

    task_status = st.selectbox(
        "📊 Task Status",
        [
            "Pending",
            "In Progress",
            "Completed"
        ]
    )


if st.button(
    "➕ ADD PROPERTY TASK",
    use_container_width=True
):

    if not task_title:

        st.warning(
            "⚠️ Please enter a task name."
        )

    else:

        st.session_state.property_tasks.append({

            "Property ID":
            property_id,

            "Property":
            property_name,

            "Original Poster ID":
            poster_id,

            "Task":
            task_title,

            "Assigned To":
            task_owner,

            "Priority":
            task_priority,

            "Status":
            task_status,

            "Created":
            datetime.now().strftime(
                "%d-%m-%Y %I:%M %p"
            )

        })

        st.success(
            "✅ Task added successfully."
        )


# ============================================================
# TASK LIST
# ============================================================

property_tasks = [

    task

    for task
    in st.session_state.property_tasks

    if task.get("Property ID")
    == property_id

    and task.get("Original Poster ID")
    == poster_id

]


if property_tasks:

    st.dataframe(
        property_tasks,
        use_container_width=True,
        hide_index=True
    )

else:

    st.info(
        "📌 No tasks created yet."
    )


# ============================================================
# FOLLOW-UP REMINDER
# ============================================================

st.markdown("""
<div class="section">

<h2>
📅 Follow-Up Reminder
</h2>

</div>
""", unsafe_allow_html=True)


r1, r2 = st.columns(2)


with r1:

    reminder_title = st.text_input(
        "🔔 Reminder Title"
    )


with r2:

    reminder_date = st.date_input(
        "📅 Follow-Up Date"
    )


reminder_notes = st.text_area(
    "📝 Reminder Notes"
)


if st.button(
    "🔔 CREATE FOLLOW-UP REMINDER",
    use_container_width=True
):

    st.session_state.property_followups.append({

        "Property ID":
        property_id,

        "Property":
        property_name,

        "Original Poster ID":
        poster_id,

        "Title":
        reminder_title,

        "Date":
        str(reminder_date),

        "Notes":
        reminder_notes,

        "Created":
        datetime.now().strftime(
            "%d-%m-%Y %I:%M %p"
        )

    })

    st.success(
        f"✅ Follow-up reminder created for {reminder_date}."
    )


# ============================================================
# FOLLOW-UP HISTORY
# ============================================================

property_followups = [

    followup

    for followup
    in st.session_state.property_followups

    if followup.get("Property ID")
    == property_id

    and followup.get("Original Poster ID")
    == poster_id

]


if property_followups:

    st.markdown("""
    <div class="section">

    <h2>
    🔔 Follow-Up History
    </h2>

    </div>
    """, unsafe_allow_html=True)


    st.dataframe(
        property_followups,
        use_container_width=True,
        hide_index=True
    )


# ============================================================
# COLLABORATION MEMBERS
# ============================================================

st.markdown("""
<div class="section">

<h2>
👥 Collaboration Members
</h2>

</div>
""", unsafe_allow_html=True)


members = st.multiselect(
    "Select people involved in this property transaction",
    [
        "Buyer",
        "Seller",
        "Builder",
        "Agent",
        "Sales Executive",
        "Legal Consultant",
        "Loan Consultant",
        "Property Manager",
        "Admin"
    ]
)


if members:

    st.markdown(
        f"""
        <div class="info-card">

        <h2>
        👥 Active Collaboration Team
        </h2>

        <p>
        {", ".join(members)}
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# ACTIVITY SUMMARY
# ============================================================

st.markdown("""
<div class="section">

<h2>
📊 Collaboration & Enquiry Activity
</h2>

</div>
""", unsafe_allow_html=True)


property_likes = [

    like

    for like
    in st.session_state.property_likes

    if like.get("Property ID")
    == property_id

]


property_saved = [

    saved

    for saved
    in st.session_state.property_saved

    if saved.get("Property ID")
    == property_id

]


property_interests = [

    interest

    for interest
    in st.session_state.property_interests

    if interest.get("Property ID")
    == property_id

]


m1, m2, m3, m4, m5, m6 = st.columns(6)


with m1:

    st.metric(
        "❤️ Likes",
        len(property_likes)
    )


with m2:

    st.metric(
        "⭐ Saved",
        len(property_saved)
    )


with m3:

    st.metric(
        "👋 Interests",
        len(property_interests)
    )


with m4:

    st.metric(
        "📨 Enquiries",
        len(poster_enquiries)
    )


with m5:

    completed_tasks = len(

        [
            x

            for x
            in property_tasks

            if x.get("Status")
            == "Completed"

        ]

    )

    st.metric(
        "🎯 Completed",
        completed_tasks
    )


with m6:

    st.metric(
        "👥 Members",
        len(members)
    )


# ============================================================
# SMART COLLABORATION WORKFLOW
# ============================================================

st.markdown("""
<div class="ai-card">

<h2>
🚀 Smart Property Collaboration Workflow
</h2>

<p>
❤️ User Likes Property
&nbsp; → &nbsp;
⭐ Saves Property
&nbsp; → &nbsp;
👋 Shows Interest
&nbsp; → &nbsp;
📨 Enquiry Created
</p>

<p>
📨 Enquiry is automatically connected to the
Original Property Poster
&nbsp; → &nbsp;
💬 Communication
&nbsp; → &nbsp;
📅 Follow-up
&nbsp; → &nbsp;
🏠 Site Visit
&nbsp; → &nbsp;
🤝 Negotiation
&nbsp; → &nbsp;
📝 Booking
</p>

<p>
The Property ID remains the permanent connection between
the property, original poster, buyer interest, enquiry,
communication and future transaction activities.
</p>

</div>
""", unsafe_allow_html=True)


# ============================================================
# FINAL NOTICE
# ============================================================

st.markdown("""
<div class="success-card">

<h2>
🏠 One Property — One Original Poster — One Enquiry Destination
</h2>

<p>
The person who originally posts the property on Page 2 remains
the primary property owner/poster record for that Property ID.
All buyer interest, enquiries, communication and follow-ups
remain connected to the same property record.
</p>

<p>
🔗 Page 2 Property ID → Page 25 Collaboration Hub
</p>

</div>
""", unsafe_allow_html=True)
