from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

# In-memory storage for devices
devices = {}

@app.route('/')
def index():
    return render_template('index.html', devices=devices)

@app.route('/add_device', methods=['POST'])
def add_device():
    device_name = request.form.get('device_name')
    if device_name and device_name not in devices:
        devices[device_name] = {'status': 'off'}
        return jsonify({'success': True, 'devices': devices})
    return jsonify({'success': False, 'error': 'Device already exists or invalid name'})

@app.route('/toggle_device/<device_name>', methods=['POST'])
def toggle_device(device_name):
    if device_name in devices:
        current_status = devices[device_name]['status']
        devices[device_name]['status'] = 'on' if current_status == 'off' else 'off'
        return jsonify({'success': True, 'devices': devices})
    return jsonify({'success': False, 'error': 'Device not found'})

if __name__ == '__main__':
    app.run(debug=True)
