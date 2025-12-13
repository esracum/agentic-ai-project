import os
from dotenv import load_dotenv
from google import genai

def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    
    if not api_key:
        print("HATA: .env dosyasında GEMINI_API_KEY bulunamadı.")
        return

    client = genai.Client(api_key=api_key)

    print("\n🔎 KULLANILABİLİR MODELLER TARANIYOR...\n")
    try:
        # SDK üzerinden model listesini çekiyoruz
        for model in client.models.list():
            # Model ismini (örn: models/gemini-1.5-flash) temizleyelim
            model_id = model.name.split("/")[-1]
            print(f"✅ Model ID: {model_id}")
            
    except Exception as e:
        print(f"LİSTELEME HATASI: {e}")

if __name__ == "__main__":
    main()