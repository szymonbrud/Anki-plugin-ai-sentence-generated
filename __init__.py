from aqt import gui_hooks
import requests
import json

# Choose the model you want to use. Note: Gemma has the largest capacity but should provide sufficient results.
AI_MODEL = "gemma-3n-e2b-it"

# You can get free api key from AI studio
GEMINI_API_KEY=""

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

        # FIELD NAMES
        source_field = "Tył_en"
        target_field = "ai_sentence"

        if source_field in note:
            source_content = note[source_field].strip()
            if source_content:
                # Generate the sentence using Gemini
                generated_sentence = generate_sentence_from_gemini(source_content)
                new_content = generated_sentence
                text = text.replace("ai_sentence", new_content)

    return text

gui_hooks.card_will_show.append(modify_card_html)
