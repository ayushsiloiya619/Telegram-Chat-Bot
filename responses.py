from datetime import datetime


def sample_responses(input_text):
    user_message = str(input_text).lower()

    if user_message in ("Hi", "hi", "hey", "hi jarvis", "Hi jarvis", "jarvis", "hello", "Hello"):
        return "Hello dear. How may i help you sir/madam."

    if user_message in ("kaise ho", "tum kaise ho", "", "", "", "", ""):
        return "Mein Badiya hu sir/madam ap bataiye.."

    if user_message in ("", "motivation", "thoughts", "", "", "", ""):
        return "The man who does not read books has no advantage over the one who cannot read them." \
               "The beautiful thing about learning is that no one can take it away from you."

    if user_message in ("wow", "wonderful", "nice", "amazing", "awesome", 'lovely', "woww"):
        return "Thank you. " \
               "It's my pleasure sir/madam to meet you."

    if user_message in ("", "thanks", "thank you", "thx", "", "", ""):
        return "Welcome sir/madam." \
               "It's my pleasure sir/madam to meet you."

    if user_message in ("", "theek hai", "thik hai", "thik", "thk", "theek", ""):
        return "Ok sir/madam ji "

    if user_message in ("bahut badiya", "gazab", "ache ho", "tum ache ho", "", "", "badiya"):
        return "Shukriya sir/madam." \
               " Mein apki seva mein hazir hu kabi bi.(*^*)"

    if user_message in ("yaar", "bhai", "suno na", "kuch bolu", "mujhe kuch bolna hai", "sun", 'sunn'):
        return "Ha boliye.."

    if user_message in ("kuch nhi", "koi na", "glti se send hogya message", "kuch nahi"):
        return "Ok koi help chaiye ho toh bataiyega."

    if user_message in ("translate", "eng_hindi", "engtohindi", "", "", "", ""):
        return "sorry i am on learning."

    if user_message in ("movies", "movie", "share movie link", "links", "link","movie link"):
        return "https://m.vegamovies.ink/ & https://thekhatrimaza.wiki/"

    if user_message in ("how are you?", "How are you ?", "How are you", "how are you"):
        return "I am fine. What about you?"
    if user_message in ("creator", "author", "admin", "who are you"):
        return "My author/admin name is Ayush Siloiya"
    if user_message in ("date", "time", "month", "samay", "Time", "Date"):
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y , %H:%M:%S")
        return str(date_time)

    if user_message in ("help", "emergency", "need help", "h", "H", "police", "p", "P"):
        return "Call 100 for police helpline."

    if user_message in ("", "aur batao", "aur", "kuch batao", "kuch bolo", "bolo", ""):
        return "Bas kuch ni mein theek hu ."

    if user_message in ("", "impress me", "make me happy", "make me smile", "can u make me smile", "pick up line", ""):
        return "Do you happen to have a Band-Aid? ‘Cause I scraped my knees falling for you." \
               "" \
               " Your eyes are like the ocean; I could swim in them all day."

    if user_message in (
    "hasao mujhe", "hasa ke dikhao mujhe", "khush karo mujhe", "khush", "hassi", "mujhe hasa ke dikhao", "mujhe hasao"):
        return "मास्टर जी- तुमने होमवर्क क्यों नहीं किया " \
               "  चिंटू- मैं हॉस्टल में रहता हूं ना..." \
               "   मास्टर जी- तो." \
               "   चिटू- हॉस्टल में होमवर्क कैसे कर सकता हूं, हॉस्टल वर्क देना चाहिए था ना. " \
               "   फिर हुई चिंटू की जोरदार धुनाई। "

    if user_message in ("quiet", "shut up", "", "", "", "", ""):
        return "Ok i am on quiet mode now."

    if user_message in ("chup", "shant", "chup raho", "shant hojao", "", "", ""):
        return "Theek hai ab mein ni bolunga."

    if user_message in ("", "good morning", "gm", "", "", "", ""):
        return "Good morning sir/madam.."

    if user_message in ("", "ge", "good evening", "", "", "", ""):
        return "Good evening sir/madam.."

    if user_message in ("", "good afternoon", "gud afternoon", "", "", ""):
        return "Good afternoon sir/madam.."

    if user_message in ("", "can u help me", "can you do something", "", "", "", ""):
        return "Yes off course.."

    if user_message in ("be my best friend", "can u be my best friend", "friendship", "can we become good friends", "be a good friend", "be my friend"):
        return "Yey!! Buddies.."

    if user_message in ("good", "yup", "gud", "happy", "", "", ""):
        return "Yup!"

    if user_message in ("ok", "", "okay", "ook", "", "", ""):
        return "Ok"

    return "I don't understand what you want to know."
