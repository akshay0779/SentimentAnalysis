🧠 Sentiment Analysis Web App (NLP Project)


📋 Overview

This project is an NLP-based Sentiment Analysis Web App that classifies user-input text as Positive, Negative, or Neutral using a pre-trained Transformer model from Hugging Face.
The app is built with Streamlit, providing a clean and interactive interface for real-time text analysis.

🚀 Features

💬 Real-time Sentiment Prediction using a pre-trained distilbert-base-uncased-finetuned-sst-2-english model.

🧠 Natural Language Processing powered by the Transformers library.

⚡ Interactive Web Interface built using Streamlit.

🔒 No dataset or training required — uses a ready-to-use model.

🎈 Smooth user experience with emojis and styled output.

⚙️ Technologies Used

Python

Streamlit

Transformers (Hugging Face)

PyTorch

🧠 How It Works

The user enters a sentence or paragraph.

The app loads a pre-trained sentiment analysis pipeline.

The text is passed to the model for inference.

The app displays the sentiment label (Positive/Negative/Neutral) and confidence score.

🧩 Example

Input:

I absolutely love this product! It works perfectly and makes my day brighter.

Output:

Label: Positive

Confidence Score: 0.98

😄 The sentiment is Positive!

🪄 No Dataset Required

The app uses Hugging Face’s pre-trained DistilBERT model, so no dataset download or training is necessary.

📄 How to Run

Install required libraries:

pip install streamlit transformers torch


Save the code as sentiment_app.py.

Run the app:

streamlit run sentiment_app.py


Open the browser window to access the live web interface.

👩‍💻 Author

Developed by Anushka Gupta as part of a Natural Language Processing learning project.
