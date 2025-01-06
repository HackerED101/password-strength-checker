import re
import string
import random
import math

# Common weak passwords and dictionary words (can expand this list)
COMMON_PASSWORDS = {
    '123456', 'password', 'qwerty', 'abc123', 'password123', 'letmein', 'welcome', 'admin', 'password1', '123123'
}
# A basic set of dictionary words (can be expanded for better checks)
DICTIONARY_WORDS = {
    'password', 'hello', 'iloveyou', 'welcome', 'sunshine', 'monkey', 'dragon', 'trustno1', 'princess', 'qwerty'
}

def check_password_strength(password):
    # Calculate entropy (randomness) of the password
    entropy = calculate_entropy(password)

    # Criteria for password strength
    criteria = {
        "length": len(password) >= 12,  # Minimum length
        "uppercase": bool(re.search(r'[A-Z]', password)),  # Uppercase letter
        "lowercase": bool(re.search(r'[a-z]', password)),  # Lowercase letter
        "digit": bool(re.search(r'\d', password)),  # Digit
        "special_char": bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password)),  # Special char
        "common_password": password.lower() not in COMMON_PASSWORDS,  # Not a common password
        "dictionary_word": not any(word in password.lower() for word in DICTIONARY_WORDS),  # No dictionary words
        "entropy": entropy >= 3.5  # Entropy threshold for randomness (higher is better)
    }
    
    # Checking each criterion
    strength = True
    missing_criteria = []
    for criterion, met in criteria.items():
        if not met:
            missing_criteria.append(criterion)

    # Strength evaluation
    if not strength or len(missing_criteria) > 0:
        return generate_feedback(missing_criteria, entropy)
    
    return f"Password is strong! Entropy: {entropy:.2f} (higher is better)."

def calculate_entropy(password):
    """Calculate the entropy (randomness) of the password."""
    unique_chars = set(password)
    entropy = len(unique_chars) * math.log2(len(unique_chars))
    return entropy

def generate_feedback(missing_criteria, entropy):
    """Generate feedback for improving the password strength."""
    feedback = []
    
    if "length" in missing_criteria:
        feedback.append("Password should be at least 12 characters long.")
    if "uppercase" in missing_criteria:
        feedback.append("Password should contain at least one uppercase letter.")
    if "lowercase" in missing_criteria:
        feedback.append("Password should contain at least one lowercase letter.")
    if "digit" in missing_criteria:
        feedback.append("Password should contain at least one digit.")
    if "special_char" in missing_criteria:
        feedback.append("Password should contain at least one special character.")
    if "common_password" in missing_criteria:
        feedback.append("Password is too common. Avoid using common passwords.")
    if "dictionary_word" in missing_criteria:
        feedback.append("Password contains a dictionary word. Try to avoid using simple words.")
    if "entropy" in missing_criteria:
        feedback.append(f"Password entropy is low. Consider adding more randomness. Current entropy: {entropy:.2f}.")

    feedback.append("\nTips for improvement:\n- Use a mix of uppercase, lowercase, numbers, and special characters.")
    feedback.append("- Avoid using common words or phrases.\n- Make your password longer (at least 12 characters).")
    
    return "\n".join(feedback)

# Example usage
if __name__ == "__main__":
    password = input("Enter your password: ")
    result = check_password_strength(password)
    print(result)
