import re

def translate_html():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    replacements = {
        # Meter UI
        'diagnose-overtuiging': 'diagnostic conviction',
        'twijfel': 'doubt',
        'herkenning': 'recognition',
        'zekerheid': 'certainty',
        
        # Banner & generic feed
        '"Gedachten: \\u201cIk voel me slecht\\u2026 wat is er mis met mij?\\u201d"': '"Thoughts: \\u201cI feel bad\\u2026 what is wrong with me?\\u201d"',
        '"Gedachten: \\u201cIk wil meer zien, ik blijf maar scrollen\\u2026\\u201d"': '"Thoughts: \\u201cI want to see more, I just keep scrolling\\u2026\\u201d"',
        '"Gedachten: \\u201cIk herken alles. Misschien heb ik dit ook.\\u201d"': '"Thoughts: \\u201cI recognize everything. Maybe I have this too.\\u201d"',
        '"Gedachten: \\u201cIk herken mezelf hierin, maar het definieert me niet.\\u201d"': '"Thoughts: \\u201cI recognize myself in this, but it doesn\'t define me.\\u201d"',
        '>Sociale media<': '>Social media<',
        'Scroll naar beneden en ontdek de volgende posts.': 'Scroll down and discover the next posts.',
        'Meer informatie': 'More information',
        
        # Special pop
        'De realiteit achter overmatig sociale media gebruik': 'The reality behind excessive social media use',
        'Overmatig gebruik van sociale media wordt in verband gebracht met concentratieproblemen, een lager zelfbeeld en depressieve gevoelens.': 'Excessive social media use is associated with concentration problems, lower self-esteem, and feelings of depression.',
        'Scroll verder naar beneden om door te gaan.': 'Keep scrolling down to continue.',
        
        # Slideshow
        'De keerzijde van die mooie diagnose post': 'The downside of that beautiful diagnosis post',
        'Veeg of sleep naar links/rechts om meer te lezen.': 'Swipe or drag left/right to read more.',
        'Onjuiste of overdreven informatie over mentale gezondheid kan een vertekend beeld geven en aanzetten tot zelfdiagnose.': 'Incorrect or exaggerated information about mental health can create a distorted picture and encourage self-diagnosis.',
        'Gelezen': 'Read',
        
        # Description
        'Beschrijving': 'Description',
        'De schaduwzijde van content over zelfbeschadiging of suïcide': 'The dark side of content about self-harm or suicide',
        'Blootstelling aan content over zelfbeschadiging of suïcide kan gevoelens versterken, risicogedrag normaliseren en kwetsbare jongeren negatief beïnvloeden.': 'Exposure to content about self-harm or suicide can intensify feelings, normalize risky behavior, and negatively impact vulnerable youth.',
        
        # Start scene
        'Stap in het verhaal van Mislabel': 'Step into the story of Mislabel',
        '>of<': '>or<',
        'Blijf kritisch kijken<br/>naar wat je ziet,<br/>ook in dit verhaal.': 'Keep looking critically<br/>at what you see,<br/>even in this story.',
        
        # Dokter Popup
        'Offline drempels, online gevolgen': 'Offline barriers, online consequences',
        'Geen afspraak mogelijk voor een diagnose': 'No appointment available for a diagnosis',
        'Veel jongeren ervaren drempels bij hulp, zoals wachttijden, kosten of beperkte toegang. TikTok kan herkenning bieden. Zelfdiagnose geeft soms duidelijkheid en gemeenschap, maar vervangt geen professionele hulp. Professionals blijven de meest betrouwbare bron.': 'Many youth experience barriers to help, such as wait times, costs, or limited access. TikTok can offer recognition. Self-diagnosis sometimes provides clarity and community, but it does not replace professional help. Professionals remain the most reliable source.',
        
        # Outcomes
        '>Uitkomst 1<': '>Outcome 1<',
        '“Dit is het… dit verklaart alles.”': '“This is it… this explains everything.”',
        '>Resultaat: Tunnelvisie<': '>Result: Tunnel vision<',
        '>Melding:<': '>Notice:<',
        'Zie het als een eerste vermoeden, geen diagnose. Blijf kritisch en check meerdere betrouwbare bronnen voordat je conclusies trekt of hulp zoekt.': 'Consider it an initial suspicion, not a diagnosis. Remain critical and consult multiple reliable sources before drawing conclusions or seeking help.',
        
        '>Uitkomst 2<': '>Outcome 2<',
        '“Het helpt me begrijpen hoe ik me voel.”': '“It helps me understand how I feel.”',
        '>Resultaat: Vrije keuze<': '>Result: Free choice<',
        'Sluit sociale media': 'Close social media',
        
        # Final Scene
        'Vermoeden of echte diagnose?': 'Suspicion or real diagnosis?',
        'Zelfdiagnose via sociale media ≠ klinische diagnose': 'Self-diagnosis via social media ≠ clinical diagnosis',
        'Klik op een knop om verder te gaan.': 'Click a button to continue.',
        'Dit is een vermoeden, geen zelfdiagnose.': 'This is a suspicion, not a self-diagnosis.',
        'Professionele hulp zoeken': 'Seek professional help'
    }

    # Custom targeted replacements:
    replacements['STAP IN HET VERHAAL VAN MISLABEL'] = 'STEP INTO THE STORY OF MISLABEL'
    
    for old_text, new_text in replacements.items():
        content = content.replace(old_text, new_text)

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == "__main__":
    translate_html()
