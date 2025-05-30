# 📊 Unemployment Analysis in India using Python

This project analyzes unemployment trends across various Indian states using publicly available data. It uses data visualization to highlight patterns before, during, and after the COVID-19 pandemic.

---

## 📁 Dataset

- Source: [Kaggle - Unemployment in India](https://www.kaggle.com/datasets/gokulrajkmv/unemployment-in-india)
- The dataset contains:
  - Region (State)
  - Date
  - Estimated Unemployment Rate (%)
  - Estimated Employed
  - Estimated Labour Participation Rate (%)
  - Area (Urban/Rural)

---

## 🧰 Tech Stack

- Python 3.7+
- Pandas
- Matplotlib
- Seaborn

---

## 📦 Installation

1. Clone the repository or download the script:

   ```bash
   git clone  https://github.com/Code-By-Mahendra/CodeAlpha_unemploymenet_analysis.git
   cd unemployment-analysis-india

## Install dependencies:
```bash
pip install pandas matplotlib seaborn
```

## Make sure the CSV file is named correctly:
[Download the dataset](https://www.kaggle.com/datasets/gokulrajkmv/unemployment-in-india) in the same folder as the script.

## ▶️ How to Run
```bash
python unemployment_analysis.py

```
## 📈 Output Visualizations
1. Yearly Average Unemployment Trend
Shows how unemployment varied by year.
![Yearly Unemployment Trend](images/yearly_unemployment_trend.png)
## 2. Top 5 States by Unemployment Rate
Displays unemployment trends over time for the five worst-affected states.
![Top States Trend](images/top_states_trend.png)
## 3. Heatmap by State & Year
A heatmap visualization of unemployment rates across all states and years.
![Unemployment Heatmap](images/state_year_heatmap.png)

## 🧼 Cleaned Dataset
A new file named **`cleaned_unemployment_india.csv`** is created after preprocessing and can be reused for dashboarding or further modeling.

## 📚 Future Ideas
Build an interactive dashboard using Streamlit or Flask

Train a forecasting model to predict unemployment rate trends

Add urban vs. rural comparisons

## 🧑‍💻 Author

- 👤 Name: [Velagapudi Mahendra](https://www.linkedin.com/in/velagapudi-mahendra-543481353)


## 📝 License
This project is open-source and free to use for educational purposes.