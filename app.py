from flask import Flask, jsonify, request
import random


app = Flask(__name__)

#route to get the random dice roll for a specified die
@app.route('/api/dice/<die_type>', methods=['GET'])
def get_die_roll(die_type):
    #available dice types
    valid_die_types = ['d4', 'd6', 'd8', 'd10', 'd12', 'd20']

    #to check if the die is valid
    if die_type not in valid_die_types:
        return jsonify({'message': f'Invalid die type. Valid types are the ff: {", ".join(valid_die_types)}'}), 400

    
    if die_type == 'd4':
        die_faces = [1, 2, 3, 4]
    elif die_type == 'd6':
        die_faces = [1, 2, 3, 4, 5, 6]
    elif die_type == 'd8':
        die_faces = [1, 2, 3, 4, 5, 6, 7, 8]
    elif die_type == 'd10':
        die_faces = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    elif die_type == 'd12':
        die_faces = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    elif die_type == 'd20':
        die_faces = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

    random_roll = random.choice(die_faces)

    return jsonify({'die_type': die_type, 'die_roll': random_roll})

#route to post number of specified dice rolled
# "num_rolls" : int between 1 and 6
@app.route('/api/dice/<die_type>', methods=['POST'])
def post_die_rolls(die_type):
    data = request.get_json()

    #to check if the die is valid
    valid_die_types = ['d4', 'd6', 'd8', 'd10', 'd12', 'd20']
    if die_type not in valid_die_types:
        return jsonify({'message': f'Invalid die type. Valid types: {", ".join(valid_die_types)}'}), 400

    if die_type == 'd4':
        die_faces = [1, 2, 3, 4]
    elif die_type == 'd6':
        die_faces = [1, 2, 3, 4, 5, 6]
    elif die_type == 'd8':
        die_faces = [1, 2, 3, 4, 5, 6, 7, 8]
    elif die_type == 'd10':
        die_faces = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    elif die_type == 'd12':
        die_faces = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    elif die_type == 'd20':
        die_faces = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

    #check if proper request body is sent
    if 'num_rolls' not in data:
        return jsonify({'message': 'Cannot find "num_rolls" request body parameter'}), 400

    num_rolls = data['num_rolls']

    if not isinstance(num_rolls, int) or num_rolls <= 0:
        return jsonify({'message': 'Invalid num_rolls value. It should be a positive integer.'}), 400

    #show the random dice rolls in list
    dice_rolls = [random.choice(die_faces) for _ in range(num_rolls)]

    return jsonify({'die_type': die_type, 'dice_rolls': dice_rolls})

if __name__ == '__main__':
    app.run(debug=True)
