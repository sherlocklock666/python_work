def city_country(city, country, population=''):
	if population:
		message = f"{city}, {country} - population {population}".title()
	else:
		message = f"{city}, {country}".title()
	return message

# city_country('beijing', 'china')