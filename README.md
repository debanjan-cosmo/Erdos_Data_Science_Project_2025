# Machine Learning Insights into Dry Eyes and Sleepless Nights

**Team**: [Debanjan Sarkar](https://github.com/debanjan-cosmo), [Anwesha Basu](https://github.com/AnweshaB12)  
**GitHub Repository**: [Erdos_Data_Science_Project_2025](https://github.com/debanjan-cosmo/Erdos_Data_Science_Project_2025)  
**Dataset**: *Dry Eye Disease Dataset* (sourced from [Kaggle](https://www.kaggle.com/datasets/dakshnagra/dry-eye-disease/data))

---

## Background and Project Overview

In this project, we explore the overlap between **Dry Eye Disease (DED)** and **insomnia**, two prevalent conditions with significant impact on quality of life. Using a publicly available dataset containing 20,000 records and 25 features, we aim to identify shared risk factors and build predictive models for both conditions.

The dataset includes a wide range of features—from demographics and health habits to screen time and ocular symptoms—making it suitable for uncovering behavioral patterns linked to DED and sleep quality. Insomnia was defined using a rule-based approach incorporating self-reported sleep issues.

---

## Objectives

- Understand how DED and insomnia are related  
- Identify which features are most influential in predicting each condition  
- Support preventive care strategies using interpretable ML models  

---

## Data Preprocessing

- Verified no missing values  
- Encoded categorical features  
- Engineered blood pressure categories from systolic/diastolic values  
- Derived a BMI-like feature from height and weight  
- Removed redundant/derived features to reduce noise  
- Created a binary insomnia label using five rule-based sleep conditions  
- Ensured data consistency across modeling tasks  

---

## Modelling Approach

We began with exploratory data analysis (EDA) to uncover distributions, patterns, and relationships among features and target labels (DED, insomnia, and both). The data was split into **80% training** (**20%** of which was kept for **cross-validation**) and **20% testing**, with part of the training set reserved for cross-validation.

After benchmarking with baseline models (mean and random classifiers), we trained and compared multiple algorithms including:

- Gradient Boosting  
- Random Forest  
- Support Vector Classifier (SVC)  
- XGBoost

<div align="center">
  <img src="Figures/benchmark_target_ded.png" width="50%"/>
  <p><em>Figure 1: Benchmark setting DED as target.</em></p>
</div>

<div align="center">
  <img src="Figures/benchmark_target_insomnia.png" width="50%"/>
  <p><em>Figure 2: Benchmark setting 'Insomnia' as target.</em></p>
</div>

<div align="center">
  <img src="Figures/benchmark_target_combined.png" width="50%"/>
  <p><em>Figure 3: Benchmark setting 'DED + Insomnia' as target.</em></p>
</div>

Based on performance, we shortlisted **Gradient Boosting**, **Random Forest**, and **XGBoost**. After hyperparameter tuning, **XGBoost** was chosen as the final model due to its high accuracy and faster training time. It was then used for feature importance analysis across different target labels.

---

## KPIs

- Model Accuracy  
- F1-Score  
- Training Time  
- Interpretability of Feature Importance  

---

## Results

### Dry Eye Disease (DED) Prediction:

<div align="center">
  <img src="Figures/DED_as_Target.png" width="50%"/>
  <p><em>Figure 4: Feature importance for predicting DED, with features grouped by category.</em></p>
</div>


- Top predictors: ocular symptoms like redness and irritation  
- Gender (female) was strongly associated with DED  
- Insomnia was also a strong predictor, especially in younger, less active individuals  

### Insomnia Prediction:

<div align="center">
  <img src="Figures/Insomnia_as_Target.png" width="50%"/>
  <p><em>Figure 5: Feature importance for predicting Insomnia, with features grouped by category.</em></p>
</div>


- DED emerged as the most influential predictor  
- Other important features: caffeine intake, BMI, and screen time  

### Combined Condition (DED + Insomnia):

<div align="center">
  <img src="Figures/Combined_Target.png" width="50%"/>
  <p><em>Figure 5: Feature importance for predicting DED + Insomnia, with features grouped by category.</em></p>
</div>

- Key features: ocular symptoms, gender, device usage, and lifestyle factors  
- Gender-specific patterns, particularly in women, were observed  

---

## Summary and Future Directions

Our findings underscore a **strong bidirectional relationship** between eye health and sleep health. These insights highlight the need for **integrated clinical assessments** that consider both conditions together.

### Future Work:
- Try more interpretable models or even deep learning for better performance.
- Explore more data — especially on stress, environmental factors, and country based. 

---

## Stakeholders

- Healthcare providers  
- Medical researchers  
- Policy makers  
- Individuals impacted by DED or sleep disorders  

---

### Repository Structure

### `Data/`
Contains all the datasets and helper scripts for feature engineering and preprocessing.

- **dry_eye_disease_rawfile.csv**: Raw data containing unprocessed information.
- **dry_eye_disease_parsed.csv**: Cleaned and structured version of the raw data.
- **features_list.py**: Defines subsets of features used for model training and evaluation.
- **model_params.py**: Stores hyperparameter settings and functions for various models.
- **utils.py**: Utility functions for data handling and preprocessing.

---

### `Exploration/`
Notebooks focused on data exploration and understanding.

- **01_Data_Parsing.ipynb**: Parses the raw dataset and performs initial data cleaning.
- **02_visualize_numerical_and_categorical_data.ipynb**: Visualization of distributions for numerical and categorical features.
- **03_determine_outliers.ipynb**: Outlier detection using statistical methods and visual inspection.
- **03_visualize_conditional_box_plots.ipynb**: Conditional boxplots comparing distributions across categories and comorbidities.

---

### `Modelling/`
Machine learning workflows for classifying DED, insomnia, and combined conditions.

- **01_Using_Multiple_Methods.ipynb**: Applies several classification algorithms and compares their performance.
- **02_Hyper_Parameter_Tuning.ipynb**: Hyperparameter optimization using grid search and cross-validation.
- **03a_Classifying_DED.ipynb**: Main notebook for classifying Dry Eye Disease and interpreting model results.
- **03b_Classifying_Insomnia.ipynb**: Applies similar techniques to classify insomnia.
- **03c_Classifying_Combined_Condition.ipynb**: Joint classification of DED and insomnia as a comorbid condition.

---

### `Figures/`
Contains some plots and figures generated during EDA and modeling.

---

## Dependencies

The project uses the following Python libraries:


- [XGBoost](https://xgboost.readthedocs.io/en/stable/)  
- [Scikit-Learn](https://scikit-learn.org/stable/)  
- [Pandas](https://pandas.pydata.org/)  
- [NumPy](https://numpy.org/)  
- [Matplotlib](https://matplotlib.org/)  
- [Seaborn](https://seaborn.pydata.org/)  
- [KaggleHub](https://github.com/Kaggle/kagglehub)  
- [SHAP (SHapley Additive exPlanations)](https://shap.readthedocs.io/en/latest/) 

---

### Installation

Install all dependencies using:

```bash
pip install -r requirements.txt
