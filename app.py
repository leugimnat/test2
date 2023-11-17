from flask import Flask, jsonify, request
import random

app = Flask(__name__)

#route to get the random dice roll
@app.route('/api/dice', methods=['GET'])
def get_dice_roll():
    dice_faces = [1, 2, 3, 4, 5, 6]
    random_roll = random.choice(dice_faces)
    return jsonify({'dice_roll': random_roll})

#route to post number of dice rolled
# "custom_roll" : int between 1 and 6
@app.route('/api/dice', methods=['POST'])
def post_dice_roll():
    data = request.get_json()

    if 'custom_roll' not in data:
        return jsonify({'message': 'Cannot find "custom_roll" request body parameter'}), 400

    custom_roll = data['custom_roll']
    
    if not isinstance(custom_roll, int) or custom_roll < 1 or custom_roll > 6:
        return jsonify({'message': 'Invalid custom_roll value. It should be a number  equal or between 1 and 6.'}), 400

    return jsonify({'custom_roll': custom_roll})

if __name__ == '__main__':
    app.run(debug=True)
