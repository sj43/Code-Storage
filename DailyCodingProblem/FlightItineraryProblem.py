def get_itinerary(flights, flight_plan):
    if not flights:
        return flight_plan

    last_stop = flight_plan[-1]

    for i, (coming_from, going_to) in enumerate(flights):
        flight_minus_current = flights[:i] + flights[i+1:]
        flight_plan.append(going_to)
        if coming_from == last_stop:
            return get_itinerary(flight_minus_current, flight_plan)
        flight_plan.pop()

    return None

print(get_itinerary([('HNL','AKL'),('YUL','ORD'),('ORD','SFO'),('SFO','HNL')],['YUL']))
