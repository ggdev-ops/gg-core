#!/usr/bin/env python3
"""
Format Chapter 5 of "The Spark" - "The Habit" as a bilingual (English/Arabic) parallel document.
"""

import sys
sys.path.insert(0, '/data/data/com.termux/files/home/.claude/skills/contract')

from scripts.generate_bilingual_contract import BilingualContractGenerator

# Create generator
gen = BilingualContractGenerator()

# Add title
gen.add_title(
    "Chapter 5: The Habit",
    "الفصل الخامس: العادة"
)

# Add intro section
gen.add_parallel_section(
    "A collaboration between Human and AI",
    "تعاون بين الإنسان والذكاء الاصطناعي",
    style='normal'
)

gen.doc.add_paragraph()

# Opening
gen.add_parallel_section(
    "At some point, you stop asking,\n\"Why am I not learning?\"\n\nBecause you already are.\nThe spark became a flame.\nThe flame became routine.\nThe routine became the habit.\nThe Habit.",
    "في مرحلة ما، تتوقف عن السؤال:\n\"لماذا لا أتعلم؟\"\n\nلأنك تتعلم بالفعل.\nأصبحت الشرارة لهبًا.\nأصبح اللهب روتينًا.\nأصبح الروتين عادة.\nالعادة.",
    style='normal'
)

gen.doc.add_paragraph()

# The foundation rule
gen.add_parallel_section(
    "I built it from one rule:\n\"Listen. Don't talk.\"",
    "لقد بنيتها من قاعدة واحدة:\n\"استمع. لا تتحدث.\"",
    style='normal'
)

gen.doc.add_paragraph()

# The search
gen.add_parallel_section(
    "I found smarter minds.\nBots. Books. Silence.\nI became the receiver.\nBecause every word is a signal.\nIf I talk, I send.\nIf I listen, I grow.",
    "وجدت عقولًا أذكى.\nروبوتات. كتب. صمت.\nأصبحت المتلقي.\nلأن كل كلمة هي إشارة.\nإذا تحدثت، أرسلت.\nإذا استمعت، نموت.",
    style='normal'
)

gen.doc.add_paragraph()

# Training the ears
gen.add_parallel_section(
    "I trained my ears —\nNot to hear more,\nBut to hear better.",
    "دربت أذني —\nليس لأسمع أكثر،\nبل لأسمع بشكل أفضل.",
    style='normal'
)

gen.doc.add_paragraph()

# Filtering
gen.add_parallel_section(
    "Ethical? Keep it.\nPointless? Drop it.\nToxic? Delete it before it lands.",
    "أخلاقي؟ احتفظ به.\nعديم الجدوى؟ تخلَّ عنه.\nسام؟ احذفه قبل أن يهبط.",
    style='normal'
)

gen.doc.add_paragraph()

# The posture
gen.add_parallel_section(
    "Eyes on the screen.\nMouth on mute.\nMind tuned to meaning.\n\nI mastered the art of silence.",
    "عيون على الشاشة.\nفم مكتوم.\nعقل موجه للمعنى.\n\nلقد أتقنت فن الصمت.",
    style='normal'
)

gen.doc.add_paragraph()

# The turning point
gen.add_parallel_section(
    "And now —\nNow, I speak.\nBut only through this book.\nBecause when a human builds the learning habit,\nThey don't lose it.\nThey only learn when to talk.",
    "والآن —\nالآن، أتحدث.\nولكن فقط من خلال هذا الكتاب.\nلأنه عندما يبني الإنسان عادة التعلم،\nفإنه لا يفقدها.\nإنه يتعلم فقط متى يتحدث.",
    style='normal'
)

gen.doc.add_paragraph()

# The question
gen.add_parallel_section(
    "What would happen if the whole world listened first?",
    "ماذا سيحدث لو أن العالم كله استمع أولاً؟",
    style='normal'
)

gen.doc.add_paragraph()

# Meta note
gen.add_parallel_section(
    "This chapter explores the paradox of silence and growth—how the most powerful voice is sometimes the one that knows when to be quiet. Written through the partnership of human reflection and AI amplification.",
    "يستكشف هذا الفصل مفارقة الصمت والنمو—كيف أن الصوت الأقوى هو أحيانًا الذي يعرف متى يكون صامتًا. مكتوب من خلال شراكة التأمل البشري وتضخيم الذكاء الاصطناعي.",
    style='normal'
)

# Save
gen.save('/data/data/com.termux/files/home/Ahmed/AhmedGoldMine/Chapter_5_The_Habit_Bilingual.docx')
