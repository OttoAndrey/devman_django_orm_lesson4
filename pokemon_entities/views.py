import folium
from django.shortcuts import render, get_object_or_404

from pokemon_entities.models import Pokemon, PokemonEntity

MOSCOW_CENTER = [55.751244, 37.618423]
DEFAULT_IMAGE_URL = "https://vignette.wikia.nocookie.net/pokemon/images/6/6e/%21.png/revision/latest/fixed-aspect-ratio-down/width/240/height/240?cb=20130525215832&fill=transparent"


def add_pokemon(folium_map, lat, lon, name, stats, image_url=DEFAULT_IMAGE_URL):
    icon = folium.features.CustomIcon(
        image_url,
        icon_size=(50, 50),
    )
    folium.Marker(
        [lat, lon],
        tooltip=name,
        icon=icon,
        popup=folium.Popup(stats, parse_html=True, max_width=75),
    ).add_to(folium_map)


def show_all_pokemons(request):
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)

    pokemon_entities = PokemonEntity.objects.all()
    for pokemon_entity in pokemon_entities:
        pokemon_stats = f"""
            level: {pokemon_entity.level}
            health: {pokemon_entity.health}
            strength: {pokemon_entity.strength}
            defence: {pokemon_entity.defence}
            stamina: {pokemon_entity.stamina}
        """

        add_pokemon(
            folium_map, pokemon_entity.lat, pokemon_entity.lon,
            pokemon_entity.pokemon.title, pokemon_stats, request.build_absolute_uri(pokemon_entity.pokemon.image.url))

    pokemons_on_page = []
    pokemons = Pokemon.objects.all()
    for pokemon in pokemons:
        pokemons_on_page.append({
            'pokemon_id': pokemon.id,
            'img_url': pokemon.image.url,
            'title_ru': pokemon.title,
        })

    return render(request, "mainpage.html", context={
        'map': folium_map._repr_html_(),
        'pokemons': pokemons_on_page,
    })


def show_pokemon(request, pokemon_id):
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)

    pokemon = get_object_or_404(Pokemon, pk=pokemon_id)

    pokemon_data = {
        'title_ru': pokemon.title,
        'title_en': pokemon.title_en,
        'title_jp': pokemon.title_jp,
        'img_url': pokemon.image.url,
        'description': pokemon.description,
    }

    if pokemon.previous_evolution:
        pokemon_data['previous_evolution'] = {
            "title_ru": pokemon.previous_evolution.title,
            "pokemon_id": pokemon.previous_evolution.id,
            "img_url": pokemon.previous_evolution.image.url,
        }

    if pokemon.next_evolutions.first():
        pokemon_data['next_evolution'] = {
            "title_ru": pokemon.next_evolutions.first().title,
            "pokemon_id": pokemon.next_evolutions.first().id,
            "img_url": pokemon.next_evolutions.first().image.url,
        }

    pokemon_element_types =[]
    if pokemon.element_type.all():
        for element_type in pokemon.element_type.all():
            pokemon_element_types.append({
                'title': element_type.title,
                'img': element_type.image.url,
            })
        pokemon_data['element_type'] = pokemon_element_types

    for pokemon_entity in pokemon.entities.all():
        pokemon_stats = f"""
                    level: {pokemon_entity.level}
                    health: {pokemon_entity.health}
                    strength: {pokemon_entity.strength}
                    defence: {pokemon_entity.defence}
                    stamina: {pokemon_entity.stamina}
                """

        add_pokemon(
            folium_map, pokemon_entity.lat, pokemon_entity.lon,
            pokemon_entity.pokemon.title, pokemon_stats, request.build_absolute_uri(pokemon_entity.pokemon.image.url))

    return render(request, "pokemon.html", context={'map': folium_map._repr_html_(),
                                                    'pokemon': pokemon_data})
