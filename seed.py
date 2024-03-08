import sqlite3

DATABASE = 'instance/app.sqlite'

def seed_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    
    success_stories = [
        ("1", "Jane Wawuda", "I can now live a more productive life because with the help of this system I broke the chains of Alcoholism. I guarantee and recommend that you will have a progressive journey.", "http://localhost:5000/mystory/1"),
        ("2", "Abdallah Masoud", "After struggling with addiction for years, I decided to seek help. Through counseling and support from this addiction solver app, I successfully overcame my addiction. Today, I am living a healthier and happier life.", "http://localhost:5000/mystory/2"),
        ("3", "John Majiba", "My journey with this application has helped me to practice self control against browsing unproductively on social media.", "http://localhost:5000/mystory/3"),
        ("4", "Isaack Kulot", "I've tried so many times, but The Addiction Solver helped me make it work. After 10 years in addiction, my kids finally call me 'Daddy' again.", "http://localhost:5000/mystory/4"),
        ("5", "Joanna Macabus", "Through the trusting guidance of the programs of Addiction Solver, I finally had the courage to go back and make peace with the demons inside me.", "http://localhost:5000/mystory/5"),
        ("6", "Mirriam Nimo", "It felt like I search a million treatment centers, The Addiction Solver was the only one that helped me about what was happening to our daughter…and our family.", "http://localhost:5000/mystory/6"),
        ("7", "William Namanu", "The Addiction Solver was the complete opposite of what I expected or had gone through in other programs. I found myself looking forward to sessions and feeling the weight lifting off of my shoulders with every new day.", "http://localhost:5000/mystory/7"),
        ("8", "William", "This is where I learned to deal with my problems properly instead of running away. I learned that I mattered.", "http://localhost:5000/mystory/8"),
        ("9", "Kelvin Ogembo", "I'm 9 years sober thanks to Addiction Solver helping me reconnect to myself & God.", "http://localhost:5000/mystory/9"),
        ("10", "Christine Ngandi", "In just 30 days, my doctor at Addiction Solver helped me find a special person I didn't realize lived inside of me.", "http://localhost:5000/mystory/10")
    ]
    
    addiction_types = [
        ('Substance use disorder',),
        ('Sexual',),
        ('Technology',),
        ('Gambling',) 
        ]

    e_resources = [
        ("Understanding Substance Abuse: Common Causes and Long-Term Effects",
         "Substance abuse affects millions, disrupting lives and health. It's a disease, not a choice, often driven by genetics, mental health, stress, and environmental factors. Childhood trauma and lack of social support play a role. Long-term abuse leads to severe health issues. Seeking help is crucial. Sage Clinic offers resources and care for recovery.",
         "https://sageclinic.org/blog/substance-abuse-causes-long-term-effects/",  
         "Addiction and Identity",
         "https://www.youtube.com/embed/J9eObiqMPnk?si=31OGaicLfsHLSnh6",
         1,
         1
         ),

         ("Drug Addiction Recovery Stories: Inspiring",
          "Read inspiring stories of triumph and transformation from individuals who have overcome drug addiction. These accounts offer hope and motivation for those on their own journey to recovery.",
          "https://lantanarecovery.com/drug-addiction-recovery-stories-inspiring-accounts-of-triumph-and-transformation/",
          "How to overcome drug addiction | The Old Path",
          "https://www.youtube.com/embed/7htpmP2QxLI?si=7QMYeQ9fxtzuAcVg",
          2,
          2     
         ),

         ("Stigma of Sex Addiction",
          "This article addresses the stigma surrounding sexual addiction and the barriers individuals may face in seeking help. It emphasizes the importance of breaking the shame cycle and seeking support from qualified professionals and support groups.",
          "https://inpatient-rehab.co.uk/blog/stigma-of-sex-addiction",
          "We Need To Talk About Sex Addiction",
          "https://www.youtube.com/embed/-Qf2e3XZ8Tw?si=VRkGCNL2Z4knPcTs",
          2,
          1
          ),

          (
             "Sex Addiction, Hypersexuality and Compulsive Sexual Behavior",
              "This article provides an overview of sexual addiction, including its causes, symptoms, and various treatment options available. It explores the psychological and emotional aspects of sexual addiction and offers insights into recovery.",
              "https://my.clevelandclinic.org/health/diseases/22690-sex-addiction-hypersexuality-and-compulsive-sexual-behavior",
              "Sex, Porn & Manhood",
              "https://www.youtube.com/embed/R1vJilg7BAQ?si=s7K43Em5hxThzL_G",
              2,
              2
          ),

          (
             "Mental wellness and digital devices: The impact of screen time on mental health",
              "This article explores the relationship between excessive screen time and mental health, discussing the negative effects of technology addiction on mood, sleep, attention span, and interpersonal relationships.",
              "https://www.kaspersky.com/resource-center/preemptive-safety/mental-health",
              "The REAL Effects of Internet Addiction",
              "https://www.youtube.com/embed/p2contq5aRg?si=zP5BSU9QdrMKeFP4",
              3,
              1
          ),

          (
              "Strategies for establishing healthy technology boundaries",
              "This article offers practical tips and advice for setting boundaries and establishing healthy technology habits. It covers strategies such as implementing screen-free zones, scheduling tech-free time, and practicing mindful tech use.",
              "https://www.miriamstl.org/aboutmiriam/news/post-details/~board/blogs/post/strategies-for-establishing-healthy-technology-boundaries",
              "How to Get Rid of Your Technology Addiction",
              "https://www.youtube.com/embed/8e1ezeq3C9c?si=Gym4i4Cbs-IqePxd",
              3,
              2
          ),

          (
             "Compulsive Gambling Symptoms, Causes and Effects",
              "This article provides an overview of gambling addiction, including common signs and symptoms, the impact of gambling on mental health and relationships, and various treatment options available for recovery.",
              "https://www.psychguides.com/behavioral-disorders/gambling-addiction/symptoms-and-effects/",
              "9 Signs of Gambling Addiction or Problem Gambling",
              "https://www.youtube.com/embed/BdgrhO0IrlQ?si=S5C8fnvEjUsCv5_T",
              4,
              1
          ),

          (
              "Dealing with Gambling Addiction Relapses",
              "Relapse can be a challenging but crucial aspect of recovery from gambling addiction. This article emphasizes that relapse should not be seen as a failure, but rather as an opportunity for growth and recommitment to recovery. It distinguishes between a slip, a brief lapse in judgment, and a relapse, a return to gambling after a period of sobriety.",
              "https://www.algamus.org/blog/gambling-addiction-relapses",
              "The fall and rise of a gambling addict",
              "https://www.youtube.com/embed/7AN3VLLlkdI?si=bd7e5DRd81cIUXK2",
              4,
              2
          )

    ]
    # cursor.executemany('INSERT INTO success_stories (user_id, user_name, story, story_url) VALUES (?, ?, ?, ?)', success_stories)
    # cursor.executemany('INSERT INTO addiction (addiction_type) VALUES (?)', addiction_types)
    cursor.executemany("INSERT INTO educational_resources(title, body, article_link, video_name, video_link, type_id, level_id) VALUES(?, ?, ?, ?, ?, ?, ?)", e_resources)

    conn.commit()
    conn.close()

seed_db()