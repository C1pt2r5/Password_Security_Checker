import re
import math
import getpass
import sys
from typing import Dict, List, Tuple
import time

class PasswordAnalyzer:
    def __init__(self):
        self.common_passwords = [
            "password", "123456", "password123", "admin", "qwerty", 
            "letmein", "welcome", "monkey", "1234567890", "abc123",
            "password1", "123456789", "welcome123", "admin123", "root",
            "toor", "pass", "test", "guest", "login", "master", "hello",
            "sunshine", "princess", "football", "charlie", "aa123456"
        ]
    
    def check_criteria(self, password: str) -> Dict[str, Dict[str, any]]:
        """Check various password security criteria"""
        criteria = {
            "length_8": {
                "met": len(password) >= 8,
                "label": "Minimum 8 characters",
                "description": "Longer passwords are harder to crack"
            },
            "length_12": {
                "met": len(password) >= 12,
                "label": "12+ characters (recommended)",
                "description": "Significantly increases security"
            },
            "lowercase": {
                "met": bool(re.search(r'[a-z]', password)),
                "label": "Lowercase letters",
                "description": "Include a-z characters"
            },
            "uppercase": {
                "met": bool(re.search(r'[A-Z]', password)),
                "label": "Uppercase letters", 
                "description": "Include A-Z characters"
            },
            "numbers": {
                "met": bool(re.search(r'[0-9]', password)),
                "label": "Numbers",
                "description": "Include 0-9 digits"
            },
            "special_chars": {
                "met": bool(re.search(r'[^a-zA-Z0-9]', password)),
                "label": "Special characters",
                "description": "Include symbols like !@#$%"
            },
            "not_common": {
                "met": password.lower() not in self.common_passwords,
                "label": "Not a common password",
                "description": "Avoid easily guessable passwords"
            },
            "no_repeats": {
                "met": not bool(re.search(r'(.)\1{2,}', password)),
                "label": "No repeated characters",
                "description": "Avoid patterns like 'aaa' or '111'"
            },
            "no_sequences": {
                "met": not bool(re.search(r'123|abc|qwe|asd|zxc', password, re.IGNORECASE)),
                "label": "No sequential patterns",
                "description": "Avoid keyboard patterns"
            }
        }
        return criteria
    
    def calculate_score(self, criteria: Dict) -> int:
        """Calculate password strength score (0-100)"""
        met_criteria = sum(1 for c in criteria.values() if c["met"])
        return min(100, int((met_criteria / len(criteria)) * 100))
    
    def get_strength_level(self, score: int) -> Tuple[str, str]:
        """Get strength level and color based on score"""
        if score >= 80:
            return "Very Strong", "🟢"
        elif score >= 60:
            return "Strong", "🔵"
        elif score >= 40:
            return "Moderate", "🟡"
        elif score >= 20:
            return "Weak", "🟠"
        else:
            return "Very Weak", "🔴"
    
    def estimate_crack_time(self, password: str) -> str:
        """Estimate time to crack password using brute force"""
        if not password:
            return "N/A"
        
        charset_size = 0
        if re.search(r'[a-z]', password):
            charset_size += 26
        if re.search(r'[A-Z]', password):
            charset_size += 26
        if re.search(r'[0-9]', password):
            charset_size += 10
        if re.search(r'[^a-zA-Z0-9]', password):
            charset_size += 32
        
        if charset_size == 0:
            return "Instantly"
        
        combinations = charset_size ** len(password)
        guesses_per_second = 1_000_000_000  # 1 billion guesses per second
        seconds_to_crack = combinations / (2 * guesses_per_second)
        
        if seconds_to_crack < 1:
            return "Instantly"
        elif seconds_to_crack < 60:
            return f"{int(seconds_to_crack)} seconds"
        elif seconds_to_crack < 3600:
            return f"{int(seconds_to_crack / 60)} minutes"
        elif seconds_to_crack < 86400:
            return f"{int(seconds_to_crack / 3600)} hours"
        elif seconds_to_crack < 31536000:
            return f"{int(seconds_to_crack / 86400)} days"
        elif seconds_to_crack < 31536000000:
            return f"{int(seconds_to_crack / 31536000)} years"
        else:
            return "Centuries"
    
    def get_warnings_and_suggestions(self, password: str, criteria: Dict) -> Tuple[List[str], List[str]]:
        """Generate warnings and suggestions based on analysis"""
        warnings = []
        suggestions = []
        
        if len(password) < 8:
            warnings.append("Password is too short")
            suggestions.append("Use at least 8 characters")
        
        if not criteria["lowercase"]["met"]:
            suggestions.append("Add lowercase letters")
        if not criteria["uppercase"]["met"]:
            suggestions.append("Add uppercase letters")
        if not criteria["numbers"]["met"]:
            suggestions.append("Add numbers")
        if not criteria["special_chars"]["met"]:
            suggestions.append("Add special characters")
        
        if password.lower() in self.common_passwords:
            warnings.append("This is a commonly used password")
            suggestions.append("Choose a unique password")
        
        if re.search(r'(.)\1{2,}', password):
            warnings.append("Contains repeated characters")
            suggestions.append("Avoid character repetition")
        
        if re.search(r'123|abc|qwe|asd|zxc', password, re.IGNORECASE):
            warnings.append("Contains keyboard patterns")
            suggestions.append("Avoid sequential patterns")
        
        return warnings, suggestions
    
    def analyze_password(self, password: str) -> Dict:
        """Complete password analysis"""
        criteria = self.check_criteria(password)
        score = self.calculate_score(criteria)
        strength, color_emoji = self.get_strength_level(score)
        crack_time = self.estimate_crack_time(password)
        warnings, suggestions = self.get_warnings_and_suggestions(password, criteria)
        
        return {
            "password": password,
            "score": score,
            "strength": strength,
            "color_emoji": color_emoji,
            "crack_time": crack_time,
            "criteria": criteria,
            "warnings": warnings,
            "suggestions": suggestions
        }

