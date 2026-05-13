import matplotlib.pyplot as plt

def plot_results(y_test, predictions):

    plt.figure(figsize=(10, 5))

    plt.plot(
        y_test.values[:50],
        label='Actual'
    )

    plt.plot(
        predictions[:50],
        label='Predicted'
    )

    plt.legend()

    plt.title(
        "Student Performance Prediction"
    )

    plt.show()