#!/usr/bin/env python3

# Password Generator and Strength Evaluator
# Usage: Run with Python 3

import random
import re

# List of common passwords to check against
COMMON_WORDS = [
    'password', '123456', 'qwerty', 'letmein', 'welcome', 'admin', 'root',
    'hello', 'monkey', 'dragon', 'football', 'baseball', 'sunshine'
]

def generate_password(length=16):
    """
    Generate a strong random password of specified length
    
    Args:
        length (int): Length of the password to generate (default: 16)
        
    Returns:
        str: A randomly generated password
    """
    lower = 'abcdefghijklmnopqrstuvwxyz'
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    digits = '0123456789'
    symbols = '!@#$%^&*()_+-=[]{}|;:,.<>?'
    all_chars = lower + upper + digits + symbols
    
    # Ensure at least one character from each category
    pwd = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(symbols)
    ]
    
    # Add remaining characters
    for _ in range(length - 4):
        pwd.append(random.choice(all_chars))
    
    # Shuffle the password characters
    random.shuffle(pwd)
    
    return ''.join(pwd)

def generate_password_from_name(name, use_special_chars=True, use_numbers=True):
    """
    Generate a strong password based on a name
    
    Args:
        name (str): The name to base the password on
        use_special_chars (bool): Whether to include special characters
        use_numbers (bool): Whether to include numbers
        
    Returns:
        str: A strong password based on the name
    """
    # Transform the name
    name = name.lower()
    
    # Character substitutions to make it stronger
    substitutions = {
        'a': '@', 'e': '3', 'i': '!', 'o': '0', 's': '$', 't': '7'
    }
    
    # Apply some substitutions (but not all, to add randomness)
    password_parts = []
    for i, char in enumerate(name):
        if char in substitutions and random.choice([True, False]):
            password_parts.append(substitutions[char])
        else:
            password_parts.append(char)
    
    # Add numbers
    if use_numbers:
        password_parts.append(str(random.randint(100, 999)))
    
    # Add special characters
    if use_special_chars:
        special_chars = ['!', '@', '#', '$', '%', '&', '*']
        password_parts.append(random.choice(special_chars))
    
    # Add some random characters for extra security
    all_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for _ in range(2):
        password_parts.insert(random.randint(0, len(password_parts)), random.choice(all_chars))
    
    # Shuffle to add randomness
    random.shuffle(password_parts)
    
    return ''.join(password_parts)

def evaluate_strength(password):
    """
    Evaluate the strength of a password
    
    Args:
        password (str): The password to evaluate
        
    Returns:
        str: A rating of the password strength
    """
    score = 0
    password_length = len(password)
    
    # Length scoring
    if password_length >= 8:
        score += 1
    if password_length >= 12:
        score += 1
    if password_length >= 16:
        score += 1
    
    # Character variety
    if re.search(r'[a-z]', password):
        score += 1
    if re.search(r'[A-Z]', password):
        score += 1
    if re.search(r'[0-9]', password):
        score += 1
    if re.search(r'[^A-Za-z0-9]', password):
        score += 1
    
    # Dictionary check
    lower_pwd = password.lower()
    if any(word in lower_pwd for word in COMMON_WORDS):
        score -= 2
    
    # Repetition penalty
    unique_chars = len(set(password))
    if unique_chars < password_length * 0.5:
        score -= 1
    
    # Final rating
    if score <= 2:
        return 'Very Weak'
    if score <= 4:
        return 'Weak'
    if score <= 6:
        return 'Fair'
    if score <= 8:
        return 'Strong'
    return 'Very Strong'

# Demo usage
if __name__ == "__main__":
    print("=" * 60)
    print("  STRONG PASSWORD GENERATOR")
    print("=" * 60)
    
    # Get user's name
    print("\nEnter your name to generate a strong password based on it!")
    user_name = input("Your name: ").strip()
    
    if user_name:
        print("\n" + "=" * 60)
        print(f"Generating Strong Passwords for: {user_name}")
        print("=" * 60)
        
        # Generate multiple password options
        print(f"\nHere are 5 strong password options based on '{user_name}':\n")
        for i in range(5):
            pwd = generate_password_from_name(user_name)
            strength = evaluate_strength(pwd)
            print(f"{i+1}. {pwd}")
            print(f"   Strength: {strength}\n")
        
        # Ask if user wants a completely random password too
        print("\n" + "=" * 60)
        print("Random Password Generator")
        print("=" * 60)
        pwd = generate_password(18)
        print(f'\nAlternatively, here\'s a completely random password:')
        print(f'Password: {pwd}')
        print(f'Strength: {evaluate_strength(pwd)}')
    
    # Interactive password strength checker
    print("\n" + "=" * 60)
    print("Password Strength Checker")
    print("=" * 60)
    user_pwd = input("\nEnter a password to check (or press Enter to quit): ")
    while user_pwd:
        print(f'Strength: {evaluate_strength(user_pwd)}')
        user_pwd = input("Enter another password (or press Enter to quit): ")