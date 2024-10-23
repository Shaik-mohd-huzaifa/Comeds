from flask import Flask, request, jsonify
from ml_model_training_utilities.model import load_model, load_vectorizer
from ml_model_training_utilities.preprocessing import preprocess_input
from ml_model_training_utilities.Classifier import classify_input
from services.prompt_templates import DBPromptTemplate
from services.llm_services import llm_calling
from producer import TopicProducer


app = Flask(__name__)

# Load pre-trained ML model and vectorizer
model = load_model(
    "./trained_model/model.pkl"
)  # Replace with your actual model filename
vectorizer = load_vectorizer(
    "./trained_model/vectorizer.pkl"
)  # Replace with your actual vectorizer filename


@app.route("/chat", methods=["POST"])
def update_doctors_availability():
    data = request.get_json()

    details = data.get("table_details")
    query = data.get("query")

    cleaned_input = preprocess_input("Update ICU number 13556 to occupied")

    # Classify user intent using the cleaned input
    intent = classify_input(cleaned_input, vectorizer, model)

    if intent == "db":
        template = DBPromptTemplate(details, query)
        response = llm_calling(template)

        return jsonify({"response": response}), 200
    elif intent == "kafka":
        TopicProducer(details["topic"], details["message"])

        return jsonify({"message": "Update Successfully"})
    else:
        response = llm_calling(query)

        return jsonify({"message": response})

if __name__ == "__main__":
    app.run(debug=True)
