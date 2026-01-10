import sys
import importlib

def check_package(package_name):
    try:
        importlib.import_module(package_name)
        print(f"✅ {package_name} installed")
        return True
    except ImportError:
        print(f"❌ {package_name} NOT installed")
        return False

def verify_setup():
    print("Verifying AI-C-Suite Setup...\n")
    
    packages = [
        "phi",
        "streamlit",
        "google.generativeai",
        "dotenv",
        "pydantic"
    ]
    
    all_passed = True
    for pkg in packages:
        if not check_package(pkg):
            all_passed = False
            
    print("\n")
    if all_passed:
        print("🎉 All dependencies appear to be installed.")
        print("Next steps:")
        print("1. Copy .env.example to .env and fill in your API keys.")
        print("2. Run 'streamlit run app.py' to start the application.")
    else:
        print("⚠️ Some dependencies are missing. Please run 'pip install -r requirements.txt'")

if __name__ == "__main__":
    verify_setup()

if __name__ == "__main__":
    verify_setup()
