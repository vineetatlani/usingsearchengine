from algoliasearch.search_client import SearchClient

client = SearchClient.create('FOL57BHXOW', '045e466101d4cf13e7ee4b16c889d2f6')
index = client.init_index('dev_MYBLOG')


dict = {
    "objectID": 5,
    "title": "My title",
    "content": "This is my content"
}

index.save_object(dict)