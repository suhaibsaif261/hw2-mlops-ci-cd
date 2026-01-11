"""Minimal Flask application for CI/CD demo."""

from flask import Flask, Response


app = Flask(__name__)


@app.route("/health", methods=["GET"])
def health() -> Response:
    """Health check endpoint.

    Returns HTTP 200 with plain text "OK". The app is intended to be
    minimal for local runs and CI/CD smoke tests.
    """
    return Response("OK", status=200, mimetype="text/plain")


if __name__ == "__main__":
    # Expose on all interfaces to allow containerized access during demos
    app.run(host="0.0.0.0", port=5000)
