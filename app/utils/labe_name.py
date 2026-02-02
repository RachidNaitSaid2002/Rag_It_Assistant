
def Get_Name(cluster_id):
    cluster_map = {
        0: "Technical IT Support Concepts",
        1: "Document Fact-Checking",
        2: "Specific Book Terminology",
        3: "Book Structure & Chapters",
        4: "Out-of-Scope Queries",
        5: "Time-Sensitive/Current Events",
        6: "General Knowledge & Tutorials",
        7: "Author Personal Details"
    }
    return cluster_map[cluster_id]

if __name__ == "__main__":
    print(Get_Name(0))
    print(Get_Name(1))
    print(Get_Name(2))
    print(Get_Name(3))
    print(Get_Name(4))
    print(Get_Name(5))
    print(Get_Name(6))
    print(Get_Name(7))