"""Find duplicate elements."""


companies = ["TCS", "Tech Mahindra", "Odoo", "TCS", "Accenture", "IBM", "Odoo"]
seen = set()
duplicate_companies_list = []

for _, company in enumerate(companies):
    if company not in seen:
        seen.add(company)
    else:
        duplicate_companies_list.append(company)

print(f"Duplicate companies: {duplicate_companies_list}")
