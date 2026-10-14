import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import seaborn as sns
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Load dataset
df = pd.read_csv('IMDB_dataset.csv')

#Class Distribution
print("Dataset Shape:", df.shape)
print("\nClass Distribution:")
print(df['sentiment'].value_counts())



# Text preprocessing pipeline
stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()


def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'<.*?>', '', text)
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    tokens = text.split()
    cleaned_tokens = [
        lemmatizer.lemmatize(token)
        for token in tokens
        if token not in stop_words
    ]
    return ' '.join(cleaned_tokens)

df['cleaned_review'] = df['review'].apply(preprocess_text)
print("Preprocessing complete!")
print(df[['review', 'cleaned_review']].head(2))





#TF-IDF Vectorizer
tfidf_vectorizer = TfidfVectorizer(max_features=5000, ngram_range=(1, 2))
X = tfidf_vectorizer.fit_transform(df['cleaned_review'])
y = df['sentiment']

# This is used to evaluate how important a word is to a file or a document


#Train/Test split (80/20)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42, stratify=y
)

print(f"Training set shape: {X_train.shape}")
print(f"Testing set shape: {X_test.shape}")


#Train classifiers and Evaluation
nb_model = MultinomialNB()
nb_model.fit(X_train, y_train)
y_pred_nb = nb_model.predict(X_test)
lr_model = LogisticRegression(max_iter=1000, random_state=42)
lr_model.fit(X_train, y_train)
y_pred_lr = lr_model.predict(X_test)

def evaluate_model(name, y_true, y_pred):
    print(f"=== {name} Performance ===")
    print(f"Accuracy: {accuracy_score(y_true, y_pred):.4f}\n")
    print("Classification Report:")
    print(classification_report(y_true, y_pred))

    plt.figure(figsize=(5, 4))
    cm = confusion_matrix(y_true, y_pred)
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
                xticklabels=nb_model.classes_, yticklabels=nb_model.classes_)
    plt.title(f'Confusion Matrix - {name}')
    plt.xlabel('Predicted')
    plt.ylabel('Actual')
    plt.show()


evaluate_model("Naive Bayes", y_test, y_pred_nb)
evaluate_model("Logistic Regression", y_test, y_pred_lr)



# Visualizations
plt.figure(figsize=(6, 4))
sns.countplot(x=df['sentiment'], palette='viridis')
plt.title('Sentiment Class Distribution')
plt.xlabel('Sentiment')
plt.ylabel('Count')
plt.show()

# 2. visualization for each sentiment class
sentiments = df['sentiment'].unique()
for sentiment in sentiments:
    text = " ".join(df[df['sentiment'] == sentiment]['cleaned_review'])
    wordcloud = WordCloud(width=800, height=400, background_color='white', max_words=100).generate(text)

    plt.figure(figsize=(8, 4))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title(f'WordCloud for {sentiment.upper()} Reviews')
    plt.show()


#Error analysis
results_df = pd.DataFrame({
    'original_review': df.loc[y_test.index, 'review'],
    'actual': y_test,
    'predicted': y_pred_lr
})

# Filter misclassified examples
errors_df = results_df[results_df['actual'] != results_df['predicted']]

print(f"Total misclassified examples: {len(errors_df)}")
print("\nShowing 5 Misclassified Examples:\n")

for idx, row in errors_df.head(5).iterrows():
    print(f"Review: {row['original_review'][:300]}...")
    print(f"Actual: {row['actual']} | Predicted: {row['predicted']}")
    print("-" * 80)


 # Summary of the best model comparison
print("Model comparison complete. Review precision, recall, and F1-scores above to determine the winner.")

