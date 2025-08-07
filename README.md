<img width="1912" height="905" alt="iris" src="https://github.com/user-attachments/assets/7488f536-e3ff-4f57-a707-7eeee55917b9" />

# 🌸 Iris Flower Classifier

A simple and interactive Streamlit app that classifies iris flower species (setosa, versicolor, virginica) based on sepal and petal measurements using a trained ML model.

## 🚀 Features

- Input sepal length, sepal width, petal length, and petal width
- Predict species with quick response in a Streamlit interface
- Shows model accuracy and features importance (if needed)
- Jupyter notebook included for data exploration and model training

## 🗂 Project Structure

```
📦 Iris-Flower-Classifier
├── app.py              # Streamlit application for classification
├── iris.data.csv       # Iris dataset
├── iris.ipynb          # Notebook with EDA, model training, and evaluation
├── iris_model.pkl      # Trained ML model for real-time prediction
├── requirement.txt     # Python dependencies
├── README.md           # This documentation
```

## 🧪 Usage

### 1. Clone the repository
```bash
git clone https://github.com/FarazhussainAI250/Iris-Flower-Classifier.git
cd Iris-Flower-Classifier
```

### 2. Install dependencies
```bash
pip install -r requirement.txt
```

### 3. Run the app
```bash
streamlit run app.py
```

App will launch in your browser at `http://localhost:8501/`.

## 🔎 How It Works

User inputs four measurements—sepal length & width, petal length & width—and the app uses a pre-trained model to predict the iris species instantly.

## 🌱 Future Enhancements

- Display model confidence scores
- Include confusion matrix and accuracy metrics
- Allow CSV batch uploads for multiple predictions

## 📄 License

Open-source project under the MIT License.

## 👨‍💻 Contact

**Faraz Hussain**  
GitHub: [@FarazhussainAI250](https://github.com/FarazhussainAI250)
