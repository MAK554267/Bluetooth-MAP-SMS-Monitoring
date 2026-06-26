from flask import Flask, request, jsonify, render_template_string
from datetime import datetime

app = Flask(__name__)

events = []

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Bluetooth MAP Dashboard</title>
    <meta http-equiv="refresh" content="2">
    <style>
        body{
            font-family:Arial,Helvetica,sans-serif;
            background:#111;
            color:white;
            margin:40px;
        }

        h1{
            color:#ff7b00;
        }

        table{
            width:100%;
            border-collapse:collapse;
            margin-top:20px;
        }

        th,td{
            border:1px solid #333;
            padding:12px;
            text-align:left;
        }

        th{
            background:#ff7b00;
            color:white;
        }

        tr:nth-child(even){
            background:#1d1d1d;
        }

        .status{
            color:#4CAF50;
            margin-bottom:20px;
        }
    </style>
</head>
<body>

<h1>Bluetooth MAP Monitoring Dashboard</h1>

<p class="status">
Server Running...
</p>

<table>
<tr>
<th>Time</th>
<th>Type</th>
<th>Content</th>
</tr>

{% for event in events %}
<tr>
<td>{{event.time}}</td>
<td>{{event.type}}</td>
<td>{{event.content}}</td>
</tr>
{% endfor %}

</table>

</body>
</html>
"""


@app.route("/")
def dashboard():
    return render_template_string(HTML, events=reversed(events))


@app.route("/", methods=["POST"])
def receive():

    data = request.get_json(force=True)

    events.append({
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "type": data.get("type", "Unknown"),
        "content": data.get("content", "")
    })

    print(data)

    return jsonify({"status": "received"})


@app.route("/api/events")
def api_events():
    return jsonify(events)


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=8080,
        debug=True
    )
