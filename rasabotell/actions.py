import requests
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

TELEGRAM_TOKEN = "YOUR_BOT_TOKEN"
TELEGRAM_CHAT_ID = "YOUR_CHAT_ID"

class ActionSendPropertyInfo(Action):
    def name(self):
        return "action_send_property_info"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: dict):
        
        # فرض بر این است که اطلاعات ملک از قبل جمع‌آوری شده
        property_info = tracker.get_slot("property_info")
        
        if property_info:
            message = f"📬 اطلاعات ملک:\n\n{property_info}"
            url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
            data = {
                "chat_id": TELEGRAM_CHAT_ID,
                "text": message
            }
            response = requests.post(url, data=data)
        
        dispatcher.utter_message(text="✅ اطلاعات به مدیر ارسال شد.")
        return []
