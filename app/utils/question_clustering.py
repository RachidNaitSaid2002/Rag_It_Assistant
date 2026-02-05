from app.utils.labe_name import Get_Name
from app.utils.embedding_function import get_embedding
import joblib
import os

def Get_Cluster(question):
    BASE_RIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    model_path = os.path.join(BASE_RIR, 'ml', 'Models', 'kmeans_model.pkl')
    print(f"Model path: {model_path}", "*"*50)
    try:
        model = joblib.load(model_path)
    except FileNotFoundError:
        print(f"Error: Model file not found at {model_path}")
        return None
    embedding = get_embedding(question)
    prediction = model.predict([embedding])
    cluster_id = Get_Name(prediction[0])
    return prediction[0]

if __name__ == "__main__":
    print(Get_Cluster("Qui est Lionel Messi ?"))
