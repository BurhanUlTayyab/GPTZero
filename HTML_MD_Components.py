
def noticeBoardMarkDown():
    return """
    # NoticeBoard
    We are currently working hard to develop SG-GPT version 2. Stay tuned for more updates. <br>
    <sub>27-Jan-2022</sub>
    """

def footerHTML():
    return """
    <div style="align-items: center; text_align: center; width:100%">
    <span style="color:red"><sub>Do you want to train Computer vision models faster. Visit [Ailiverse](https://ailiverse.com)</sub></span> <br>
    <p>Powered by Ailiverse</p> <br>
    <a href="https://github.com/BurhanUlTayyab/GPTZero">Code</a>
    <div>.</div> 
    <p>email here</p>
    </div>
    """

def bannerHTML():
    return """
<h4 style="text-align:center;border-radius: 25px;color:#FFFFFF;font-size:1.5em;padding:10px;background-image: linear-gradient(90deg, #20B2AA, #FFEBCD);border-style : solid; border-color : white; border-width: 1px">SG-GPTZero is a beta version. Please give us some feedback for further improvement.</h4>
    """
def emailHTML():
    return """
    <form action="/postdb" method="post" id="formPost">
        <input data-testid="textbox" name="email" type="email" class="scroll-hide block gr-box gr-input w-full gr-text-input" placeholder="Enter your email" autocomplete="email">
        <button class="gr-button gr-button-lg gr-button-secondary"  type="submit" form="formPost" id="email" style="margin-top:10px;">Send</button>
    </form>
    """

def googleAnalytics():
    return """
        <!-- Google tag (gtag.js) -->
        <script async src="https://www.googletagmanager.com/gtag/js?id=G-94REYHLBJM"></script>
        <script>
        window.dataLayer = window.dataLayer || [];
        function gtag(){dataLayer.push(arguments);}
        gtag('js', new Date());

        gtag('config', 'G-94REYHLBJM');
        </script>
    """