student = {
    "name" : "Agostino Scholes",
    "school" : "Shenyang city university",
    "hours_coded" : 100
}

student['learning'] = "python"

work = f"{student["name"]} is learning {student['learning']}"

print(work)


confidence = 0.6

if confidence > 0.90:
    print("Highly confident")
elif confidence >= 0.70:
    print("Moderately Confident")
else:
    print("Low Confidence")


error_rate = 0.02

if error_rate > 0.15:
    print("Model needs serious retraining") 
elif 0.05 <= error_rate <= 0.20:
    print("Model perfomance is acceptable")
else:
    print("Model is highly optimised")    