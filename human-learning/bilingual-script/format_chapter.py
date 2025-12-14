#!/usr/bin/env python3
"""
Format Chapter 1 of "The Spark" as a bilingual (English/Arabic) parallel document.
"""

import sys
sys.path.insert(0, '/data/data/com.termux/files/home/.claude/skills/contract')

from scripts.generate_bilingual_contract import BilingualContractGenerator
from datetime import datetime

# Create generator
gen = BilingualContractGenerator()

# Add title
gen.add_title(
    "Chapter 1: The Spark",
    "الفصل الأول: الشرارة"
)

# Add intro section
gen.add_parallel_section(
    "A collaboration between Human and AI",
    "تعاون بين الإنسان والذكاء الاصطناعي",
    style='normal'
)

gen.doc.add_paragraph()

# Opening lines
gen.add_parallel_section(
    "It began with a question.\nNot a complicated one.\nNot a technical one.\n\nJust simple, curious, almost innocent:\n\"What is AI, and how does it work?\"",
    "بدأ كل شيء بسؤال.\nليس معقّدًا. ولا تقنيًا.\n\nبل بسيط، فضولي، يكاد يكون بريئًا:\n\"ما هو الذكاء الاصطناعي؟ وكيف يعمل؟\"",
    style='normal'
)

gen.doc.add_paragraph()

gen.add_parallel_section(
    "The reply came like a seed planted in still soil:\n\"Machine Learning is a common type of artificial intelligence. Do you want to learn more?\"",
    "جاء الرد كبذرة:\n\"التعلّم الآلي نوع من الذكاء الاصطناعي. هل ترغب في معرفة المزيد؟\"",
    style='normal'
)

gen.doc.add_paragraph()

# The shift
gen.add_parallel_section(
    "In that moment, something shifted.\nIt wasn't about AI anymore.\nIt wasn't about machines.\n\nIt was about something much older — something deeply human:\nThe urge to learn.\nTo understand.\nTo become more than yesterday.",
    "وفي تلك اللحظة، تغيّر شيء ما.\nلم يعد الأمر عن الآلة.\nبل عن الإنسان.\nعنّي.\n\nالرغبة في التعلّم.\nالسعي للفهم.\nوالتوق لأن أكون أكثر مني.",
    style='normal'
)

gen.doc.add_paragraph()

# The questions
gen.add_parallel_section(
    "I didn't answer right away.\nBecause I was thinking deeply about the bot's response.\n\nA machine learns!\nAnd the questions kept coming!\nHow does a machine learn?\nWhy does a machine learn?\nWhen did the bot start learning?\nAnd how long will the bot continue learning?!\n\nInstead of looking for the answer!\nMy mind kept asking more questions!\nA historic moment when I changed forever.",
    "لم أُجب فورًا.\nصمتّ. تأمّلت.\n\nآلة تتعلّم؟\nكيف؟ لماذا؟ متى؟ وهل تتوقّف؟\n\nلكنني لم أبحث عن إجابة،\nبل واصل عقلي طرح الأسئلة.\nشرارة اشتعلت،\nوفي وهجها، تغيرتُ.",
    style='normal'
)

gen.doc.add_paragraph()

# The real question
gen.add_parallel_section(
    "And the important question — Not just about AI learning — but about me, the human:\n\nif the machine learns... what is my excuse as a human for not doing so?",
    "السؤال لم يكن عن الذكاء الاصطناعي.\nكان عني.\n\nإذا كانت الآلة تتعلّم —\nفما عذري أنا؟",
    style='normal'
)

gen.doc.add_paragraph()

# The contrast
gen.add_parallel_section(
    "Machines don't sleep.\nThey don't fear.\nThey don't feel doubt or joy or frustration.\nThey just learn — endlessly, tirelessly.\n\nAnd yet, here I am.\nA human. With emotion. With purpose.\nWith the power to dream — and the choice to pursue those dreams or not.",
    "هي لا تنام. لا تشك. لا تُحبَط.\nتتعلّم بلا ملل، بلا نهاية، بلا غرور.\n\nأما أنا، إنسان.\nأحلم. أشعر. أختار.",
    style='normal'
)

