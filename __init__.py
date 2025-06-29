from aqt import gui_hooks
import requests
import json

# SEtTINGS

# Choose the model you want to use. Note: Gemma has the largest capacity but should provide sufficient results.
AI_MODEL = "gemma-3n-e2b-it"

# You can get free api key from AI Studio
GEMINI_API_KEY=""

# Field with the word you want to create the sentence
SOURCE_FIELD = "card_back"

# Target you place in the card style template, which will be replaced with the generated sentence
TARGET_TO_REPLACE = "<ai_sentence>"

def generate_sentence_from_gemini(word: str) -> str:
    """Generates a sentence with the given word using the Gemini API"""
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{AI_MODEL}:generateContent"


    headers = {
        "Content-Type": "application/json"
    }

    prompt = f"Generate a simple English sentence using the word '{word}'. Reply only with the sentence, without any additional comments."

    data = {
        "contents": [{
            "parts": [{
                "text": prompt
            }]
        }]
    }

    try:
        response = requests.post(f"{url}?key={GEMINI_API_KEY}", json=data, headers=headers)
        response.raise_for_status()
        result = response.json()

        # GET DATA FROM RESPONSE
        if 'candidates' in result and len(result['candidates']) > 0:
            generated_text = result['candidates'][0]['content']['parts'][0]['text'].strip()
            return generated_text
        else:
            return f"Generated sentence with: {word}"

    except Exception as e:
        return f"Error generating sentence: {str(e)}"

def modify_card_html(text: str, card, kind: str) -> str:
    """Modifies the card's HTML - minimal version"""
    if card and card.note():
        note = card.note()

        if SOURCE_FIELD in note:
            source_content = note[SOURCE_FIELD].strip()
            if source_content:
                # Generate the sentence using Gemini
                generated_sentence = generate_sentence_from_gemini(source_content)
                new_content = generated_sentence
                text = text.replace(TARGET_TO_REPLACE, new_content)

    return text

gui_hooks.card_will_show.append(modify_card_html)
