"""
Adversarial / edge-case profile runner for the Music Recommender.

Each profile is designed to expose a potential weakness or surprising
behaviour in the scoring function.  Run from the project root:

    python adversarial_profiles.py
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

from recommender import load_songs, recommend_songs

CSV = os.path.join(os.path.dirname(__file__), "data", "songs.csv")

# ---------------------------------------------------------------------------
# Adversarial profiles
# ---------------------------------------------------------------------------
PROFILES = [
    {
        "name": "1 · The Contradiction",
        "description": (
            "Wants 'chill' mood BUT energy 0.9 — those are opposite ends of the "
            "catalog.  Every chill song has energy < 0.45.  Does the +2.0 mood "
            "bonus drag a sleepy track past high-energy songs?"
        ),
        "prefs": {
            "favorite_genre": "lofi",
            "favorite_mood":  "chill",
            "target_energy":  0.90,
            "likes_acoustic": 0.20,
            "target_valence": 0.65,
            "target_tempo":   130.0,
        },
    },
    {
        "name": "2 · The Ghost Genre",
        "description": (
            "'k-pop' does not exist in the catalog — the +2.0 genre bonus is "
            "never earned.  Ranking is 100 % continuous-attribute driven.  "
            "What rises when the biggest flat bonus is permanently off the table?"
        ),
        "prefs": {
            "favorite_genre": "k-pop",
            "favorite_mood":  "happy",
            "target_energy":  0.80,
            "likes_acoustic": 0.20,
            "target_valence": 0.80,
            "target_tempo":   120.0,
        },
    },
    {
        "name": "3 · The Acoustic Rager",
        "description": (
            "Wants max acousticness (1.0) AND max energy (1.0) — physically "
            "contradictory.  Highly acoustic songs in the catalog are calm "
            "(energy < 0.40).  High-energy songs are nearly all non-acoustic.  "
            "Which dimension wins the trade-off?"
        ),
        "prefs": {
            "favorite_genre": "blues",
            "favorite_mood":  "angry",
            "target_energy":  1.00,
            "likes_acoustic": 1.00,
            "target_valence": 0.30,
            "target_tempo":   90.0,
        },
    },
    {
        "name": "4 · The Tempo Extremist",
        "description": (
            "target_tempo = 250 BPM — far beyond the catalog's maximum of 178.  "
            "The window is 100 BPM, so any song below 150 BPM scores 0 tempo "
            "points, and even the fastest song only earns ~0.14.  Does tempo "
            "become irrelevant, and how do genre/mood bonuses fill the vacuum?"
        ),
        "prefs": {
            "favorite_genre": "metal",
            "favorite_mood":  "angry",
            "target_energy":  0.90,
            "likes_acoustic": 0.05,
            "target_valence": 0.30,
            "target_tempo":   250.0,
        },
    },
    {
        "name": "5 · The Dead-Center Profile",
        "description": (
            "Every continuous target is exactly 0.5 — the mathematical midpoint "
            "of each 0–1 scale.  No song can score above 50 % on any continuous "
            "axis.  The +2.0 genre and mood flat bonuses completely dominate.  "
            "Does the top-5 reduce to 'whichever songs share genre or mood'?"
        ),
        "prefs": {
            "favorite_genre": "lofi",
            "favorite_mood":  "chill",
            "target_energy":  0.50,
            "likes_acoustic": 0.50,
            "target_valence": 0.50,
            "target_tempo":   100.0,
        },
    },
]

# ---------------------------------------------------------------------------
# Runner
# ---------------------------------------------------------------------------
def run_profile(songs, profile):
    print("\n" + "=" * 60)
    print(f"  {profile['name']}")
    print("=" * 60)
    print(f"  {profile['description']}")
    print()
    print("  Prefs:", {k: v for k, v in profile["prefs"].items()})
    print()

    results = recommend_songs(profile["prefs"], songs, k=5)

    for rank, (song, score, explanation) in enumerate(results, start=1):
        print(f"  #{rank}  {song['title']} — {song['artist']}")
        print(f"       Score : {score:.4f} / 7.5")
        print(f"       Genre : {song['genre']}  |  Mood: {song['mood']}  |  Energy: {song['energy']}")
        print(f"       Why   : {explanation}")
        print()


def main():
    songs = load_songs(CSV)
    print("\n*** Adversarial Profile Runner ***")
    print(f"    Catalog size: {len(songs)} songs")
    print(f"    Max possible score: 7.5 (genre+mood+energy+valence+acoustic+tempo)")

    for profile in PROFILES:
        run_profile(songs, profile)

    print("=" * 60)
    print("  Done.\n")


if __name__ == "__main__":
    main()
