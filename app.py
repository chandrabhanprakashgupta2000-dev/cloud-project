from flask import Flask

# Create a Flask application instance
app = Flask(__name__)

# The route() decorator binds a URL path to a function
@app.route("/")
def hello_world():
    """Renders the 'Hello, World!' message for the home page."""
    return "Hello, World!"

# Optional: Run the application directly when the script is executed
if __name__ == "__main__":
    # Runs the app in debug mode, which automatically reloads on code changes
    app.run(debug=True)
