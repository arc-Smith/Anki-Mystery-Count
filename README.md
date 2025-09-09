# Anki Mystery-Count Add-On

<p align="center">
  <img width="496" height="115" alt="Screenshot 2025-09-09 at 12 34 54 PM" src="https://github.com/user-attachments/assets/9e937664-5dcc-430a-bca9-2217abadaaa8" />
</p>

This add-on is designed to improve review sessions by removing the psychological pressure of the card counter. It replaces the remaining card count with a question mark (`?`), encouraging users to prioritize active recall and engagement with the material over the anticipation of finishing the deck.

---

## Motivation

I felt overwhelmed when I had a large number of cards due. Seeing a big number on the screen became a mental barrier that made me want to procrastinate or rush through my reviews just to get the count down. I built Anki-Mystery-Count to solve this problem by obscuring the exact number, allowing me to focus on the content of each individual card without feeling discouraged by the sheer volume.

---

## Technologies Used

* **Programming Language:** Python 3.9.6
* **Framework:** Anki Add-on API

---

## How it Works

This add-on hooks into Anki's user interface functions. Instead of retrieving and displaying the numerical count of remaining cards, it intercepts the call and simply renders a question mark (`?`) in its place. This is a lightweight and non-intrusive modification that requires no user interaction and does not alter core Anki behavior.

---

## Future Work

I have several ideas for improving and expanding this add-on:

* **Customizable Symbol:** Allow users to easily choose their own character, string, or even emojis to display instead of a question mark.
* **Progress Bar:** Instead of a simple number or symbol, a progress bar could provide a sense of accomplishment without revealing the exact count. This would allow users to track their progress visually and feel a sense of completion as the bar fills up.
* **Time-Based Estimate:** Some users might prefer a time-based goal over a card count. The add-on could estimate the remaining time to complete the deck based on the user's average review speed, reframing the task from "how many cards" to "how much time."
* **Motivational Messages:** Displaying encouraging messages could further reduce procrastination. The messages could be dynamic, changing as the user completes more cards, such as "Keep it up!" or "You're almost there!"