def print_analysis_report(analysis: Dict):
    """Print formatted analysis report"""
    print("\n" + "="*60)
    print("🔐 PASSWORD SECURITY ANALYSIS REPORT")
    print("="*60)
    
    # Overall strength
    print(f"\n📊 OVERALL STRENGTH")
    print(f"   Score: {analysis['score']}/100")
    print(f"   Level: {analysis['color_emoji']} {analysis['strength']}")
    print(f"   Estimated crack time: {analysis['crack_time']}")
    
    # Security criteria
    print(f"\n✅ SECURITY CRITERIA")
    for key, criterion in analysis['criteria'].items():
        status = "✅" if criterion['met'] else "❌"
        print(f"   {status} {criterion['label']}")
        print(f"      {criterion['description']}")
    
    # Warnings
    if analysis['warnings']:
        print(f"\n⚠️  SECURITY WARNINGS")
        for warning in analysis['warnings']:
            print(f"   • {warning}")
    
    # Suggestions
    if analysis['suggestions']:
        print(f"\n💡 IMPROVEMENT SUGGESTIONS")
        for suggestion in analysis['suggestions']:
            print(f"   • {suggestion}")
    
    # Security tips
    print(f"\n🛡️  SECURITY BEST PRACTICES")
    tips = [
        "Use a unique password for each account",
        "Consider using a password manager",
        "Enable two-factor authentication when available",
        "Use passphrases with random words",
        "Avoid personal information in passwords",
        "Update passwords regularly for sensitive accounts"
    ]
    for tip in tips:
        print(f"   • {tip}")
    
    print("\n" + "="*60)

def interactive_mode():
    """Interactive password checking mode"""
    analyzer = PasswordAnalyzer()
    
    print("🔐 Password Security Checker")
    print("="*40)
    print("Enter passwords to analyze their security.")
    print("Type 'quit' or 'exit' to stop.\n")
    
    while True:
        try:
            # Use getpass to hide password input
            password = getpass.getpass("Enter password (hidden): ")
            
            if password.lower() in ['quit', 'exit', '']:
                print("Goodbye! Stay secure! 🛡️")
                break
            
            analysis = analyzer.analyze_password(password)
            print_analysis_report(analysis)
            
            print("\n" + "-"*40)
            
        except KeyboardInterrupt:
            print("\n\nGoodbye! Stay secure! 🛡️")
            break
        except Exception as e:
            print(f"Error: {e}")

def batch_mode(passwords: List[str]):
    """Batch analysis mode for multiple passwords"""
    analyzer = PasswordAnalyzer()
    
    print("🔐 Batch Password Analysis")
    print("="*50)
    
    for i, password in enumerate(passwords, 1):
        print(f"\n📋 Analysis {i}/{len(passwords)}")
        analysis = analyzer.analyze_password(password)
        print_analysis_report(analysis)
        
        if i < len(passwords):
            print("\n" + "="*60)

def demo_mode():
    """Demonstration with sample passwords"""
    sample_passwords = [
        "123456",           # Very weak
        "password",         # Very weak  
        "Password1",        # Weak
        "MyP@ssw0rd",      # Moderate
        "Tr0ub4dor&3",     # Strong
        "correct-horse-battery-staple-2024!", # Very strong
    ]
    
    print("🔐 Password Security Checker - Demo Mode")
    print("="*50)
    print("Analyzing sample passwords to demonstrate the tool...\n")
    
    batch_mode(sample_passwords)

def main():
    """Main function with command line interface"""
    if len(sys.argv) > 1:
        if sys.argv[1] == "--demo":
            demo_mode()
        elif sys.argv[1] == "--help":
            print("🔐 Password Security Checker")
            print("Usage:")
            print("  python password_checker.py           # Interactive mode")
            print("  python password_checker.py --demo    # Demo with sample passwords")
            print("  python password_checker.py --help    # Show this help")
        else:
            print("Unknown option. Use --help for usage information.")
    else:
        interactive_mode()

if __name__ == "__main__":
    main()
