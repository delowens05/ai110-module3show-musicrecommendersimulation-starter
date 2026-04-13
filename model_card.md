# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  

- Rec The Party Room!

---

## 2. Intended Use  

This recommender suggests the top 5 songs from catalog by scoring each song against a user's stated preferences for genre, mood, energy, valence, acousticness, and tempo. It describe a users taste as a fixed profile and it is built to explore how scoring rules and weight choices each shape what gets recommended to the user.

---

## 3. How the Model Works  
Real-world platforms like Spotify or YouTube learn your taste by watching what you play, skip, and save, then finding patterns across other listeners who behave and listen similarly. That works well, but takes a lot of data and it is hard to explain. However my version takes a simpler and more vauqe approach. it looks directly at the qualities of each song like energy level, emotional tone, and whether it feels acoustic or produced. It then compares them against what a user says they prefer. Songs that are closer to thw users preferences score higher, and the top matches get recommended. The system priorties energy, since that tends to be the one thing listeners feel most immediately when listening to a song and treats genre and mood as signals rather than strict rules.

Each song tracks seven components: genre, mood, energy, tempo, valence, danceability, and acousticness. Each user profile stores four preferences: a favorite genre, a favorite mood, a target energy level, and whether they like acoustic music. 

Algorithm Recipe: Each song is scored out of a maximum of 7.5 points where: 

- genre match earns +2.0, mood match earns +2.0, and the remaining 3.5 points come from how closely the song's energy, valence, acousticness, and tempo match the user's targets. 

- Songs are then ranked by total score and the top K are returned. 

- One thing id look out for is that genre and mood together make up more than half the possible score, so a song that perfectly matches a user's energy and vibe but falls into an unfamiliar genre will often lose to a weaker fit that just happens to share the same genre label.

---

## 4. Data  

The catalog contains 18 songs that may have one of the 15 genres and 14 moods, and was used as-is without adding or removing tracks. Because 13 of those 15 genres appear only once, theres not a lot of songs in general  and there are no songs that blend styles, the dataset has real gaps for listeners whose taste sits between categories or outside the genres represented.
---

## 5. Strengths  

The system works best when a user's genre, mood, and energy preferences all align in the same direction. Like when someone who wants metal, angry, and high energy will reliably get a song that matches a near-perfect score. It also surfaces reasonable runners-up in those cases, since songs that share even one of those traits still cluster near the top rather than random songs filling out the list.

---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

I think the most significant weakness discovered through testing is that the two same bonuses+2.0 for a genre match and +2.0 for a mood match. Together they total 4.0 points, which exceeds the maximum any song can earn from all four continuous attributes combined (energy + valence + acousticness + tempo = 3.5 points max). This means a song that is a perfect genre and mood match will almost always rank first, even if its energy, tempo, and acousticness are completely wrong for the user. This creates a filter bubble where users are repeatedly shown the same one or two songs that share their genre and mood labels, regardless of how well the songs actually fit their listening habits. 

---

## 7. Evaluation  


I tested the user profile where the mood was chill but the energy was 1.00. In those results, I saw that the mood for the first two songs was not chill, but instead intense and happy but the energy fit was good. I also tested a personal profile, basically seeing if my personal profile will provide songs that i would most likely listen to. My profile is genre: pop and mood:chill but it really only recommended me songs that fit the mood and not the actaul genre of pop.

---

## 8. Future Work  

The biggest improvement I would be probably make is making sure the weights of genre and mood are differnt bonuses so it cannot automatically override all continuous scores combined. This would force the system to actually measure how well a song sounds right rather than just whether it shares a label. I would also add a diversity rule that prevents the top 5 from being dominated by the same genre, so a user gets a real range of options instead of just staying in a "genre bubble"

---

## 9. Personal Reflection  

I learned that analyzing a dataset and choosing the right weights can have a bigger impact on what gets recommended than I expected. Decisions about how many points to assign a genre match completely changed which songs rose to the top. What I found most interesting was using a point system to see exactly how much each component of a user's profile contributed to the final decision, because it made the reasoning visible in a way that felt fair and checkable. I also learned that recommending only within one genre creates a bubble fast, and that diversity in results matters just as much as accuracy. Now when I use Spotify, I pay more attention to how varied the recommendations actually are and whether they are playing it safe by repeating the same style, or genuinely recommending me something new.
