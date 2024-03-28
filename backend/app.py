from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config["MONGO_URI"] = "mongodb://mongo:27017/userdb"
mongo = PyMongo(app)

@app.route('/api/user', methods=['POST'])
def add_user():
    try:
        user_data = request.get_json()
        # Basic validation
        if not user_data or not isinstance(user_data, dict):
            return jsonify({"error": "Invalid user data"}), 400

        # Insert user data into the database
        inserted_user = mongo.db.users.insert_one(user_data)

        # Response formatting
        response = {
            "message": "User added successfully",
            "user_id": str(inserted_user.inserted_id)  # Convert ObjectId to string
        }
        return jsonify(response), 201

    except Exception as e:
        # Error handling
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
