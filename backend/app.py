from flask import Flask


app = Flask(__name__)


@app.route("/updateDoctorStatus", methods=["POST"])
def update_doctors_availability():
  return "Words"  

if __name__ == "__main__":
    app.run(debug=True)