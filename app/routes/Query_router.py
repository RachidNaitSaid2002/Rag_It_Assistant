from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.db_connection import get_db_session
from app.models.queries_model import Queryies
from app.schemas.querie_schema import Query
from scripts.Core_function import Final_function
from app.auth.token_auth import get_current_user
from app.utils.check_answer import Check_Answer
from app.utils.question_clustering import Get_Cluster
import mlflow
import json
import time


router = APIRouter(prefix="/query", tags=["Query"])

@router.post("/query")
def create_query(question: str, db: Session = Depends(get_db_session), user_id: int = Depends(get_current_user)):

    checker_an = Check_Answer(question)

    if checker_an == 1:
        return {'message': "La question n'est pas pertinente"}
    else:
        # MLflow Tracking for API requests
        mlflow.set_experiment("RAG_Assistant_Tracking")
        with mlflow.start_run(run_name=f"API_Query_{int(time.time())}"):
            # Log Parameters
            mlflow.log_params({
                "source": "API",
                "question": question,
                "user_id": user_id
            })

            t0 = time.time()
            result, latency = Final_function(question)
            t1 = time.time()
            
            # Log Metrics & Result
            mlflow.log_metric("latency", t1 - t0)
            mlflow.log_text(result.get('result'), "generated_response.txt")

            cluster_id = Get_Cluster(question)
            mlflow.log_param("cluster_id", cluster_id)
            
            formatted_sources = []
            not_found_msg = "Je ne trouve pas l'information dans le contexte fourni."
            
            if result.get('result') != not_found_msg:
                formatted_sources = [
                    {
                        "page": doc.metadata.get("page"),
                        "file_source": doc.metadata.get("source"),
                        "page_content": doc.page_content
                    }
                    for doc in result.get('source_documents', [])
                ]
                # Log detailled chunks as artifact
                mlflow.log_text(json.dumps(formatted_sources, indent=2), "retrieved_chunks_api.json")

            db_query = Queryies(
                question=question,
                answer=result.get('result'),
                latency_ms=float(latency),
                user_id=user_id,
                formatted_sources=formatted_sources,
                cluster=int(cluster_id)
            )
            db.add(db_query)
            db.commit()
            db.refresh(db_query)
            
            # Add MLflow Run ID to the database record if possible (optional but good for traceability)
            # db_query.mlflow_run_id = mlflow.active_run().info.run_id 
            
            return db_query