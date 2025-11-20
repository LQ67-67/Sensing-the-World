from flask import Flask, render_template_string
import explorerhat
import time

app = Flask(__name__)

# HTML Template with auto-refresh every 5 seconds
HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Smart Temperature Monitor</title>
    <meta http-equiv="refresh" content="5">
    <style>
        body { font-family: Arial; text-align: center; margin-top: 60px; }
        .temp { font-size: 48px; color: #007acc; }
        .alert { color: red; font-weight: bold; }
    </style>
</head>
<body>
    <h1>🌡️ Smart Temperature Monitor</h1>
    <div class="temp">{{ temp }} °C</div>
    {% if temp > 30 %}
        <p class="alert">Warning: High Temperature!</p>
    {% endif %}
    <p>Auto-refresh every 5 seconds</p>
</body>
</html>
"""

@app.route("/")
def index():
    # 1. Read Analog Value from A1
    analog_value = explorerhat.analog.one.read() [cite: 103]
    
    # 2. Convert to Voltage (Explorer HAT uses 3.3V logic usually, but scaling may vary)
    # Standard formula provided in documentation:
    voltage = analog_value * 3.3 [cite: 104]
    
    # 3. Convert to Celsius
    temp_c = round((voltage - 0.5) * 100, 2) [cite: 105]
    
    # 4. Check Threshold logic
    if temp_c > 30: [cite: 106]
        # Alarm: ON for 1 second
        explorerhat.output.one.on() [cite: 107]
        time.sleep(1)
        explorerhat.output.one.off() [cite: 109]
        
    return render_template_string(HTML, temp=temp_c)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
