import csv
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str = "hip-hop"
    favorite_mood: str = "chill"
    target_energy: float = 0.60
    likes_acoustic: float = 0.57
    target_valence: float = 0.65
    target_tempo: float = 90.0

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """Loads and parses songs from a CSV file into a list of dicts."""
    int_fields = {"id"}
    float_fields = {"energy", "tempo_bpm", "valence", "danceability", "acousticness"}
    songs = []
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            for field in int_fields:
                row[field] = int(row[field])
            for field in float_fields:
                row[field] = float(row[field])
            songs.append(row)
    return songs

#heres where u neeed to implement the scoring and recommendation logic for the functional approach.
def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Returns a numeric score and list of reasons for how well a song matches user preferences."""
    score = 0.0
    reasons = []

    # Genre match (+2.0)
    if song["genre"] == user_prefs["favorite_genre"]:
        score += 2.0
        reasons.append("genre match (+2.0)")

    # Mood match (+2.0)
    if song["mood"] == user_prefs["favorite_mood"]:
        score += 2.0
        reasons.append("mood match (+2.0)")

    # Energy fit — weighted 1.5, highest numerical priority
    # similarity = 1 - |song_value - target|  (both are 0–1 scale)
    energy_points = round((1.0 - abs(song["energy"] - user_prefs["target_energy"])) * 1.5, 2)
    score += energy_points
    reasons.append(f"energy fit (+{energy_points})")

    # Valence fit — weighted 0.75
    valence_points = round((1.0 - abs(song["valence"] - user_prefs["target_valence"])) * 0.75, 2)
    score += valence_points
    reasons.append(f"valence fit (+{valence_points})")

    # Acousticness fit — weighted 0.75
    acoustic_points = round((1.0 - abs(song["acousticness"] - user_prefs["likes_acoustic"])) * 0.75, 2)
    score += acoustic_points
    reasons.append(f"acousticness fit (+{acoustic_points})")

    # Tempo fit — weighted 0.5, normalized over a 100 BPM window
    tempo_sim = max(0.0, 1.0 - abs(song["tempo_bpm"] - user_prefs["target_tempo"]) / 100)
    tempo_points = round(tempo_sim * 0.5, 2)
    score += tempo_points
    reasons.append(f"tempo fit (+{tempo_points})")

    return round(score, 4), reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Returns the top-k songs sorted by score along with their match reasons."""
    scored = [
        (song, score, ", ".join(reasons))
        for song in songs
        for score, reasons in [score_song(user_prefs, song)]
    ]
    ranked = sorted(scored, key=lambda x: x[1], reverse=True)
    return ranked[:k]
