import subprocess
import time
import webbrowser

def main():
    print("Starting Winston Filter Backend...")
    # Start the FastAPI backend
    backend = subprocess.Popen(["python", "-m", "uvicorn", "main:app", "--reload"])
    
    # Give the backend 3 seconds to boot up
    time.sleep(3)
    
    print("Starting Streamlit Dashboard...")
    # Start the user-friendly Streamlit frontend
    frontend = subprocess.Popen(["python", "-m", "streamlit", "run", "app.py"])
    
    # Automatically open your browser to the Streamlit app
    webbrowser.open("http://localhost:8501")
    
    try:
        backend.wait()
        frontend.wait()
    except KeyboardInterrupt:
        backend.terminate()
        frontend.terminate()

if __name__ == "__main__":
    main()