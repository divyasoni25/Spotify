import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Replace these values with your own Spotify API credentials
client_id = 'b054e41f597e45a8b9d52bb6c1feb6c7'
client_secret = '06134e47cfcb4e489393119493125188'

# Set up Spotify API credentials
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def get_recommendations(seed_tracks, limit=10):
    # Get song recommendations based on seed tracks
    recommendations = sp.recommendations(seed_tracks=seed_tracks, limit=limit)
    return recommendations['tracks']

def search_track(query, limit=1):
    # Search for a track using the query
    results = sp.search(q=query, type='track', limit=limit)
    return results['tracks']['items']

def main():
    # Example usage
    user_preference = input("Enter a song or artist for recommendations: ")
    print("You entered:", user_preference)  # Add this line to check if input is working

    # Search for the provided song or artist
    search_results = search_track(user_preference)

    if not search_results:
        print("Song or artist not found. Please try again.")
        return

    seed_track_id = search_results[0]['id']
    
    # Get recommendations based on the seed track
    recommendations = get_recommendations(seed_tracks=[seed_track_id])

    print("\nRecommendations:")
    for i, track in enumerate(recommendations):
        print(f"{i + 1}. {track['name']} by {', '.join([artist['name'] for artist in track['artists']])}")

if __name__ == "__main__":
    main()
