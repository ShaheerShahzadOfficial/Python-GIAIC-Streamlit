import random
import string
import re
import streamlit as st


# Function to check password strength
def check_password_strength(password):
    score = 0
    feedback = []

    # Length Check (weight: 1)
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")

    # Upper & Lowercase Check (weight: 1)
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include both uppercase and lowercase letters.")

    # Digit Check (weight: 1)
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9).")

    # Special Character Check (weight: 2)
    if re.search(r"[!@#$%^&*]", password):
        score += 2
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&*).")

    # Common Password Check
    if check_common_password(password):
        return

    # Strength Rating
    if score == 5:
        feedback.append("✅ Strong Password!")
    elif score == 4:
        feedback.append("⚠️ Moderate Password - Consider adding more security features.")
    else:
        feedback.append("❌ Weak Password - Improve it using the suggestions above.")

    # Display the feedback
    for line in feedback:
        st.write(line)


# Function to generate a strong password
def generate_password():

    length = random.randint(
        12, 16
    )  # Strong passwords should be between 12-16 characters.
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    password = "".join(random.choice(characters) for i in range(length))
    return password


# Function to check if the password is in the common password list
def check_common_password(password):
    common_passwords = [
        "password123",
        "123456",
        "qwerty",
        "letmein",
        "admin",
        "welcome",
    ]

    if password.lower() in common_passwords:
        st.write("❌ This password is too common. Please choose a stronger one.")
        return True
    return False


# Main Streamlit Interface
def main():
    st.set_page_config(page_title="Password Strength Checker", page_icon="🔒", layout="centered")

    st.title("🔒 **Password Strength Checker**")

    # Password Input
    password = st.text_input("Enter your password:", type="password")

    if password:
        # Check Password Strength
        check_password_strength(password)

    # Password Generator Section
    if st.button("Generate Strong Password"):
        strong_password = generate_password()
        st.write(f"Suggested Strong Password: {strong_password}")


if __name__ == "__main__":
    main()

# Footer with a personal touch
st.markdown("---")
st.markdown("Made with ❤️ by [Shaheer Shahzad](https://shaheershahzad.com)")

