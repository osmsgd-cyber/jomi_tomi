# مكتبة البرومبات الاحترافية لنظام تومي جومي (Jommi Tomi Prompt Library)

## 1. المقدمة
تعتبر هندسة الأوامر (Prompt Engineering) حجر الزاوية في نظام "تومي جومي" لضمان جودة المخرجات واتساقها. يهدف هذا المستند إلى توفير مكتبة شاملة من البرومبات (Prompts) المصممة خصيصًا لكل مرحلة من مراحل الإنتاج، بدءًا من تحويل صورة الطفل إلى شخصية بأسلوب Pixar، وصولاً إلى توليد المشاهد، الفيديوهات، ومحتوى وسائل التواصل الاجتماعي. تم تصميم هذه البرومبات لتكون قابلة للتخصيص (عبر المتغيرات بين الأقواس `[ ]`) لتناسب كل طفل وقصة.

## 2. برومبتات توليد الشخصية (Character Generation Prompts)
الهدف من هذه المرحلة هو تحويل صورة الطفل الحقيقية إلى شخصية ثلاثية الأبعاد بأسلوب Pixar، مع الحفاظ على ملامحه الأساسية وإنشاء ورقة مرجعية (Character Sheet) لضمان ثبات الشخصية في المشاهد اللاحقة.

### 2.1. برومبت تحويل الصورة الأساسية (Base Image to Pixar Style)
يُستخدم هذا البرومبت مع أداة مثل Magnific.ai أو Midjourney (مع استخدام الصورة كمرجع `Image Prompt`).

> **البرومبت:**
> "A highly detailed, 3D rendered portrait of a [Age]-year-old [Gender] child in the style of a modern Pixar or Disney animation. The child has [Hair Color and Style], [Eye Color] eyes, and a [Facial Expression/Feature, e.g., cheerful smile, freckles]. They are wearing [Clothing Description]. The lighting is soft, cinematic, and magical, with vibrant colors and exaggerated, expressive, yet charming facial features. High quality, 8k resolution, masterpiece, octane render, unreal engine 5."

### 2.2. برومبت ورقة الشخصية (Character Sheet / Model Sheet)
يُستخدم هذا البرومبت لإنشاء ورقة مرجعية للشخصية من زوايا متعددة، وهو أمر بالغ الأهمية للحفاظ على ثبات الشخصية.

> **البرومبت:**
> "A comprehensive 3D character design model sheet of a [Age]-year-old [Gender] child in Pixar animation style. The sheet includes multiple angles: front view, side profile, three-quarter view, and back view. The character has [Hair Color and Style], [Eye Color] eyes, and is wearing [Clothing Description]. The background is a neutral, solid light gray color. The character's expressions are neutral but expressive. High resolution, clean lines, professional character design turnaround, 8k, highly detailed."

## 3. برومبتات توليد المشاهد الثابتة (Still Scene Generation Prompts)
تُستخدم هذه البرومبات لتوليد مشاهد القصة بناءً على السكريبت، مع دمج الشخصية التي تم إنشاؤها مسبقًا. يجب استخدام أدوات تدعم ثبات الشخصية (مثل Character Reference في Midjourney أو ControlNet في Stable Diffusion).

### 3.1. برومبت مشهد عام (General Story Scene)
يُستخدم هذا البرومبت لتوليد مشهد داخلي أو خارجي مع التركيز على البيئة والشخصية.

> **البرومبت:**
> "A cinematic, wide-angle shot in Pixar 3D animation style. The main character, a [Age]-year-old [Gender] child with [Hair Color] and [Clothing Description], is [Action/Pose, e.g., discovering a glowing magical book] in a [Setting/Environment, e.g., cozy, dimly lit ancient library]. The lighting is dramatic and magical, with glowing particles and soft shadows. Vibrant colors, highly detailed environment, emotional storytelling, 8k resolution, masterpiece. Aspect ratio: [16:9 for video / 3:4 or A4 ratio for print]."

