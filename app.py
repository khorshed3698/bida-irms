from flask import Flask, render_template_string
import datetime
import platform

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Runner Dashboard</title>
    <style>
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #0f172a; color: #f8fafc; margin: 0; padding: 40px; display: flex; justify-content: center; }
        .card { background: #1e293b; padding: 30px; border-radius: 12px; box-shadow: 0 10px 15px -3px rgba(0,0,0,0.5); width: 100%; max-width: 500px; border: 1px solid #334155; }
        h1 { color: #38bdf8; margin-top: 0; }
        .stat { margin: 15px 0; padding: 10px; background: #0f172a; border-radius: 6px; }
        .label { color: #94a3b8; font-size: 0.85em; text-transform: uppercase; }
        .value { color: #f1f5f9; font-size: 1.1em; font-weight: bold; margin-top: 4px; }
    </style>
</head>
<body>
    <div class="card">
        <h1>🚀 Container Dashboard</h1>
        <div class="stat">
            <div class="label">Server Status</div>
            <div class="value" style="color: #4ade80;">● Online & Dockerized</div>
        </div>
        <div class="stat">
            <div class="label">Python Version</div>
            <div class="value">{{ python_version }}</div>
        </div>
        <div class="stat">
            <div class="label">Server Time</div>
            <div class="value">{{ current_time }}</div>
        </div>
    </div>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(
        HTML_TEMPLATE,
        python_version=platform.python_version(),
        current_time=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S UTC")
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
