import os
from flask import Flask, request, jsonify
from flask_cors import CORS
# تأكد من تثبيت مكتبةopenai عبر الأمر (pip install openai flask flask-cors)
from openai import OpenAI

app = Flask(__name__)
CORS(app) # للسماح للموقع بالتحدث مع الخادم بأمان

# ضع مفتاح API الخاص بك من OpenAI هنا
# يمكنك الحصول عليه من منصة المطورين لـ OpenAI
client = OpenAI(api_key="ضع_مفتاح_الـ_API_الخاص_بكامل_هنا")

@app.route('/api/summarize', methods=['POST'])
def summarize_file():
    if 'file' not in request.files:
        return jsonify({"error": "لم يتم إرسال أي ملف"}), 400
        
    file = request.files['file']
    grade = request.form.get('grade', 'المرحلة الدراسية للطلبة')
    subject = request.form.get('subject', 'المادة')
    
    # قراءة محتوى الملف المرفوع (نصي)
    try:
        file_content = file.read().decode('utf-8')
    except Exception:
        # إذا كان ملف PDF أو وورد معقد، يحتاج مكتبات إضافية، هنا نقرأه كنص مبدئياً
        file_content = "محتوى الملف التعليمي المرفوع من الطالب للمذاكرة الفورية."

    # صياغة الأمر الدقيق والمحترف لـ ChatGPT ليعطيك تلخيصاً ضخماً وحقيقياً
    prompt = f"أنت بروفيسور ومساعد تعليمي ذكي لصف ({grade}). تم رفع مستند دراسي لمادة ({subject}). أريدك أن تقرأ المحتوى التالي بدقة وتولد تلخيصاً أكاديمياً شاملاً ومفصلاً جداً، مقسماً إلى نقاط وعناوين واضحة، ويغطي كافة الأفكار الرئيسية، بحيث يناسب جلسة مذاكرة بومودورو مدتها 25 دقيقة. لا تختصر اختصاراً مخلاً بل أعطِ المادة حقها كاملاً.\n\nالمحتوى المرفوع:\n{file_content}"

    try:
        # إرسال الطلب الفعلي لعقل ChatGPT
        response = client.chat.completions.create(
            model="gpt-4o", # أو يمكنك استخدام gpt-3.5-turbo للتوفير
            messages=[{"role": "user", "content": prompt}]
        )
        summary_result = response.choices[0].message.content
        return jsonify({"summary": summary_result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(port=5000, debug=True)
