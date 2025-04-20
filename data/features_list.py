feature_list = ['gender',
                'age',
                'sleep_duration',
                'sleep_quality',
                'stress_level',
                'heart_rate',
                'daily_steps',
                'physical_activity',
                'height',
                'weight',
                'bmi',
                'sleep_disorder',
                'wake_up_during_night',
                'feel_sleepy_during_day',
                'caffeine_consumption',
                'alcohol_consumption',
                'smoking',
                'medical_issue',
                'ongoing_medication',
                'smart_device_before_bed',
                'average_screen_time',
                'blue-light_filter',
                'discomfort_eye-strain',
                'redness_in_eye',
                'itchiness/irritation_in_eye',
                'dry_eye_disease',
                'systolic',
                'diastolic',
                'bp_category',
                'insomnia',
                'combined_condition']

features_for_bp_category = ['systolic', 'diastolic']

features_for_insomnia = ['sleep_disorder',
                         'sleep_duration',
                         'sleep_quality',
                         'feel_sleepy_during_day',
                         'wake_up_during_night']

features_for_bmi = ['weight','height']


refined_list = ['gender',
                'age',
                'stress_level',
                'heart_rate',
                'daily_steps',
                'physical_activity',
                'bmi',
                'caffeine_consumption',
                'alcohol_consumption',
                'smoking',
                'medical_issue',
                'ongoing_medication',
                'smart_device_before_bed',
                'average_screen_time',
                'blue-light_filter',
                'discomfort_eye-strain',
                'redness_in_eye',
                'itchiness/irritation_in_eye',
                'bp_category']


# Map each feature to a category
category_map = {
    "Demographics": [
        'gender', 'age', 'bmi'
    ],
    "Health_Lifestyle": [
        'stress_level', 'heart_rate', 'daily_steps', 'physical_activity', 'bp_category',
        'medical_issue', 'ongoing_medication'
    ],
    "Consumption_Habits": [
        'caffeine_consumption', 'alcohol_consumption', 'smoking'
    ],
    "Device_Use": [
        'smart_device_before_bed', 'average_screen_time', 'blue-light_filter'
    ],
    "Ocular_Surface_Symptoms": [
        'discomfort_eye-strain', 'redness_in_eye', 'itchiness/irritation_in_eye']
}

# Map each feature to a category
feature_to_category = {
    'gender': 'Demographics', 'age': 'Demographics', 'bmi': 'Demographics',
    'stress_level': 'Health_Lifestyle', 'heart_rate': 'Health_Lifestyle', 'daily_steps': 'Health_Lifestyle',
    'physical_activity': 'Health_Lifestyle', 'bp_category': 'Health_Lifestyle',
    'medical_issue': 'Health_Lifestyle', 'ongoing_medication': 'Health_Lifestyle',
    'caffeine_consumption': 'Consumption_Habits', 'alcohol_consumption': 'Consumption_Habits', 'smoking': 'Consumption_Habits',
    'smart_device_before_bed': 'Device_Use', 'average_screen_time': 'Device_Use', 'blue-light_filter': 'Device_Use',
    'discomfort_eye-strain': 'Ocular_Surface_Symptoms', 'redness_in_eye': 'Ocular_Surface_Symptoms', 'itchiness/irritation_in_eye': 'Ocular_Surface_Symptoms'
}


category_colors = {
    "Demographics": (0.12156862745098039, 0.4666666666666667, 0.7058823529411765),  # blue
    "Health_Lifestyle": (1.0, 0.5, 0.0),  # orange
    "Consumption_Habits": (0.15294117647058825, 0.6823529411764706, 0.3764705882352941),  # green
    "Device_Use": (0.8392156862745098, 0.15294117647058825, 0.1568627450980392),  # red
    "Ocular_Surface_Symptoms": (0.5803921568627451, 0.403921568627451, 0.7411764705882353)  # purple
}


### Below is a function for generating lists of features present in the dataset:
def extract_features(df, feature_list):
    return [
    feature for feature in feature_list 
    if feature in df.columns 
]