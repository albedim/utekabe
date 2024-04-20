WELCOME_EMAIL = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Anek+Kannada:wght@100..800&family=Roboto:ital,wght@0,100;0,300;0,400;0,500;0,700;0,900;1,100;1,300;1,400;1,500;1,700;1,900&display=swap" rel="stylesheet">
    <title>Document</title>
    <style>
        .box{
            margin: 0;
            padding: 150px;
        }
        .boxer{
            padding: 24px;
            border: 1px solid #dadada;
            border-radius: 4px;
            display: flex;
            flex-direction: row;
            justify-content: space-around;
            background-color: rgb(245, 245, 245);;
        }
        .text{
            max-width: 540px;
            font-family: 'Roboto', sans-serif;
        }
        h2{
            font-size: 18px;
            font-weight: 400;
            color: #333;
        }
        .imagewr{
            display: flex;
            padding-bottom: 8px;
            border-bottom: 1px solid #bbbbbb;
            justify-content: space-around;
        }
        .buttonwr{
            display: flex;
            margin-top: 24px;
            justify-content: space-around;
        }
        .image{
            border-radius: 4px;
        }
        button{
            padding: 18px 32px;
            font-size: 14px;
            border: none;
            border-radius: 4px;
            background-color: rgb(255, 123, 0);
            color: white;
            font-family: 'Roboto', sans-serif;
            cursor: pointer;
        }
        p{
            font-family: 'Roboto', sans-serif;
        }
    </style>
</head>
<body class="box">
    <div class="boxer">
        <div>
            <div class="imagewr">
                <div style="align-items: center; display: flex;">
                    <img class="image" height="54px" width="54px" src="https://bliddofe.pages.dev/static/media/logo.800997bd8f7675755b0b.png" alt="">
                    <div style="margin-left: 14px;">
                        <p style="font-weight: 400;"><span style="font-weight: 500;">Bliddo</span><br>Auto e-mail service.</p>
                    </div>
                </div>
            </div>
            <div class="text">
                <h1>Bliddo</h1>
                <h2>Hey {name}! Welcome to Bliddo and thank you for joining us.<br/>We are going to help you create your digital library and sell your products to everyone, we can't wait to make you get your first sales and earn money with your passion! Get started now</h2>
            </div>
            <div class="buttonwr">
                <a href="{BASE_FE_URL}"><button style="cursor: pointer;">Get Started</button></a>
            </div>
            <div class="text" style="margin-top: 54px;">
                <p style="font-weight: 300; font-size: 11px;">This is an auto-generated e-mail, please don't respond to this.</p>
            </div>
        </div>
    </div>
</body>
</html>
'''

RECOVER_PASSWORD_EMAIL = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Anek+Kannada:wght@100..800&family=Roboto:ital,wght@0,100;0,300;0,400;0,500;0,700;0,900;1,100;1,300;1,400;1,500;1,700;1,900&display=swap" rel="stylesheet">
    <title>Document</title>
    <style>
        .box{
            margin: 0;
            padding: 150px;
        }
        .boxer{
            padding: 24px;
            border: 1px solid #dadada;
            border-radius: 4px;
            display: flex;
            flex-direction: row;
            justify-content: space-around;
            background-color: rgb(245, 245, 245);;
        }
        .text{
            max-width: 540px;
            font-family: 'Roboto', sans-serif;
        }
        h2{
            font-size: 18px;
            font-weight: 400;
            color: #333;
        }
        .imagewr{
            display: flex;
            padding-bottom: 8px;
            border-bottom: 1px solid #bbbbbb;
            justify-content: space-around;
        }
        .buttonwr{
            display: flex;
            margin-top: 24px;
            justify-content: space-around;
        }
        .image{
            border-radius: 4px;
        }
        button{
            padding: 18px 32px;
            font-size: 14px;
            border: none;
            border-radius: 4px;
            background-color: rgb(255, 123, 0);
            color: white;
            font-family: 'Roboto', sans-serif;
            cursor: pointer;
        }
        p{
            font-family: 'Roboto', sans-serif;
        }
    </style>
</head>
<body class="box">
    <div class="boxer">
        <div>
            <div class="imagewr">
                <div style="align-items: center; display: flex;">
                    <img class="image" height="54px" width="54px" src="https://bliddofe.pages.dev/static/media/logo.800997bd8f7675755b0b.png" alt="">
                    <div style="margin-left: 14px;">
                        <p style="font-weight: 400;"><span style="font-weight: 500;">Bliddo</span><br>Auto e-mail service.</p>
                    </div>
                </div>
            </div>
            <div class="text">
                <h1>Bliddo</h1>
                <h2>Hey {name}, we received a request to change your password.<br/>if you forgot your password please click this button and follow the steps in our website to recover your account, if the request wasn't made by you please ignore it.</h2>
            </div>
            <div class="buttonwr">
                <a href="{RECOVER_URL}"><button style="cursor: pointer;">Recover password</button></a>
            </div>
            <div class="text" style="margin-top: 54px;">
                <p style="font-weight: 300; font-size: 11px;">This is an auto-generated e-mail, please don't respond to this.</p>
            </div>
        </div>
    </div>
</body>
</html>
'''