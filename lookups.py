from Duty import Duty

duties_map = {
        1: Duty(1, "Duty 1 Script and code in at least one general purpose language and at least one domain-specific language to orchestrate infrastructure, follow test driven development and ensure appropriate test coverage."),
        2: Duty(2, "Duty 2 Initiate and facilitate knowledge sharing and technical collaboration with teams and individuals, with a focus on supporting development of team members."),
        3: Duty(3, "Duty 3 Engage in productive pair/mob programming to underpin the practice of peer review."),
        4: Duty(4, "Duty 4 Work as part of an agile team, and explore new ways of working, rapidly responding to changing user needs and with a relentless focus on the user experience. Understand the importance of continual improvement within a blameless culture."),
        5: Duty(5, "Duty 5 Build and operate a Continuous Integration (CI) capability, employing version control of source code and related artefacts"),
        6: Duty(6, "Duty 6 Implement and improve release automation & orchestration, often using Application Programming Interfaces (API), as part of a continuous delivery and continuous deployment pipeline, ensuring that team(s) are able to deploy new code rapidly and safely."),
        7: Duty(7, "Duty 7 Provision cloud infrastructure using APIs, continually improve infrastructure-as-code, considering use of industry leading technologies as they become available (e.g. Serverless, Containers)."),
        8: Duty(8, "Duty 8 Evolve and define architecture, utilising the knowledge and experience of the team to design in an optimal user experience, scalability, security, high availability and optimal performance."),
        9: Duty(9, "Duty 9 Apply leading security practices throughout the Software Development Lifecycle (SDLC)."),
        10: Duty(10, "Duty 10 Implement a good coverage of monitoring (metrics, logs), ensuring that alerts are visible, tuneable and actionable."),
        11: Duty(11, "Duty 11 Keep up with cutting edge by committing to continual training and development - utilise web resources for self-learning; horizon scanning; active membership of professional bodies such as Meetup Groups; subscribe to relevant publications."),
        12: Duty(12, "Duty 12 Look to automate any manual tasks that are repeated, often using APIs."),
        13: Duty(13, "Duty 13 Accept ownership of changes; embody the DevOps culture of 'you build it, you run it', with a relentless focus on the user experience.")
    }

themes = {
    "1 Apprenticeship": 'apprenticeship',
    "2 Bootcamp": 'bootcamp',
    "3 Automate!": 'automate',
    "4 Houston, Prepare to Launch": 'houston',
    "5 Going Deeper": 'deeper',
    "6 Assemble": 'assemble',
    "7 Call Security": 'security'
}

themes_formatted = {
    'apprenticeship': 'Apprenticeship',
    'bootcamp': 'Bootcamp',
    'automate': 'Automate!',
    'houston': 'Houston, Prepare to Launch',
    'deeper': 'Going Deeper',
    'assemble': 'Assemble!',
    'security': 'Call Security'
}

themes_to_duties_map = {
    'apprenticeship': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
    'bootcamp': [1, 2, 3, 4, 13],
    'automate': [5, 7, 10],
    'houston': [6, 7, 10, 12],
    'deeper': [11],
    'assemble': [8],
    'security': [9]
}

choices_themes = [
        "1 Apprenticeship",
        "2 Bootcamp",
        "3 Automate!",
        "4 Houston, Prepare to Launch",
        "5 Going Deeper",
        "6 Assemble",
        "7 Call Security"
        ]

choices_display = [
        "1 View duties in terminal",
        "2 View duties in browser",
        "3 Output duties as HTML",
        "4 Download duties as HTML"
    ]