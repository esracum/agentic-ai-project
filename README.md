


Autonomous Coding Agent (Built from Scratch)

![Python](https://img.shields.io/badge/Python-3.13-blue?style=for-the-badge&logo=python)
![Gemini API](https://img.shields.io/badge/Google%20Gemini-Flash-orange?style=for-the-badge&logo=google)
![Agentic AI](https://img.shields.io/badge/Agentic-AI-purple?style=for-the-badge)

Bu proje, herhangi bir hazır framework (LangChain, CrewAI vb.) kullanılmadan, tamamen **Python** ve **Google Gemini Flash API** kullanılarak **sıfırdan (from scratch)** geliştirilmiş bir otonom kodlama ajanıdır.

Standart LLM'lerin aksine, bu ajan sadece kod üretmez; ürettiği kodu yerel ortamda çalıştırır, hataları analiz eder ve kendi kendini düzelterek (Self-Correction) görevi tamamlar.

## Demo



https://github.com/user-attachments/assets/ae523fae-91b8-49bb-875d-4e19a179409a





## Temel Özellikler

* **Otonom Döngü (Autonomous Loop):** Kod yazma, çalıştırma ve test etme süreçlerini insan müdahalesi olmadan yönetir.
* **Hata Düzeltme (Self-Correction):** Çalışan kod hata verirse (Runtime Error), ajan `stderr` çıktısını okur, hatanın nedenini anlar ve kodu revize eder.
* **Function Calling Mimarisi:** Modelin yapılandırılmış verilerle sistem komutlarını ve dosya işlemlerini yönetmesini sağlar.
* **Güvenli Çalıştırma (Safe Execution):** Kodlar izole edilmiş alt süreçlerde (`subprocess`) çalıştırılır.
* **Yerel Dosya Entegrasyonu:** Proje dizinindeki dosyaları okuyabilir, analiz edebilir ve güncelleyebilir.

## Nasıl Çalışır?

Ajan, kendisine verilen bir görevi yerine getirmek için aşağıdaki döngüyü izler:

1.  **Analiz:** Kullanıcı isteğini ve proje bağlamını (dosyalar) anlar.
2.  **Planlama & Kodlama:** Gemini Flash API üzerinden gerekli Python kodunu oluşturur.
3.  **Çalıştırma (Execution):** Oluşturulan kodu sistemde çalıştırır.
4.  **Doğrulama (Verification):**
    * **Başarılı:** Sonucu kullanıcıya sunar.
    * **Hata:** Hata mesajını analiz eder, çözüm üretir ve **2. adıma** geri döner (Iteration).

##  Kurulum

Projeyi yerel makinenizde çalıştırmak için adımları izleyin:

1.  **Repoyu klonlayın:**
    ```bash
    git clone [https://github.com/KULLANICI_ADIN/repo-adi.git](https://github.com/KULLANICI_ADIN/repo-adi.git)
    cd repo-adi
    ```

2.  **Gerekli paketleri yükleyin:**
    *Öneri: `uv` veya `venv` kullanarak sanal ortam oluşturun.*
    ```bash
    pip install -r requirements.txt
    ```

3.  **API Anahtarını Ayarlayın:**
    `.env` dosyası oluşturun ve Google Gemini API anahtarınızı ekleyin:
    ```env
    GEMINI_API_KEY=senin_api_anahtarin_buraya
    ```

## Kullanım

Ajanı başlatmak için `main.py` dosyasını çalıştırın:

```bash
uv run main.py args



