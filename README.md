# Project Title

A data-driven project that analyzes and visualizes insights from `data_extended.csv` using Python, Jupyter Notebook, and a Streamlit app for interactive exploration.

**Live App Link:** [Streamlit App](https://ann---breast-cancer-dataset-kkjqkeo7rhu83vmfkjz2ew.streamlit.app/)

---

## 📂 Repository Structure

```
├── data_extended.csv     # Dataset used for analysis
├── code.ipynb            # Jupyter Notebook with data processing & modeling
├── app.py                # Streamlit app script (if separated from notebook)
├── requirements.txt
├── model.pkl
├── scaler.pkl
├── README.md             # Project documentation
```

---

## 🚀 Features

* Exploratory Data Analysis (EDA) on `data_extended.csv`
* Data preprocessing & feature engineering
* Model training and evaluation (if applied in the notebook)
* Interactive Streamlit web app to explore insights & visualizations

---

## ⚙️ Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/your-username/your-repo.git
   cd your-repo
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

*Make sure `requirements.txt` includes libraries like `pandas`, `numpy`, `matplotlib`, `seaborn`, `scikit-learn`, and `streamlit`.*

---

## ▶️ Usage

### Run Jupyter Notebook

```bash
jupyter notebook code.ipynb
```

### Run Streamlit App

```bash
streamlit run app.py
```

This will launch the web app in your browser (default: `http://localhost:8501`).

---

## 📊 Dataset

* **File:** `data_extended.csv`
* **Description:** \[Add a brief explanation of what the dataset contains, e.g., health records, patient data, etc.]
* **Size:** \[Number of rows × columns]

---

## 🌐 Streamlit App

The app provides:

* Interactive filters for exploring the dataset
* Dynamic charts & plots
* Model predictions (if included)

<img width="1332" height="910" alt="Screenshot 2025-09-17 233100" src="https://github.com/user-attachments/assets/4a058d05-b7f6-4416-bf68-e24052114db1" />

<br>
<br>

<img width="1164" height="756" alt="Screenshot 2025-09-17 231954" src="https://github.com/user-attachments/assets/6b455366-2460-4571-9a20-f2d9529dc2ff" />

---

## 📈 Results / Insights

* The dataset shows a roughly balanced distribution between malignant and benign cases, ensuring reliable model training.
* Feature correlations reveal that attributes like radius_mean, concave_points_mean, and perimeter_mean are strongly associated with malignancy.
* The ANN model achieved high accuracy (~97–98%) on the test set, demonstrating strong predictive performance.
* Visualizations indicate that malignant cases generally have higher values for texture and smoothness metrics, while benign cases cluster in lower-value ranges.
* The interactive Streamlit app allows users to explore individual features and see how changes affect predicted outcomes.

---

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

---

## 📜 License

[MIT License](LICENSE) (or whichever license you choose)
