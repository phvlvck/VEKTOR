from pywebio import *
from pywebio.input import *
from pywebio.output import *
from pywebio import start_server
from pywebio import config

def app():
    put_image('https://images.app.goo.gl/rb1oHCY7F2a8jub36', width='900px', height='200px')

    put_html("""
    <!DOCTYPE html>
    <html>
    <head>
        <title></title>
        <style>
            body {
                background-color: black;
                color: white;
                font-family: monospace;
                margin: 0;
                padding: 0;
            }
            h1, h3, p, li, a {
                color: white;
            }
            .social-media {
                display: flex;
                justify-content: center;
            }
            .social-media a {
                color: white;
                text-decoration: none;
                margin: 0 10px;
            }
        </style>
    </head>
    <body>
        <h1>مرحباً بك في موقعي</h1>
        <p>18 ديسمبر 2023</p>
        <ul>
            <li>𝗠𝗬 𝗡𝗔𝗠𝗘:𝗔𝗵𝗺𝗲𝗱</li>
            <li>𝗠𝗬 𝗡𝗜𝗖𝗞𝗡𝗔𝗠𝗘:𝗕𝗶𝘀𝗼</li>
            <li>𝗠𝗠𝗬 𝗔𝗚𝗘:𝟭𝟱</li>
            <li>𝗘𝗩𝗘𝗡 𝗠𝗘, 𝗪𝗛𝗢 𝗨𝗦𝗘𝗗 𝗧𝗢 𝗠𝗔𝗞𝗘 𝗧𝗛𝗘𝗠 𝗙𝗘𝗘𝗟 𝗚𝗢𝗢𝗗, 𝗪𝗔𝗦𝗡'𝗧 𝗙𝗘𝗘𝗟𝗜𝗡𝗚 𝗪𝗘𝗟𝗟.</li>

        </ul>
        <details id='y'>
            <summary>
                ╰☆☆ 𝗦𝗼𝗰𝗶𝗮𝗹 𝗠𝗲𝗱𝗶𝗮☆☆╮
            </summary>
            <ul>
            
            <li>𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐦:@𝐈𝐒𝐒𝐅𝐈𝐈</li>
            
            
            <li>𝐈𝐧𝐬𝐭𝐚𝐠𝐫𝐚𝐦:@𝟒𝟒𝐣𝐣𝟒𝐣</li>
            
            
            <li>𝐏𝐔𝐁𝐆:𝟓𝟐𝟏𝟏𝟓𝟐𝟎𝟗𝟏𝟏</li>
            
            
            </ul>
            <details id='y'>
                    <summary>·.¸¸.·♩♪♫ music ♫♪♩·.¸¸.·</summary>
                    <p>اسم الاغنيه</p>
                    <audio controls>
                    <source src="https://h.top4top.io/m_3310dhiod0.m4a" type =" "audio/mp4">
                    </audio>
            <details>
                                <audio controls>
                    <source src="https://www.google.com/url?sa=t&source=web&rct=j&opi=89978449&url=https://www.youtube.com/watch%3Fv%3DgQoEoQEakIM&ved=2ahUKEwjivr6hxIyLAxUxygIHHS8eFxEQo7QBegQIFhAG&usg=AOvVaw1W8Q3IiN-eRkETxKdRaT5E" type =" "audio/mp4">
                    </audio>
            </details>
    """)

start_server(app, port=34345, debug=True)
