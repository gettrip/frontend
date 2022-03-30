from flask import Blueprint, render_template

view = Blueprint('places', __name__)


@view.route('/<route_id>/')
def show_places_for_route(city_id, route_id):
    routes = {
        '1': {
            'name': 'Музеи Калининграда за 1 день',
            'places': [
                'Музей янтаря',
                'Музей Мирового океана',
                'Историко-художественный музей',
                'Музей «Бункер»',
                'Музей марципана',
                'Кенигсбергский собор'],
            'description': 'Музейная программа в городе может быть настолько насыщенной,\
             что и целого дня не хватит для основных экспозиций.'
        },
        '2': {
            'name': 'Three paks',
            'places': ['park1', 'park2', 'park3'],
            'description': 'Three paks'
        },
        '3': {
            'name': 'Two museums and a park',
            'places': ['museum1', 'park2', 'museum3'],
            'description': 'Two museums and a park'
        },
    }
    route = routes[route_id]
    city_name = 'Калининград'
    route_name = route['name']
    route_description = route['description']
    places = route['places']

    return render_template(
        'places_on_route.html',
        city_name=city_name,
        route_name=route_name,
        route_description=route_description,
        places=places,
    )
