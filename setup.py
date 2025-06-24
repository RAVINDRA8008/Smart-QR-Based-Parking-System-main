#!/usr/bin/env python3
"""
Smart Parking System Setup Script
This script helps you set up and run the Smart Parking System
"""

import os
import subprocess
import sys

def install_dependencies():
    """Install required Python packages"""
    print("📦 Installing dependencies...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Dependencies installed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install dependencies: {e}")
        return False

def check_environment():
    """Check if environment is set up correctly"""
    print("🔍 Checking environment...")
    
    # Check if .env file exists
    if os.path.exists('.env'):
        print("✅ .env file found")
    else:
        print("⚠️  .env file not found (optional for SMS functionality)")
        print("   Copy .env.example to .env and configure Twilio credentials if needed")
    
    # Check Python version
    if sys.version_info >= (3, 8):
        print(f"✅ Python version: {sys.version.split()[0]}")
    else:
        print(f"❌ Python version {sys.version.split()[0]} is too old. Python 3.8+ required.")
        return False
    
    return True

def run_application():
    """Run the Flask application"""
    print("🚀 Starting Smart Parking System...")
    print("📱 Open your browser and go to: http://localhost:5000")
    print("🛑 Press Ctrl+C to stop the server")
    print("-" * 50)
    
    try:
        subprocess.run([sys.executable, "app.py"])
    except KeyboardInterrupt:
        print("\n👋 Smart Parking System stopped.")

def main():
    """Main setup function"""
    print("🅿️  Smart QR-Based Parking System Setup")
    print("=" * 45)
    
    # Check environment
    if not check_environment():
        sys.exit(1)
    
    # Install dependencies
    if not install_dependencies():
        sys.exit(1)
    
    print("\n🎉 Setup completed successfully!")
    print("\nOptions:")
    print("1. Run the application now")
    print("2. Exit (run 'python app.py' later)")
    
    choice = input("\nEnter your choice (1/2): ").strip()
    
    if choice == "1":
        print()
        run_application()
    else:
        print("\n✅ Setup complete! Run 'python app.py' to start the server.")
        print("📚 Check README.md for detailed documentation.")

if __name__ == "__main__":
    main()
