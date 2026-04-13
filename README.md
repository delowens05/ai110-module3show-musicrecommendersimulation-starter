# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

---

## How The System Works

Real-world platforms like Spotify or YouTube learn your taste by watching what you play, skip, and save, then finding patterns across other listeners who behave and listen similarly. That works well, but takes a lot of data and it is hard to explain. However my version takes a simpler and more vauqe approach. it looks directly at the qualities of each song like energy level, emotional tone, and whether it feels acoustic or produced. It then compares them against what a user says they prefer. Songs that are closer to thw users preferences score higher, and the top matches get recommended. The system priorties energy, since that tends to be the one thing listeners feel most immediately when listening to a song and treats genre and mood as signals rather than strict rules.

Each song tracks seven components: genre, mood, energy, tempo, valence, danceability, and acousticness. Each user profile stores four preferences: a favorite genre, a favorite mood, a target energy level, and whether they like acoustic music. 

Algorithm Recipe: Each song is scored out of a maximum of 7.5 points where: 

- genre match earns +2.0, mood match earns +2.0, and the remaining 3.5 points come from how closely the song's energy, valence, acousticness, and tempo match the user's targets. 

- Songs are then ranked by total score and the top K are returned. 

- One thing id look out for is that genre and mood together make up more than half the possible score, so a song that perfectly matches a user's energy and vibe but falls into an unfamiliar genre will often lose to a weaker fit that just happens to share the same genre label.

Screen Shot: 
![alt text](<Screenshot 2026-04-12 at 6.52.41 PM.png>)

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Testing two different profiles made it clear that the system does not treat genre and mood equally, it treats them as two separate bonus tickets that happen to be worth the same amount. My forst tested profile  asked for a chill mood but a very high energy level (1.0). Because no song in the catalog is both chill and high-energy at the same time, the system was forced to pick a side. Songs with a chill mood earned +2.0 for the mood match but were then penalized heavily on energy because their actual energy (around 0.35–0.42) is so far from 1.0.  The result was that intense and happy songs floated to the top even though the user explicitly asked for chill. The system was not "wrong" by its own math, it just did not understand that chill and energy 1.0 are contradictory requests, so it treated them as two independent dials instead of one conflicting signal.

my personal profile (pop genre, chill mood) was hard. there is no pop song in the catalog that is also tagged chill. That means no song can ever earn both the +2.0 genre bonus and the +2.0 mood bonus at the same time. The system is forced to recommend either a pop song that feels wrong emotionally, or a chill song from a completely different genre. Since the default energy and acousticness targets happen to line up better with the chill lofi songs than with the upbeat pop songs, mood ended up winning and the pop genre preference was essentially ignored. 


---

## 7. `model_card_template.md`

Combines reflection and model card framing from the Module 3 guidance. :contentReference[oaicite:2]{index=2}  

```markdown
# 🎧 Model Card - Music Recommender Simulation

## 1. Model Name

Give your recommender a name, for example:

> VibeFinder 1.0

---

## 2. Intended Use

- What is this system trying to do
- Who is it for

Example:

> This model suggests 3 to 5 songs from a small catalog based on a user's preferred genre, mood, and energy level. It is for classroom exploration only, not for real users.

---

## 3. How It Works (Short Explanation)

Describe your scoring logic in plain language.

- What features of each song does it consider
- What information about the user does it use
- How does it turn those into a number

Try to avoid code in this section, treat it like an explanation to a non programmer.

---

## 4. Data

Describe your dataset.

- How many songs are in `data/songs.csv`
- Did you add or remove any songs
- What kinds of genres or moods are represented
- Whose taste does this data mostly reflect

---

## 5. Strengths

Where does your recommender work well

You can think about:
- Situations where the top results "felt right"
- Particular user profiles it served well
- Simplicity or transparency benefits

---

## 6. Limitations and Bias

Where does your recommender struggle

Some prompts:
- Does it ignore some genres or moods
- Does it treat all users as if they have the same taste shape
- Is it biased toward high energy or one genre by default
- How could this be unfair if used in a real product

---

## 7. Evaluation

How did you check your system

Examples:
- You tried multiple user profiles and wrote down whether the results matched your expectations
- You compared your simulation to what a real app like Spotify or YouTube tends to recommend
- You wrote tests for your scoring logic

You do not need a numeric metric, but if you used one, explain what it measures.

---

## 8. Future Work

If you had more time, how would you improve this recommender

Examples:

- Add support for multiple users and "group vibe" recommendations
- Balance diversity of songs instead of always picking the closest match
- Use more features, like tempo ranges or lyric themes

---

## 9. Personal Reflection

A few sentences about what you learned:

- What surprised you about how your system behaved
- How did building this change how you think about real music recommenders
- Where do you think human judgment still matters, even if the model seems "smart"

