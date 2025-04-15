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


refined_list = ['gender',
                'age',
                'stress_level',
                'heart_rate',
                'daily_steps',
                'physical_activity',
                'height',
                'weight',
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
        'gender', 'age', 'height', 'weight'
    ],
    "Health_Lifestyle": [
        'stress_level', 'heart_rate', 'daily_steps', 'physical_activity', 'bp_category',
        'medical_issue', 'ongoing_medication'
    ],
    "Substance_Use": [
        'caffeine_consumption', 'alcohol_consumption', 'smoking'
    ],
    "Device_Screen_Use": [
        'smart_device_before_bed', 'average_screen_time', 'blue-light_filter'
    ],
    "Eye_Health_Symptoms": [
        'discomfort_eye-strain', 'redness_in_eye', 'itchiness/irritation_in_eye'
    ]
}

# Map each feature to a category
feature_to_category = {
    'gender': 'Demographics', 'age': 'Demographics', 'height': 'Demographics', 'weight': 'Demographics',
    'stress_level': 'Health_Lifestyle', 'heart_rate': 'Health_Lifestyle', 'daily_steps': 'Health_Lifestyle',
    'physical_activity': 'Health_Lifestyle', 'bp_category': 'Health_Lifestyle',
    'medical_issue': 'Health_Lifestyle', 'ongoing_medication': 'Health_Lifestyle',
    'caffeine_consumption': 'Substance_Use', 'alcohol_consumption': 'Substance_Use', 'smoking': 'Substance_Use',
    'smart_device_before_bed': 'Device_Screen_Use', 'average_screen_time': 'Device_Screen_Use', 'blue-light_filter': 'Device_Screen_Use',
    'discomfort_eye-strain': 'Eye_Health_Symptoms', 'redness_in_eye': 'Eye_Health_Symptoms', 'itchiness/irritation_in_eye': 'Eye_Health_Symptoms'
}


# Define category-color mapping
category_colors = {
    "Demographics": "#1f77b4",        # blue
    "Health_Lifestyle": "#ff7f0e",    # orange
    "Substance_Use": "#2ca02c",       # green
    "Device_Screen_Use": "#d62728",   # red
    "Eye_Health_Symptoms": "#9467bd"  # purple
}



### Below is a function for generating lists of features present in the dataset:
def extract_features(df, feature_list):
    return [
    feature for feature in feature_list 
    if feature in df.columns 
]