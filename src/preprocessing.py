from sklearn.preprocessing import LabelEncoder

def preprocess_data(df):

    encoder = LabelEncoder()

    # Find categorical columns
    categorical_columns = df.select_dtypes(
        include=['object']
    ).columns

    # Encode categorical columns
    for column in categorical_columns:

        df[column] = encoder.fit_transform(
            df[column]
        )

    return df