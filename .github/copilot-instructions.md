# Copilot Instructions for Wind Turbine Power Forecasting Project

## Project Overview
This repository demonstrates how to build a wind turbine power forecasting model using machine learning. The project is structured to be beginner-friendly and focuses on:
- Predicting wind turbine power output based on weather data.
- Using tools like Streamlit for visualization and Jupyter Notebooks for data exploration.

### Key Components
1. **Jupyter Notebook (`wind-power-forecasting.ipynb`)**:
   - Contains the full data science workflow, including data preprocessing, feature engineering, model training, and evaluation.
   - Outputs trained artifacts (`xgboost_forecast.pkl`, `model_features.pkl`) for reuse.

2. **Streamlit App (`streamlit_app.py`)**:
   - Provides an interactive interface for users to input weather parameters and predict power output.
   - Loads the pre-trained model and ensures feature alignment during inference.

3. **Artifacts**:
   - `xgboost_forecast.pkl`: Trained XGBoost model.
   - `model_features.pkl`: List of features used during training to ensure consistency.

---

## Developer Workflows

### Running the Streamlit App
1. Ensure dependencies are installed:
   ```bash
   pip install -r requirements.txt
   ```
2. Start the app:
   ```bash
   streamlit run streamlit_app.py
   ```
3. Open the app in your browser (default: `http://localhost:8501`).

### Exploring the Jupyter Notebook
1. Open `wind-power-forecasting.ipynb` in Jupyter or VS Code.
2. Follow the cells sequentially to understand the data science workflow.
3. Ensure the required libraries are installed (see `requirements.txt`).

---

## Project-Specific Conventions

### Feature Engineering
- Features are engineered both in the notebook and the Streamlit app.
- Ensure consistency between training and inference by using `model_features.pkl` to align columns.

### Model Artifacts
- Always save models and feature lists after training for reproducibility.
- Use `joblib` for saving and loading artifacts.

### Streamlit Patterns
- Use `@st.cache_resource` to cache expensive operations like model loading.
- Use sliders and time inputs for user-friendly parameter selection.

---

## External Dependencies
- **XGBoost**: Core ML model used for regression.
- **Streamlit**: For building the interactive web app.
- **Pandas, NumPy**: For data manipulation.
- **Matplotlib, Seaborn, Plotly**: For data visualization.

---

## Notes for AI Agents
- When modifying the Streamlit app, ensure that the feature engineering logic aligns with the training notebook.
- When updating the notebook, ensure that any changes to feature engineering are reflected in `model_features.pkl`.
- Follow the minimalistic structure of the repository to maintain clarity for learners.

---

## Example Commands
- Install dependencies:
  ```bash
  pip install -r requirements.txt
  ```
- Run the Streamlit app:
  ```bash
  streamlit run streamlit_app.py
  ```
- Open the Jupyter Notebook for exploration:
  ```bash
  jupyter notebook wind-power-forecasting.ipynb
  ```