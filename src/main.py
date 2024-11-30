from podcastfy.client import generate_podcast
import yaml
import os

def load_config():
    with open('config.yaml', 'r') as file:
        return yaml.safe_load(file)

def create_podcast(url):
    try:
        config = load_config()
        audio_file = generate_podcast(
            urls=[url],
            language=config['defaults']['language'],
            style=config['defaults']['style']
        )
        print(f'Podcast created successfully: {audio_file}')
        return audio_file
    except Exception as e:
        print(f'Error creating podcast: {e}')
        return None

if __name__ == '__main__':
    # Example usage
    test_url = 'https://example.com'
    create_podcast(test_url)
