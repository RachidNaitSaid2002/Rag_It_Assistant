import joblib
from app.utils.embedding_function import get_embedding
import os

def Check_Answer(question):
    BASE_PATH = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

    model_path = os.path.join(
        BASE_PATH,
        "ml",
        "Models",
        "answer_status_model_v2.pkl"
    )
    
    print(f"Looking for model at: {model_path}") 

    try:
        model = joblib.load(model_path)
        embedding = get_embedding(question)
        prediction = model.predict([embedding])
        return prediction[0]
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    print(Check_Answer("Qui est Lionel Messi ?"))