from SPARQLWrapper import SPARQLWrapper, JSON


class Guru:
    def __init__(self, endpoint: str = 'https://query.wikidata.org/sparql'):
        self.endpoint = endpoint

    def __query_wikidata_and_get_prop(self, prop, query):
        sparql = SPARQLWrapper(self.endpoint)

        sparql.setQuery(query=query)
        sparql.setReturnFormat(JSON)
        results = sparql.query().convert()
        return results["results"]["bindings"][0][prop]['value'] if len(results) > 0 else -1 

    def __get_population_for_city(self, city_param):
        query = f"""SELECT ?city ?cityLabel ?population WHERE {{
            VALUES ?city {{ {city_param} }}.
                    ?city wdt:P1082 ?population .
            SERVICE wikibase:label {{ bd:serviceParam wikibase:language "en". }}  
        }}"""

        return self.__query_wikidata_and_get_prop('population', query)

    def __how_old_is_famous_person(self, person_param):
        query = f"""SELECT ?age WHERE {{   
            {person_param} wdt:P569 ?birth .
            BIND(now() as ?today)
                bind( year(?today) - year(?birth) - if(month(?today) < month(?birth) || (month(?today) = month(?birth) && day(?today)< day(?birth)), 1, 0) as ?age )
            SERVICE wikibase:label {{ bd:serviceParam wikibase:language "en". }}  
        }}"""

        return self.__query_wikidata_and_get_prop('age', query)

    def ask(self, question: str):
        match question:
            case 'how old is Tony Blair':
                tony_blair  = "wd:Q9545"
                return self.__how_old_is_famous_person(tony_blair)

            case 'how old is trump':
                donald_trump = "wd:Q22686"
                return self.__how_old_is_famous_person(donald_trump)

            case 'what is the population of London':
                london = "wd:Q84"
                return self.__get_population_for_city(london)
            
            case 'what is the population of Paris':
                paris = "wd:Q90"
                return self.__get_population_for_city(paris)

            case _:
                print("I am indeed a guru, but I don't have an answer to all of your questions!")


