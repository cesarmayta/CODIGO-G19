import requests

class GitHubProfile:
    
    def __init__(self):
        self.url_base = 'https://api.github.com/users/cesarmayta'
        dataPerfil = requests.get(self.url_base).json()
        self.nombre = dataPerfil['name']
        self.biografia = dataPerfil['bio']
        self.imagen = dataPerfil['avatar_url']
        self.ubicacion = dataPerfil['location']
        self.twitter = dataPerfil['twitter_username']
        self.github = dataPerfil['html_url']
        
        
#gb = GitHubProfile()
#print(gb.dataPerfil['name'])