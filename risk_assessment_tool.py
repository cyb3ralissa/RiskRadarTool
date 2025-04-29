import csv

# Function to read the vendor data
def read_vendor_data(file_name):
    vendors = []
    with open(file_name, mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            vendors.append(row)
    return vendors

# Function to calculate risk score based on multiple criteria
def calculate_risk(vendor):
    risk_score = 0

    # Example criteria for risk scoring
    if vendor["Data Access"] == "Customer PII":
        risk_score += 3  # Higher risk for customer PII
    elif vendor["Data Access"] == "Financial Data":
        risk_score += 2  # Moderate risk for financial data

    # SOC 2 certification adds trust, lack of it increases risk
    if "SOC 2" not in vendor["Compliance Certifications"]:
        risk_score += 2

    # Add risk if encryption is missing
    if vendor["Encryption Used"] == "None":
        risk_score += 2
    elif vendor["Encryption Used"] == "AES-128":
        risk_score += 1  # Slightly better than no encryption, but not ideal

    # Risk based on third-party storage (more risk if data is stored externally)
    if vendor["Third-party Storage"] == "Yes":
        risk_score += 1

    return risk_score

# Function to assess vendors and output results
def assess_vendors(vendors):
    results = []
    for vendor in vendors:
        risk_score = calculate_risk(vendor)
        risk_level = "High" if risk_score >= 5 else "Moderate" if risk_score >= 3 else "Low"
        result = {
            "Vendor Name": vendor["Vendor Name"],
            "Risk Score": risk_score,
            "Risk Level": risk_level,
            "Recommendations": generate_recommendations(risk_score)
        }
        results.append(result)
    return results

# Function to generate recommendations based on risk score
def generate_recommendations(risk_score):
    if risk_score >= 5:
        return "Urgent: Implement stricter controls and certifications."
    elif risk_score >= 3:
        return "Moderate: Consider conducting a detailed security audit."
    else:
        return "Low: Regular monitoring and compliance checks recommended."

# Function to write the assessment results to a CSV file
def write_results_to_csv(results, output_filename="assessment_results.csv"):
    keys = results[0].keys()  # Get the header from the first result
    with open(output_filename, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=keys)
        writer.writeheader()
        writer.writerows(results)

# Main execution
if __name__ == "__main__":
    # Read the vendor data
    vendors = read_vendor_data("sample_vendor_data.csv")
    # Assess the vendors
    results = assess_vendors(vendors)
    # Write results to a CSV file
    write_results_to_csv(results)
    # Print results to the console for immediate feedback
    for result in results:
        print(f"Vendor: {result['Vendor Name']}, Risk Level: {result['Risk Level']}, Risk Score: {result['Risk Score']}")
        print(f"Recommendations: {result['Recommendations']}")
        print()

