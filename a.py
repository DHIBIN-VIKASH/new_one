
from json import dumps
from httplib2 import Http
@app.route('/send-reminder', methods=['POST'])
def send_reminder():
    try:
        """Google Chat incoming webhook quickstart."""
        url = "https://chat.googleapis.com/v1/spaces/AAAA5J899q0/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=XJQteLOq-1fSgRSJYqunAfHimRbe_lDjCVU-ZPT7tAA"
        app_message = {"text": "Hello from a new script!"}
        message_headers = {"Content-Type": "application/json; charset=UTF-8"}
        for i in range(10):
            http_obj = Http()
            response = http_obj.request(
                uri=url,
                method="POST",
                headers=message_headers,
                body=dumps(app_message),
        )
        print('Reminder sent successfully')
        return jsonify({'message': 'Reminder sent successfully'}), 200
    except Exception as e:
        print('Error sending reminder:', str(e))
        return jsonify({'error': 'Error sending reminder'}), 500
    
