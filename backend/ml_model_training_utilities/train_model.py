# train_model.py

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import classification_report, confusion_matrix
from training_data import train_data
import joblib
import os
import pandas as pd


def preprocess_text(text):
    # Simple text preprocessing (lowercase, remove special characters, etc.)
    return text.lower()


def train_initial_model():
    # Convert to DataFrame
    df = pd.DataFrame(train_data, columns=["text", "label"])

    # Preprocess the text
    df["text"] = df["text"].apply(preprocess_text)

    # Split the dataset into features and labels
    train_x = df["text"]
    train_y = df["label"]

    # Create a TF-IDF Vectorizer with optimized parameters
    vectorizer = TfidfVectorizer(
        ngram_range=(1, 2), max_df=0.85, min_df=2, max_features=5000
    )
    X_vectorized = vectorizer.fit_transform(train_x)

    # Train-test split (80% train, 20% test)
    X_train, X_test, y_train, y_test = train_test_split(
        X_vectorized, train_y, test_size=0.2, random_state=42
    )

    # Train a Random Forest classifier with GridSearch for tuning
    rf_model = RandomForestClassifier(random_state=42)

    # Hyperparameter tuning (can be adjusted based on your requirements)
    param_grid = {
        "n_estimators": [100, 200],
        "max_depth": [10, 20, None],
        "min_samples_split": [2, 5],
        "min_samples_leaf": [1, 2],
    }

    grid_search = GridSearchCV(
        rf_model, param_grid, cv=5, scoring="accuracy", verbose=2, n_jobs=-1
    )
    grid_search.fit(X_train, y_train)

    # Best model from Grid Search
    best_model = grid_search.best_estimator_

    # Test the model
    y_pred = best_model.predict(X_test)

    # Evaluate the model
    print("Classification Report:\n", classification_report(y_test, y_pred))
    print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))

    # Save the model and vectorizer
    joblib.dump(best_model, "./../trained_model/model.pkl")
    joblib.dump(vectorizer, "./../trained_model/vectorizer.pkl")


# No Need to calling this function because the model is already trained on training dataset
train_initial_model()


# Function to update the model with new data
# Function to update the model with new data
def update_model(new_query, new_label):
    # Load the pre-trained model and vectorizer
    model_path = "./../trained_model/model.pkl"
    vectorizer_path = "./../trained_model/vectorizer.pkl"

    if os.path.exists(model_path) and os.path.exists(vectorizer_path):
        model = joblib.load(model_path)
        vectorizer = joblib.load(vectorizer_path)
    else:
        print("Model or vectorizer not found. Please train the initial model first.")
        return

    # Vectorize the new query
    new_query_vectorized = vectorizer.transform([new_query])

    # Assuming 'train_data' is maintained persistently
    train_x = [text for text, label in train_data]
    train_y = [label for text, label in train_data]

    # Append the new data to the current dataset
    train_x.append(new_query)
    train_y.append(new_label)

    # Retrain the model with the updated data
    X_vectorized = vectorizer.fit_transform(train_x)
    model.fit(X_vectorized, train_y)

    # Save the updated model and vectorizer
    joblib.dump(model, model_path)
    joblib.dump(vectorizer, vectorizer_path)
    print("New Query Updated")
