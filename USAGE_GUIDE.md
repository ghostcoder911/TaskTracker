# 📱 Usage Guide - Task Tracker

A visual guide on how to use the Task Tracker application.

## Overview

Task Tracker is a chat-based system where team members check in at the start and end of each day. The chatbot asks questions, collects responses, and saves everything to Google Sheets.

## User Journey

### Step 1: Access the Application

Open the Task Tracker URL in your browser (e.g., `http://localhost:3000` or your deployed URL).

**You'll see the Welcome Screen:**
- Clean, modern interface
- Purple gradient header
- Name input field
- Two radio buttons: "Start of Day" and "End of Day"

### Step 2: Enter Your Information

1. **Type your name** in the input field
2. **Select check-in type:**
   - 🌅 **Start of Day** - For morning check-ins
   - 🌇 **End of Day** - For evening check-outs
3. **Click "Start Check-in"**

### Step 3: Chat with the Bot

The chat interface opens with:
- Your name in the header
- Check-in type indicator
- Progress bar showing how many questions remain
- Chat messages area
- Input field at the bottom

**The bot will:**
- Greet you with a friendly message
- Ask questions one at a time
- Wait for your response
- Show typing indicator while processing

### Step 4: Answer Questions

#### Morning Check-in (5 Questions)

1. **Energy Check** ☕
   - Example: "Coffee and feeling good!"
   - What's your morning vibe?

2. **Yesterday's Progress** 📋
   - Example: "Completed API integration, Fixed 3 bugs"
   - What did you accomplish?

3. **Today's Priorities** 🎯
   - Example: "1. Review PRs, 2. Start new feature, 3. Team meeting"
   - What will you focus on?

4. **Blockers** 🚧
   - Example: "Waiting for design assets"
   - Any obstacles?

5. **State of Mind** 💭
   - Example: "Focused"
   - One word for how you feel

#### Evening Check-out (5 Questions)

1. **Today's Wins** 🎉
   - Example: "Deployed new feature, Helped teammate debug issue"
   - What did you accomplish?

2. **Learnings** 💡
   - Example: "Learned about React hooks optimization"
   - Anything new you discovered?

3. **Challenges** 🤔
   - Example: "Performance issue with large datasets"
   - What was difficult?

4. **Tomorrow's Focus** 🔜
   - Example: "Continue optimization work, Write tests"
   - What's next?

5. **Ending Mood** 🌙
   - Example: "Satisfied and ready to rest"
   - How are you feeling?

### Step 5: Review Progress

As you answer:
- Your messages appear on the right (purple background)
- Bot messages appear on the left (white background)
- Progress bar fills up
- Counter shows: "3 / 5" (current/total questions)

### Step 6: Completion

After the last question:
- Bot shows success message: "✅ All done! Your responses have been saved. Have a great day! 🌟"
- "Start New Check-in" button appears
- You can start another check-in or close the browser

### Step 7: View Your Data

**In Google Sheets:**
1. Open your shared spreadsheet
2. Look for today's date as a worksheet tab
3. See all team responses organized in rows

**Columns include:**
- Timestamp
- Name
- Type (Morning/Evening)
- All responses in order

## Tips for Great Check-ins

### Be Concise
✅ Good: "Fixed login bug, reviewed 3 PRs"
❌ Too long: "I started my day by checking emails, then I fixed the login bug that was reported yesterday, after that I reviewed three pull requests from the team..."

