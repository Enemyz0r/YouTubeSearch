import webbrowser

query = input("Please enter your search input: ")

base_url = "http://www.youtube.com/results?search_query="

final_url = base_url + query
webbrowser.open(final_url)
