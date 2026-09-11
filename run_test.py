from flask import Flask, jsonify
import subprocess
import sys

app = Flask(__name__)


@app.route("/run-test", methods=["GET"])
def run_test():

    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "pytest",
            r"C:\Pytest\test_pytest.py"
        ],
        capture_output=True,
        text=True
    )

    return jsonify({
        "status": "PASS" if result.returncode == 0 else "FAIL",
        "return_code": result.returncode,
        "output": result.stdout,
        "error": result.stderr
    })


if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=5000
    )