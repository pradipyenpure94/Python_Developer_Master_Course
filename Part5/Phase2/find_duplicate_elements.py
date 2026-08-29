"""Find duplicate elements."""


companies = ["TCS", "Tech Mahindra", "Odoo", "TCS", "Accenture", "IBM", "Odoo"]
seen = set()

duplicate_companies_list = [
    company for company in companies if (
        company in seen or seen.add(company)
    )
]

print(f"Duplicate companies: {duplicate_companies_list}")
