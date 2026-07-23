import streamlit as st
from datetime import datetime
import uuid


def init_property_store():

    if "properties" not in st.session_state:
        st.session_state.properties = []

    if "property_likes" not in st.session_state:
        st.session_state.property_likes = []

    if "property_interests" not in st.session_state:
        st.session_state.property_interests = []

    if "property_enquiries" not in st.session_state:
        st.session_state.property_enquiries = []

    if "property_messages" not in st.session_state:
        st.session_state.property_messages = []

    if "property_tasks" not in st.session_state:
        st.session_state.property_tasks = []

    if "property_followups" not in st.session_state:
        st.session_state.property_followups = []


def create_property(
    poster_id,
    poster_name,
    poster_mobile,
    poster_role,
    property_title,
    property_type,
    purpose,
    description,
    state,
    city,
    locality,
    pincode,
    address,
    price,
    price_negotiable,
    maintenance,
    amenities,
    contact_options
):

    property_id = "FC-PROP-" + uuid.uuid4().hex[:8].upper()

    property_data = {

        "property_id": property_id,

        "poster_id": poster_id,

        "poster_name": poster_name,

        "poster_mobile": poster_mobile,

        "poster_role": poster_role,

        "property_title": property_title,

        "property_type": property_type,

        "purpose": purpose,

        "description": description,

        "state": state,

        "city": city,

        "locality": locality,

        "pincode": pincode,

        "address": address,

        "price": price,

        "price_negotiable": price_negotiable,

        "maintenance": maintenance,

        "amenities": amenities,

        "contact_options": contact_options,

        "created_at":
        datetime.now().strftime(
            "%d-%m-%Y %I:%M %p"
        )

    }

    st.session_state.properties.append(
        property_data
    )

    return property_id


def get_property(property_id):

    for property in st.session_state.properties:

        if property["property_id"] == property_id:

            return property

    return None


def get_poster_properties(poster_id):

    return [

        property

        for property in st.session_state.properties

        if property["poster_id"] == poster_id

    ]


def add_like(
    property_id,
    user_id,
    user_name
):

    existing = [

        x

        for x in st.session_state.property_likes

        if x["property_id"] == property_id
        and x["user_id"] == user_id

    ]

    if not existing:

        st.session_state.property_likes.append({

            "property_id":
            property_id,

            "user_id":
            user_id,

            "user_name":
            user_name,

            "created_at":
            datetime.now().strftime(
                "%d-%m-%Y %I:%M %p"
            )

        })

        return True

    return False


def add_interest(
    property_id,
    user_id,
    user_name
):

    property_data = get_property(
        property_id
    )

    if not property_data:

        return False

    st.session_state.property_interests.append({

        "property_id":
        property_id,

        "poster_id":
        property_data["poster_id"],

        "poster_name":
        property_data["poster_name"],

        "user_id":
        user_id,

        "user_name":
        user_name,

        "created_at":
        datetime.now().strftime(
            "%d-%m-%Y %I:%M %p"
        )

    })

    return True


def add_enquiry(
    property_id,
    user_id,
    user_name,
    user_mobile,
    message
):

    property_data = get_property(
        property_id
    )

    if not property_data:

        return False

    st.session_state.property_enquiries.append({

        "enquiry_id":
        "ENQ-" +
        uuid.uuid4().hex[:8].upper(),

        "property_id":
        property_id,

        # IMPORTANT
        # Enquiry always goes to
        # original property poster

        "receiver_id":
        property_data["poster_id"],

        "receiver_name":
        property_data["poster_name"],

        "receiver_mobile":
        property_data["poster_mobile"],

        "sender_id":
        user_id,

        "sender_name":
        user_name,

        "sender_mobile":
        user_mobile,

        "message":
        message,

        "status":
        "New",

        "created_at":
        datetime.now().strftime(
            "%d-%m-%Y %I:%M %p"
        )

    })

    return True


def get_poster_enquiries(
    poster_id
):

    return [

        enquiry

        for enquiry
        in st.session_state.property_enquiries

        if enquiry["receiver_id"]
        == poster_id

    ]
