from data.file_storage import FileStorage

storage = FileStorage()

country_data = storage.load_model_data('data/country.json')

place_data = storage.load_model_data('data/place.json')

amenity_data = storage.load_model_data('data/amenity.json')

place_to_amenity_data = storage.load_model_data('data/place_to_amenity.json')

user_data = storage.load_model_data('data/user.json')

review_data = storage.load_model_data('data/review.json')

city_data = storage.load_model_data("data/city.json")

