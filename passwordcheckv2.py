import re
import time
from termcolor import colored

def check_password_strength(password):
    score = 0

    # Check length
    if len(password) >= 8:
        score += 1
    # Check for presence of lowercase and uppercase letters
    if re.search(r"[a-z]", password) and re.search(r"[A-Z]", password):
        score += 1
    # Check for presence of digits
    if re.search(r"\d", password):
        score += 1
    # Check for presence of special characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1

    # Output password strength
    if score == 0:
        strength = "Terrible"
        color = "red"
    elif score == 1:
        strength = "Bad"
        color = "yellow"
    elif score == 2:
        strength = "Medium"
        color = "blue"
    elif score == 3:
        strength = "Good"
        color = "green"
    else:
        strength = "Excellent"
        color = "cyan"

    print(colored(f"\nPassword Strength: {strength}", color))

def main():
    print(colored("Password Strength Checker", "magenta"))
    print("Enter a password to check its strength:")
    password = input()

    # Simulate loading animation
    print("Checking password strength ", end="", flush=True)
    for _ in range(3):
        for char in ["|", "/", "-", "\\"]:
            print("\b" + char, end="", flush=True)
            time.sleep(0.2)
    print("\b\b\b\b\b", end="", flush=True)  # Clear loading animation

    check_password_strength(password)

if __name__ == "__main__":
    main()

