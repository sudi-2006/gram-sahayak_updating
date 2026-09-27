import os
import joblib
import numpy as np
import pandas as pd

from step23_environmental_inputs import get_environmental_inputs


# ============================================================
# PATH SETUP
# ============================================================

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_PATH = os.path.join(
    SCRIPT_DIR,
    "models",
    "yield_model.pkl"
)


# ============================================================
# LOAD MODEL
# ============================================================

print("Loading production yield model...")

model_package = joblib.load(MODEL_PATH)

model = model_package["model"]
preprocessor = model_package["preprocessor"]

print("Production model loaded successfully.")


# ============================================================
# PREDICTION FUNCTION
# ============================================================

def predict_yield(
    state,
    crop_type,
    crop,
    area_in_hectares
):
    """
    Predict crop yield and total production.

    Inputs:
        state              : State name
        crop_type          : kharif / rabi / summer / whole year
        crop               : Crop name
        area_in_hectares   : Farm area in hectares

    Returns:
        Dictionary containing environmental inputs,
        predicted yield and predicted production.
    """

    # --------------------------------------------------------
    # Validate area
    # --------------------------------------------------------

    area_in_hectares = float(area_in_hectares)

    if area_in_hectares <= 0:
        raise ValueError(
            "Area must be greater than 0 hectares."
        )


    # --------------------------------------------------------
    # Get automatic rainfall + temperature
    # --------------------------------------------------------

    environmental = get_environmental_inputs(
        state,
        crop_type
    )

    rainfall = environmental["rainfall"]
    temperature = environmental["temperature"]


    # --------------------------------------------------------
    # Feature engineering
    # --------------------------------------------------------

    log_area = np.log1p(area_in_hectares)

    rainfall_squared = rainfall ** 2

    temperature_squared = temperature ** 2

    rainfall_temperature = rainfall * temperature


    # --------------------------------------------------------
    # Create model input
    # --------------------------------------------------------

    input_data = pd.DataFrame({

        "State_Name": [state],

        "Crop_Type": [crop_type],

        "Crop": [crop],

        "rainfall": [rainfall],

        "temperature": [temperature],

        "Area_in_hectares": [area_in_hectares],

        "log_area": [log_area],

        "rainfall_squared": [rainfall_squared],

        "temperature_squared": [temperature_squared],

        "rainfall_temperature": [
            rainfall_temperature
        ]

    })


    # --------------------------------------------------------
    # Preprocess
    # --------------------------------------------------------

    encoded_input = preprocessor.transform(
        input_data
    )


    # --------------------------------------------------------
    # Predict log-transformed yield
    # --------------------------------------------------------

    predicted_log_yield = model.predict(
        encoded_input
    )[0]


    # --------------------------------------------------------
    # Convert back from log1p
    # --------------------------------------------------------

    predicted_yield = np.expm1(
        predicted_log_yield
    )


    # Prevent negative prediction
    predicted_yield = max(
        float(predicted_yield),
        0.0
    )


    # --------------------------------------------------------
    # Calculate total production
    # --------------------------------------------------------

    predicted_production = (
        predicted_yield *
        area_in_hectares
    )


    # --------------------------------------------------------
    # Return result
    # --------------------------------------------------------

    return {

        "state": environmental["state"],

        "crop_type": environmental["crop_type"],

        "crop": crop,

        "area_in_hectares": area_in_hectares,

        "rainfall": rainfall,

        "temperature": temperature,

        "predicted_yield_ton_per_hectare":
            predicted_yield,

        "predicted_production_tons":
            predicted_production

    }


# ============================================================
# TEST
# ============================================================

if __name__ == "__main__":

    print("\n" + "=" * 65)
    print("       GRAM SAHAYAK - YIELD PREDICTION TEST")
    print("=" * 65)

    result = predict_yield(
        state="karnataka",
        crop_type="kharif",
        crop="Rice",
        area_in_hectares=2
    )

    print("\nPrediction result:")
    print("-" * 65)

    for key, value in result.items():

        if isinstance(value, float):
            print(
                f"{key}: {value:.4f}"
            )
        else:
            print(
                f"{key}: {value}"
            )

    print("-" * 65)
    print("Prediction completed successfully.")