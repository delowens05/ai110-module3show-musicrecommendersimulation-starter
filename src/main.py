"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from .recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv")

    user_prefs = {
        "favorite_genre":  "pop",
        "favorite_mood":   "happy",
        "target_energy":   0.60,
        "likes_acoustic":  0.57,
        "target_valence":  0.65,
        "target_tempo":    90.0,
    }

    recommendations = recommend_songs(user_prefs, songs, k=5)

    print("\n" + "=" * 44)
    print(f"  Top {len(recommendations)} Recommendations")
    print("=" * 44)

    for rank, (song, score, explanation) in enumerate(recommendations, start=1):
        print(f"\n#{rank}  {song['title']} — {song['artist']}")
        print(f"    Score : {score:.2f} / 7.5")
        print(f"    Genre : {song['genre']}  |  Mood: {song['mood']}")
        print(f"    Why   : {explanation}")

    print("\n" + "=" * 44 + "\n")


if __name__ == "__main__":
    main()
