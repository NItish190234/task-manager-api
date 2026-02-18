from flask import Flask, jsonify

app = Flask(__name__)

tasks = [
    {"id": 1, "title": "Learn Flask"},
    {"id": 2, "title": "Build API"}
]

@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(tasks)
    
print("Task Manager API Running")

if __name__ == "__main__":
    app.run(debug=True)
