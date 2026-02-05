import joblib
from app.utils.embedding_function import get_embedding
import os

def Check_Answer(question):
    BASE_RIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    model_path = os.path.join(BASE_RIR, 'ml', 'Models', 'answer_status_model_v2.pkl')
    print(f"Model path: {model_path}", "*"*50)
    try:
        model = joblib.load(model_path)
    except FileNotFoundError:
        print(f"Error: Model file not found at {model_path}")
        return None

    embedding = get_embedding(question)
    prediction = model.predict([embedding])
    return prediction[0]

if __name__ == "__main__":
    print(Check_Answer("Qui est Lionel Messi ?"))