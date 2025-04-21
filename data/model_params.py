from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction import DictVectorizer
from sklearn.dummy import DummyClassifier
import xgboost as xgb
from xgboost import XGBClassifier
from sklearn.metrics import mean_squared_error
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd




## Function used in Hyper Parameter Tuning
def compare_models_with_tuning(df, col, test_size=0.2, random_state=1205):
    target_col = col 
    y = df[target_col]
    X = df.drop(columns=target_col)
    
    # Initial split: training and test sets
    X_train_init, X_test, y_train_init, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state
    )
    
    # Further split: training and validation sets
    X_train, X_val, y_train, y_val = train_test_split(
        X_train_init, y_train_init, test_size=test_size, random_state=random_state
    )

    models = {
        "GradientBoosting": (GradientBoostingClassifier(random_state=random_state), {
            'n_estimators': [100, 200, 300],
            'learning_rate': [0.01, 0.05, 0.1],
            'max_depth': [3, 5, 7],
            'subsample': [0.7, 0.85, 1.0],
            'min_samples_split': [2, 5, 10]
        }),
        "RandomForest": (RandomForestClassifier(random_state=random_state), {
            'n_estimators': [100, 200, 500],
            'max_depth': [None, 10, 20],
            'max_features': ['sqrt', 'log2', None],
            'min_samples_split': [2, 5, 10],
            'min_samples_leaf': [1, 2, 4, 8]
        }),
        "XG Boost Classifier": (xgb.XGBClassifier(objective='reg:squarederror', random_state=random_state), {
            'n_estimators': [100, 200, 300],
            'learning_rate': [0.01, 0.05, 0.1],
            'max_depth': [3, 5, 7],
            'subsample': [0.7, 0.85, 1.0]
        })
    }

    results = {
        'Model': [],
        'Train Accuracy': [],
        'Test Accuracy': []
    }

    for name, (model, param_grid) in models.items():
        print(f"Tuning {name}...")
        grid = GridSearchCV(model, param_grid, cv=3, scoring='accuracy', n_jobs=-1)
        grid.fit(X_train, y_train)

        best_model = grid.best_estimator_
        y_train_pred = best_model.predict(X_val)
        y_test_pred = best_model.predict(X_test)

        acc_train = accuracy_score(y_val, y_train_pred)
        acc_test = accuracy_score(y_test, y_test_pred)

        prec_train = precision_score(y_val, y_train_pred, average='weighted', zero_division=0)
        prec_test = precision_score(y_test, y_test_pred, average='weighted', zero_division=0)

        rec_train = recall_score(y_val, y_train_pred, average='weighted', zero_division=0)
        rec_test = recall_score(y_test, y_test_pred, average='weighted', zero_division=0)

        f1_train = f1_score(y_val, y_train_pred, average='weighted', zero_division=0)
        f1_test = f1_score(y_test, y_test_pred, average='weighted', zero_division=0)

        results['Model'].append(name)
        results['Train Accuracy'].append(acc_train * 100)
        results['Test Accuracy'].append(acc_test * 100)

        print(f"{name} - Best Params: {grid.best_params_}")
        print(f"Accuracy: Test {acc_test * 100:.2f}%, Train {acc_train * 100:.2f}%")
        print(f"Precision: Test {prec_test * 100:.2f}%, Train {prec_train * 100:.2f}%")
        print(f"Recall: Test {rec_test * 100:.2f}%, Train {rec_train * 100:.2f}%")
        print(f"F1 Score: Test {f1_test * 100:.2f}%, Train {f1_train * 100:.2f}%")
        print("-" * 30)

    # === Dummy Models ===
    dummy_models = {
        "Mean (Most Frequent)": DummyClassifier(strategy="most_frequent", random_state=random_state),
        "Random": DummyClassifier(strategy="uniform", random_state=random_state)
    }

    for name, dummy in dummy_models.items():
        dummy.fit(X_train, y_train)
        y_train_pred = dummy.predict(X_val)
        y_test_pred = dummy.predict(X_test)

        acc_train = accuracy_score(y_val, y_train_pred)
        acc_test = accuracy_score(y_test, y_test_pred)

        prec_train = precision_score(y_val, y_train_pred, average='weighted', zero_division=0)
        prec_test = precision_score(y_test, y_test_pred, average='weighted', zero_division=0)

        rec_train = recall_score(y_val, y_train_pred, average='weighted', zero_division=0)
        rec_test = recall_score(y_test, y_test_pred, average='weighted', zero_division=0)

        f1_train = f1_score(y_val, y_train_pred, average='weighted', zero_division=0)
        f1_test = f1_score(y_test, y_test_pred, average='weighted', zero_division=0)

        results['Model'].append(name)
        results['Train Accuracy'].append(acc_train * 100)
        results['Test Accuracy'].append(acc_test * 100)

        print(f"{name}")
        print(f"Accuracy: Test {acc_test * 100:.2f}%, Train {acc_train * 100:.2f}%")
        print(f"Precision: Test {prec_test * 100:.2f}%, Train {prec_train * 100:.2f}%")
        print(f"Recall: Test {rec_test * 100:.2f}%, Train {rec_train * 100:.2f}%")
        print(f"F1 Score: Test {f1_test * 100:.2f}%, Train {f1_train * 100:.2f}%")
        print("-" * 30)

    # Create DataFrame for plotting
    df_result = pd.DataFrame(results)

    # Melt for plotting with seaborn
    df_plot = df_result.melt(id_vars='Model', var_name='Dataset', value_name='Accuracy')

    # Plot
    plt.figure(figsize=(10, 6))
    sns.barplot(data=df_plot, x='Accuracy', y='Model', hue='Dataset', palette='Set2')
    plt.xlabel("Accuracy (%)")
    plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.2), ncol=2)
    plt.xlim(0, 105)
    plt.tight_layout()
    plt.show()
    