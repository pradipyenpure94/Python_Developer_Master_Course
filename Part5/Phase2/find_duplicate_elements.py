"""Find duplicate elements."""


companies = ["TCS", "Tech Mahindra", "Odoo", "TCS", "Accenture", "IBM", "Odoo"]
seen = set()
duplicate_companies_list = []
n = len(companies)
index = 0

while index < n:
    if companies[index] not in seen:
        seen.add(companies[index])
    else:
        duplicate_companies_list.append(companies[index])
    index += 1

print(f"Duplicate companies: {duplicate_companies_list}")