### 3.2. برومبت لقطة قريبة (Close-up / Emotional Shot)
يُستخدم هذا البرومبت للتركيز على تعابير وجه الشخصية وردود أفعالها.

> **البرومبت:**
> "A close-up portrait shot in Pixar 3D animation style. The main character, a [Age]-year-old [Gender] child with [Hair Color], is showing a [Emotion, e.g., look of pure wonder and amazement]. The background is beautifully blurred (bokeh effect) showing hints of a [Setting, e.g., magical forest]. Soft, warm rim lighting on the character's hair, highly expressive eyes, detailed textures, cinematic lighting, 8k resolution."

## 4. برومبتات توليد الفيديو (Video Generation Prompts)
تُستخدم هذه البرومبات مع أدوات توليد الفيديو من الصور (Image-to-Video) مثل RunwayML (Gen-2) أو Pika Labs، لتحريك المشاهد الثابتة التي تم توليدها.

### 4.1. برومبت تحريك مشهد هادئ (Subtle Motion)
> **البرومبت:**
> "Subtle, cinematic motion. The child's hair blows gently in the wind, and they blink naturally. The camera slowly pans forward (dolly in). The magical glowing elements in the background twinkle softly. High quality, smooth animation, consistent character."

### 4.2. برومبت تحريك مشهد نشط (Active Motion)
> **البرومبت:**
> "Dynamic motion. The child [Action, e.g., reaches out to touch the glowing butterfly]. The camera follows the movement smoothly. The environment reacts to the movement, with [Environmental Effect, e.g., leaves rustling]. Cinematic lighting, high frame rate, smooth transition."

## 5. برومبتات توليد محتوى السوشيال ميديا (Social Media Content Prompts)
تُستخدم هذه البرومبات لإنشاء مواد ترويجية جذابة لمنصات "تومي جومي".

### 5.1. برومبت غلاف القصة (Book Cover)
> **البرومبت:**
> "A magical and captivating children's book cover in Pixar 3D animation style. The main character, a [Age]-year-old [Gender] child, is standing in the center, looking up at a [Magical Element, e.g., giant glowing tree]. The title area at the top is left blank with negative space for text. Vibrant, eye-catching colors, bold composition, magical atmosphere, highly detailed, 8k resolution. Aspect ratio: 3:4."

### 5.2. برومبت منشور ترويجي (Promotional Post - e.g., Instagram)
> **البرومبت:**
> "A vibrant, engaging promotional image in Pixar 3D style. The main character is holding a glowing, magical storybook that is emitting soft light onto their face. They are looking directly at the camera with an inviting smile. The background is a colorful, abstract magical realm. High contrast, saturated colors, perfect for social media, 8k resolution. Aspect ratio: 1:1 or 4:5."

## 6. إرشادات عامة لاستخدام البرومبات
*   **التخصيص:** يجب استبدال جميع المتغيرات بين الأقواس `[ ]` بالبيانات الفعلية للطفل والقصة قبل استخدام البرومبت.
*   **الوزن (Weighting):** في بعض الأدوات (مثل Midjourney)، يمكن استخدام الأوزان (مثل `::2`) للتركيز على عناصر معينة في البرومبت (مثل `Pixar style::2`).
*   **البرومبت السلبي (Negative Prompt):** يُنصح دائمًا باستخدام برومبت سلبي لتجنب التشوهات، مثل: "ugly, deformed, poorly drawn, realistic, photographic, anime, 2d, text, watermark, extra limbs, bad anatomy".
*   **التجربة والتحسين:** قد تتطلب البرومبات بعض التعديلات الطفيفة بناءً على الأداة المستخدمة والصورة الأصلية للطفل للحصول على أفضل النتائج.

## 7. الخلاصة
توفر هذه المكتبة أساسًا قويًا لتوليد محتوى عالي الجودة ومتسق لمشروع "تومي جومي". من خلال دمج هذه البرومبات في النظام العقدي (Node System)، يمكن أتمتة عملية الإنتاج بشكل كبير مع الحفاظ على اللمسة الفنية الساحرة التي تميز أسلوب Pixar.
