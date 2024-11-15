# importing and initializing Exa with API key
from exa_py import Exa
exa = Exa('4c1199ac-a5da-446e-a911-258e09d57665')

# Creating a variable called "query" to hold the response to the input
query = input('Search here: ')

response = exa.search(
  query,
  num_results=5,
  type='keyword',
  include_domains=['google.com', 'news.google.com', 'hindustantimes.com']
)

# Print or process the response
print(response)
