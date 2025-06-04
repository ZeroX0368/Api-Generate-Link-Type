


from flask import Flask, request, jsonify
import string
import random

app = Flask(__name__)

def generate_random_hwid_fluxus(length=96):
    letters_and_digits = string.ascii_lowercase + string.digits
    return ''.join(random.choice(letters_and_digits) for _ in range(length))

def generate_random_hwid_arceus(length=18):
    letters_and_digits = string.ascii_lowercase + string.digits
    return ''.join(random.choice(letters_and_digits) for _ in range(length))

def generate_random_id_delta(length=64):
    letters_and_digits = string.ascii_lowercase + string.digits
    return ''.join(random.choice(letters_and_digits) for _ in range(length))

def generate_random_id_deltaios(length=64):
    letters_and_digits = string.ascii_lowercase + string.digits
    return ''.join(random.choice(letters_and_digits) for _ in range(length))

def generate_random_id_cryptic(length=64):
    letters_and_digits = string.ascii_lowercase + string.digits
    return ''.join(random.choice(letters_and_digits) for _ in range(length))

def generate_random_id_hydrogen(length=10):
    digits = string.digits
    return ''.join(random.choice(digits) for _ in range(length))

def generate_random_hwid_vegax():
    parts = []
    for _ in range(5):
        part_length = random.choice([8, 7])
        part = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(part_length))
        parts.append(part)
    return '-'.join(parts)

def generate_random_hwid_trigonevo():
    return '{}-{}-{}-{}-{}'.format(
        ''.join(random.choices(string.ascii_lowercase + string.digits, k=8)),
        ''.join(random.choices(string.ascii_lowercase + string.digits, k=4)),
        ''.join(random.choices(string.ascii_lowercase + string.digits, k=4)),
        ''.join(random.choices(string.ascii_lowercase + string.digits, k=4)),
        ''.join(random.choices(string.ascii_lowercase + string.digits, k=12))
    )

def generate_random_id_cacti(length=64):
    letters_and_digits = string.ascii_lowercase + string.digits
    return ''.join(random.choice(letters_and_digits) for _ in range(length))

def generate_random_hwid_evon():
    return '{}-{}-{}-{}-{}'.format(
        ''.join(random.choices(string.ascii_lowercase + string.digits, k=8)),
        ''.join(random.choices(string.ascii_lowercase + string.digits, k=4)),
        ''.join(random.choices(string.ascii_lowercase + string.digits, k=4)),
        ''.join(random.choices(string.ascii_lowercase + string.digits, k=4)),
        ''.join(random.choices(string.ascii_lowercase + string.digits, k=12))
    )

@app.route('/api/gen', methods=['GET'])
def generate_link():
    service = request.args.get('type')

    if service:
        if service == 'fluxus':
            random_hwid = generate_random_hwid_fluxus()
            result = f"https://flux.li/android/external/start.php?HWID={random_hwid}"
        elif service == 'arceus':
            random_hwid = generate_random_hwid_arceus()
            result = f"https://spdmteam.com/key-system-1?hwid={random_hwid}&zone=Europe/Rome&os=android"
        elif service == 'delta':
            random_id = generate_random_id_delta()
            result = f"https://gateway.platoboost.com/a/8?id={random_id}"
        elif service == 'deltaios':
            random_id = generate_random_id_deltaios()
            result = f"https://gateway.platoboost.com/a/2?id={random_id}"
        elif service == 'cryptic':
            random_id = generate_random_id_cryptic()
            result = f"https://gateway.platoboost.com/a/39097?id={random_id}"
        elif service == 'hydrogen':
            random_id = generate_random_id_hydrogen()
            result = f"https://gateway.platoboost.com/a/2569?id={random_id}"
        elif service == 'vegax':
            random_hwid = generate_random_hwid_vegax()
            result = f"https://pandadevelopment.net/getkey?service=vegax&hwid={random_hwid}&provider=linkvertise"
        elif service == 'trigon':
            random_hwid = generate_random_hwid_trigonevo()
            result = f"https://trigonevo.fun/whitelist/?HWID={random_hwid}"
        elif service == 'cacti':
            random_id = generate_random_id_cacti()
            result = f"https://gateway.platoboost.com/a/23344?id={random_id}"
        elif service == 'evon':
            random_hwid = generate_random_hwid_evon()
            result = f"https://pandadevelopment.net/getkey?service=evon&hwid={random_hwid}"
        else:
            return jsonify({"result": "Failed to generate key, service not found"}), 400

        return jsonify({"result": result})
    else:
        return jsonify({"result": "Failed to generate key, service not found"}), 400

@app.route('/')
def home():
    return "API is running! Use /api/gen?type=<service> to generate links."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
