from src.data_loader import load_data
from src.preprocessing import preprocess_data
from src.train_model import train_model
from src.evaluation import evaluate_model
from src.visualization import plot_results
from src.save_model import save_model

def main():

    # Load dataset
    df = load_data(
        'Data/student-mat.csv'
    )

    print(df.head())

    # Preprocess dataset
    df = preprocess_data(df)
    print(df.dtypes)

    print("\nAfter Preprocessing:\n")
    print(df.head())

    # Train model
    model, X_test, y_test = train_model(df)

    # Evaluate model
    predictions = evaluate_model(
        model,
        X_test,
        y_test
    )
    save_model(model)
    # Visualization
    plot_results(
        y_test,
        predictions
    )

if __name__ == "__main__":

    main()