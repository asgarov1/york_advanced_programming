PADDING_LENGTH = 16

data = {
    'April 18': {'L3': 390, 'P2': 250, 'N6': 460, 'B8': 470},
    'May 18': {'L3': 345, 'P2': 270, 'N6': 480, 'B8': 510},
    'June 18': {'L3': 379, 'P2': 300, 'N6': 450, 'B8': 360},
}
company_names = {'L3': 'London', 'P2': 'Paris', 'N6': 'New York', 'B8': 'Beijing'}


def get_grand_total():
    result = 0
    for month in data.values():
        result += sum(month.values())

    result += sum(get_totals_for_companies().values())
    return result


def get_totals_for_companies():
    company_total = {}
    for month in data:
        for company in data[month]:
            company_total[company] = company_total.get(company, 0) + data[month][company]
    return company_total


def print_stats_per_company():
    companies_total = get_totals_for_companies()
    for company in companies_total:
        average = companies_total[company] / len(data.keys())
        company_name = company_names.get(company)
        print(
            f' {company_name}{company.rjust(PADDING_LENGTH - len(company_name))}: {average:.2f} {companies_total[company]}')


def print_stats_per_month():
    for index, month in enumerate(data.values()):
        date = list(data.keys())[index]
        total = sum(month.values())
        average = total / len(month.values())
        print(f' {(date[0:3] + date[-2:]).ljust(PADDING_LENGTH)}: {average:.2f} {total}')


print(' Quarterly sales report\n')
print_stats_per_company()
print()
print_stats_per_month()
print(f'\n Total: {get_grand_total()}')
