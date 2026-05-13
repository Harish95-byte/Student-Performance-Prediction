import joblib

def save_model(model):

    joblib.dump(
        model,
        'models/student_performance_model.pkl'
    )

    print(
        "Model Saved Successfully"
    )