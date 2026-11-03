# JLPT N3 Daily Challenge — Deployment starter

## Current status

- `index.html` is the previously created v3 game. It runs on GitHub Pages.
- The existing game stores progress locally and exchanges result codes. **It is not yet connected to Firebase.**
- `data/lesson-plan.json` is a planning template, **not a working automatic lesson loader**.
- `firebase/firestore.rules` is a proposed rules starter, **not deployed**. These rules restrict fields and permit one create per anonymous UID per challenge, but do NOT prove scores were earned honestly. Anonymous accounts can be recreated.
- No Outlook email has been sent and no public URL has been created.

## Step 1: GitHub Pages

1. Sign in to https://github.com/ using an account permitted by your organization's IT policies.
2. Create a repository named `jlpt-n3-daily-challenge` (public repo on GitHub Free).
3. Upload the contents of this folder, retaining `index.html` at repository root.
4. Open **Settings > Pages > Build and deployment > Deploy from a branch**.
5. Choose `main` and `/(root)`, then Save.
6. Open the displayed site URL, typically `https://YOUR_USERNAME.github.io/jlpt-n3-daily-challenge/`.
7. Test on both desktop and phone, especially Japanese voice selection and the result-code exchange.

## Step 2: Firebase (future integration)

1. Open https://console.firebase.google.com/ and create a project if permitted by IT.
2. Add a Web app, then enable Firestore and Firebase Authentication > Sign-in method > Anonymous.
3. Add the GitHub Pages domain to Firebase Authentication authorized domains if required.
4. Review the sample `firebase/firestore.rules` and publish approved rules.
5. A developer must integrate Firebase SDK into `index.html`, implement authentication, write scores and read rankings. **This starter does not implement that integration.**
6. For trustworthy ranked competition, validate answer submissions on a server/Cloud Function; Firestore rules alone cannot verify scores or prevent replay/multiple anonymous accounts.
7. Never put Firebase service-account private keys or Outlook credentials in the public repository. Firebase web app configuration is public by design; security comes from rules and backend checks.

## Step 3: Daily content workflow

- Cycle: Chapter 1 Lesson 1–5, then Chapter 1 review, then Chapter 2 Lesson 1–5, review, etc.
- At 08:00 Asia/Tokyo, prepare or review 20 original questions; ensure Kanji readings and answer keys are verified.
- The currently scheduled ChatGPT task prepares content but **cannot automatically commit to GitHub or update the game**.
- To publish today: edit the game question data and upload updated `index.html` to the repository; GitHub Pages republishes after the commit.
- Future automation needs a trusted content generator, validation step, and GitHub Actions or authorized GitHub API access.
- Respect JTest's site terms; do not copy entire question banks without permission.

## Step 4: Manual Outlook invitation

Only after the website works:

To: nafarina.nhazmee@murata.com
Subject: JLPT N3 Daily Challenge — Let's study together!

Hi,

I'd like to invite you to our JLPT N3 Daily Challenge! We'll practice one lesson each day and have a chapter review after every five lessons. We can compare our scores and improve together.

Game link: [INSERT VERIFIED GITHUB PAGES URL]
Today's lesson: [INSERT LESSON]

See you on the leaderboard!

**Do not send until the URL has been verified.**
