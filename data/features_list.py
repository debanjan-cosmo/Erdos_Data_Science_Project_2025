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



### Below is a function for generating lists of features present in the dataset:
def extract_features(df, feature_list):
    return [
    feature for feature in feature_list 
    if feature in df.columns 
]