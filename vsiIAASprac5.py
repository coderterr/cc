from flask import Flask, request, jsonify

app = Flask(__name__)
virtual_servers = []
storage_used = 0
total_storage = 100000

@app.route('/create_server', methods=['POST'])
def create_server():
    global storage_used
    data = request.json
    server_name, cpu, ram = data.get('server_name'), int(data.get('cpu')), int(data.get('ram'))

    if not all([server_name, cpu, ram]) or cpu <= 0 or ram <= 0:
        return jsonify({"error": "Invalid data. Server name, CPU, and RAM must be positive."}), 400

    virtual_server = {"name": server_name, "cpu": cpu, "ram": ram}
    virtual_servers.append(virtual_server)
    storage_used += cpu * ram
    return jsonify({"message": "Server created successfully", "server": virtual_server})

@app.route('/list_servers', methods=['GET'])
def list_servers():
    return jsonify({"servers": virtual_servers})

@app.route('/get_storage_status', methods=['GET'])
def get_storage_status():
    return jsonify({"used": storage_used, "total": total_storage})

if __name__ == '__main__':
    app.run(debug=True)