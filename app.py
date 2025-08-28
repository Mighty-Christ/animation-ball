from flask import Flask, render_template
import os

app = Flask(__name__)

# Enable debug mode for automatic reloading
app.config['DEBUG'] = True

@app.route("/")
def home():
    return render_template("first.html")

@app.route("/health")
def health():
    return {"status": "healthy", "message": "Bouncing balls animation is running!"}

if __name__ == "__main__":
    # Run in debug mode with host binding for external access
    app.run(debug=True, host='0.0.0.0', port=5000)
