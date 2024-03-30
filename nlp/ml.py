import tensorflow as tf
import pandas as pd
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Embedding, LSTM, Dense, Concatenate
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler, Tokenizer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from tensorflow.keras.preprocessing.sequence import pad_sequences

def main():
    # Create dataframe with all my data
    df = pd.read_excel('data/american/american.xlsx')  # Update with file path later

    # Preprocessing
    X = df[['Mission Statement', 'Assets', 'NTEE Sector', 'State']]
    y = df['Revenue']

    # 20% of data will be randomly set aside as test data. 80% will be used for training.
    # random_state is a seed for the random number generator during split of data into training and test sets. 
    # using a specific number ensures that the split is reproducible; you get the same training and test sets across different runs of the code.
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42) 

    # Tokenize mission statements
    # this tokenizer splits words by spaces, filters out punctuation, and converts text to lowercase
    # does NOT remove stop words or lemmatize. must use SpaCy for this.
    tokenizer = Tokenizer()
    tokenizer.fit_on_texts(X_train['Mission Statement']) # train tokenizer on missions from training set. tokenizer converts text into sequences of integers. each integer represents a word in a dictionary of all words in the training set
    max_length = max(len(s.split()) for s in X_train['Mission Statement'])
    vocab_size = len(tokenizer.word_index) + 1 # add 1 bias unit
    X_train_mission_seq = pad_sequences(tokenizer.texts_to_sequences(X_train['Mission Statement']), maxlen=max_length)
    X_test_mission_seq = pad_sequences(tokenizer.texts_to_sequences(X_test['Mission Statement']), maxlen=max_length)

    # One-hot encode categorical variables (state, sector) and normalize numerical variables (assets)
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', StandardScaler(), ['Assets']),
            ('cat', OneHotEncoder(), ['NTEE Sector', 'State'])
        ]
    )

    X_train_processed = preprocessor.fit_transform(X_train.drop('Mission Statement', axis=1))
    X_test_processed = preprocessor.transform(X_test.drop('Mission Statement', axis=1))

    # Model Building
    # Mission statement input
    mission_input = Input(shape=(max_length,), name='mission_input')
    mission_embed = Embedding(input_dim=vocab_size, output_dim=50, input_length=max_length)(mission_input)
    mission_out = LSTM(64)(mission_embed)

    # Processed data input
    processed_input = Input(shape=(X_train_processed.shape[1],), name='processed_input')
    processed_out = Dense(64, activation='relu')(processed_input)

    # Concatenate and output
    concat = Concatenate()([mission_out, processed_out])
    hidden = Dense(64, activation='relu')(concat)
    output = Dense(1)(hidden)  # No activation function for regression

    model = Model(inputs=[mission_input, processed_input], outputs=output)

    # Compile and train the model
    model.compile(optimizer='adam', loss='mean_squared_error')
    model.fit([X_train_mission_seq, X_train_processed], y_train, validation_data=([X_test_mission_seq, X_test_processed], y_test), epochs=10, batch_size=32)

if __name__=="__main__":
    main()