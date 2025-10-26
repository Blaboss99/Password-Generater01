# 🔐 Password Generator

A powerful and secure Python password generator with strength evaluation.

## 🌟 Features

- **Name-based Password Generation**: Generate strong passwords based on user's name
- **Random Password Generation**: Create completely random secure passwords
- **Password Strength Evaluator**: Analyze and rate password strength
- **Multiple Password Options**: Get 5 different password suggestions
- **Character Substitutions**: Intelligent character replacements for enhanced security

## 📋 Requirements

- Python 3.6 or higher
- No external dependencies (uses only standard library)

## 🚀 Installation

1. Clone or download this repository
2. Navigate to the project directory:
```bash
cd password-generator-project
```

## 💻 Usage

### Basic Usage

Run the script:
```bash
python password_generator.py
```

### Interactive Mode

The program will:
1. Ask for your name
2. Generate 5 strong password options based on your name
3. Show strength ratings for each password
4. Provide a random password alternative
5. Allow you to test password strength

### Example Output

```
============================================================
  STRONG PASSWORD GENERATOR
============================================================

Enter your name to generate a strong password based on it!
Your name: Sarah

============================================================
Generating Strong Passwords for: Sarah
============================================================

Here are 5 strong password options based on 'Sarah':

1. @3r$ah782*X
   Strength: Strong

2. s@4raH926!k
   Strength: Strong

3. $ARah743%p
   Strength: Strong

4. s4@RaH892&x
   Strength: Strong

5. $4r@Ah567*P
   Strength: Strong
```

## 🔧 How It Works

### Name-based Password Generation

The program uses several techniques to create strong passwords:
- **Character Substitutions**: a→@, e→3, i→!, o→0, s→$, t→7
- **Random Numbers**: Adds 3-digit random numbers
- **Special Characters**: Includes symbols like !, @, #, $, %, &, *
- **Random Characters**: Inserts additional random letters
- **Shuffling**: Randomizes character order for unpredictability

### Password Strength Rating

Passwords are evaluated based on:
- Length (8, 12, 16+ characters)
- Character variety (lowercase, uppercase, numbers, symbols)
- Dictionary word detection
- Character repetition penalty

Ratings: Very Weak, Weak, Fair, Strong, Very Strong

## 📁 Project Structure

```
password-generator-project/
│
├── password_generator.py    # Main program file
├── README.md                # This file
├── requirements.txt         # Python dependencies (none required)
└── LICENSE                  # MIT License
```

## 🛡️ Security Features

- Uses cryptographically secure random number generation
- Prevents common weak passwords
- Includes multiple character types
- Randomized character ordering
- No password storage or transmission

## ⚠️ Important Notes

- **Never share your generated passwords**
- **Use a password manager** to store passwords securely
- **Use different passwords** for different accounts
- **Change passwords regularly** for important accounts
- **Enable two-factor authentication** when available

## 🧪 Testing

To test the password generator:
```bash
python password_generator.py
```

Enter different names to see various password generations.

## 📝 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

## 👨‍💻 Author

Created with ❤️ for secure password generation.

## 📧 Contact

For questions or suggestions, please open an issue in the repository.

---

**Happy and Safe Password Generation!** 🔐✨
