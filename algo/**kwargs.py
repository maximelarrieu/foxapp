def capitals(title, ending='', **kwargs):
    print(title)
    for country, capital in kwargs.items():
        print("The capital of {} is {}".format(country, capital))
    if ending:
        print(ending)


capitals("List of countries", "Goodbye", France="Paris", Spain="Madrid")

keywords = {'France': 'Paris', 'Germany': 'Berlin'}
capitals("List of countries 2", "Goodbye", **keywords)
