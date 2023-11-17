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
# "num_rolls" : int between 1 and 6
@app.route('/api/dice', methods=['POST'])
def post_dice_rolls():
    data = request.get_json()

    if 'num_rolls' not in data:
        return jsonify({'message': 'Cannot find "num_rolls" parameter'}), 400

    num_rolls = data['num_rolls']

    if not isinstance(num_rolls, int) or num_rolls <= 0:
        return jsonify({'message': 'Please input a positive number.'}), 400

    dice_rolls = [random.choice([1, 2, 3, 4, 5, 6]) for _ in range(num_rolls)]

    return jsonify({'dice_rolls': dice_rolls})

if __name__ == '__main__':
    app.run(debug=True)
