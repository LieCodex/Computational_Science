data = [
    ("Rainy", "Hot", "High", False, "No"),
    ("Rainy", "Hot", "High", True, "No"),
    ("Overcast", "Hot", "High", False, "Yes"),
    ("Sunny", "Mild", "High", False, "Yes"),
    ("Sunny", "Cool", "Normal", False, "Yes"),
    ("Sunny", "Cool", "Normal", True, "No"),
    ("Overcast", "Cool", "Normal", True, "Yes"),
    ("Rainy", "Mild", "High", False, "No"),
    ("Rainy", "Cool", "Normal", False, "Yes"),
    ("Sunny", "Mild", "Normal", False, "Yes"),
    ("Rainy", "Mild", "Normal", True, "Yes"),
    ("Overcast", "Mild", "High", True, "Yes"),
    ("Overcast", "Hot", "Normal", False, "Yes"),
    ("Sunny", "Mild", "High", True, "No"),
]

total_yes = sum(1 for d in data if d[4] == "Yes")
total_no = sum(1 for d in data if d[4] == "No")
total = len(data)

P_yes = total_yes / total
P_no = total_no / total

def likelihood(feature_index, feature_value, play_golf_value): 
    count_feature = sum(1 for d in data if d[feature_index] == feature_value and d[4] == play_golf_value)
    count_play_golf = total_yes if play_golf_value == "Yes" else total_no
    return count_feature / count_play_golf if count_play_golf != 0 else 0


features = ["Rainy", "Mild", "High", False]


P_features_given_yes = 1
P_features_given_no = 1
for i in range(4): 
    P_features_given_yes *= likelihood(i, features[i], "Yes")
    P_features_given_no *= likelihood(i, features[i], "No")


P_yes_given_features = P_features_given_yes * P_yes
P_no_given_features = P_features_given_no * P_no


prediction = "Yes" if P_yes_given_features > P_no_given_features else "No"

print(f"P(Yes | features) = {P_yes_given_features}")
print(f"P(No | features) = {P_no_given_features}")
print(f"Prediction: Play Golf? {prediction}")
