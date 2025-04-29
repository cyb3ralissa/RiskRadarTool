import csv

# Function to read the vendor data
def read_vendor_data(file_name):
    vendors = []
    with open(file_name, mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            vendors.append(row)
    return vendors

# Function to calculate risk score based on simple criteria
def calculate_risk(vendor):
    risk_score = 0

    # Example criteria for risk scoring
    if vendor["Data Access"] == "Customer PII":
        risk_score += 2  # Higher risk for customer PII
    if "SOC 2" not in vendor["Compliance Certifications"]:
        risk_score += 1  # Increase risk if no SOC 2 certification

    # Example check for encryption
    if vendor["Encryption Used"] == "None":
        risk_score += 1  # Increase risk if no encryption used

    # Return calculated risk score
    return risk_score

# Function to assess vendors and output results
def assess_vendors(vendors):
    for vendor in vendors:
        risk_score = calculate_risk(vendor)
        print(f"Vendor: {vendor['Vendor Name']}, Risk Score: {risk_score}")
        # Add more output details as needed

# Main execution
if __name__ == "__main__":
    # Read the vendor data
    vendors = read_vendor_data("sample_vendor_data.csv")
    # Assess the vendors
    assess_vendors(vendors)
