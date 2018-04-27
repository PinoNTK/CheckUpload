# recruitment_recommender_system-
Building a web service for a recommender system in vietnamese 

1. Install all requirements
pip install -r requirements.txt 

Note: Remember to add new requirements to requirements.txt 

2. To migrate db 
python manager.py makemigrations
python manager.py migrate 

3. To runserver 
python manager.py runserver 

4. To create django admin user 
python manager.py createsuperuser

5. Sử dụng API extract cv

http://127.0.0.1:8000/extraction/api/extract-cv/<file_pdf>

với file_pdf là tên file lưu trong thư mục Api_Extraction/cv

ví dụ : http://127.0.0.1:8000/extraction/api/extract-cv/nguyen_van_huy.pdf

kết quả trả về dưới dạng json

http://127.0.0.1:8000/extraction/api/upload/

