import requests

url = r'https://api.github.com/users/Pineson86'

def get_git_info(url):
    #Getting page content from url
    try:
        response = requests.get(url)
        page_content = response.json()
    except Exception as E:
        return f'Page does not response because the error: {E}'
    #Getting required strings from the page content
    login = page_content.get('login', '"login" has been not found')
    public_repos = page_content.get('public_repos', '"public_repos" has been not found')
    return f'Login: {login}, Public_repos: {public_repos}'

print(get_git_info(url))