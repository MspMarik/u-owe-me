def send_email():
    smtp_host = "email-smtp.us-east-1.amazonaws.com"
    smtp_port = 465
    sender_email = "etrostydev@gmail.com"
    receiver_email = ["eric.trostin@gmail.com"]
    password = "BCjURsGWOGJexIjhbbMSJjGah7J1KSt5jXpltAzfiLlL"
    username = "AKIAXBCLJP7K6AM4GXWZ"

    if store.lower() == "microcenter":
        stock = cd.find_element(By.XPATH, '//*[@id="pnlInventory"]/p').text
        global count
        # print(count)
        # x = re.findall("((?:|[0-2])[0-9](?:|\+) NEW IN STOCK)", stock)[0]

        html = f"""
            <html>
                <body>
                    <p>{prod} found in stock at {store}!<br><br>
                    Product: {prod}<br>
                    URL: {url}<br>
                    Stock: {count} currently in stock!
                    </p>
                </body>
            </html>
        """
    else:
        html = f"""
            <html>
                <body>
                    <p>{prod} found in stock at {store}!<br><br>
                    Product: {prod}<br>
                    URL: {url}
                    </p>
                </body>
            </html>
        """

    message = MIMEMultipart("alternative")
    message["Subject"] = f"{prod} found in stock at {store}!"
    message["From"] = sender_email
    message["To"] = ",".join(receiver_email)
    message.attach(MIMEText(html, "html"))
    message.attach(MIMEImage(open(screenshot, "rb").read()))

    context = ssl.create_default_context()

    # msg = f"**{prod} found in stock!!** \n\n" \
    #       f"URL: {url}"
    # test.send_message(msg)

    with smtplib.SMTP_SSL(smtp_host, smtp_port, context=context) as server:
        server.login(username, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
        server.quit()
    print("Email sent!")
    os.remove(screenshot)