import os
import smtplib
from email.message import EmailMessage

EMAIL_ADDRESS = "javosite@gmail.com"
EMAIL_PASS = os.environ.get("JAVO_PASS")

def sendEmail(to_address, subject, content):
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASS)

        msg = EmailMessage()
        msg["Subject"] = subject
        msg["From"] = EMAIL_ADDRESS
        msg["To"] = to_address
        msg.set_content(content)

        msg.add_alternative("""\
        <!DOCTYPE html>
        <html>
            <head>
                <style>
                    @import url('https://fonts.googleapis.com/css?family=Roboto&display=swap');
                    
                    * {
                        margin: 0;
                        padding: 0;
                    }
                    
                    body {
                        background-color: #efefef;
                    }
                    
                    .content-container {
                        position: fixed;
                        top: 50%;
                        left: 50%;
                        transform: translate(-50%, -50%);
                    }
                    
                    .logo {
                        display: flex;
                        margin: 0 auto 0 auto;
                    }
                    
                    h1 {
                        font-family: Roboto;
                        text-align: center;
                        color: #3f3f3f;
                    }
                    
                    h2 {
                        margin: 20px 0 20px 0;
                        font-family: Roboto;
                        text-align: center;
                    }
                    
                    h3 {
                        font-family: Roboto;
                        text-align: center;
                    }
                    
                </style>
            </head>
            <body>
                <div class="content-container" >
                    <img class="logo" src="static/Media/LogoDefault.png" height="100" width="100" />
                    <h1>Javo Support Team</h1>
                    <h2>MESSAGE</h2>
                    <h3>This message was automated <br> by Javo Support Team</h3>
                </div>
            </body>
        </html>
        """, subtype="html")

        smtp.send_message(msg)