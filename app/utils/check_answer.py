import joblib
from app.utils.embedding_function import get_embedding

def Check_Answer(question):
    model = joblib.load("/media/rachid/d70e3dc6-74e7-4c87-96bc-e4c3689c979a/lmobrmij/Projects/Rag_It_Assistant/ml/Models/answer_status_model_v2.pkl")
    embedding = get_embedding(question)
    prediction = model.predict([embedding])
    return prediction[0]

if __name__ == "__main__":
    print(Check_Answer("Qui est Lionel Messi ?"))