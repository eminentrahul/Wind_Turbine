# 🌬️ How I Built a Wind Turbine Power Forecasting Model (A Beginner‑Friendly Data Science Story)

If you’ve ever wondered how **raw weather data** turns into **accurate power forecasts**, this project is my attempt to show that journey — step by step, without skipping the thinking.

This is not just a notebook.
It’s a **story of how a Data Scientist approaches a real-world energy forecasting problem**.

Whether you’re a beginner, a Kaggle learner, or preparing for interviews, my goal is simple:

> By the end of this project, you should understand **what was done, why it was done, and how you can do it yourself**.

---

## 🧩 The Problem I Wanted to Solve

Wind energy depends heavily on nature — and nature is noisy.

Given historical data about:
- Wind speed
- Wind direction
- Temperature
- Humidity
- Time

👉 **Can we predict how much power a wind turbine will generate in the future?**

This makes the problem:
- A **regression problem** (predicting a continuous value)
- With a strong **time-series component** (past affects the future)

---

## 📂 Project Structure (Simple & Intentional)

```
Wind_Turbine/
│
├── wind-power-forecasting.ipynb   # The full story lives here
├── xgboost_forecast.pkl           # Trained model (ready for reuse)
├── model_features.pkl             # Features used during training
├── README.md                      # You’re reading it now
```

I intentionally kept the repo minimal so learners focus on **thinking**, not folder chaos.

---

## 🧠 Step 1: Setting Up the Tools

Before touching the data, I loaded the tools every Data Scientist relies on:

- **Pandas & NumPy** → for data handling
- **Matplotlib, Seaborn, Plotly** → to *see* patterns, not guess
- **Scikit-learn** → modeling and evaluation
- **XGBoost** → a powerful real-world ML model
- **Statsmodels** → time series analysis

👉 Lesson: *Good tools don’t make you smart — knowing when to use them does.*

---

## 📊 Step 2: Meeting the Data for the First Time

The dataset came as two files:
- **Train.csv** – historical data
- **Test.csv** – future periods

First things I checked:
- Shape of the data
- Column names
- Data types

Why?

> Because many projects fail in the first 10 minutes due to careless data loading.

---

## 🔍 Step 3: Asking the Right Questions About Data

Before modeling, I asked:

- Are there missing values?
- Are sensor readings noisy?
- Do values make physical sense?

Using:
- `.info()`
- `.isnull()`
- `.describe()`

I built a **numerical intuition** of the dataset.

👉 This step tells you *what kind of mess you’re dealing with*.

---

## ⏰ Step 4: Respecting Time (Very Important)

Time series data is unforgiving.

So I:
- Converted the `Time` column to datetime
- Sorted everything chronologically

Why?

> If time order is wrong, even the best model becomes useless.

---

## 📈 Step 5: Visualizing Reality

I plotted:
- Power generation over time
- Wind speed distributions
- Correlations between features

These plots revealed:
- Daily patterns
- Strong dependency on wind speed
- Noise caused by sensors

👉 Visuals help you *see the physics behind the data*.

---

## 🧹 Step 6: Cleaning the Noise

Real-world data is messy — especially sensor data.

So I:
- Interpolated missing values using time logic
- Clipped extreme outliers (1%–99%)

Why not delete everything?

> Because in energy data, extremes often matter.

---

## 🛠️ Step 7: Turning Raw Data into Intelligence (Feature Engineering)

This is where the project truly comes alive.

### 🕒 Time-Based Features
I extracted:
- Hour
- Day
- Month
- Weekday

Why?

> Power demand and wind patterns follow human and natural cycles.

---

### ⏪ Lag Features (Memory of the Past)

I added:
- Power 1 hour ago
- Power 24 hours ago

This teaches the model:

> *What happened recently influences what happens next.*

---

### 📊 Rolling Statistics (Smoothing the Chaos)

- 24-hour rolling mean
- 7-day rolling mean

These capture:
- Short-term trends
- Weekly seasonality

---

### 🌬️ Physics-Inspired Thinking

Since:

> Wind power ∝ (wind speed)³

I created features that respect **real-world physics**, not just math.

---

### 🔄 Cyclical Encoding

Time is circular, not linear.

So instead of treating hour 23 and 0 as far apart, I used:
- Sine
- Cosine transformations

👉 This small trick massively improves learning.

---

## ✂️ Step 8: Handling NA Values After Features

Lag and rolling features naturally create missing rows.

Instead of forcing values, I:
- Dropped only the unavoidable initial rows

Clean, honest data beats fake completeness.

---

## 🔬 Step 9: Understanding the Time Series Itself

I decomposed the power signal into:
- Trend
- Seasonality
- Residual noise

Then ran the **Augmented Dickey-Fuller test** to check stationarity.

👉 This step improves *conceptual clarity*, even if the model doesn’t strictly need it.

---

## 🔀 Step 10: Train-Test Split (Done the Right Way)

Instead of random splitting, I used:
- First 80% → training
- Last 20% → testing

Why?

> In forecasting, the future must remain unseen.

---

## 🤖 Step 11: Modeling Strategy

### Baseline: Linear Regression
- Simple
- Interpretable
- Sets a performance floor

### Main Model: XGBoost Regressor
- Handles non-linearity
- Works brilliantly on tabular data
- Industry-proven

---

## 📏 Step 12: Measuring Success

I evaluated models using:
- MAE (Mean Absolute Error)
- RMSE (Root Mean Squared Error)
- MAPE (Mean Absolute Percentage Error)
- R² Score

Each metric answers a different business question.

---

## 📊 Step 13: Visual Validation

I plotted:
- Actual vs Predicted power

This answered the most important question:

> *Can I trust this model in the real world?*

---

## 🔎 Step 14: Feature Importance

Using XGBoost’s feature importance, I identified:
- Which signals matter most
- Which features drive decisions

This builds **explainability and confidence**.

---

## 💾 Step 15: Saving the Work (Like a Professional)

I saved:
- The trained model
- The exact feature list

Why?

> A model that can’t be reused is just an experiment.

---

## 🔮 Step 16: Looking Ahead

Possible next steps:
- Hyperparameter tuning
- Deep learning (LSTM / Transformers)
- Probabilistic forecasting
- API deployment

---

## 🏁 Final Thoughts

This project reflects how **real Data Science actually works**:

✔ Think before coding
✔ Respect time
✔ Engineer features thoughtfully
✔ Validate visually
✔ Save for reuse

If you truly understand this notebook, you are no longer a beginner — you’re becoming an **applied Data Scientist**.

Happy forecasting 🚀

