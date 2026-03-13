# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

---
- Whatever number I enter keeps showing the hint "Go Lower", even when the number I put is 1. The solution was 77.
When the solution was 77, I started at 15 and the hint was "Go Lower". I expected it to be "Go Higher" 
- When I get the "Game Over", I can't start a new game. 
After finishing a game, I tried to press New Game. I expected a new game to start, but instead I just kept seeing the "Game Over", and I couldn't start a new game. 
- When I changed the mode to easy mode, the range was supposed to be 1-20, but the secret was 31. I expected the secret to be  within the range the numbers were supposed to be in. The secret ended up being 31, which was outside of the range. 


## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
I used Claude as the AI tool for this project.
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
Claude showed me where the functionality for Higher and Lower was going wrong. It suggested I change the solution so that the higher and lower functionality is working as intended. I verified this by making sure the test cases I created work working as intended and also manually playing the game.
AI Solution:
if guess > secret:
        return "Too High", "📉 Go LOWER!"
    else:
        return "Too Low", "📈 Go HIGHER!"

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
One time I was trying to figure out how to make my "Submit Guess" button work on every click, it asked me to use a streamlit form and that would batch my submission into a single rerun. Although this could have worked I felt as though it was leading me in a direction I didn't want ot go. That's because it was going to change my UI and I believe keeping the core functionality easy to comprehend is a big reason why this project is successful.
AI Solution:
with st.form(key="guess_form"):
    raw_guess = st.text_input(
        "Enter your guess:",
        key=f"guess_input_{difficulty}"
    )

    col1, col2 = st.columns(2)
    with col1:
        submit = st.form_submit_button("Submit Guess 🚀")
    with col2:
        show_hint = st.checkbox("Show hint", value=True)
new_game = st.button("New Game 🔁")
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
One thing I did is implement changes on the UI to make sure it was working as intended. Another thing I did is create test cases. 
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
One test case that I ran was to check if the secret number is getting the proper response from my guesses. When I first started, the secret that we started off with 
- Did AI help you design or understand any tests? How?
AI helped me design my guess too high or too low tests. Basically it used an example as a secret, in this case it was 50, and if my guess was 60, I would get "Go Lower" as the response and when my guess was 40 I would get "Go Higher". 

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
I learned that Streamlit state sometimes takes a while to render. Basically, on the submit guess feature, it sometimes requires multiple clicks to process state. I would say Streamlit is really cool cause it makes creating an application on the web very seamless. 

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
One thing that I did was always ask Claude where specific code could be altered or fixed, then I read through those blocks of code to understand what's happening. Then I'd ask for a specific line prompt in order to solve the questions accordingly. 
- What is one thing you would do differently next time you work with AI on a coding task?
One thing I would do differntly is try to use Claude to find specific lines faster, as opposed to asking for it to fix something then wondering if it's right or wrong. Another thing I will use is the "Plan" mode a lot more aggressively. I'd like to know what steps it'll take before it makes changes so that the changes make sense to me. 
- In one or two sentences, describe how this project changed the way you think about AI generated code.
I think AI does a great job at generating code and helping us solve issues a lot quicker. I haven't used AI to make projects before but I think now I can make full fledged apps a lot quicker and improve my skills exponentially with the use of AI.