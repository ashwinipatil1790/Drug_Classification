import pickle
import numpy as np

def predict_drug_type(age, Na_to_K, sex, bp, cholesterol):
    drug_pickle_path = r"artifacts\Logistic_Reg_Drug.pkl"
    
    with open(drug_pickle_path, 'rb') as f:
        model = pickle.load(f)

    test_array = np.array([[age, Na_to_K, sex, bp, cholesterol]])
    drug_type = model.predict(test_array)[0]

    return drug_type

