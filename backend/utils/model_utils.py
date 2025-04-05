import joblib

def save_model(model, filename):
    joblib.dump(model, filename)

def load_model(filename):
    return joblib.load(filename)


def save_encoder(encoder, filename):
    joblib.dump(encoder, filename)

def load_encoder(filename):
    return joblib.load(filename)