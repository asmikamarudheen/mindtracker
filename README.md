

### Project Description
[<p align="center">
  <img src="./img.png" alt="Project Banner" width="100%">
</p>

# MindTracker 🎯

## Basic Details

### Team Name: [TechTinkerettes]

### Team Members
- Member 1: [Asmi Kamarudheen] - [Vidya Academy of Science and Technology]
- Member 2: [Fareedha Shihabudheen] - [Vidya Academy of Science and Technology]

### Hosted Project Link
[mention your project hosted link here]

### Project Description
[MindTracker is a web-based stress assessment tool that uses a 5-question survey to calculate and display a user's stress score instantly]

### The Problem statement
[n today’s fast-paced lifestyle, especially among students and working professionals, stress often goes unnoticed until it becomes severe. Many people do not have access to immediate mental health screening tools.]

### The Solution
[]

---

## Technical Details

### Technologies/Components Used

**For Software:**
- Languages used: [e.g.,  Python,HTML,CSS]
- Frameworks used: [e.g., Flask]
- Libraries used: [e.g.,Flask]
- Tools used: [e.g., VS Code, Git,Github]

**For Hardware:**
- Main components: [List main components]
- Specifications: [Technical specifications]
- Tools required: [List tools needed]

---

## Features

List the key features of your project:
- Feature 1: [User friendly interface]
- Feature 2: [stress score calculation]
- Feature 3: [real time processing]


---

## Implementation

### For Software:

#### Installation
```bash
[Installation commands - e.g.,pip install flask]
```

#### Run
```bash
[Run commands - e.g., python app.py]
```

### For Hardware:

#### Components Required
[List all components needed with specifications]

#### Circuit Setup
[Explain how to set up the circuit]

---

## Project Documentation

### For Software:

#### Screenshots (Add at least 3)
https://drive.google.com/drive/folders/1ercx3sj5XCybrZM6Pux-L0AGGsDF-4Ha?usp=sharing
#### Diagrams

**System Architecture:**

![Architecture Diagram](docs/architecture.png)
*Explain your system architecture - components, data flow, tech stack interaction*

**Application Workflow:**

![Workflow](docs/workflow.png)
*Add caption explaining your workflow*

---



Additional Documentation

For Web Projects with Backend

API Documentation

Base URL: http://localhost:5000

(Production URL depends on deployment platform)

Endpoints

GET /
Description: Loads the home page (index.html).
Response: Renders the homepage template.

GET /survey
Description: Displays the 5-question stress assessment survey page.
Response: Renders the survey.html template.

POST /submit
Description: Processes the submitted survey form, calculates the stress score, stores the result, and displays feedback.

Request Form Data:

stress (integer) – Stress level rating

sleep (integer) – Sleep quality rating

mood (integer) – Mood rating

motivation (integer) – Motivation level rating

anxiety (integer) – Anxiety level rating

Processing Logic:

Calculates total score out of 25

Converts total score into percentage

Stores the percentage in data.json

Determines stress category:

Less than 40% → Low Stress

40% to 69% → Moderate Stress

70% and above → High Stress

Response:
Returns an HTML page displaying:

Calculated Stress Percentage

Personalized Stress Message

Link to return to Home page

Data Storage

Stress scores are stored in a local file named data.json

Each submission appends a new percentage value

This data can be used for dynamic stress trend graph visualization

#### Installation Guide

**For Android (APK):**
1. Download the APK from [Release Link]
2. Enable "Install from Unknown Sources" in your device settings:
   - Go to Settings > Security
   - Enable "Unknown Sources"
3. Open the downloaded APK file
4. Follow the installation prompts
5. Open the app and enjoy!

**For iOS (IPA) - TestFlight:**
1. Download TestFlight from the App Store
2. Open this TestFlight link: [Your TestFlight Link]
3. Click "Install" or "Accept"
4. Wait for the app to install
5. Open the app from your home screen

**Building from Source:**
```bash
# For Android
flutter build apk
# or
./gradlew assembleDebug

# For iOS
flutter build ios
# or
xcodebuild -workspace App.xcworkspace -scheme App -configuration Debug
```

---

## Project Demo

### Video
[Add your demo video link here - YouTube, Google Drive, etc.]

https://drive.google.com/drive/folders/1t7w9uI1hLYPVn35Ix41qjUeFY7yLfZNN?usp=sharing



## AI Tools Used (Optional - For Transparency Bonus)

If you used AI tools during development, document them here for transparency:

**Tool Used:** [e.g., GitHub Copilot, v0.dev, Cursor, ChatGPT, Claude]

**Purpose:** [What you used it for]
- Example: "Generated boilerplate React components"
- Example: "Debugging assistance for async functions"
- Example: "Code review and optimization suggestions"

**Key Prompts Used:**
- "Create a REST API endpoint for user authentication"
- "Debug this async function that's causing race conditions"
- "Optimize this database query for better performance"

**Percentage of AI-generated code:** [Approximately X%]

**Human Contributions:**
- Architecture design and planning
- Custom business logic implementation
- Integration and testing
- UI/UX design decisions

*Note: Proper documentation of AI usage demonstrates transparency and earns bonus points in evaluation!*

---

## Team Contributions

- [Name 1]: [Specific contributions - e.g., Frontend development, API integration, etc.]
- [Name 2]: [Specific contributions - e.g., Backend development, Database design, etc.]
- [Name 3]: [Specific contributions - e.g., UI/UX design, Testing, Documentation, etc.]

---


Made with ❤️ at TinkerHub



b
