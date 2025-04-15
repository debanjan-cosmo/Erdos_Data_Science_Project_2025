#Hyperparameters found through randomized_search_CV. grid_search_CV did not find a drastically better set of parameters

xgb_ded_full = {'colsample_bytree': 0.7, 'lambda': 9, 'learning_rate': 0.1, 'max_depth': 3, 'n_estimators': 100, 'subsample': 0.8}

xgb_insomnia_full = {'colsample_bytree': 1.0, 'lambda': 9, 'learning_rate': 0.01, 'max_depth': 7, 'n_estimators': 50, 'subsample': 0.8}