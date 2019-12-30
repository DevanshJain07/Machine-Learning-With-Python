import webbrowser
    
a=input("enter your favourite movie")
    
if(a=="comedy"):
        webbrowser.open_new_tab("https://www.google.com/search?q=hero&oq=hero&aqs=chrome..69i57j0l5.2396j0j7&sourceid=chrome&ie=UTF-8")
elif(a=="romantic"):
        webbrowser.open_new_tab("https://www.youtube.com/watch?v=-KfsY-qwBS0")
elif(a=="action"):
        webbrowser.open_new_tab("https://www.youtube.com/watch?v=fxm4KcKDQl0")
else:
        webbrowser.open_new_tab("https://www.youtube.com/watch?v=mSlgu8AQAd4")

