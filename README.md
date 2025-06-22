# 🔐 Password Security Checker

A comprehensive password security evaluation tool that analyzes password strength and provides actionable recommendations for improvement. Available as both a web application and Python command-line tool.

## 🌟 Features

### Security Analysis
- **Real-time Strength Evaluation**: Analyzes passwords against 9 security criteria
- **Crack Time Estimation**: Calculates estimated time to crack using brute force
- **Common Password Detection**: Checks against database of frequently used passwords
- **Pattern Recognition**: Identifies keyboard patterns and character repetition
- **Visual Feedback**: Color-coded strength indicators and progress bars

### Privacy & Security
- **Local Analysis**: All password checking happens locally - no data sent to servers
- **Secure Input**: Command-line version uses hidden password input
- **No Storage**: Passwords are never saved or logged

### Multiple Interfaces
- **Web Application**: Interactive React-based interface with modern UI
- **Python Script**: Command-line tool for developers and security professionals
- **Batch Processing**: Analyze multiple passwords simultaneously

## 🚀 Quick Start

### Web Application

1. **Install Dependencies**
   ```bash
   npm install
   ```

2. **Run Development Server**
   ```bash
   npm run dev
   ```

3. **Open Browser**
   Navigate to `http://localhost:3000`

### Python Script

1. **Run Interactive Mode**
   ```bash
   python password_checker.py
   ```

2. **Try Demo Mode**
   ```bash
   python password_checker.py --demo
   ```

3. **View Help**
   ```bash
   python password_checker.py --help
   ```

## 📋 Security Criteria

The tool evaluates passwords against these security requirements:

| Criterion | Description | Weight |
|-----------|-------------|---------|
| **Length (8+ chars)** | Minimum recommended length | ⭐⭐⭐ |
| **Length (12+ chars)** | Strongly recommended length | ⭐⭐⭐⭐ |
| **Lowercase Letters** | Contains a-z characters | ⭐⭐ |
| **Uppercase Letters** | Contains A-Z characters | ⭐⭐ |
| **Numbers** | Contains 0-9 digits | ⭐⭐ |
| **Special Characters** | Contains symbols (!@#$% etc.) | ⭐⭐⭐ |
| **Not Common** | Avoids frequently used passwords | ⭐⭐⭐⭐ |
| **No Repetition** | Avoids repeated characters (aaa, 111) | ⭐⭐ |
| **No Patterns** | Avoids keyboard sequences (123, qwe) | ⭐⭐ |

## 🎯 Strength Levels

| Level | Score Range | Description | Color |
|-------|-------------|-------------|-------|
| **Very Strong** | 80-100 | Excellent security | 🟢 Green |
| **Strong** | 60-79 | Good security | 🔵 Blue |
| **Moderate** | 40-59 | Acceptable security | 🟡 Yellow |
| **Weak** | 20-39 | Poor security | 🟠 Orange |
| **Very Weak** | 0-19 | Unacceptable security | 🔴 Red |

## 💻 Usage Examples

### Interactive Mode
```bash
\$ python password_checker.py
🔐 Password Security Checker
========================================
Enter passwords to analyze their security.
Type 'quit' or 'exit' to stop.

Enter password (hidden): 
```

### Demo Mode Output
```bash
\$ python password_checker.py --demo
🔐 Password Security Checker - Demo Mode
==================================================

📋 Analysis 1/6
============================================================
🔐 PASSWORD SECURITY ANALYSIS REPORT
============================================================

📊 OVERALL STRENGTH
   Score: 11/100
   Level: 🔴 Very Weak
   Estimated crack time: Instantly

✅ SECURITY CRITERIA
   ❌ Minimum 8 characters
      Longer passwords are harder to crack
   ❌ 12+ characters (recommended)
      Significantly increases security
   ❌ Lowercase letters
      Include a-z characters
   ...
```

## 🛡️ Security Best Practices

### Password Creation
- **Use unique passwords** for each account
- **Combine multiple character types** (upper, lower, numbers, symbols)
- **Avoid personal information** (names, birthdays, addresses)
- **Use passphrases** with random words
- **Make it memorable** but unpredictable

### Password Management
- **Use a password manager** to generate and store strong passwords
- **Enable two-factor authentication** whenever possible
- **Update passwords regularly** for sensitive accounts
- **Never share passwords** or write them down insecurely

### Common Mistakes to Avoid
- ❌ Using dictionary words
- ❌ Keyboard patterns (qwerty, 123456)
- ❌ Personal information
- ❌ Short passwords (\< 8 characters)
- ❌ Reusing passwords across sites

## 🔧 Technical Details

### Web Application Stack
- **Framework**: Next.js 15 with App Router
- **UI Components**: shadcn/ui with Tailwind CSS
- **Icons**: Lucide React
- **TypeScript**: Full type safety

### Python Script Dependencies
- **Built-in modules only**: No external dependencies required
- **Python 3.6+**: Compatible with modern Python versions
- **Cross-platform**: Works on Windows, macOS, and Linux

### Algorithm Details
- **Charset Calculation**: Dynamic based on character types used
- **Brute Force Estimation**: Assumes 1 billion guesses per second
- **Pattern Detection**: Regular expressions for common sequences
- **Scoring System**: Weighted criteria with 0-100 scale

## 📁 Project Structure

```
password-security-checker/
├── README.md                    # This file
├── password_checker.py          # Python command-line tool
├── password-strength-checker.tsx # React component
├── app/
│   ├── page.tsx                # Next.js page
│   ├── layout.tsx              # App layout
│   └── globals.css             # Global styles
├── components/
│   └── ui/                     # shadcn/ui components
├── package.json                # Node.js dependencies
└── tailwind.config.ts          # Tailwind configuration
```

## 🤝 Contributing

Contributions are welcome! Here are some ways to help:

### Areas for Improvement
- Add more sophisticated entropy calculations
- Implement additional language support
- Create mobile-responsive enhancements
- Add password breach database checking
- Implement password generation features

### Development Setup
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🔗 Related Resources

### Password Security
- [NIST Password Guidelines](https://pages.nist.gov/800-63-3/)
- [OWASP Authentication Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html)
- [Have I Been Pwned](https://haveibeenpwned.com/)

### Password Managers
- [Bitwarden](https://bitwarden.com/)
- [1Password](https://1password.com/)
- [LastPass](https://www.lastpass.com/)
- [KeePass](https://keepass.info/)

## ⚠️ Disclaimer

This tool is for educational and security assessment purposes. While it provides helpful guidance for password security, it should not be the only method used to evaluate password strength. Always follow your organization's security policies and consider using professional security tools for critical applications.

## 📞 Support

If you encounter issues or have questions:

1. Check the [Issues](https://github.com/your-repo/issues) page
2. Review this README for common solutions
3. Create a new issue with detailed information

---

**Stay secure! 🛡️**
```

This comprehensive README.md file includes:

**📋 Complete Documentation:**
- Feature overview and capabilities
- Installation and usage instructions
- Security criteria and strength levels
- Technical implementation details

**🎯 User-Friendly Sections:**
- Quick start guides for both web and Python versions
- Usage examples with sample output
- Security best practices and tips
- Common mistakes to avoid

**🔧 Developer Information:**
- Project structure and technical stack
- Contributing guidelines
- Algorithm details and dependencies
- Related resources and tools

**📊 Visual Elements:**
- Tables for criteria and strength levels
- Code examples and command snippets
- Emojis for better readability
- Proper markdown formatting

The README follows best practices for open source projects and provides everything users need to understand, install, and use the password security checker effectively [^1].

