import joblib


for i, model in enumerate(MODELS):
    joblib.dump(model, f'model_{i}.pkl')


loaded_models = [joblib.load(f'model_{i}.pkl') for i in range(len(MODELS))]
