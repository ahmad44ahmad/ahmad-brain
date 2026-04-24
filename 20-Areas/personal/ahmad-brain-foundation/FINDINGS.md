---
type: resource
status: active
track: personal
lang: ar
created: 2026-04-17
updated: 2026-04-24
tags: ['findings', 'audit', 'ahmad-brain']
---

# نتائج الجولة الاستكشافية — 2026-04-17

## 1. البيئة الحالية

- **الصلاحيات:** كاملة على `Bash`, `Write`, `Edit`, `Agent`, MCPs (Supabase, Vercel). لا حاجة لطلب إذن لأي عملية قياسية.
- **Hooks نشطة:** checkpoint, file-overwrite-guard, verify-before-stop, notify, session-start. الحماية تعمل تلقائيًا.
- **Skills محلية:** `basira-dev`, `file-overwrite-guard`, `pt-modeling-qa`, `tts-round-runner` — كلها إنتاجية. **لا مهارة لمسار «التعرّف عليك»** — فجوة تستحق مهارة لاحقًا.
- **Slash commands:** `arabic-check`, `basira`, `mission`, `pt-start`, `tts-round`, `verify`.

## 2. بصيرة — الحقيقة على الأرض

- **المسار:** `C:\dev\basira\` ← يطابق CLAUDE.md بعد flatten 2026-04-16.
- **الحجم:** 66,636 سطر TS/TSX ← يطابق رقمك تمامًا.
- **Git remote:** `ahmad44ahmad/Beneficiary-System-Clean-Backup` (origin).
- **آخر commits:** data restore (2026-04-14)، UI/RTL تحديثات، PR #21 merged.

## 3. إرث GitHub — 20+ مستودعًا

### متصلة مباشرة بالمهمة
- **`bareed`** — أرشيف بريد عربي MBOX → SQLite FTS5 → FastAPI → React 19. **حساسية التشكيل مُعالجة فعليًا.** هذا بروتوتايب «العقل الخارجي».
- **`iso9001`, `BICSL-Mock-Exam-Simulator`, `Case-File-Consultant`, `tanomah-hospital-`, `sanaduk-dashboard-project`** — محاور جودة/امتحانات/حوكمة/مستشفيات.
- **`https-ai.studio-apps-drive-1exnD55wBrF3CHrQOb2ZwUCE2BP7ryLUr`** — «التحول التقني لعموم النماذج».
- **`dictation-and-prompts-`, `dictating-app`** — تفريغ صوتي عربي/إنجليزي (رابط مع Habibi-TTS).

### إصدارات بصيرة التاريخية
- `Basira`, `Basira-v1.1`, `Basira-v2`, `Basira-improvements`, `updated_Beneficiary-Management-System`, `Beneficiary-System-Clean-Backup` (الحالي).

### منوّعات
- `catering-88`, `catering-`, `88`, `desktop-tutorial`.

## 4. إرث محلي في `C:\Users\aass1\` (مخالف لقاعدة CLAUDE.md)

`Basira/`, `Basira-1/`, `Basira-v1.1/`, `Beneficiary-System-Clean-Backup/`, `f5-tts-project/`, `habibi-tts-project/`, `tts-recording-studio/`, `basira-diagnostic.mjs`.

**القاعدة الحالية:** المشاريع في `C:\dev\`. لكن هذه المجلدات القديمة باقية. **ترشيح للأرشفة/الحذف لاحقًا** — ليس في هذه المهمة.

## 5. ذاكرتي — فجوات مكتشفة

- **`user_profile.md`** عمره 18 يومًا ويذكر `Beneficiary-System-Clean-Backup` كمسار canonical. هذا صحيح للـgit، لكن المحلي الآن `C:\dev\basira\`. **سأحدّث.**
- **لا ذاكرة** عن: مشروع نماذج الذكاء (H100)، بيئة العمل البيروقراطية، دور «مهندس نظم متكاملة»، المسارات الثلاثة، «درجة النضج».
- **`feedback_autonomy.md`** يغطي "نفّذ لا تقترح" — لكن لا يغطي **الصلاحية على مستوى الهدف** + **حرية التفريع**. سأحدّث.

## 6. اكتشافات استراتيجية

1. **العقل الخارجي له سابقة مثبتة عندك:** SQLite FTS5 في `bareed` يحل مشكلة البحث العربي بتكلفة صفر (لا embedding، لا network). **توصية معدَّلة:** هجين FTS5 (لفظي) + pgvector (دلالي) بدل pgvector وحيد. يضاعف الجودة ويخفّض التكلفة.
2. **مسار «التعرّف عليك» بحاجة مهارة محلية** — مثل `basira-dev` بالضبط — تحمّل السياق الشخصي تلقائيًا عند بدء جلسة شخصية.
3. **تراكم إصدارات بصيرة القديمة** يؤكد كلامك عن إعادة البناء من الصفر قبل الطرح — التاريخ يثبت أن التراكم مشكلة حقيقية، ليست مخاوف نظرية.
