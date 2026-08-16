import json
import os
import requests


def generate_quran_pass():
  # 1. جلب آية عشوائية وتفسيرها من الـ API
  url = "https://api.alquran.cloud/v1/ayah/random/ar.muyassar"
  response = requests.get(url)

  if response.status_code == 200:
    data = response.json()["data"]
    surah_name = data["surah"]["name"]
    ayah_number = data["numberInSurah"]
    ayah_text = data["text"]

    # 2. تجهيز هيكل بيانات البطاقة (Pass JSON)
    pass_data = {
        "formatVersion": 1,
        "passTypeIdentifier": "pass.com.quran.wallet",
        "teamIdentifier": "ABCD1234EF",
        "organizationName": "آية الأسبوع",
        "description": "تذكير بالآيات القرآنية الأسبوعية",
        "logoText": "القرآن الكريم",
        "backgroundColor": "rgb(20, 50, 40)",
        "foregroundColor": "rgb(255, 255, 255)",
        "generic": {
            "primaryFields": [{
                "key": "surah",
                "label": "السورة الكريمة",
                "value": f"{surah_name} (آية {ayah_number})",
            }],
            "secondaryFields": [{
                "key": "ayah",
                "label": "النص الشريف",
                "value": ayah_text,
            }],
        },
    }

    # 3. حفظ الملف في مجلد المشروع
    with open("pass.json", "w", encoding="utf-8") as f:
      json.dump(pass_data, f, ensure_ascii=False, indent=4)

    print("--- ممتاز! تم تحديث وتجهيز بيانات البطاقة بنجاح ---")
    print(f"الآية الحالية: {surah_name} - آية {ayah_number}")

  else:
    print("فشل في الاتصال بالـ API، تأكدي من اتصال الإنترنت.")


if __name__ == "__main__":
  generate_quran_pass()