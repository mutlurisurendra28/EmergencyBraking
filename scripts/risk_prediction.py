def predict_risk(distance, label):

    if label == "person":

        if distance < 2:
            return "HIGH"

        elif distance < 4:
            return "MEDIUM"

        else:
            return "LOW"

    elif label in ["car","bus","motorbike","bicycle"]:

        if distance < 3:
            return "HIGH"

        elif distance < 6:
            return "MEDIUM"

        else:
            return "LOW"

    else:
        return "LOW"