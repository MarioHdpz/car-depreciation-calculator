"""Kavak's data acquisition"""
import pymongo
from algoliasearch.search_client import SearchClient


def get_all_cars():
    """Retrieve all cars data"""
    client = SearchClient.create("app_id", "admin_api_key")
    index = client.init_index("prod_Kavak")

    myclient = pymongo.MongoClient(
        "mongodb://user:passwprd@localhost:27017/?authSource=admin"
    )
    mydb = myclient["kavak"]

    for page in range(7, 9):
        response = index.search("", {"page": page, "hitsPerPage": 1000})
        results = response["hits"]

        mycol = mydb["cars"]
        mycol.insert_many(results)


if __name__ == "__main__":
    get_all_cars()