### Be Honest
✅ Good: "Struggling with the new API documentation"
❌ Not helpful: "Everything is fine" (when it's not)

### Be Specific
✅ Good: "Waiting for API keys from DevOps"
❌ Too vague: "Some blockers"

### One Word for Mood
✅ Good: "Energized", "Focused", "Tired", "Excited"
❌ Not one word: "Feeling pretty good today"

## Use Cases

### Daily Standup Replacement
- Team members check in async
- Review responses in team meeting
- Focus discussion on blockers and help needed

### Remote Team Alignment
- Keep everyone connected
- See what everyone is working on
- Spot patterns and trends

### Personal Reflection
- Track your own progress
- See what energizes you
- Identify recurring blockers

### Management Insights
- Monitor team morale
- Identify bottlenecks early
- Celebrate wins
- Provide support where needed

## Viewing Team Data

### Google Sheets Interface

**Daily View:**
- Each date is a separate worksheet
- Easy to see today's updates

**Weekly Review:**
- Compare multiple days
- Spot trends
- Export to Excel for analysis

**Individual Tracking:**
- Filter by name
- See one person's journey
- Understand individual patterns

### Data Analysis Tips

1. **Mood Tracking**
   - Notice patterns in state of mind
   - Correlate with wins/challenges

2. **Blocker Identification**
   - See recurring obstacles
   - Take action to resolve

3. **Productivity Patterns**
   - Compare mornings vs evenings
   - Understand energy levels

4. **Team Dynamics**
   - Who helps whom
   - Cross-team dependencies

## Best Practices

### Timing

**Morning Check-in:**
- Do it first thing when you start work
- Before diving into tasks
- Sets intention for the day

**Evening Check-out:**
- End of workday
- Before closing your laptop
- Reflection while fresh in mind

### Consistency

- Check in every working day
- Same time each day helps build habit
- Don't skip even if "nothing happened"

### Privacy

- Be professional but genuine
- Share what's helpful for the team
- Don't overshare personal issues

### Team Culture

- Encourage honest responses
- No judgment on blockers or challenges
- Celebrate wins together
- Offer help when needed

## Common Scenarios

### "I forgot to check in this morning"

**Solution:** 
- Check in when you remember
- Still valuable even if late
- Note was late in progress field

### "I have nothing new to report"

**Solution:**
- Still check in
- "Continuing yesterday's work" is fine
- Routine updates are valuable

### "I need to update my morning response"

**Current:** Can't edit once submitted
**Workaround:** Add note in evening check-out
**Future:** Edit feature may be added

### "Can I do both check-ins at once?"

**Answer:** Yes, but not recommended
- Do them at appropriate times
- Better reflection when separate
- More accurate data

## Troubleshooting

### "Chat is stuck"

**Fix:**
- Refresh the page
- Start new check-in
- Previous data is saved

### "I can't find my responses"

**Check:**
1. Correct Google Spreadsheet
2. Today's date worksheet tab
3. Your name in the Name column

### "Bot isn't responding"

**Try:**
1. Check internet connection
2. Verify backend is running
3. Refresh the page
4. Contact admin if persists

## Mobile Usage

The app works great on mobile:
- Responsive design
- Touch-friendly buttons
- Scrollable chat
- Easy typing on phone keyboard

**Tip:** Add to home screen for quick access!

### iOS
1. Open in Safari
2. Tap share button
3. "Add to Home Screen"

### Android
1. Open in Chrome
2. Menu → "Add to Home Screen"

## Keyboard Shortcuts

- **Enter** - Submit response
- **Refresh page** - Start over
- **Esc** (future) - Cancel session

## Privacy & Security

### What's Stored
- Your name (as you entered it)
- Your responses to questions
- Timestamp of responses
- Check-in type

### What's NOT Stored
- No passwords
- No email addresses
- No IP addresses
- No browsing data

### Who Can See
- Team members with access to the shared Google Sheet
- Spreadsheet owner
- Service account (automated access only)

### Data Retention
- Google Sheets: Forever (unless manually deleted)
- Backend: Only during active session
- No long-term storage on server

## Getting Help

### During Check-in
- Type your question in the chat
- Bot will respond (or may not understand)
- Cancel and restart if needed

### Technical Issues
- Check with your team admin
- Review documentation
- Check backend health: `/api/health`

### Feedback
- Share suggestions with your team
- Request new features
- Report bugs

## Advanced Features

### Multiple Check-ins Per Day
- Can do multiple morning or evening check-ins
- Each saved separately
- Useful for split shifts

### Team Analytics (Manual)
1. Export Google Sheet data
2. Create pivot tables
3. Analyze trends
4. Share insights

### Integration (Future)
- Slack notifications
- Email reminders
- Calendar integration
- Analytics dashboard

---

## Quick Reference

### Morning Questions (5)
1. Energy Check
2. Yesterday's Progress
3. Today's Priorities
4. Blockers
5. State of Mind

### Evening Questions (5)
1. Today's Wins
2. Learnings
3. Challenges
4. Tomorrow's Focus
5. Ending Mood

### URLs
- Local: `http://localhost:3000`
- Production: (your deployed URL)
- API Health: `/api/health`

### Support
- Documentation: `README.md`
- Quick Start: `QUICKSTART.md`
- Setup Guide: `SETUP.md`

---

**Remember:** The goal is to stay aligned as a team and move faster together! 🚀

Keep it crisp, honest, and consistent! 💪

