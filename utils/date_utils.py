def add_years_to_date(original_date, years_to_add):
    result = original_date.replace(year=original_date.year + years_to_add)
    return result

def substract_years_to_date(original_date, years_to_substract):
    result = original_date.replace(year=original_date.year - years_to_substract)
    return result