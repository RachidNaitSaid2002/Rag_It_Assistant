from app.utils.labe_name import Get_Name
from app.utils.embedding_function import get_embedding
import joblib

def Get_Cluster(question):
    model = joblib.load("/media/rachid/d70e3dc6-74e7-4c87-96bc-e4c3689c979a/lmobrmij/Projects/Rag_It_Assistant/ml/Models/kmeans_model.pkl")
    embedding = get_embedding(question)
    prediction = model.predict([embedding])
    cluster_id = Get_Name(prediction[0])
    return prediction[0]

if __name__ == "__main__":
    print(Get_Cluster("Qui est Lionel Messi ?"))
