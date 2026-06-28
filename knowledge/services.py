import os
import json
from dotenv import load_dotenv
from groq import Groq
from .models import FaqEntry

load_dotenv()


class GeminiNLUService:
    """
    Service NLU avec Groq AI + base de données juridique marocaine.
    """

    def __init__(self):
        self.client = Groq(api_key=os.getenv("GROQ_API_KEY"))
        self.model = "llama-3.3-70b-versatile"

    def match(self, text: str) -> dict | None:
        if not text:
            return None

        is_arabic = any('\u0600' <= char <= '\u06FF' for char in text)
        direction = "rtl" if is_arabic else "ltr"
        lang = "ar" if is_arabic else "fr"

        from knowledge.models import LegalDocument
        from django.db.models import Q

        words = text.lower().replace('?', '').replace('!', '').split()

        # Mapping arabizi → mots français pour chercher dans les PDFs
        search_mapping = {
            'travail': ['travail', 'licenciement', 'salarié', 'employeur', 'contrat'],
            'khedma': ['travail', 'licenciement', 'salarié'],
            'tardoni': ['licenciement', 'rupture', 'abusif'],
            'sarqa': ['vol', 'soustraction', 'peine', 'emprisonnement'],
            'zawaj': ['mariage', 'époux', 'consentement', 'adoul'],
            'talaq': ['divorce', 'répudiation', 'dissolution'],
            'cin': ['identité', 'carte nationale', 'renouvellement'],
            'cnss': ['sécurité sociale', 'cotisation', 'affiliation'],
            'irs': ['succession', 'héritage', 'héritier'],
            'kra': ['bail', 'location', 'loyer', 'locataire'],
            'tribunal': ['tribunal', 'juridiction', 'procédure'],
            'بطاقة': ['identité', 'carte nationale', 'renouvellement'],
            'تجديد': ['renouvellement', 'carte nationale', 'identité'],
            'عقد': ['contrat', 'bail', 'travail'],
            'طلاق': ['divorce', 'répudiation', 'dissolution'],
            'ميراث': ['héritage', 'succession', 'héritier'],
        }

        search_terms = []
        for word in words:
            if word in search_mapping:
                search_terms.extend(search_mapping[word])
            else:
                search_terms.append(word)

        query = Q()
        for term in search_terms[:8]:
            query |= Q(content__icontains=term)

        travail_words = ['tardoni', 'khedma', 'travail', 'licenci', 'salari', 'عمل', 'شغل']
        is_travail = any(w in text.lower() for w in travail_words)

        if is_travail:
            chunks = LegalDocument.objects.filter(
                source_file__icontains='travail'
            ).filter(query)[:8]
            if not chunks:
                chunks = LegalDocument.objects.filter(query)[:8]
        else:
            chunks = LegalDocument.objects.filter(query)[:8]

        if chunks:
            context = "\n\n---\n\n".join([
                f"Source: {c.source_file}\nPage: {c.page_number}\n{c.content[:500]}"
                for c in chunks
            ])
        else:
            context = "Aucun document juridique trouvé pour cette question."

        prompt = f"""أنت مساعد قانوني مغربي متخصص في القانون المغربي.
لديك إمكانية الوصول إلى الوثائق القانونية الرسمية التالية:

{context}

سألك المستخدم هذا السؤال:
"{text}"

تعليمات مهمة:
1. أجب فقط بناءً على المعلومات الموجودة في الوثائق أعلاه
2. أجب باللغة العربية الفصحى البسيطة والواضحة
3. استخدم مصطلحات قانونية مغربية صحيحة
4. إذا لم تجد المعلومة في الوثائق، قل ذلك بوضوح
5. الجواب يجب أن يكون قصيراً (3 جمل maximum)

أرجع فقط هذا JSON بدون أي نص إضافي:
{{
    "category": "cin أو naissance أو location أو travail أو tribunal أو heritage أو cnss أو autre",
    "answer": "الجواب بالعربية الفصحى البسيطة بناءً على الوثائق",
    "legal_reference": "المرجع القانوني الدقيق من الوثائق",
    "disclaimer": "تنبيه: هذه المعلومات للاستئناس فقط وليست استشارة قانونية رسمية"
}}"""

        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[{"role": "user", "content": prompt}],
                temperature=0.3,
            )
            raw = response.choices[0].message.content.strip()

            if "```" in raw:
                raw = raw.split("```")[1]
                if raw.startswith("json"):
                    raw = raw[4:]
            raw = raw.strip()

            data = json.loads(raw)

            return {
                'answer': data.get('answer', ''),
                'legal_reference': data.get('legal_reference', ''),
                'category': data.get('category', 'autre'),
                'disclaimer': data.get('disclaimer', ''),
                'direction': direction,
                'lang': lang,
            }

        except Exception as e:
            print(f"Erreur Groq: {e}")
            return None