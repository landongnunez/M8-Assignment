# Module 8 Assignment

# Welcome message
print("=" * 60)
print("GLOBALTECH SOLUTIONS - CUSTOMER MANAGEMENT SYSTEM")
print("=" * 60)

# TODO 1: Create a dictionary of service categories and hourly rates
services = {
    "AI Consulting": 240,
    "Mobile App Development": 180,
    "Network Infrastructure": 160,
    "Database Management": 145,
    "Technical Support": 90
}

# TODO 2: Create customer dictionaries
customer1 = {
    "company_name": "Titan Group",
    "contact_person": "Author Storm",
    "email": "Mr.strom@titangroup.net",
    "phone": "813-555-1111"
}

customer2 = {
    "company_name": "Bright Solutions",
    "contact_person": "Emily Davis",
    "email": "emily@brightsolutions.com",
    "phone": "613-555-2222"
}

customer3 = {
    "company_name": "Queen Tech",
    "contact_person": "Oliver Queen",
    "email": "Ollie@queentech.com",
    "phone": "727-555-3333"
}

customer4 = {
    "company_name": "Doom Inc.",
    "contact_person": "Victor Doom",
    "email": "VicDoom@doomtech.net",
    "phone": "305-555-4444"
}

# TODO 3: Create a master customers dictionary
customers = {
    "C001": customer1,
    "C002": customer2,
    "C003": customer3,
    "C004": customer4
}

# TODO 4: Display all customers
print("\nAll Customers:")
print("-" * 60)

for cid, info in customers.items():
    print(cid, info)

# TODO 5: Look up specific customers
c002_info = customers["C002"]
c003_contact = customers["C003"]["contact_person"]
c999_info = customers.get("C999", "Customer not found")

print("\n\nCustomer Lookups:")
print("-" * 60)
print("C002 Info:", c002_info)
print("C003 Contact:", c003_contact)
print("C999 Lookup:", c999_info)

# TODO 6: Update customer information
customers["C001"]["phone"] = "555-9999"
customers["C002"]["industry"] = "Finance"

print("\n\nUpdating Customer Information:")
print("-" * 60)
print("Updated C001:", customers["C001"])
print("Updated C002:", customers["C002"])

# TODO 7: Create project dictionaries
project1 = {"name": "AI Chatbot Setup", "service": "AI Consulting", "hours": 100, "budget": 24000}
project2 = {"name": "Mobile Shopping App", "service": "Mobile App Development", "hours": 120, "budget": 21600}
project3 = {"name": "Office Network Upgrade", "service": "Network Infrastructure", "hours": 80, "budget": 12800}
project4 = {"name": "Customer Data System", "service": "Database Management", "hours": 60, "budget": 8700}
project5 = {"name": "Help Desk Support", "service": "Technical Support", "hours": 40, "budget": 3600}

projects = {
    "C001": [project1, project2],
    "C002": [project3],
    "C003": [project4],
    "C004": [project5]
}

print("\n\nProject Information:")
print("-" * 60)

for cid, plist in projects.items():
    print(cid, plist)

# TODO 8: Calculate project costs
print("\n\nProject Cost Calculations:")
print("-" * 60)

for cid, plist in projects.items():
    for p in plist:
        rate = services[p["service"]]
        cost = rate * p["hours"]
        print(p["name"], "- Cost:", cost)

# TODO 9: Customer statistics using dictionary methods
print("\n\nCustomer Statistics:")
print("-" * 60)

print("Customer IDs:", customers.keys())

companies = [c["company_name"] for c in customers.values()]
print("Customer Companies:", companies)

print("Total Customers:", len(customers))

# TODO 10: Service usage analysis
service_counts = {}

for plist in projects.values():
    for p in plist:
        s = p["service"]
        service_counts[s] = service_counts.get(s, 0) + 1

print("\n\nService Usage Analysis:")
print("-" * 60)
print(service_counts)

# TODO 11: Financial aggregations
all_hours = []
all_budgets = []

for plist in projects.values():
    for p in plist:
        all_hours.append(p["hours"])
        all_budgets.append(p["budget"])

total_hours = sum(all_hours)
total_budget = sum(all_budgets)
avg_budget = total_budget / len(all_budgets)
max_budget = max(all_budgets)
min_budget = min(all_budgets)

print("\n\nFinancial Summary:")
print("-" * 60)
print("Total Hours:", total_hours)
print("Total Budget:", total_budget)
print("Average Budget:", avg_budget)
print("Max Budget:", max_budget)
print("Min Budget:", min_budget)

# TODO 12: Customer summary report
print("\n\nCustomer Summary Report:")
print("-" * 60)

for cid, cust in customers.items():
    plist = projects.get(cid, [])
    hours = sum(p["hours"] for p in plist)
    budget = sum(p["budget"] for p in plist)

    print(cid, cust["company_name"])
    print("Projects:", len(plist))
    print("Total Hours:", hours)
    print("Total Budget:", budget)
    print()

# TODO 13: Rate adjustments using dictionary comprehension
adjusted_rates = {service: rate * 1.1 for service, rate in services.items()}

print("\n\nAdjusted Service Rates (10% increase):")
print("-" * 60)
print(adjusted_rates)

# TODO 14: Filter customers using dictionary comprehension
active_customers = {cid: customers[cid] for cid in customers if cid in projects}

print("\n\nActive Customers (with projects):")
print("-" * 60)
print(active_customers)

# TODO 15: Create project summaries using dictionary comprehension
customer_budgets = {cid: sum(p["budget"] for p in plist) for cid, plist in projects.items()}

print("\n\nCustomer Budget Totals:")
print("-" * 60)
print(customer_budgets)

# TODO 16: Service pricing tiers using dictionary comprehension
service_tiers = {
    s: ("Premium" if r >= 200 else "Standard" if r >= 100 else "Basic")
    for s, r in services.items()
}

print("\n\nService Pricing Tiers:")
print("-" * 60)
print(service_tiers)

# TODO 17: Customer validation function
def validate_customer(customer_dict):
    required = ["company_name", "contact_person", "email", "phone"]
    for field in required:
        if field not in customer_dict:
            return False
    return True

print("\n\nCustomer Validation:")
print("-" * 60)

for cid, cust in customers.items():
    print(cid, validate_customer(cust))

# TODO 18: Project status tracking
statuses = ["active", "completed", "pending"]
status_counts = {"active": 0, "completed": 0, "pending": 0}

i = 0
for plist in projects.values():
    for p in plist:
        p["status"] = statuses[i % 3]
        status_counts[p["status"]] += 1
        i += 1

print("\n\nProject Status Summary:")
print("-" * 60)
print(status_counts)

# TODO 19: Budget analysis function
def analyze_customer_budgets(projects_dict):
    result = {}

    for cid, plist in projects_dict.items():
        budgets = [p["budget"] for p in plist]
        total = sum(budgets)
        count = len(budgets)
        avg = total / count if count > 0 else 0

        result[cid] = {
            "total": total,
            "average": avg,
            "count": count
        }

    return result

print("\n\nDetailed Budget Analysis:")
print("-" * 60)

budget_analysis = analyze_customer_budgets(projects)
print(budget_analysis)

# TODO 20: Service recommendation system
def recommend_services(customer_id, customers, projects, services):

    used_services = set()

    for p in projects.get(customer_id, []):
        used_services.add(p["service"])

    recommendations = []

    for s in services:
        if s not in used_services:
            recommendations.append(s)

    return recommendations


print("\n\nService Recommendations:")
print("-" * 60)

for cid in customers:
    recs = recommend_services(cid, customers, projects, services)
    print(cid, "recommended services:", recs)
