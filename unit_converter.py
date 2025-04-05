import streamlit as st

# Function for unit conversion
def convert_units(value, from_unit, to_unit, category):
    conversions = {
        'Length': {
            'Meters': 1, 'Kilometers': 0.001, 'Centimeters': 100, 'Millimeters': 1000, 'Miles': 0.000621371, 'Yards': 1.09361, 'Feet': 3.28084
        },
        'Weight': {
            'Kilograms': 1, 'Grams': 1000, 'Milligrams': 1000000, 'Pounds': 2.20462, 'Ounces': 35.274
        },
        'Temperature': {
            'Celsius': 1, 'Fahrenheit': lambda c: (c * 9/5) + 32, 'Kelvin': lambda c: c + 273.15
        }
    }

    # Convert the value from the original unit to base unit
    if category == 'Temperature':
        base_value = value if from_unit == 'Celsius' else conversions[category][from_unit](value)
    else:
        base_value = value / conversions[category][from_unit]

    # Convert to the desired unit
    if category == 'Temperature' and to_unit != 'Celsius':
        return conversions[category][to_unit](base_value) if to_unit != 'Celsius' else base_value
    return base_value * conversions[category][to_unit]


# Streamlit App layout with custom styling
st.set_page_config(page_title="Unit Converter", page_icon="🔄", layout="centered")

st.title("🔄 **Unit Converter**")

# Adding some description
st.markdown("""
Welcome to the **Unit Converter**! This app allows you to convert between various units of length, weight, and temperature.
Simply input the value, select your units, and hit **Convert** to see the result.
""")

# Select category with icons
category = st.selectbox("Choose Conversion Category", ["Length", "Weight", "Temperature"])

# Define units dynamically based on selected category
if category == "Length":
    units = ['Meters', 'Kilometers', 'Centimeters', 'Millimeters', 'Miles', 'Yards', 'Feet']
    icon = "📏"
elif category == "Weight":
    units = ['Kilograms', 'Grams', 'Milligrams', 'Pounds', 'Ounces']
    icon = "⚖️"
else:
    units = ['Celsius', 'Fahrenheit', 'Kelvin']
    icon = "🌡️"

# Display category icon next to title
st.subheader(f"{icon} **{category} Converter**")

# Input fields for the value to convert
value = st.number_input(f"Enter value in {category}:", min_value=0.0, format="%.2f")

# Select from and to units with tooltips for helpful hints
from_unit = st.selectbox(f"Select {category} From Unit", units, help=f"Choose the unit you are converting from")
to_unit = st.selectbox(f"Select {category} To Unit", units, help=f"Choose the unit you are converting to")

# Displaying the conversion button with custom styling
convert_button = st.button("✨ **Convert**", use_container_width=True)

# Show the result when clicked
if convert_button:
    result = convert_units(value, from_unit, to_unit, category)
    st.write(f"🔄 **{value} {from_unit}** is equal to **{result:.2f} {to_unit}**")

# Footer with a personal touch
st.markdown("---")
st.markdown("Made with ❤️ by [Shaheer Shahzad](https://shaheershahzad.com)")

# Custom styling
st.markdown("""
    <style>
        .css-1d391kg {
            padding: 10px 50px;
            font-size: 20px;
            background-color: #008CBA;
            color: white;
            border-radius: 5px;
        }
        .stButton > button {
            font-size: 18px;
            color: white;
            background-color: #4CAF50;
            border: 1px solid #4CAF50;
            padding: 12px;
            border-radius: 5px;
            transition: 0.3s ease;
        }
        .stButton > button:hover {
            background-color: #45a049;
            border: 1px solid #45a049;
        }
    </style>
""", unsafe_allow_html=True)
