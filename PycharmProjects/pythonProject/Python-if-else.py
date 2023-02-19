# age = 17
#
# # if age >= 18 and age <=50:
# #     print(f"Du bist {age} Jahre alt. Einlass erlaubt!")
# # elif age < 18:
# #     print(f"Du bist ja erst {age}! Sorry, heute nicht.")
# # else:
# #     print(f"Mit {age} Jahren bist Du leider zu alt ...")
#
#
# if age <= 6:
#     print(f"Du bist {age} Jahre und alt und kommst kostenfrei rein")
# elif age > 6 or age <= 60:
#     print(f"Du bist {age} und zahlst den vollen Eintrittspreis")
# else:
#     print(f"Du bist {age} und bekommst Rabatt")
#

# cities = ["Berlin", "Madrid", "Paris"]
#
# if "Madrid" in cities:
#     print("Ist enthaltem")
# else:
#     print("Nö")

monthly_revenues = [
    1000, 2000, 3000, 2500, 1500, 800, 2200, 2600, 3000, 2100, 2000, 1800
]
total = sum(monthly_revenues)
total_count_best_months = 0
total_best_months = 0
schwelle = 2800

for revenue in monthly_revenues:
    if revenue >= schwelle:
        total_best_months += revenue
        total_count_best_months += 1

print(f"Total revenue: {total}€, total of best months: {total_best_months}€, number of best months with more than {schwelle}€ turnover: {total_count_best_months}")
