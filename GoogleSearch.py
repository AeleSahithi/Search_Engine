# importing and initialising exa with API key S
from exa_py import Exa
exa = Exa('4c1199ac-a5da-446e-a911-258e09d57665')

# Creating a Variable called  "query" , which will hold the response to the input 

query = input('Search here: ')

response = exa.search(
  query,
  num_results=5,
  type='keyword',
  include_domains=['https://www.google.com/'],
)

for result in response.results:
  print(f'Title: {result.title}')
  print(f'URL: {result.url}')
  print()