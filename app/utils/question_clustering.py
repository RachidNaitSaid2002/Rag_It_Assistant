from app.utils.labe_name import Get_Name
from app.utils.embedding_function import get_embedding
import joblib
import os

def Get_Cluster(question):
    BASE_PATH = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

    model_path = os.path.join(
        BASE_PATH,
        "ml",
        "Models",
        "kmeans_model.pkl"
    )
    
    print(f"Looking for model at: {model_path}") 
    model = joblib.load(model_path)
    embedding = get_embedding(question)
    prediction = model.predict([embedding])
    cluster_id = Get_Name(prediction[0])
    return prediction[0]

if __name__ == "__main__":
    print(Get_Cluster("Qui est Lionel Messi ?"))
