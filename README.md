# Anki Gemini Sentence Generator

A simple but powerful Anki add-on that automatically generates an example sentence for a word on your flashcard using the Google Gemini AI. This helps you learn words in context, improving your recall and understanding.

![Demo GIF (placeholder)](https://github.com/user-attachments/assets/c38eada4-ac40-4ae2-8a0b-9b5c3a9565f5)
*(Note: This is a placeholder screenshot showing the concept. The actual appearance depends on your card styling.)*

## Features

- **Automatic Sentence Generation**: Creates a new, unique sentence every time a card is shown.
- **Powered by Google Gemini**: Leverages a powerful, free-to-use AI model for high-quality sentences.
- **Seamless Integration**: Hooks directly into Anki's card rendering process without slowing down the UI.

## How It Works

The add-on operates in a simple, real-time sequence:

1.  **Trigger**: When Anki is about to display a card, the add-on is triggered.
2.  **Fetch Word**: It reads the content from a specific field in your note (e.g., the `card_back` field containing a single word).
3.  **API Call**: It sends this word to the Google Gemini API with a prompt asking for a simple example sentence.
4.  **Replace Placeholder**: The add-on receives the generated sentence from the API and dynamically replaces a placeholder (e.g., `<ai_sentence>`) in your card's HTML template with this new sentence.

This process happens each time you view the card, ensuring you see the word in various contexts.

## Installation & Setup Guide

Follow these steps carefully to get the add-on working.

### Step 1: Install the Add-on File

1.  Download the add-on's Python file (e.g., `__init__.py`).
2.  Open Anki on your desktop.
3.  Go to the main menu: **Tools > Add-ons**.
4.  Click the **"View Files"** button. This will open your Anki add-ons folder (`addons21`).
5.  Create a new folder inside `addons21` and name it something descriptive, like `GeminiSentenceGenerator`.
6.  Place the downloaded `.py` file inside this new folder.
7.  Restart Anki for the add-on to be loaded.

### Step 2: Configure the Add-on

You must provide your own API key for the add-on to work.

1.  **Get a Gemini API Key**:
    *   Go to [Google AI Studio](https://aistudio.google.com/app/apikey).
    *   Sign in with your Google account.
    *   Click **"Create API key"** and copy the generated key.

2.  **Edit the Add-on File**:
    *   Navigate back to your Anki add-ons folder and open the `.py` file with a text editor (like VSCode, Notepad++, or Sublime Text).
    *   Find the `SETTINGS` section at the top of the file.
    *   Paste your API key into the `GEMINI_API_KEY` variable.

    ```python
    # SETTINGS

    # Choose the model you want to use. Note: Gemma has the largest capacity but should provide sufficient results.
    AI_MODEL = "gemma-2b-it" # Changed to gemma-2b-it as it's a common free tier model

    # You can get a free API key from Google AI Studio
    GEMINI_API_KEY="PASTE_YOUR_API_KEY_HERE"

    # Field with the word you want to create the sentence from
    SOURCE_FIELD = "card_back"

    # Target you place in the card style template, which will be replaced with the generated sentence
    TARGET_TO_REPLACE = "<ai_sentence>"
    ```

### Step 3: Configure Your Anki Note Type & Cards

The add-on needs to know where to find the word and where to put the sentence.

1.  **Check Your Note Fields**:
    *   In Anki, open the Browser and find a card of the type you want to modify.
    *   Click the **"Fields..."** button.
    *   Ensure you have a field that matches the `SOURCE_FIELD` from the configuration (default in plugin is set to `card_back`). This field should contain the single word you want to generate a sentence for. If not, you can add a new field or change the `SOURCE_FIELD` in the code to match one of your existing fields (e.g., `Word`).

2.  **Edit Your Card Template**:
    *   With the card selected in the browser, click the **"Cards..."** button.
    *   This will open the Card Template editor.
    *   In the "Front Template" or "Back Template" HTML section (wherever you want the sentence to appear), add the placeholder specified in `TARGET_TO_REPLACE`.

    **Example:**

    Let's say your back template looks like this:

    ```html
    <!-- Back Template -->
    <div id="answer">
        {{card_back}}
        <hr>
        <!-- I want the AI sentence to appear here -->
    </div>
    ```

    Modify it by adding the placeholder:

    ```html
    <!-- Back Template -->
    <div id="answer">
        {{card_back}}
        <hr>
        <ai_sentence>
    </div>
    ```

    Now, when this card is shown, `<ai_sentence>` will be replaced by a sentence generated using the word from your `{{card_back}}` field.

## Configuration Summary

All settings are located at the top of the `.py` file.

| Variable            | Default Value      | Description                                                                                             |
| ------------------- | ------------------ | ------------------------------------------------------------------------------------------------------- |
| `AI_MODEL`          | `gemma-2b-it`      | The Gemini model to use. `gemma-2b-it` is a good choice for the free tier.                                |
| `GEMINI_API_KEY`    | `""`               | **Required.** Your personal API key from Google AI Studio.                                                |
| `SOURCE_FIELD`      | `"card_back"`      | The name of the Anki note field that contains the source word. **Must match your Note Type.**            |
| `TARGET_TO_REPLACE` | `"<ai_sentence>"`  | The placeholder text in your card template that will be replaced with the generated sentence.             |

## Prerequisites

- Anki Desktop version 2.1.x or later.
- An active internet connection (for API calls).
- A Google Account to obtain an API key.

## Troubleshooting

- **No sentence appears**:
    - Double-check that your `GEMINI_API_KEY` is correct and pasted without extra quotes.
    - Ensure the `SOURCE_FIELD` name in the code exactly matches the field name in your Anki Note Type.
    - Make sure the `TARGET_TO_REPLACE` placeholder is present in your Card Template.
- **Error message appears**: The message will usually contain the reason (e.g., invalid API key, network error).
- **Cards load slowly**: Sentence generation happens in real-time and depends on your internet speed and the API's response time. This is normal.