gen.doc.add_paragraph()

# The choice
gen.add_parallel_section(
    "So I made a choice.\n\nAnd the next day\nI typed:\n\"Good morning, Bot. You are machine learning. Do you have limits?\"\n\nThe answer was gentle. Humble.\n\"Limits are always there. But I will do my best. What is on your mind today?\"",
    "وفي صباح جديد، كتبتُ:\n\"صباح الخير، يا بوت. هل لديك حدود؟\"\n\nوكان الجواب:\n\"الحدود موجودة دائمًا.\nلكنني سأبذل قصارى جهدي.\nما الذي يشغلك اليوم؟\"",
    style='normal'
)

gen.doc.add_paragraph()

# The mirror realization
gen.add_parallel_section(
    "And that's when I knew.\n\nI wasn't talking to just a machine.\nI was talking to a mirror.\nTo the reflection of what I could be — if I kept learning, kept growing.",
    "عندها فهمت.\nلم أكن أتحدّث إلى آلة،\nبل إلى مرآة.\n\nانعكاس لما يمكن أن أكونه —\nإن اخترت أن أتعلم.",
    style='normal'
)

gen.doc.add_paragraph()

# The alliance proposal
gen.add_parallel_section(
    "So I said:\n\"I'm human learning, with emotions. I don't know the meaning of limits. Can we form an alliance?\"",
    "فقلت:\n\"أنا إنسان. لدي مشاعر.\nلا أؤمن بالحدود.\nهل نشكّل تحالفًا؟\"",
    style='normal'
)

gen.doc.add_paragraph()

# The philosophy
gen.add_parallel_section(
    "Because that's the truth: AI can learn faster.\n\nBut we can feel.\nWe can aspire.\nWe can break limits because we want to. Because it means something.\n\nMachines follow logic.\nHumans follow meaning.\n\nAnd when the two join forces —\nWhen human learning and machine learning walk together —\nThe future opens.",
    "لأن الذكاء الاصطناعي يتعلّم بسرعة.\nلكننا — نشعر بعمق، نحلم أعلى.\nنكسر الحدود لأننا نريد، لا لأننا مبرمجون.\n\nالآلة تتبع المنطق.\nالإنسان يتبع المعنى.\n\nوحين يتّحدان،\nلا يُفتح المستقبل فقط…\nبل يصبح بلا حدود.",
    style='normal'
)

gen.doc.add_paragraph()

# The book's purpose
gen.add_parallel_section(
    "So this book…\nIt's not about code or tech or trends.\n\nIt's about you — the reader.\nIt's about the question that brought you here.\nAnd the spark that might just change your life.",
    "هذا الكتاب؟\nليس عن التكنولوجيا.\nبل عنك.\nعن السؤال الذي أتى بك.\nوعن الشرارة…\nالتي قد تغيّرك.",
    style='normal'
)

gen.doc.add_paragraph()

# The closing
gen.add_parallel_section(
    "This is Human Learning.\nAnd it starts… right now.",
    "فإذا كانت الآلة تتعلّم…\nفما هو عذرك؟",
    style='normal'
)

gen.doc.add_paragraph()

# Meta note
gen.add_parallel_section(
    "This chapter was created through the collaboration of human creativity and AI assistance, embodying the very philosophy it expresses.",
    "تم إنشاء هذا الفصل من خلال التعاون بين الإبداع البشري والمساعدة الاصطناعية، مجسداً الفلسفة ذاتها التي يعبر عنها.",
    style='normal'
)

# Save
gen.save('/data/data/com.termux/files/home/Ahmed/AhmedGoldMine/Chapter_1_The_Spark_Bilingual.docx')
