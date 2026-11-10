"""Legacy data importer -- INTENTIONALLY INSECURE."""
import pickle


def load_session(blob: bytes):
    # Deserializing untrusted bytes can execute arbitrary code.
    return pickle.loads(blob)


def compute_discount(expression: str):
    # "Flexible" pricing rules typed in by an admin.
    return eval(expression)
