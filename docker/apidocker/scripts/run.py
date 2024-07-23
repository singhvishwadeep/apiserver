from flask import Flask, jsonify
import platform
import psutil

app = Flask(__name__)

def get_system_info():
    return {
        "platform": platform.system(),
        "platform_version": platform.version(),
        "platform_release": platform.release(),
        "cpu_cores": psutil.cpu_count(logical=False),
        "cpu_logical_processors": psutil.cpu_count(logical=True),
        "memory": psutil.virtual_memory()._asdict()
    }

@app.route('/system_info', methods=['GET'])
def system_info():
    return jsonify(get_system_info())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

