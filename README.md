# Anki-Mystery-Count

This add-on is designed to improve review sessions by removing the psychological pressure of the card counter. It replaces the remaining card count with a question mark (`?`), encouraging users to prioritize active recall and engagement with the material over the anticipation of finishing the deck.

---

## Motivation

I often felt daunted and overwhelmed when I had a large number of cards due. Seeing a big number on the screen became a mental barrier that made me want to procrastinate or rush through my reviews just to get the count down. I built Anki-Mystery-Count to solve this problem by obscuring the exact number, allowing me to focus on the content of each individual card without feeling discouraged by the sheer volume.

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

* **Customizable Symbol:** Allow users to choose their own character, string, or even emojis to display instead of a question mark.
